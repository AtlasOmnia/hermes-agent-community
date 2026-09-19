---
title: "I tried 5 ways to give my Hermes agent long-term memory. Only one actually moved work forward"
author: u/SamuelT6
date: 2026-09-19
score: 41
comments: 38
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wjm700/i_tried_5_ways_to_give_my_hermes_agent_longterm/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# I tried 5 ways to give my Hermes agent long-term memory. Only one actually moved work forward

**Posted by u/SamuelT6 on 2026-09-19 · 41 points (78% upvoted) · 38 comments**

My Hermes agent kept losing important context, so I spent the last month testing the usual fixes. Honest ratings:
1. Manual project notes
Worked until I forgot to update them. Two weeks in, they were a history lesson.
2. AGENTS.md
Good for stable things like conventions, stack, and known gotchas. Bad at live project state. Still goes stale.
3. Compression summaries
/compress
keeps the session alive, but it captures what happened, not what still needed to happen. Decisions got lost in the summary.
**4. A memory provider (I tried an MCP memory server)**It remembered everything and did nothing with it. I could ask what we discussed, but it never helped push past a blocker.
5. One giant ongoing session
Expensive, slow, and compression eats the details anyway. It just postpones the problem.
And yes, I know Hermes ships persistent memory, session_search, and skills, and I use all of them. They're excellent at recall. What none of them do is tell me what to do next. That's the gap.
The first setup that actually changed how work moves is this open source repo:
https://github.com/OpenSenseNova/SenseNova-Skills/blob/main/docs/sn-proactive-agent.md
Two pieces:
- Team Harness:
a self-hosted workspace where my Hermes agent works like a teammate instead of a disposable chat session. Tasks, owners, outputs, and blockers are visible instead of living in my head. Runs locally, artifacts saved.
- Proactive Agent:
tracks structured project state and suggests next steps only when there's something worth doing. Accept the suggestion and it resumes the original session.
The key difference: it doesn't just store memory. It uses project state to drive the next action. That's the part none of the other five did.
Honest limits, because this is early software:
- No built-in auth or TLS, so I keep it bound to localhost.
- Proactive Agent is built for Hermes right now. Fine for this sub, less so if you're running something else.
- Setup isn't quick, and Team Harness has no Docker image yet.
- The docs themselves say Team Harness is not a production security boundary.
The bigger idea is what got me: my Hermes agent's state should be a first-class thing. One shared view of where the project actually is, plus something that knows what needs attention and when to stay quiet.
If you found a better cure for my Hermes agent's amnesia, I want to hear it. I'd rather run one solid service than stitch two together.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wjm700/i_tried_5_ways_to_give_my_hermes_agent_longterm/)
