---
title: "Herald 0.12: the native Android client for Hermes Agent now has a Wear OS app, phone tools, and an agent that can call you"
author: u/PineappleOld5898
date: 2026-10-21
score: 19
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1xapwr1/herald_012_the_native_android_client_for_hermes/
flair: "Showcase"
---

# Herald 0.12: the native Android client for Hermes Agent now has a Wear OS app, phone tools, and an agent that can call you

**Posted by u/PineappleOld5898 on 2026-10-21 · 19 points (100% upvoted) · 3 comments**

Two weeks ago I posted Herald 0.6. Since then there have been six more releases and three new contributors, so here’s another update.
If you missed it: Herald is a native Android app for Hermes Agent. It connects to your hermes dashboard the same way Hermes Desktop’s “Remote gateway” connection does, over LAN, Tailscale or an https address. Nothing is hosted by me.
What’s new since 0.6:
The agent can call you.
When a turn waits on an approval or a question, your phone rings, and when you answer, Hermes is on the line. The agent can also call you itself with a
phone_call_me
tool. Quiet hours keep it from ringing at night.
Wear OS app.
Tap the orb on the watch and talk. It does live voice calls from the wrist, and the watch rings when the agent calls.
Phone tools (opt-in, all off by default).
The agent can use your phone: battery, location, contacts lookup, calendar, Health Connect, alarms, Do Not Disturb, opening links and maps. Each tool has its own switch, and anything that changes the phone asks you first.
Voice:
talk over a spoken reply to cut in, read replies aloud, and use dictation on the phone itself.
Inbox:
the reports from your cron jobs in one feed, with a quiet or notify setting per job and alerts when a run fails.
Threads:
permanent chat slots. “Start fresh” archives the old chat and keeps the slot.
New design:
every screen is redrawn.
Offline chats:
chats you’ve read open without the gateway, from an encrypted saved copy.
Checkpoints:
see what the agent changed on disk and restore it.
Goal, loop and heartbeat:
/goal
,
/loop
and
/heartbeat
shown live above the composer, with pause, resume and clear.
/bg
answers now too.
Starred models
, plus better model search
Files:
a PDF viewer, HEIC/AVIF/TIFF pictures, link previews and inline HTML widgets
Rooms:
attach files to messages
Call Hermes shortcut
on the launcher icon, swipe actions on chats, and a choice of app icon
Privacy is unchanged: Herald only talks to your gateway, apart from a GitHub update check you can turn off. There are no analytics.
Issues, ideas and PRs are welcome, and a star helps if you like it!
GitHub (MIT):
https://github.com/Giton22/herald
APK:
https://github.com/Giton22/herald/releases/latest
Discord:
https://discord.gg/wCtyvQ3KcM

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1xapwr1/herald_012_the_native_android_client_for_hermes/)
