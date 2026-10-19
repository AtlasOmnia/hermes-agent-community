---
title: "Qwen 3.8 27B thinks itself into oblivion"
author: u/_bibolp_
date: 2026-10-19
score: 11
comments: 15
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x996ze/qwen_38_27b_thinks_itself_into_oblivion/
flair: "Help"
---

# Qwen 3.8 27B thinks itself into oblivion

**Posted by u/_bibolp_ on 2026-10-19 · 11 points (92% upvoted) · 15 comments**

Hi guys!
I think i have a pretty common local setup:
Hermes runs in Docker (on a separate machine) with a
Qwen 3.8 27B Q5_K_M
on an
NVIDIA 5090 (32GB)
.
It seems like the model thinks itself into oblivion. Simplest questions result in multiple long thinking sessions and most of it is just going through the same reasoning over and over.
I set the reasoning on low, but as far as I understand its a suggestion, not a rule.
Non-practical example, btu good demo:
Tell hermes to generate 100 puns - usually no problem.
Tell it to generate another 100 - it generates in thinking mode - fails/aborts, tries again and again and again.
Doing the same in Pi-Harness or in OpenCode works perfectly fine.
What are your experiences with it? Any way to fix it?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x996ze/qwen_38_27b_thinks_itself_into_oblivion/)
