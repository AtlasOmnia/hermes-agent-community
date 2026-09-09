---
title: "Looking for people who actually self-host Hermes"
author: u/LeatherEfficient9434
date: 2026-09-09
score: 35
comments: 86
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wavno5/looking_for_people_who_actually_selfhost_hermes/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# Looking for people who actually self-host Hermes

**Posted by u/LeatherEfficient9434 on 2026-09-09 · 35 points (84% upvoted) · 86 comments**

I spent about two and a half months on Hermes and it already got me far. I started by running Hermes locally and connecting it to Obsidian. Then I hosted it on a Hetzner VPS with Coolify (Docker), so it runs 24/7. I only use one gateway: Telegram. Grok 4.6 is my main model. I’ve updated the stack myself.
In Obsidian I keep a Hermes learning library plus a learning history: newest at the top, what I learned and what I failed at, with tables so it doesn’t turn into a random pile of notes. Hermes writes into that vault with me. I gave Hermes access to the Hetzner server, so if I tell it what’s wrong it can fix stuff on the VPS. I also set up encrypted recovery backups from Hetzner to OneDrive with rclone, local memory on the server, and cron jobs.
I still feel behind because I want to build my own OS with a proper foundation. That means strict rules it has to follow, like not letting Hermes update itself in a way that crashes the whole thing, and not letting Hermes fill the disk so I can’t even chat it to fix it. After that happened I made a cron that pings me when the disk is around 85% full. I haven’t made a single dollar from this yet and I don’t know how to offer it to people or clients. There’s a lot I’ve learned that I can share, and a lot I haven’t. I’m looking for a peer to work together, connect, and exchange ideas.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wavno5/looking_for_people_who_actually_selfhost_hermes/)
