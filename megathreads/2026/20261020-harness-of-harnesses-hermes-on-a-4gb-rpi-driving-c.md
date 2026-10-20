---
title: "Harness of harnesses: Hermes on a 4GB RPi driving Claude Code, Kimi and Copilot CLIs"
author: u/msalsas
date: 2026-10-20
score: 8
comments: 5
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x9ptoo/harness_of_harnesses_hermes_on_a_4gb_rpi_driving/
flair: "Use Cases & Workflows"
---

# Harness of harnesses: Hermes on a 4GB RPi driving Claude Code, Kimi and Copilot CLIs

**Posted by u/msalsas on 2026-10-20 · 8 points (100% upvoted) · 5 comments**

Been running Hermes on a Raspberry Pi (4GB) for about a week now and I'm not sure if what I built is a good solution or just a weird one, so I'm curious what you all think. It ended up managing three coding CLIs, each with a specific model for a specific job:
Claude Code (Opus 5.5)
writes the spec before any code exists and gives the final verdict on the diff.
Kimi Code (Kimi K3)
implements it in a sandboxed worktree.
Copilot CLI (GPT-5.6 Terra)
reviews everything with fresh eyes before merge; it's also used as backup when one of the others is unavailable.
Hermes (Qwen3.8-Flash-Next GGUF, served from an RTX 5080 rig at home)
orchestrates all of it: runs the test gate itself, handles git and GitHub, and talks to me over Telegram.
Four different model families checking each other's work. Each harness lives in bubblewrap with only the repo bind-mounted and a scoped GitHub token.
Built llama-doctor with this setup (a read-only diagnostician for llama.cpp servers): spec, implement, 378 tests green, double review, public repo. Took surprisingly few iterations.
This is probably overengineered, but I'm having too much fun :)

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x9ptoo/harness_of_harnesses_hermes_on_a_4gb_rpi_driving/)
