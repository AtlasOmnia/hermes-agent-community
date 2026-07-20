# Hermes Agent on Windows: Complete Installation and Configuration Guide

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to installing and configuring Hermes Agent on Windows. Covers native install, WSL2 setup, GPU passthrough, Windows Service configuration, and troubleshooting common Windows-specific issues.

---

## Table of Contents

- [Windows Support Overview](#windows-support-overview)
- [Method 1: Native Windows Install (Recommended)](#method-1-native-windows-install-recommended)
- [Method 2: WSL2 Install](#method-2-wsl2-install)
- [Method 3: Git Bash / MSYS2](#method-3-git-bash-msys2)
- [Setting Up Local Models on Windows](#setting-up-local-models-on-windows)
- [GPU Configuration](#gpu-configuration)
- [Running Hermes as a Windows Service](#running-hermes-as-a-windows-service)
- [Windows-Specific Configuration](#windows-specific-configuration)
- [Known Windows Issues and Fixes](#known-windows-issues-and-fixes)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## Windows Support Overview

Hermes Agent runs natively on Windows via PowerShell, Command Prompt, Windows Terminal, Git Bash (mintty), and VS Code's integrated terminal. Both native Windows and WSL2 (Windows Subsystem for Linux) are fully supported.

**Minimum requirements for Windows:**

- Windows 10 (build 19041+) or Windows 11
- Python 3.11+ (native Windows install or WSL2)
- 4GB RAM (8GB recommended for local models)
- 2GB free disk space (plus model storage for local LLMs)
- PowerShell 5.1+ or Windows Terminal

**Which installation method should you choose?**

| Method | Best For | GPU Support | Gateway Service | Complexity |
|--------|----------|------------|-----------------|------------|
| **Native Windows** | Most users, direct GPU access | Native CUDA/DirectML | Windows Service or NSSM | Low |
| **WSL2** | Linux-native workflows, Docker | GPU passthrough (WSL2) | systemd service | Medium |
| **Git Bash** | Lightweight, POSIX-like terminal | Limited | Manual | Low |

---

## Method 1: Native Windows Install (Recommended)

### Step 1: Install Python

Download Python 3.11 or 3.12 from [python.org](https://python.org/downloads/). During installation:

- ✅ Check "Add Python to PATH"
- ✅ Check "Install for all users" (optional, but recommended)

Verify:

```powershell
python --version
# Python 3.12.x
```

### Step 2: Install Hermes Agent

Open PowerShell as Administrator and run:

```powershell
# Using the PowerShell installer (recommended):
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

Or download the Windows installer from the [releases page](https://github.com/NousResearch/hermes-agent/releases).

### Step 3: Run Setup

```powershell
hermes setup
```

The setup wizard walks you through:

1. Model selection (local vs. cloud)
2. API key configuration (if using cloud models)
3. Tool enablement (terminal, browser, web search, etc.)
4. Gateway configuration (optional — for Telegram/Discord)

### Step 4: Verify Installation

```powershell
hermes --version
hermes doctor
```

`hermes doctor` checks your config, Python environment, and dependencies. Fix any issues it reports before proceeding.

### Step 5: Start Using Hermes

```powershell
hermes
```

You're now in an interactive Hermes session. Try:

```
Create a file called hello.txt on my desktop with the text "Hello from Hermes on Windows!"
```

### Windows-Specific Paths

After native installation, Hermes lives at:

```
~\.hermes\                    # Hermes home directory
~\.hermes\config.yaml         # Configuration
~\.hermes\.env                # API keys and secrets
~\.hermes\skills\             # Installed skills
~\.hermes\sessions\           # Session data
~\.hermes\logs\               # Gateway and error logs
~\.hermes\venv\               # Python virtual environment
```

Unlike macOS/Linux, `~` resolves to `C:\Users\<YourUsername>`.

---

## Method 2: WSL2 Install

WSL2 provides a full Linux environment on Windows, which some users prefer for development workflows.

### Step 1: Install WSL2

Open PowerShell as Administrator:

```powershell
wsl --install
```

This installs WSL2 with Ubuntu by default. Restart your computer if prompted.

### Step 2: Configure WSL2 for GPU Access

```powershell
wsl --update
```

WSL2 with updated kernel includes GPU passthrough for CUDA and DirectML.

Verify GPU is available in WSL2:

```bash
# Inside WSL2:
nvidia-smi
# Should show your GPU
```

### Step 3: Install Hermes in WSL2

Open your WSL2 terminal (Ubuntu) and follow the Linux installation:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
```

### Step 4: Enable systemd for Gateway Service

WSL2 needs systemd enabled for `hermes gateway start` to work as a service:

Edit `/etc/wsl.conf`:

```ini
[boot]
systemd=true
```

Then restart WSL2 from PowerShell:

```powershell
wsl --shutdown
wsl
```

### WSL2 Pros and Cons

**Pros:**
- Full Linux environment — all Linux tools work natively
- GPU passthrough works well for CUDA workloads
- Easier gateway service management (systemd)
- Better Docker integration

**Cons:**
- Slight performance overhead vs. native Windows
- WSL2 must be running for Hermes to work
- File paths differ between Windows and WSL2 (`/mnt/c/Users/...` vs. `C:\Users\...`)
- Network configuration can be tricky for multi-machine setups

---

## Method 3: Git Bash / MSYS2

For a lightweight POSIX-like environment without WSL2:

### Install

```bash
# In Git Bash:
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### Limitations

- GPU access is limited (no CUDA passthrough from Git Bash)
- No systemd — gateway must be run manually
- Some terminal tools may not work as expected
- Python packages with C extensions may fail to compile

Git Bash is fine for cloud-model-only usage or basic terminal tasks. For local models or gateway services, use Native Windows or WSL2.

---

## Setting Up Local Models on Windows

### Option 1: LM Studio (Easiest)

LM Studio runs natively on Windows with full GPU acceleration.

1. Download from [lmstudio.ai](https://lmstudio.ai)
2. Install and launch
3. Search for a model (e.g., "qwen2.5-coder-14b-instruct")
4. Download a GGUF quant (Q4_K_M recommended)
5. Load the model
6. Start the local server (default: `http://127.0.0.1:1234`)

Configure Hermes to use LM Studio:

```yaml
# In ~\.hermes\config.yaml:
model:
  provider: "custom:lmstudio"
  default: "qwen2.5-coder-14b-instruct"

providers:
  custom:lmstudio:
    base_url: "http://127.0.0.1:1234/v1"
    api_key: "lm-studio"
```

### Option 2: Ollama on Windows

Ollama now has native Windows support:

1. Download from [ollama.com](https://ollama.com)
2. Install and it runs as a Windows service automatically
3. Pull a model:

```powershell
ollama pull qwen2.5-coder:14b
```

Configure Hermes:

```yaml
model:
  provider: "ollama"
  default: "qwen2.5-coder:14b"
```

### Option 3: llama.cpp (Advanced)

Build llama.cpp natively on Windows (requires CMake and a C++ compiler) or download pre-built binaries.

```powershell
# Download a GGUF from Hugging Face, then:
.\llama-server.exe -m qwen2.5-coder-14b-q4_k_m.gguf --port 8080
```

---

## GPU Configuration

Hermes doesn't use the GPU directly — your model server does. The key is making sure your model runner can see your GPU.

### NVIDIA GPUs (CUDA)

**Native Windows:**
- Install [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) or just the latest NVIDIA driver
- LM Studio and Ollama auto-detect CUDA GPUs
- llama.cpp must be built with `-DGGML_CUDA=ON`

**WSL2:**
- Install NVIDIA driver for WSL2 (included in standard NVIDIA drivers now)
- CUDA toolkit inside WSL2: `sudo apt install nvidia-cuda-toolkit`

### AMD GPUs (ROCm / Vulkan)

- LM Studio supports AMD GPUs via Vulkan (enable in Settings → GPU Acceleration)
- llama.cpp can be built with Vulkan or ROCm support

### Intel Arc GPUs

- LM Studio supports Intel Arc via Vulkan
- llama.cpp Intel SYCL backend is available but less mature than CUDA

### Verifying GPU Is Used

```powershell
# Check GPU usage while a model is running:
nvidia-smi              # NVIDIA
# Or check Task Manager → Performance → GPU
```

If your GPU shows 0% utilization while a model is running, the model is on CPU. Check your model server's settings.

---

## Running Hermes as a Windows Service

For 24/7 gateway availability, run Hermes as a Windows service.

### Option 1: NSSM (Non-Sucking Service Manager) — Recommended

Download [NSSM](https://nssm.cc/download) and extract it.

```powershell
# Install Hermes gateway as a service:
nssm install HermesGateway

# In the NSSM GUI that opens:
# Application tab:
#   Path: C:\Users\you\.hermes\venv\Scripts\hermes.exe
#   Arguments: gateway run
#   Startup directory: C:\Users\you

# Start the service:
nssm start HermesGateway

# Check status:
nssm status HermesGateway
```

### Option 2: Windows Task Scheduler

1. Open Task Scheduler (taskschd.msc)
2. Create Task → "Run whether user is logged on or not"
3. Trigger: "At startup"
4. Action: Start a program
   - Program: `C:\Users\you\.hermes\venv\Scripts\hermes.exe`
   - Arguments: `gateway run`

### Option 3: Manual (for testing)

```powershell
# Run in the current terminal window (stops when you close it):
hermes gateway run

# Or use the built-in service commands (if configured):
hermes gateway start
hermes gateway stop
hermes gateway status
```

---

## Windows-Specific Configuration

### Forward Slashes vs. Backslashes

Hermes tools accept forward slashes everywhere, which avoids escaping issues:

```yaml
# Good — forward slashes:
terminal:
  cwd: "C:/Users/you/projects"

# Avoid — backslashes require escaping:
terminal:
  cwd: "C:\\Users\\you\\projects"
```

### Path Environment

On Windows, Hermes uses PowerShell-style environment resolution. `~` is expanded to `$HOME` (typically `C:\Users\<Username>`).

### UTF-8 BOM in config.yaml

**Issue:** Some Windows editors (notably Notepad) save files with a UTF-8 BOM (Byte Order Mark). Hermes can't parse YAML with a BOM, resulting in an "HTTP 400 — No models provided" error on first run.

**Fix:** Always edit `config.yaml` with a proper editor that doesn't add BOM:
- VS Code
- Notepad++
- Sublime Text
- Or use `hermes config edit` (always writes without BOM)

### Windows Terminal and Keybindings

**Alt+Enter:** Windows Terminal intercepts Alt+Enter for fullscreen toggle — it never reaches Hermes. Use **Ctrl+Enter** to insert a newline in the Hermes CLI.

**Ctrl+J side effect:** On Windows, Ctrl+Enter and Ctrl+J send the same keycode, so Ctrl+J also inserts a newline. This is unavoidable due to Windows Console API behavior.

**Diagnostic tool:**

```powershell
python scripts/keystroke_diagnostic.py
```

Shows exactly how each keystroke is recognized by prompt_toolkit.

---

## Known Windows Issues and Fixes

### 1. "No models provided" (HTTP 400)

**Cause:** config.yaml was saved with UTF-8 BOM by a Windows editor.

**Fix:**
```powershell
hermes config edit
# Save and exit. Hermes rewrites without BOM.
```

### 2. WinError 10106 in execute_code

**Cause:** The code execution sandbox strips essential Windows environment variables (`SYSTEMROOT`, `WINDIR`, `COMSPEC`), preventing Python from creating network sockets.

**Fix:** This was patched in the Hermes codebase. Update to the latest version:

```powershell
hermes update
```

### 3. Test suite doesn't run on Windows

The test runner script (`scripts/run_tests.sh`) expects POSIX venv layouts (`.venv/bin/activate`). The Hermes-installed venv at `venv/Scripts/` is stripped for install size.

**Workaround:**
```powershell
# Install pytest into system Python 3.11:
& "C:\Program Files\Python311\python.exe" -m pip install --user pytest pytest-xdist pyyaml

# Run tests directly:
$env:PYTHONPATH = (Get-Location).Path
& "C:\Program Files\Python311\python.exe" -m pytest tests/ -v --tb=short -n 0
```

Use `-n 0` (not `-n 4`) because `pyproject.toml` defaults include `-n`.

### 4. Gateway dies when WSL2 terminal closes

**Cause:** WSL2 without systemd falls back to `nohup`, which dies when the session closes.

**Fix:** Enable systemd in `/etc/wsl.conf`:
```ini
[boot]
systemd=true
```

Then restart WSL2 from PowerShell:
```powershell
wsl --shutdown
wsl
```

### 5. Line ending warnings from Git

**Cause:** Git warns `LF will be replaced by CRLF`. This is cosmetic — the repo's `.gitattributes` normalizes line endings.

**Fix:** Don't let editors auto-convert committed POSIX-newline files to CRLF. If you see the warning, it's benign.

### 6. GPU not detected by LM Studio

- Ensure NVIDIA drivers are up to date
- In LM Studio, go to Settings → GPU Acceleration → select your GPU
- For WSL2: update the WSL2 kernel (`wsl --update`)

### 7. "Python was not found" after install

Python wasn't added to PATH. Re-run the Python installer and check "Add Python to PATH," or add it manually:

```powershell
# Add to current session:
$env:Path += ";C:\Users\you\AppData\Local\Programs\Python\Python312"

# Add permanently:
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\you\AppData\Local\Programs\Python\Python312", "User")
```

---

## FAQ

### Does Hermes Agent work on Windows 10 and Windows 11?

Yes. Both are fully supported. Windows 10 requires build 19041 or later.

### Can I use Hermes Agent without WSL?

Yes. Native Windows install works perfectly via PowerShell, Command Prompt, Windows Terminal, or Git Bash. WSL2 is optional.

### Which terminal should I use on Windows?

Windows Terminal (from the Microsoft Store) is the best experience. It supports tabs, themes, and proper keybinding handling. Command Prompt works but is less polished. Git Bash (mintty) works for basic use.

### How do I set up GPU acceleration for local models?

Install LM Studio or Ollama natively on Windows. Both auto-detect NVIDIA GPUs. For llama.cpp, build with CUDA support. See the [GPU Configuration section](#gpu-configuration).

### Can the gateway run as a Windows Service?

Yes. Use NSSM to wrap `hermes gateway run` as a Windows Service. It will auto-start on boot and restart on crash. See [Running as a Windows Service](#running-hermes-as-a-windows-service).

### What if I want to use both Windows and Linux tools?

Install Hermes natively on Windows and connect to it from WSL2 via the gateway or by configuring multi-machine access. Or use the [Multi-Machine Setup Guide](wiki/multi-machine-setup) to run Hermes on a separate Linux machine.

### Do cron jobs work on Windows?

Yes. The Hermes scheduler runs natively on Windows. It doesn't use the Windows Task Scheduler — it's an internal scheduler that works identically across platforms.

### Is there a Windows installer with a GUI?

Currently, installation is via PowerShell script or manual download. The setup wizard (`hermes setup`) provides an interactive text-based UI. A graphical installer is planned but not yet available.

### How do I fix "Execution of scripts is disabled on this system"?

PowerShell's execution policy may block the install script:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then re-run the install command.

### Will Hermes work on ARM Windows (Snapdragon X)?

Python and most tools work on ARM Windows. However, local model support is limited — many GGUF inference engines don't yet have ARM Windows builds. Cloud models work fine. ARM Windows support is improving rapidly.

### How do I completely uninstall Hermes from Windows?

```powershell
hermes uninstall
```

This removes the Hermes installation. To also remove all configuration and data:

```powershell
# Remove Hermes data directory:
Remove-Item -Recurse -Force "$env:USERPROFILE\.hermes"

# Remove from PATH if manually added:
# Edit System Environment Variables → Path → Remove Hermes entry
```

### Can I run Hermes alongside WSL2 for GPU model serving and native Windows for the gateway?

Yes — this is a powerful hybrid setup. Run LM Studio or Ollama in WSL2 (Linux CUDA support is more mature) and connect to it from native Windows Hermes via `http://localhost:11434` (WSL2 auto-forwards localhost). The gateway runs natively on Windows for better service management.

### What's the best editor for Hermes config on Windows?

VS Code or Notepad++. Avoid plain Notepad — it adds a UTF-8 BOM that breaks YAML parsing. Use `hermes config edit` which opens your `$EDITOR` and always writes without BOM.

### How do I add Hermes to Windows Terminal profiles?

Open Windows Terminal Settings → "Add a new profile" → Command line:

```
C:\Users\you\.hermes\venv\Scripts\hermes.exe
```

Set the name to "Hermes" and optionally choose an icon. Now Hermes has a dedicated tab in Windows Terminal.

### Does Hermes work with Windows Sandbox?

Hermes can be installed inside Windows Sandbox for isolated testing, but the sandbox is ephemeral — everything is lost when you close it. Use a proper VM (Hyper-V, VirtualBox) for persistent Windows testing environments.

### How do I set up Hermes for multiple Windows user accounts?

Install Hermes once (system-wide or per-user), then each user runs `hermes setup` in their own account. Each user gets their own `~\.hermes\` directory with isolated configs, skills, and memory. This is simpler than profiles for truly separate users.

---

## Next Steps

**Now that Hermes is running on Windows:**

1. **[Model Guide →](wiki/model-guide)** Pick the right model for your Windows GPU
2. **[Telegram Gateway Setup →](wiki/telegram-gateway-setup)** Connect Hermes to your phone
3. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule tasks that run 24/7

**Also see:** [Start Here](wiki/start-here) · [Multi-Machine Setup](wiki/multi-machine-setup) · [Browser Automation](wiki/browser-automation) · [Official Docs](https://hermes-agent.nousresearch.com/docs)
