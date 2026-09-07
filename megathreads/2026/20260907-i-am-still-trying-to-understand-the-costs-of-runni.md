---
title: "I am still trying to understand the costs of running Hermes locally + VPS"
author: u/Usual-Buffalo-1791
date: 2026-09-07
score: 9
comments: 16
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1w907xz/i_am_still_trying_to_understand_the_costs_of/
flair: "Infra / Hosting - VPS, Docker, Coolify, Proxmox, Remote, uptime"
---

# I am still trying to understand the costs of running Hermes locally + VPS

**Posted by u/Usual-Buffalo-1791 on 2026-09-07 · 9 points (84% upvoted) · 16 comments**

My Hermes agent needs to parse through a ton of data and write to a ton of files. The main model I settled on is a 70B and needs ~42 GB VRAM at Q4_K_M. Before discovering Hermes I tried running this model on a local shared M2 Max with 64GB and it crashed.
After reading through posts like these
https://www.reddit.com/r/hermesagent/comments/1w8mbla/whats_your_hermes_setup_on_a_vps_or_server/
https://www.reddit.com/r/hermesagent/comments/1uw1a67/is_it_safe_to_run_hermes_on_a_local_mini_pc/
https://www.reddit.com/r/hermesagent/comments/1uh9dkw/best_way_to_selfhost_hermes_securely_without_a/
https://www.reddit.com/r/hermesagent/comments/1uc7rw5/mac_mlx_megathread_hermes_agent_on_apple_silicon/
and this
https://hostingsift.com/blog/self-hosted-llm-5-dollar-vps-2026
and the VPS megathread
https://www.reddit.com/r/hermesagent/comments/1tw9lbd/the_rhermesagent_vps_megathread_communitycurated/
I am still confused on the best way to host Hermes. Do I put the Hermes agent on an old Mac mini and then have the model on a VPS? For the Hermes agent to do its complex tasks, is it relying on the power of the machine it is on, or the machine the model is on? How bad can I expect the costs of the VPS to go through the roof with usage since I am not using "tokens" exactly because I am hosting everything?
Is it better to just buy an M4 Pro 48GB mac mini solely for this and put Hermes + the model on that?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1w907xz/i_am_still_trying_to_understand_the_costs_of/)
