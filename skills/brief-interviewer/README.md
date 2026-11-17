# Brief Interviewer

**[Download the skill for Claude](https://github.com/bdaniels78/botstuff/raw/claude/dreamy-wright-a9hv5k/skills/brief-interviewer.skill)** · [Copy the version for other AI tools](brief-interviewer-instructions.txt)

A Claude skill for people handing a complex task to AI. Instead of guessing, Claude asks you for the context only you know, then writes a complete brief.

## What it does

1. Reads what you already gave it, and never asks for that again.
2. Asks only about the gaps in the five parts of a good brief: the goal, who it's for, what done looks like, the material, and the rules. Three questions at most, each with example answers. You can say "you decide".
3. Hands back a brief you can use straight away or save, ending with a line that asks the AI to briefly explain its main choices, so you can check the work.
4. Points out old prompting habits when you paste in an old prompt, and suggests the swap.

If your request already covers everything, it skips the questions.

## Install

No GitHub account needed.

- **Claude:** [download brief-interviewer.skill](https://github.com/bdaniels78/botstuff/raw/claude/dreamy-wright-a9hv5k/skills/brief-interviewer.skill), then add it under Settings > Capabilities > Skills.
- **ChatGPT, Copilot, Jasper or Gemini:** open [brief-interviewer-instructions.txt](brief-interviewer-instructions.txt), copy the text, and paste it into the instructions of a custom GPT, agent, app or Gem.

## Try it

> I need to put together a competitive review before Q1 planning. Help me brief you properly before we start.

Companion guide: The Prompt Brief, a field guide to briefing the newest AI models. Based on prompting guidance from Anthropic, OpenAI and Google.
