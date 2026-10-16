---
title: "I'm the internal IT department of a mid-sized travel company (~165 employees, ~200 M365 accounts). We have a separate dev team for the product, but I don't work with them. Everything below is internal IT."
author: u/Physical-Economist27
date: 2026-10-16
score: 16
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x6n24u/im_the_internal_it_department_of_a_midsized/
flair: "Use Case — Real tasks, business & personal"
---

# I'm the internal IT department of a mid-sized travel company (~165 employees, ~200 M365 accounts). We have a separate dev team for the product, but I don't work with them. Everything below is internal IT.

**Posted by u/Physical-Economist27 on 2026-10-16 · 16 points (100% upvoted) · 4 comments**

Over the past few months I've moved my daily work into Hermes, across every area I'm responsible for. By now about 80% of it is covered. Some of it runs fully on its own. Most of the rest is "pre-automated": the agent has done the research, diagnosis and draft, and I approve, adjust or reject.
The setup
I run separate Hermes profiles on a private Slack workspace that only I use. Each profile has its own bot, SOUL.md, memory and tools:
IT Ops for the tenant, endpoints, network, servers, licenses, contracts and security
Helpdesk for every incoming request from employees
Dev for my own software projects (internal tools, integrations, MCP servers)
The IT Ops profile works in a Root → Workstations → Projects folder layout (Jeff Su's method). Each area (M365, RMM, network, Azure, servers, NIS2, contracts and so on) has its own rules file and memory file. Before a task the agent reads the right workstation, and afterwards it updates that workstation's memory itself.
90% of our software stack is behind MCPs
About 90% of the software we use is connected to Hermes through MCP servers, some off the shelf and some I wrote myself. That's what lets me manage and control all of it from one place. Two examples:
Lokka for Microsoft: I started with Lokka and extended it to roughly full coverage of Graph v1.0 and beta: users, groups, Entra, Exchange, Intune, Teams settings and so on. Whatever the Graph API can't do, Lokka runs as PowerShell instead, so in practice nothing in the Microsoft stack is out of reach.
Action1 (my own MCP): the agent reads device state directly, so for any device issue it has already looked at the machine (read-only) before I do.
Beyond those, Asana, Atlassian (Jira/Confluence), Azure, our security stack (Purview, Sentinel, Defender) and most of our other tools are connected too. A shared gateway with a few hundred tools loads them on demand, so the context window stays usable.
It also has access to my Teams. It catches incoming messages and prepares answers, but it doesn't send anything there on its own.
Helpdesk
Whatever employees need from IT lands with the helpdesk agent first: access and permissions, licenses, onboarding and offboarding, MFA and sign-in problems, mailboxes and shared mailboxes, Teams, software requests, Atlassian access, devices, security questions. Hardware is one category among many.
Right now employees open tickets through an Asana form. Asana sends them to Hermes via webhook, and a sweep job catches any the webhook missed. For each ticket the agent:
works out what the person actually needs
checks the affected systems: the account and permissions through Graph, the device through Action1, and whatever other tool is involved through its MCP
pulls the matching skill (onboarding, offboarding, conditional access, Exchange, MDM/Autopilot, BitLocker/FileVault recovery, compromised account response and so on)
drafts the answer, or the exact change it wants to make
Where tickets end up:
30% I never see. The agent solves them on its own. For hardware problems, for example, it answers with a short how-to video (made with Remotion) that walks the person through the fix.
50% take a yes/no or a one-line answer from me. Diagnosis, drafted reply and planned change are already there.
20% I still work on properly. Even those arrive with the analysis done.
Next: Support v2.0
We're rolling out Claude to every employee. Once everyone has access, a support MCP takes over ticket intake: people describe their problem to Claude, and it creates the ticket directly on the Hermes kanban board. The Asana form drops out completely. The first tests have gone smoothly, and now we're only waiting for the rollout to reach all employees.
The rest of my day
Tickets are only part of it. The same pre-work happens for everything else I do:
Security: Defender, Sentinel and Purview alerts are triaged and summarized before I look, with a recommendation attached.
Tenant and tool analysis: license usage, conditional access, Azure subscriptions and adoption of the tools we pay for get analyzed up front. I get a finding with a recommendation and decide.
Contracts and licenses: reviews, renewals and usage-based billing checks are prepared, and a small contract management tool keeps the overview.
Meetings: to-dos from meeting transcripts land in my task list automatically.
Changes: whenever something has to change in production, the agent has already prepared it and only needs my go.
Dev environment
I don't open a terminal for most of my coding anymore. All my projects run through Hermes and Claude Code.
Every repo has its own Slack channel. A new message in a project channel starts its own Claude Code session (Opus with the Superpowers plugin), and the thread under it is that session.
Each session posts a live status message that shows what it's currently doing. I reply in the thread like I would in a terminal, including screenshots, and use short commands like stop, status or done. /resume lists the recent sessions of a project.
Agent teams run in the background, and I can keep talking to the main session in the meantime and ask for status at any point, like in Claude Code itself.
When a session's context gets too full, it compresses automatically and resends my message.
Hermes writes the briefs for larger builds. Every brief has to name concrete steps: brainstorming and a written plan for new features, TDD for every change, systematic debugging for every bug, a code review before merge, and verification before it reports done.
Before anything gets merged, a separate red-team run tries to break it. On a pass it fast-forwards, pushes and closes the ticket. Minor findings go onto a collection list instead of spawning new runs.
Hermes checks every result itself before telling me it's done: it reruns the test suite in a clean worktree, scans for secrets and checks the remote. Claude's self-reports aren't enough.
That's how the custom MCPs were built, along with the contract management tool and a few internal tools for colleagues.
The rule that makes it safe on production
Diagnose before action. The agent can read, export and analyze whatever it needs. Anything that changes production (Set/New/Remove, permissions, enabling or disabling accounts) stops at a written finding with one recommendation, and it waits for my "yes". Larger changes run in batches with a check after each one. In the dev environment it has more freedom: building, testing, red-teaming and pushing on my own repos happen without asking.
Other things I use daily
Subagents for research or parallel audits, where only the summary comes back
Long-term memory (Hindsight) across sessions
Cron jobs for recurring checks and reports
Slack on my phone as the main interface
Happy to answer questions or share sanitized versions of the rules files and the dev environment setup.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x6n24u/im_the_internal_it_department_of_a_midsized/)
