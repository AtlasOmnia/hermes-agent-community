---
title: "52 Hermes Agent PRs merged in the last 24 hours — through September 8, 2026, 1:30 PM ET"
author: u/Jonathan_Rivera
date: 2026-09-09
score: 14
comments: 17
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wav0i0/52_hermes_agent_prs_merged_in_the_last_24_hours/
flair: "News — Official Releases, announcements, major changes"
---

# 52 Hermes Agent PRs merged in the last 24 hours — through September 8, 2026, 1:30 PM ET

**Posted by u/Jonathan_Rivera on 2026-09-09 · 14 points (81% upvoted) · 17 comments**

GitHub merged 52 pull requests in
NousResearch/hermes-agent
during the
24 hours ending September 8, 2026, 1:30 PM ET
. I grouped them by area below and sorted each section newest to oldest by merge time.
Models, providers & routing
#105550
fix: command-authenticated providers show full model catalogs (salvage #99893)
#105352
fix(compressor): per-model
context_length
overrides in custom_providers reach the compressor (salvage #83324)
#105347
fix(delegation): pinned children stop inheriting the parent fallback chain;
delegation.fallback_providers
declares their own (#80450, #65038, salvage #80479)
Prompts, skills & agent behavior
#105873
fix(skills): RSS and Reddit reading no longer activate by default
#105328
fix(compression): inflated past-window estimates no longer force preflight compaction (#104462)
#105351
fix(agent): a host that merely runs containers is no longer classified as one (#58135, #48594, salvage #58141)
Desktop & UI
#105813
feat(desktop): organize sessions by gateway and reuse saved Cloud instances
#104407
fix(desktop): expose plugin installation from settings
#105727
fix(desktop): stop transcript text bleeding through task cards (salvage #69069)
#105593
feat: keep live subagents visible in CLI, TUI, and Desktop
#105585
fix(desktop): busy Bot Chat stays current on return (salvage #102474)
#105569
fix(desktop): keep group chat replies visible in arrival order
#105493
fix(tui): match the redo chord case-insensitively so Cmd+Shift+Z works on extended-key terminals
#90674
fix(tui): restore Shift+letter case in the composer for extended-key terminals
#105442
fix: cron and local DMs reach an open Desktop Bot Chat
#105350
fix(desktop): a READY sentinel spliced onto a stderr chunk is recognised in merged output (#103792, salvage #103841)
#105199
Desktop task panel follows the todo_list rename; subagent progress survives tool_progress off
Gateway, channels & integrations
#105884
fix(gateway): provision linger and derive the user bus per spawn for system-level units (#104893, salvage #105222 + #105135)
#99220
fix(relay): authorize send_message targets and surface egress declines (P5)
#102602
fix(relay): re-dial once with a fresh token before treating a 4401 as revocation
#105356
fix(gateway): heartbeat and completion events resume the owning conversation
#105334
fix(gateway): error recovery no longer duplicates accepted inputs (#104653)
#105346
fix(gateway): cron and Kanban children start under a system-level systemd unit (#104893, salvage #105037)
#105348
fix(tools): the Windows Git Bash probe no longer takes the TUI gateway down on the first terminal call (#78820, salvage #104832)
Core runtime, state & reliability
#105826
fix: correct two stale in-code comments left out of the docs batch (#105788)
#105763
fix(browser): locked auth copies fail cleanly without stale logins (salvage #105754)
#105744
fix: make /review recognizable in live subagent viewers
#105736
feat: collapse terminal subagent docks to one line
#105571
fix: shared chats keep every attached client synchronized
#105545
fix: native Gemini tool calls survive nullable and union parameters (salvage #55643)
#105330
fix(approvals): paths and launchers no longer bypass explicit deny rules (#104308)
#105349
fix(qqbot): approval buttons in QQ private chats resolve instead of timing out (salvage #31593)
#105125
delegate_task: subagents can hand background processes to the parent; leftovers are reported, not trusted
Maintenance, documentation & formatting
#101420
test(install): cross-OS install/update E2E matrix (windows, macos, linux)
#105824
test: Desktop saved-pane checks no longer time out during cold imports
#105823
fmt(js):
npm run fix
auto-fix
#105818
fmt(js):
npm run fix
auto-fix
#105786
docs: eight small accuracy fixes from open type/docs issues
#105785
docs(bot-mode): state that same-gateway Group Chats keep running after Desktop closes
#105787
docs(mcp): surface device-code login in the remote/headless hosts section
#105784
docs(code-execution): document the session kernel, reset, and stdout spillover
#105783
docs(sessions): fix tip box that still says auto-prune ships disabled
#105782
docs(delegation): update shipped defaults (250 iterations, 10 concurrent children) and document output_schema
#105739
fmt(js):
npm run fix
auto-fix
#105732
fmt(js):
npm run fix
auto-fix
#105729
fmt(js):
npm run fix
auto-fix
#105601
fmt(js):
npm run fix
auto-fix
#105600
fmt(js):
npm run fix
auto-fix
#105451
fmt(js):
npm run fix
auto-fix
#105448
test: Desktop deadline checks no longer race CI scheduling
#105374
chore: release v0.21.1 (2026.9.7)
#105355
test: search and package fixtures keep their real dependencies reachable
Source
GitHub merged-PR search for this exact window
Window:
2026-09-07T17:30:00Z
through
2026-09-08T17:30:00Z
(end exclusive)
Plain-English summary
If technical terms are not your thing: this is mostly maintenance, not 52 brand-new features.
The fixes cover model connections and routing, agent behavior and skills, desktop and interface issues, gateways and integrations, core reliability, state, and recovery, and maintenance, tests, and documentation. In practical terms, they aim to deliver better model and provider compatibility, more complete responses, tool calls, and long-running work, fewer desktop and interface glitches, smoother gateways and integrations, safer state and recovery behavior, and security fixes for specific risks called out in the log.
You only need to open an individual PR if it mentions a feature or problem you care about.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wav0i0/52_hermes_agent_prs_merged_in_the_last_24_hours/)
