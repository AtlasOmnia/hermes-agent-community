---
title: "How do u run subagents with a specific model/reasoning-effort from main thread in Hermes Agent, without changing the global profile default?"
author: u/pck91999
date: 2026-09-25
score: 5
comments: 10
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wp7foj/how_do_u_run_subagents_with_a_specific/
flair: "Help — Technical issues, errors, config, debugging"
---

# How do u run subagents with a specific model/reasoning-effort from main thread in Hermes Agent, without changing the global profile default?

**Posted by u/pck91999 on 2026-09-25 · 5 points (100% upvoted) · 10 comments**

I wanted to  use  delegate_task tool to fan out work to subagents just like  the pattern of claude code and codex use. A cheap/fast model for exploration or implementation, a stronger model for review, dispatched from a main thread.
So today, if I want one batch of subagents on gpt-6-sol at medium reasoning and a different batch (say, reviewers) on something else, my only option is:
delegate_task's schema only takes goal, context, images, and output_schema. There's no model, provider, or reasoning_effort parameter on the call itself. Every subagent it spawns inherits whatever is set in delegation.model / delegation.provider / delegation.reasoning_effort in the profile's config.yaml. I confirmed this by reading delegate_tool.py and delegate_tool_config.py there's genuinely no per-task override wired up.
What I'm missing: is there an existing way to pass model/provider/reasoning per delegate_task call that I haven't found? Environment variable scoping, a task-level override field I'm not seeing in some newer version, a wrapper pattern people use, a config profile-switching trick, anything? Or is "mutate the global default before each dispatch" genuinely the intended workflow right now?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wp7foj/how_do_u_run_subagents_with_a_specific/)
