---
title: "Turns out the real Qwen benchmark is whether it can pay for its own GPU. Running my Qwen 3.8 27B trading agent live 24/7."
author: u/artguerilla
date: 2026-09-21
score: 40
comments: 38
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wlkn3v/turns_out_the_real_qwen_benchmark_is_whether_it/
flair: "Showcase — Projects, tools, builds, demos"
---

# Turns out the real Qwen benchmark is whether it can pay for its own GPU. Running my Qwen 3.8 27B trading agent live 24/7.

**Posted by u/artguerilla on 2026-09-21 · 40 points (90% upvoted) · 38 comments**

So yeah, this may be a terrible idea.
I’ve been building an autonomous trading setup around
Hermes + Qwen 3.8 27B
.
It watches the market, opens trades, manages positions, reviews its own trades, and keeps adjusting the strategy based on what actually happened.
Naturally the logical next step was:
leave it running 24/7 until I’m rich.
Or until the AI discovers a sufficiently advanced method of losing money.
The stream is basically the opposite of polished AI demo content. No cinematic “AI is changing EVERYTHING” voiceover, no fake terminal animation, no guy pointing at a graph with his mouth open.
Just the actual system running.
You can watch:
what the agent is thinking / doing
trades opening and closing
strategy changes
occasional questionable decisions
me finding bugs I absolutely should have found before going live
Current stack is roughly
Hermes as the agent harness + Qwen 3.8 27B + our trading/data tooling
. We’re also experimenting with different time horizons, market/event detection and letting the system analyze its own trading history rather than just blindly hammering one strategy forever.
Stream stays online 24/7.
Either we slowly build a decent autonomous trader, or this becomes an extremely elaborate screensaver.
Both outcomes are acceptable.
Twitch: aimademedoit
Not financial advice. Probably not even artificial financial advice.
I'm not familiar with trading whatsoever, but go ahead and ask me anything 😅

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wlkn3v/turns_out_the_real_qwen_benchmark_is_whether_it/)
