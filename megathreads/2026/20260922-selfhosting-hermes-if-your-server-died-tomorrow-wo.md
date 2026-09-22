---
title: "Self-hosting Hermes: if your server died tomorrow, would your agent's memory survive?"
author: u/AjitSpliceRun
date: 2026-09-22
score: 25
comments: 103
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wmhiea/selfhosting_hermes_if_your_server_died_tomorrow/
flair: "Infra / Hosting - VPS, Docker, Coolify, Proxmox, Remote, uptime"
---

# Self-hosting Hermes: if your server died tomorrow, would your agent's memory survive?

**Posted by u/AjitSpliceRun on 2026-09-22 · 25 points (90% upvoted) · 103 comments**

Genuine question for anyone running Hermes on their own VPS or home server: what happens if the box just disappears tomorrow? Disk failure, provider cancels you, billing mishap, whatever.
The model weights are replaceable, that's just a re-download. What I'm thinking about is everything else: the memory files, the system prompt tweaks, the tool configs, all the context the agent has built up over weeks. That part you can't pull from Hugging Face again.
So what's your plan?
Daily offsite backup of the memory/config? To where, and how do you automate it?
Everything in git and you'd just redeploy?
Nothing yet and this post is mildly stressful to read?
And honestly: has anyone actually tested restoring an agent onto a fresh box and confirmed it still remembers everything? Or is the backup a "hope I never need it" thing?
Curious to hear real setups, messy ones included.
UPDATE: this thread went better than I expected. So here is a proper summary: every backup style people shared, its weak spot, and the easy fix for it. Plus the official hermes way, and my own setup checked honestly against all this.
Style 1: Provider snapshots
(hetzner backups, VPS images)
How it works: your provider takes a copy of the whole server automatically.
Weak spot: the snapshot lives in the same account as the server. Account locked or billing problem means server and backup gone together.
Easy fix: keep one copy anywhere outside that provider. Even a weekly download to your own PC closes this hole.
Style 2: Git repo
(config, skills, memories pushed to github, some agents even commit their own state)
How it works: everything important is version controlled, you can see every change.
Weak spot: the session database is a sqlite file, and copying it while the agent is running can give you a file that won't open later. Also most people only push config and skills, so the memories never make it in.
Easy fix: before the git push, let
hermes backup
make a clean copy of the databases and commit that. Then the repo really has everything.
Style 3: "Just ask your agent"
(agent sets up its own backups and writes its own restore instructions)
How it works: the agent knows its own setup best, so it builds the backup and documents the restore.
Weak spot: the instructions are untested. They always look right until you follow them on an empty machine.
Easy fix: tell the agent to spin up a fresh instance and follow its own readme once. It wrote the instructions, let it prove them.
Style 4: Second machine at home
(NAS, old PC, icloud or gdrive folder)
How it works: a copy syncs to another machine you own.
Weak spot: if both machines are in the same room, one fire or one power surge takes both. And if the copy is manual, it quietly stops happening after week 2.
Easy fix: add one cloud copy (any provider, any bucket) and put the copying on a cron so no human has to remember it.
Style 5: Proxmox to PBS
How it works: full VM snapshots, several times a day, very consistent.
Weak spot: only as safe as where the PBS box sits. Same rack means same disaster.
Easy fix: PBS supports remote sync, push the snapshots to a second PBS somewhere else.
None of these are wrong. Every one of them survives some disasters. The difference is only how many.
Best advice from the comments so far (updating as promised):
u/Don_Crespo
:
"Back up the state, not the server image."
Config and skills in git, the state directory encrypted offsite with restic or borg, and when you test a restore dont just check the files came back, check that a session, a scheduled job and a tool integration actually work. Cleanest way anyone has put it.
u/Technical-Ant-2866
has his agent open a
pull request
every time a skill or memory changes, he reviews and it auto merges. So the backup reviews itself before it becomes permanent. He has recovered twice with this.
u/Rachel_talks
:
separate the irreplaceable from the regenerable.
Your memories and corrections are kilobytes and gone forever if lost, the 40GB VM image is mostly a re-downloadable OS. Back up the kilobytes often and offsite, snapshot the big stuff weekly, stop treating the image like its the precious part.
The official hermes way (some may not know this exists now)
hermes backup
makes a zip of your config, skills, sessions and data. It copies the sqlite databases the safe way, so the backup is clean even while the agent is running.
hermes import <zipfile>
restores it. Docs say stop the gateway first.
One warning: the zip contains your .env, which means all your provider API keys are inside it. Wherever you keep that zip, keep it like you keep your keys.
So the simplest solid plan is: cron runs
hermes backup
daily, the zip goes somewhere offsite, and you run
hermes import
once on a clean box so you know it works. That's the whole plan.
One catch found in the comments: helper containers. hermes backup only covers the hermes folder itself. If you run hindsight for memory, its postgres db lives in its own container and needs its own daily dump, or your restored agent comes back with empty memories. camoufox and similar are fine, those are re downloadable.
How I do it (I run hermes agent servers for clients, so this part is my job)
Every night a full copy of the agent's data folder is taken, encrypted before it leaves the machine, and sent to storage on a completely different provider. The restore has a strict health check, a restore only counts as done when the agent actually comes back healthy, not just when the container starts.
And a small confession.
While writing this post I went and rechecked my own setup looking for the same weak spots I listed above:
The sqlite risk from style 2? We had it too in the beginning. Turns out my team already fixed it earlier this month, the backup now takes a clean database copy the safe way before archiving, same idea as the official
hermes backup
.
Restore testing? Also covered better than I remembered. There is a nightly job that actually restores the newest backup and checks the agent's database opens clean, including the search index, because a "restored" agent with broken memory is the worst surprise.
One thing genuinely missing: my clients can't download their own backup copy themselves yet. This thread made it clear people want to hold their own copy, and they're right.
That one is now on my list for real.
So I asked this question partly to check myself, and I still walked away with homework. Worth it.
If you take one thing from this thread:
whichever style you use, it's fine. Just do the restore test once. Almost everyone here has backups, and only two people had ever actually restored one. That one test is the difference between a backup and a hope.
One safety note for that test
, from
u/maritime_sh
in the comments: disable outbound messaging and scheduled jobs on the restored copy first. It carries the same tokens and crons as your live agent, so otherwise your test copy wakes up as a second live agent, answering your messages and firing your jobs in duplicate while you are busy checking if its memory survived.
We have a strong Hermes community here, so I'm sure more setups will keep coming in the comments. I'll keep updating this post as they do, so it stays a useful reference instead of going stale.
And if I got anything wrong above, tell me and I'll correct it. Rather have an accurate thread than a perfect looking one.
once again thanks to all the beautiful people for correcting and indirectly letting me know my mistakes...
Will keep checking the comments.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wmhiea/selfhosting_hermes_if_your_server_died_tomorrow/)
