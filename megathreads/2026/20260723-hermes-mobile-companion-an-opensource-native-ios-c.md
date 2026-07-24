---
title: "Hermes Mobile Companion - an opensource native iOS companion app for Hermes Agent, now in public beta!"
author: u/fan7as7ic_7
date: 2026-07-23
score: 18
comments: 15
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v4cl63/hermes_mobile_companion_an_opensource_native_ios/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# Hermes Mobile Companion - an opensource native iOS companion app for Hermes Agent, now in public beta!

**Posted by u/fan7as7ic_7 on 2026-07-23 · 18 points (93% upvoted) · 15 comments**

I have been using Hermes Agent as a persistent personal operator, but Telegram became limiting once I had several sessions and longer-running work.

Telegram is still good at bringing me back when a new message arrives. What I wanted was a native mobile interface with better session management and support for agent-specific interactions.

I built Hermes Mobile for that:

* browse and resume Hermes sessions
* follow live tool activity
* answer approval and clarify prompts
* receive push notifications when the agent needs attention

Hermes continues to run on your server. The iOS connects directly to your authenticated Hermes instance.

For push delivery, the path is:

Hermes Agent -> local plugin -> stateless gateway -> APNs -> Hermes Mobile

Push notifications contain no conversation text, command details, tool output, files, or credentials. The app fetches the full session directly from your Hermes instance.

The project is open source:  
[https://github.com/goncharik/hermes-mobile](https://reddit.comhttps://github.com/goncharik/hermes-mobile)

Public TestFlight beta:  
[https://testflight.apple.com/join/SyHGvf9n](https://reddit.comhttps://testflight.apple.com/join/SyHGvf9n)

I also wrote a technical postmortem about the push architecture and the integration failures behind it:  
[https://honcharenko.me/posts/hermes-mobile-public-beta-push-notifications/](https://reddit.comhttps://honcharenko.me/posts/hermes-mobile-public-beta-push-notifications/)

I would especially value feedback on setup, notification reliability, approvals, session restoration, and whether this can replace Telegram or terminal check-ins in day-to-day use.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v4cl63/hermes_mobile_companion_an_opensource_native_ios/)

