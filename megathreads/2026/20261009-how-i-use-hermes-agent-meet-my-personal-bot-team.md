---
title: "How I Use Hermes Agent: Meet My Personal Bot Team"
author: u/saivighnesh2190
date: 2026-10-09
score: 5
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x1b9dg/how_i_use_hermes_agent_meet_my_personal_bot_team/
flair: "Use Cases & Workflows"
---

# How I Use Hermes Agent: Meet My Personal Bot Team

**Posted by u/saivighnesh2190 on 2026-10-09 · 5 points (63% upvoted) · 4 comments**

Hermes Agent is the foundation. The bots are how I organize the work.
Hermes Agent, from Nous Research, gives me an assistant that can work with tools—not just generate text. Depending on the task and enabled tools, that means reading files, running commands, searching documentation, editing code, or checking an actual result.
My main interface is Hermes Desktop. The bot setup is built around separate Hermes profiles, with their own instructions, memories, skills, and conversation histories.
That separation matters. My interview-preparation discussions don’t need to live in the same conversation as a desktop troubleshooting session.
Here’s how I’ve organized it.
Jinwoo — my main agent
Jinwoo is my general entry point: the assistant with the broader context about my projects, preferences, and goals.
I use this role to clarify the outcome, break down a task, and decide where specialist help belongs.
One important instruction in my setup is technical honesty: don’t describe demo data as real, don’t call classical optimization AI, and don’t say something works without checking it.
Example prompt:
>
The point isn’t to generate a bigger plan. It’s to connect the request to evidence and a useful next action.
Beru — the builder
Beru is configured for execution: scaffolding, repetitive edits, refactoring, test generation, and rapid prototyping.
Its instructions emphasize reporting what changed, which files were touched, and what remains blocked. For Git work, the role also calls for worktree isolation.
My Beru history includes project-building requests such as Sprint Prep and work on an InterviewOS dashboard.
Example prompt:
>
The useful handoff is a change I can inspect—not just a confident “done.”
Igris — the reviewer and interview-prep partner
Igris is the deliberate counterpart to Beru.
I’ve configured it for architecture, trade-offs, code correctness, maintainability, and technical placement preparation.
My actual conversations include Java/OOP interview preparation and reviewing campus-hiring material. That makes it useful beyond software implementation: it also helps me understand and explain the concepts behind the code.
Example prompt:
>
Building something and explaining why it works are different skills. I want support for both.
Tusk / The Scholar — research and practical system work
Tusk is my research and generalist profile, currently named The Scholar in its persona file.
Its reference context covers research, DevOps, automation, documents, and the AI tooling ecosystem. Its history also includes practical requests such as investigating Manjaro issues and a recurring WPS Writer error.
Example prompt:
>
For troubleshooting, I want the same discipline: identify the cause, make a scoped change, verify the result, and explain recovery if needed.
How the roles fit together
For a feature-development demo, the handoff would look like this:
Jinwoo scopes the task → Tusk researches uncertainties → Beru implements → Igris reviews → I inspect the evidence.
That is an example workflow, not a claim that every task follows an automatic pipeline. A simple question does not need every bot involved.
Separate profiles also don’t automatically share everything they know. A useful handoff needs explicit context: the goal, relevant files, constraints, findings, and acceptance criteria.
What I find valuable about this setup
Clear responsibilities. I know which bot to approach and what kind of output to ask for.
Persistent context. I can return to a role without rebuilding its purpose from scratch. That doesn’t mean perfect recall; important details still need verification.
Reusable skills. Procedures can be saved as skills instead of remaining buried in a chat. This is workflow reuse—not model retraining.
Evidence over confidence. A code change should come with test output. Research should come with sources. A system fix should come with verification.
I still review the work. Bots can misunderstand requirements, repeat an incorrect assumption, or hit tool and provider limits. Adding more agents also adds coordination overhead; it is not automatically faster or cheaper.
For me, the interesting shift is from “Which AI should I ask?” to “What role does this task need, and what evidence should that role return?”
That’s what my Hermes bot team is built
around.Hermes
Agent is the foundation. The bots are how I organize the work.
Hermes Agent, from Nous Research, gives me an assistant that can work with tools—not just generate text. Depending on the task and enabled tools, that means reading files, running commands, searching documentation, editing code, or checking an actual result.
My main interface is Hermes Desktop. The bot setup is built around separate Hermes profiles, with their own instructions, memories, skills, and conversation histories.
That separation matters. My interview-preparation discussions don’t need to live in the same conversation as a desktop troubleshooting session.
Here’s how I’ve organized it.
Jinwoo — my main agent
Jinwoo is my general entry point: the assistant with the broader context about my projects, preferences, and goals.
I use this role to clarify the outcome, break down a task, and decide where specialist help belongs.
One important instruction in my setup is technical honesty: don’t describe demo data as real, don’t call classical optimization AI, and don’t say something works without checking it.
Example prompt:
I want to improve termbrain. First inspect what actually exists, identify the most useful next improvement, and separate research, implementation, and review work.
The point isn’t to generate a bigger plan. It’s to connect the request to evidence and a useful next action.
Beru — the builder
Beru is configured for execution: scaffolding, repetitive edits, refactoring, test generation, and rapid prototyping.
Its instructions emphasize reporting what changed, which files were touched, and what remains blocked. For Git work, the role also calls for worktree isolation.
My Beru history includes project-building requests such as Sprint Prep and work on an InterviewOS dashboard.
Example prompt:
Implement this scoped feature in an isolated worktree. Run the relevant tests, then report the files changed, the actual test results, and any blockers.
The useful handoff is a change I can inspect—not just a confident “done.”
Igris — the reviewer and interview-prep partner
Igris is the deliberate counterpart to Beru.
I’ve configured it for architecture, trade-offs, code correctness, maintainability, and technical placement preparation.
My actual conversations include Java/OOP interview preparation and reviewing campus-hiring material. That makes it useful beyond software implementation: it also helps me understand and explain the concepts behind the code.
Example prompt:
Review this implementation for correctness and maintainability. Then ask me to explain its design as if this were a technical interview. Challenge weak assumptions instead of agreeing with me.
Building something and explaining why it works are different skills. I want support for both.
Tusk / The Scholar — research and practical system work
Tusk is my research and generalist profile, currently named The Scholar in its persona file.
Its reference context covers research, DevOps, automation, documents, and the AI tooling ecosystem. Its history also includes practical requests such as investigating Manjaro issues and a recurring WPS Writer error.
Example prompt:
Compare these tools using current official sources. Separate verified capabilities from marketing claims, explain the limitations, and save a cited recommendation.
For troubleshooting, I want the same discipline: identify the cause, make a scoped change, verify the result, and explain recovery if needed.
How the roles fit together
For a feature-development demo, the handoff would look like this:
Jinwoo scopes the task → Tusk researches uncertainties → Beru implements → Igris reviews → I inspect the evidence.
That is an example workflow, not a claim that every task follows an automatic pipeline. A simple question does not need every bot involved.
Separate profiles also don’t automatically share everything they know. A useful handoff needs explicit context: the goal, relevant files, constraints, findings, and acceptance criteria.
What I find valuable about this setup
Clear responsibilities. I know which bot to approach and what kind of output to ask for.
Persistent context. I can return to a role without rebuilding its purpose from scratch. That doesn’t mean perfect recall; important details still need verification.
Reusable skills. Procedures can be saved as skills instead of remaining buried in a chat. This is workflow reuse—not model retraining.
Evidence over confidence. A code change should come with test output. Research should come with sources. A system fix should come with verification.
I still review the work. Bots can misunderstand requirements, repeat an incorrect assumption, or hit tool and provider limits. Adding more agents also adds coordination overhead; it is not automatically faster or cheaper.
For me, the interesting shift is from “Which AI should I ask?” to “What role does this task need, and what evidence should that role return?”
That’s what my Hermes bot team is built around.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x1b9dg/how_i_use_hermes_agent_meet_my_personal_bot_team/)
