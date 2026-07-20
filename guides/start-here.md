# Start Here: Hermes Agent by Nous Research — Complete Beginner's Guide

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Everything you need to get started with Hermes Agent by Nous Research: installation, first setup, configuration, models, skills, and real automation examples. Beginner-friendly guide updated for 2026.

---

## Table of Contents

- [What Is Hermes Agent?](#what-is-hermes-agent)
- [Quick Installation (3 Steps)](#quick-installation-3-steps)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Linux](#linux)
- [Your First 10 Minutes With Hermes](#your-first-10-minutes-with-hermes)
- [Choosing a Model (Important!)](#choosing-a-model-important)
- [Essential Configuration](#essential-configuration)
- [Real Automations You Can Set Up Today](#real-automations-you-can-set-up-today)
- [Community Resources](#community-resources)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## What Is Hermes Agent?

Hermes Agent is an **open-source, local-first AI agent framework** developed by [Nous Research](https://nousresearch.com). It gives AI models full access to your terminal, browser, file system, and messaging platforms — turning an LLM from a chatbot into a persistent, tool-using agent that can do real work on your computer.

**Who makes it:** Nous Research, the team behind the Hermes model series and one of the most active open-source AI research groups.

**What it does:**

- **Runs in your terminal** — full shell access with command execution, process management, and file operations
- **Controls your browser** — navigate websites, click buttons, fill forms, extract content
- **Schedules recurring tasks** — cron jobs that run 24/7, even when you're not at your computer
- **Connects to messaging platforms** — Telegram, Discord, Slack, and 10+ other platforms (control Hermes from your phone)
- **Learns from experience** — saves reusable procedures as skills that improve over time
- **Remembers across sessions** — persistent memory of your preferences, environment, and past work

**Key capabilities at a glance:**

| Feature | What It Does |
|----------|--------------|
| Terminal | Run shell commands, install packages, manage processes |
| File System | Read, write, search, and patch files |
| Browser | Navigate websites, click elements, extract content |
| Cron Jobs | Schedule automations that run on a timer |
| Skills | Reusable, self-contained procedure documents |
| Memory | Persistent cross-session context and preferences |
| Gateway | Control Hermes from Telegram, Discord, Slack, and more |
| Profiles | Run multiple independent Hermes instances |

**What makes Hermes different from ChatGPT or Claude?**

ChatGPT and Claude are chatbots — you send a message, they reply. Hermes is an **agent**. When you give it a task, it uses tools (terminal, browser, file system) to complete that task autonomously. It doesn't just tell you what to do — it does it.

For a deeper comparison, see the [Hermes Agent vs Alternatives](wiki/comparison-hermes-vs-alternatives) guide.

---

## Quick Installation (3 Steps)

Hermes installs via a single command on all platforms. Minimum requirements: Python 3.11+, 4GB RAM, 1GB disk space (plus model storage if running local LLMs).

### macOS

Open Terminal and run:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

After installation, run the setup wizard:

```bash
hermes setup
```

The wizard walks you through model selection, API key configuration, and tool setup. You'll be chatting with Hermes in under 5 minutes.

**Homebrew alternative:**

```bash
brew install nousresearch/hermes-agent/hermes
```

### Windows

Open PowerShell as Administrator and run:

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

Or use the Windows installer from the [releases page](https://github.com/NousResearch/hermes-agent/releases).

After installation:

```powershell
hermes setup
```

For detailed Windows-specific configuration (WSL, native vs. WSL tradeoffs, GPU passthrough, Windows Service setup), see the [Windows Installation Guide](wiki/windows-install).

### Linux

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Then:

```bash
hermes setup
```

Hermes works on any modern Linux distribution (Ubuntu 20.04+, Debian 11+, Fedora 38+, Arch). For headless server setups, see the [Multi-Machine Setup Guide](wiki/multi-machine-setup).

**Verify your installation:**

```bash
hermes --version
hermes doctor
```

`hermes doctor` checks your config, dependencies, and environment — it'll tell you if anything's missing.

---

## Your First 10 Minutes With Hermes

After `hermes setup` completes, you're ready to run your first commands. These copy-paste prompts will get you productive immediately.

### 1. Start an interactive session

```bash
hermes
```

This opens the interactive CLI. You'll see a prompt where you can type naturally.

### 2. Create a file

Inside the Hermes session, try:

```
Create a file called hello.txt in my home directory with the text "Hello from Hermes Agent!"
```

Hermes will use its file system tools to create the file, then confirm it's done.

### 3. Search the web

```
Search the web for the latest Nous Research announcements and summarize them
```

Hermes uses its web search tool to find current information and presents a summary.

### 4. Run a cron job

```
Create a cron job that checks the weather in New York every morning at 8 AM and saves it to a file
```

Hermes schedules the job using its cron system. You can view all scheduled jobs with `hermes cron list`.

### 5. Load a skill

```
Load the hermes-agent skill and explain what it contains
```

Skills are reusable procedure documents. The `hermes-agent` skill is included by default and contains detailed reference information about Hermes itself.

### 6. Use a slash command

Type `/help` inside your Hermes session to see all available commands. Try:

- `/model` — change your model/provider
- `/config` — view current configuration
- `/skills` — browse and install skills
- `/cron` — manage scheduled jobs

### Going Further

For a deeper walkthrough of your first session, including file editing, git integration, and multi-step workflows, check the [Skills Guide](wiki/skills-guide) and the [50 Use Cases](wiki/use-cases) page.

---

## Choosing a Model (Important!)

Hermes is model-agnostic — it works with local models running on your hardware and cloud models via API. Your choice depends on your hardware, privacy needs, and task complexity.

### Local vs Cloud: Quick Comparison

| Factor | Local Models | Cloud Models |
|--------|-------------|--------------|
| Privacy | Complete — data never leaves your machine | Data sent to API provider |
| Cost | Free (hardware cost only) | Pay-per-token or subscription |
| Speed | Depends on GPU/CPU | Fast, consistent |
| Offline | Works without internet | Requires internet |
| Quality | Very good at 24B+ parameters | State-of-the-art |
| Setup | Requires downloading and loading models | API key only |

### Recommended Models by Hardware Tier

**8GB VRAM or Less (entry-level GPU / Apple Silicon base):**

- **Qwen2.5-Coder-7B-Instruct** (GGUF, Q4_K_M) — excellent coding capability, fits in 6GB
- **Llama-3.2-3B-Instruct** — fast, capable for simple tasks
- **Hermes-3-Llama-3.2-3B** — Nous Research's own model tuned for agent use

**16GB VRAM (RTX 4060 Ti, RTX 4070, M1/M2 Pro):**

- **Qwen2.5-Coder-14B-Instruct** (GGUF, Q4_K_M) — strong all-around coding agent
- **Mistral-Nemo-12B-Instruct** — fast, good reasoning
- **Hermes-3-Llama-3.1-8B** — Nous-tuned for tool use

**24GB+ VRAM (RTX 3090, RTX 4090, M2/M3 Max, M3 Ultra):**

- **Qwen3.6-27B** (GGUF, Q4_K_M) — excellent coding, reasoning, and instruction following
- **Command-R-Plus** — strong for complex multi-step tasks
- **Llama-3.1-Nemotron-51B** (with quantization) — near-frontier performance

**48GB+ / Multi-GPU (RTX 5090 32GB, dual 3090s, Mac Studio Ultra):**

- **Qwen3.6-27B** at Q6_K or Q8_0 — higher quality quantization
- **Llama-3.3-70B-Instruct** (Q4_K_M) — frontier-level reasoning
- **Mixtral-8x22B** — strong for parallel tool use

### Cloud Model Options

| Provider | Best Model for Hermes | Setup |
|----------|----------------------|-------|
| DeepSeek | deepseek-v4-pro | `DEEPSEEK_API_KEY` |
| Anthropic | Claude Sonnet 4 | `ANTHROPIC_API_KEY` |
| OpenAI | GPT-4o | `OPENAI_API_KEY` |
| OpenRouter | Any model, one API | `OPENROUTER_API_KEY` |
| Nous Portal | Hermes-3-405B (free tier) | `hermes auth add nous` |

To switch models, run:

```bash
hermes model
```

This opens an interactive picker. You can also specify a model directly:

```bash
hermes chat --model "anthropic/claude-sonnet-4" --provider anthropic
```

For a complete breakdown of models, benchmarks, and provider setup, see the [Model Guide](wiki/model-guide).

---

## Essential Configuration

Hermes stores configuration in two files:

- `~/.hermes/config.yaml` — settings (models, tools, compression, gateway)
- `~/.hermes/.env` — secrets (API keys, tokens)

### The Must-Change Settings

Edit your config with:

```bash
hermes config edit
```

**1. Set your default model:**

```yaml
model:
  default: "qwen2.5-coder-14b-instruct"
  provider: "lmstudio"  # or openrouter, anthropic, openai, deepseek
  context_length: 32768
```

**2. Configure terminal backend:**

```yaml
terminal:
  backend: "local"  # local, docker, ssh, modal
  timeout: 300
```

**3. Enable memory:**

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
```

**4. Set up compression (for long sessions):**

```yaml
compression:
  enabled: true
  threshold: 0.85
  target_ratio: 0.70
```

### Profiles Explained

Profiles let you run multiple independent Hermes instances — each with its own config, skills, memory, and sessions. Think of them as separate "personas" for different contexts.

```bash
hermes profile create work       # Work profile with work-related skills
hermes profile create personal   # Personal profile, isolated memory
hermes profile use work          # Switch to work profile
```

Each profile lives in `~/.hermes/profiles/<name>/` with its own complete configuration.

For a deep dive into profiles — including domain-specific profiles, memory isolation, and multi-profile workflows — see the [Profiles Guide](wiki/profiles-guide).

### Skills: What They Are

Skills are reusable, self-contained procedure documents that Hermes loads to gain expertise in specific domains. When you install a skill, Hermes references it when performing related tasks — like giving a specialist a reference manual.

```bash
hermes skills browse          # Browse available skills
hermes skills install NAME    # Install a skill
hermes skills list            # Show installed skills
```

In-session, load a skill with:

```
/skill hermes-agent
```

Skills are the core extensibility mechanism in Hermes. Community members have published skills for everything from GitHub PR review to sports betting research. Learn to write your own in the [Skills Guide](wiki/skills-guide).

### Gateway Setup (Optional)

The gateway connects Hermes to messaging platforms like Telegram, Discord, and Slack. This lets you control Hermes from your phone.

```bash
hermes gateway setup     # Interactive configuration
hermes gateway run       # Start the gateway
```

Each platform has its own setup requirements. For a complete walkthrough, see the [Telegram Gateway Setup Guide](wiki/telegram-gateway-setup).

---

## Real Automations You Can Set Up Today

Here are five complete automations you can deploy right now. Each links to a dedicated guide with full instructions.

### 1. Daily News Briefing (Cron Job)

A cron job that runs every morning, searches for top headlines in your chosen topics, and saves a formatted summary.

```bash
hermes cron create "0 8 * * *" --prompt "Search the web for today's top AI and technology news. Summarize the 5 most important stories and save to ~/briefings/$(date +%Y-%m-%d)-news.md"
```

For more cron job recipes, see the [Cron Jobs & Automation Guide](wiki/cron-jobs-automation).

### 2. GitHub PR Reviewer (Skill)

Load the `github-code-review` skill and point Hermes at an open PR:

```
Load the github-code-review skill, then review the PR at https://github.com/user/repo/pull/42
```

Hermes fetches the diff, analyzes the changes, and provides inline comments via the GitHub API. See the [Skills Guide](wiki/skills-guide) for the full workflow.

### 3. Telegram Bot That Responds to Messages (Gateway)

Connect Hermes to Telegram, then it can respond to your DMs, participate in group chats, and deliver cron job results to your phone.

After gateway setup (see the [Telegram Setup Guide](wiki/telegram-gateway-setup)), simply send a message to your bot — Hermes processes it with full tool access.

### 4. File Organizer (Terminal)

Point Hermes at a messy directory and let it organize:

```
Organize ~/Downloads by file type. Move images to an Images folder, documents to Documents, archives to Archives, and everything else into Misc. Create subfolders by year for files with dates in their names.
```

Hermes uses its terminal and file system tools to analyze and reorganize your files. It'll show you what it plans to do and ask for confirmation before moving anything.

### 5. Web Monitor (Browser + Cron)

A cron job that monitors a website for changes and alerts you:

```
Create a cron job that runs every 4 hours, navigates to https://nousresearch.com, extracts any new blog posts or announcements since the last check, and saves them to ~/monitors/nous-updates.md. If there's new content, send me a notification.
```

For more browser automation patterns, see the [Browser Automation Guide](wiki/browser-automation).

---

## Community Resources

- **[r/hermesagent](https://reddit.com/r/hermesagent)** — 75,000+ members. Daily discussions, setup help, automation showcases
- **[Official Documentation](https://hermes-agent.nousresearch.com/docs)** — Complete reference for every feature
- **[GitHub (Nous Research)](https://github.com/NousResearch/hermes-agent)** — Source code, issues, contributions
- **[Discord](https://discord.gg/nousresearch)** — Real-time chat with the dev team and community
- **[Skills Hub](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)** — Browse community skills
- **[Community Showcase](wiki/use-cases)** — 50 real automation ideas from the community

---

## FAQ

### Does Hermes Agent work offline?

Yes. When running with a local model (llama.cpp, Ollama, LM Studio), Hermes works completely offline — no internet connection needed. Web search and browser tools require internet, but the core agent loop, terminal, file operations, and cron jobs all function offline.

### Is Hermes Agent free?

Yes. Hermes Agent is open-source (MIT license) and free to use. You only pay for cloud model API usage (DeepSeek, Anthropic, OpenAI) if you choose to use cloud providers. Running with a local model costs nothing beyond your electricity.

### What's the difference between Hermes Agent and Claude Code?

Claude Code is Anthropic's cloud-only coding agent, locked to Claude models. Hermes Agent is open-source, model-agnostic, runs locally, supports messaging platforms, has cron scheduling, and is extensible via skills and plugins. For a detailed comparison, see [Hermes Agent vs Alternatives](wiki/comparison-hermes-vs-alternatives).

### Can Hermes Agent control my browser?

Yes. Hermes has a full browser automation toolset (navigate, click, type, scroll, extract content) and `computer_use` for desktop automation. See the [Browser Automation Guide](wiki/browser-automation) for setup and use cases.

### What models work best with Hermes Agent?

For local use: Qwen2.5-Coder (7B-32B), Llama 3.1/3.3 (8B-70B), and Command-R-Plus. For cloud: Claude Sonnet 4, DeepSeek V4, GPT-4o. The [Model Guide](wiki/model-guide) has detailed tiered recommendations.

### How do I connect Hermes Agent to Telegram?

Create a Telegram bot via @BotFather, add the token to your `~/.hermes/.env` file, then run `hermes gateway setup` and select Telegram. Full step-by-step in the [Telegram Gateway Setup Guide](wiki/telegram-gateway-setup).

### Does Hermes Agent work on Windows/Mac/Linux?

Yes — all three platforms are fully supported. macOS and Linux via bash script, Windows via PowerShell script or installer. Platform-specific guides: [Windows Installation](wiki/windows-install), [Multi-Machine Setup](wiki/multi-machine-setup).

### How much does it cost to run Hermes Agent?

The software is free. Running a local model costs electricity only ($0.10-0.50/day for a desktop GPU). Cloud models cost $0.50-5.00/day for typical usage depending on the provider and model. Many users run a mix: local for routine tasks, cloud for complex work.

### Can Hermes Agent write and execute code?

Yes. Hermes can write code (using its file tools), execute it (using its terminal), run tests, debug errors, and iterate. It supports Python, JavaScript, TypeScript, Rust, Go, and any language with a command-line toolchain. It can also create and manage git repositories, push to GitHub, and review pull requests.

### How is Hermes different from a regular AI chatbot?

A chatbot only reads and generates text. Hermes has tools — it can run shell commands, search the web, read and write files, control a browser, schedule recurring tasks, and communicate through messaging platforms. It takes action, not just gives advice.

### Is my data safe with Hermes Agent?

When running local models, your data never leaves your machine. When using cloud providers, data is sent to the provider's API following their privacy policies. Hermes includes security features like secret redaction (API keys in tool output are auto-masked), command approval prompts for dangerous operations, and PII redaction in gateway messages.

---

## Next Steps

**Now that you're set up, here's your learning path:**

1. **[Model Guide →](wiki/model-guide)** Pick the right model for your hardware and use case
2. **[Skills Guide →](wiki/skills-guide)** Learn to use and write skills — the core extensibility system
3. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule automations that run 24/7
4. **[50 Use Cases →](wiki/use-cases)** See what the community is building

**Also see:** [Telegram Setup](wiki/telegram-gateway-setup) · [Profiles Guide](wiki/profiles-guide) · [Browser Automation](wiki/browser-automation) · [Official Docs](https://hermes-agent.nousresearch.com/docs)
