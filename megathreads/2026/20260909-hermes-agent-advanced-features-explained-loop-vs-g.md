---
title: "Hermes Agent Advanced Features Explained: Loop vs Goal vs Cron vs Delegation vs Kanban vs Mixture of Agents"
author: u/viky_shetye
date: 2026-09-09
score: 40
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1war5vy/hermes_agent_advanced_features_explained_loop_vs/
flair: "Guide — Tutorials, walkthroughs, repeatable how-tos"
---

# Hermes Agent Advanced Features Explained: Loop vs Goal vs Cron vs Delegation vs Kanban vs Mixture of Agents

**Posted by u/viky_shetye on 2026-09-09 · 40 points (90% upvoted) · 4 comments**

I spent some time digging into the more advanced parts of
Hermes Agent
, and the biggest thing that clicked for me was that its autonomy features are solving very different problems.
A useful mental model:
🔁
Loop
= repeat something inside the current session
🎯
Goal
= keep working until a defined objective is actually complete
⏰
Cron Jobs
= scheduled, unattended agent workflows
🧩
Delegation
= temporary parallel sub-agents
🤖
Profiles / Bot Mode
= persistent specialist agents
📋
Kanban
= durable multi-agent orchestration with dependencies and handoffs
🧠
Mixture of Agents
= multiple LLM perspectives feeding one acting model
The distinctions matter more than they initially seem.
For example, /goal isn’t a background workflow or a multi-agent system. It keeps the current Hermes session focused on one objective and uses a judge/completion contract to decide whether it should continue.
Delegation is different again: sub-agents are temporary workers with isolated context.
Bot Mode gives you persistent specialists agents interface.
And once those specialists need dependencies, retries, artifacts, human review, or workflows lasting hours or days, that’s where Kanban starts making much more sense.
Mixture of Agents is probably the easiest one to misunderstand because it isn’t really multi-agent orchestration at all. It’s
model-layer parallelism
: multiple reference models provide perspectives, while an aggregator remains the acting model inside the normal Hermes agent loop.
I made a full video breaking down how all of these work under the hood, including examples and when I’d choose one over another.
🎥 Video:
https://youtu.be/E_tj3VgHAUY
Curious how others are using Hermes Agent: are you leaning more toward autonomous single-agent workflows, persistent specialist bots, or coordinated multi-agent systems?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1war5vy/hermes_agent_advanced_features_explained_loop_vs/)
