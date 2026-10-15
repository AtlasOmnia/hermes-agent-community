---
title: "Hermes Tool Router: (Unnofficial) update"
author: u/Jonathan_Rivera
date: 2026-10-15
score: 5
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x6dc13/hermes_tool_router_unnofficial_update/
flair: "Integrations"
---

# Hermes Tool Router: (Unnofficial) update

**Posted by u/Jonathan_Rivera on 2026-10-15 · 5 points (100% upvoted) · 0 comments**

I need to work on branding a bit more.
The Omnia Tool Router for Hermes just received an update. This is made for the vram impared or the people who have a light cloud plan.
What it is: every request Hermes makes to the model includes the description of every tool it has. That's often 20–30k tokens before you've said anything, sent again on every call
(unless in cache which is most of the time)
. The router is a free plugin that reads your first message, works out which tools you'll likely need, and sends only those for the rest of the session. If it isn't sure, it keeps everything. If a missing tool is needed later, it's added back automatically.
Works with or without a model:
Out of the box: built-in rules, no API key, nothing sent anywhere. Clear requests get trimmed; anything unclear keeps the full list.
Most accurate: connect a small classifier model, either local (an OpenAI-compatible server such as Ollama or LM Studio) or cloud (OpenRouter or DeepSeek). It sorts out vague first messages the rules can't, so more requests get the smaller list. If the model is slow or unsure, the router still keeps everything.
What's new:
Works on current Hermes again (newer builds had silently broken it)
Hermes's on-demand tool search keeps working with the router on
Ask "what can you do?" and get a full answer, even with a trimmed tool list
/router on | off | status switches it instantly, with no model call
Better Chinese-language routing, safer session handling, 190 tests
Real results (router off → on, rules only, no model connected):
Starting prompt: ~29k → ~18.8k tokens (−36%)
7 everyday tasks, every call counted: −34%
A bigger profile: 58.6k → 24.8k (−58%)
Same answers in every test. Bigger tool sets save more.
Plugin-only, no Hermes core changes, MIT.
👉
github.com/AtlasOmnia/hermes-tool-router

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x6dc13/hermes_tool_router_unnofficial_update/)
