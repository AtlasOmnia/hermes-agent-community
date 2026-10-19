---
title: "Ling-3.1-flash goes open source, with Hermes Agent named in the model card"
author: u/Automatic-Praline578
date: 2026-10-19
score: 7
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x924i6/ling31flash_goes_open_source_with_hermes_agent/
flair: "Models"
---

# Ling-3.1-flash goes open source, with Hermes Agent named in the model card

**Posted by u/Automatic-Praline578 on 2026-10-19 · 7 points (100% upvoted) · 0 comments**

The Ling-3.1-flash model card explicitly includes Hermes Agent among the frameworks in which the model performs well, and the weights have now been released under MIT.
For choosing where it belongs in an agent stack, the release gives a few concrete inputs: a 1M-token model context, native reasoning on/off, and an Artificial Analysis launch snapshot around 210 output tokens/s with a blended price near $0.19 per million tokens.
The documented API lets an application set the reasoning mode per request. That makes the distinction between a routine tool step and a deeper planning step an explicit model-setting decision. Open weights and SGLang/vLLM serving recipes also provide an owned-inference path for the same checkpoint.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x924i6/ling31flash_goes_open_source_with_hermes_agent/)
