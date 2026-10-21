---
title: "Hermes just decrapified my cheap smart tv!"
author: u/frankentriple
date: 2026-10-21
score: 290
comments: 79
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1xamiyp/hermes_just_decrapified_my_cheap_smart_tv/
flair: "Use Cases & Workflows"
---

# Hermes just decrapified my cheap smart tv!

**Posted by u/frankentriple on 2026-10-21 · 290 points (98% upvoted) · 79 comments**

I bought a cheap 75” hisense Amazon fire tv. I like the tv but the menus suck.  loud ads that auto play, it turns on straight to their ad filled dashboard and I have to find the remote to switch to hdmi 1 every single time I use it.
I took a pic of the about page and gave it to Hermes and asked him to find me some firmware that removes the Amazon crap and blocks the ads.
damn if he didn’t walk me through putting it in developer mode then he loaded a custom dashboard and setup blocking for all the amazon crap in my pihole.  like damn.  it’s like a new tv!
edit:  tl;dr from my agent:
TL;DR:
No firmware flash. I used ADB to disable 11 ad/telemetry packages, installed
Projectivy Launcher
as the home screen, and set the TV to resume
HDMI1
. Pi-hole blocks the ad domains. Everything is reversible.
The 5-step version
Enable ADB:
Settings → My Fire TV → About → tap “Fire TV” 7× → Developer Options → ADB debugging → On.
Connect:
adb connect <TV_IP>:5555
Debloat:
disable the 11 Amazon ad/telemetry packages — full list below.
Replace the launcher:
install
Projectivy 4.72
, enable its accessibility service, set
Override current launcher = ON
and
Autostart on boot = Projectivy
.
Default to HDMI1:
switch to HDMI1, then
adb shell settings put secure power_on_launch_mode 1
. Sleep/wake now comes back to HDMI1.
What actually killed the hero ad:
Projectivy. The debloat and Pi-hole blocks alone did not remove it.
Don’t bother with
Custom firmware — signed bootloader, no recovery path, brick risk.
Disabling the Amazon launcher — Fire OS protects it.
Blocking all Amazon domains — you’ll break apps and the store.
Watch out:
Fire OS can turn the Projectivy accessibility service off after a reboot/update. If the Amazon launcher comes back, re-enable that service first — don’t reinstall anything.
edit2:  I just got off work, turned on my tv, and it went straight to hdmi1 and it was amazing.  NO ADS AT ALL!

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1xamiyp/hermes_just_decrapified_my_cheap_smart_tv/)
