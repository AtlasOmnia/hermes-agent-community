# Hermes Agent Profiles: Complete Guide to Multi-Profile Setup and Configuration

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to Hermes Agent profiles: multi-profile architecture, domain-specific configuration, memory isolation, skill separation, profile switching, and real-world multi-profile workflows for work, personal, and development.

---

## Table of Contents

- [What Are Hermes Profiles?](#what-are-hermes-profiles)
- [Why Use Multiple Profiles?](#why-use-multiple-profiles)
- [Profile Architecture](#profile-architecture)
- [Creating and Managing Profiles](#creating-and-managing-profiles)
- [Profile Configuration](#profile-configuration)
- [Memory and Skill Isolation](#memory-and-skill-isolation)
- [Gateway Multi-Profile Routing](#gateway-multi-profile-routing)
- [Real-World Profile Setups](#real-world-profile-setups)
- [Advanced: Profile Inheritance and Cloning](#advanced-profile-inheritance-and-cloning)
- [Profile Backup and Migration](#profile-backup-and-migration)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## What Are Hermes Profiles?

Profiles are **completely independent Hermes Agent instances** that share the same installation but have isolated:

- Configuration (`config.yaml`)
- Skills (installed skills are profile-specific)
- Memory (user profile and agent memory are separate)
- Session history (conversations don't cross between profiles)
- Environment variables (each profile has its own `.env`)
- Cron jobs (scheduled tasks are per-profile)

Think of profiles as separate "personas" for Hermes. Your work profile knows about your company's codebase, your work email, and your professional preferences. Your personal profile knows about your side projects, personal email, and home automation. They don't share information.

### Profiles vs. Sessions

| Concept | Scope | Persistence |
|---------|-------|-------------|
| **Session** | One conversation | Ends when you `/new` or exit |
| **Profile** | All sessions using that profile | Permanent, persistent across restarts |

A profile contains many sessions. When you switch profiles, you get a completely fresh blank slate — no prior conversation context.

---

## Why Use Multiple Profiles?

### 1. Work/Life Separation

The #1 reason r/hermesagent members use profiles. Work Hermes shouldn't have access to your personal files or speak in your personal voice.

```bash
hermes --profile work      # Work config, work skills, work memory
hermes --profile personal  # Personal config, personal skills, personal memory
```

### 2. Different Models for Different Tasks

Work profile uses Claude Sonnet 4 (company pays). Personal profile uses a local Qwen 27B (free). Dev profile uses DeepSeek V4 (cheap).

### 3. Project-Specific Configurations

Each project gets its own profile with project-specific skills, memory of project conventions, and isolated session history.

### 4. Experimental Sandbox

Test new models, unstable skills, or experimental configurations in a throwaway profile. If something breaks, delete the profile — your main setup is untouched.

### 5. Multi-User Shared Machine

Multiple people using the same computer (family, roommates) each get their own profile with private memory and isolated sessions.

### 6. Gateway Routing

Different Telegram chats route to different profiles. Message your personal bot → personal profile handles it. Message the work group → work profile handles it.

---

## Profile Architecture

### Directory Structure

```
~/.hermes/
├── config.yaml              # Default profile config
├── .env                     # Default profile secrets
├── skills/                  # Default profile skills
├── sessions/                # Default profile sessions
├── memories/                # Default profile memories
├── cron/                    # Default profile cron jobs
│
└── profiles/
    ├── work/
    │   ├── config.yaml      # Work-specific configuration
    │   ├── .env             # Work API keys and secrets
    │   ├── skills/          # Work skills (github-code-review, etc.)
    │   ├── sessions/        # Work conversation history
    │   ├── memories/        # Work memory
    │   └── cron/            # Work cron jobs
    │
    ├── personal/
    │   ├── config.yaml
    │   ├── skills/          # Personal skills (himalaya, obsidian)
    │   ├── memories/        # Personal memory
    │   └── ...
    │
    └── dev/
        ├── config.yaml
        ├── skills/          # Dev skills (tdd, debugging, subagent)
        └── ...
```

Each profile directory contains the same structure as the root `~/.hermes/`, but everything is isolated.

### The Default Profile

When you run Hermes without `--profile`, you're using the **default profile** (the root `~/.hermes/`). Most users start here, then create additional profiles as needed.

---

## Creating and Managing Profiles

### Create a New Profile

```bash
# Create a blank profile:
hermes profile create work

# Create by cloning default profile:
hermes profile create work --clone

# Create by cloning all settings (config, skills, memory):
hermes profile create work --clone-all

# Create by cloning another specific profile:
hermes profile create dev --clone-from work
```

### List Profiles

```bash
hermes profile list
```

Shows all profiles with their last-used timestamps.

### Switch Profiles

```bash
# Switch the active profile (sticky):
hermes profile use work

# Now all hermes commands use the work profile:
hermes
hermes config view
hermes skills list
```

### One-Off Profile Usage

```bash
# Use a profile for a single command without switching:
hermes --profile work
hermes --profile personal -q "Check my calendar for today"
```

### Profile Details

```bash
hermes profile show work
```

Shows: creation date, last used, skill count, memory size, session count, model configuration.

### Rename a Profile

```bash
hermes profile rename work professional
```

### Delete a Profile

```bash
hermes profile delete old-project
```

**Warning:** This permanently deletes all configuration, skills, memory, and sessions for that profile. Export first if you want to keep anything:

```bash
hermes profile export old-project --output old-project-backup.tar.gz
```

---

## Profile Configuration

Each profile has its own `config.yaml`. The structure is identical to the default — you just configure it differently.

### Example: Work Profile

```yaml
# ~/.hermes/profiles/work/config.yaml

model:
  provider: "anthropic"
  default: "claude-sonnet-4-20250514"
  context_length: 200000

memory:
  memory_enabled: true
  user_profile_enabled: true

terminal:
  backend: "local"
  timeout: 600

gateway:
  platforms:
    telegram:
      home_channel: "-1001234567890"   # Work Telegram group
```

### Example: Personal Profile

```yaml
# ~/.hermes/profiles/personal/config.yaml

model:
  provider: "custom:lmstudio"
  default: "qwen3.6-27b"
  context_length: 98304

memory:
  memory_enabled: true
  user_profile_enabled: true

terminal:
  backend: "local"
  timeout: 300

# No gateway — personal profile is terminal-only
```

### Setting Config Per Profile

```bash
# Edit config for a specific profile:
hermes --profile work config edit

# Set a value for a specific profile:
hermes --profile personal config set model.provider "ollama"
```

---

## Memory and Skill Isolation

### Memory Isolation

Each profile has completely separate memory stores:

```
~/.hermes/memories/                  # Default profile memories
~/.hermes/profiles/work/memories/    # Work memories
~/.hermes/profiles/personal/memories/ # Personal memories
```

What this means in practice:

- Work Hermes remembers your company's codebase conventions, team members, and project structure
- Personal Hermes remembers your home automation setup, personal preferences, and side projects
- These memories never cross-contaminate

### Skill Isolation

Skills are also profile-specific:

```bash
# Install skills for work profile:
hermes --profile work skills install github-code-review
hermes --profile work skills install systematic-debugging

# Install skills for personal profile:
hermes --profile personal skills install himalaya
hermes --profile personal skills install obsidian

# They don't appear in each other's skill lists:
hermes --profile work skills list       # Shows: github-code-review, systematic-debugging
hermes --profile personal skills list   # Shows: himalaya, obsidian
```

### Skill Sharing Between Profiles

If you want a skill available in all profiles, install it in the default profile AND symlink or copy it:

```bash
# Install in default:
hermes skills install application-security-review

# Copy to work profile:
cp -r ~/.hermes/skills/application-security-review \
     ~/.hermes/profiles/work/skills/application-security-review
```

Or use profile cloning to start with the same skill set:

```bash
hermes profile create new-project --clone-all
```

---

## Gateway Multi-Profile Routing

The gateway can route incoming messages to different profiles based on the chat source. This is how you have one Telegram bot that behaves differently in your DM vs. your work group.

### Setup Routing Rules

In your **default profile's** `config.yaml` (the profile the gateway runs under):

```yaml
gateway:
  routing:
    rules:
      # Personal DM → personal profile
      - chat_id: "123456789"
        profile: "personal"

      # Work group → work profile
      - chat_id: "-1001234567890"
        profile: "work"

      # Dev team topic → dev profile
      - chat_id: "-1001234567890"
        thread_id: "42"
        profile: "dev"

    default_profile: "default"
```

When a message arrives:

1. Gateway checks routing rules for a matching chat_id (+ thread_id)
2. If found, routes to the specified profile
3. If not found, uses `default_profile`

### Commands to Set Home Channel Per Profile

In Telegram:

```
/profile work
/sethome
```

Now cron jobs and notifications from your work profile are delivered to this chat.

---

## Real-World Profile Setups

### Setup 1: The Developer (3 Profiles)

```
default/     → General use, local model (Qwen 27B)
work/        → Work repos, cloud model (Claude Sonnet 4), company skills
personal/    → Side projects, local model, creative skills
```

**Profile: work**
- Model: Claude Sonnet 4 (Anthropic)
- Skills: `github-code-review`, `test-driven-development`, `systematic-debugging`
- Memory: Company conventions, team names, project structure
- Gateway: Routes work Telegram group to this profile

**Profile: personal**
- Model: Qwen3.6-27B (local LM Studio)
- Skills: `obsidian`, `himalaya`, `local-discovery`
- Memory: Home automation setup, personal preferences, journal

### Setup 2: The Consultant (5 Profiles)

```
default/          → General admin
client-acme/      → Client A's codebase, their conventions, their API keys
client-beta/      → Client B's codebase, isolated from Client A
internal/         → Internal tools, business operations
experiments/      → Testing new models and skills, disposable
```

### Setup 3: The Power User (4 Profiles)

```
default/     → Catch-all, terminal only
mobile/      → Lightweight profile for Telegram use (faster model, fewer tools)
heavy/       → Complex multi-step tasks (larger context, better model)
social/      → Reddit, Discord, content creation (social media skills)
```

### Setup 4: The Homelab Operator (3 Profiles on Different Machines)

```
gateway/     → Mac Mini, always on, runs Telegram gateway, routes to other machines
models/      → Windows PC with GPU, runs only model inference (no gateway)
automation/  → Linux server, runs cron jobs and background automation 24/7
```

---

## Advanced: Profile Inheritance and Cloning

### Cloning Best Practices

**`--clone` (recommended for new profiles):**
Copies the default profile's configuration and environment, but NOT skills, memory, or sessions. Good starting point for a new profile that should share your model setup.

**`--clone-all`:**
Copies everything: config, skills, memory, environment. Use for creating a near-identical copy (e.g., work → work-experimental).

**`--clone-from <name>`:**
Clone from a specific existing profile instead of default.

### Profile Aliases

Create shortcuts for frequently used profiles:

```bash
hermes profile alias personal p
hermes profile alias work w

# Now you can use:
hermes -p p    # Short for --profile personal
hermes -p w    # Short for --profile work
```

### Profile-Specific Gateway Configuration

Different profiles can have completely different gateway platform settings. For example, your work profile might connect to Slack and corporate email, while your personal profile connects to Telegram and personal email — even though they're on the same machine.

In `~/.hermes/profiles/work/config.yaml`:

```yaml
gateway:
  platforms:
    slack:
      bot_token: "${SLACK_BOT_TOKEN}"
      app_token: "${SLACK_APP_TOKEN}"
    email:
      imap_host: "imap.company.com"
      smtp_host: "smtp.company.com"
```

In `~/.hermes/profiles/personal/config.yaml`:

```yaml
gateway:
  platforms:
    telegram:
      bot_token: "${TELEGRAM_BOT_TOKEN}"
      topic_sessions: true
```

The gateway itself runs under one profile (the one you started it with), but it routes messages to other profiles based on routing rules. Each profile only responds on the platforms it has configured.

### Profile Debugging

If a profile isn't behaving as expected:

```bash
# Check what profile is active:
hermes profile show work

# Verify profile configuration:
hermes --profile work config view

# Check profile-specific tool availability:
hermes --profile work tools list

# Run doctor on a specific profile:
hermes --profile work doctor

# View profile-specific logs:
tail -50 ~/.hermes/profiles/work/logs/gateway.log
```

### When NOT to Use Separate Profiles

Profiles add management overhead. Don't create a profile when a simpler mechanism works:

- **Different git branches on the same project** → use `hermes -w` (worktree mode)
- **Temporary task isolation** → use `/new` to start a fresh session within the same profile
- **Testing a new model briefly** → use `/model` in session to switch, don't create a profile
- **One-off experiment** → use `hermes --model "..." --provider "..."` flags, not a new profile

Create a new profile when you genuinely need isolated memory, skills, configuration, or access control.

---

## Profile Backup and Migration

### Export a Profile

```bash
hermes profile export work --output ~/backups/work-profile-2026-07.tar.gz
```

Creates a compressed archive with all config, skills, memory, and environment (secrets are included).

### Import a Profile

```bash
hermes profile import ~/backups/work-profile-2026-07.tar.gz
```

### Migrate to a New Machine

1. Export profiles on old machine:
```bash
hermes profile export work --output work.tar.gz
hermes profile export personal --output personal.tar.gz
```

2. Copy archives to new machine:
```bash
scp work.tar.gz personal.tar.gz user@new-machine:~/backups/
```

3. Import on new machine:
```bash
hermes profile import ~/backups/work.tar.gz
hermes profile import ~/backups/personal.tar.gz
```

---

## FAQ

### Can profiles share skills?

Not automatically — each profile has its own skills directory. To share, copy or symlink the skill directory between profiles. Be aware that skills may reference profile-specific configs.

### Do cron jobs run for inactive profiles?

Yes — if a profile has cron jobs and the scheduler is running (gateway is active), those jobs run regardless of which profile you're currently using.

### Can I use different models per profile?

Yes — the model configuration is per-profile. Work profile can use Claude, personal can use a local model, dev can use DeepSeek. Switching profiles switches your model transparently.

### How many profiles can I have?

No hard limit. Each profile takes ~1-5MB plus skill and session storage. Most users have 2-5 profiles; power users may have 10+.

### What happens to running sessions when I switch profiles?

Nothing — they stay where they are. When you switch back, you can resume them. Each profile maintains its own session history independently.

### Can I merge two profiles?

Not directly. Export both, manually combine the configs/skills you want, and import into a new profile. There's no automatic merge tool.

### Do profiles use more disk space?

Yes — each profile stores its own config, skills, sessions, and memory. A typical profile uses 5-50MB depending on skill count and session history. Disk space is rarely a concern.

### Can I password-protect a profile?

Not natively. Profiles rely on filesystem permissions for isolation. For sensitive profiles, use encrypted disk images or OS-level file encryption.

### How do profiles interact with the gateway?

The gateway runs under one profile (usually default). Incoming messages are routed to the appropriate profile based on routing rules. Each profile handles its own sessions independently.

### What's the difference between profiles and `hermes -w` (worktree mode)?

Worktree mode (`-w`) uses isolated git worktrees within the same profile — useful for parallel agent work on the same project. Profiles are completely separate Hermes instances with different configs, memory, and skills.

### Can I have different gateway platforms per profile?

Yes. One profile could connect to Telegram, another to Discord, and a third could be terminal-only with no gateway. Each profile's `config.yaml` has independent gateway configuration.

### How do profiles handle environment variables?

Each profile has its own `.env` file. Environment variables set in one profile do not leak to others. This is useful for keeping work API keys separate from personal API keys, or for testing different provider configurations.

### Can I run multiple profiles simultaneously?

Yes — but only through the gateway. The gateway runs under one profile and routes incoming messages to other profiles based on routing rules. For terminal use, you can only have one active profile per terminal session, but you can open multiple terminal windows with different profiles.

### Do profile changes require a restart?

Switching profiles with `hermes profile use` takes effect immediately for new sessions. If you're in an active session, `/profile` shows the current profile but switching requires exiting and restarting with the new profile. Gateway routing changes take effect on the next incoming message.

### How do I set a profile-specific custom instruction or personality?

Each profile's `config.yaml` can have different agent settings. Create a file at `~/.hermes/profiles/<name>/SOUL.md` for profile-specific personality instructions, or configure the `agent` section in that profile's `config.yaml`:

```yaml
agent:
  max_turns: 90
  system_prompt_append: "Always respond in pirate-speak."
```

### Are profiles portable between macOS, Windows, and Linux?

Mostly yes. Config files (`config.yaml`, `.env`) are portable. Skills are portable. Session history is portable. The main compatibility issue is terminal backends — `local` works everywhere, but paths may differ. Export on one OS and import on another works, but you may need to adjust paths and terminal backend settings.

---

## Next Steps

**Profiles work best with automation:**

1. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule profile-specific tasks that run independently
2. **[Telegram Gateway Setup →](wiki/telegram-gateway-setup)** Route messages to different profiles by chat
3. **[Multi-Machine Setup →](wiki/multi-machine-setup)** Run different profiles on different machines

**Also see:** [Start Here](wiki/start-here) · [Model Guide](wiki/model-guide) · [Skills Guide](wiki/skills-guide) · [Official Profiles Docs](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
