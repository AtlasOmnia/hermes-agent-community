---
title: "I layered JEV into the skill and tool selection in my Hermes"
author: u/MediamanJack
date: 2026-09-25
score: 29
comments: 12
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wp4wkn/i_layered_jev_into_the_skill_and_tool_selection/
flair: "Showcase — Projects, tools, builds, demos"
---

# I layered JEV into the skill and tool selection in my Hermes

**Posted by u/MediamanJack on 2026-09-25 · 29 points (93% upvoted) · 12 comments**

Recently I was beginning to notice that my Hermes was not reliably selecting tools or skills to use when I prompt it with a task. Now, I know that there are plenty of other methods to solve this, but the timing of this was aligned almost perfectly with news of JEV. So after seeing what JEV was capable of and how it responded I realized that this could be a perfect use case, which of course it is already! A cookbook from the creators of JEV is already available.
https://docs.typesafe.ai/cookbooks/skill_suggestion
Anyways, I walked through the design with Hermes and came up with a plan, but there was one tweak that I made based on one issue, what about prompts that should be multi-skilled? And honestly, so much more than just simply that.
So to summarize what was changed, here's my Hermes with a write up:
The TypeSafe cookbook suggests skills with two API calls: a quick skim to shortlist, then a second call to verify the winner against full descriptions. We replaced that with one call that returns Jev's pick plus a probability score for every skill at once, injected into the AI's context before it even sees your message — through a memory-provider hook that works on every surface (desktop, Telegram, cron), with each profile only ever seeing its own authorized skill menu.
Since every skill arrives with a probability, we also hint two skills when a prompt clearly needs both — "check my servers and save the report to Obsidian" now hints the server tool and the note-taking tool — but only when Jev is actually confident; if it says "none," the router stays silent. We tested three versions against a stratified test corpus: cookbook-style single hint scored 74%, unconditional two-hint scored worse (72% — it leaked suggestions on restricted profiles), and our final confident-picks-only version scored 79%.
Crucially, the router hints but never specifies: the suggestion arrives as one advisory line the AI is free to ignore, and the full skill catalog stays available regardless — if the whisper is wrong, nothing breaks, the AI just picks the right skill itself. That advisory-only stance runs through the whole design: a local privacy filter checks every message first, so anything password-shaped never leaves the machine at all, and a Jev outage just means "no hint" — never a blocked turn. Total cost per call: about $0.00002.
So far, so good! I'll update as I play around with the new setup.
Let me know if there is something I missed or something I should consider changing! I'm not having fun!
EDIT: if you are needing access to JEV, I use OpenRouter, from what I can tell it's publicly available there.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wp4wkn/i_layered_jev_into_the_skill_and_tool_selection/)
