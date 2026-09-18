---
title: "Self-taught, 2 months into Hermes Agent"
author: u/Erraticeuphoria
date: 2026-09-18
score: 23
comments: 18
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wiv4hp/selftaught_2_months_into_hermes_agent/
flair: "Workflow — Daily habits, multi-agent setups, best practices"
---

# Self-taught, 2 months into Hermes Agent

**Posted by u/Erraticeuphoria on 2026-09-18 · 23 points (84% upvoted) · 18 comments**

TLDR: Self-taught, 2 months into Hermes Agent: Struggling with agent delegation, hallucinated handoffs, and memory. Looking for best practices / advanced guides.
Hey everyone,
I wanted to share my journey and ask for some advice from people who are further along with Hermes Agent.
To give you some background: I'm completely self-taught with no formal IT background, just someone who loves tinkering with tech. I’ve been experimenting with Hermes Agent for the last 2 months, learning from YouTube and just breaking/fixing things on my own. I started with a single agent, and now I've scaled up to managing a team of 5 agents.
However, I feel like my approach or setup might be fundamentally flawed or suboptimal because I'm running into some frustrating bottlenecks now that I'm trying to incorporate Hermes into my daily workflow.
I'm hoping to get your input on a few specific pain points:
Delegation & "Ghost" Handoffs
My initial goal was to set up a hierarchical structure—ideally having a "lead" agent where I can just talk to it directly, and it would cleanly delegate tasks down to the specialized worker agents.
* The Problem: Instead of properly delegating, the lead agent will often just do the work itself by spawning sub-agents, while claiming or hallucinating that it handed the task off to the designated worker. When I check the worker agent, it has zero clue that a task was ever assigned to it. Inter-agent messaging still feels very hit-or-miss.
2. Memory and Context
* The Problem: Session-to-session memory and context handling have been pretty disappointing. I know context window and memory management are universal headaches, but I have a strong feeling my setup or prompt configuration might be making it worse. So far I've been using built in memory and honcho. Haven't started using obsidian as knowledge base.
3. Moving Past the Basics
Most YouTube tutorials and resources focus heavily on basic installation (setting up a VPS, creating users, and configuring soul.md), which I've already got down.
* What I need now: I want to level up my game. Are there any best practices, advanced guides, or frameworks for structuring a multi-agent team from scratch? I’ve heard about things like LangChain, but I honestly haven’t had the time to dive deep into them yet.
If anyone has found specific architectural blueprints, organizational hierarchies, or day-to-day workflow patterns that actually make Hermes reliable for production/daily use, I would love to hear your recommendations or see resources you found genuinely useful.
Thanks in advance!

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wiv4hp/selftaught_2_months_into_hermes_agent/)
