---
title: "How do you handle SSRF and prompt injection with Hermes? Sharing my setup, stealing yours"
author: u/_Scorpoon_
date: 2026-09-07
score: 6
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1w8s6c7/how_do_you_handle_ssrf_and_prompt_injection_with/
flair: "Workflow — Daily habits, multi-agent setups, best practices"
---

# How do you handle SSRF and prompt injection with Hermes? Sharing my setup, stealing yours

**Posted by u/_Scorpoon_ on 2026-09-07 · 6 points (100% upvoted) · 4 comments**

Self-hosted Hermes here, fully local models, single-user homelab. Been building up defenses against the usual vectors (prompt injection, SSRF, exfil) and I keep wondering if I'm overengineering this or whether I'm missing something obvious. Curious how the rest of you deal with it.
My setup, briefly:
Hermes runs on a VM with no outbound internet at all, only a few allowed ssh connections inside my lan
All web access goes through one research profile that shells out to a separate container running a fetch/search/crawl server (donsetch). That box has its own route out: a MITM proxy (iron-proxy) that swaps real tokens for dummy ones before anything leaves the house, then a content-inspection proxy (pipelock), then the final egress
Coding workers live in a separate LXC. No keys in the workspace, no env inheritance from the main box. Packages go in by scp and install offline.
What bugs me is that I don't know what the setup actually defends against. The honest list: tokens can't leak through search queries because the real ones get swapped out, workers can't read credentials they never see, egress is chokepointed so exfil has one visible door. But if an injected page tells my agent to read a file I mounted for it and summarize it loudly, the inspection proxy just sees an agent doing its job.
Concrete incidents from the last two weeks that made me uneasy:
My research agent looped for ~8 minutes hammering a failed tool call because the model didn't follow a negative instruction. No injection needed, just a dumb model and a circuit breaker that kept re-arming.
Search engines started 403ing my exit IP while fetch worked fine. Turns out anti-bot fingerprinting doesn't help much against plain IP reputation blocks, or maybe my proxies behind donsetch ruin the fingerprint.
So, my questions:
Who else runs a proxy chain in front of their agent, and did it ever actually catch something? Or is it paperwork?
SSRF: my web tools hard-refuse LAN and loopback, but my agents also have terminal access in a sandbox that shares a bridge with IoT devices. How do you draw this line without ending up in a VLAN per process?
Prompt injection: does anyone have anything beyond "hardened soul files and approvals"? The approval fatigue thing is real, and a hardened soul is still just prose the model may or may not respect.
Any tools worth looking at? Curious what people actually run vs what sounds good on paper. Maybe I can reduce my setup a bit, currently it seems very overengineered to me.
No wrong answers, I'm mostly trying to find out whether my threat model has holes I can't see because I built it myself or I'm just overengineering my whole setup 😅
PS: Some details (setup, incidents) came out of my agent, the post was read, shortened, rewritten at some places by myself. May still have some AI nounces in it.
If post shows as edited, posting from my phone and I fixed the formatting.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1w8s6c7/how_do_you_handle_ssrf_and_prompt_injection_with/)
