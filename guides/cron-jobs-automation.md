# Hermes Agent Cron Jobs & Automation: Recipes, Scheduling, and Best Practices

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to Hermes Agent cron jobs: syntax, scheduling, 10 real automation recipes, chaining jobs, debugging failures, and best practices for 24/7 autonomous workflows.

---

## Table of Contents

- [What Are Hermes Cron Jobs?](#what-are-hermes-cron-jobs)
- [Cron Job Syntax and Scheduling](#cron-job-syntax-and-scheduling)
- [Creating Your First Cron Job](#creating-your-first-cron-job)
- [10 Real Automation Recipes](#10-real-automation-recipes)
  - [1. Daily News Briefing](#1-daily-news-briefing)
  - [2. GitHub PR Monitor](#2-github-pr-monitor)
  - [3. System Health Watchdog](#3-system-health-watchdog)
  - [4. Email Digest](#4-email-digest)
  - [5. Website Change Monitor](#5-website-change-monitor)
  - [6. Daily Journal Prompt](#6-daily-journal-prompt)
  - [7. Weather and Calendar Summary](#7-weather-and-calendar-summary)
  - [8. Stock/Crypto Price Alert](#8-stockcrypto-price-alert)
  - [9. Automated Backups](#9-automated-backups)
  - [10. Reddit Community Monitor](#10-reddit-community-monitor)
- [Chaining Cron Jobs](#chaining-cron-jobs)
- [Script-Only Jobs (No Agent)](#script-only-jobs-no-agent)
- [Managing Cron Jobs](#managing-cron-jobs)
- [Debugging Failing Jobs](#debugging-failing-jobs)
- [Delivery and Notifications](#delivery-and-notifications)
- [Best Practices](#best-practices)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## What Are Hermes Cron Jobs?

Cron jobs are **scheduled automations that run even when you're not at your computer**. Hermes's built-in scheduler can:

- Run an agent task on a recurring schedule (every hour, daily, weekly)
- Execute a script and deliver the output
- Chain jobs together so the output of one feeds into the next
- Deliver results to Telegram, Discord, Slack, email, or SMS

**Why this matters:** Regular chatbots only respond when you message them. Hermes can proactively do work — checking your PRs every morning, monitoring websites for changes, fetching news, running system health checks — all without you touching a keyboard.

### Cron Jobs vs. Other Hermes Features

| Feature | When to Use |
|---------|------------|
| **Cron jobs** | Recurring scheduled tasks (daily digest, hourly monitor) |
| **delegate_task** | One-off parallel subtasks during a session |
| **Background terminal** | Long-running single commands |
| **Gateway messages** | On-demand tasks you trigger from your phone |

---

## Cron Job Syntax and Scheduling

Hermes supports four scheduling formats:

### 1. Duration Format

```bash
"30m"     # Every 30 minutes
"2h"      # Every 2 hours
"45m"     # Every 45 minutes
```

### 2. "Every" Phrase Format

```bash
"every 2h"              # Every 2 hours
"every monday 9am"      # Every Monday at 9 AM
"every weekday 8am"     # Monday-Friday at 8 AM
"every day 6pm"         # Daily at 6 PM
```

### 3. Cron Expression (5-field)

```bash
"0 9 * * *"       # Daily at 9:00 AM
"0 */6 * * *"     # Every 6 hours
"*/15 * * * *"    # Every 15 minutes
"0 8 * * 1-5"     # Weekdays at 8:00 AM
"0 0 1 * *"       # Midnight on the 1st of every month
```

Fields: `minute hour day-of-month month day-of-week`

### 4. ISO Timestamp (One-Shot)

```bash
"2026-07-25T14:00:00"   # Runs once at this exact time
```

---

## Creating Your First Cron Job

### Via CLI

```bash
# Daily at 8 AM: search for AI news and save a summary
hermes cron create "0 8 * * *" \
  --prompt "Search the web for today's top 5 AI and tech news stories. Write a 2-paragraph summary of each and save the result to ~/briefings/$(date +%Y-%m-%d)-news.md"
```

### Via In-Session Slash Command

```
/cron
```

Opens an interactive cron manager inside your Hermes session.

### Via the Tool (in conversation)

```
Create a cron job that runs every morning at 7 AM, checks the weather in St. Petersburg FL, and saves it to ~/weather/daily.md
```

### Verify It's Scheduled

```bash
hermes cron list
```

Output shows job IDs, schedules, last run status, and next run time.

---

## 10 Real Automation Recipes

Each recipe is a complete, copy-paste cron job you can create right now.

### 1. Daily News Briefing

```bash
hermes cron create "0 7 * * *" \
  --name "daily-news" \
  --prompt "Search the web for today's top 10 news stories across technology, science, and world events. For each story, write a 3-sentence summary and include the source URL. Format as markdown and save to ~/briefings/$(date +%Y-%m-%d)-daily-news.md. If the file already exists, append a 'LATE UPDATE' section instead."
```

### 2. GitHub PR Monitor

```bash
hermes cron create "0 9,14,18 * * 1-5" \
  --name "pr-monitor" \
  --prompt "Check the GitHub repo nousresearch/hermes-agent for any new or updated pull requests since the last check. For each PR, extract: title, author, number of files changed, and whether CI is passing. Save the summary to ~/monitors/pr-activity.md. If there are new PRs, note them prominently at the top."
```

### 3. System Health Watchdog (Script-Only)

This uses a script instead of an agent — faster, cheaper, more reliable for system checks.

First, create the script at `~/.hermes/scripts/health-check.sh`:

```bash
#!/bin/bash
# Health check: disk, memory, CPU, and running services

DISK=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
MEM=$(vm_stat | awk '/free/ {print $3}' | sed 's/\.//')
LOAD=$(sysctl -n vm.loadavg | awk '{print $2}')

if [ "$DISK" -gt 90 ]; then
  echo "WARNING: Disk usage at ${DISK}%"
fi

if [ "$LOAD" > "3.0" ]; then  # intentional string compare for bc-free threshold
  echo "WARNING: High CPU load: $LOAD"
fi

echo "Health check complete. Disk: ${DISK}%, Load: $LOAD"
```

Then schedule it:

```bash
hermes cron create "0 * * * *" \
  --name "health-watchdog" \
  --script ~/.hermes/scripts/health-check.sh \
  --no_agent true
```

With `--no_agent true`, the script runs directly — no LLM involved. Non-empty stdout is delivered. Empty stdout = silent (nothing to report).

### 4. Email Digest

Requires: `himalaya` skill installed and email configured.

```bash
hermes cron create "0 8,17 * * *" \
  --name "email-digest" \
  --prompt "Check my email inbox for new messages since the last check. Summarize each unread email in one sentence: sender, subject, and whether it needs a response. Save to ~/digests/email-$(date +%H%M).md. Flag anything marked urgent or from my manager at the top." \
  --skills "himalaya"
```

### 5. Website Change Monitor

```bash
hermes cron create "0 */4 * * *" \
  --name "site-monitor" \
  --prompt "Navigate to https://nousresearch.com. Check if there are any new blog posts, announcements, or product changes since the last run. Compare against ~/monitors/nousresearch-state.md (the last known state). If there are changes, update the state file and list the changes prominently. If nothing changed, just note 'No changes detected' at the bottom."
```

### 6. Daily Journal Prompt

```bash
hermes cron create "0 21 * * *" \
  --name "journal-prompt" \
  --prompt "Generate 3 reflective journal prompts for today. They should be specific to the date and any notable events (check the web for today in history). Save them to ~/journal/$(date +%Y-%m-%d)-prompts.md. Include a brief 'Today In History' section with 3 interesting facts."
```

### 7. Weather and Calendar Summary

```bash
hermes cron create "0 6 * * *" \
  --name "morning-brief" \
  --prompt "Check today's weather forecast for my location. Also check my calendar for today's events. Combine into a morning brief: weather summary at top, then today's schedule, then a 1-line reminder about any preparation needed (umbrella? jacket? meeting prep?). Save to ~/briefings/today-$(date +%Y-%m-%d).md."
```

### 8. Stock/Crypto Price Alert

```bash
hermes cron create "0 */2 * * *" \
  --name "price-alert" \
  --prompt "Check current prices for BTC, ETH, and NVDA. Compare against the alert thresholds in ~/monitors/price-alerts.json. If any price crosses a threshold (above or below), write an alert to ~/alerts/price-$(date +%Y%m%d-%H%M).md and flag it as urgent. Otherwise, just append the current prices to ~/monitors/price-history.csv silently."
```

### 9. Automated Backups

```bash
hermes cron create "0 2 * * *" \
  --name "daily-backup" \
  --prompt "Create a compressed backup of ~/Atlas/, ~/.hermes/skills/, and ~/.hermes/config.yaml. Save to ~/backups/backup-$(date +%Y-%m-%d).tar.gz. After creating the backup, delete any backups older than 30 days. Verify the backup file is non-zero size before declaring success."
```

### 10. Reddit Community Monitor

```bash
hermes cron create "0 10,16,22 * * *" \
  --name "reddit-monitor" \
  --prompt "Check r/hermesagent for new posts in the last 6 hours with score > 10. For each qualifying post, extract: title, author, score, comment count, and flair. Also check for any posts that might need moderator attention (reports, rule violations). Save summary to ~/monitors/subreddit-activity.md."
```

---

## Chaining Cron Jobs

Hermes supports chaining jobs together so the output of one feeds into the next. This is powerful for multi-stage pipelines.

### How Chaining Works

Job A runs, completes, and saves its output. Job B is configured with `context_from` pointing to Job A's ID — it receives Job A's most recent output as context before running.

### Example: Morning Brief Pipeline

```bash
# Job 1: Fetch weather (runs at 6:00 AM)
hermes cron create "0 6 * * *" \
  --name "fetch-weather" \
  --prompt "Fetch today's weather forecast and save to ~/pipeline/weather.json"

# Job 2: Fetch calendar (runs at 6:02 AM)
hermes cron create "2 6 * * *" \
  --name "fetch-calendar" \
  --prompt "Fetch today's calendar events and save to ~/pipeline/calendar.json"

# Job 3: Compose briefing using both (runs at 6:05 AM)
hermes cron create "5 6 * * *" \
  --name "compose-briefing" \
  --prompt "Combine the weather data and calendar events into a formatted morning briefing. Save to ~/briefings/today.md." \
  --context_from "fetch-weather,fetch-calendar"
```

### Tips for Chaining

- **Stagger start times** — give upstream jobs time to complete (2-3 minutes between dependent jobs)
- **Use `context_from`** — it injects the upstream output into the downstream job's prompt
- **Jobs run independently** — the scheduler doesn't wait for upstream jobs; it grabs the most recent completed output
- **Keep jobs idempotent** — if an upstream job fails, the downstream job should still handle stale data gracefully

---

## Script-Only Jobs (No Agent)

For simple, deterministic checks, script-only jobs are faster and don't consume any LLM tokens.

### When to Use Script-Only

| Use Script-Only | Use Agent Job |
|----------------|---------------|
| System health checks (disk, memory, CPU) | News summaries and digests |
| API status polling (is endpoint up?) | Content generation and writing |
| File system monitoring (new files?) | PR review and code analysis |
| Simple data collection (fetch and store JSON) | Multi-step research tasks |
| Watchdog alerts (threshold exceeded) | Context-aware responses |

### Creating a Script-Only Job

```bash
hermes cron create "*/5 * * * *" \
  --name "api-health" \
  --script ~/.hermes/scripts/api-health.sh \
  --no_agent true \
  --deliver "telegram"
```

**Rules for script-only jobs:**
- Non-empty stdout is delivered verbatim as the message
- Empty stdout = silent (nothing delivered) — design your script to be quiet when nothing's wrong
- Non-zero exit code triggers an error alert
- The `--prompt` and `--skills` flags are ignored (there's no agent to receive them)

---

## Managing Cron Jobs

### List All Jobs

```bash
hermes cron list          # Active jobs
hermes cron list --all    # Including disabled
```

### View Job Details

```bash
hermes cron edit <job-id>   # Opens interactive editor for schedule, prompt, delivery
```

### Control Jobs

```bash
hermes cron pause <job-id>    # Pause without deleting
hermes cron resume <job-id>   # Resume a paused job
hermes cron run <job-id>      # Trigger immediately (once)
hermes cron remove <job-id>   # Delete permanently
```

### Check Scheduler Status

```bash
hermes cron status
```

Shows the scheduler process status, uptime, and recent job execution history.

### In-Session Cron Management

```
/cron list
/cron run <job-id>
/cron pause <job-id>
```

---

## Debugging Failing Jobs

### 1. Check Last Run Status

```bash
hermes cron list
```

Look at the `last_status` column. Common statuses:

| Status | Meaning |
|--------|---------|
| `completed` | Ran successfully |
| `error` | Failed during execution |
| `timeout` | Exceeded 3-minute hard limit |
| `skipped` | Previous run still in progress |

### 2. Check Gateway Logs

```bash
grep "cron" ~/.hermes/logs/gateway.log | tail -30
```

### 3. Verify the Job Config

```bash
hermes cron edit <job-id>
```

Check that:
- The schedule is valid
- The prompt is self-contained (cron jobs have no conversation context)
- If using scripts, the script path exists and is executable
- If using skills, the skill names are spelled correctly

### 4. Run It Manually

```bash
hermes cron run <job-id>
```

This triggers the job immediately so you can see the output.

### 5. Check for Script Path Issues

Script-only jobs with invalid paths show as errors:

```bash
# Check if the script exists
ls -la ~/.hermes/scripts/health-check.sh
```

### Common Failure Causes

- **Script not found:** The script path in the cron job doesn't exist — likely an orphaned job from a deleted project. Remove it.
- **API key missing:** A job that calls an API but the key isn't in `.env`
- **Model unavailable:** The configured model/provider is unreachable
- **Disk full:** Job can't write output files
- **Timeout:** Job exceeded 3-minute execution limit (split into smaller jobs or use a script)
- **Paused job:** The job is paused — `hermes cron list` shows `paused` status

---

## Delivery and Notifications

### Default Delivery

By default, cron job results are delivered back to the chat/channel where they were created.

### Custom Delivery Targets

```bash
# Deliver to Telegram
hermes cron create "0 8 * * *" --prompt "..." --deliver "telegram"

# Deliver to Discord
hermes cron create "0 8 * * *" --prompt "..." --deliver "discord:#general"

# Deliver to all connected platforms
hermes cron create "0 8 * * *" --prompt "..." --deliver "all"

# Deliver to specific Telegram topic
hermes cron create "0 8 * * *" --prompt "..." --deliver "telegram:-1001234567890:17585"
```

### Delivery Options

| Value | Behavior |
|-------|----------|
| (omitted) | Auto-deliver to origin chat |
| `local` | Save only, no delivery |
| `all` | Fan out to every connected platform |
| `origin` | Same as omitting |
| `telegram` | Deliver to connected Telegram |
| `telegram:chat_id:thread_id` | Specific Telegram chat/thread |
| `discord:#channel` | Specific Discord channel |

---

## Best Practices

### 1. Keep Prompts Self-Contained

Cron jobs run in fresh sessions with no conversation history. Every prompt must include all necessary context:

**Bad:** "Summarize the PRs like we discussed"
**Good:** "Check the GitHub repo nousresearch/hermes-agent for open PRs. For each PR, extract the title, author, and CI status. Save to ~/pr-summary.md."

### 2. Set Realistic Schedules

Don't run a complex agent task every 5 minutes — it'll burn through API credits and may not finish before the next tick. A good rule of thumb:

| Task Complexity | Minimum Interval |
|----------------|-----------------|
| Simple API check | 5 minutes |
| Web search task | 15 minutes |
| Multi-step research | 1 hour |
| Code generation | 2 hours |

### 3. Use Script-Only for Simple Checks

Don't burn LLM tokens on "is the disk full?" checks. Use `--no_agent true` with a simple bash script.

### 4. Stagger Heavy Jobs

Don't schedule 5 complex tasks at the same minute — they'll compete for resources. Space them out by 2-5 minutes.

### 5. Set Up Error Notifications

Configure failing jobs to notify you:

```bash
hermes cron create "..." --prompt "..." --deliver "telegram"
```

A silent cron job that fails is worse than no cron job — you'll assume everything's fine.

### 6. Clean Up Stale Jobs

Remove jobs you no longer need. A job that references a deleted script, monitors a retired service, or was created for a one-off project should be cleaned up:

```bash
hermes cron list --all | grep -i error
hermes cron remove <stale-job-id>
```

### 7. Pin Stable Models

If you switch your main model frequently, pin cron jobs to a specific model to avoid surprises:

```bash
hermes cron create "0 9 * * *" \
  --prompt "..." \
  --model "{\"provider\": \"anthropic\", \"model\": \"claude-sonnet-4-20250514\"}"
```

### 8. Test Before Scheduling

Run the job manually once before setting it on a recurring schedule:

```bash
hermes cron run <job-id>
```

Check the output. If it looks right, leave it scheduled. If not, edit and re-test.

---

## FAQ

### Can cron jobs run when my computer is asleep?

No. Cron jobs run on the machine where Hermes is installed. If your Mac sleeps, cron jobs pause. For 24/7 uptime, run Hermes on an always-on machine (home server, VPS, or a dedicated Mac Mini). See the [Multi-Machine Setup Guide](wiki/multi-machine-setup) for always-on configurations.

### How many cron jobs can I have?

There's no hard limit. However, jobs that run simultaneously compete for resources (CPU, memory, API rate limits). For typical setups, keep concurrent jobs under 5 for smooth operation.

### Do cron jobs use my main model or a separate one?

By default, cron jobs use the model that was active when you created them (pinned at creation time). You can override per-job with `--model`. Cron jobs do NOT use a separate model unless you explicitly configure one.

### Why did my cron job not run?

Common reasons: (1) the job is paused — check with `hermes cron list`, (2) the scheduler isn't running — check with `hermes cron status`, (3) the gateway process isn't running, (4) the job's schedule hasn't been reached yet, (5) a previous run is still in progress.

### Can cron jobs access my files?

Yes — cron jobs have the same tool access as regular sessions (terminal, file system, browser, web search). This is why self-contained prompts are important: the job doesn't know what you were working on in your last conversation.

### What's the maximum runtime for a cron job?

3 minutes hard limit per run. If your task takes longer, break it into smaller jobs (chain them with `context_from`) or use a script.

### Can I get cron job results on my phone?

Yes. Set `--deliver "telegram"` (or Discord/Slack) and the job's output will arrive as a message on your phone. See the [Telegram Gateway Setup Guide](wiki/telegram-gateway-setup).

### How do I pause all cron jobs temporarily?

There's no global pause command. Pause individual jobs with `hermes cron pause <id>`. To pause everything, stop the gateway: `hermes gateway stop`.

### Do cron jobs share context with my active sessions?

No. Each cron job runs in a completely fresh session — no memory of your conversations, no access to your active session's state. This is by design to keep cron jobs deterministic and self-contained.

### Can I use cron jobs with local models?

Yes. If your default model is local (LM Studio, Ollama), cron jobs will use it. Make sure your local model server stays running — cron jobs can't start LM Studio for you.

---

## Next Steps

**Cron jobs deliver results to you automatically. Set up the delivery channel:**

1. **[Telegram Gateway Setup →](wiki/telegram-gateway-setup)** Get cron results on your phone
2. **[Skills Guide →](wiki/skills-guide)** Use skills inside cron jobs for domain expertise
3. **[Multi-Machine Setup →](wiki/multi-machine-setup)** Run cron jobs on an always-on server

**Also see:** [Start Here](wiki/start-here) · [Model Guide](wiki/model-guide) · [50 Use Cases](wiki/use-cases) · [Official Cron Docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
