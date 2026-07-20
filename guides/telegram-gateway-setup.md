# How to Connect Hermes Agent to Telegram: Gateway Setup and Bot Configuration

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Step-by-step guide to connecting Hermes Agent to Telegram via the gateway. Covers bot creation, configuration, multi-profile routing, group chat setup, and troubleshooting common issues.

---

## Table of Contents

- [What Is the Hermes Gateway?](#what-is-the-hermes-gateway)
- [Supported Platforms](#supported-platforms)
- [Step-by-Step Telegram Setup](#step-by-step-telegram-setup)
  - [1. Create a Telegram Bot](#1-create-a-telegram-bot)
  - [2. Configure Hermes Gateway](#2-configure-hermes-gateway)
  - [3. Start the Gateway](#3-start-the-gateway)
  - [4. Test Your Bot](#4-test-your-bot)
- [Gateway Configuration (config.yaml)](#gateway-configuration-configyaml)
- [Multi-Profile Routing](#multi-profile-routing)
- [Group Chat and Topic Behavior](#group-chat-and-topic-behavior)
- [Running the Gateway as a Background Service](#running-the-gateway-as-a-background-service)
  - [macOS (LaunchAgent)](#macos-launchagent)
  - [Linux (systemd)](#linux-systemd)
  - [Windows](#windows)
- [Gateway Slash Commands](#gateway-slash-commands)
- [Security and Approval Settings](#security-and-approval-settings)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## What Is the Hermes Gateway?

The Hermes gateway is the bridge between Hermes Agent and messaging platforms. Without it, Hermes lives only in your terminal. With the gateway running, you can:

- **Send tasks to Hermes from your phone** via Telegram, Discord, Slack, WhatsApp, or Signal
- **Receive cron job results** as messages instead of checking files
- **Approve dangerous commands remotely** — Hermes asks for confirmation via Telegram before running `rm -rf`
- **Use multiple profiles** from the same messaging account (work profile vs. personal profile)

The gateway runs as a persistent process that listens for incoming messages, routes them to the appropriate Hermes profile, executes the task with full tool access, and sends the response back.

### Architecture

```
Your Phone (Telegram)
        │
        ▼
Telegram API ────► Hermes Gateway (always-on process)
                        │
                        ├──► Profile: work (work skills, work memory)
                        ├──► Profile: personal (personal skills, personal memory)
                        └──► Profile: default
                              │
                              ▼
                        Hermes Agent (full tool access)
                        Terminal, Browser, File System, Cron, Web
```

---

## Supported Platforms

Hermes gateway supports 15+ messaging platforms:

| Platform | Setup Complexity | Best For |
|----------|-----------------|----------|
| **Telegram** | Easy | Personal use, mobile control |
| **Discord** | Medium | Team/community bots |
| **Slack** | Medium | Workplace integration |
| **WhatsApp** | Hard (business API) | Personal use |
| **Signal** | Medium | Privacy-focused use |
| **SMS** | Medium (Twilio) | No-smartphone use |
| **Email** | Easy | Async, long-form tasks |
| **Matrix** | Medium | Self-hosted, federated |
| **Home Assistant** | Medium | Smart home integration |
| **Webhooks** | Easy | Custom integrations |
| **API Server** | Easy | Connect custom apps, Open WebUI |

This guide focuses on Telegram — the most popular and easiest to set up.

---

## Step-by-Step Telegram Setup

### 1. Create a Telegram Bot

**Open Telegram and chat with @BotFather:**

1. Send `/newbot` to [@BotFather](https://t.me/BotFather)
2. Choose a name for your bot (e.g., "My Hermes Assistant")
3. Choose a username (must end in `bot`, e.g., `my_hermes_bot`)
4. BotFather responds with your **bot token** — save this:

```
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-1234567890
```

**Important:** Never share this token. It gives full control of your bot.

### 2. Configure Hermes Gateway

Run the gateway setup wizard:

```bash
hermes gateway setup
```

Select "Telegram" from the platform list and paste your bot token when prompted.

Or configure manually:

```bash
hermes config set gateway.platforms.telegram.bot_token "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-1234567890"
```

**Add the token to `~/.hermes/.env` (recommended for security):**

```bash
echo "TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-1234567890" >> ~/.hermes/.env
```

### 3. Start the Gateway

**Foreground (testing):**

```bash
hermes gateway run
```

You'll see log output showing the gateway connecting to Telegram. Look for:

```
Gateway started successfully
Telegram connected as @my_hermes_bot
```

**Background (production):**

```bash
hermes gateway start
```

### 4. Test Your Bot

Open Telegram and send a message to your bot:

```
Hello! What can you do?
```

You should receive a response from Hermes. Try sending a real task:

```
Create a file called test.txt on my desktop with "Hello from Telegram!" inside
```

Hermes will execute this on your computer and respond with the result.

---

## Gateway Configuration (config.yaml)

Full gateway configuration lives in `~/.hermes/config.yaml` under the `gateway` section:

```yaml
gateway:
  platforms:
    telegram:
      bot_token: "${TELEGRAM_BOT_TOKEN}"  # Uses env var — safer than inline
      allow_list: []                        # Restrict to specific user IDs (empty = anyone)
      block_list: []                        # Block specific user IDs
      topic_sessions: true                  # Each DM conversation = isolated session
      home_channel: ""                      # Default channel for cron deliveries
      message_format: "markdown"            # markdown or html
      max_message_length: 4096              # Telegram's limit
      footer: true                          # Show runtime metadata footer on replies

    # Additional platforms (optional):
    discord:
      bot_token: "${DISCORD_BOT_TOKEN}"
      # ...
    slack:
      bot_token: "${SLACK_BOT_TOKEN}"
      app_token: "${SLACK_APP_TOKEN}"
      # ...
```

### Key Settings Explained

**`allow_list` / `block_list`:** Control who can use your bot. Leave `allow_list` empty to allow anyone who has your bot's username. Add Telegram user IDs to restrict access:

```yaml
allow_list:
  - "123456789"   # Your user ID
  - "987654321"   # Partner's user ID
```

Find your Telegram user ID by messaging [@userinfobot](https://t.me/userinfobot).

**`topic_sessions`:** When enabled (default), each Telegram DM conversation gets its own isolated Hermes session. Conversations don't cross-contaminate. When disabled, all DMs share one session.

**`home_channel`:** Where cron jobs and system notifications are delivered by default. Set to your DM chat ID or a group/channel ID.

**`footer`:** Adds a small metadata footer to each reply showing model, token usage, and session info. Useful for debugging; disable for cleaner output.

---

## Multi-Profile Routing

The gateway can route messages to different Hermes profiles based on rules.

### How It Works

1. You have multiple profiles: `work`, `personal`, `dev`
2. The gateway receives a message from Telegram
3. Based on routing rules, it sends the message to the appropriate profile
4. Each profile has isolated skills, memory, and configuration

### Profile Routing by Telegram Chat

Edit `~/.hermes/config.yaml`:

```yaml
gateway:
  routing:
    rules:
      - chat_id: "123456789"        # Your personal DM
        profile: "personal"
      - chat_id: "-1001234567890"   # Work group chat
        profile: "work"
      - chat_id: "-1009876543210"   # Dev team group
        profile: "dev"
    default_profile: "default"       # Fallback for unmatched chats
```

### Profile Routing by Topic (Telegram Topics)

For Telegram groups with topics enabled, route by topic ID:

```yaml
gateway:
  routing:
    rules:
      - chat_id: "-1001234567890"
        thread_id: "5"
        profile: "work-dev"
      - chat_id: "-1001234567890"
        thread_id: "12"
        profile: "work-ops"
```

### How to Find Chat and Thread IDs

Send a message in the target chat, then check the gateway logs:

```bash
grep "chat_id" ~/.hermes/logs/gateway.log | tail -5
```

Or forward a message from the chat to [@getidsbot](https://t.me/getidsbot) on Telegram.

---

## Group Chat and Topic Behavior

### Adding Your Bot to a Group

1. Open the group in Telegram
2. Tap the group name → "Add Members"
3. Search for your bot's username and add it
4. **Important:** If the group has "Slow Mode" or admin-only messaging, grant your bot admin privileges or the bot won't be able to read messages

### Bot Privacy Mode

By default, Telegram bots only see messages that mention them or start with `/`. To let your bot see all messages in a group:

1. Chat with @BotFather
2. Send `/mybots`
3. Select your bot → "Bot Settings" → "Group Privacy" → "Turn off"

Now your bot can read all group messages, not just commands.

### Topic-Based Sessions

When `topic_sessions: true` is enabled, each Telegram topic (or each DM) gets its own Hermes session. This means:

- You can have 5 different conversations with your bot simultaneously
- Each conversation has independent context — they don't interfere
- Use `/new` to reset a specific topic's session

### Home Channel

Set a default delivery target for cron jobs and system notifications:

```
/sethome
```

Send this command in the chat where you want notifications delivered. Hermes remembers this as the "home channel."

---

## Running the Gateway as a Background Service

For 24/7 availability, the gateway should run as a system service that auto-starts on boot and restarts on crash.

### macOS (LaunchAgent)

Create `~/Library/LaunchAgents/ai.hermes.gateway.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>ai.hermes.gateway</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/hermes</string>
        <string>gateway</string>
        <string>run</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/you/.hermes/logs/gateway-stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/you/.hermes/logs/gateway-stderr.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
    </dict>
</dict>
</plist>
```

Load it:

```bash
launchctl load ~/Library/LaunchAgents/ai.hermes.gateway.plist
```

### Linux (systemd)

Create `~/.config/systemd/user/hermes-gateway.service`:

```ini
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/hermes gateway run
Restart=always
RestartSec=10
Environment="PATH=/usr/local/bin:/usr/bin:/bin"

[Install]
WantedBy=default.target
```

Enable and start:

```bash
systemctl --user daemon-reload
systemctl --user enable hermes-gateway
systemctl --user start hermes-gateway

# Enable linger so it runs without you being logged in:
sudo loginctl enable-linger $USER
```

### Windows

Create a scheduled task to run on startup, or use NSSM (Non-Sucking Service Manager):

```powershell
nssm install HermesGateway "C:\Users\you\.hermes\venv\Scripts\hermes.exe" "gateway run"
nssm start HermesGateway
```

For full Windows service setup details, see the [Windows Installation Guide](wiki/windows-install).

---

## Gateway Slash Commands

These commands work from any messaging platform connected to your gateway:

| Command | Action |
|---------|--------|
| `/new` | Start a fresh session |
| `/model` | Show or change the current model |
| `/config` | Show current configuration |
| `/skills` | Browse and install skills |
| `/cron` | Manage scheduled jobs |
| `/profile` | Show active profile info |
| `/approve` | Approve a pending dangerous command |
| `/deny` | Deny a pending dangerous command |
| `/sethome` | Set current chat as home channel |
| `/restart` | Restart the gateway |
| `/stop` | Stop background processes |
| `/status` | Show session info |
| `/help` | List all available commands |
| `/topic` | Toggle Telegram topic session mode |
| `/platforms` | Show connected platform status |
| `/debug` | Generate and upload a debug report |

---

## Security and Approval Settings

### Command Approval

By default, Hermes prompts for approval before running potentially dangerous commands (`rm -rf`, `git push --force`, etc.). Via Telegram, you'll see a message like:

```
⚠️ Hermes wants to run:
  rm -rf /important/directory

/approve — Allow this command
/deny   — Block this command
```

Configure approval behavior:

```bash
# Always ask (default, safest)
hermes config set approvals.mode "manual"

# Use an auxiliary LLM to auto-approve low-risk commands
hermes config set approvals.mode "smart"

# Skip all approval prompts (not recommended)
hermes config set approvals.mode "off"
```

### User Access Control

Restrict who can control your Hermes via Telegram:

```yaml
gateway:
  platforms:
    telegram:
      allow_list:
        - "YOUR_TELEGRAM_USER_ID"
```

Anyone not in the allow list will be ignored by the bot.

### Secret Redaction

API keys and passwords in tool output are automatically redacted from gateway messages. This is enabled by default:

```bash
hermes config set security.redact_secrets true
```

---

## Troubleshooting

### Bot doesn't respond

1. Check gateway is running: `hermes gateway status`
2. Check bot token is correct: the token from @BotFather
3. Check `.env` has `TELEGRAM_BOT_TOKEN`
4. Check gateway logs:

```bash
tail -50 ~/.hermes/logs/gateway.log
```

### "Gateway not running" after reboot

Your background service might not be configured correctly:

- **macOS:** Check LaunchAgent is loaded: `launchctl list | grep hermes`
- **Linux:** Check systemd service: `systemctl --user status hermes-gateway`
- **Linux WSL2:** Ensure `systemd=true` in `/etc/wsl.conf`

### Bot only sees commands starting with /

Telegram bot privacy mode is on. Turn it off via @BotFather → Bot Settings → Group Privacy → Turn off.

### Gateway dies when I close the terminal

You're running in foreground mode (`hermes gateway run`). Use background mode instead:

```bash
hermes gateway start
```

Or set up a system service (see [Running as a Background Service](#running-the-gateway-as-a-background-service)).

### Multiple people using my bot get mixed sessions

Enable `topic_sessions: true` in gateway config. This gives each DM its own isolated session.

### Can't add bot to a group

The group may have restrictions. Ask the group admin to add the bot, or create a new group where you're admin.

### "Forbidden: bot was blocked by the user"

You (or someone) blocked the bot on Telegram. Unblock it: open the bot's chat, tap the name, tap "Unblock."

### Discord bot is silent

Enable **Message Content Intent** in Discord Developer Portal → Bot → Privileged Gateway Intents.

### Slack bot only works in DMs

Subscribe to the `message.channels` event in your Slack app configuration.

### Gateway crash loop

Reset the failed state:

```bash
# Linux/systemd:
systemctl --user reset-failed hermes-gateway

# macOS:
launchctl unload ~/Library/LaunchAgents/ai.hermes.gateway.plist
launchctl load ~/Library/LaunchAgents/ai.hermes.gateway.plist
```

---

## FAQ

### Is the Telegram bot free?

Yes. Creating a Telegram bot via @BotFather is free. There are no costs for messages sent through the bot. The only costs are your LLM API usage if you use a cloud model.

### Can I use multiple Telegram bots with Hermes?

Yes, but only one bot per gateway instance. If you need multiple bots, run multiple gateway instances with different profiles or on different machines.

### Can Hermes read my other Telegram conversations?

No. The bot only sees messages sent directly to it or in groups where it's a member. It cannot access your private chats with other people.

### Can I use Hermes via Telegram when my computer is off?

No — the gateway runs on your computer. If your computer is off or asleep, the bot won't respond. For 24/7 access, run Hermes on an always-on machine (see the [Multi-Machine Setup Guide](wiki/multi-machine-setup)).

### How do I switch profiles from Telegram?

Use the `/profile` command or configure [routing rules](#multi-profile-routing) so different chats go to different profiles automatically.

### Can the bot send messages proactively?

Yes — cron jobs and system notifications can deliver to your Telegram chat, even if you haven't messaged the bot recently. The bot initiates the conversation.

### What happens if I send a file to the bot?

The gateway forwards it to Hermes for processing. Images can be analyzed with vision, documents can be read, and code files can be processed. Hermes will use its tools to handle the file appropriately.

### Is my conversation history stored on Telegram's servers?

Standard Telegram cloud chats are stored on Telegram's servers (encrypted in transit, stored encrypted). For maximum privacy, use Telegram's "Secret Chat" feature (note: bots don't support Secret Chats) or use a local-only setup without the gateway.

### Can I have different skills for Telegram vs. terminal?

Yes. Configure skill enablement per platform in `~/.hermes/config.yaml`:

```bash
hermes skills config
```

You can have certain skills only available via Telegram and others only in the terminal.

### How do I know which model is responding?

Enable the gateway footer: `hermes config set gateway.platforms.telegram.footer true`. Each reply will include the model name and session ID at the bottom.

### Can I use the same bot token for multiple Hermes instances?

Technically yes, but it causes message routing conflicts — Telegram only delivers webhook events to one URL. If two gateway instances share a token, messages will randomly go to one or the other. Use one gateway instance and route to different profiles within it, or use separate bot tokens.

### How do I set up a custom bot name, profile picture, and description?

Chat with @BotFather on Telegram:
- `/setname` — change the display name
- `/setuserpic` — set a profile photo
- `/setdescription` — set the description shown in the bot's profile
- `/setabouttext` — set the "What can this bot do?" text
- `/setcommands` — set the command list (e.g., `/help`, `/new`, `/model`)

For Hermes, a suggested command list:

```
help - Show available commands
new - Start a fresh session
model - Show or change the current model
status - Show session info
profile - Show active profile
cron - Manage scheduled jobs
skills - Browse and install skills
```

### Can I use Hermes with Telegram topics (threads in groups)?

Yes. Telegram groups with topics enabled create threaded conversations. Hermes can route each topic to a different profile using `thread_id` in routing rules. When `topic_sessions: true`, each topic gets its own isolated Hermes session.

### What happens when Telegram rate limits my bot?

Telegram allows ~30 messages per second per bot. Hermes queues outgoing messages and respects rate limits automatically. If you're sending very long responses, Hermes splits them into multiple messages (Telegram's limit is 4,096 characters per message).

### How do I disconnect a platform without uninstalling?

```bash
# Disable a specific platform while keeping the config:
hermes tools disable messaging

# Or remove the platform from config entirely:
hermes config edit
# Delete the platform block under gateway.platforms
```

The gateway needs a restart after disabling platforms.

---

## Next Steps

**Gateway delivers the results — now automate the work:**

1. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule tasks and get results on your phone
2. **[Multi-Machine Setup →](wiki/multi-machine-setup)** Run the gateway on an always-on home server
3. **[Profiles Guide →](wiki/profiles-guide)** Route different Telegram chats to different profiles

**Also see:** [Start Here](wiki/start-here) · [Skills Guide](wiki/skills-guide) · [Official Gateway Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
