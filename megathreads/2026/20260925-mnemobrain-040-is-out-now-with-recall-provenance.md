---
title: "MnemoBrain 0.4.0 is out - Now with recall provenance"
author: u/AxelFooley
date: 2026-09-25
score: 10
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wov0s9/mnemobrain_040_is_out_now_with_recall_provenance/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# MnemoBrain 0.4.0 is out - Now with recall provenance

**Posted by u/AxelFooley on 2026-09-25 · 10 points (100% upvoted) · 3 comments**

Your feedbacks in my
last post
were exactly what i needed.
A simple question as "
do you log which memories entered each answer?
" sent me back into thinking mode and i'm so grateful for that because i realised that this gap was deeper than i thought, the upstream service Mnemosyne, didn't provide such feature so with the current state it was impossible to have such capability.
So this is what i did: i've contributed to Mnemosyne
with a PR
, and on the side i've integrated the feature in MnemenoBrain in a new release.
How it works, deliberately lean:
Flip MNEMOSYNE_RECALL_PROVENANCE=1 and every recall writes one JSONL line right after the final top-k selection: the query, which memory IDs came back, their scores. The log lives next to the DB (<db>.recall_provenance.jsonl), one file per database, trivially greppable.
IDs and scores only, no content previews, enough to audit "
why did the agent say X?
" without turning the log itself into a second memory dump. The agent will autonomously look up for that memory ID in the database to show it to you.
Off by default, it's an audit trail tool so you don't have to turn it on if you don't need it.
The result now is that if your agent says something bogus you can just ask "
why did you say that? show me which memory generated that answer
" and there you have it.
Repo:
https://github.com/AxelFooley/MnemoBrain
Release:
https://github.com/AxelFooley/MnemoBrain/releases/tag/v0.4.0
Feedbacks and contribution as always are much appreciated.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wov0s9/mnemobrain_040_is_out_now_with_recall_provenance/)
