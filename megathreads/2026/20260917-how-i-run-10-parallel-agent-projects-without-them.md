---
title: "How I run ~10 parallel agent projects without them all reading as "the same task" — the codename + registry system"
author: u/Gryknight9
date: 2026-09-17
score: 6
comments: 2
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wi5el0/how_i_run_10_parallel_agent_projects_without_them/
flair: "Workflow — Daily habits, multi-agent setups, best practices"
---

# How I run ~10 parallel agent projects without them all reading as "the same task" — the codename + registry system

**Posted by u/Gryknight9 on 2026-09-17 · 6 points (75% upvoted) · 2 comments**

I run Hermes-Agent as an assistant that spans a lot of concurrent, long-running work: fleet dashboard redesigns, bare-metal server trims, llama.cpp replacement benchmarks, voice-agent sandboxes, RTL-SDR migrations, profile/pipeline restructures.
On paper that's fine. In practice, two weeks in you have ~15 things half-done and three of them are secretly about the same box. Plain-language labels don't survive that — "the dashboard thing," "the migration," "that ComfyUI cleanup" all collapse into one blob, and someone ends up overwriting another job's backup or restarting the wrong machine.
So I had Hermes start assigning every project an **evocative codename**, and it fixed most of the confusion overnight.
Here's the convention:
- **Codename = adjective + noun, memorable but not precious.** e.g. *GlassAnvil*, *QuickForge*, *QuietShelf*. A pair like QuietRhythm vs QuietShelf is fine *because the nouns differ* — the whole point is the pair reads unambiguously at a glance. The description column carries scope; the codename carries recall.
- **One flat registry table** (`_registry.md`) with exactly one row per operation: `codename | description | start date | status`. Register the row the moment the project starts — *before* any detail work — otherwise the row gets forgotten and you're back to guessing.
- **Dated detail pages** later under `operations/YYYY-MM-DD-<codename-slug>.md`, with YAML frontmatter tying back to the codename. This keeps the registry thin (one line each) while every decision has a permanent home.
Why it actually works as an anti-confusion tool:
The registry has **exactly one row per project**, so two jobs can't silently merge into one entry. When someone reaches for "work on the dashboard," they look up the codename first instead of improvising. Distinct nouns prevent cluster-collapse.
Examples:
Concrete (anonymized) example from last week: three fleet-related jobs ran in parallel — one redesigning a single service page / telemetry card for a host, one migrating an entire monitoring profile from one agent install to another, and one formalizing a ComfyUI setup onto a spare GPU.
Under plain labels ("the redesign," "the migration," "the ComfyUI thing") all three read as the same task; *GlassAnvil*, *Lioness*, and *Cartographer* never collide, and the status field means nobody does "did we finish that?" archaeology — active/completed/blocked is always visible.  (I realize that we are breaking convention with the single worded codenames 'Lioness' and 'Cartographer' but they were applicable so I didn't have it changed..)
Lessons worth repeating:
- **Register before you work.** The convention only holds if the row exists first.  I also enforced a 'only if this project is going to take 10-15 minutes of work or is defined as multi-session', this removes the codename 'LIVINGDRAMA' (the mission to turn off the Living Room lights.)
- **Keep the registry flat and human-readable** — don't let it metastasize into a wiki with cross-links between pages. One table, one row per job. That's the whole trick.
- **Evocative beats descriptive** for the codename; put the detail in the body.
- **Sanitize aggressively**, internal writeups included: strip IPs, host aliases, tokens, phone numbers. Keep the codenames — they're anonymous by construction.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wi5el0/how_i_run_10_parallel_agent_projects_without_them/)
