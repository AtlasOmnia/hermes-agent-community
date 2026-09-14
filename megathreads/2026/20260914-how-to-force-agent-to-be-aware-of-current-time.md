---
title: "How to force agent to be aware of current time?"
author: u/alex7912
date: 2026-09-14
score: 13
comments: 16
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wf5maz/how_to_force_agent_to_be_aware_of_current_time/
flair: "Help — Technical issues, errors, config, debugging"
---

# How to force agent to be aware of current time?

**Posted by u/alex7912 on 2026-09-14 · 13 points (93% upvoted) · 16 comments**

I'm trying to set up my AI assistant to manage my tasks and projects via telegram. But I encountered a stupid problem: it almost always mistakes time and date. It offers solutions, promised no mistakes anymore, but still has this problem. Last his excuse was: "I have the rule (requesting the time via execute_code before every time-dependent response), but I failed to execute it properly: I based some answers on a timestamp retrieved several turns earlier instead of making a new call. * The second reason I overlooked: the session underwent context compression and an extended pause. The last activity was on August 29, but today is already September 13. I kept treating August 29 as the current day based on outdated tool outputs, even though the session metadata shows September 13.". So what's wrong, how to fix it properly?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wf5maz/how_to_force_agent_to_be_aware_of_current_time/)
