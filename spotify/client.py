"""Minimal Spotify Web API client.

The app's Client ID/Secret are injected by the environment's network proxy as
Basic auth on requests to accounts.spotify.com, so no secret lives in code.
The user's refresh token is kept in .spotify_token.json (gitignored).
"""
import base64
import json
import pathlib
import time
import urllib.parse
import urllib.request

TOKEN_FILE = pathlib.Path(__file__).resolve().parent.parent / ".spotify_token.json"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API = "https://api.spotify.com/v1"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPES = " ".join([
    "user-read-playback-state", "user-modify-playback-state",
    "user-read-currently-playing", "user-read-recently-played", "user-top-read",
    "playlist-read-private", "playlist-modify-private", "playlist-modify-public",
    "user-library-read", "user-library-modify",
])
# Placeholder header; the proxy overwrites it with the real Client ID/Secret.
_PLACEHOLDER_BASIC = "Basic " + base64.b64encode(b"proxy:injected").decode()


def _post_token(data: dict) -> dict:
    req = urllib.request.Request(
        TOKEN_URL,
        data=urllib.parse.urlencode(data).encode(),
        headers={"Authorization": _PLACEHOLDER_BASIC,
                 "Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def authorize_url(client_id: str) -> str:
    return "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode({
        "client_id": client_id, "response_type": "code",
        "redirect_uri": REDIRECT_URI, "scope": SCOPES,
    })


def exchange_code(redirect_url_or_code: str) -> None:
    code = redirect_url_or_code
    if "code=" in code:
        code = urllib.parse.parse_qs(urllib.parse.urlparse(code).query)["code"][0]
    tok = _post_token({"grant_type": "authorization_code", "code": code,
                       "redirect_uri": REDIRECT_URI})
    _save(tok)


def _save(tok: dict) -> None:
    old = json.loads(TOKEN_FILE.read_text()) if TOKEN_FILE.exists() else {}
    tok["refresh_token"] = tok.get("refresh_token") or old.get("refresh_token")
    tok["expires_at"] = time.time() + tok["expires_in"] - 60
    TOKEN_FILE.write_text(json.dumps(tok))
    TOKEN_FILE.chmod(0o600)


def access_token() -> str:
    tok = json.loads(TOKEN_FILE.read_text())
    if time.time() >= tok["expires_at"]:
        _save(_post_token({"grant_type": "refresh_token",
                           "refresh_token": tok["refresh_token"]}))
        tok = json.loads(TOKEN_FILE.read_text())
    return tok["access_token"]


def call(method: str, path: str, body=None, **params):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(
        url, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": "Bearer " + access_token(),
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        raw = r.read()
        return json.loads(raw) if raw else None
