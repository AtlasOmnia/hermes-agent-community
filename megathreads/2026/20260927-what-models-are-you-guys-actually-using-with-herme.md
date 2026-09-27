---
title: "What models are you guys actually using with Hermes? I’ve had some surprising results"
author: u/Severe-Cap1333
date: 2026-09-27
score: 24
comments: 54
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wr5jka/what_models_are_you_guys_actually_using_with/
flair: "MODELS - model choice, routing, pricing, local vs cloud, VRAM"
---

# What models are you guys actually using with Hermes? I’ve had some surprising results

**Posted by u/Severe-Cap1333 on 2026-09-27 · 24 points (96% upvoted) · 54 comments**

Been using Hermes pretty heavily for the last few weeks and I’ve ended up building a pretty big setup around it. Multiple agents, cron jobs, delegation, background stuff, etc.
I also managed to burn through $1,500+ on OpenRouter in under 4 weeks 😅
I started mostly with DeepSeek, then moved to Sonnet and recently started testing the GPT-6 models because I wanted to cut costs.
What surprised me is that I actually liked Sonnet more than Luna.
On paper Luna looked really interesting because it’s so much cheaper, but in my actual Hermes usage I felt like Sonnet was more reliable for some of the deeper reasoning / agent stuff I throw at it. Luna had some moments where I just didn’t trust what it was doing.
So right now I’m probably going back to Sonnet as the main model, with Opus for the really difficult stuff. Quality and Performance matters the most for me.
But I’m curious what other Hermes users are doing.
What are you guys using for:
main/default agent
coding
research / fact checking
long agent tasks
subagents
cron/background jobs
And has anyone got a good automatic model routing setup working? Something like cheap model for normal tasks → stronger model when things get difficult.
Mostly looking for real-world Hermes experience, not benchmark results. I’m sure models behave differently once they’re actually inside an agent loop.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wr5jka/what_models_are_you_guys_actually_using_with/)
