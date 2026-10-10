---
title: "state.db got fixed, but who else writes to it?"
author: u/Worldly_Ship4470
date: 2026-10-10
score: 14
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x1enxx/statedb_got_fixed_but_who_else_writes_to_it/
flair: "Help — Technical issues, errors, config, debugging"
---

# state.db got fixed, but who else writes to it?

**Posted by u/Worldly_Ship4470 on 2026-10-10 · 14 points (100% upvoted) · 0 comments**

Read the v0.21.2 notes and two of the causes jumped out: profile gateways writing to the root database, and dashboard handles. Both are second writers.
The reason I care: a learning loop that reads its own sessions and writes skills back is a second writer too, by design. That one the patch can't close.
I keep reef's record store next to my Hermes and the rule there is boring: everything in it was appended by the runtime, one record per exchange and per report, and training reads from that. Compacting retires old records from training but keeps the bodies. It's the same SQLite with WAL that state.db runs on, or Postgres. Same engine, different writer.
What I can't see from outside: where does Hermes write the skills its learning loop produces, and does that path share a writer with state.db? If it does, the patch closed one race and the next one is a design choice.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x1enxx/statedb_got_fixed_but_who_else_writes_to_it/)
