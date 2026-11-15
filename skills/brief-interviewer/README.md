# Brief Interviewer

A Claude skill for people who need to hand a complex task to AI. Instead of guessing, Claude interviews you for the context only you know, then writes a complete brief.

## What it does

1. Reads what you already gave it, and never asks for that again.
2. Asks only about the gaps: three questions at most, each with example answers. You can say "you decide".
3. Hands back a task brief: task, audience, why it matters, inputs, what done looks like, the hard part, boundaries, decisions and assumptions.
4. Adds "run notes" when the brief is for a saved prompt or agent, so every run shows its work.
5. Flags old prompting habits when you paste in an old prompt.

If your request already covers everything, it skips the questions.

## Install

- **Claude:** download `brief-interviewer.skill` and add it under Settings > Capabilities > Skills, or copy this folder into your skills folder.
- **ChatGPT, Copilot, Jasper or Gemini:** paste `brief-interviewer-instructions.txt` into a custom GPT, agent, app or Gem.

## Try it

> I need to put together a competitive review before Q1 planning. Help me brief you properly before we start.

Based on prompting guidance from Anthropic, OpenAI and Google.
