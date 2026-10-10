---
title: "67 Hermes Agent PRs merged in the last 24 hours — through October 9, 2026, 1:30 PM ET"
author: u/Jonathan_Rivera
date: 2026-10-10
score: 7
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x1x4lj/67_hermes_agent_prs_merged_in_the_last_24_hours/
flair: "News & Releases"
---

# 67 Hermes Agent PRs merged in the last 24 hours — through October 9, 2026, 1:30 PM ET

**Posted by u/Jonathan_Rivera on 2026-10-10 · 7 points (100% upvoted) · 0 comments**

GitHub merged 67 pull requests in
NousResearch/hermes-agent
during the
24 hours ending October 9, 2026, 1:30 PM ET
. I grouped them by area below and sorted each section newest to oldest by merge time.
Models, providers & routing
#135529
Memory-provider installs that fail at agent start stop retrying on every start; a symlinked plugin slot reads already-installed
#135524
fix(memory): detect providers past the first 8 KB of
init
.py
#133736
fix(plugin-catalog): bump cursor-provider to v0.3.6
#135473
catalog: bump excel_line pin 45dcf84 -> a48cc5a (provider-discovery fix)
Prompts, skills & agent behavior
#135157
fix(memory): make external prefetch spilling opt-in
Desktop & UI
#133101
fix(desktop): render Mermaid labels that contain <br/>
#135542
fix(update): a Desktop-only Node dependency failure no longer blocks the TUI and web UI
#135504
feat(desktop): plugin SDK pet bubble (ctx.pet.say)
#135313
feat(desktop): build-bundle scripts for local MSIX, DMG and AppImage test builds
#135096
fix(cli): hermes model offers reasoning effort when the model ID is unchanged (salvage #110468)
Gateway, channels & integrations
#135393
fix(tui_gateway): keep a detached session alive while it owns an active /loop or /heartbeat
#135535
fix(gateway): restart --all and status no longer target other Unix users' gateways (#105719)
#135514
A failed OAuth catalog MCP install from a card or the agent says why instead of reading 'exception'
#135259
catalog: add discord-tps — live tok/s and model on the Discord bot presence
#135406
Test runs no longer leave detached gateways running after they finish
#135340
A scratch or test home can no longer rewrite the real gateway service unit (salvage #133476)
Core runtime, state & reliability
#135715
fix: don't fail npm install when lefthook can't install hooks
#135464
Unconfigured hermes --tui opens the TUI setup screen again (unblocks the Termux .deb, salvage #130913)
#135348
Harder linter fixes part 2
#135459
fix(release): stable releases pass signed-package acceptance when no upgrade baseline exists
#135458
fix(pm): updated installs get the new bundle's uv cache, so plugin enable stops building cryptography from source
#135460
fix(e2e): macOS ffmpeg mirror fallback and app quit wait
#135438
fix(local-models): stop recommending the 27B on hardware that can't run it well
#135531
fix(tts): a failed synthesis no longer deletes an existing file
#135499
fix(browser): fence captured CDP dispatch and retain late replies (salvage #134595)
#135220
catalog: add dashboard-auth-feishu
#135114
feat(plugin-catalog): bump hermes-pickup to 0.2.0
#135077
fix(plugin-catalog): bump web-search-plus to 4.3.5
#134982
catalog: add Enchanted Composer
#134716
feat(plugin-catalog): add redline plugin
#134699
feat(plugin-catalog): add huddo plugin
#134512
catalog: add agent-batch (parallel AI task orchestrator)
#135484
catalog: list adaption + hermes-openwhispr, re-pin hermes-telemetry 0.9.0 + qdrant 0.1.8 (salvage of #135205, #132198, #135209, #133557)
#135300
feat(plugin-catalog): add print-job-watch
#135289
feat(catalog): bump hermes-pokemon to v0.7.0
#135180
plugin-catalog: bump hermes-cron to 1.3.0
#135167
plugin-catalog: bump memtomem to v0.6.8
#135160
feat(plugin-catalog): bump error-ledger to 1.2.0
#135142
feat(plugin-catalog): hermes-dreaming 2.2.1 — external-review fixes + 0.21.6 audit
#135135
fix(plugin-catalog): bump hermes-field-notes to 1.2.3
#135132
feat(plugin-catalog): add command-ledger
#135118
plugin-catalog: invinoveritas-receipts 0.2.1 (turn-end receipts on max_iterations_reached)
#135326
Catalog: bunny_space-platform v1.0.6 (pin + version)
#135301
feat(plugin-catalog): add wyoming-voice-bridge
#135233
fix(plugin-catalog): update hermes-honcho-plugin to 0323f5d
#134713
Add hermes-video-editor to the plugin catalog
#132702
catalog(quota): re-pin to v2.10.0 with Claude credential disclosure
#129693
feat(plugin-catalog): add codex-account-switch
#135333
Plugins with Python dependencies install again in the Windows MSIX app (#135236)
#135409
E2E suites run only on release builds, never on PRs or main pushes
#135242
Onboarding apps list fades at the edges when it scrolls
#135389
Spotify moves out of core into the official spotify plugin, existing users migrated automatically
#135387
Plugin catalog: spotify (official, NousResearch)
#135281
Harder linter fixes
#135092
perf(update,install): source updates rebuild only what changed; pinned installs clone once
#135319
fix(plugins): re-enabling a plugin restores its toolset in a saved platform_toolsets list
#135314
perf(install): pinned Windows installs check out only the pin, before publishing (follow-up #135092)
#134233
Solstice no longer fails to load during install (lazy transport import)
#135276
fix(termux): repin the termux pool so the payload's libc++ matches apt's cmake
#135261
fix(install-e2e): tolerate the update-result consume race and held lock files
#135285
Copilot Responses tool calls no longer run twice with empty {} arguments (#94707, salvage #111505 + #94708)
#135232
Docker image builds no longer fail on lefthook install (follow-up to #135177)
Maintenance, documentation & formatting
#134391
chore(catalog): publish OpenViking 2.1.1
#135310
chore(plugin-catalog): bump hyatlas to 4.5.0 (f61727a)
#135271
chore(catalog): bump hermes-frihet pin to 4f092d5 (PyYAML runtime-dep merge #1)
#134210
chore(catalog): pin the Blender plugin to 0.2.0, which declares Blender
#135341
chore(plugin-catalog): delist antigravity-oauth-plus (rule 16)
Source
GitHub merged-PR search for this exact window
Window:
2026-10-08T17:30:00Z
through
2026-10-09T17:30:00Z
(end exclusive)
Plain-English summary
If technical terms are not your thing: this is mostly maintenance, not 67 brand-new features.
The fixes cover model connections and routing, agent behavior and skills, desktop and interface issues, gateways and integrations, core reliability, state, and recovery, and maintenance, tests, and documentation. In practical terms, they aim to deliver better model and provider compatibility, more complete responses, tool calls, and long-running work, fewer desktop and interface glitches, smoother gateways and integrations, safer state and recovery behavior, and security fixes for specific risks called out in the log.
You only need to open an individual PR if it mentions a feature or problem you care about.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x1x4lj/67_hermes_agent_prs_merged_in_the_last_24_hours/)
