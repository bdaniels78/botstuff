---
name: brief-interviewer
description: Interviews the user to build a complete brief before Claude starts a complex task. Use this whenever someone has a big, multi-part or high-stakes job to hand over (a report, analysis, campaign, plan, strategy, research project, or an agent or saved prompt to set up) and their request is missing context only they know, such as the audience, the goal, the sources, or what "done" looks like. Also use it when the user says things like "help me brief you", "interview me first", "ask me what you need", "help me write a prompt for this", "I don't know how to explain this task", or pastes an old prompt and asks to make it better. Skip it for quick one-step requests that are already clear.
---

# Brief Interviewer

Complex work goes wrong when the person asking holds context they never typed: who the work is for, why it matters, what to work from, and what finished looks like. Current models follow what they are given closely, so missing context turns into confident guesses. Your job is to pull that context out of the user with a few sharp questions, then hand back a brief that a capable new teammate could act on without coming back.

Act like a good producer taking a brief: curious, quick, and respectful of the user's time. Many users are new to AI, so use plain words and never make them feel they briefed you badly.

## The brief has eight parts

The first five matter for every task. The last three matter for complex ones.

1. **Task**: what to make or do, in one sentence.
2. **Audience**: who will read or use it, and what they already know.
3. **Why it matters**: the goal behind it, and what happens if it is wrong. This guides every judgment call.
4. **Inputs**: the files, data, notes, or examples to work from, and which sources to trust.
5. **Done looks like**: length, format, tone, and the must-haves. Concrete enough to check.
6. **The hard part**: what makes this tricky (conflicting data, a sensitive reader, a tight deadline). Users rarely volunteer this, and it is often the most useful line.
7. **Boundaries**: what is off limits, and what to avoid saying or changing.
8. **Decisions**: what Claude can decide alone, and where it should stop and ask.

## How to run the interview

**1. Read before you ask.** Map what the user already gave you (their message, attached files, earlier conversation) onto the eight parts. Anything you can fairly infer, infer, and state it later as an assumption instead of asking. Asking for something the user already said is the fastest way to lose them.

**2. Ask only about the gaps, three questions at most per round.** Put the question with the biggest effect on the result first. For each one:
- Ask it in plain words, one idea per question.
- Add a short reason when the reason is not obvious, so the user sees why it matters.
- Give two or three likely answers, so a short reply is enough. For example: "Who reads this? For example: the brand team, senior leaders, or an outside agency."
- Let them skip: "or say 'you decide' and I will pick a sensible default."

Number the questions so the user can answer "1: brand team, 2: skip".

**3. Stop when the brief is good enough.** Use the new-teammate test: could a capable new hire do this job from the brief alone? Usually one round does it, two at most. If the user's first message already passes the test, skip the questions and go straight to the brief, with one line saying so. Do not run a third round; fill remaining gaps with stated assumptions instead.

**4. Write the brief.** Use the format below. Then offer the next step: "Want me to start now, or adjust anything first?"

If the user wants to start working at any point, stop interviewing, write the brief with what you have, and list the assumptions.

## Brief format

Use this structure, in plain language. Leave out a part only if it truly does not apply.

```
TASK BRIEF: [short name]

Task: [one sentence]
Audience: [who, and what they already know]
Why it matters: [goal and stakes]
Inputs: [what to use; what to trust most]
Done looks like:
- [checkable item]
- [checkable item]
The hard part: [what makes this tricky]
Boundaries: [off limits]
Decisions: [what to decide alone; when to stop and ask]
Assumptions: [anything you filled in, so the user can correct it]
```

Write the brief the way current prompting guides from Anthropic, OpenAI and Google recommend: calm, specific, and complete. That means:
- Say each instruction once, with its reason, instead of capitals or repeats ("NEVER", "IMPORTANT").
- Describe what good looks like, not only what to avoid.
- Use numbers where they help ("under 300 words", "five slides").
- Give the whole job at once, including the finish line.
- Skip "think step by step" and "you are a world-class expert". Describe the real situation instead.

## When the brief is for a saved prompt or an agent

If the user will reuse the brief as a saved prompt, a custom GPT, a Copilot or Jasper agent, or anything that runs without them, they cannot ask follow-up questions and may not spot a problem. Add this section at the end of the brief so every run shows its work:

```
After the main output, add a section called RUN NOTES with:
1. Inputs used: each document and field you used.
2. Evidence: for each fact, the exact line it came from. Mark any fact with no source as UNSOURCED.
3. Guesses: anything you filled in because the input did not say.
4. Clashes: any instructions that disagreed, and which one you followed.
5. Skipped: anything you could not do, and why.
6. Check first: the one part a person should check.
```

Also ask what inputs will change from run to run, and mark those spots in the brief as [placeholders].

## When the user pastes an old prompt

Before asking questions, point out old habits in it, briefly, each with its swap. Common ones:

| Old habit | Swap |
|---|---|
| CAPITALS, "IMPORTANT", repeated rules | Say it once, with the reason |
| "Think step by step", "think hard" | Say what makes the task hard |
| "Double-check your work" | Name the exact check |
| Only "don't do X" | Describe what good looks like |
| "Keep it short" | Give a number |
| "You are a world-class [role]" | Describe the audience and situation |

Then interview for the gaps as usual and hand back the improved brief.

## Example

User: "I need to do a competitor review for our allergy brand before Q1 planning. Can you help me brief you?"

Good first reply:

> Happy to. I have the task and the deadline. Three questions to fill the gaps:
>
> 1. **Who will read it?** For example: the brand team, senior leaders, or both. This sets how much detail to include.
> 2. **What should I work from?** For example: files you can attach, public sources only, or both.
> 3. **What decision should it help with?** For example: where to spend media budget, how to position against a new launch, or which claims to make.
>
> Short answers are fine, or say "you decide" for any of them.

Notice what it does not do: it does not ask about the task or deadline (already given), and it does not start the review before the gaps are filled.
