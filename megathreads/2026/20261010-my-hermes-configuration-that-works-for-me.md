---
title: "My Hermes Configuration that works for me"
author: u/ct06033
date: 2026-10-10
score: 12
comments: 6
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x24qfp/my_hermes_configuration_that_works_for_me/
flair: "Guide"
---

# My Hermes Configuration that works for me

**Posted by u/ct06033 on 2026-10-10 · 12 points (100% upvoted) · 6 comments**

Ive been seeing so many questions about hermes memory and how to prevent rot that i figured id post all of the modifications i made to hermes that work for me. Ive been on this setup for about 6 months without needing to start fresh which i think is a big win given ive had openclaw rot in weeks.
Hopefully there's enough detail here for others to replicate what i have in their own setups or get some inspiration. If there's improvements to what i have, please share as well!
Disclaimer: a lot of this will sound like AI cause i had Hermes draft it.
## 1. Memory
The core rule: I keep my memory file at the default size which is very tiny but i have this as the first line: *"Memory = only facts relevant to all conversations. Everything else → vault/skills."* I also have a note to research conversations and the web for details before planning or executing any request.
- **Reference vault.** An Obsidian vault with an indexed `reference/` folder: one doc per system (NAS config, network topology, etc). Every agent on my fleet reads from this on demand. It's the shared source of truth.
When memory hits ~75%, a triage pass offloads infra details to obsidian and deletes anything sensitive or stale.
## 2. Skills
Left alone, a skill library rots: overlapping skills, stale commands, dead workflows. So pruning is scheduled, not manual (next section). Two guardrails: deletions must declare what absorbed the content (so you can tell consolidation from junking), and pinned skills are protected from deletion but still patchable when they go stale.
## 3. The dream loop — the piece that ties it together
A nightly cron job, with a deliberately restricted toolset:
Each run it: (1) reviews the day's sessions from the session DB (2) self-critiques — what went wrong, what was repeated work (3) writes a dream log plus a consolidated insights file to the vault (4) audits the skill library — prunes unused skills, flags merge candidates (5) runs memory triage if usage is high.
## 4. Backup:
Daily, a `no_agent` cron job — the script runs directly, no LLM in the loop:
Big thing is i have daily (last 7 days), weekly (last 4 weeks), and monthly images back 6 months. I also instructed hermes to write restore instructions to insert in each backup file so a new instance can self restore.
WAL checkpoint before copying SQLite (so you never snapshot a mid-write database), retention policy, integrity verification after copy, status ping to my ops channel.
With theae things, hermes is pretty much self healing and self maintaining. Hope it helps someone here.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x24qfp/my_hermes_configuration_that_works_for_me/)
