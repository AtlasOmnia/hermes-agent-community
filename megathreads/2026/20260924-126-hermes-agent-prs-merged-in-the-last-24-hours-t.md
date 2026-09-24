---
title: "126 Hermes Agent PRs merged in the last 24 hours — through September 23, 2026, 1:30 PM ET"
author: u/Jonathan_Rivera
date: 2026-09-24
score: 9
comments: 1
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wochxx/126_hermes_agent_prs_merged_in_the_last_24_hours/
flair: "News — Official Releases, announcements, major changes"
---

# 126 Hermes Agent PRs merged in the last 24 hours — through September 23, 2026, 1:30 PM ET

**Posted by u/Jonathan_Rivera on 2026-09-24 · 9 points (90% upvoted) · 1 comments**

GitHub merged 126 pull requests in
NousResearch/hermes-agent
during the
24 hours ending September 23, 2026, 1:30 PM ET
. I grouped them by area below and sorted each section newest to oldest by merge time.
Models, providers & routing
#120189
api_server: automatic memory recall lands on continued sessions (one provider per session, #120116)
#120137
profile --clone keeps the active memory provider's config (#120115, supersedes #43107)
#120124
fix: chats switched to a Codex model resume on the Codex endpoint, not the previous provider's
#120117
fix(agent): hosted providers no longer get the local-server "wait and /retry" context rejection
#120052
fix(models): a curated fallback never pins itself in the provider models cache
#114732
catalog: honcho and supermemory memory providers from their maintainers' repos
#119767
catalog: hindsight memory provider from vectorize-io/hindsight (subdir, pin dc75038; memory-provider migration)
#120003
Memory providers receive the exact committed entry on replace/remove (salvage #118903)
#119981
fix(models): drop gpt-6-terra, a tier OpenAI never published
#119410
feat(models): GPT-6 Sol/Terra/Luna replace the 5.6 tiers on Nous/OpenRouter, with Codex -900k variants
Prompts, skills & agent behavior
#120406
perf(agent): remove quadratic and per-character work from agent hot paths
#120187
fix(compression): turn-start in-place compaction no longer hides the newest summarized turn
#120062
fix(memory/holographic): store the default fact DB path as $HERMES_HOME so clones and renames keep their own store
#119962
fix(compression): keep the /compress here N tail in state.db under in-place compaction
#119406
compression.threshold_tokens: null takes effect live; cap survives a failed config load (follow-up to #115986)
Desktop & UI
#120261
Deleting a renamed bot roster section no longer brings it back under its old name (Desktop)
#120427
fix(desktop): localize live slash-command descriptions
#120236
feat(cli,tui): live dock shows the standing /goal and queued /queue prompts
#120425
fix(desktop): clarify plugin copy and contain the scope selector
#120434
fix(desktop): preserve Unicode graphemes in profile initials
#120423
fix(desktop): teach the correct archive shortcut in every locale
#120424
fix(desktop): localize update-dialog headings and fallback copy
#120389
fix(desktop): keep translated reasoning labels on one line
#119606
fix(desktop): preserve chronology when backfill offset drifts forward
#120080
Supervised 0.0.0.0 dashboard no longer crash-loops behind a Desktop pool backend; inherited HERMES_DESKTOP no longer binds a second backend (#119824, #119210, salvage #119832 #119214)
#120273
fix(desktop): a submit that resumes the selected session moves the chat to the resumed runtime
#119878
fix(desktop): stop duplicate and misplaced turns after transcript refresh
#120089
Session renames no longer stall the backend event loop; Desktop chat frames keep flowing (#119643 A, salvage #119650)
#120079
Windows: Desktop update restarts the messaging gateways it stopped (#119809, salvage #119815)
#119836
fix(desktop): stop background secondary reopens from re-resuming every tile
#108914
feat: Bot Screen — per-bot Xfce desktop streamed into Hermes Desktop, take over and hand back (related #92524)
#119906
feat(desktop/kanban): task modal UI pass — shared Dialog, markdown, tidy sidebar and composer
#120099
fix(desktop): Settings and Capabilities follow the "Applies to" profile on the shared local backend (salvage #118941)
#119428
fix(desktop): render Files-pane HTML with a Preview | Source toggle (supersedes #107464)
#120055
fix(desktop): in-app browser no longer reloads your page on every agent file edit (#81487, salvage #81503)
#120040
Desktop: non-default profile chats no longer stream garbled text or double bubbles (#120005; closes #120006, #120007)
#120026
fix(desktop): models added by a plugin or catalog update no longer start hidden in the picker
#119872
fix(memory): user-dir memory providers keep Desktop config + OAuth (salvage #116566 slice)
#119727
fix(desktop): show saved gateways without opening Settings
#119605
fix(desktop): keep typing and refreshed transcripts stable
#119601
The last four MCP enabled-flag readers use the shared reader (ACP, hermes tools picker, desktop connector card, health sweep)
#119557
fix(desktop): remember Simple and Advanced workspace layouts
#119349
Desktop: after a plugin install, "Connect now" connects its MCP servers in place (no relaunch, no gateway restart)
Gateway, channels & integrations
#120405
perf(gateway): take file I/O and per-message scans off the event loop
#119774
feat(gateway): stop, start and restart one profile under the host multiplexer
#120087
gateway: launchd install honours --no-start-now, drain cap sees the launchd label, /api/status ports match owned platforms, dashboard shows server error detail, email pairing/decline reach the gateway (#119948 #119598 #119918 #119991 #119923; salvage #119949 #119607 #119920 #119992 #119924)
#120257
fix(telegram): keep update receipts across adapter rebuilds and restarts
#120143
fix: dashboard, tui-gateway and CLI lifecycle verbs act on the right profile (multiplexer, not the sticky/served one)
#120127
hermes update: in-gateway cron updates no longer exit STALE, stale editable finder is refreshed, linger/schtasks tests fixed (#119597, #119466, #119786, #119845; salvage #119525 #119790 #119847)
#120129
Gateway slash commands and session routing act on the routed profile under multiplex (#119915, #119971, #119864, #119876; salvage #119922 #119972 #119868 #119875 #119904)
#120122
fix(gateway): --replace no longer starts a second gateway on a lost lock race, respawn-storms beside a standalone owner, or deadlocks on the stale systemd drop-in (#119837, #119807, #119467)
#120085
Docker: the image's
gateway run
keeps the root profile and a copied profile dir never reads as running (#119880, salvage #119881 #119772)
#120072
gateway config: env refs expand for platforms.* and WEBHOOK_SECRET/PORT apply to a yaml-enabled webhook (#119733 #119763; salvage #119755/#119765, supersede #119737 #119750 #119770)
#120152
hermes gateway stop no longer exits 1 (and gets revived) when the stop watcher beats the CLI's SIGTERM
#120158
fix(tui_gateway): manual /compress keeps the session workspace in the stored prompt, so the next resume hits the prompt cache
#120140
hermes update no longer restarts other homes' gateways or the account's real hermes-gateway.service (#93349)
#120126
fix(tui_gateway): a warm session.resume reports the chat's own model, not the profile default
#120082
fix(gateway): bare allowlist entries no longer admit any sender sharing the '@' localpart (#119446, salvage #119447)
#119960
Two plugins installed together both go live with their MCP tools and skills
#119900
Installing a second plugin no longer removes the first plugin's MCP tools from the profile
#119680
feat(gateway): gateway.standalone, TEMPORARY per-profile compat opt-out of the host multiplexer
#119644
Installed plugins' MCP tools and skills are live in every open chat, no Connect-now
#119536
Profile editor MCP toggles take effect at runtime (#89441, salvage #107451)
#119365
feat(catalog): install the official Blender Lab integration
Core runtime, state & reliability
#114530
feat(catalog): add standalone Microsoft 365 plugin
#120386
fix(state): dashboard and
hermes sessions list
no longer fail with 'database is locked' in DELETE journal mode
#120342
fix(bot-mode): a local group member no longer answers its own reply until the round cap
#120076
catalog: bump hindsight to 1.0.1 (pin f7a153d)
#120231
Plugin dependencies follow the plugin's own security policy; Hermes's 14-day quarantine applies to Hermes deps only (reverses #118841 item 3, unblocks #120076 #114530)
#120435
fix(sessions): export-then-delete keeps compacted history and refuses on drift
#120404
perf(picker): stop re-reading config per model and blocking on expired catalogs
#120407
perf(web): keep dashboard log, media and file reads off the event loop
#120402
perf(config): cheaper config and profile reads on hot paths
#120103
Cron, kanban, ledger and adapter background paths follow the owning profile under multiplex (#119858, #119859, #119973, #119242; salvage #119974 #120045 #120019 #120009 #112888)
#120092
fix(profiles): per-profile SDK client caches and scoped dashboard/cron memory readers under multiplex
#120312
fix(cron): a pinned job never falls back to the global fallback chain
#120268
Multiplexed housekeeping: one profile's failure no longer skips the rest or leaks its home (salvage #110405)
#120274
fix(state): surface corrupt state.db as one degraded session-storage state
#120128
fix(secret-scope): bound scopes carry their home; foreign-home misses fail closed, setup raises release tokens, readers never borrow os.environ
#120176
fix(process): killing a background job no longer orphans children its shell starts during the grace window
#120161
fix(serve): READY is the first stdout line again — peer-less global broadcasts no longer print in WS backends (salvage #113249)
#120178
fix: hermes -z runs in its launch directory and loads its AGENTS.md again (#95577, salvage #88281)
#120175
Mid-turn compaction no longer drops this turn's tool results from the next request (salvage #91234)
#119273
fix(process_registry): bash startup noise no longer leaks into background output when the reader wakes between writes (deflakes test_process_dock, test_process_registry_list_exit)
#120095
plugin-catalog: claude-subscription-directsdk pin → 885ba106 (four plugin fixes)
#117834
Dashboard chat can start in a chosen project/repo directory from any browser or phone (Amp-inspired workspace picker)
#120078
fix(imessage): links no longer leak raw markdown into iMessage, URLs survive stripping (salvage #118591, #96867)
#120068
fix(imessage): Photon and BlueBubbles replies text like a person, not markdown
#120043
plugin-catalog: claude-subscription-directsdk pin → 815c05e7 (Opus 5.5 route)
#119888
hindsight moves to the plugin catalog (auto-migrated on first start / hermes update)
#119860
fix(state): micro-compaction no longer strands summarized tool rows as rewind debris (part of #118481, salvage #119500)
#119914
Connector rows say "Waiting for your browser…" only after the user opens the sign-in link
#119902
tool_search tells the model to search with keywords, not questions
#119912
Catalog installs the NVIDIA plugins with skills that let Hermes own the connection
#119913
The first build after onboarding is named and started from the stored reply, so its title and brief cannot come out garbled
#119901
Plugins installed at the same time both keep their install record
#119812
Onboarding offers catalog plugins next to connectors and installs the picked ones before handoff
#119724
Setup agent can search the catalog and install plugins through the approval card; tools live the same turn
#119633
Catalog install card: plugin and skill rows with an Advanced install modal
#119567
MCP server on/off reads the same on every surface (one reader for enabled)
#119491
Setup profile sessions get the
setup
toolset by profile role; nothing else can grant it
#119436
fix(codex): Codex picker and context probe no longer hide GPT-6 Sol/Luna behind the 0.0.0 catalog sentinel (#119412, supersedes #119420)
#119456
Setup profile is minted by the backend and found by role, not by name
#119422
Legacy checkpoints: true no longer busts the agent cache on migration; cache signature = one cfg_get per key (follow-up to #119406)
#119399
Profile toolset pin from profiles.configure now takes effect in sessions
Maintenance, documentation & formatting
#120472
fmt(js):
npm run fix
auto-fix
#120468
test(actual): clear CA env vars before asserting the macOS certifi default
#120465
fmt(js):
npm run fix
auto-fix
#120459
fmt(js):
npm run fix
auto-fix
#120456
test(web): make attach-token fixtures deterministic
#120400
fmt(js):
npm run fix
auto-fix
#120392
fmt(js):
npm run fix
auto-fix
#120267
test(desktop): respect host locales in UI assertions
#119278
test(mcp): OAuth callback-latch tests no longer race the waiter's 500 ms listener shutdown (4 main reds)
#120113
fmt(js):
npm run fix
auto-fix
#120098
fmt(js):
npm run fix
auto-fix
#120071
test: remove ~8,200 low-value, brittle and CI-blocking tests
#120060
test(desktop-e2e): local e2e runs no longer chat through the developer's real Hermes
#120048
fmt(js):
npm run fix
auto-fix
#119817
fmt(js):
npm run fix
auto-fix
#119739
fmt(js):
npm run fix
auto-fix
#119649
fmt(js):
npm run fix
auto-fix
#119581
fmt(js):
npm run fix
auto-fix
#119573
fmt(js):
npm run fix
auto-fix
#119476
fmt(js):
npm run fix
auto-fix
#119356
fmt(js):
npm run fix
auto-fix
Source
GitHub merged-PR search for this exact window
Window:
2026-09-22T17:30:00Z
through
2026-09-23T17:30:00Z
(end exclusive)
Plain-English summary
If technical terms are not your thing: this is mostly maintenance, not 126 brand-new features.
The fixes cover model connections and routing, agent behavior and skills, desktop and interface issues, gateways and integrations, core reliability, state, and recovery, and maintenance, tests, and documentation. In practical terms, they aim to deliver better model and provider compatibility, more complete responses, tool calls, and long-running work, fewer desktop and interface glitches, smoother gateways and integrations, safer state and recovery behavior, and security fixes for specific risks called out in the log.
You only need to open an individual PR if it mentions a feature or problem you care about.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wochxx/126_hermes_agent_prs_merged_in_the_last_24_hours/)
