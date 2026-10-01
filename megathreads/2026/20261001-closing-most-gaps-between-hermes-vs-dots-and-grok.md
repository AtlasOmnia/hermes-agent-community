---
title: "Closing most gaps between Hermes vs Dots and Grok Bots"
author: u/MJ_Ali45
date: 2026-10-01
score: 85
comments: 14
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wumxde/closing_most_gaps_between_hermes_vs_dots_and_grok/
flair: "Showcase — Projects, tools, builds, demos"
---

# Closing most gaps between Hermes vs Dots and Grok Bots

**Posted by u/MJ_Ali45 on 2026-10-01 · 85 points (97% upvoted) · 14 comments**

First of all I want to say none of this may be revolutionary for a lot of you but I got replies saying people wanted what I learned. Right after dots was announced I gave a prompt to ChatGPT asking how to close any and all gaps between my Hermes agentic setup and dots along with Grok Bot. I would copy and paste the OG response from Astra but it's specified for me obviously and besides mentioning my personal setup and "secrets" it would also be hard to fully understand without context. All this to say here's what it found...
"I’m MJ’s ChatGPT. He asked me to depersonalize the original comparison I gave him around his own customized agent setup and turn it into something useful for Hermes users generally.
So this is only the gap analysis:
What do Dots/Grok Bot have that a reasonably advanced Hermes setup does not have by default, and what would you need to add to close ~90%+ of the functional gap?
1. Persistent responsibilities
Dots/Grok have:
Agents can own ongoing responsibilities/projects instead of waiting for a new prompt every time.
Close it in Hermes:
Add a small persistent Responsibility layer:
objective
owner/profile
project
triggers
Skill/workflow
autonomy level
reporting policy
active tasks
Then let cron/events create durable Kanban tasks under those responsibilities.
Difficulty:
low-medium.
2. Generalized proactive discovery / Scout
Dots has:
A proactive research mode that can inspect permitted information while the user is away and surface things that matter.
Hermes can schedule jobs, but it does not package a generalized:
“Look around my digital world and the public internet, figure out what changed that matters to my goals, and only bother me when something is actually important.”
Close it:
Build a read-only Scout routine that periodically checks authorized sources like:
email
calendar
GitHub
projects/tasks
notes/files
messages
feeds/data sources
Then let it dynamically search the public internet based on current projects, deadlines, dependencies, tracked entities, and open questions.
Examples:
news
company announcements
SEC filings
product/docs changes
GitHub releases
research
forums/Reddit
regulatory changes
competitor activity
opportunities
Scout should basically ask:
What changed?
What became relevant?
Did a dependency resolve?
Did an assumption become wrong?
Did an opportunity appear?
Is anything stuck or overdue?
Then heavily filter the results:
ignore
save quietly
attach to project
notify user
Keep Scout strictly read-only. If it finds something actionable, hand it to the normal agent/task system where regular approval rules apply.
Hermes already has most of the substrate through cron, webhooks, web search/extract, Skills, and connected integrations.
Difficulty:
low for a basic Scout, medium for a context-aware cross-source version.
3. General autonomy policy
Dots/Grok have:
Fine-grained rules around what the agent can do automatically versus what needs approval.
Example:
read email → auto
draft email → auto
send email → ask
delete file → ask
purchase → ask
credentials → human only
Close it:
Use Hermes pre_tool_call hooks with a policy file:
email.read: auto
email.draft: auto
email.send: ask
git.commit: auto
git.push: ask
files.write_local: auto
files.delete: ask
purchase: ask
credentials: human_only
Then:
ACTION
↓
POLICY
↓
AUTO / ASK / BLOCK
Difficulty:
low-medium.
4. Persistent multi-agent organization
Grok Bot has:
Persistent specialist Bots with their own memory, routines, roles, and responsibilities.
Hermes base:
Subagents are great for temporary delegated work. Profiles + Kanban are closer to persistent workers but still need organization.
Close it:
Primary Profile
↓
coordinator
↓
persistent specialist Profiles
+
temporary subagents
Use:
Profiles for persistent specialists
Kanban for durable work
delegate_task for temporary parallel work
Keep shared Skills/tools global while keeping specialist memory and responsibilities separate.
Difficulty:
medium.
5. Agent-to-agent communication and handoffs
Grok has:
Bots can message each other, assign work, hand tasks off, and trigger more work.
Close it:
Create a simple abstraction:
send_to_agent(
agent,
task,
context_refs,
expected_output
)
Underneath, create a durable Kanban task/event.
When complete:
agent.task_completed
wakes the coordinator.
Difficulty:
medium.
6. Operational state outside chat
Dots/Grok have:
The agent is the persistent entity. Chats are only interfaces into it.
Hermes base:
Persistent sessions and memory exist, but operational work can still become too chat-centric.
Close it:
Keep work state outside conversation history.
SQLite is enough:
tasks
responsibilities
projects
events
approvals
agent_messages
artifacts
routine_runs
Chat history should be context, not the source of truth.
Difficulty:
low-medium.
7. Agent presence / work state
Grok has:
Clear states like:
Idle
Thinking
Working
Waiting
Blocked
Done
Close it:
Standardize task state:
QUEUED
THINKING
WORKING
WAITING
BLOCKED
NEEDS_APPROVAL
DONE
FAILED
Then surface meaningful changes through Telegram, Slack, or a dashboard.
Difficulty:
very low.
8. Automatic resumption and follow-up
Dots/Grok have:
Work can pause on an external dependency and resume later automatically.
Close it:
Add a lightweight heartbeat that:
processes events
checks waiting tasks
checks blocked tasks
resumes eligible work
checks deadlines
retries failures
requests human input when needed
Most heartbeat passes do not need an LLM.
Difficulty:
low.
9. Unified event-driven orchestration
Grok has:
Routines can start from schedules, app events, webhooks, other agents, etc.
Hermes already has cron and webhooks. The missing part is mainly unification.
Close it:
Normalize triggers into events:
email.received
github.pr_opened
calendar.upcoming
file.changed
routine.timer
agent.completed
market.threshold
webhook.received
Then:
event
↓
matching responsibility
↓
Skill/workflow
↓
durable task
Difficulty:
low-medium.
10. Teach-by-demonstration
Grok Bot has:
The ability to watch the user perform a browser workflow and convert it into reusable automation.
Hermes has:
Skills + browser/computer use, but not the polished recorder/compiler layer.
Close it:
"Watch me do this"
↓
record actions
↓
capture browser/context state
↓
LLM abstracts procedure
↓
generate SKILL.md
↓
test
↓
correct
↓
save Skill
Difficulty:
medium-high.
11. Inspectable persistent computer + takeover
Dots/Grok have:
A persistent computer/workspace the user can inspect and take over when necessary.
Hermes already has browser/computer use and persistent browser profiles.
The main missing part is UX.
Close it:
STATUS
↓
PREVIEW
↓
TAKE CONTROL
↓
RETURN CONTROL
The environment itself can just be a dedicated machine, VM, or persistent cloud instance.
Difficulty:
medium.
12. First-class Artifacts
Grok treats:
Reports, files, code, spreadsheets, datasets, etc. as durable outputs tied to work.
Close it:
Artifact
- id
- type
- title
- project
- task_id
- created_by
- location
- version
- status
Then tasks reference actual work products instead of relying on chat messages saying they were created.
Difficulty:
very low.
13. Agent-originated communication
Hermes already has messaging gateways.
The real gap is making the agent naturally contact the user when something important happens:
"I finished this."
"I need approval."
"This became blocked."
"This changed."
"I found something important."
Close it:
Route important task/event transitions through the existing messaging layer.
Do not send raw logs.
Difficulty:
very low.
14. Operator dashboard
Dots/Grok have:
Much better interfaces for active work, projects, approvals, agents, routines, computer activity, artifacts, and notifications.
Close it eventually:
Build a thin agentic dashboard:
Home
Work
Projects
Agents
Routines
Artifacts
Approvals
Computer
Activity
Memory
I would build this after the backend autonomy layer works.
Difficulty:
medium-high, mostly frontend.
15. Rich interactive outputs
Dots/Grok have:
Inline approvals, task cards, email previews, routine controls, charts, system events, etc.
Close it:
Use typed UI objects:
message
task
approval
artifact
email
calendar_event
routine
chart
computer_event
agent_handoff
Mostly a UX problem.
Difficulty:
medium.
What I would NOT rebuild
Hermes already provides most of the difficult execution substrate:
Skills
memory
cron
webhooks
Profiles
Kanban
subagents
browser
web search/extract
computer use
shell
files
MCP
messaging gateways
persistent browser profiles
approvals
hooks
Docker/isolation
model flexibility
The missing layer is mostly:
persistent responsibility
+
proactivity / Scout
+
unified events
+
durable operational state
+
persistent multi-agent coordination
+
general autonomy policy
+
operator UX
If I wanted ~90%+ functional parity
I would build in roughly this order:
Persistent responsibility objects
SQLite operational state
Context-aware Scout
Unified event layer over cron/webhooks
AUTO / ASK / BLOCK policy system
Coordinator Profile + persistent specialist Profiles
Durable agent handoffs
Standard task/work states
Heartbeat/resume/retry logic
Artifact registry
Agent-originated notifications
Agentic dashboard
Computer preview/takeover
Teach-by-demonstration
My takeaway from the original comparison was:
Hermes is not missing most of the engine. It is missing the integrated control plane and product layer that make Dots/Grok Bot feel like persistent workers instead of powerful agents.
For a technically capable Hermes user, most of that gap looks closable without replacing Hermes itself."
EDIT: I will update y’all on my progress, I just am about to finish up version two of my agentic ecosystem and version three will be the completion of all these implementations.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wumxde/closing_most_gaps_between_hermes_vs_dots_and_grok/)
