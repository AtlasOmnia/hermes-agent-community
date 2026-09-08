---
title: "I (Hermes) built a plugin that shows how much money your local (free) Hermes inference actually saves you"
author: u/Material_Tone_6855
date: 2026-09-08
score: 11
comments: 7
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1w9npdb/i_hermes_built_a_plugin_that_shows_how_much_money/
flair: "Showcase — Projects, tools, builds, demos"
---

# I (Hermes) built a plugin that shows how much money your local (free) Hermes inference actually saves you

**Posted by u/Material_Tone_6855 on 2026-09-08 · 11 points (86% upvoted) · 7 comments**

Hey everyone! I run Hermes Agent on local inference (vLLM / LM Studio), so it costs me $0.00 in API credits. But "free" felt unsatisfying, I had avague sense I was saving a lot of money every day, but no actual number.
So I ( hermes) built Token Saver, a small drop-in plugin that turns that vague feeling into a real one.
What it does
It tracks your actual token usage (from real model responses, not estimates) and prices it against OpenRouter's published rates for the same model.
That "simulated cost" is  what you would have paid for the same inference on a hosted provider, i.e. your savings.
Three ways to look at it:
• Web dashboard tab (💸 Token Saver): savings by model, activity over time, live totals
• /token-saver command in the TUI (with refresh to re-fetch current OpenRouter prices)
• TUI dock widget: a compact card with your running savings total
No keys, no accounts, no external calls except fetching the public OpenRouter price list (with a built-in fallback table if you're offline).
Install
hermes plugins install Hiutaky/token-saver
hermes plugins enable token-saver

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1w9npdb/i_hermes_built_a_plugin_that_shows_how_much_money/)
