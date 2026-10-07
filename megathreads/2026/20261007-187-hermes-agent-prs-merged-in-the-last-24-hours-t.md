---
title: "187 Hermes Agent PRs merged in the last 24 hours — through October 6, 2026, 1:30 PM ET"
author: u/Jonathan_Rivera
date: 2026-10-07
score: 16
comments: 8
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wz8pi2/187_hermes_agent_prs_merged_in_the_last_24_hours/
flair: "News & Releases"
---

# 187 Hermes Agent PRs merged in the last 24 hours — through October 6, 2026, 1:30 PM ET

**Posted by u/Jonathan_Rivera on 2026-10-07 · 16 points (90% upvoted) · 8 comments**

GitHub merged 187 pull requests in
NousResearch/hermes-agent
during the
24 hours ending October 6, 2026, 1:30 PM ET
. I grouped them by area below and sorted each section newest to oldest by merge time.
Models, providers & routing
#131267
plugin-catalog: add mem0 and openviking (vendor-maintained memory providers)
#133715
fix(cache): skill turns no longer re-write their whole scaffold after the first tool round
#133723
feat(tts): let PCM-streaming plugin TTS providers join the streaming voice path (salvage #120398)
#132343
plugin-catalog: add Stack Markdown memory provider
#131807
plugin-catalog: add hydradb memory provider
#133666
feat(plugin-catalog): add cursor-provider v0.3.5
#133165
catalog: add kimchi-provider
#133064
Catalog memory-provider installs stop failing on every agent start and every Install click (hindsight 91%, mnemosyne 87%)
#133047
Memory-provider plugin installs now activate the provider instead of a dead-end plugins enable (#119909, salvage #119937)
#85891
fix(providers): stop sending thinking.disabled on GLM-5.3
#131796
fix(stt): opt-in 16 kHz mono normalization for command STT providers [risk 0.30]
#120901
fix(providers): bare named custom providers resolve to custom profile for reasoning_effort (#119681)
Prompts, skills & agent behavior
#133967
fix(skills): resolve skills by frontmatter display name in the manager and dashboard editor
#133951
fix(skills): trust-scope inline-shell auto-exec to non-community hub skills
#133864
fix(todo): reject empty content instead of substituting '(no description)'
#133729
fix(agent): a reasoning model's private chain-of-thought is no longer shown as the reply when it stops with empty content (#114082, salvage #112833)
#133627
feat(telemetry): memory and compression rows say why they failed or were skipped
#133054
fix(telemetry): compression attempts that could not fail count as skipped, not failed
#133051
fix(compression): fail a silent chat-completions summary stream at the no-progress window (salvage #100526)
#133039
fix(skills): skills.sh skills in a generic skills/ dir install again; index resolves paths before its token expires (#130129, salvage #130135)
#133040
fix(compression): name the main model when the aux summary falls back
#131932
fix(agent): detect pronounless action acknowledgements (#72692)
#131907
fix(agent): unwrap data/success envelope in auxiliary LLM responses [risk 0.30]
#131811
fix(delegation): collect a child's real result in a grace window after the stale-heartbeat verdict [risk 0.30]
Desktop & UI
#131135
fix(desktop): evict inactive tool disclosure atoms
#133987
fix(cli): honor model_catalog.excluded_providers in the TUI /model picker's unconfigured rows
#133941
fix(desktop): a session-picker click re-selects the active session
#120952
fix(desktop): preserve caret only across same-draft scope rekeys
#98515
fix(desktop): avoid Windows SSH probe command-line limit
#133940
fix(bundle): unblock macOS channel builds and bundled desktop smoke, add signing progress logs
#132354
Desktop update hand-off scripts hold the update marker as a lock and report committed updates as committed
#132345
fix(desktop): update gate waits for a live updater; hand-off needs the script to take the marker
#133807
Desktop web picker stops marking unconfigured providers active or ready (#132526, salvage #112022)
#133783
Desktop web picker marks the rows really serving search and extract (#132511, salvage #132519)
#133773
Desktop: choose your own key or the Nous Tool Gateway for web search and extract separately (#100513)
#132747
Add plugin-catalog entry: usage-flame — pinned subscription-limits chip & panel (community, desktop)
#133674
fix(desktop): opening a preview no longer flips the focused chat between tiles (#132550, salvage #132763)
#133585
Desktop Bot Chat with a remote bot resumes on its own connection again (Desktop core E2E red on main)
#133566
feat(plugins): plugin aux slots inherit a built-in slot and show up in Dashboard/Desktop aux settings
#133043
fix(desktop): a hidden window no longer drops its own healthy gateway socket
#133035
Provider sign-in cancels and lapsed codes count as abandoned, not failed (Desktop, dashboard, CLI)
#132018
fix(desktop): distinguish backend connection from messaging-gateway health [risk 0.65]
#132019
fix(desktop): keep completion notification body off the session title [risk 0.65]
#131996
fix(desktop): sync the live composer draft on press so a stalled flush can't disable Send [risk 0.60]
#131999
fix(desktop): keep the chat scrollbar off the right-sidebar sash [risk 0.60]
#132017
fix(desktop): drop stale persisted session owner hints on resume [risk 0.60]
#132007
fix(desktop): truncate cron text on Unicode boundaries [risk 0.60]
#132870
fix(desktop): keep sidebar pin toggles from reverting after the write guard [risk 0.50]
#132013
fix(desktop): keep SSH Windows probe stable against CLIXML progress-stream pollution [risk 0.50]
#132009
fix(desktop): paginate archived sessions [risk 0.50]
#132000
fix(desktop): refresh readiness on OAuth success so a stale credential failure clears while unfocused [risk 0.50]
#131917
fix(desktop): Nous recommended default skips Anthropic frontier tiers [risk 0.30]
#132010
fix(desktop): preserve typed Windows SSH probe errors [risk 0.20]
#133518
Desktop shared-metrics strip retires on the focused profile instead of coming back forever (#130714, salvage #130809)
#133182
feat(desktop): Settings ▸ Plugins — one pane for every plugin's settings pages (WoW AddOns style)
#128834
fix(tui_gateway+desktop): pooled profile sessions land in their own workspace
#133453
fix(desktop): count limited accounts in credential-pool pickers
Gateway, channels & integrations
#133936
fix(pty): clean up channel marker files on every session end path
#133948
fix(gateway): a channel_overrides model no longer evicts the cached agent after every turn
#132338
fix(update): a killed Windows updater no longer strands paused gateways, and never resumes them onto a torn tree
#133710
fix(tui_gateway): a prompt sent during a manual /compress waits for it and keeps its reply (#133504)
#133721
fix(telegram): reconnects no longer stall the gateway loop on TLS setup (#133339, salvage #133340)
#133694
fix(gateway): Telegram messages held by a failed reconnect attempt are delivered after the reconnect instead of lost (#133399)
#133645
fix(discord): a programmatic voice join binds the requested text channel on every path
#133213
Discord buttons stop accepting a user revoked after connect (salvage #132801)
#133598
fix(gateway): voice turns drop the /voice join message id and name uncached speakers
#133478
fix(discord): a role-authorized member's speech, native slash commands and /thread starters reach the agent
#133563
feat(plugins): inject_message(origin=...) starts a gateway session in the plugin's own profile
#133471
fix(discord): an utterance transcribed across a /voice join rebind is not posted to the new channel
#133470
fix(voice): one Discord bot's transcript dedup no longer drops another bot's turn
#133023
fix(whatsapp): a missing aiohttp no longer loops the bridge forever — PM installs it or a named error stops it (#126358, salvage #131431)
#133532
MCP read-only tools on untrusted servers stop asking for approval under mcp 2.x (salvage #111270)
#131891
fix(mcp): make sampling.tools capability opt-in via expose_client_tools [risk 0.30]
#131890
fix(processes): signal a process group only when the child leads it [risk 0.35]
#131833
fix(discord): track live voice credentials across re-keys instead of snapshotting at start() [risk 0.30]
#106856
fix(gateway): tolerate unresolvable UIDs in launchd plist path lookup (#57292)
#133469
fix(gateway): a thread's own channel skill binding wins over its parent's in any config order
#133463
fix(discord): slash, /thread and voice turns carry a message turn's prompt inputs
#133411
fix(discord): an auto-threaded mention reads the new thread's topic
Core runtime, state & reliability
#133991
fix(dashboard): attribute models analytics per API call from session_model_usage
#133952
fix(scratch): record every pruned entry and reaped process in logs/scratch-prune.log
#133975
fix(tools): a task's own patch keeps its full-file write baseline
#132299
fix(stt): normalize local language hints
#133958
fix(dashboard): route native text paste through term.paste to stop last-char duplication (#52471)
#134007
fix(sessions): validate imported values before persistence
#133934
fix(dashboard): don't 500 file listings on dangling symlinks or vanished entries
#133938
fix(dashboard+auth): cap HTTP JSON response body reads
#133997
fix(dashboard): surface the messaging platform's auth posture in the Test result
#133996
fix(dashboard): preserve CLI-configured custom endpoints on same-endpoint model/set
#133981
fix(dashboard): backfill /api/sessions/search with title matches
#133980
fix(web): preserve repeat count when creating cron jobs from dashboard
#133937
fix(dashboard): gate the chat xterm WebGL renderer and fall back to DOM
#133944
fix(state): chain-aware dashboard session deletes; stats exclude compression children
#133961
fix(dashboard): badge follows the PTY runtime model, not config, during fallback
#133960
fix(web): make the chat composer usable by screen readers (xterm screenReaderMode)
#133869
fix(dashboard): confine fs preview and git diff reads to the managed root
#133903
fix(dashboard): auth URLs honour X-Forwarded-Prefix behind reverse-proxy subpath
#133899
fix(dashboard): serve SPA assets with explicit MIME types
#133870
fix(dashboard): move CORSMiddleware outermost so OPTIONS preflights bypass auth
#133865
fix(dashboard-auth): bound password-login rate buckets
#133863
fix(dashboard-auth): serve plugin assets through the OAuth gate
#133873
fix(dashboard-auth): clock-skew leeway for JWT verification; classify not-yet-valid tokens as validation failures
#133928
fix(dashboard-auth): rotate dashboard-auth.log at 5MB/3 backups
#133847
fix(dashboard): release the stranded PTY holding a resumed chat's lease
#129397
fix(web): ignore replayed sidebar connection state
#133822
Mem0 installs from Mem0's own catalog plugin; core no longer bundles it
#133573
fix(bedrock): route GPT-6 family and prefixed OpenAI inference profiles, size their 1M window
#132365
fix(update): update marker v2 (owner liveness, no age ceiling) + checkout lock held by the whole update tree
#133789
PRs with CI from before a new required job no longer merge on that stale green (required check → v2)
#132386
fix(update): after the commit point nothing fails hermes update (C3)
#133743
Ctrl+D leaves a menu like Esc instead of redrawing forever once raw mode is on
#133760
revert: back out #133714 (merged accidentally; still under review)
#133733
hermes update: the parked-branch check no longer lazy-fetches on git builds without GIT_NO_LAZY_FETCH (#124767, salvage #126693)
#133403
plugin-catalog: bump evalroute to v0.6.4
#131827
feat(catalog): add limbic entry
#125521
feat(plugin-catalog): add hermes-tenuo
#133161
fix(catalog): update Resetwatch to 0.2.21
#132936
feat(plugin-catalog): add session-lens
#132312
Update hermes-monitor to v0.3.5
#126525
feat(catalog): add hermes-gemini-live
#126198
feat(plugin-catalog): add openclawcash-agentwallet
#133571
Shared-metrics offer asks once more where a "No thanks" may never have been seen
#133498
feat(plugin-catalog): bump pushover-hermes-plugin to 1.2.0
#133414
catalog: gods-eye-view v0.1.3 (upstream embed mode)
#133384
feat(plugin-catalog): add stt-vocab
#133359
feat(plugin-catalog): bump plan-mode to 0.3.3
#133330
feat(plugin-catalog): add the stream-speed catalog card
#133322
feat(plugin-catalog): bump redaction-pack to 1.3.0
#133237
plugin-catalog: bump hermes-slash-router to v0.3.1
#133235
plugin-catalog: hermes-review-loop 0.1.1 (re-pin)
#133072
Add pdf-surgeon to the plugin catalog (community, tier: community)
#132991
plugin-catalog: re-pin agora to v2.0.9 (fix #3 dashboard 500, fix #5 completion gate)
#132619
feat(catalog): add Tabro local browser automation plugin
#133559
fix(catalog): refresh Parallel Search listing status
#133524
feat(plugin-catalog): add bento plugin
#133356
feat(plugin-catalog): add stalkchain plugin
#133335
feat(plugin-catalog): add error-ledger
#133214
feat(plugin-catalog): add hermes-teammates plugin
#133144
plugin-catalog: add session-token-counter
#132378
hermes update: the parked-branch check no longer lazy-fetches a partial clone into a 180 GiB pack runaway (#131444, salvage #124777)
#133717
catalog: bump honcho (pin 3dd3b7a) (salvage #133486)
#133718
feat(plugin-catalog): add fxmacrodata (salvage #133564)
#133579
Windows updates from an old Python 3.11 install no longer fail certificate checks on GitHub downloads (salvage #133497)
#133704
fix(compaction): two working fallback summaries no longer block automatic compaction (salvage #129431)
#133653
Solstice ships as a self-contained plugin, hidden until sign-in, with token refresh and aux support (salvage #131402)
#133593
fix(build): a gutted node_modules package no longer fails every hermes update (#128935, salvage #128946)
#133650
Pack cleanup stops duplicating the update's tmp-pack sweep (follow-up to #133567)
#133648
fix(process): a kill's result stands on every backend, and a failed scope stop never counts as stopped
#133534
fix(auxiliary): support MiniMax OAuth side tasks [risk 0.80]
#133562
feat(plugins): let plugins register Automation Blueprints via ctx
#133567
Treeless installs convert before the update's dependency steps and on installer re-runs (#129514, salvage #132428)
#133556
Computer use: plugins can ship the one active driver (computer_use.backend)
#133552
feat(browser): public CDP call seam for trusted plugins (salvage #132752)
#131927
feat(qqbot): add support for proactive media delivery via send_message [risk 0.70]
#133551
CLI shared-metrics offer is no longer answered by an Enter typed during startup
#133042
Messaging platform health counts one failed connect per outage, not per reconnect retry
#133068
Installing a built-in skill by name (computer-use, pdf, …) makes it available instead of always failing; failed hub installs exit non-zero (#118301, salvage #128140)
#133032
fix(compression): serialize plugin loads and exempt persistence-isolated forks from checkpoint_required (salvage #131509)
#133038
Memory writes stop failing on hand-formatted files, and refused writes say exactly what to fix (#107270, #90468)
#133022
A revoked GITHUB_TOKEN no longer breaks skills installs: falls through to gh auth / anonymous and names the rejected credential (#98725)
#133019
fix(pm): one failing pin no longer blocks every other pm update pin (#125386, salvage #125400)
#133484
fix(build,pm): wait out Windows scanner holds on fresh-tree renames
#132008
fix: deduplicate project folders in sidebar across profiles [risk 0.60]
#131908
fix(skills): make env_passthrough registrations visible across tool context snapshots [risk 0.30]
#103650
fix(verify): clear workspace stale after hermes verify on another session
#131926
fix(runtime): read the OpenRouter fallback keys from .env after an exhausted pool entry [risk 0.30]
#132015
fix(nous): list on-sale models in the paid-tier picker [risk 0.35]
#132002
fix(serve): reap orphaned host owner instead of looping observe-only [risk 0.30]
#131800
fix(config): serialize .env read-modify-write cycles with a file lock [risk 0.30]
#131893
fix(runtime): normalize dual-surface base URLs for OpenAI chat-completions [risk 0.30]
#131802
fix(net): sanitize bracketed-IPv6 NO_PROXY entries so bare httpx clients construct [risk 0.25]
#133451
fix(plugins): catalog dependencies resolve without test-tool conflicts
#133434
fix(process): a completion is published once, by its owner, with its final output
Maintenance, documentation & formatting
#133802
fmt(js):
npm run fix
auto-fix
#133774
test(e2e): interactive suites no longer stall on the shared-metrics re-ask (main red since #133571)
#133780
fmt(js):
npm run fix
auto-fix
#132912
test(desktop): accept the attached host backend in macOS update smoke
#133714
test: pin each provider's wire, real error bodies, and the prompt-cache prefix contract
#133555
chore(plugin-catalog): update Gmail to v1.0.15
#133443
chore(plugin-catalog): bump pinned-folders entry sha to v0.1.3
#133368
chore(plugin-catalog): crew card image and screenshot, re-pin to 2f82dcd
#133341
chore(plugin-catalog): repin apify to a3a7af0c (0.1.5)
#133302
chore(catalog): update hermes-memory-ui to v0.6.3
#133329
chore(catalog): pin pass-secrets @ 485f105 after publish-identity scrub
#133708
docs(user-stories): add 45 business and professional stories
#133225
test(desktop): settle the render-count test past the code-plugin swap
#133416
fmt(js):
npm run fix
auto-fix
Source
GitHub merged-PR search for this exact window
Window:
2026-10-05T17:30:00Z
through
2026-10-06T17:30:00Z
(end exclusive)
Plain-English summary
If technical terms are not your thing: this is mostly maintenance, not 187 brand-new features.
The fixes cover model connections and routing, agent behavior and skills, desktop and interface issues, gateways and integrations, core reliability, state, and recovery, and maintenance, tests, and documentation. In practical terms, they aim to deliver better model and provider compatibility, more complete responses, tool calls, and long-running work, fewer desktop and interface glitches, smoother gateways and integrations, safer state and recovery behavior, and security fixes for specific risks called out in the log.
You only need to open an individual PR if it mentions a feature or problem you care about.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wz8pi2/187_hermes_agent_prs_merged_in_the_last_24_hours/)
