"""One-time login.

  python -m spotify.auth url <CLIENT_ID>      # prints the login link
  python -m spotify.auth code <REDIRECT_URL>  # saves the refresh token
"""
import sys
from . import client

if __name__ == "__main__":
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "url":
        print(client.authorize_url(arg))
    elif cmd == "code":
        client.exchange_code(arg)
        me = client.call("GET", "/me")
        print("Logged in as", me.get("display_name") or me.get("id"))
