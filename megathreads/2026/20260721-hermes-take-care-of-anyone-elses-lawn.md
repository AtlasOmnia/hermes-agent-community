---
title: "Hermes take care of anyone else's lawn?!"
author: u/FlyFission
date: 2026-07-21
score: 13
comments: 10
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v2l4ud/hermes_take_care_of_anyone_elses_lawn/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# Hermes take care of anyone else's lawn?!

**Posted by u/FlyFission on 2026-07-21 · 13 points (88% upvoted) · 10 comments**

My locally hosted Palisades zoysia operations dashboard. It combines an approval-gated SQLite journal with a FastAPI backend and an installable vanilla-JS PWA. It tracks the next 14 days, treatments, holds, observations, photos, and time since major applications. Everything runs on my Windows PC and reaches my phone privately through Tailscale, with no public cloud database or internet-facing service

* **Frontend:** Vanilla HTML, CSS, and JavaScript
* **Mobile:** Installable iPhone PWA with safe-area support
* **Backend:** FastAPI and Uvicorn
* **Database:** SQLite with append-only event and audit tables
* **Photos:** Validated local media storage with SHA-256 hashes
* **Hosting:** Windows + WSL, automatically started at login
* **Private access:** Tailscale Serve over HTTPS, tailnet only
* **Offline behavior:** Cached dashboard snapshot, intentionally read-only
* **Verification:** Python API tests plus automated desktop and iPhone-sized browser/accessibility QA

My zoysia grass has never looked better...

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v2l4ud/hermes_take_care_of_anyone_elses_lawn/)

