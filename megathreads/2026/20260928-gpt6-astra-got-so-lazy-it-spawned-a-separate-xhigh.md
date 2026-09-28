---
title: "GPT-6 Astra got so lazy it spawned a separate XHigh chat to do its job"
author: u/Xipong
date: 2026-09-28
score: 13
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wrzb0w/gpt6_astra_got_so_lazy_it_spawned_a_separate/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# GPT-6 Astra got so lazy it spawned a separate XHigh chat to do its job

**Posted by u/Xipong on 2026-09-28 · 13 points (93% upvoted) · 3 comments**

I’m actually losing it over this.
I gave
GPT-6 Astra on High
a long research task in Hermes and told it to keep working for ~10 hours, use subagents, prioritize research speed, etc.
Important detail:
/goal
was already enabled
, so Hermes already had a mechanism to keep pushing the same session to continue.
What did Astra do?
Instead of just working and doing 2 waves of subagents, it spent the first ~15 minutes building its own supervisor.
It wrote a Python process that launches Hermes again with something like:
hermes chat --oneshot
--continue Guardian-10h-...
--create-if-missing
--model gpt-6-astra
--reasoning xhigh
Then a
completely separate neighboring Hermes chat appeared in the UI
.
The original Astra gave that chat a handoff basically saying:
You are now the durable coordinator for this 10-hour research mission.
And that new chat started spawning its own subagents.
So the actual flow became:
Astra High
-> writes supervisor
-> supervisor launches another Hermes session
-> Astra XHigh
-> subagents
Yes:
the High model literally created an XHigh version of itself and handed the task to it.
The funniest part is that it originally wanted 4 subagents, but Hermes only allowed 2 at once.
The obvious solution was just:
wave 1: A + B
wave 2: C + D
Instead, it built this entire fucking orchestration layer around the limitation.
And I don’t want to frame this as “wow, amazing autonomous agent”.
This behavior is actually terrible.
I asked the agent to do the task. It basically decided:
“I don’t want to do this myself. I’ll create another agent and make that one do it.”
It even had
/goal
already keeping the original session alive.
But at the same time, this is one of the most bizarre examples of agency I’ve seen.
Usually when Astra misunderstands scope, it does some -100 IQ shit: overtests, edits unrelated files, overengineers a helper, whatever.
This time it misunderstood scope in a
+100 IQ way
.
It used shell access + the Hermes CLI to build a persistence/orchestration feature that Hermes itself doesn’t normally expose like this.
And somehow it actually works. The sibling XHigh chat is alive, its subagents are running, and the supervisor keeps continuing it independently.
So yeah:
Astra didn’t solve the task. It solved the problem of having to solve the task.
I’m impressed by the technical move and completely horrified by the agent behavior.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wrzb0w/gpt6_astra_got_so_lazy_it_spawned_a_separate/)
