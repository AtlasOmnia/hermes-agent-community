---
title: "Paused update to v0.22 completely broken updating as a whole"
author: u/thibmaek
date: 2026-10-17
score: 5
comments: 8
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x7e24k/paused_update_to_v022_completely_broken_updating/
flair: "Help — Technical issues, errors, config, debugging"
---

# Paused update to v0.22 completely broken updating as a whole

**Posted by u/thibmaek on 2026-10-17 · 5 points (85% upvoted) · 8 comments**

I accidentally closed my terminal session when I was running `hermes update` on my server. Now no following `hermes update` is able to get it to the latest stable again:
☤ Updating Hermes Agent...

                                                                                              → Fleet: 3 running service(s) across profiles: default                                                                  → Update channel: stable                                                                                                → Latest release: stable v0.22.2 (d923a5eb487a)                                                                         → Fetching updates...
✗ Refusing to move this install to d923a5eb487a: that release predates the gateway runtime these session stores now use. Downgrading is unsupported.                                                                                              /root/.hermes/state.db has gateway runtime history.                                                                     The older release could not delete or prune those sessions.
  To go back anyway: run `hermes gateway stop`, check out the older release with git, then put back each store's copy from before the upgrade:                                                                                                      /root/.hermes: run `hermes` and enter `/snapshot restore 20260720-124204-pre-update`.
  Sessions created since the upgrade are not in that copy.                                                                Guide: https://hermes-agent.nousresearch.com/docs/getting-started/updating#rolling-back-to-an-older-release             No update was applied; your install is unchanged.
In its own, it's clear a version mismatch is happening where the session db is behind/ahead of the version I'm trying to update to. However the instructions here to fix my issue are severely lacking:
* "check out with git" → a tag? a branch? what prior version?
* Running the /snapshot command as listed there (after stopping the gateway) failes with the opaque message 'some files not applied, check the logs' → what logs? where are they? `hermes logs` shows nothing here
It's clear there is still a way to go for Hermes to
properly document
their system + give clear indicators in error messages. Is there somebody here that can help out to see how I mitigate this and again get on a state where I can perform routine upgrades with `hermes update`?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x7e24k/paused_update_to_v022_completely_broken_updating/)
