---
title: "Console 1.2.15: a native Android app for Hermes Agent, redesigned from scratch"
author: u/xP3ta
date: 2026-10-13
score: 7
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x4gtog/console_1215_a_native_android_app_for_hermes/
flair: "Showcase — Projects, tools, builds, demos"
---

# Console 1.2.15: a native Android app for Hermes Agent, redesigned from scratch

**Posted by u/xP3ta on 2026-10-13 · 7 points (100% upvoted) · 3 comments**

Hi all, it's been a while, sorry for disappearing.
The app worked, but it had grown in a messy way and I wasn't happy with it. So instead of piling on more features I rebuilt it from scratch. 1.2.15 is a full redesign, and I focused on making it stable rather than adding new stuff.
The biggest change is what I took out: the Mobile Bridge is gone. Console now talks straight to Hermes Gateway and Dashboard, so there's nothing extra to install on your server. Setup is one command on the machine running Hermes, then you scan a code. If you're upgrading, the app sorts itself out on first launch and the wizard can remove the old bridge for you.
There's also a chat that shows what Hermes is doing in plain words, voice inside the chat, and a Home that never scrolls. Tablet layout isn't great yet, and I'm working on iOS.
I built it mainly for myself and I'm happy with how it turned out. It's open source (GPLv3), no account, no telemetry. If something breaks, tell me, bug reports really help.
- GitHub:
https://github.com/xP3ta/hermes-console
- Site and setup guide:
https://hermes.xpetalab.dev
- Google Play:
https://play.google.com/store/apps/details?id=dev.xpetalab.hermesconsole
Thanks to everyone for the support!

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x4gtog/console_1215_a_native_android_app_for_hermes/)
