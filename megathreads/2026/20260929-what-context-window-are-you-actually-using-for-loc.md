---
title: "What context window are you actually using for local models?"
author: u/firejava
date: 2026-09-29
score: 5
comments: 35
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wsjdfy/what_context_window_are_you_actually_using_for/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# What context window are you actually using for local models?

**Posted by u/firejava on 2026-09-29 · 5 points (85% upvoted) · 35 comments**

For those of you running local models as agents or daily drivers, what context window are you actually finding practical?
I'm currently using cloud APIs through Nous, OpenRouter, OpenAI, and Anthropic, but I'd like to move one or two of my agent profiles over to local models.
I had been thinking
64K context was my minimum
since that is requirement for hermes, but I started looking more closely at my actual usage last night. My cloud-based profiles seem to blow past 64K pretty quickly once you include conversation history, system prompts, tool calls, memory/context injection, etc.
So now I'm wondering whether I should really be targeting
96K, 128K, or even higher
for a local model.
For people actually running local LLMs long-term:
What context size do you normally run?
Is 64K enough for an agent that stays active for a while?
Are you running 96K/128K+?
At what point do performance, VRAM/RAM usage, or model quality start becoming a problem?
Do you rely on context pruning/summarization instead of just increasing the context window?
I'm especially interested in experiences with local models being used as agents, rather than just one-off chat or coding prompts.
I'm trying to figure out what context size I should realistically design around before buying more hardware.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wsjdfy/what_context_window_are_you_actually_using_for/)
