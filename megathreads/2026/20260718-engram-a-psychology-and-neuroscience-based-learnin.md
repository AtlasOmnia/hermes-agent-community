---
title: "Engram, a psychology and neuroscience based learning plugin, is now on Hermes (it teaches you, not the agent)"
author: u/No_Skill_8393
date: 2026-07-18
score: 123
comments: 21
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1uzu2ck/engram_a_psychology_and_neuroscience_based/
flair: "ECOSYSTEM — Tools, Plugins, Extensions, Integrations"
---

# Engram, a psychology and neuroscience based learning plugin, is now on Hermes (it teaches you, not the agent)

**Posted by u/No_Skill_8393 on 2026-07-18 · 123 points (96% upvoted) · 21 comments**

Agentic AI made building about 10x faster. Learning didn't get any faster. I noticed I was shipping systems I couldn't re-explain a week later, and it started to bug me. We have a 10x tool for building, so I wanted the equivalent for learning, in the same terminal where the building happens.

That's Engram. It's a tutoring loop grounded in the memory research. And it's aimed at you, not the agent. Hermes already learns for itself; this is the missing half:

\- It breaks a topic into a first-principles concept graph and teaches one node at a time.  
\- It won't explain anything until you've committed to a guess first. Retrieval before instruction is the single best-replicated result in learning science, and also the part every chatbot skips because agreeing with you is easier.  
\- Your recall gets graded by a separate blind assessor that never sees the tutoring conversation. The tutor can't inflate grades on its own teaching.  
\- Reviews are scheduled with FSRS, so they show up right before you'd forget. A few minutes a day.  
\- Wrong models get logged verbatim and re-probed later. Mine has ten entries for transformers alone, which is humbling to read back.

Honest origin story: with an early version I encoded seven concepts, never returned, and lost about half of them right on schedule. Writing the scheduler earns you nothing if you don't come back. So the whole loop got redesigned around returning: two-minute reviews and a "when will you do this" question instead of reminders. No streaks, no XP.

v1.0.5 adds Hermes as the fourth platform, after Claude Code, Codex and OpenCode. It started as a user issue asking for it, and every claim in the install guide was verified against a live Hermes 0.18.2 before shipping. One naming collision doubles as the whole pitch: /learn on Hermes is Hermes' own command, it teaches the agent new skills. Same word, opposite direction. Engram's tutor is /skill learn (or a one-line /study bundle), and /review and /coach are ordinary slash commands on every surface, Telegram gateway included. Your learning state is local JSON, shared across all four tools, so a topic encoded in one gets reviewed in another.

Repo: https://github.com/nagisanzenin/engram — INSTALL-HERMES.md is the verified walkthrough.

I'm the author, so grain of salt. But I've been dogfooding it daily to learn transformer internals and it's the first setup where week-old material actually stays with me.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1uzu2ck/engram_a_psychology_and_neuroscience_based/)

