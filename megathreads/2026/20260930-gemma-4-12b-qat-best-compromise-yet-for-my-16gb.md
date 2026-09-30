---
title: "Gemma 4 12B QAT : best compromise yet for my 16gb"
author: u/CycleNo3036
date: 2026-09-30
score: 10
comments: 25
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wtd84a/gemma_4_12b_qat_best_compromise_yet_for_my_16gb/
flair: "MODELS - model choice, routing, pricing, local vs cloud, VRAM"
---

# Gemma 4 12B QAT : best compromise yet for my 16gb

**Posted by u/CycleNo3036 on 2026-09-30 · 10 points (91% upvoted) · 25 comments**

Hey everyone, I'm new to using hermes and in the past few days i've tested various local models to use as a brain for hermes.
My hardware (4060ti with 16gb of vram) can comfortably run Qwen 3.8 27B (the quantized versions from ISTA-DASlab) when it comes to just Q&A in LMstudio. It's actually a very impressive model for the size, as many people have noted.
However, hermes requires a minimum 64k context window to work, and this is where i struggle with this model as its speed gets down to 6 t/s (full gpu load not possible).
A good alternative i've found is Gemma 4 12B QAT. It still has some very decent coding capabilities and is much faster on my card at around 31 t/s (full gpu load possible).
Since i can obviously not test every model out there, i was wondering if some of you found other good all-rounder alternatives for the same hardware range ?
Thanks in advance for answers.
EDIT :
I've tried three recommendations in the comments, here's what i've concluded :
Gemma-4-26B-A4B-QAT is indeed faster than gemma-4-12B-QAT at same context window (i get around 40 t/s). From what i've tested so far, it looks similar in terms of coding capabilities. But I see no point of keeping the 12B.
Qwen-3.6-35B-A3B is MUCH faster than Qwen-3.8-27B (i get 36 t/s). However, it seems to me that there is a significant downgrade in coding capabilities compared to qwen 3.8. It's closer to the gemma models.
Qwen-3.8-27B (Unsloth IQ3S quantization) doesn't really improve anything for me. It runs at 6 t/s for a 64k context window, so roughly the same as i got with the ISTA quantization. Still the best in terms of coding/reasoning. Just too slow for me for hermes. Maybe it's my graphics card bandwidth idk.
So, yeah. I would defo change my title to Gemma 4 26B A4B now ^^

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wtd84a/gemma_4_12b_qat_best_compromise_yet_for_my_16gb/)
