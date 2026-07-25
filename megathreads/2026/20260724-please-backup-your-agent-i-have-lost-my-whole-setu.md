---
title: "Please Backup your Agent! I have lost my whole setup 3 times!"
author: u/HolmeBengt
date: 2026-07-24
score: 8
comments: 21
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v5if6y/please_backup_your_agent_i_have_lost_my_whole/
flair: "Guide — Tutorials, walkthroughs, repeatable how-tos"
---

# Please Backup your Agent! I have lost my whole setup 3 times!

**Posted by u/HolmeBengt on 2026-07-24 · 8 points (70% upvoted) · 21 comments**

I've been deep in Hermes and OpenClaw for a while now. And every time I got something working and set up a real complicated agent and it finally learns how to do that particular thing ... I'd eventually break it. Tweak a setting wrong, mess up the memory, overwrite a good config, have Open Claw or Hermes Break it self.

 Start over from zero. or sit in the silence of youre dead telegram bot!

That happened three times. After the third redo I thought: why am I not backing this up?

So I hacked together a daily cron that tars my \~/.hermes/ into iCloud. Simple, worked great. Except my iCloud filled up fast because I was backing up 2 GB every day — mostly caches and node\_modules I didn't need.

Today I finally built a real backup system that lives up to my agent. I've improved my setup so much since then, but I still relied on cleaning my iCloud folder manually because I was still using the old backup cron job from months ago.

That's when I realized: a "backup script" is easy. A *good* backup system is harder. You need to decide:

\- Where should backups live? (iCloud, USB, server, Dropbox?)

\- What actually needs backing up? (Config/memory/skills/cron — not caches/logs/node\_modules)

\- How often? (Daily? Weekly? Only before risky changes?)

\- How many to keep? (5? 10? 30?)

\- How to test that a backup actually works before you need it?

\- How to restore when things go south?

I ended up writing a protocol, just a list of requirements that I give to my agent. It reads it, builds the script for my specific OS, sets up the cron, tests it, and documents what it did. 

I made this backup protocol completely free and available for everyone to just download it. Here: [https://blog.holmebengt.com/post.html?id=backup-protocol](https://reddit.comhttps://blog.holmebengt.com/post.html?id=backup-protocol)

The screenshots are from the tool showing how the setup process works.

How do you handle Hermes backups?

I hope you take something useful from this and maybe it's just a reminder to build a script that cleans out your backups for you. If you do decide to download my protocol, I'd feel honored to be a part of your Hermes setup.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v5if6y/please_backup_your_agent_i_have_lost_my_whole/)

