---
title: "Local AI on 5070ti is killing me."
author: u/Previous-Ad-5371
date: 2026-09-23
score: 7
comments: 34
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wn5th2/local_ai_on_5070ti_is_killing_me/
flair: "MODELS - model choice, routing, pricing, local vs cloud, VRAM"
---

# Local AI on 5070ti is killing me.

**Posted by u/Previous-Ad-5371 on 2026-09-23 · 7 points (66% upvoted) · 34 comments**

Hello!
I am pretty new to hosting LLMs locally. I have been trying different models and found that Qwen3.6 35B (Q5) with the context set to around 210,000 seems to work really well when I need Hermes to sort out network tasks and other things I want help with.
But—and people are probably laughing at me now—I'm running it through LM Studio on my RTX 5070 Ti 16GB and offloading to system RAM. Let's just say it's not the fastest setup. Honestly, it's killing me. Prompt processing is a slog, and my tokens per second jump anywhere from 1 to 14 tok/s (let's be real, it's mostly stuck at 1-2).
Adding more GPUs is out of the question since prices are way too high for a hobby, which leaves the cloud-provider route.
Where do I go from here, and what should I try first? I'm worried that "pay-as-you-go" services could become super expensive unless I just sit around doing nothing due to throttling. Help! :)

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wn5th2/local_ai_on_5070ti_is_killing_me/)
