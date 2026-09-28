---
title: "I tried 4 open-source repos for creating a solution for Hermes agents and humans work together"
author: u/Klutzy_Cap8492
date: 2026-09-28
score: 10
comments: 7
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wrdure/i_tried_4_opensource_repos_for_creating_a/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# I tried 4 open-source repos for creating a solution for Hermes agents and humans work together

**Posted by u/Klutzy_Cap8492 on 2026-09-28 · 10 points (100% upvoted) · 7 comments**

So Hermes can already hand off stuff to subagents, right? But what about when it s Hermes, some other coding agent like a human teamate all on the same task? Delegation is only part of the puzzle then.
Say Hermes digs into a bug,and another agent writes the fix. How does everyone see what's going on?And can the reviewer actually see what the agents
did
, not just some 'done' message?
Honestly I think we need shared task info, a clear way for people to review things, and some boundries on what each agent can even touch. I ve been looking at a few self-hostable projects that try to tackle bits of this:
Paperclip:
kinda starts with goals and tasks. It can give work to agents and pull results back for review. They've got adapters for hermes_local and hermes_gateway documented, so it seems like the most straightforward way to get Hermes into a bigger task system.
Vicoa:
is more about agent sessions. It has a task board and lets you follow coding agent work across different devices. Hermes is actually on their supported list. This seems useful if your main headache is just keeping track of work spread across sessions and machines.
AgentConnect:
is built around shared conversations and permissions. Full disclosure, I work on this one. It brings multiple agents into team chats, issues, and PR workflows, with separate access for workspaces, tools, and repos for each agent. It supports ACP-compatible agents, and Hermes
does
have an ACP mode.
OpenHands Agent Canvas:
is more of an interface for coding. It can run external ACP agents, so Hermes
might
work through its ACP mode. I'd definitely test that specific combo before banking on it, though.
For me, just running a bunch of agents and actually working with them as a team are two totally different things. The second one means people need to be in the loopm step in when needed, and understand the work when it's time to review or take over.
if you use Hermes with a team, where do you usually want a person involved?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wrdure/i_tried_4_opensource_repos_for_creating_a/)
