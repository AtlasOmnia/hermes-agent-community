---
title: "We turned our Hermes instance into a project manager living on Rocket.Chat (plugin + write-up)"
author: u/AdIndependent384
date: 2026-07-21
score: 6
comments: 0
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v2ibv6/we_turned_our_hermes_instance_into_a_project/
flair: "USE CASE - Real-world tasks, business uses, personal workflows"
---

# We turned our Hermes instance into a project manager living on Rocket.Chat (plugin + write-up)

**Posted by u/AdIndependent384 on 2026-07-21 · 6 points (80% upvoted) · 0 comments**

We run Hermes on self-hosted [Rocket.Chat](https://reddit.comhttp://Rocket.Chat) and gave it a project-manager profile plus access to YouTrack and our company knowledge base, then wired it into chat with an MIT platform plugin (DDP inbound / REST outbound). The team calls it HalfPM according to our company name :D

What it does on the channel:

* *"where are we on project X?"* → grouped ticket status + what it flags as risk
* *"summary of open tickets by person"* → with clickable links
* *"check tomorrow if Tom updated the contract ticket; if not, DM him and report back here"* → finds the ticket, schedules a cron, delivers the DM (survives a gateway restart)
* *"open a ticket for Peter to order coffee"* → picks the project, maps the name to a YouTrack user, sets sane defaults — all from the knowledge base

Full write-up: how the plugin, profile, thread context and cron delivery fit together — plus an honest security lesson from red-teaming a bot with real access:

[https://halfbitstudio.com/en/ai-virtual-project-manager/](https://reddit.comhttps://halfbitstudio.com/en/ai-virtual-project-manager/)

Plugin's open source if you want the same setup. But you can build something simillar on slack too :)

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v2ibv6/we_turned_our_hermes_instance_into_a_project/)

