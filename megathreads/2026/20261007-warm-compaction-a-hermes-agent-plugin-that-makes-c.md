---
title: "Warm Compaction: a Hermes Agent plugin that makes context compaction 3–4x faster by reusing the prompt cache"
author: u/shayanx45
date: 2026-10-07
score: 44
comments: 10
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wzj132/warm_compaction_a_hermes_agent_plugin_that_makes/
flair: "Memory & Context"
---

# Warm Compaction: a Hermes Agent plugin that makes context compaction 3–4x faster by reusing the prompt cache

**Posted by u/shayanx45 on 2026-10-07 · 44 points (100% upvoted) · 10 comments**

I built a context-engine plugin for Hermes Agent that makes compaction a lot faster.
The problem
When Hermes compacts a long session, the built-in compressor sends the history to a separate summary request. That request has a new prompt prefix, so the server processes all ~100K tokens again.
The idea
At compaction time, warm_compaction sends the last main-model request again, plus the rows that came after it and one handoff instruction at the end. The server reuses its cached prefix and reads only the new rows. The main model then writes a five-heading handoff (Goal, User instructions, Current state, Key facts, Next step).
If the warm request cannot run, it falls back to an auxiliary-model summary, and then to a fixed-format summary that needs no model. A cancelled attempt leaves the history unchanged.
Results (synthetic 100K+ token sessions, 10 cases each, median)
Compaction time:
• warm_compaction: 16.8 s
• hermes-lcm: 43.5 s
• built-in: 78.5 s
Compacted facts kept:
• warm_compaction: 59/60
• hermes-lcm: 43/60
• built-in: 50/60
Fact in the middle of a long message:
• warm_compaction: 10/10
• hermes-lcm: 0/10
• built-in: 0/10
On a DGX-hosted server, at least 99.9% of each warm request's ~108K prompt tokens were reported as cached. On LM Studio (Qwen3.5 4B), compaction went from ~34 s to ~21 s.
Details
• Works on unpatched Hermes. It uses only the documented plugin APIs, with no monkeypatching.
• No dependencies. Python 3.10+. Apache-2.0.
• Manual /compress and automatic compaction.
• The speedup needs the same model and a server with a prefix cache: hosted APIs with prompt caching, vLLM, SGLang, llama.cpp, MLX, LM Studio, Ollama, and others. It works on any OpenAI-compatible endpoint, but it is faster only when the server reuses its cache.
• Rollback: set context.engine back to compressor.
Install
hermes plugins install Elevatormusic/hermes-warm-compaction#warm_compaction --enable
Then in config.yaml:
context:
engine: warm_compaction
Repo:
https://github.com/Elevatormusic/hermes-warm-compaction
Feedback and benchmark runs on other servers are welcome.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wzj132/warm_compaction_a_hermes_agent_plugin_that_makes/)
