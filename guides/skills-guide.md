# Hermes Agent Skills: Complete Guide to Writing, Sharing, and Using Skills

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to Hermes Agent skills: what they are, how to use them, how to write your own, and how to share them with the community. Includes copy-paste templates and best practices.

---

## Table of Contents

- [What Are Hermes Agent Skills?](#what-are-hermes-agent-skills)
- [How Skills Work](#how-skills-work)
- [Finding and Installing Skills](#finding-and-installing-skills)
- [Using Skills in Your Workflow](#using-skills-in-your-workflow)
- [How to Write a Skill From Scratch](#how-to-write-a-skill-from-scratch)
- [Skill Anatomy (Template)](#skill-anatomy-template)
- [Best Practices for Skill Authoring](#best-practices-for-skill-authoring)
- [Publishing and Sharing Skills](#publishing-and-sharing-skills)
- [Skill Lifecycle Management (Curator)](#skill-lifecycle-management-curator)
- [Community Skill Directory](#community-skill-directory)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## What Are Hermes Agent Skills?

Skills are **reusable, self-contained procedure documents** that Hermes loads to gain expertise in specific domains. Think of them as:

- **A reference manual** for a specialist — Hermes consults the skill when performing related tasks
- **A saved workflow** — capture how you solved a problem once so Hermes can solve it the same way next time
- **A plugin without code** — skills are plain markdown, no programming required

When Hermes successfully completes a complex task, discovers a new workflow, or gets corrected by you, it can save that knowledge as a skill. Over time, your skills library grows, and Hermes gets better at your specific tasks, tools, and environment.

**What skills can do:**

| Use Case | Example Skills |
|----------|---------------|
| Domain expertise | `github-code-review`, `systematic-debugging`, `test-driven-development` |
| Platform integration | `himalaya` (email CLI), `obsidian` (note-taking), `huggingface-hub` |
| Workflow automation | `kanban-orchestrator`, `subagent-driven-development`, `writing-plans` |
| Tool configuration | `hermes-agent` (Hermes itself), `computer-use`, `local-model-selection` |
| Research | `agent-community-analysis`, `sports-betting-research`, `local-discovery` |

---

## How Skills Work

### The Loading Mechanism

1. A skill is installed to `~/.hermes/skills/` (or `~/.hermes/profiles/<name>/skills/` for profile-specific skills)
2. Hermes scans the skills directory on startup
3. Skill metadata (name, description, tags) is injected into the system prompt so Hermes knows what's available
4. When you ask Hermes to do something that matches a skill's domain, Hermes loads the full skill content into context
5. Hermes follows the skill's instructions, commands, and workflows to complete your task

### Explicit vs. Automatic Loading

**Explicit loading** (you tell Hermes to load a skill):

```
/skill github-code-review
```

Or when starting Hermes:

```bash
hermes --skills github-code-review,systematic-debugging
```

**Automatic loading:** Hermes detects when a skill is relevant based on your task and loads it automatically. You don't need to remember which skill covers which domain — Hermes figures it out.

### Where Skills Live

```
~/.hermes/skills/                    # Global skills (all profiles)
~/.hermes/skills/SKILL.md            # A single-file skill
~/.hermes/skills/my-skill/           # A directory skill
~/.hermes/skills/my-skill/SKILL.md   # Main skill document
~/.hermes/skills/my-skill/references/ # Supporting files
~/.hermes/skills/my-skill/scripts/    # Scripts the skill uses
~/.hermes/skills/my-skill/templates/  # Templates the skill generates
~/.hermes/skills/my-skill/assets/     # Images, configs, etc.
```

Profile-specific skills go in `~/.hermes/profiles/<name>/skills/` and are isolated from other profiles.

---

## Finding and Installing Skills

### Browse the Skills Hub

```bash
hermes skills browse
```

Opens an interactive browser showing all available skills with descriptions.

### Search for Skills

```bash
hermes skills search "code review"
hermes skills search "email"
hermes skills search "browser"
```

### Install a Skill

```bash
# From the hub by ID:
hermes skills install github-code-review

# From a GitHub repo:
hermes skills tap add https://github.com/user/hermes-skills
hermes skills install my-custom-skill

# From a direct URL:
hermes skills install https://raw.githubusercontent.com/user/repo/main/SKILL.md
```

### Preview Before Installing

```bash
hermes skills inspect github-code-review
```

Shows the full SKILL.md content without installing it. Useful for evaluating quality before committing.

### List Installed Skills

```bash
hermes skills list
```

### Update Skills

```bash
hermes skills check     # Check for updates
hermes skills update    # Update all outdated skills
```

### Uninstall

```bash
hermes skills uninstall github-code-review
```

---

## Using Skills in Your Workflow

### Pattern 1: Load a Skill and Ask a Question

Inside an active Hermes session:

```
Load the github-code-review skill, then review the PR at https://github.com/nousresearch/hermes-agent/pull/1234
```

Hermes loads the skill, follows its workflow, fetches the PR diff, applies the review criteria from the skill, and produces a code review.

### Pattern 2: Start Hermes With Skills Pre-loaded

```bash
hermes --skills systematic-debugging,test-driven-development
```

Now every interaction in this session benefits from both skills' expertise.

### Pattern 3: Use Skills in Cron Jobs

```bash
hermes cron create "0 9 * * *" --prompt "Review all open PRs in the nousresearch/hermes-agent repo" --skills "github-code-review"
```

The cron job loads the skill each time it runs, applying its domain knowledge to the scheduled task.

### Pattern 4: Chain Skills Together

Some skills are designed to work together:

```
/skill writing-plans
/skill subagent-driven-development

Create an implementation plan for adding OAuth support to my FastAPI app, then execute it with subagents
```

The `writing-plans` skill provides the planning methodology, and `subagent-driven-development` handles the execution phase.

### Pattern 5: Profile-Specific Skills

Assign skills to specific profiles so they only load in the right context:

```bash
# Work profile gets dev skills:
hermes --profile work
/skill github-code-review
/skill test-driven-development

# Personal profile gets different skills:
hermes --profile personal
/skill himalaya
/skill obsidian
```

---

## How to Write a Skill From Scratch

### Step 1: Identify the Domain

A good skill covers one clear domain. Ask yourself:

- What does the user need to know to do this task well?
- What commands, APIs, or tools are involved?
- What are the common pitfalls?
- What are the step-by-step workflows?

### Step 2: Create the Skill File

```bash
mkdir -p ~/.hermes/skills/my-skill
```

Create `~/.hermes/skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: "Short description of what this skill does."
version: 1.0.0
author: Your Name
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [tag1, tag2]
---

# My Skill Title

Brief overview of what this skill covers.

## When to Use This Skill

Specific triggers and scenarios.

## Prerequisites

What needs to be installed or configured.

## Workflow

### Step 1: Do This

```bash
command here
```

Explanation.

### Step 2: Do That

```bash
another command
```

## Pitfalls

- Common mistake 1 and how to avoid it
- Common mistake 2

## Verification

How to confirm the task was done correctly.

## Reference

Links to external docs, related skills, etc.
```

### Step 3: Add Supporting Files (Optional)

```bash
mkdir -p ~/.hermes/skills/my-skill/references
mkdir -p ~/.hermes/skills/my-skill/scripts
mkdir -p ~/.hermes/skills/my-skill/templates
```

- `references/` — markdown files with API docs, configuration references, cheat sheets
- `scripts/` — Python or shell scripts the skill needs
- `templates/` — file templates the skill generates (configs, boilerplate code)
- `assets/` — images, icons, sample files

### Step 4: Test the Skill

```bash
hermes --skills my-skill
```

Then ask Hermes to do something in the skill's domain. Verify that Hermes:

1. Loads the skill correctly
2. Follows the documented workflow
3. Handles edge cases mentioned in pitfalls
4. Completes the verification steps

### Step 5: Iterate

If Hermes misses a step, add it. If a pitfall wasn't covered, document it. Skills improve with use — update them whenever you discover a better approach.

---

## Skill Anatomy (Template)

Here's a complete, annotated skill template you can copy:

```markdown
---
name: my-automation-skill
description: "Automate recurring task X with proven workflows and error handling."
version: 1.0.0
author: YourName
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [automation, productivity]
    homepage: https://github.com/you/repo
    related_skills: [related-skill-1]
---

# My Automation Skill

One-paragraph overview. Explain what problem this skill solves
and why someone would use it.

## When to Use This Skill

- When the user asks to do task X
- When the user mentions keywords Y or Z
- When the user is working with tool W

## Prerequisites

- Python 3.11+ installed
- API key for service X (set `SERVICE_X_API_KEY` in `.env`)
- `jq` installed for JSON processing

## Quick Start

```bash
# One command to verify everything is set up
hermes --skills my-automation-skill -q "Run the setup check"
```

## Workflow

### Step 1: Prepare the Environment

```bash
# Create working directory if it doesn't exist
mkdir -p ~/automation-output
```

### Step 2: Fetch Data

Use the `web_search` tool to find relevant data, or `terminal` to query an API:

```bash
curl -s "https://api.example.com/data" | jq '.results'
```

### Step 3: Process and Save

Save results, apply transformations, generate output files.

### Step 4: Verify

```bash
# Check that output files exist with expected content
ls -la ~/automation-output/
head -20 ~/automation-output/results.md
```

## Error Handling

### If the API is down

- Retry up to 3 times with exponential backoff (5s, 10s, 20s)
- If all retries fail, save the error to ~/automation-output/errors.log
- Notify the user

### If the output directory doesn't exist

- Create it automatically
- Warn the user if disk space is below 1GB

## Pitfalls

- **Rate limiting:** Service X allows 100 requests/day. Batch requests where possible.
- **Time zones:** All timestamps should be in the user's local timezone.
- **File permissions:** Output files should be created with 0o644 permissions.

## Verification Checklist

After running the automation, verify:

- [ ] Output files exist in the expected location
- [ ] File sizes are non-zero
- [ ] No errors in ~/automation-output/errors.log
- [ ] Timestamps are current

## Reference

- [Service X API Docs](https://docs.example.com)
- [Related Skill](wiki/skills-guide)
- [Community Discussion](https://reddit.com/r/hermesagent)
```

---

## Best Practices for Skill Authoring

### 1. One Skill, One Domain

A skill should cover one clear area of expertise. Don't create a mega-skill that covers everything — it'll be too large for context and hard to maintain. Instead, create multiple focused skills that can be loaded independently or chained together.

**Good:** `github-code-review` (just code review workflows)
**Bad:** `github-everything` (PRs, issues, actions, pages, wikis, all in one file)

### 2. Write Triggers Clearly

In the "When to Use This Skill" section, list specific keywords and scenarios. Hermes uses these to decide when to auto-load the skill.

### 3. Include Copy-Paste Commands

Every workflow step should include the exact command the user (or Hermes) should run. Don't describe what to do — show the command.

### 4. Document Pitfalls Aggressively

The most valuable part of a skill is the section on what goes wrong. Every time you hit an error, add it to the pitfalls. This is the knowledge that would otherwise be lost between sessions.

### 5. Keep Skills Up to Date

APIs change, tools get updated, workflows improve. When you use a skill and find it's stale, update it immediately:

```bash
# Edit a skill directly:
hermes config edit  # Then navigate to ~/.hermes/skills/<name>/SKILL.md

# Or ask Hermes to update it:
/skill my-skill
"Update this skill — the API endpoint changed from /v1 to /v2"
```

### 6. Use Version Numbers

Increment the version in the frontmatter when you make changes. This helps you track which version of a skill produced which results.

### 7. Test on All Target Platforms

If your skill claims `platforms: [macos, linux, windows]`, test it on all three. Platform-specific quirks (file paths, shell syntax, package managers) are the most common source of skill failures.

### 8. Leverage Supporting Files

Put large reference material (API docs, full schemas, long configuration examples) in `references/` files, not in the main SKILL.md. Hermes can load these on demand, keeping the main skill lean.

---

## Publishing and Sharing Skills

### Publish to the Skills Hub

```bash
hermes skills publish ~/.hermes/skills/my-skill
```

This submits your skill to the community registry. After review, it becomes available to everyone via `hermes skills browse`.

### Share via GitHub

The simplest way to share a skill: put it in a GitHub repo.

```bash
# Create a repo for your skills
git init my-hermes-skills
cp -r ~/.hermes/skills/my-skill my-hermes-skills/
cd my-hermes-skills
git add .
git commit -m "Add my-automation skill"
git push origin main
```

Others can install from your repo:

```bash
hermes skills tap add https://github.com/yourname/my-hermes-skills
hermes skills install my-automation-skill
```

### Share on r/hermesagent

Post your skill to the subreddit with the "Skill" flair. Include:

- What the skill does
- Prerequisites
- A link to the SKILL.md (GitHub raw URL or the skill hub link)
- A screenshot or example of it in action

---

## Skill Lifecycle Management (Curator)

Hermes includes a Curator system that tracks skill usage and manages their lifecycle automatically.

### How Curator Works

1. **Tracks usage** — records how often each skill is loaded and used
2. **Marks stale** — skills unused for a configurable period get flagged
3. **Archives** — long-stale skills get moved to an archive (never deleted)
4. **Backs up** — pre-archive snapshots so nothing is lost

### Curator Commands

```bash
hermes curator status     # See skill usage stats and states
hermes curator run        # Run a maintenance cycle manually
hermes curator pin NAME   # Protect a skill from auto-archiving
hermes curator unpin NAME # Allow auto-management again
hermes curator archive NAME # Manually archive a stale skill
hermes curator restore NAME  # Restore an archived skill
```

### In-Session

```
/curator status
/curator pin my-skill
```

**Important:** Curator only manages skills with `created_by: "agent"` provenance. Bundled and hub-installed skills are never automatically touched.

---

## Community Skill Directory

Here are some of the most popular community skills. All are installable via `hermes skills install <name>`.

### Development

| Skill | What It Does |
|-------|-------------|
| `github-code-review` | Reviews PRs with diffs, inline comments via `gh` or REST API |
| `systematic-debugging` | 4-phase root cause debugging methodology |
| `test-driven-development` | Enforces RED-GREEN-REFACTOR: tests before code |
| `subagent-driven-development` | Executes implementation plans via delegate_task subagents |
| `writing-plans` | Creates bite-sized implementation plans with paths and code |
| `typescript-testing-patterns` | TypeScript/vitest TDD patterns for add-in projects |
| `application-security-review` | Concrete security review for application repos |
| `integration-review` | Spec-compliance and code-quality integration review |

### DevOps & Infrastructure

| Skill | What It Does |
|-------|-------------|
| `cross-machine-connectivity` | Remote machine access and troubleshooting |
| `dashboard-backend` | Dashboard backend project notes and API contract |
| `kanban-orchestrator` | Multi-agent work queue decomposition and orchestration |

### Productivity

| Skill | What It Does |
|-------|-------------|
| `himalaya` | Terminal email via Himalaya CLI (IMAP/SMTP) |
| `obsidian` | Read, search, create, and edit Obsidian vault notes |
| `computer-use` | Desktop automation: clicking, typing, screenshots |
| `browser-automation` | Browser navigation and interaction |

### AI/ML

| Skill | What It Does |
|-------|-------------|
| `hermes-agent` | Configure, extend, and contribute to Hermes Agent itself |
| `llama-cpp` | Local GGUF inference + Hugging Face model discovery |
| `huggingface-hub` | Search, download, upload models and datasets |
| `local-model-selection` | Choose and recommend local LLM models |

### Research

| Skill | What It Does |
|-------|-------------|
| `agent-community-analysis` | Review external AI agent communities and forums |
| `site-mapping` | Map out a website's full structure |
| `local-discovery` | Find local events, venues, and activities |

---

## FAQ

### What's the difference between a skill and a plugin?

Skills are markdown documents — no code required. They provide instructions, workflows, and reference material. Plugins are Python packages that add new functionality (new tools, new slash commands, new platform adapters). Skills are easier to create; plugins are more powerful.

### Can I use a skill without installing it?

Yes. Load any SKILL.md directly with:

```bash
hermes --skills /path/to/local/SKILL.md
```

This is great for testing before publishing.

### How do skills interact with memory?

Skills and memory serve different purposes. Skills are procedural knowledge (how to do things). Memory stores facts about you and your environment (who you are, your preferences, past decisions). They complement each other: a skill might say "use the user's preferred package manager," while memory stores that the user prefers `brew` over `pip`.

### Do skills work with cron jobs?

Yes. Pass skills to cron jobs with `--skills`:

```bash
hermes cron create "0 9 * * *" --prompt "Review open PRs" --skills "github-code-review"
```

The cron job loads the skill on each run.

### Can skills call other skills?

Yes. List related skills in the `metadata.hermes.related_skills` field. Hermes will load related skills when they're relevant to the current task. A skill can also instruct Hermes to explicitly load another skill as part of its workflow.

### How do I update a skill I installed from the hub?

```bash
hermes skills check    # See which skills have updates
hermes skills update   # Update all outdated skills
```

### Can I have profile-specific skills?

Yes. Install skills while a profile is active, or copy them to `~/.hermes/profiles/<name>/skills/`. Profile-specific skills are isolated — the "work" profile won't see skills installed in the "personal" profile.

### What happens if a skill is out of date?

Hermes will still load and use it, but the instructions may be stale. If you notice a skill is outdated, update it (edit the SKILL.md directly or ask Hermes to fix it) and increment the version. Consider submitting an update to the hub if it's a community skill.

### Are skills version-controlled?

Hub-installed skills track versions automatically (`hermes skills check` detects updates). For your own skills, version numbers in the frontmatter are manual — increment them when you make changes. There's no built-in git integration for skills, but you can keep them in a git repo manually.

### How do I delete a skill I no longer need?

```bash
hermes skills uninstall skill-name
```

For manually created skills, delete the directory from `~/.hermes/skills/`. Curator can also archive unused skills automatically (never deletes — always recoverable).

---

## Next Steps

**Skills become truly powerful when scheduled:**

1. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule skills to run automatically on a timer
2. **[Telegram Gateway Setup →](wiki/telegram-gateway-setup)** Get skill results delivered to your phone
3. **[Profiles Guide →](wiki/profiles-guide)** Organize skills by profile (work, personal, dev)

**Also see:** [Start Here](wiki/start-here) · [Model Guide](wiki/model-guide) · [50 Use Cases](wiki/use-cases) · [Official Skills Docs](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
