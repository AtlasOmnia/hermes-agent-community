---
title: "Hound stealth fetch: now bypasses Cloudflare Turnstile. Here's how."
author: u/Opening_Library9560
date: 2026-07-21
score: 9
comments: 1
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v2jv0m/hound_stealth_fetch_now_bypasses_cloudflare/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# Hound stealth fetch: now bypasses Cloudflare Turnstile. Here's how.

**Posted by u/Opening_Library9560 on 2026-07-21 · 9 points (100% upvoted) · 1 comments**

Been shipping anti-bot improvements to Hound's browser pipeline. The short version: it now passes the detection targets that were blocking it before. Want to share the technical approach and get feedback from people running it in production.

The core problem:

Patchright fixes CDP protocol leaks. That's it.

It does NOT touch the JS layer. Detectors read `navigator.webdriver`, canvas hashes, WebGL vendor, UA strings, plugin counts, behavioral telemetry. All untouched.

Cloudflare v9 adds ML scoring on mouse movement on top of that.

Baseline before this work: patchright + channel=chrome passed 25/31 hard targets. The misses were Cloudflare Turnstile and DataDome. 

# What I changed

**1. System Chrome (channel=chrome)**

Biggest single win. Launch the user's installed Chrome, not bundled Chromium.

Real TLS fingerprint (JA4). Bundled Chromium's TLS differs and is detectable.

Falls back to Chromium if Chrome isn't installed.

**2. JS-layer injection**

The hard part. Three standard methods are broken with patchright:

* `add_init_script` \-> uses Routes, breaks DNS
* CDP `addScriptToEvaluateOnNewDocument` \-> needs `Runtime.enable`, patchright patches that out
* `route.fulfill` with inline scripts -> doesn't execute

Working method: `page.goto(url, wait_until='commit')` then immediate `page.evaluate()`.

The commit event fires when the response body starts arriving, before the page's own JS runs. Patches land in patchright's isolated context before the page reads original values.

Patches:

* HeadlessChrome stripped from UA (read real Chrome version, build proper UA string)
* `navigator.webdriver` = `undefined` (patchright sets `false`, which is itself a detection signal)
* Canvas noise on `getImageData` AND `toDataURL` (sannysoft/creepjs hash via `getImageData` directly, so patching only `toDataURL` does nothing)
* Permissions API consistency
* WebGL, plugins, `window.chrome` only on bundled Chromium (system Chrome already has real values, overriding them creates contradictions)

**3. Coherent fingerprint profiles**

4 identities. Platform matches WebGL renderer matches GPU.

Win32 + NVIDIA, Win32 + Intel, Win32 + AMD, MacIntel + Apple.

A mismatch (Win32 platform with Apple GPU) is an instant flag. Detectors cross-reference these.

**4. Human behavior simulation**

CF v9 ML weights behavioral telemetry. Real mouse movement isn't linear.

Quadratic Bezier curves, 15-30 steps, ease-in-out, overshoot + correction wobble. One mouse move, one smooth scroll, 1-2.5s randomized dwell.

\~1.5-2.5s total overhead, only on stealthy + humanize fetches.

The Turnstile solver moves the mouse to the checkbox via Bezier before clicking. That was the difference between passing and failing CanadianInsider (hardest Turnstile target).

**5. Memory**

Browser processes leak RAM across fetches. Three fixes:

* `--renderer-process-limit=1` (one page at a time, saves \~100-200MB)
* `--js-flags=--max-old-space-size=512` (caps V8 heap at 512MB vs 4GB default)
* `Memory.simulatePressureNotification` via CDP after each fetch (triggers Chrome GC, \~5ms)

Also fixed a CDP session leak: sessions were never detached.

# Results

Detection sites (sannysoft, CreepJS, BrowserScan, Pixelscan): all checks pass.

Hard targets:

* CanadianInsider (CF Turnstile, hardest): 200 OK, 78KB
* Medium (CF interstitial): 200 OK, 93KB
* StackOverflow (CF): 200 OK, 1.1MB
* NowSecure (CF challenge): 200 OK, 180KB
* Glassdoor (DataDome): 200 OK, 849KB

Google Search: still 429. Own detection, not Cloudflare. Expected.

Memory: RSS dropped 3.5MB over 5 sequential fetches. No creep.

# Want feedback

If you're running Hound with Hermes, update and try it:

    hound -u

Interested in:

* Sites that still block (what protection?)
* Perf on lower-spec machines (\~2s added per stealthy fetch)
* Memory over long sessions with many fetches
* Canvas noise causing issues in extracted content

GitHub: [https://github.com/dondai1234/master-fetch](https://reddit.comhttps://github.com/dondai1234/master-fetch)

Full benchmark in the README.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v2jv0m/hound_stealth_fetch_now_bypasses_cloudflare/)

