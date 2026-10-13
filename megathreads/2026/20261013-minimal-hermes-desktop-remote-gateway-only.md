---
title: "Minimal Hermes Desktop - Remote Gateway Only"
author: u/Timus0708
date: 2026-10-13
score: 10
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x4384v/minimal_hermes_desktop_remote_gateway_only/
flair: "Guide — Tutorials, walkthroughs, repeatable how-tos"
---

# Minimal Hermes Desktop - Remote Gateway Only

**Posted by u/Timus0708 on 2026-10-13 · 10 points (100% upvoted) · 4 comments**

I have been looking for a way to install hermes with minimal memory footprint, and i guess I found one..
Problem :
Hermes Desktop own windows consumes
~8.7 GB of disk space
, even though I only need it to connect to a remote gateway.
Installs desktop/web dependencies, creates multiple Python environments, and bundles toolchains I already have installed.
This is massive, unnecessary overhead for a lightweight remote-gateway client.
Solution :
While the hemes installer exe has full agent/python/driver setup.. the git repo has desktop app decoupled..
This means we can install only ui without local agent installtion by building it from source and select the remote gateway on first launch.
----------------------------------------
-----------
Steps:
-----------
Install Git, Node.js (supported version), and npm.
Clone and build:
git clone --depth 1
https://github.com/NousResearch/hermes-agent.git
C:\hsb
cd C:\hsb
npm install
cd apps\desktop
npm run pack
Launch Hermes.exe from apps\desktop\release\win-unpacked\.
On first launch, choose
Remote Gateway
instead of local installation.
Enter http://<gateway-host>:9119, test the connection, sign in, and apply.
Important:
Ensure %LOCALAPPDATA%\hermes\hermes-agent does not already exist, or the app may detect an existing local installation.
----------------------------------------
This keeps the Windows desktop app focused on connecting to your remote Hermes gateway,
The memory disk imusage with this setup is <500mb
Which is huge and it dosent constantly monitor and install driver for browser-use, computer-use and others.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x4384v/minimal_hermes_desktop_remote_gateway_only/)
