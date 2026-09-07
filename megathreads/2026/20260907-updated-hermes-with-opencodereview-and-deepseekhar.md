---
title: "Updated: Hermes with open-code-review and deepseek-harness"
author: u/PoppaBear1950
date: 2026-09-07
score: 8
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1w9az27/updated_hermes_with_opencodereview_and/
flair: "Showcase — Projects, tools, builds, demos"
---

# Updated: Hermes with open-code-review and deepseek-harness

**Posted by u/PoppaBear1950 on 2026-09-07 · 8 points (90% upvoted) · 3 comments**

A common bottleneck with local agentic coding is context bloat. Stuffing repository context, tool execution, test logs, and high-level orchestration into a single context window quickly blows through limits, destroys prompt caching, and drives up token costs.
To solve this, I split the workload into a
three-tier architecture
that isolates dirty execution loops from high-level orchestration, using
open-code-review
as the context-control firewall.
The Three-Tier Architecture
Tier 1: Orchestration & Session State (Hermes Agent)
Maintains the primary cached context window, user session state, and persistent memory/notes.
Defines tasks, boundaries, and acceptance criteria without ingesting raw repository files or terminal spew.
Delegates targeted development work downstream.
Main Model:
gemini-3.6-flash
Tier 2: Context Firewall & Scope Control (
open-code-review
)
Acts as the filter between the orchestrator and the execution environment.
Extracts minimal semantic context, analyzes AST/diff boundaries, and generates condensed task specs.
Reviews subagent output to distill massive compiler/test logs down to structured summaries, clean diffs, and exit codes before anything returns to Tier 1.
Tier 3: Isolated Execution Subagent (DeepSeek Harness /
dsh
**)**
Local TypeScript CLI agent running against the DeepSeek API (
deepseek-chat
/
deepseek-reasoner
).
Handles dirty work in an isolated environment: reading multiple files, applying diffs, running test suites, and handling iterative failure loops.
Discards intermediate tool output upon task completion, preventing context contamination.
Aux tasks set to:
Why It Works
Preserved Prompt Caching:
Tier 1 never sees thousands of lines of build artifacts, intermediate failed tests, or file dumps. Context stays lean and fully cacheable.
Structured Token Economy:
Expensive reasoning tokens are spent only where needed. Tier 3 burns cheap tokens inside an isolated execution loop, while Tier 2 ensures only high-signal summaries make it back to Tier 1.
Context Isolation:
Failure loops inside the coding subagent do not degrade the orchestrator’s instruction-following ability over long sessions.
Deterministic State Sync:
Lessons learned, architectural patterns, and task outcomes are parsed by
open-code-review
and logged cleanly into Hermes’s persistent memory.
Setup & Workflow
1. Install DeepSeek Harness (
dsh
)
Requires Node.js (\ge 22) and
pnpm
:
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm build
2. Configure
open-code-review
Ensure
open-code-review
is available in your PATH to parse diffs, inspect repo ASTs, and sanitize subagent reports before handoff.
npm install -g open-code-review
# Verify configuration and target repo bindings
open-code-review --help
3. Execution Loop
Hermes
generates the implementation goal and invokes
open-code-review
to extract target context.
dsh
runs headless against the isolated context bundle to apply edits and run verification tests.
open-code-review
validates the patch, trims the run logs, and passes a concise completion report back to
Hermes
.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1w9az27/updated_hermes_with_opencodereview_and/)
