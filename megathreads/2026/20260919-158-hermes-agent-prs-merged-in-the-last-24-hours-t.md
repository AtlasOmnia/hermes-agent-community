---
title: "158 Hermes Agent PRs merged in the last 24 hours — through September 18, 2026, 1:30 PM ET"
author: u/Jonathan_Rivera
date: 2026-09-19
score: 5
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wjwoa6/158_hermes_agent_prs_merged_in_the_last_24_hours/
flair: "News — Official Releases, announcements, major changes"
---

# 158 Hermes Agent PRs merged in the last 24 hours — through September 18, 2026, 1:30 PM ET

**Posted by u/Jonathan_Rivera on 2026-09-19 · 5 points (85% upvoted) · 0 comments**

GitHub merged 158 pull requests in
NousResearch/hermes-agent
during the
24 hours ending September 18, 2026, 1:30 PM ET
. I grouped them by area below and sorted each section newest to oldest by merge time.
Models, providers & routing
#114887
fix(security): provider, model, pet and skills-hub URL fetches refuse internal targets (#114468, #44728, salvage #114469)
#114883
fix(runtime): local alias with no endpoint stops instead of routing to OpenRouter (#113703, salvage #113768)
#114868
fix(aux): a 401 on an explicit auxiliary provider walks that task's own fallback_chain (#114060, salvage #114066)
#114809
fix(config): malformed custom_providers no longer empties the providers view; config set refuses type mismatches; nested aliases keep key_env (#114605, #114471, salvage #45730, #109834)
#114806
fix(reasoning): custom-provider-prefixed reasoning_overrides keys apply to bare model ids (#114073, salvage #114084)
#114784
fix(gemini): Vertex AI express keys (AQ.) reach aiplatform instead of 403ing on AI Studio (#114335, salvage #96587)
#114742
fix: memory-provider migration checks presence in the profile being migrated
#115002
Remove the dead keyless opencode-free provider rather than patching it (salvage #114735, fixes #114753)
#114569
feat: memory providers that leave core are installed from the catalog automatically
#114333
A callable key_cmd credential survives every auxiliary custom-provider branch (#88667, credit #107344)
Prompts, skills & agent behavior
#114885
fix(agent): reversed 'reasoning_effort none unsupported' 400 now retries without reasoning on title generation and the main loop (#114460, salvage #114461)
#107234
fix(agent): preserve accepted steers across soft interrupt clears
#114840
fix(agent): a greeting opener no longer locks the session title (#113864, salvage #113876)
#114832
fix(agent): Perplexity Agent API tool calls and aux/MoA calls stop 400ing on reserved tool names (#114260, salvage #103775, #114457)
#114829
fix(delegation): Anthropic child gets its goal once and refusals show stop_details (#113689, salvage #113693, #108682)
#114823
fix(compression): aux summariser clamp survives model switches and is re-checked at switch time (#114707, salvage #114710)
#114777
fix(skills): shell snippets paste cleanly and OS-bound skills stop claiming platforms they cannot run on (#113448, #113449, salvage #113710, #113464)
Desktop & UI
#114892
fix(cli): a benched or signed-out credential prints its reason and cooldown instead of the first-run provider wizard (#113720, supersedes #113732)
#114888
fix(tui): project-local skills register and dispatch with the default terminal.cwd placeholder (#114359, salvage #96514)
#114881
fix(desktop): serve/Desktop sessions keep their own profile's persistent-Docker container instead of collapsing onto default (#114724, salvage #73051)
#114876
fix(desktop): sessions opened behind dashboard login record the logged-in user_id (#114378, salvage #114398)
#114861
fix(cli): one malformed LaunchAgent plist no longer aborts update cleanup or dashboard --stop (#114142, salvage #114148)
#108156
fix(desktop): weakly retain transcript source arrays
#114834
fix(tui): /model picker keeps long model ids on the ❯ cursor row with their indent (#113759, salvage #113760)
#114830
fix(gateway, desktop): Discord turns persist and display the user's text, not the triggering-message note (#114719, #71304, salvage #71309)
#114828
fix(cli): Shift+symbol keys type their character under modifyOtherKeys=2 instead of leaking ESC[27;2;…~ (#114242, #102683, salvage #112526)
#114827
fix(desktop): stale Bot Mode session references stop being re-sent and mislogged as rejected RPCs on startup (#114694, salvage #114700)
#114826
fix(cli): hermes --help documents -p/--profile and the gateway service verbs (#114495, salvage #114497)
#114802
fix(desktop): update check and gh probes skip unlaunchable git/gh on PATH (#114718, salvage #114729)
#114799
fix(cli): startup auth fallback sends the fallback model its own reasoning effort (#113492, salvage #113497)
#114790
fix(desktop): Terminal backend picker confirms before persisting a needs-setup backend (#114275, salvage #114291)
#114772
fix(config): custom endpoints with dotted, colon or mixed-case keys activate, save and delete from Desktop (#114572, salvage #114573)
#114762
fix(mcp): Desktop and dashboard MCP re-auth show the real OAuth failure instead of 'callback did not include an authorization code' (#114727, salvage #114734)
#114758
fix(desktop): Windows SSH probe parses again — try/catch no longer split by ';' (#114015, salvage #102568)
#114329
Desktop gateway switch no longer keeps the previous gateway's workspace folder (#114306)
#115067
feat(connectors): the backend API for the desktop Connectors page; connect an app without a chat session
#115142
fix(desktop): ordinary peer windows keep the selected device on New session (salvage #115102)
#115026
fix(desktop): backgrounded primary sign-out is surfaced; portal login and forced renewal wait for a new access cookie
#114766
fix(desktop): Reconnect redials a rejected gateway session again (follow-up to #114666)
#114666
fix(desktop): handle Cloud auth migration and team changes
#103938
fix(cli): preserve startup alias base URL
#114358
fix(desktop): MEDIA paths with spaces render as one card, also mid-stream (#96657, salvage #96686)
#113247
fix(desktop): working WSLg window controls and native Wayland launch
#113950
fix(desktop): stranded-resume overlay offers Start new session instead of a Retry-only wall (partial #106217, salvage #107162)
#113954
Cross-connection message_agent reaches a Bot Chat open in Desktop instead of SESSION_NOT_OWNED (#113753)
#113956
Desktop: pooled-profile chats no longer land on the local primary and get refused SESSION_NOT_OWNED after reload (#101416 class)
#114302
fix(desktop): improve first-run onboarding
#101065
feat(desktop): per-project toggle for gitignored files in the file tree
Gateway, channels & integrations
#114894
fix(mcp): servers connect under the connection owner's profile scope instead of parking with UnscopedSecretError (#113746, salvage #113749)
#114893
fix(gateway): launchctl exit 5 over a supervised job no longer brands macOS launchd-unsupported or starts a detached duplicate (#114571, salvage #114577)
#114877
fix(telegram): split replies arrive once and complete under flood control — resume from the refused chunk, per-chat send order and cooldown (#114396, salvage #52095, #114512)
#114871
fix(feishu): rich-text posts keep their file attachments and report inlining honestly (#114176, salvage #114187)
#114865
fix(mcp): hermes mcp test exits 1 on connection failure and 3 on unknown server (#114230, salvage #70287)
#114855
fix(feishu): a websocket link lost mid-life is detected and rebuilt (#113662, salvage #113668)
#114854
fix(gateway): FTS rebuild retries on a cooldown instead of giving up for the process lifetime; stalled transcript appends escalate to ERROR (#114266, salvage #114301)
#114849
fix(mcp): stdio servers start in the session working directory, not the Hermes launch dir (#113888, salvage #113890)
#114838
fix(gateway-windows): a failed Startup-folder install leaves no Hermes_Gateway.tmp for Notepad to open at login (#114093, salvage #81511)
#114835
fix(teams): require_mention gates unmentioned channel and group-chat messages before attachment download (#113577, #114366, salvage #113591)
#114831
fix(state): profile delete/rename no longer fail on legacy Telegram topic tables (#113757, salvage #113767)
#114818
fix(mcp): Asana catalog entry installs the V2 server with a pre-registered OAuth client (#113907, salvage #113910)
#114815
fix(discord): missed-message backfill dispatches a message once, never on every reconnect (#113631, salvage #113633)
#114813
fix(dingtalk): edits without AI Cards return not-configured instead of warning every heartbeat (#113924, salvage #113929)
#114810
fix(slack): rich_blocks renders <url|label> autolinks as links inside lists, quotes and tables (#113761, salvage #113763)
#114808
fix(codex): a configured max reasoning effort reaches custom Responses relays instead of xhigh (#114249, salvage #114255)
#114804
fix(update): hermes update from v2026.9.14 finishes the gateway restart instead of dying on a stale utils (#114616, salvage #114653)
#114801
fix(telegram): approval buttons always arrive; the HTML card fits 4096 chars after escaping (#114036, salvage #35812, #114040)
#114800
fix(discord): exec approval shows the command and reason once, buttons and embed-free fallback kept (#114693, salvage #114699)
#114798
fix(cron): data files named in a python heredoc no longer trip the gateway lifecycle guard; refusals name their reason (#113944, salvage #114523)
#114797
fix(gateway): scale-to-zero no longer suspends while a direct platform is live in a served profile (#113546, salvage #113556, #113553)
#114791
fix(kanban): goal-mode complete/request-review no longer fails when the judge transport fails; headless judge carries the relay affinity key (#113669, #83610, salvage #113691, #78605)
#114780
fix(gateway): /stop, /new and /reset no longer drop a parked delegation-completion wake (#114456, salvage #114538)
#114779
fix(api-server): a contended Bot Chat resurrection write no longer stalls the gateway event loop (#113772, salvage #113777)
#114778
fix(cron): gateway_state.json and
hermes gateway status
report a watchdog-killed event loop as degraded, not running (#113372, salvage #113513, #113386)
#114774
fix(api): gateway shutdown leaves /v1/runs records terminal as interrupted, not running (#113541, salvage #113558)
#114765
fix(gateway): async completion no longer re-pins a route after /stop or /new won the race (#113690, salvage #113692, #113716)
#114761
fix(gateway): queued voice/video/document follow-ups each get their own turn in queue mode (#114363, salvage #65522)
#114754
fix(cron): restart-safe cron worker is reaped instead of lingering as a zombie under the gateway (#114509, salvage #114514)
#113052
fix(update): keep manual serve restart obligations visible through gateway recovery
#114889
fix(gateway): a /stop in a thread stops every run of that thread (#114721 follow-up)
#114721
fix(gateway): /stop stops a run in the same chat even when its key misses (#113738, salvage)
#113524
fix(slack): reopen a native task card when Slack seals the stream mid-turn
#114483
fix(slack): retain bearer on validated Enterprise Grid file redirects
#114413
fix(mcp): skip dynamic tool refresh when the server session is already gone
#114402
fix(gateway): watchdog falls back to wall-clock when no agent snapshot exists
#114370
feat(notifications): opt-in suppression of user-channel warning notifications (salvage #112302)
#114356
fix(discord): bot handoffs need a typed mention by default and arrive whole across chunks (salvage #106874, #27265)
#113974
fix(tui_gateway): isolated turns no longer fence themselves out of their own session lease (#101416, salvage #103737)
Core runtime, state & reliability
#114899
fix(browser): browser_get_images and multi-line eval scripts survive the Windows .cmd shim (#113838, salvage #113844)
#114898
fix(cron): bot-chat delivery books the bot's turn, not its exit linger — no more 600s timeouts on completed turns (#113608, supersedes #113649)
#114897
fix(browser): CDP supervisor stops retrying a dead endpoint after 5 failed reconnects (#114172, salvage #114178)
#114890
fix(tests): run_tests_parallel.py --help prints usage and unknown flags error out instead of sweeping the suite (#114059, salvage #114065)
#114886
fix(kanban): host spawn refusals no longer park cards as blocked; oneshot-unit dispatch workers survive unit exit (#114720, #113612, salvage #113624)
#114882
fix(kanban): dashboard sets, shows and unbinds a board's Project (#114652, salvage #114664)
#114879
fix(profiles): polled profile lists no longer walk skill trees; vanished skill dirs no longer abort enumeration (#114041, salvage #114044)
#114878
fix(auth): Nous 'not logged in' refresh failures leave rotation and name hermes auth add nous instead of a silent hour-long bench (#113718, salvage #113726)
#114875
fix(clarify): CLI clarify prompt honours agent.clarify_timeout instead of a hidden 120 s cap (#113873, salvage #72714)
#114874
fix(config):
config set platform_toolsets.<platform>
no longer flagged as an unrecognized key (#113658, salvage #89781)
#114873
fix(config,update): a broken SOUL.md symlink no longer bricks home init; failed pre-update snapshot warns loudly (#114592, salvage #114600, #108007)
#114869
fix(aux): caller thinking-off no longer ships beside a task reasoning.effort on custom profiles (#114020, salvage #114022)
#114866
fix(auth): /model and doctor status reads no longer refresh or bench a pool OAuth credential (#114323, salvage #114379)
#114864
fix(send): hermes send names the resolved home and the credential sources it read (#114272, salvage #114297)
#114862
fix(file-state): a finished cron run or subagent is no longer reported as a concurrent sibling writer (#114446, salvage #114470)
#114859
fix(file-safety): credential write guards cover the real home under profile-home deployments (#113628, salvage #113629)
#114851
fix(cron): no_agent scripts get the owning profile's declared secret, never the launch profile's (#114209, supersedes #114218)
#114850
fix(kanban): guarded or per-profile-capped review cards no longer starve the ready lane (#113598, salvage #113600)
#114848
fix(guardrails): file-tool loop refusals no longer count as failures or escalate to repeated_exact_failure_block (#113895, salvage #113897)
#114847
fix(tools): hermes send and send_message deliver text with lone surrogates instead of dropping it (#113799, salvage #113809)
#114846
fix(plugins): public repos install and update anonymously; stored git credential attached only when the remote refuses (#114526, salvage #114545)
#114845
fix(auth): revoked Codex grant names openai-codex, the failing profile and the raw error (#114012)
#114844
fix(tirith): circuit breaker half-opens and resumes scanning after transient failures (#113744, salvage #73167)
#114843
fix(tirith): emoji folder names no longer trigger a variation-selector approval prompt (#114039, salvage #114043)
#114839
fix(redact): dotted sk- keys and prefix-less Zhipu keys are fully masked in tool output (#113901, #78128, #106508, salvage #113908)
#114837
fix(cron): a completed run keeps its result when a fire-claim heartbeat sample misses (#113357, #105861, salvage #113364)
#114836
fix(bootstrap): cold start no longer stalls on a dead IPv6 route — every sync connect races IPv6/IPv4 (#114265, salvage #114277)
#114833
fix(tools): file tools keep working outside /workspace when terminal.cwd is a host path on the docker backend (#113894, #98723, salvage #113946, #113931)
#114825
fix(kanban): kanban.dispatch_profiles fails closed for a blank/null key and an unreadable config (#113620, salvage #113623)
#114824
fix(config): HERMES_HOME with a literal ~ resolves to the real home, not cwd (#114353, salvage #109212)
#114822
fix(kanban): decomposed children and the root card fall back to the root task's assignee, never the dispatcher's own profile (#114294, salvage #114303)
#114821
fix(tts): xAI streaming TTS uses XAI_API_KEY over the subscription OAuth bearer (#113727, salvage #113728)
#114820
fix(kanban): served profile's api_server session wake is delivered in its own scope under multiplex (#114679, salvage #114680)
#114812
fix(buzz): message edits publish the replacement text instead of a literal dash (#113909, salvage #113912, #113918)
#114811
fix(plugins): plugin listings stop paying one catalog timeout per installed plugin; hub rebuild leaves the event loop (#113677, #114106, salvage #113687, #113682)
#114807
fix(cron): a failing job alerts once per incident, then reminds on a cooldown (#113665, salvage #113685)
#114803
fix(dashboard): --stop and the update sweep stop only this home's backend, sparing foreign installs and the caller's shell (#113978, salvage #113982 #113994)
#114796
fix(codex): successful command exit status survives projected replay (#113871, salvage #111616)
#114795
fix(acp): concurrent Copilot ACP sessions no longer kill a sibling's process or leak their own (#114639, salvage #114640)
#114792
fix(cron): resume keeps a recurring slot that elapsed while paused due instead of skipping it silently (#113603, salvage #114296)
#114789
fix(cron): LLM job output is secret-redacted on every delivery lane — chat, session mirror, job name, Bot Chat (#113745, salvage #73026)
#114787
fix(file-sync): sync-back tolerates live sockets, reclaims hard-kill tars by owner PID, cap overridable (#114437, salvage #114440)
#114786
fix(kanban): kanban_link refuses a running child and dependency refusals name the open parents (#113374, #113373, salvage #113398, #113452)
#114785
fix(kanban): cards no longer carry a session id that no state.db resolves (#114092, salvage #114098)
#114782
fix(profiles): profile clone keeps NTFS skill junctions as junctions, no external-dirs name collision (#113471, salvage #113487)
#114775
fix(tools): tool_call parses a JSON-string calls envelope and its rejections restate the valid single-entry shape (#114484, #114646, salvage #114486)
#114773
fix(read_file): notebook output recovery hint names the original quoted notebook path (#113872, salvage #112678)
#114771
fix(read_file): XLSX/DOCX phonetic guides no longer appended to extracted text (#113875, salvage #113858)
#114770
fix(disk-cleanup): protected top-level dirs like cache/ survive cleanup; kanban/ is never tracked (#114552, supersedes #114555)
#114768
fix(kanban): stop guard no longer nudges a worker that handed its card to review (#114598, salvage #97753, #105708)
#114767
fix(kanban): dependency block with no open parent parks as needs_input and escalates instead of respawning forever (#114627, salvage #114529)
#114759
fix(cron,tools): a parseable non-dict JSON state file no longer wedges the Bot Chat drain or its 8 sibling scans (#114240, salvage #114241)
#114756
fix(auth): Codex device-code login survives transient transport blips instead of aborting the poll (#114610, salvage #114614)
#114755
fix(cron): ticker fires on a fixed period instead of drifting later each tick (#114467, salvage #114473)
#115179
Podman-only machines no longer report Docker as missing (dashboard, doctor, setup)
#112830
fix(cron): report satellite scheduler health and missed fires
#114726
fix(cron): a stale long-lived process no longer skips every job after an update (#114672, salvage #114675 #114692)
#114539
fix: installed directory plugin keeps its identity over a same-name pip entry point
#111219
fix(bedrock): restore Grok context and preserve confirmed cache limits
#114261
catalog: mnemosyne key goes to mnemosyne-oss; unaffiliated Devs-Foundation entry delisted
#114415
fix(state): name each writable SessionDB holder in the live-handles warning
#114427
fix(env): self-referential .env values resolve once per process instead of growing on every reload
#114332
A delivered cron run keeps its real status when the fire-claim sample misses afterwards (#105861, salvage #113283)
#114336
fix(local-runtime): resumed llamacpp sessions follow the live managed port on every surface
#114312
Parent session no longer inherits the delegate_task marker from the terminal snapshot (#90782, #71941; salvage #90786)
#114315
Gemini Standard-key guidance now surfaces on 400 API_KEY_INVALID (salvage #114233)
Maintenance, documentation & formatting
#114896
docs(portal): Profile setup describes the real per-profile sign-in instead of automatic cross-profile pickup (#114259, salvage #114273)
#114867
test(mcp): 2.0-only MCP tests skip with an actionable reason under an older installed SDK (#114132, salvage #114137)
#114819
test(agent): auxiliary cache-hint suite stays hermetic on hosts with a Claude Code login (#114424, salvage #114431)
#114781
docs(skills): coding-agent delegation skill defaults to permission prompts; bypass is an explicit opt-in (#113447, salvage #113464)
#114747
docs(security): how to re-request an approval after the prompt times out (#114204)
Source
GitHub merged-PR search for this exact window
Window:
2026-09-17T17:30:00Z
through
2026-09-18T17:30:00Z
(end exclusive)
Plain-English summary
If technical terms are not your thing: this is mostly maintenance, not 158 brand-new features.
The fixes cover model connections and routing, agent behavior and skills, desktop and interface issues, gateways and integrations, core reliability, state, and recovery, and maintenance, tests, and documentation. In practical terms, they aim to deliver better model and provider compatibility, more complete responses, tool calls, and long-running work, fewer desktop and interface glitches, smoother gateways and integrations, safer state and recovery behavior, and security fixes for specific risks called out in the log.
You only need to open an individual PR if it mentions a feature or problem you care about.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wjwoa6/158_hermes_agent_prs_merged_in_the_last_24_hours/)
