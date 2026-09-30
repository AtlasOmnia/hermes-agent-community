---
title: "How we use Hermes to run most of our SDLC"
author: u/UC_Kratom
date: 2026-09-30
score: 5
comments: 2
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wtpoar/how_we_use_hermes_to_run_most_of_our_sdlc/
flair: "Use Case — Real tasks, business & personal"
---

# How we use Hermes to run most of our SDLC

**Posted by u/UC_Kratom on 2026-09-30 · 5 points (100% upvoted) · 2 comments**

We’re Moosky AI - two humans building an agentic multimodal video platform.
Internally, Hermes runs most of our SDLC: grooming, pick up work, implement, test, PR, gate, ship.
We mostly review outcomes.
Three PM-owned domains
Each Hermes team has a PM plus Engineers/Architects. The PMs own Azure DevOps Boards end to end.
Marketing
covers growth work we actually run: SEO landings, organic search ops (GSC / indexation / CTR), blogs, and posting to places (Quora, Threads/X, Medium, newsletter).
It also watches/manages Google Ads, Meta, and related channels alongside that organic work.
Feature Dev
takes two kinds of intake: feedback stories filed as agents ship, and human goal-oriented epics/stories we drop in to steer (product upgrades, localization, Director work, infra we care about). New work keeps showing up; the system keeps producing code.
We steer with goals, standards, and gates.
Production Support
is alert-driven. It watches Kubernetes and application error logs, cards incidents, and routes by severity.
P1s escalate to a human. Lower severity joins the queue like any other card.
How we got past the review bottleneck
Early on, humans reviewed everything - that became the choke point.
Agents were shipping faster than we could look, so we added a management-layer agent on a different harness: more context, less freestyle autonomy, more bursty.
It talks to the Hermes teams through ADO (boards, PRs, work items) and owns the final merge decision on eligible work.
Gating
Every PR goes through a stack before anything hits main:
Peer agent code review
Build validation
Preview env deploy + e2e testing
PM sign-off
If those clear, the Dev Mgr agent runs its own merge checklist: story objective vs diff, diff skim for secrets / wrong env / obvious breakage, evidence (screenshots or live preview), open follow-ups/conflicts, and a
complexity gate
.
Lower-complexity work can merge fully agent-side, higher-complexity stays human-required for now (we remain a required reviewer on those).
A fair portion of what we ship is already fully e2e and agent-merged.
We ship daily and the agents smoke-test their work-items from the deployment.
What we still own
Direction, standards, and “is this good enough.”
We document the patterns, make review enforce them, point the machine with goal epics when we want a turn. Hermes keeps grinding the backlog without us midwifing every ticket.
Cost-wise, a lot of this runs on our own lab hardware. Same token burn on public APIs would be ugly. That’s a big reason two humans can keep a swarm going.
Happy to go deeper in the comments if anyone is interested.
We are curious if others here are using it similarly to automate their SDLC process, and to what degree.
We are continuously evolving this - our next steps are likely building out more of the management layers, and backfilling other types of roles.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wtpoar/how_we_use_hermes_to_run_most_of_our_sdlc/)
