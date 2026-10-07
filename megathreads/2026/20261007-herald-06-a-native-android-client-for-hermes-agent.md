---
title: "Herald 0.6: a native Android client for Hermes Agent, now with Bot Mode, multi-bot rooms and live voice calls"
author: u/PineappleOld5898
date: 2026-10-07
score: 17
comments: 5
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wzf126/herald_06_a_native_android_client_for_hermes/
flair: "Showcase"
---

# Herald 0.6: a native Android client for Hermes Agent, now with Bot Mode, multi-bot rooms and live voice calls

**Posted by u/PineappleOld5898 on 2026-10-07 · 17 points (94% upvoted) · 5 comments**

A few days ago I posted Herald, a native Android app for Hermes Agent, because the dashboard's web UI on a phone was painful. Thanks for all the feedback and stars! Since then it has had two big releases, and two contributors have already shipped major features, so here's an update.
If you missed it: Herald connects to your hermes dashboard the same way Hermes Desktop's "Remote gateway" connection does, over LAN, Tailscale or an https address. Nothing is hosted by me.
What's new:
Bot Mode: each profile is a bot with its own chat, model, skills, tools and routines. A "Needs you" list shows which bots are waiting on you.
Rooms: join Hermes's multi-bot rooms, @ mention members and get notified when bots write. (Thanks @ asmodaydoescoding!)
Live voice calls: GPT-Live, as on Desktop. Talk over it to interrupt, and it keeps going with the screen off. (Thanks @ Rockey011!)
Notifications from every chat: approvals and replies now notify for turns started on Desktop or in the CLI too.
Notifications off your network: the optional herald-push plugin sends bot messages over ntfy, end-to-end encrypted.
Several gateways: stay signed in to more than one and switch between them.
Steer a running turn: add a note mid-turn, queue it, or stop and send.
Regenerate replies and edit any earlier prompt
Syntax-highlighted code and TeX math
Share to Herald or straight to a bot
Vault prompts: unlock your password manager, enter codes and save logins from the phone
Projects: filter chats by project folder
Accent colors, a chat background, App lock, better reconnects, and a ~10 MB APK
Privacy is unchanged: it only talks to your gateway, apart from a GitHub update check you can turn off. There are no analytics, and your login is kept in Android's encrypted storage.
It's still early, so expect rough edges. It needs Android 8+, a dashboard login (token-only setups aren't supported yet) and a recent Hermes Agent main branch.
Issues, ideas and PRs are welcome, and a star helps if you like it!
GitHub (MIT):
https://github.com/Giton22/herald
APK:
https://github.com/Giton22/herald/releases/latest

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wzf126/herald_06_a_native_android_client_for_hermes/)
