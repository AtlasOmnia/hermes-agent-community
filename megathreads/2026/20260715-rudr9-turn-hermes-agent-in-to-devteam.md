---
title: "RUDR9 - Turn Hermes Agent in to dev-team."
author: u/humanth-shashani
date: 2026-07-15
score: 53
comments: 13
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1uxnr3u/rudr9_turn_hermes_agent_in_to_devteam/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# RUDR9 - Turn Hermes Agent in to dev-team.

**Posted by u/humanth-shashani on 2026-07-15 · 53 points (100% upvoted) · 13 comments**

One-command installer that turns Hermes Agent into a 9-role dev team

I've been using Hermes Agent for a while and kept running into the same setup work every time I wanted a structured dev workflow. Create profiles, configure toolsets, set up Kanban, install skills, wire MCPs. So I packaged all of it into a single script.

It's called RUDR9. You run it on a fresh Hermes install and you get 8 specialist profiles plus the default profile acting as CTO:

\- Planner (specs, BDD acceptance criteria)

\- Architect (technical design, API contracts)

\- Version Control Manager (git workflow, PRs, merges)

\- Builder (implementation + inline validation)

\- Security Auditor

\- Performance Auditor

\- Reviewer (final quality gate)

Coordination goes through Hermes's built-in Kanban board. The CTO creates tasks, the dispatcher spawns the assigned profile as a worker, results flow through task comments and linked dependencies. You see everything on the board.

The part I care most about: authority is enforced by toolset restrictions, not just system prompt instructions. The planner profile doesn't have the file write tool. The security auditor doesn't have terminal. A guard plugin (pre\_tool\_call hook) catches anything the toolset config misses. "Cannot write code" means the tool isn't there, not that the model was told not to.

Some honest limitations:

Builder and VCM both have terminal access, so the "physically cannot" claim is true for the read-only roles but not for those two. That's a known gap. The guard plugin checks tool names, not command content, so a determined Builder can still write app code through the shell. Branch protection and merge tokens are the real enforcement layer for that, and those aren't wired up yet.

The GitHub MCP uses @modelcontextprotocol/server-github which is the deprecated reference server. There's a newer official one I haven't switched to yet.

No CI workflow. The Dockerfile exists for manual testing but there's no GitHub Actions pipeline running it on PRs.

Install time is about 30 seconds. The first version took 8 minutes because the ponytail skill was getting downloaded and security-scanned once per profile (8 times). Fixed by installing it once on the default profile before cloning — clones inherit skills from default, so 7 of those scans just disappear.

It's MIT licensed, open source, and the repo has the full architecture review (done by Claude Opus, which told us 9 roles was over-engineered and we should ship 3 instead — we disagreed on some points and agreed on others).

Repo: https://github.com/ardhaecosystem/RUDR9

If anyone's interested in testing it or contributing, the Dockerfile gives you an isolated Hermes environment so you don't risk your own setup. Feedback welcome, especially on the role model — I know 9 profiles sounds like a lot, and I'm open to being wrong about it.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1uxnr3u/rudr9_turn_hermes_agent_in_to_devteam/)

