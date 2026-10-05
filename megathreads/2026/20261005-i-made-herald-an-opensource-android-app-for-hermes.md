---
title: "I made Herald, an open-source Android app for Hermes Agent"
author: u/PineappleOld5898
date: 2026-10-05
score: 16
comments: 9
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wxtvoe/i_made_herald_an_opensource_android_app_for/
flair: "Showcase — Projects, tools, builds, demos"
---

# I made Herald, an open-source Android app for Hermes Agent

**Posted by u/PineappleOld5898 on 2026-10-05 · 16 points (100% upvoted) · 9 comments**

I use
Hermes Agent
a lot, and whenever I was away from my computer the only option was the dashboard's web UI in a mobile browser. It wasn't built for a phone. Navigating between chats was a pain, chatting in it was clunky, and answering an approval meant zooming and scrolling around. I looked for an Android app and couldn't find one that was actually usable.
So I made
Herald
, a native Android client. It connects to the
hermes dashboard
, the same way Hermes Desktop's "Remote gateway" connection does. That works over LAN, Tailscale or an https address, and nothing is hosted by me.
What it does:
Phone assistant:
set Herald as Android's digital assistant, and the assist gesture opens a panel over any app where you can ask Hermes about what's on screen, or circle part of it to ask about just that part. You can use voice or typing, and the screen is only sent if you choose to send it.
Streaming chat with Markdown, reasoning and tool activity, plus one status line for whatever the agent is working on
Approvals, questions and sudo/secret prompts, which you can also answer straight from a notification
Steering a running turn: "Send now", queue the next prompt for after the current task, or stop it. You can also switch model, thinking level and profile per chat
Selecting part of a reply (or of a tool's output) to comment on it or ask about it on the side
Sessions sidebar with search, pin, archive and export, plus filters for chats that are running or need you
Scheduled jobs, insights (cost and tokens by day), and toggles for skills, toolsets and MCP servers
Subagents and background processes shown live, with stop buttons
Voice: dictation and a hands-free voice chat mode
A live notification while a turn runs, and another when it finishes or needs you
And also planned a lot for the future!
It only talks to your gateway. The one exception is a GitHub update check, which you can turn off. No analytics, and your login sits in Android's encrypted storage.
Note:
his is an early pilot, so expect rough edges. It needs Android 8+, a dashboard login (token-only setups aren't supported yet) and a fairly recent Hermes Agent main branch.
Give it a star if you like it and let me know how can I improve!
GitHub (MIT):
https://github.com/Giton22/herald
APK:
https://github.com/Giton22/herald/releases/latest

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wxtvoe/i_made_herald_an_opensource_android_app_for/)
