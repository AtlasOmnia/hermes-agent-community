---
title: "Hermes + Jev + LiteLLM : 50% tokens saving"
author: u/Timus0708
date: 2026-10-10
score: 101
comments: 32
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x1sjss/hermes_jev_litellm_50_tokens_saving/
flair: "MODELS"
---

# Hermes + Jev + LiteLLM : 50% tokens saving

**Posted by u/Timus0708 on 2026-10-10 · 101 points (98% upvoted) · 32 comments**

Last week I made a setup which is working great and saving close to 50% in token costs.
A lot of my usage is coding and basic Q&A/fact-checking/summaries/todos/MCP questions — which can be handled with a decent tool-calling model.
I heavily use LLM Wiki and Todoist to manage stuff.
Every query gets validated by JEV to see if it can be answered by a simpler model, and based on the need, it selects the appropriate model.
\------------------------------
Here is my setup:
Step 1:
Set up LiteLLM as the main model-serving API.
I have a few services like a qBittorrent bot, Telegram bot, and ESP32-based bot that leverage this gateway, so this works best for me.
Step 2:
Add a custom Python script for the JEV model — “JEV Classifier”.
It takes two inputs: state and question.
State:
Last 10K tokens of the chat
Question:
A prompt with examples and a choice to select from: simple / medium / complex / reasoning.
Step 3:
Set up a model router — “JEV Router” — using these exact labels, with the LLM classifier (JEV Classifier):
Simple:
Gemma 4 / Ling 3.0
Medium:
DeepSeek Flash
Complex:
Qwen 3.8
Reasoning:
Sonnet 5
Step 4:
Connect this gateway to Hermes and select this router as the model. Now it automatically switches models based on the complexity of the query.
\--------------------------------
This setup is not only helpful in Hermes, but also works with any other service I connect to this gateway.
I saw people asking about JEV-based setups in the comments, so dropping this here.
Let me know your thoughts/comments, or if anyone else is using JEV in a better way with Hermes.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x1sjss/hermes_jev_litellm_50_tokens_saving/)
