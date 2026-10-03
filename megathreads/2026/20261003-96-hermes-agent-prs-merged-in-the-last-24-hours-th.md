---
title: "96 Hermes Agent PRs merged in the last 24 hours — through October 2, 2026, 1:30 PM ET"
author: u/Jonathan_Rivera
date: 2026-10-03
score: 7
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wvztux/96_hermes_agent_prs_merged_in_the_last_24_hours/
flair: "News — Official Releases, announcements, major changes"
---

# 96 Hermes Agent PRs merged in the last 24 hours — through October 2, 2026, 1:30 PM ET

**Posted by u/Jonathan_Rivera on 2026-10-03 · 7 points (88% upvoted) · 0 comments**

GitHub merged 96 pull requests in
NousResearch/hermes-agent
during the
24 hours ending October 2, 2026, 1:30 PM ET
. I grouped them by area below and sorted each section newest to oldest by merge time.
Models, providers & routing
#131063
fix(agent): normalize provider-minted parallel tool-call ids at mint time
#131269
fix(memory): never lose memory silently when a provider moves out of core
#131256
Cloned profiles keep their catalog-installed plugins and memory provider
#131265
retaindb, byterover and holographic memory providers join the plugin catalog (Nous-maintained)
#131309
fix(models): a failed Codex/Anthropic catalog fetch no longer hides Astra for an hour (salvage #130957, #121248)
#128408
fix(plugins): memory provider setup lists the dependencies PM would install
Prompts, skills & agent behavior
#130551
fix(agent): a model stuck in a repetition loop no longer streams forever on an uncapped endpoint (#127234, salvage #127242)
#130528
Effectful tool calls refuse cut-short compression markers, and mid-turn corrections no longer end long turns (#128000, salvage #127613, #128682)
Desktop & UI
#131676
fix(tui): answer the vault save-login and verification-code prompts
#131669
fix(desktop): ship exact-size, theme-aware MSIX icons instead of one 44px tile
#131642
fix(desktop,tui): /browser use [off] works outside the CLI
#131627
fix(desktop): model picker keeps names whole; message time on hover
#122976
feat(desktop): macOS 26 layered app icon, ring dropped from every icon
#128863
fix(desktop): run the Windows update checkers from bundled core code
#131266
Memory providers migrate on Desktop, the gateway and scripted updates — no terminal needed for their Python deps
#130996
fix(desktop): scope preview tabs to the session that opened them (re-land #128552)
#131350
fix(tui): arm the slash-worker parent watchdog before the cli import
#131310
fix(desktop): the reasoning pill no longer shows a stale clamp after a model switch (#128871, salvage #128883, #130963)
#131349
fix(desktop): clear a deleted session's subagents, todos, goal and background status
#131328
fix(tui): close agents that finish building after their session closed
#131229
Desktop SDK: plugins decorate model menu rows; themes style chat switches via data-session-switching
#131015
fix(desktop): YouTube embed host answers malformed paths with 404 instead of crashing
#130983
Desktop: pick Classic Hermes gold/navy in Appearance without repainting stock installs (#76579)
#131215
fix(desktop): right-click in a pane opens the menu for what you clicked (#127313, #127997, salvage #129402)
#130975
fix(desktop): play YouTube embeds through a loopback player host
#130729
Desktop update no longer spends minutes syntax-checking renderer chunks one Node process at a time (salvage #127400, #125201)
#130939
fix(desktop): X and Instagram embeds no longer run vendor scripts in the app window (salvage #129637)
#130921
Desktop keeps remote gateway credentials off redirect hops that leave the gateway (salvage #129625)
#130826
revert: approval and clarify prompts time out again in the CLI, TUI and Desktop (reverts #130167)
#130852
revert: Desktop connects to remote backends and keeps its settings again (reverts #127201, #130015, #128552)
#130795
Plugin catalog refuses plugins that override Hermes core or Desktop at runtime
#130595
fix(cli): exiting a
--worktree
session keeps the worktree when it has uncommitted changes (#129482, salvage #129489)
#130527
fix(desktop): preview saves and new-project IDEA.md stay on the connection they started on (#127659, #127676, salvage #127662 #127677)
#130505
fix(desktop): Quick Entry sends to a stored session after this window's own unsynced turn (#130031, salvage #130035)
Gateway, channels & integrations
#131249
Local MCP/plugin tool batches in one tool_call now run instead of being rejected (#119891, #121616, salvage #131006)
#126142
feat(plugin-catalog): add go-whatsapp
#131221
fix(gateway): /fast and /fast ultrafast follow the session's /model route (#118761, salvage #65028)
#131071
fix(gateway): skip restart-safe scoped cron runs in the restart wait, keyed per profile
#130866
fix(gateway): SMS, email and WeCom deliver long replies and cron output in full instead of failing or truncating
#130920
Matrix invites and approval reactions stop accepting revoked pairing users without a restart (salvage #129773)
#130917
fix(whatsapp): WhatsApp Cloud only accepts inbound messages addressed to its own phone number and business account (salvage #129851)
#130918
fix(webhook): a stale subscription update no longer brings back a deleted or disabled route, and moving a route to another profile rotates its secret (salvage #129804)
#130522
fix(gateway): two gateway.standalone profiles can run side by side again, including after a WSL clock resync (#128600, salvage #128602 #129035)
#130692
fix(gateway): webhook deliveries on different routes or profiles no longer drop each other as duplicates (#7448, salvage #129626)
#130727
fix(relay): chunk long cron output through the relay connector instead of truncating it
#130518
fix(gateway): stop the cgroup cleanup reaper from killing a live gateway (#126845, salvage #126846)
Core runtime, state & reliability
#131252
Skills and Plugins are back to the list tabs; card catalog browser removed again (reverts #119381)
#97876
fix(dashboard): show the slot model as current in aux/MoA pickers
#131623
fix(browser): /browser connect and disconnect retarget browser_exec
#131272
Supermemory installs from the plugin catalog — existing setups migrate automatically
#131301
Honcho memory installs from Plastic Labs' catalog plugin; core no longer bundles it
#131430
fix(tests): failure-writer ownership probe stops flaking at 19/20 (no real tirith download mid-probe)
#131383
Onboarding on a Spark no longer offers a local model that a task chat installs by hand
#131393
retaindb, byterover and holographic are no longer listed as Nous-maintained catalog plugins
#131346
fix(tests): kanban wake drain helpers no longer busy-spin forever on Python 3.12+
#131306
fix(dashboard): free PTY sessions whose process died, and end their helpers
#131351
fix(logging): stop writing into a profile deleted while serve runs
#129093
catalog(hindsight): pin the released v1.2.1
#129218
feat(plugin-catalog): add 0bull community plugin
#122099
plugin-catalog: add hermes-workflows (community, automation)
#131001
Finished updates stay finished: no same-commit re-run on launch, Windows exit 124 after completion is success (salvage #123863, #127198)
#131217
hermes status --full lists each messaging platform once, with the summary's verdict (#96190)
#126093
fix(plugin-guard): catalog false positives no longer block or prompt (denylist regex, host noun, sha256sum, SQL exec, coin keyword, JSON tips, quoted fixtures)
#131034
hermes status shows a one-screen summary by default, --full for every section (salvage #130857)
#131048
Plugin catalog submission guide: one complete page, synced with the README rules
#129588
fix(cron): ignore measured durations in the incident error signature
#127883
Session list stops reading every message row when planner stats predate idx_messages_session_id (#119403)
#130894
fix(git): hermes -w and automatic worktrees work again in repos with an includeIf (follow-up to #130661)
#130526
fix(cron): recurring jobs resume after a transient croniter import failure (#127182, salvage #127195)
#130661
fix(git): automatic git runs in kanban, worktree cleanup, subagents and hermes -w no longer execute a cloned repo's filters or hooks (#126017, salvage #126019)
#130619
Negative backup retention, JSON NaN/Infinity writes, and replace_all Unicode flattening fixed in backup and file tools (salvage #128886, #128888, #128894)
#130601
Heartbeats stay quiet during
hermes pause
instead of resending the paused notice every poll, and /loop wakeups wait for resume (salvage #126905)
#130685
Dashboard native sign-in only sends login codes back to a real loopback callback (salvage #129621)
#130632
fix(state): a re-flushed restored history block no longer duplicates in state.db (#129065, salvage #129133)
#130618
fix: symlinked jobs.json, .env and config files survive a crash mid-save when the link points to another filesystem (salvage #126237)
#130599
fix(cron): context_from injects the full previous answer when it contains a "## Response" heading (#128543, salvage #128685)
#130600
Disk cleanup no longer deletes existing test_/tmp_ files the agent only edited or listed (salvage #128090)
#130548
Dump, debug share and other strict-redaction egress no longer leak credentials kept in the URL username (#129983, salvage #129985)
#130516
fix(a2a): refuse peers on a network-exposed A2A bind with no trusted-peer allow-list (#126756, salvage #130310)
#130787
One rejected encrypted-reasoning blob no longer ends replay for the session, and the verdict no longer follows /model or fallback (Responses/Codex, salvage #61552)
#130645
fix: preserved Anthropic thinking survives rejection and resume (salvage #129620)
#130743
GPT sessions without terminal/execute_code are no longer told to use them (#106506, salvage #106548)
#130716
Fallback-pinned sessions return to a Codex primary whose quota reopened early, without flip-flopping (salvage #130578)
#130660
fix(web): free managed fast search reaches registered Nous accounts (guests keep the keyless ring)
#130740
Custom codex_responses routes cap -900k at their own catalog max; empty Codex catalog probes are not repeated (#128288 review)
#130735
codex_app_server runs the Hermes-selected model, including after /model (salvage #83269)
#130712
Plugin catalog CI can no longer be bypassed by renames, subdir traversal or tag pins (salvage #125842)
#130707
feat(plugin-catalog): add woof — WOOF weather simulations on your own GPU
Maintenance, documentation & formatting
#131680
fmt(js):
npm run fix
auto-fix
#131545
docs: route agents and contributors to SECURITY.md for security reports
#131603
fmt(js):
npm run fix
auto-fix
#131246
test: seed the version cache per test process instead of running git 7 times
#131236
ci: run the Python suite and the macOS lane as two slices each
#131253
ci(label-rerun): never rerun a CI run whose PR head has moved
#131251
fmt(js):
npm run fix
auto-fix
#130953
fmt(js):
npm run fix
auto-fix
Source
GitHub merged-PR search for this exact window
Window:
2026-10-01T17:30:00Z
through
2026-10-02T17:30:00Z
(end exclusive)
Plain-English summary
If technical terms are not your thing: this is mostly maintenance, not 96 brand-new features.
The fixes cover model connections and routing, agent behavior and skills, desktop and interface issues, gateways and integrations, core reliability, state, and recovery, and maintenance, tests, and documentation. In practical terms, they aim to deliver better model and provider compatibility, more complete responses, tool calls, and long-running work, fewer desktop and interface glitches, smoother gateways and integrations, safer state and recovery behavior, and security fixes for specific risks called out in the log.
You only need to open an individual PR if it mentions a feature or problem you care about.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wvztux/96_hermes_agent_prs_merged_in_the_last_24_hours/)
