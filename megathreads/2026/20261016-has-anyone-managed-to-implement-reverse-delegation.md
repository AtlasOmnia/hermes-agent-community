---
title: "Has anyone managed to implement reverse delegation / model escalation in Hermes?"
author: u/IaryBreko
date: 2026-10-16
score: 6
comments: 6
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x6ir99/has_anyone_managed_to_implement_reverse/
flair: "MODELS - model choice, routing, pricing, local vs cloud, VRAM"
---

# Has anyone managed to implement reverse delegation / model escalation in Hermes?

**Posted by u/IaryBreko on 2026-10-16 · 6 points (100% upvoted) · 6 comments**

I’m experimenting with a multi-model setup in Hermes and wondering if anyone has managed to get something like this working.
My ideal setup would be:
- Claude Sonnet
as the main orchestrator.
- DeepSeek Flash
for cheaper delegated tasks via delegate_task.
- Claude Opus
for particularly difficult tasks where Sonnet needs extra reasoning power.
Essentially, the reverse of delegate_task. Rather than just delegating easier work to cheaper models, I’d like the main agent to be able to escalate difficult problems to a stronger model when needed.
Ideally, Sonnet could recognise when it’s struggling, consult Opus or hand off a specific problem, receive the result, and continue the original task. No need to manually switch models or change the entire session.
I’ve found a few related GitHub discussions:
PR #100821 - Consult tool
PR #92370 - Loop-bounce escalation skill
Issue #119780 - Failure-triggered model escalation
I realise automatic model routing has received some pushback from maintainers, but I’m curious whether anyone has built a working solution independently.
Has anyone achieved this using custom skills, tools, plugins, or external orchestration?
Particularly interested in how you handle context handoff, deciding when escalation is necessary, and preventing unnecessary expensive model calls.
Would love to hear what people have tried!

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x6ir99/has_anyone_managed_to_implement_reverse/)
