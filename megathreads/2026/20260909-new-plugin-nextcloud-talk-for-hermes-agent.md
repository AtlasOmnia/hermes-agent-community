---
title: "New plugin: Nextcloud Talk for Hermes Agent"
author: u/vadimsurpin
date: 2026-09-09
score: 6
comments: 1
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wawz3y/new_plugin_nextcloud_talk_for_hermes_agent/
flair: "Showcase — Projects, tools, builds, demos"
---

# New plugin: Nextcloud Talk for Hermes Agent

**Posted by u/vadimsurpin on 2026-09-09 · 6 points (87% upvoted) · 1 comments**

Hey! I've built a platform plugin that turns Nextcloud Talk into a full messaging channel for Hermes Agent — self-hosted, private, no third-party clouds.
Repo:
https://github.com/VadimSurpin/hermes-nextcloud-talk
Install in one line: hermes plugins install VadimSurpin/hermes-nextcloud-talk
What it does:
Full two-way chat — long-poll receive, pairing, sessions/memory/skills all work
Native voice messages — OGG→MP3 via ffmpeg, posted through the attachment API so Talk renders the compact waveform player (like Telegram)
Images / video / files with captions — caption lives on the media itself, one message
Threads & :thumbsup: reactions
Cron delivery — deliver=talk routes scheduled jobs to your Talk room
Fallback path (Files + share-to-chat) if the attachment API is unavailable
Why: Telegram is great, but some of us want an agent channel on our own infrastructure. If you already run Nextcloud, you get a private Hermes channel for free — same UX, zero extra services.
Requirements: Nextcloud + Talk ≥ 17, an app password for the bot user, ffmpeg on the Hermes host.
Docs cover setup, config gotchas (watch the home_channel shape!), and debugging. MIT licensed — issues and PRs welcome. Would love feedback from anyone running Nextcloud + Hermes!

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wawz3y/new_plugin_nextcloud_talk_for_hermes_agent/)
