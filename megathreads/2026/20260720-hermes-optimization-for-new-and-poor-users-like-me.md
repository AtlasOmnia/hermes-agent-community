---
title: "Hermes Optimization for new and poor users like me"
author: u/ralphcalls1
date: 2026-07-20
score: 15
comments: 8
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v2759r/hermes_optimization_for_new_and_poor_users_like_me/
flair: "MEMORY &amp; Context — Providers, context window, forgetting issues"
---

# Hermes Optimization for new and poor users like me

**Posted by u/ralphcalls1 on 2026-07-20 · 15 points (100% upvoted) · 8 comments**

If you want optimizations and for your stock hermes to be usuable without additional cost, make your agent read this and optimize your set-up. I built in free schemas for the agent to implement. this will make your agent memory bigger without bloat and added self learning to avoid future mistakes.

    # Hermes Agent Optimization Guide
    
    
    > 
    *The playbook for taking a stock Hermes from "it works" to "it watches itself, fixes itself, and proves it's improving."*
    
    
    ---
    
    
    ## The Elevator Pitch
    
    
    Stock Hermes is blind. No telemetry. No auto-fixes. No cross-profile awareness. No way to know if a model change actually helps.
    
    
    This guide fixes that in 5 phases — ordered by impact-to-effort ratio. Each phase is a self-contained playbook your Hermes agent can execute against any system.
    
    
    ---
    
    
    ## Architecture Overview
    
    
    ```
    ┌────────────────────────────────────────────────────────────┐
    │                    Stock Hermes                              │
    │  [Memory: flat 5KB file] [Skills: ~85 enabled] [No guard]  │
    └────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴──────────┐
                    ▼                    ▼
    ┌──────────────────────┐  ┌──────────────────────────┐
    │   Phase 1-2: Core     │  │   Phase 3-5: Intelligence │
    │   (30 min, $0)       │  │   (2 hrs, ~$0.01/week)    │
    ├──────────────────────┤  ├──────────────────────────┤
    │ • Kill unused skills  │  │ • Vector memory (140x    │
    │ • Enable guardrails   │  │   faster recall)          │
    │ • Compress context    │  │ • Auto-remediation (self- │
    │ • Lock cron costs     │  │   healing infrastructure) │
    │ • Archive memory      │  │ • Multi-profile fleet mgmt│
    └──────────────────────┘  │ • Champion/Challenger     │
                              │   (weekly model eval)      │
                              └──────────────────────────┘
    ```
    
    
    ---
    
    
    ## Phase 1: Stop the Leaks
    
    
    ### 1.1 Skills: Your Biggest Lever
    
    
    **The problem:**
     Every enabled skill adds tokens to your system prompt on EVERY turn. Stock enables ~85. Most are never used.
    
    
    **Agent: discover your system**
    ```bash
    # Count active vs disabled
    hermes skills list | grep -c enabled
    hermes skills list | grep -c disabled
    ```
    
    
    **Agent: decide which to kill**
    - Keep only skills actively loaded in the last 30 days
    - Check `~/.hermes/profiles/<profile>/config.yaml` for the disabled list
    - Target: 15-25 active skills
    
    
    **Agent: implement**
    ```yaml
    # Add to config.yaml under skills:
    skills:
      disabled:
        # Keep only: plan, plan-and-build, test-driven-development,
        # hermes-cost-optimization, hermes-model-strategy,
        # obsidian, doc-coauthoring, cron-data-fetch
        # Disable everything else
        - claude-code
        - codex
        - opencode
        - spotify
        - notion
        - songwriting
        - pixel-art
        - gif-search
        # ... ~65 more
    ```
    
    
    **Verify:**
     Restart session. System prompt should be visibly shorter.
    
    
    ---
    
    
    ### 1.2 Enable Guardrails
    
    
    **The problem:**
     `tool_loop_guardrails` is disabled by default. An agent can loop 50+ times on a failing tool call silently.
    
    
    **Agent: discover**
    ```bash
    grep "hard_stop_enabled" ~/.hermes/profiles/*/config.yaml
    ```
    
    
    **Agent: implement across ALL profiles**
    ```yaml
    tool_loop_guardrails:
      warnings_enabled: true
      hard_stop_enabled: true
      warn_after:
        exact_failure: 2
        same_tool_failure: 3
        idempotent_no_progress: 2
      hard_stop_after:
        exact_failure: 5
        same_tool_failure: 8
        idempotent_no_progress: 5
    ```
    
    
    **Verify:**
     Intentionally cause a tool failure. It should warn on attempt 2-3, halt by attempt 5-8.
    
    
    ---
    
    
    ### 1.3 Cap Cron Costs
    
    
    **The problem:**
     Cron jobs have no max_turn limit. A stuck job burns 150+ API calls overnight.
    
    
    **Agent: discover**
    ```bash
    grep "max_turns" ~/.hermes/profiles/*/config.yaml
    ```
    
    
    **Agent: implement**
    ```yaml
    cron:
      max_turns: 20
    ```
    
    
    For any cron job that can run without an LLM, add `no_agent: true` — zero token cost.
    
    
    **Verify:**
     Check cron job output files — they should complete faster.
    
    
    ---
    
    
    ### 1.4 Model Tiering
    
    
    **The problem:**
     Your $0.14/M primary model handles vision, compression, and session search. Switch these to a free/cheap aux model.
    
    
    **Agent: discover**
    ```yaml
    # Check what your config.yaml says for auxiliary:
    grep -A2 "auxiliary:" ~/.hermes/profiles/*/config.yaml
    ```
    
    
    **Agent: implement**
    ```yaml
    auxiliary:
      vision:
        provider: google        # Or whichever free tier you have
        model: gemini-3.1-flash-lite
      compression:
        provider: google
        model: gemini-3.1-flash-lite
      session_search:
        provider: google
        model: gemini-3.1-flash-lite
    ```
    
    
    Don't have a Google key? Use any provider that offers a cheap/free tier. The goal is to move non-reasoning tasks off your primary model.
    
    
    **Verify:**
     Run `hermes insights` before and after. Vision/compression costs should drop to near zero.
    
    
    ---
    
    
    ### 1.5 Memory Archive
    
    
    **The problem:**
     MEMORY.md has a 5KB cap. Every character loads every turn. No auto-archival.
    
    
    **Agent: discover**
    ```bash
    wc -c ~/.hermes/profiles/*/memories/MEMORY.md 2>/dev/null
    wc -c ~/.hermes/profiles/*/memories/USER.md 2>/dev/null
    ```
    
    
    **Agent: implement the archive pattern**
    
    
    For memory over 2,500 chars:
    1. Identify entries that are stable facts (infrastructure, historical tasks, one-time fixes)
    2. Move them to `archive/memory_reference.md`
    3. Replace with a pointer: `"Archived → see archive/memory_reference.md for: [topics]"`
    4. Compress remaining entries — shorter phrasing, merge duplicates
    
    
    **Verify:**
     Memory usage should drop below 60%.
    
    
    ---
    
    
    ## Phase 2: Give It Eyes
    
    
    ### 2.1 Guardrail Telemetry
    
    
    **The problem:**
     Guardrails are completely silent. You have no idea how often the agent nearly breaks something.
    
    
    **Agent: build the scanner**
    
    
    Create a script that:
    1. Scans all `errors.log*` files for `[Tool loop warning:` and `[Tool loop hard stop:` patterns
    2. Scans all `agent.log*` files for `Tool X returned error` patterns
    3. Scans all `agent.log*` files for `API call #N:` to track usage
    4. Outputs a structured cross-profile report
    
    
    ```python
    # Pattern reference for the scanner:
    GUARDRAIL_RE = r"
    \[
    Tool loop warning|Tool loop hard stop:\s*(?P<code>\w+);\s*count=(?P<count>\d+);"
    TOOL_ERROR_RE = r"Tool\s+(?P<tool>\S+)\s+returned error"
    API_CALL_RE = r"API call #\d+: model=(?P<model>\S+) in=(?P<tokens_in>\d+)"
    ```
    
    
    **Agent: schedule it**
    ```yaml
    # Cron: daily at 9am
    script: guardrail_telemetry.py
    no_agent: true
    deliver: origin
    ```
    
    
    **Verify:**
     Next morning, you get a report showing guardrails, errors, and API usage per profile.
    
    
    ---
    
    
    ### 2.2 Cross-Profile Audit
    
    
    **The problem:**
     Profiles are isolated. Config drifts. One profile has Tavily key, another doesn't. Hard stops enabled on one, disabled on another.
    
    
    **Agent: discover**
    ```bash
    # Audit every profile
    for p in ~/.hermes/profiles/*/; do
      name=$(basename "$p")
      echo "$name"
      echo "  Model:     $(grep 'default:' "$p/config.yaml" | awk '{print $NF}')"
      echo "  Extract:   $(grep 'extract_backend' "$p/config.yaml" | awk '{print $NF}')"
      echo "  HardStop:  $(grep 'hard_stop_enabled' "$p/config.yaml" | awk '{print $NF}')"
      echo "  TavilyKey: $(grep -qi 'TAVILY_API_KEY' "$p/.env" && echo YES || echo NO)"
    done
    ```
    
    
    **Agent: fix**
    - Profile has `extract_backend: tavily` but no Tavily key? Add the key from the profile that has it.
    - Profile has different guardrail settings? Standardize.
    - Profile has no session_reset? Add it.
    
    
    **Agent: verify**
     — Re-run the audit. All profiles should match.
    
    
    ---
    
    
    ## Phase 3: Give It a Brain
    
    
    ### 3.1 Vector Memory
    
    
    **The problem:**
     Flat memory means every conversation is a blank slate. The agent can't recall what you discussed 3 weeks ago without burning tokens on session_search scrolls.
    
    
    **The insight:**
     
    *Memory should be searchable by meaning, not by file.*
    
    
    **Agent: build the index**
    
    
    ```bash
    pip install sentence-transformers numpy
    ```
    
    
    Directory structure:
    ```
    memory/vector_index/
    ├── search.py           # CLI: search "your query" --top-k 3
    ├── entries.json        # Session metadata (140 entries = 50KB)
    ├── embeddings.npy      # 384-dim vectors
    └── index.json          # Metadata
    ```
    
    
    **Agent: index existing sessions**
    
    
    Query `state.db` for all non-cron sessions with >5 messages. For each:
    1. Get the first user message as a summary
    2. Generate a 384-dim embedding via all-MiniLM-L6-v2
    3. Append to `entries.json + embeddings.npy`
    
    
    **Agent: implement auto-search behavior**
    
    
    Whenever the user mentions a known topic (project name, profile name, technical concept):
    1. Search vector index: `python3 search.py search "topic" --top-k 3`
    2. If score > 0.3, use `session_search()` to pull full context
    3. Incorporate findings into the response naturally
    
    
    **Agent: schedule auto-indexing**
    
    
    ```yaml
    # Cron: daily at 4am
    script: vector_auto_index.py
    no_agent: true
    ```
    
    
    The script queries state.db for sessions NOT in entries.json, indexes them. Should take <1s.
    
    
    **Verify:**
     Ask "remember that thing we built for X?" The agent should recall it instantly.
    
    
    ---
    
    
    ### 3.2 Context Compression Strategy
    
    
    **The problem:**
     Long sessions bloat context. Stock compression treats all turns equally.
    
    
    **The insight:**
     
    *Not all history is equal.*
    
    
    **Agent: implement custom strategy**
    - Latest turn: FULL
    - Previous 5 turns: Summarize to key decisions
    - Older turns: ≤1K "Previously" block — just enough to avoid contradicting past decisions
    - Strip DM closing lines, keep ~250 chars core narrative
    
    
    **Verify:**
     After 50+ turn conversations, token usage should grow sub-linearly.
    
    
    ---
    
    
    ## Phase 4: Give It Hands
    
    
    ### 4.1 Auto-Remediation
    
    
    **The problem:**
     Issues accumulate silently. SearXNG goes down, logs fill disk, cron jobs fail, API keys expire. You notice when something breaks, not before.
    
    
    **The insight:**
     
    *The agent that manages the system should also heal it.*
    
    
    **Agent: build the auto-remediation script**
    
    
    The script runs 4 phases:
    
    
    | Phase | What | How |
    |---|---|---|
    | 
    **Scan**
     | Collect guardrails, errors, API calls per profile | Parse log files |
    | 
    **Diagnose**
     | Check SearXNG, API keys, disk, gateway, vector index | Port check, env check, df, ss |
    | 
    **Fix**
     | Attempt auto-remediation for each issue | Start docker, copy keys, gzip logs, restart gateway |
    | 
    **Report**
     | Structured digest of issues + fixes | Formatted text |
    
    
    **Agent: implement the fix matrix**
    
    
    | Issue | Detection | Auto-Fix |
    |---|---|---|
    | SearXNG down | Port 8888 unreachable | `docker start searxng` or flag |
    | Missing API key | `extract_backend` set but no key in `.env` | Copy key from main profile |
    | Log pressure | Total logs >500MB | Gzip oldest rotated logs |
    | Gateway down | Port 8642 not listening | `hermes gateway restart` |
    | Vector stale | `state.db` has newer sessions than index | Run auto-index |
    
    
    **Agent: schedule it**
    ```yaml
    # Cron: daily at 5am
    script: auto_remediation.py
    no_agent: true
    deliver: origin
    ```
    
    
    **Verify:**
     Next morning, you get a report. Issues found, fixes attempted, success/failure status.
    
    
    ---
    
    
    ## Phase 5: Give It Proof
    
    
    ### 5.1 Champion/Challenger System
    
    
    **The problem:**
     How do you know if a model change actually helps? Gut feel. "Feels smarter." No data.
    
    
    **The insight:**
     
    *Run the same challenges against both models. Score them. Compare.*
    
    
    **Agent: build the benchmark**
    
    
    **Phase A — System Health**
     ($0, tests infrastructure):
    1. 
    **File I/O**
    : Write content → read back → verify exact match
    2. 
    **Web Search**
    : SearXNG responds with relevant results for a known query
    3. 
    **Code Execution**
    : Bubble sort written + executed, verify correct output
    4. 
    **Data Reasoning**
    : JSON transformation (averages, ranking)
    
    
    **Phase B — Model Comparison**
     (~$0.001/week, tests the LLM itself):
    1. 
    **Code Generation**
    : "Write merge_sorted(a,b)" → execute and verify
    2. 
    **Factual Recall**
    : "Boiling point of water?" → exact answer match
    3. 
    **JSON Formatting**
    : Return structured JSON → validate keys and values
    4. 
    **Instruction Following**
    : "List exactly 5 items" → count the lines
    5. 
    **Arithmetic**
    : "15 × 37" → exact number
    
    
    Each prompt is sent to BOTH models via direct API call. Responses are scored programmatically — no LLM judges needed.
    
    
    **Agent: schedule it**
    ```yaml
    # Cron: Sunday 1am
    script: champion_challenger.py
    no_agent: true
    deliver: origin
    ```
    
    
    **Agent: score and report**
    
    
    ```
    ⚔️ Champion vs Challenger
    
    
    DeepSeek V4 Flash (80/100) vs Gemini 3.5 Flash (60/100)
    
    
    Task              | Champion | Challenger | Winner
    ------------------|----------|------------|--------
    Code Generation   | ❌ 0     | ❌ 0       | Tie
    Factual Recall    | ✅ 100   | ✅ 100     | Tie
    JSON Formatting   | ✅ 100   | ❌ 0       | 🏆 Champion
    Instruction       | ✅ 100   | ✅ 100     | Tie
    Arithmetic        | ✅ 100   | ✅ 100     | Tie
    ------------------|----------|------------|--------
    Average           | 80.0     | 60.0       | 🏆 Champion
    Verdict           |          |            | No change needed
    ```
    
    
    **Historical trend:**
    
    
    ```
    Date       | System | Champion | Challenger
    -----------|--------|----------|------------
    2026-07-07 | 75     | —        | —
    2026-07-14 | 75     | —        | —
    2026-07-21 | 75     | 80       | 60
    ```
    
    
    **Verify:**
     Each Sunday, you get a report showing whether your system is healthier than last week and which model performs better.
    
    
    ---
    
    
    ## The Complete Transformation
    
    
    | Metric | Before | After |
    |---|---|---|
    | Active skills | ~85 | ~17 |
    | Memory usage | 99% full | ~50% (room to grow) |
    | Session recall | Manual scroll | Vector search, 0.01s |
    | Guardrail visibility | Silent | Daily telemetry report |
    | Auto-fixes | None | Daily at 5am |
    | Model evaluation | Gut feel | Weekly champion/challenger |
    | Config consistency | Drifted per profile | Verified across all |
    | Cron cost | Unknown | ~$0.004/month |
    | Monthly token cost | $15-30/profile | $2-5/profile |
    
    
    ---
    
    
    ## Mistakes We Made (So You Don't Have To)
    
    
    **1. The vector index was stuck at 40 sessions for 3 days**
    The cron prompt hardcoded `created_at` but the actual DB column is `started_at`. Every run silently failed. The cron "succeeded" (exit code 0) but did nothing. 
    **Lesson:**
     Use `no_agent` scripts for predictable tasks, not LLM prompts.
    
    
    **2. SearXNG was down for weeks without anyone noticing**
    Config said `backend: searxng` but Docker wasn't running. Every web_search failed silently. The agent retried 3-5 times → guardrail warnings → no one checked. 
    **Lesson:**
     Build telemetry before you need it.
    
    
    **3. Yuki-nagato had 56 web_extract failures from a missing API key**
    Config said `extract_backend: tavily` but the .env had no Tavily key. Every extraction call fell back to SearXNG → failed → retried → guardrail. 
    **Lesson:**
     Audit all profiles, not just the main one.
    
    
    **4. The archive pattern saves 2,000+ chars but creates a blind spot**
    Archived info (swap config, Power Apps fixes) is no longer in memory. The agent can't surface it unprompted. 
    **Fix:**
     When a user asks about services or integrations, proactively read `archive/memory_reference.md` before answering "not found."
    
    
    **5. Zero hard stops ever fired across 6 profiles**
    Our guardrails are tuned as early warnings (2 warnings → 5 hard stop), which means they warn but rarely halt. This is 
    *by design*
     — we'd rather the agent complete its task with guidance than get blocked. But it means guardrails are advisory, not enforced.
    
    
    ---
    
    
    ## Quick Start (For Impatient Agents)
    
    
    **Your human just gave you this file. Here's your 10-minute quick start:**
    
    
    1. 
    **Phase 1.1**
    : Count active skills. If >30, disable aggressively.
    2. 
    **Phase 1.2**
    : Check `hard_stop_enabled`. If false, enable it.
    3. 
    **Phase 1.3**
    : Check `cron.max_turns`. If absent, set to 20.
    4. 
    **Phase 1.5**
    : Check `memories/MEMORY.md` size. If >2,500 chars, archive.
    5. 
    **Phase 2.2**
    : Run the cross-profile audit. Fix any mismatches.
    
    
    That's 10 minutes for 70% of the benefit. Everything else is incremental.
    
    
    ---
    
    
    > 
    **Author:**
     Irisu Fuyumi
    > 
    **Based on:**
     Hermes Agent by Nous Research
    > 
    **This file is designed for dual consumption:**
     humans read the story, agents execute the playbook.
    > 
    > 
    *Last updated: 2026-07-21*

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v2759r/hermes_optimization_for_new_and_poor_users_like_me/)

