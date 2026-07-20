# Multi-Machine Hermes Agent: Remote Gateway, Distributed Setup, and Home Server Guide

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to running Hermes Agent across multiple machines: remote gateway architecture, Mac host + Windows PC worker pattern, networking, firewall, SSH tunneling, and always-on home server configuration.

---

## Table of Contents

- [Why Run Hermes on Multiple Machines?](#why-run-hermes-on-multiple-machines)
- [Architecture Patterns](#architecture-patterns)
- [Pattern 1: Gateway Host + Model Server](#pattern-1-gateway-host--model-server)
- [Pattern 2: Mac Host + Windows PC Worker](#pattern-2-mac-host--windows-pc-worker)
- [Pattern 3: Home Server + Remote Access](#pattern-3-home-server--remote-access)
- [Pattern 4: Multi-Profile Multi-Machine](#pattern-4-multi-profile-multi-machine)
- [Networking and Firewall Setup](#networking-and-firewall-setup)
- [SSH Tunneling for Secure Remote Access](#ssh-tunneling-for-secure-remote-access)
- [Always-On Configuration](#always-on-configuration)
- [Troubleshooting Multi-Machine Issues](#troubleshooting-multi-machine-issues)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## Why Run Hermes on Multiple Machines?

Distributing Hermes across multiple machines is the most common power-user pattern in the r/hermesagent community. The motivations:

| Pattern | Why People Do It |
|---------|-----------------|
| **GPU server + lightweight client** | Run large models on a beefy Linux box; interact from a laptop |
| **Always-on gateway** | Mac Mini stays on; Windows PC with GPU shuts down when idle |
| **Separate concerns** | Gateway + skills on one machine, model inference on another |
| **Remote access** | Hermes on a home server, controlled from anywhere via Telegram |
| **Multi-OS workflow** | macOS for daily use, Windows/Linux for GPU-heavy AI work |

The key insight: Hermes is modular. The gateway (messaging), the terminal backend, and the model inference server can all run on different machines.

---

## Architecture Patterns

### The Hermes Stack (What Runs Where)

```
┌─────────────────────────────────────────────────┐
│                  Hermes Stack                     │
│                                                   │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ Gateway  │  │  Agent   │  │ Model Server  │  │
│  │(Telegram,│  │  Core    │  │(LM Studio,    │  │
│  │ Discord, │  │ (Tool    │  │ Ollama,       │  │
│  │ Slack)   │  │  Loop)  │  │ llama.cpp)   │  │
│  └──────────┘  └──────────┘  └───────────────┘  │
│       │              │               │            │
│       ▼              ▼               ▼            │
│  "Always on"    "Where the       "Where the      │
│   machine"      work happens"    GPU lives"      │
└─────────────────────────────────────────────────┘
```

These three components can be on one machine (typical laptop setup) or distributed across three machines (advanced home lab setup).

---

## Pattern 1: Gateway Host + Model Server

**The most common multi-machine pattern.** The gateway runs on an always-on machine (Mac Mini, Raspberry Pi, old laptop). The model server runs on a GPU-equipped machine (gaming PC, workstation).

```
┌──────────────────┐         ┌──────────────────────┐
│  Always-On Host  │         │   GPU Machine         │
│  (Mac Mini)      │         │   (Windows/Linux PC)  │
│                  │         │                       │
│  ┌────────────┐  │  HTTP   │  ┌─────────────────┐ │
│  │ Gateway    │──┼────────►│  │ LM Studio       │ │
│  │ + Agent    │  │  1234   │  │ Qwen 27B        │ │
│  │ Core       │  │         │  │ 192.168.1.117   │ │
│  └────────────┘  │         │  └─────────────────┘ │
│        │         │         │                       │
│  Telegram API    │         │  GPU: RTX 5090 32GB  │
└──────────────────┘         └──────────────────────┘
```

### Setup Steps

**On the GPU machine (Windows/Linux):**

1. Install LM Studio and download your model
2. Start the local server: Settings → Local Server → Start
3. Note the IP address (e.g., `192.168.1.117`) and port (`1234`)
4. Configure firewall to allow port 1234 from your local network:

**Windows:**
```powershell
New-NetFirewallRule -DisplayName "LM Studio" -Direction Inbound -LocalPort 1234 -Protocol TCP -Action Allow
```

**Linux:**
```bash
sudo ufw allow from 192.168.1.0/24 to any port 1234
```

**On the gateway machine (Mac/Linux):**

In `~/.hermes/config.yaml`:

```yaml
model:
  provider: "custom:lmstudio-windows"
  default: "qwen3.6-27b-claude-4.6-instruct"

providers:
  custom:lmstudio-windows:
    base_url: "http://192.168.1.117:1234/v1"
    api_key: "lm-studio"
    default_model: "qwen3.6-27b-claude-4.6-instruct"
```

Verify connectivity:

```bash
curl http://192.168.1.117:1234/v1/models
```

If you see a JSON response with model info, the gateway can reach the model server.

### Configuring Auxiliary Models

You may want auxiliary tasks (vision, compression) to run on a different endpoint:

```yaml
auxiliary:
  compression:
    provider: "custom:lmstudio-windows"
    model: "qwen2.5-coder-7b-instruct"
  vision:
    provider: "custom:lmstudio-mac"    # Vision stays on Mac
    model: "qwen2.5-vl-7b-instruct"
```

---

## Pattern 2: Mac Host + Windows PC Worker

**Jonathan's setup** and the most common r/hermesagent power-user configuration. The Mac runs the gateway and agent loop. The Windows PC runs the models on its GPU.

```
┌─────────────────────────┐       ┌──────────────────────────┐
│  Mac (macOS)            │       │  Windows PC (JARVIS)      │
│  Always On              │       │  GPU Server               │
│                         │       │                           │
│  ┌───────────────────┐  │ HTTP  │  ┌─────────────────────┐  │
│  │ Hermes Gateway    │──┼──────►│  │ LM Studio           │  │
│  │ + Agent Core      │  │ :1234 │  │ Qwen 27B Q4_K_M     │  │
│  │                   │  │       │  │ RTX 5090 32GB       │  │
│  │ ┌───────────────┐ │  │       │  │ RTX 5070 Ti 16GB    │  │
│  │ │Cron Scheduler │ │  │       │  │ Split GPU inference │  │
│  │ └───────────────┘ │  │       │  └─────────────────────┘  │
│  │                   │  │       │                           │
│  │ ┌───────────────┐ │  │ HTTP  │  ┌─────────────────────┐  │
│  │ │Auxiliary Tasks│ │──┼──────►│  │ Unsloth (optional)  │  │
│  │ │(compression,  │ │  │ :8888 │  │ Aux model endpoint  │  │
│  │ │ title, etc.)  │ │  │       │  └─────────────────────┘  │
│  │ └───────────────┘ │  │       │                           │
│  └───────────────────┘  │       └──────────────────────────┘
│                         │
│  ┌───────────────────┐  │
│  │ Dashboard Backend │  │
│  │ (FastAPI)         │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

### Setup Steps

**On the Windows PC:**

1. Install LM Studio, download and load `qwen3.6-27b-claude-4.6-instruct` (Q4_K_M)
2. Start the local server on port 1234
3. Set a static IP or DHCP reservation for the Windows PC (e.g., `192.168.1.117`)
4. Allow port 1234 through Windows Firewall
5. Optionally: set up Unsloth or a second LM Studio instance on port 8888 for auxiliary model

**On the Mac:**

```yaml
# ~/.hermes/config.yaml

model:
  provider: "custom:lmstudio-windows"
  default: "qwen3.6-27b-claude-4.6-instruct"
  context_length: 98304

providers:
  custom:lmstudio-windows:
    base_url: "http://192.168.1.117:1234/v1"
    api_key: "lm-studio"
    default_model: "qwen3.6-27b-claude-4.6-instruct"

  custom:unsloth-windows:
    base_url: "http://192.168.1.117:8888/v1"
    api_key: "sk-unsloth-..."

auxiliary:
  compression:
    provider: "custom:unsloth-windows"
    model: "qwen3.5-9b-claude-4.6-instruct"
  vision:
    provider: "custom:lmstudio-mac"   # Vision stays local
    model: "qwen2.5-vl-7b-instruct"

fallback_providers:
  - "main"   # If Windows is unreachable, fall back to local Mac model
```

**Auto-start LM Studio on Windows:**

Set LM Studio to start with Windows and auto-load your model. In LM Studio: Settings → "Start Server on Launch" + "Load Model on Launch."

### Power Management

The Windows PC doesn't need to stay on 24/7. The Mac runs the gateway — when you send a message from Telegram, the Mac tries to reach the Windows PC. If it's sleeping:

- **Wake-on-LAN:** Configure WOL on the Windows PC's network adapter and BIOS, then send a magic packet from the Mac when needed
- **Scheduled power:** Set the PC to wake at 7 AM and sleep at midnight via Task Scheduler
- **Manual:** Turn on the PC when you need heavy AI work; the Mac gateway still responds (with fallback model) when the PC is off

---

## Pattern 3: Home Server + Remote Access

Run Hermes on a dedicated home server (old desktop, NUC, Raspberry Pi 5, Mac Mini) and access it from anywhere.

### Hardware Options

| Hardware | Cost | GPU? | Best For |
|----------|------|------|----------|
| Mac Mini M2/M3/M4 | $599+ | Integrated (good) | Gateway + local models (7B-14B) |
| Old Gaming PC | Free-$300 | Dedicated GPU | Gateway + large local models |
| Intel NUC | $200-500 | Integrated (weak) | Gateway only (cloud models or remote GPU) |
| Raspberry Pi 5 | $60-120 | No | Gateway only (lightweight, cloud models) |
| Used Dell/HP SFF | $100-300 | Optional low-profile GPU | Budget always-on server |

### Setup

1. Install Hermes on the server (Linux recommended for always-on)
2. Configure for cloud models (no GPU needed) or connect to a separate GPU machine
3. Set up Telegram gateway for remote access:

```bash
hermes gateway setup   # Select Telegram
hermes gateway start   # Run as background service
```

4. Enable automatic startup:

```bash
# systemd (Linux):
systemctl --user enable hermes-gateway

# LaunchAgent (macOS):
# Create ~/Library/LaunchAgents/ai.hermes.gateway.plist
```

5. Now message your bot from anywhere — Hermes processes the task on your home server.

### Security Considerations

- **Use allow_list:** Restrict Telegram access to your user ID only
- **Firewall:** Block direct access to LM Studio/Ollama ports from outside your LAN
- **SSH tunneling:** If you need terminal access to the server remotely, use SSH keys (never passwords)
- **VPN:** Consider Tailscale or WireGuard for secure access to your home network

---

## Pattern 4: Multi-Profile Multi-Machine

Run different profiles on different machines, all connected to the same Telegram bot.

```
┌──────────────────────────────────────────────────┐
│               Telegram Bot (@my_hermes)            │
└──────────┬──────────┬──────────┬─────────────────┘
           │          │          │
           ▼          ▼          ▼
    ┌──────────┐ ┌──────────┐ ┌──────────────┐
    │ Mac Mini │ │ Windows  │ │ Linux Server │
    │ Profile: │ │ Profile: │ │ Profile:     │
    │ personal │ │ work     │ │ dev          │
    └──────────┘ └──────────┘ └──────────────┘
```

This requires running separate Hermes gateway instances on each machine, all sharing the same Telegram bot token. **However, this is problematic** — Telegram only delivers messages to one webhook URL.

**Better approach: One gateway, remote model endpoints.** Run the gateway on one machine and configure different profiles with different model endpoints:

```yaml
# Profile "work" → uses Windows PC's GPU
# Profile "personal" → uses Mac's local model
# Profile "dev" → uses cloud model (Anthropic)
```

Route messages to profiles based on Telegram chat or topic (see the [Telegram Gateway Setup Guide](wiki/telegram-gateway-setup) for routing rules).

---

## Networking and Firewall Setup

### Finding Your Machines' IPs

**macOS:**
```bash
ipconfig getifaddr en0   # Wi-Fi
ipconfig getifaddr en1   # Ethernet
```

**Windows:**
```powershell
ipconfig | findstr "IPv4"
```

**Linux:**
```bash
ip addr show | grep "inet "
```

### Setting Static IPs

Assign static IPs via your router's DHCP reservation so addresses don't change on reboot.

### Verifying Connectivity

From the gateway machine:

```bash
# Ping the model server:
ping 192.168.1.117

# Check the model server port:
curl http://192.168.1.117:1234/v1/models

# Expected response: JSON with model info
```

### Firewall Rules

| Machine | Port | Direction | Purpose |
|---------|------|-----------|---------|
| Model server (PC) | 1234 | Inbound | LM Studio API |
| Model server (PC) | 8888 | Inbound | Auxiliary model (if separate) |
| Ollama server | 11434 | Inbound | Ollama API |
| Gateway machine | 8080 | Inbound | Dashboard (optional) |

Only expose these ports on your **local network** (not the internet), unless you know what you're doing.

---

## SSH Tunneling for Secure Remote Access

If you need to access your model server from outside your home network:

```bash
# From your laptop (outside home):
ssh -L 1234:192.168.1.117:1234 user@your-home-ip

# Now localhost:1234 tunnels to your home model server
# Configure Hermes to use http://127.0.0.1:1234/v1
```

### Auto-SSH for Persistent Tunnels

Install `autossh` to maintain the tunnel:

```bash
autossh -M 0 -N -L 1234:192.168.1.117:1234 user@your-home-ip &
```

### Tailscale (Easier Alternative)

[Tailscale](https://tailscale.com) creates a mesh VPN between your machines. Each machine gets a stable IP (like `100.x.x.x`) regardless of physical location.

```bash
# Install Tailscale on all machines
tailscale up

# Then configure Hermes with Tailscale IPs:
# base_url: "http://100.123.45.67:1234/v1"
```

Much simpler than SSH tunneling and works through NAT/firewalls automatically.

---

## Always-On Configuration

### macOS (LaunchAgent)

See the [Telegram Gateway Setup Guide](wiki/telegram-gateway-setup#macos-launchagent) for the full LaunchAgent plist.

```bash
launchctl load ~/Library/LaunchAgents/ai.hermes.gateway.plist
```

### Linux (systemd)

```bash
systemctl --user enable hermes-gateway
sudo loginctl enable-linger $USER   # Keeps running when you log out
```

### Windows (NSSM / Task Scheduler)

See the [Windows Installation Guide](wiki/windows-install#running-hermes-as-a-windows-service).

### Keeping the Model Server Alive

LM Studio and Ollama both run persistently after starting the server. But to survive reboots:

**LM Studio on Windows:** Settings → "Start Server on Launch" + "Auto-load last model"

**LM Studio on macOS:** Add to Login Items (System Settings → General → Login Items)

**Ollama on Linux:** It installs as a systemd service automatically:
```bash
systemctl status ollama
```

---

## Troubleshooting Multi-Machine Issues

### "Connection refused" to model server

1. Is LM Studio/Ollama running on the target machine?
2. Is the local server enabled? (LM Studio: Settings → Local Server → Start)
3. Is the port correct? Default LM Studio: 1234, Ollama: 11434
4. Firewall blocking the port? Temporarily disable to test.

### Model server responds but Hermes can't use it

```bash
# Test the endpoint manually:
curl http://192.168.1.117:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen3.6-27b", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 10}'
```

If this works but Hermes doesn't, check your config.yaml provider configuration.

### IP address changes after reboot

Set a DHCP reservation on your router. Find the MAC address of the model server's network adapter and assign a fixed IP.

### Gateway works but model inference is slow

- The gateway machine might be too weak — that's fine, it only handles messaging
- If the model server is on Wi-Fi, switch to Ethernet (lower latency, more stable)
- For Wi-Fi-only setups, use a model with lower context length to reduce network transfer

### "Model not found" on remote endpoint

The model name in config.yaml must match exactly what the endpoint reports:

```bash
curl http://192.168.1.117:1234/v1/models | python3 -m json.tool
```

Look for the `"id"` field and use that exact string.

---

## FAQ

### Can I run Hermes on a Raspberry Pi?

Yes — as a gateway-only machine. The Pi handles messaging (Telegram, Discord) and routes tasks to cloud models or a separate GPU server. A Pi 4 or Pi 5 with 4GB+ RAM works well for this. Don't expect to run local models on a Pi (too slow).

### Do I need a static public IP for remote access?

No. Use Telegram as the remote control interface — it works from anywhere without port forwarding. If you need SSH access, use Tailscale or a similar mesh VPN.

### What's the cheapest always-on machine for Hermes?

A used thin client (Dell Wyse, HP T640) for $50-100, or a Raspberry Pi 5 for $60. Both draw <15W, cost pennies a day in electricity, and are perfectly capable as gateway-only machines.

### Can multiple people share the same Hermes instance?

Yes — via the Telegram gateway in a group chat. Each user's messages create isolated sessions if `topic_sessions: true` is enabled. For more control, use `allow_list` to restrict access.

### How do I run Hermes on a headless Linux server?

Same install process. Use `ssh` to access the server, run `hermes setup`, then start the gateway. Control everything via Telegram. No monitor, keyboard, or GUI needed.

### Can I wake my GPU machine on demand?

Yes with Wake-on-LAN. Enable WOL in the PC's BIOS and network adapter settings. From your always-on machine, send a magic packet:

```bash
# Install wakeonlan: brew install wakeonlan (macOS) or apt install wakeonlan (Linux)
wakeonlan AA:BB:CC:DD:EE:FF   # MAC address of GPU machine
```

### What happens if the model server is unreachable?

If you've configured `fallback_providers`, Hermes falls through to the next provider. Without fallback, tasks will fail with a connection error. See [Pattern 2](#pattern-2-mac-host--windows-pc-worker) for fallback configuration.

### Can I use different models for different profiles across machines?

Yes. Each profile can have its own model and provider configuration. Create a profile for each machine/endpoint combination. See the [Profiles Guide](wiki/profiles-guide).

### Is a VPN necessary for multi-machine Hermes?

Not for local network setups — they just need to be on the same LAN (or have static routes). For remote access (laptop + home server in different locations), Tailscale is the simplest solution.

---

## Next Steps

**Now that your machines are connected:**

1. **[Profiles Guide →](wiki/profiles-guide)** Create isolated profiles for each machine or use case
2. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule tasks on your always-on machine
3. **[Telegram Gateway Setup →](wiki/telegram-gateway-setup)** Control your multi-machine setup from your phone

**Also see:** [Start Here](wiki/start-here) · [Model Guide](wiki/model-guide) · [Windows Install](wiki/windows-install) · [Browser Automation](wiki/browser-automation)
