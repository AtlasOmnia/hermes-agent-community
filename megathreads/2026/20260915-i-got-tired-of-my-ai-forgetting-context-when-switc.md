---
title: "I got tired of my AI forgetting context when switching between my work laptop and home PC, so I built a zero-token-overhead shared memory mesh (Open Source)"
author: u/Alarmed_Bit2249
date: 2026-09-15
score: 7
comments: 12
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wfwktq/i_got_tired_of_my_ai_forgetting_context_when/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# I got tired of my AI forgetting context when switching between my work laptop and home PC, so I built a zero-token-overhead shared memory mesh (Open Source)

**Posted by u/Alarmed_Bit2249 on 2026-09-15 · 7 points (73% upvoted) · 12 comments**

Hey everyone,
Like many of you, I jump between multiple setups daily: my work laptop at the office, my workstation rig at home, and a mobile agent on Telegram while on the go.
The biggest friction point? Context amnesia.
Whenever I switch devices, Claude Desktop or Cursor has zero recollection of architectural decisions, ongoing debug sessions, or project quirks I spent hours discussing earlier that day.
Most existing multi-agent memory solutions (like injecting full memory markdown into system prompts) have two fatal flaws:
Token bloat: Dumping memory into the system prompt destroys prompt caching and burns tokens on every casual turn.
Privacy leaks: There's no clean way to guarantee your work secrets don't leak into your personal gaming PC or vice-versa.
So over the past few weeks, I built and open-sourced Hermes Fleet Memory.
What it does differently:
• Zero Ambient Token Overhead (0 tokens): It doesn't bloat your prompt. Memory is exposed as FastMCP tools (fleet_memory_search, fleet_graph_search). The model queries memory strictly on-demand.
• Hardware-Enforced Domain Firewall: Instead of trusting an LLM prompt to "keep work and personal separate", domain isolation is enforced at the host environment level (FLEET_HARD_DOMAIN=work vs personal). Physical boundaries, zero hallucinated leaks.
• Deterministic LWW Conflict Resolution: Avoids fuzzy duplicates. Updates use deterministic UUID5 slots + Unix timestamps (Last-Write-Wins) so editing a config updates in-place instead of creating conflicting memories.
• Native Knowledge Graph Traversal: Extracts entity relations on the fly so your agent can do multi-hop graph queries without running a heavy Neo4j instance.
• Zero VPS Required (For 2 Devices): While it supports full self-hosted VPS mesh with reverse NAT tunnels, regular users can just connect their Work Laptop + Home PC in 2 minutes using Qdrant's permanent $0 Free Tier (1GB RAM).
It works natively with Claude Desktop, Cursor, and Hermes Agent via FastMCP.
The project is 100% open-source under MIT:
👉 GitHub:
https://github.com/amrlazw/hermes-fleet-memory
Would love your brutal feedback, critiques on the architecture, or PRs. If you try the 60-second quickstart, let me know if anything feels clunky!

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wfwktq/i_got_tired_of_my_ai_forgetting_context_when/)
