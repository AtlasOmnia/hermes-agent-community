---
title: "A Warning For Beginners For Hermes: My Hermes agents kept "forgetting" at 100k tokens — because of hermes compression error. It made me fix Token Usage by a lot."
author: u/Pheidiase
date: 2026-09-08
score: 25
comments: 17
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1w9p76w/a_warning_for_beginners_for_hermes_my_hermes/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# A Warning For Beginners For Hermes: My Hermes agents kept "forgetting" at 100k tokens — because of hermes compression error. It made me fix Token Usage by a lot.

**Posted by u/Pheidiase on 2026-09-08 · 25 points (100% upvoted) · 17 comments**

sharing for anyone new like me hitting the same problems: before you blame the model for "forgetting"-"being an idiot", or use of high tokens for simple tasks, check your compression threshold.
for the past few days my main models and subagents would forget what they done mid-task and restart from scratch for more than 4-5 times or forget the files they read and tried to read the same files over and over (and can't read because of hermes same file reading stop and making it a non ending cycle) making some jobs use arounda 200k more tokens. checked the logs from openrouter and it always happens around 80-100k tokens. deepseek flash has 1M+ context so i assumed the model itself was losing it.
nope.
in hermes's model catalog these models have no context_length field. so hermes falls back to a 200k default window, and with main threshold of 0.5 it compresses the chat at 100k token. the model wasn't forgetting — hermes was compacting early, and making the models forget essential data of the job you are doing. They don't remember the things they did before in that chat and begins from scratch, then forgets the next thing they did and start again lol.
fix is simple:
model:
context_length: 1048576
compression threshold: 0.5
this moves the trigger to ~524k. if the hermes model catalog had these filled in, none of this would've been needed.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1w9p76w/a_warning_for_beginners_for_hermes_my_hermes/)
