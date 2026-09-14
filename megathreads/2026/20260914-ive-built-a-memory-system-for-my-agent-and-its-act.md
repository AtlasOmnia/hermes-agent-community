---
title: "I've built a memory system for my agent and it's actually working"
author: u/AxelFooley
date: 2026-09-14
score: 42
comments: 31
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wf2agm/ive_built_a_memory_system_for_my_agent_and_its/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# I've built a memory system for my agent and it's actually working

**Posted by u/AxelFooley on 2026-09-14 · 42 points (86% upvoted) · 31 comments**

We all know the struggle, constantly having to reiterate stuff to our agent because it doesn't remember stuff.
I've been interested in memory management for LLMs for quite a while, and i have built a system i've been using for a long time now, fixing and fine tuning quirks along the way. The other day i realised i haven't been chasing small bugs since a while which made me thinking that the system is mature enough for every day usage.
Here i am sharing it with you, i am not looking for money :D i am looking for feedbacks, and PRs for improving it.
It's called MnemoBrain, at its core it's based out of Mnemosyne and Gbrain, what i did was building some scaffolding to put together at work the way i wanted, and more importantly, it just works without me having to explicitly say "search your memory" or "remember that".
I've found that the key to make this logic work isn't to write a prompt for the agent, it will consistently fail that's guaranteed. Today's agentic harnesses offer hooks, those are independent from the model and don't rely on the model to "decide" to remember things, it just searches for the relevant context (via semantic search) and injects it in the context.
The whole architecture is described in the repo, have a look try it if you fancy, feedbacks welcome. PRs even more welcome if you want to contribute.
https://github.com/AxelFooley/MnemoBrain

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wf2agm/ive_built_a_memory_system_for_my_agent_and_its/)
