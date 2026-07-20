# Hermes Agent Model Guide: Best Local & Cloud LLMs (2026)

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to choosing the best LLM for Hermes Agent. Tiered recommendations by VRAM and budget, local vs cloud comparison, provider setup, and benchmark analysis. Updated for 2026.

---

## Table of Contents

- [How Hermes Uses LLMs](#how-hermes-uses-llms)
- [Local vs Cloud: Making the Right Choice](#local-vs-cloud-making-the-right-choice)
- [Local Model Recommendations by Hardware Tier](#local-model-recommendations-by-hardware-tier)
  - [8GB VRAM or Less](#8gb-vram-or-less)
  - [16GB VRAM](#16gb-vram)
  - [24GB VRAM](#24gb-vram)
  - [48GB+ / Multi-GPU](#48gb-multi-gpu)
- [Cloud Model Recommendations](#cloud-model-recommendations)
- [Provider Setup Guide](#provider-setup-guide)
- [How to Switch Models in Hermes](#how-to-switch-models-in-hermes)
- [What Makes a Good Hermes Model?](#what-makes-a-good-hermes-model)
- [Auxiliary Models](#auxiliary-models)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## How Hermes Uses LLMs

Hermes Agent routes every user message and every tool result through a language model. Unlike a chatbot where the model just generates text, Hermes's model must:

1. **Understand the task** — parse natural language instructions into a plan
2. **Choose the right tool** — decide whether to use terminal, browser, file system, or web search
3. **Format tool calls correctly** — produce valid JSON that matches the tool's schema
4. **Interpret tool results** — read terminal output, file contents, web page data, and decide next steps
5. **Know when to stop** — recognize when the task is complete

This means Hermes needs a model that's **strong at instruction following, tool calling, and reasoning** — not just one that writes good prose.

Key capabilities that matter for Hermes:

| Capability | Why It Matters |
|------------|----------------|
| **Function calling / tool use** | The model must reliably output correct JSON for tool invocations |
| **Instruction following** | Hermes sends complex multi-step instructions; the model must follow them precisely |
| **Long context** | Conversations with tool calls grow fast — 32K minimum, 96K+ recommended |
| **Code understanding** | Many tools operate on code; the model needs strong programming skills |
| **Planning** | Multi-step tasks require breaking goals into subtasks |

---

## Local vs Cloud: Making the Right Choice

Running Hermes with a local model means the LLM runs on your own hardware. With a cloud model, you send requests to an API.

| Factor | Local Models | Cloud Models |
|--------|-------------|--------------|
| **Privacy** | Complete — data stays on your machine | Data sent to provider's servers |
| **Cost** | Free after hardware (electricity ~$0.10-0.50/day) | Pay-per-token: $0.50-$20/day depending on usage |
| **Latency** | 10-50 tokens/sec (GPU-dependent) | 50-200 tokens/sec (consistent) |
| **Offline use** | Yes | No (requires internet) |
| **Model quality** | Very good at 27B+ params | State-of-the-art (frontier models) |
| **Context length** | 32K-128K (depending on model/quant) | 128K-1M (provider-dependent) |
| **Setup effort** | Install llama.cpp/Ollama/LM Studio, download models | Paste API key |
| **Reliability** | Your hardware, your uptime | Provider's infrastructure (99.9%+ uptime) |

**The hybrid approach (recommended):** Many power users run a local model for routine tasks (file management, simple coding, cron jobs) and fall back to a cloud model for complex work (multi-file refactors, research synthesis, production deployments). Hermes supports this natively — you can switch models mid-session with `/model`.

---

## Local Model Recommendations by Hardware Tier

All recommendations include the recommended quantization format. GGUF is the standard format for llama.cpp, Ollama, and LM Studio. The Q4_K_M quant offers the best speed/quality tradeoff for most models.

### 8GB VRAM or Less

If you have an entry-level GPU (GTX 1060, RTX 3050), integrated graphics, or a base Apple Silicon Mac (M1/M2/M3 8GB), you can still run capable models at lower quantizations.

**Best overall:** **Qwen2.5-Coder-7B-Instruct** (Q4_K_M, ~4.5GB)
- Excellent instruction following and tool calling
- Strong coding capability across Python, JavaScript, TypeScript, and shell
- 32K native context window

**Best for speed:** **Llama-3.2-3B-Instruct** (Q4_K_M, ~2GB)
- Very fast on any hardware
- Surprisingly capable for simple tasks
- Good for quick terminal commands and file operations

**Best Nous-tuned:** **Hermes-3-Llama-3.2-3B** (Q4_K_M, ~2GB)
- Specifically fine-tuned for agent/tool-use behavior
- Nous Research's own model — tight integration with Hermes
- Good for beginners learning the agent workflow

**Setup for 8GB:**

```bash
# With Ollama
ollama pull qwen2.5-coder:7b-instruct-q4_K_M

# Then configure Hermes:
hermes config set model.default "qwen2.5-coder:7b-instruct-q4_K_M"
hermes config set model.provider "ollama"
```

### 16GB VRAM

This is the sweet spot for Hermes. GPUs like RTX 4060 Ti 16GB, RTX 4070, or Apple M1/M2 Pro with 16GB unified memory can run 12-14B models comfortably.

**Best overall:** **Qwen2.5-Coder-14B-Instruct** (Q4_K_M, ~9GB)
- Significantly stronger than the 7B version
- Handles multi-file refactoring confidently
- Good reasoning for debugging and troubleshooting

**Best for general tasks:** **Mistral-Nemo-12B-Instruct** (Q4_K_M, ~7.5GB)
- Fast inference, strong reasoning
- 128K context window (excellent for long sessions)
- Good multi-turn instruction following

**Best Nous-tuned:** **Hermes-3-Llama-3.1-8B** (Q4_K_M, ~5GB)
- Space for larger context with the 8B parameter count
- Strong tool-calling performance
- Good option if you want room for auxiliary models

**Setup:**

```bash
# With LM Studio: download the model in the GUI, then:
hermes config set model.default "qwen2.5-coder-14b-instruct"
hermes config set model.provider "lmstudio"
```

### 24GB VRAM

RTX 3090, RTX 4090, M2/M3 Max with 32GB+, or M3 Ultra. This tier can run 27B-35B models — the point where local models become genuinely competitive with cloud APIs for agent tasks.

**Best overall:** **Qwen3.6-27B-Claude-4.6-Instruct** (Q4_K_M, ~17GB)
- Currently the strongest open-weight model for agent tasks
- Excellent instruction following, code generation, and reasoning
- Handles complex multi-step workflows reliably
- 96K+ effective context window

**Best for long context:** **Command-R-Plus** (Q4_K_M, ~16GB)
- 128K native context — great for long sessions
- Strong RAG and retrieval capabilities
- Good for research and analysis tasks

**Alternative:** **Llama-3.1-Nemotron-51B** (IQ3_XXS, ~22GB)
- Frontier-level reasoning at heavy quantization
- Better planning and analysis than 27B models
- Tradeoff: slower inference at heavy quant

**Setup:**

```bash
# In LM Studio's config for Hermes:
hermes config set model.default "qwen3.6-27b-claude-4.6-instruct"
hermes config set model.provider "lmstudio"
hermes config set model.context_length 98304
```

### 48GB+ / Multi-GPU

RTX 5090 32GB, dual RTX 3090s, Mac Studio Ultra 64GB+. This tier runs 70B+ models, achieving near-frontier performance entirely locally.

**Best overall:** **Llama-3.3-70B-Instruct** (Q4_K_M, ~40GB)
- Frontier-level reasoning and instruction following
- Excellent for complex multi-file development tasks
- Strong planning for multi-step automation

**Best for parallel tasks:** **Mixtral-8x22B-Instruct** (Q4_K_M, ~44GB)
- MoE architecture: fast inference for its size
- Strong multi-tool coordination
- Good at handling multiple simultaneous instructions

**Alternative:** **Qwen3.6-27B** (Q6_K or Q8_0, ~20-25GB)
- Higher quality quantization of the 27B sweet spot
- If 70B models are too slow, this gives you the best 27B experience

---

## Cloud Model Recommendations

If you prefer cloud models or want a fallback for complex tasks, here are the best options for Hermes.

### DeepSeek V4 Pro

**Best value cloud model.** Extremely strong at coding and reasoning at a fraction of Anthropic/OpenAI prices.

- Provider: DeepSeek
- Cost: ~$0.50-2.00/day for typical Hermes use
- Context: 128K
- Setup: Get an API key at [platform.deepseek.com](https://platform.deepseek.com)

```bash
hermes config set model.default "deepseek-v4-pro"
hermes config set model.provider "deepseek"
# Add DEEPSEEK_API_KEY to ~/.hermes/.env
```

### Claude Sonnet 4 (Anthropic)

**Best overall cloud model for Hermes.** Claude models are known for excellent instruction following and tool use — exactly what Hermes needs.

- Provider: Anthropic
- Cost: ~$2-10/day for typical Hermes use
- Context: 200K
- Setup: Get an API key at [console.anthropic.com](https://console.anthropic.com)

```bash
hermes config set model.default "claude-sonnet-4-20250514"
hermes config set model.provider "anthropic"
# Add ANTHROPIC_API_KEY to ~/.hermes/.env
```

### GPT-4o (OpenAI)

**Strong all-rounder.** Great for tasks that require broad knowledge and nuanced understanding.

- Provider: OpenAI
- Cost: ~$2-8/day for typical Hermes use
- Context: 128K
- Setup: Get an API key at [platform.openai.com](https://platform.openai.com)

```bash
hermes config set model.default "gpt-4o"
hermes config set model.provider "openai"
# Add OPENAI_API_KEY to ~/.hermes/.env
```

### OpenRouter

**One API key, every model.** The most flexible option — switch between providers without changing configs.

- Provider: OpenRouter
- Cost: Varies by model, usually +5% above direct
- Context: Model-dependent
- Setup: Get a key at [openrouter.ai](https://openrouter.ai)

```bash
hermes config set model.default "anthropic/claude-sonnet-4"
hermes config set model.provider "openrouter"
# Add OPENROUTER_API_KEY to ~/.hermes/.env
```

---

## Provider Setup Guide

Hermes supports 20+ providers. Here's how to configure the most common ones.

### LM Studio (Local)

Most popular local option. Runs models with a GUI and exposes an OpenAI-compatible API.

```bash
# 1. Download LM Studio from lmstudio.ai
# 2. Load a model in the GUI
# 3. Start the local server (port 1234 by default)

# 4. Configure Hermes:
hermes config set model.provider "custom:lmstudio"
hermes config set model.default "qwen2.5-coder-14b-instruct"
```

In `~/.hermes/config.yaml`, add or update:

```yaml
providers:
  custom:lmstudio:
    base_url: "http://127.0.0.1:1234/v1"
    api_key: "lm-studio"
    default_model: "qwen2.5-coder-14b-instruct"
```

### Ollama (Local)

Lightweight, CLI-focused local model runner.

```bash
# 1. Install: brew install ollama (macOS) or from ollama.com
# 2. Pull a model: ollama pull qwen2.5-coder:14b
# 3. Verify: ollama list

# 4. Configure Hermes:
hermes config set model.provider "ollama"
hermes config set model.default "qwen2.5-coder:14b"
```

### llama.cpp (Local)

For users who want maximum control. Build from source or use the pre-built server.

```bash
# 1. Download a GGUF from Hugging Face
# 2. Start the server:
./llama-server -m qwen2.5-coder-14b-q4_k_m.gguf --port 8080

# 3. Configure Hermes:
hermes config set model.provider "custom:llamacpp"
```

In config.yaml:

```yaml
providers:
  custom:llamacpp:
    base_url: "http://127.0.0.1:8080/v1"
    api_key: "not-needed"
```

### Anthropic / OpenAI / DeepSeek (Cloud)

All follow the same pattern — set the provider and add the API key:

```bash
hermes config set model.provider "anthropic"
echo "ANTHROPIC_API_KEY=sk-ant-..." >> ~/.hermes/.env

# Or with the auth manager:
hermes auth add anthropic
```

For the full list of supported providers (20+ including xAI/Grok, Google Gemini, Hugging Face, Kimi, and more), see the [official provider docs](https://hermes-agent.nousresearch.com/docs/integrations/providers).

---

## How to Switch Models in Hermes

### Interactive switch (recommended):

```bash
hermes model
```

Opens a picker with all configured providers and models. Select and confirm — applies immediately for your next session.

### Command-line switch:

```bash
hermes config set model.default "claude-sonnet-4-20250514"
hermes config set model.provider "anthropic"
```

### In-session switch:

```
/model
```

This slash command opens the picker inside an active session. The change takes effect on your next message.

### Per-session override:

```bash
hermes --model "deepseek-v4-pro" --provider "deepseek"
```

### Switching just the auxiliary model:

You can set a different model for auxiliary tasks (vision, compression, web extraction) without changing your main model:

```yaml
auxiliary:
  vision:
    provider: "custom:lmstudio"
    model: "qwen2.5-vl-7b-instruct"
  compression:
    provider: "custom:lmstudio"
    model: "qwen2.5-coder-7b-instruct"
```

See the [official auxiliary model docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/auxiliary-models) for full details.

---

## What Makes a Good Hermes Model?

Not every LLM works well as an agent. Here's what to look for:

### Must-Haves

1. **Tool calling / function calling support** — The model must be trained to output function calls in the expected format. Most modern instruct models support this, but some older or base models do not.

2. **Instruction following** — Agent workflows involve multi-step instructions. The model must follow system prompts and multi-part user requests reliably.

3. **32K+ context** — Conversations with tool results grow quickly. A model with less than 32K context will hit the limit after only a few tool calls.

### Nice-to-Haves

4. **Code generation quality** — Most Hermes tasks involve writing or editing code, shell scripts, or config files. Strong coding = strong Hermes performance.

5. **Structured output reliability** — The model must consistently output valid JSON for tool calls. Even one malformed function call breaks the agent loop.

6. **Planning ability** — Complex tasks require the model to break goals into subtasks, choose the right order, and adapt when a step fails.

### Red Flags

- **Base models** (not instruction-tuned) — won't follow Hermes's system prompt format
- **Models without function calling in their training data** — will hallucinate tool calls or ignore them
- **Models under 7B parameters** — rarely reliable enough for multi-step tool use
- **Heavily censored/refusal-trained models** — may refuse legitimate system commands like `rm` or `curl`

---

## Auxiliary Models

Hermes can use a separate, smaller model for auxiliary tasks — saving your main model's context and reducing costs:

| Task | What It Does | Recommended Model |
|------|-------------|-------------------|
| **Vision** | Analyze screenshots and images | Qwen2.5-VL-7B, LLaVA |
| **Compression** | Summarize conversation history | Qwen2.5-Coder-7B, Llama-3.2-3B |
| **Web extraction** | Parse and structure web content | Any capable 7B+ instruct model |
| **Title generation** | Name sessions concisely | Small, fast model (3B is fine) |
| **Skills hub search** | Search and recommend skills | Any capable 7B+ model |

**Why use an auxiliary model?**

- **Cost savings:** Use a free local 7B for summarization instead of burning cloud tokens
- **Speed:** A local 3B model summarizes faster than a cloud roundtrip
- **Context preservation:** Offload vision tasks so they don't consume your main model's context window

Set up auxiliary routing:

```yaml
auxiliary:
  vision:
    provider: "custom:lmstudio"
    model: "qwen2.5-vl-7b-instruct"
  compression:
    provider: "custom:lmstudio"
    model: "qwen2.5-coder-7b-instruct"
```

---

## FAQ

### What's the best model for Hermes Agent?

There's no single best — it depends on your hardware, budget, and tasks. For most users: Qwen3.6-27B locally (if you have 24GB+ VRAM) or Claude Sonnet 4 via API (if you prefer cloud). The sweet spot for value is DeepSeek V4 Pro (cloud) or Qwen2.5-Coder-14B (local).

### Can I run Hermes Agent with a free model?

Yes. Hermes-3-Llama-3.2-3B is completely free and runs on almost any hardware. For better quality at zero cost, Qwen2.5-Coder-7B-Instruct is excellent and free (open-weight). Nous Portal also offers a free tier for Hermes-3-405B.

### Does Hermes work with Ollama?

Yes. Set your provider to `ollama` and model to the Ollama model name (e.g., `qwen2.5-coder:14b`). Hermes auto-detects Ollama's context length and configuration.

### How much VRAM do I need for a good local model?

8GB is the minimum for a 7B model. 16GB gets you 12-14B models which are a noticeable step up. 24GB runs 27B models that are genuinely competitive with cloud APIs. 48GB+ runs 70B models at frontier quality.

### Why does my local model keep running out of context?

Hermes sessions grow fast — each tool call adds hundreds of tokens. Enable compression in config (`compression.enabled: true`) and set a reasonable `threshold` (0.85) and `target_ratio` (0.70). Also consider using a model with a larger native context window.

### Can I use the same model for both main tasks and auxiliary tasks?

Yes, but it's not recommended — auxiliary tasks (especially vision) will consume your main context. A 7B auxiliary model for summarization and vision is cheap to run alongside a larger main model.

### What's the difference between Q4_K_M and other quants?

GGUF quants trade size for quality. Q4_K_M is the recommended sweet spot: ~4.5 bits per weight, good quality, good speed. Q5_K_M is higher quality but slower. Q2_K is very small but noticeably degraded. For agent use, don't go below Q4_K_M.

### Can I use GPT-4o with Hermes?

Yes. Set `model.provider` to `openai` and `model.default` to `gpt-4o`. Add your `OPENAI_API_KEY` to `~/.hermes/.env`.

### Will my local model work offline?

Yes — Hermes + a local model via LM Studio, Ollama, or llama.cpp works completely offline. Web search and browser tools need internet, but the core agent does not.

### How do I add a custom model endpoint?

Use the `custom:<name>` provider pattern. Define it in `config.yaml` under `providers` with a `base_url` and `api_key`, then set `model.provider` to that name. This works for any OpenAI-compatible endpoint (vLLM, text-generation-webui, llama.cpp server, etc.).

---

## Next Steps

**Now that you've chosen a model:**

1. **[Skills Guide →](wiki/skills-guide)** Load and write skills to give Hermes domain expertise
2. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule tasks that run on your chosen model 24/7
3. **[Profiles Guide →](wiki/profiles-guide)** Create separate profiles with different models for different contexts

**Also see:** [Start Here](wiki/start-here) · [Windows Install](wiki/windows-install) · [Multi-Machine Setup](wiki/multi-machine-setup) · [Official Provider Docs](https://hermes-agent.nousresearch.com/docs/integrations/providers)
