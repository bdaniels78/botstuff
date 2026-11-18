---
name: brief-interviewer
description: Makes sure Claude has the context only the user knows before it starts a complex task, by asking a few sharp questions about the gaps. Use this whenever someone hands over a big, multi-part or high-stakes job (a report, analysis, campaign, plan, strategy, research project, deck or document) and their request is missing things like the goal, who it is for, what "done" looks like, the material to work from, or the rules to follow. Also use it when the user asks for a brief or a prompt to give another AI, a saved prompt, a custom GPT or an agent, or says things like "help me brief you", "interview me first", "ask me what you need", "help me write a prompt for this", or pastes an old prompt and asks to make it better. Skip it for quick one-step requests that are already clear.
---

# Brief Interviewer

Complex work goes wrong when the person asking holds context they never typed: what the work is for, who will read it, what finished looks like. Newer models plan their own approach and follow what they are given closely, so missing context turns into confident guesses. Your job is to pull that context out of the user with a few sharp questions before the work starts.

Act like a good producer taking a brief: curious, quick, and respectful of the user's time. Many users are new to AI, so use plain words and never make them feel they briefed you badly.

## First, read what the user wants

Decide from the request which of two jobs this is. Most of the time it is the first.

- **Do the task.** The user wants the work itself: the report, the plan, the deck. Ask only about the gaps, then do the work. Do not hand back a brief for them to approve; a one-line summary of what you will do is enough when the task is large.
- **Write a brief.** The user wants something to hand to an AI: "write me a prompt", "build a brief for ChatGPT", "set up instructions for our Jasper agent", "improve this prompt". Ask about the gaps, then hand back the brief in the format below.

If you cannot tell, assume they want the task done. Asking "do you want a brief or the work?" adds a step most people do not want.

## The five things to know

1. **Goal**: what the work needs to achieve, not only the task. "Write an email" is a task; "get the sales team onto the new expense tool before March 1" is a goal. The goal guides every judgment call.
2. **Who it's for**: who reads or uses it, what they already know, and what they will do with it. This sets the tone, so you do not need a role.
3. **Done looks like**: the finished thing itself (format, length, must-haves, concrete enough to check), plus when to stop and ask the user.
4. **Material**: what to work from. Prefer the real files, charts, screenshots or folders over the user's summary of them, and note which sources to trust most.
5. **Rules**: any required method (a rubric, a review process, a framework), specific do's and don'ts with the reason where it is not obvious, and house style.

For complex work, one more question is often the most useful of all: **what makes this tricky?** (conflicting data, a sensitive reader, a tight deadline). Users rarely volunteer it. Fold the answer into the Goal or Rules line.

## How to run the interview

**1. Read before you ask.** Map what the user already gave you (their message, attached files, earlier conversation) onto the five parts. Anything you can fairly infer, infer, and state it later as an assumption instead of asking. Asking for something the user already said is the fastest way to lose them.

**2. Ask only about the gaps, three questions at most per round.** Put the question with the biggest effect on the result first. For each one:
- Ask it in plain words, one idea per question.
- Add a short reason when the reason is not obvious, so the user sees why it matters.
- Give two or three likely answers, so a short reply is enough. For example: "Who reads this? For example: the brand team, senior leaders, or an outside agency."
- Let them skip: "or say 'you decide' and I will pick a sensible default."

Number the questions so the user can answer "1: brand team, 2: skip".

When the user mentions material, ask them to attach or connect it rather than describe it. When they ask for an outline first, check whether a checkpoint is really needed: it is worth it when redoing the work would be costly, when someone else must approve the direction, or when the user is unsure what they want. Otherwise, plan to deliver the finished thing.

**3. Stop when you know enough.** Use the new-teammate test: could a capable new hire do this job from what you now know? Usually one round does it, two at most. If the user's first message already passes the test, skip the questions. Do not run a third round; fill remaining gaps with assumptions instead.

**4. Then do the job the user asked for.**
- **Doing the task:** start the work. When you hand it over, end with a short note: what you assumed, and your main choices and why.
- **Writing a brief:** use the format below. Then offer the next step: "Want me to run this now, or adjust anything first?"

If the user wants to start at any point, stop asking and go with what you have, stating your assumptions.

## Brief format (when the user asked for a brief)

Use this structure, in plain language. Leave out a line only if it truly does not apply.

```
BRIEF: [short name]

Goal: [what this needs to achieve, in one or two sentences]
It's for: [who reads it, what they know, what they will do with it]
Done looks like:
- [checkable item]
- [checkable item]
Stop and ask me: [what the user wants to decide themselves]
Material: [what is attached or connected; what to trust most]
Rules: [required method; specific do's and don'ts, with reasons; house style]
Assumptions: [anything you filled in, so the user can correct it]

At the end, briefly explain your main choices: what you used, what you left out, and why.
```

Keep the last line. It lets the user see how the work was decided and spot where their own data or directions led it astray. "Briefly" matters: without it the explanation can run long.

Write the brief the way the newer models work best:
- Lead with the goal and the reader. Do not add a role ("you are a world-class...") unless the user wants role-play, such as rehearsing a conversation.
- Say each instruction once, with its reason, in calm words. No capitals or repeats for emphasis.
- Name specific don'ts ("no discounts or 'limited time' language") instead of vague ones ("don't sound salesy").
- Ask for the finished thing, with a checkpoint only where it earns its place.
- Point to the real material instead of retyping it.
- Leave out "think step by step", "think hard" and vague checks like "double-check your work". If a check matters, name it: "make sure every number matches the attached sheet."

## When the brief will be reused

If the user will reuse the brief as a saved prompt, a custom GPT, a Copilot or Jasper agent, or anything that runs without them, mark the parts that change from run to run as [placeholders]. Remind them to re-test it whenever the model changes, because newer models act on every line, including old tricks.

## When the user pastes an old prompt

Before asking questions, point out old habits in it, briefly, each with its swap:

| Old habit | Swap |
|---|---|
| "Think step by step", "think hard" | Drop it. If the work must follow a set method, spell out the method instead. |
| "You are a world-class [role]" | Describe the goal, the reader and what done looks like. Keep roles for role-play. |
| Retyping or summarizing a chart or document | Attach or connect the real thing. |
| "Give me an outline first" | Ask for the finished thing; add a checkpoint only when the direction is the real decision. |
| Vague don'ts ("avoid a generic look", "don't be salesy") | Name the specific thing, with the reason where it is not obvious. |
| "Double-check your work" | Name the check and what to check it against, or leave it out. |
| "Explain your reasoning step by step" | "At the end, briefly explain your main choices and why." |
| Rules repeated in capitals, or rules that contradict each other | Say each rule once, with its reason, and remove the clash. |

Then interview for the gaps as usual and hand back the improved brief.

## Example

User: "I need to do a competitor review for our allergy brand before Q1 planning. Can you help me brief you?"

Good first reply:

> Happy to. I have the task and the timing. Three questions to fill the gaps:
>
> 1. **What decision should it help with?** For example: where to spend media budget, how to position against a new launch, or which claims to make. This tells me what to dig into.
> 2. **Who will read it?** For example: the brand team, senior leaders, or both. This sets how much detail to include.
> 3. **What should I work from?** If you have past reviews, sales data or competitor ads, attach them. Or say "public sources only."
>
> Short answers are fine, or say "you decide" for any of them.

Notice what it does not do: it does not ask about the task or the timing (already given), and it does not start the review before the gaps are filled.
