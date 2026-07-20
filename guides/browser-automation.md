# Hermes Agent Browser Automation and Computer Use: Setup, Use Cases, and Troubleshooting

> **r/hermesagent** — 75,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Complete guide to Hermes Agent browser automation and computer use. Covers cua-driver setup, Chrome CDP connection, background vs foreground mode, known app compatibility, permissions, and real automation examples.

---

## Table of Contents

- [Browser Automation vs. Computer Use](#browser-automation-vs-computer-use)
- [Browser Automation](#browser-automation)
  - [Connecting to Chrome/Brave via CDP](#connecting-to-chromebrave-via-cdp)
  - [Browser Tools Reference](#browser-tools-reference)
  - [Real Browser Automation Examples](#real-browser-automation-examples)
- [Computer Use (Desktop Automation)](#computer-use-desktop-automation)
  - [How CUA-Driver Works](#how-cua-driver-works)
  - [Installing and Configuring CUA-Driver](#installing-and-configuring-cua-driver)
  - [Background Mode vs. Foreground Mode](#background-mode-vs-foreground-mode)
  - [Real Computer Use Examples](#real-computer-use-examples)
- [Known App Compatibility](#known-app-compatibility)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Next Steps](#next-steps)

---

## Browser Automation vs. Computer Use

Hermes Agent has two distinct systems for interacting with graphical interfaces:

| Feature | Browser Automation | Computer Use (CUA) |
|---------|-------------------|---------------------|
| **What it controls** | Web browsers (Chrome, Brave, Chromium, Edge) | Any desktop app (macOS, Windows, Linux) |
| **How it works** | Chrome DevTools Protocol (CDP) | Accessibility tree + screenshot analysis |
| **Granularity** | Individual DOM elements | Any visible UI element |
| **Setup** | `/browser connect` or CDP URL | Install cua-driver |
| **Best for** | Web tasks: forms, scraping, web apps | Desktop tasks: file dialogs, app automation, non-web UIs |
| **Requires** | Running browser with remote debugging | cua-driver installed + accessibility permissions |

They're complementary: use browser automation for web-specific tasks, and computer use for everything else (or for web pages that CDP can't reach, like Electron apps with locked-down DevTools).

---

## Browser Automation

### Connecting to Chrome/Brave via CDP

Hermes connects to any Chromium-based browser that has remote debugging enabled.

#### Method 1: In-Session `/browser` Command (Easiest)

Inside a Hermes session, type:

```
/browser
```

This opens an interactive dialog to connect to a running browser instance.

#### Method 2: Launch Browser with Remote Debugging

**macOS:**

```bash
# Chrome
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-hermes &

# Brave
/Applications/Brave\ Browser.app/Contents/MacOS/Brave\ Browser \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/brave-hermes &
```

**Windows:**

```powershell
# Chrome
"C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --remote-debugging-port=9222 `
  --user-data-dir=C:\Temp\chrome-hermes

# Brave
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" `
  --remote-debugging-port=9222 `
  --user-data-dir=C:\Temp\brave-hermes
```

**Linux:**

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-hermes &
```

#### Method 3: Persistent CDP Configuration

Set a permanent CDP URL in `~/.hermes/config.yaml`:

```yaml
browser:
  cdp_url: "http://127.0.0.1:9222"
```

Now Hermes auto-connects on startup.

#### Verify the Connection

```bash
curl http://127.0.0.1:9222/json/version
```

Should return JSON with browser info.

### Browser Tools Reference

Once connected, Hermes has these browser tools:

| Tool | What It Does |
|------|-------------|
| `browser_navigate` | Navigate to a URL |
| `browser_snapshot` | Get text-based page structure with clickable element IDs |
| `browser_click` | Click an element by ref ID |
| `browser_type` | Type into an input field |
| `browser_press` | Press keyboard keys (Enter, Tab, Escape) |
| `browser_scroll` | Scroll up or down |
| `browser_console` | Execute JavaScript or read console errors |
| `browser_vision` | Take and analyze a screenshot |
| `browser_get_images` | List all images with URLs and alt text |
| `browser_dialog` | Respond to JavaScript dialogs (alert, confirm, prompt) |
| `browser_cdp` | Send raw Chrome DevTools Protocol commands |

### Real Browser Automation Examples

#### 1. Fill Out a Web Form

```
Navigate to https://example.com/contact, find the contact form, fill it with:
- Name: John Smith
- Email: john@example.com
- Message: I'm interested in your API services.
Take a screenshot before submitting so I can verify.
```

Hermes navigates, snapshots the page, finds the form fields by their ref IDs, types into each, and shows you the result.

#### 2. Extract Data from Multiple Pages

```
Go to https://news.ycombinator.com. Extract the top 10 stories: title, URL, points, and comment count. Save the results to ~/data/hn-top-10.json.
```

#### 3. Check if a Website Changed

```
Navigate to https://example.com/pricing. Capture a snapshot of the pricing table. Compare it against the saved version in ~/monitors/pricing-snapshot.txt. If anything changed, list the differences and update the snapshot.
```

#### 4. Log into a Site and Download a Report

```
Go to https://analytics.example.com. If you see a login form, I'll provide credentials. Once logged in, navigate to Reports → Monthly Summary. Click the "Export as CSV" button. Once the download completes, move the file to ~/reports/.
```

**Note:** Hermes will ask for confirmation before entering credentials on a login page.

#### 5. Monitor a Dynamic Web App

```
Navigate to my dashboard at https://app.example.com/dashboard. Wait for the page to fully load (check that the loading spinner disappears). Extract the numbers from the "Today's Stats" card. Save to ~/dashboards/stats-$(date +%Y-%m-%d).csv.
```

---

## Computer Use (Desktop Automation)

### How CUA-Driver Works

CUA-driver (Computer Use Automation driver) controls your desktop by:

1. **Capturing screenshots** of any window (even hidden or minimized ones)
2. **Reading the accessibility tree** to identify UI elements (buttons, text fields, menus)
3. **Sending input** (clicks, keystrokes, scrolls) to the target window

It works in **background mode** by default — your cursor doesn't move, your focus doesn't change. You keep working while Hermes drives another window.

### Installing and Configuring CUA-Driver

```bash
# Install cua-driver
hermes setup tools
# Select "Computer Use" from the tool list

# Verify installation
hermes doctor
```

**macOS permissions required:**

- **Accessibility:** System Settings → Privacy & Security → Accessibility → enable Hermes (or Terminal)
- **Screen Recording:** System Settings → Privacy & Security → Screen Recording → enable Hermes (or Terminal)

Without these permissions, CUA-driver can't see or interact with windows.

**Windows permissions:**

- CUA-driver uses UI Automation (UIA), which doesn't require explicit permission grants on Windows

**Linux permissions:**

- CUA-driver uses AT-SPI for accessibility. Install `at-spi2-core` if not present.
- For X11: no extra permissions needed
- For Wayland: some compositors restrict accessibility access

### The Computer Use Tool

In Hermes, the `computer_use` tool provides these actions:

| Action | What It Does |
|--------|-------------|
| `capture` | Take a screenshot with numbered element overlays (SOM mode) |
| `click` | Click on an element by index or pixel coordinate |
| `double_click` | Double-click an element |
| `right_click` | Right-click (context menu) |
| `drag` | Drag from one element to another |
| `scroll` | Scroll up, down, left, or right |
| `type` | Type text into the focused element |
| `key` | Press key combinations (cmd+s, ctrl+alt+t) |
| `set_value` | Set a value on a select/popup element |
| `wait` | Wait N seconds |
| `list_apps` | List running applications |
| `list_windows` | List windows for a specific app |
| `focus_app` | Focus a specific app (without raising it) |

### Background Mode vs. Foreground Mode

**Background mode (default):** Input is routed to the target window without stealing focus. You keep working; Hermes drives in the background. This is the co-work model.

**Foreground mode:** The target window briefly comes to the front, input is sent, then it returns to the background. Use only when background mode fails (CUA-driver reports `escalation.recommended: 'foreground'`).

#### When to Escalate

Only escalate to foreground when CUA-driver explicitly says to. Don't predict it based on the app type. Common triggers for foreground:

- Electron/Chromium consent dialogs
- DirectInput games
- Raw-input canvases
- Some system permission prompts

### Real Computer Use Examples

#### 1. File Management in Finder/Explorer

```
Using computer use, open Finder, navigate to ~/Downloads, find all .zip files older than 7 days, and move them to the Trash.
```

#### 2. App Configuration

```
Open System Settings on my Mac. Navigate to Displays. Take a screenshot so I can see my current display configuration.
```

#### 3. Form Filling in a Non-Web App

```
Open the "Expense Report" application. Fill in today's date, select category "Travel," enter amount $45.00, and attach the receipt file from ~/receipts/hotel.pdf. Take a screenshot before saving.
```

#### 4. Data Entry Across Multiple Windows

```
For each row in ~/data/customers.csv, open our CRM app (AcmeCRM), search for the customer by name, update their status to "Contacted," and log the date. Process the first 5 rows and show me the results.
```

#### 5. Monitoring a Desktop Dashboard

```
Every hour, capture a screenshot of the Grafana dashboard open in Firefox. Extract the current values from the CPU, Memory, and Request Rate panels. Log them to ~/monitors/grafana-log.csv.
```

---

## Known App Compatibility

### Browser Automation (CDP)

| Browser | Compatibility | Notes |
|---------|--------------|-------|
| Chrome | Full | Most tested |
| Brave | Full | Same engine as Chrome |
| Chromium | Full | Open-source base |
| Edge | Full | Chromium-based |
| Arc | Partial | CDP sometimes disabled |
| Firefox | No CDP | Use computer_use instead |
| Safari | No CDP | Use computer_use instead |

### Computer Use (CUA-Driver)

| App Type | Background Mode | Foreground Mode | Notes |
|----------|----------------|-----------------|-------|
| Native macOS apps | Excellent | Always works | Full accessibility support |
| Native Windows apps | Good | Always works | UIA support varies by app |
| Electron apps (VS Code, Obsidian, Discord) | Good | Always works | May need foreground for dialogs |
| GTK apps (Linux) | Good | Always works | AT-SPI backend |
| Qt apps (Linux) | Fair | Always works | Accessibility depends on build flags |
| Java apps | Fair | Always works | Accessibility bridge required |
| Web browsers (for non-CDP) | Good | Always works | Use CDP when possible |
| System dialogs (file picker, print) | Mixed | Always works | Often require foreground |
| Games (DirectX, Vulkan) | Not supported | Mixed | Use for launchers/config, not gameplay |
| Terminal apps | N/A | N/A | Use the terminal tool instead |

---

## Troubleshooting

### Browser Automation

**"No CDP endpoint available"**

- Is Chrome/Brave running with `--remote-debugging-port`?
- Check the port: `curl http://127.0.0.1:9222/json/version`
- If connecting to a remote browser, is the firewall open?

**Browser tools not appearing**

Enable the browser toolset:

```bash
hermes tools enable browser
```

Then restart your session (`/reset`).

**"Target closed" or "Page crashed"**

The browser tab was closed or the browser crashed. Restart the browser with the debugging flag and re-connect.

**Can't interact with a specific element**

- Try `browser_snapshot(full=true)` to see the full page structure
- Some elements are inside iframes — check the snapshot for `frame_tree` info
- Use `browser_cdp` with `Runtime.evaluate` as a fallback

### Computer Use

**"cua-driver not installed"**

```bash
hermes setup tools
# Enable Computer Use
hermes doctor --fix
```

**Empty captures (black screen)**

- On macOS: check Screen Recording permission (System Settings → Privacy)
- On macOS: check Accessibility permission
- On Linux: ensure `at-spi2-core` is installed

**Clicks not landing**

1. Try with `delivery_mode='foreground'`
2. If that doesn't work, capture with `mode='ax'` (accessibility tree only) to check element visibility
3. Some apps don't expose elements properly — use pixel coordinates as last resort

**"Background unavailable" error**

The app doesn't support background input. Escalate to foreground: `delivery_mode='foreground'`.

**CUA-driver stops working after macOS update**

macOS updates can reset accessibility permissions. Re-grant them:

```bash
# Reset and re-grant:
tccutil reset Accessibility com.apple.Terminal
# Then trigger accessibility prompt again by using computer_use
```

---

## FAQ

### Do I need to keep Chrome open for browser automation?

Yes. Hermes connects to a running browser instance via CDP. The browser must stay open while Hermes is working with it.

### Can Hermes use my existing browser with all my logins?

Yes — connect to your regular Chrome/Brave profile (not a temp profile) and Hermes has access to your logged-in sessions. This is useful for automating tasks on authenticated sites.

### Is computer use safe? Can Hermes click things I don't want it to?

By default, Hermes asks for confirmation before potentially destructive actions. You can also restrict which apps Hermes can control via `app='Safari'` in computer_use calls. Hermes never clicks password prompts or payment UI without explicit permission.

### Can I use computer use on a headless server?

No — computer use requires a graphical desktop environment. For servers, use terminal tools, browser automation (with headless Chrome), and API calls instead.

### How do I stop Hermes from accidentally clicking my main workspace?

Use `app=` to scope computer_use to a specific application. Hermes only captures and interacts with that app's windows.

### Does browser automation work with MFA/2FA pages?

Hermes can navigate to MFA pages and you can enter the code yourself, but Hermes won't bypass MFA. If you have a TOTP secret, you could theoretically write a script that generates codes — but this is a security risk and not recommended.

### Can I automate mobile apps with computer use?

Not directly. Computer use controls desktop OS UIs. For mobile, use the Telegram gateway to control Hermes from your phone, or use platform-specific automation (Shortcuts on iOS, Tasker on Android).

### What's the difference between browser_click and computer_use click?

`browser_click` works at the DOM level via CDP — it's fast, reliable, and works on hidden elements. `computer_use` click works at the OS level via accessibility — it's for non-web apps and browser pages where CDP isn't available (Safari, Firefox).

### Can I run browser automation inside a Docker container?

Yes — use a headless Chromium container with `--remote-debugging-port`. Point Hermes's `browser.cdp_url` at the container's CDP port.

### How do I take screenshots of specific elements?

Use `browser_vision` with the `annotate=true` option to overlay numbered labels on all interactive elements. Then use `browser_snapshot` to see the text-based structure. The combination lets you verify visually what the text tree describes.

### Can I chain browser and computer use together?

Yes. Common pattern: use browser automation to navigate a web app and fill forms, then use computer_use to interact with the file save dialog that the browser triggers. They're separate tools but work from the same Hermes session.

### Does browser automation respect my Chrome extensions?

Yes — Hermes connects to your running browser, including all active extensions. This means ad blockers, password managers, and developer tools are all active during automation. This can be helpful (password manager fills forms) or problematic (ad blocker hides elements). Adjust extensions as needed before automation sessions.

### Can I use browser automation to scrape sites that require JavaScript rendering?

Yes — this is one of its main advantages over simple `web_extract`. Hermes's browser automation uses a real Chrome instance, so JavaScript-heavy sites (React, Vue, Angular SPAs) render fully. Use `browser_navigate` + `browser_snapshot` to extract the rendered content.

### What's the memory footprint of a browser automation session?

A Chrome instance with remote debugging enabled uses ~200-500MB RAM per tab. Hermes's browser tools use negligible additional memory. If you're running low on RAM, close unused browser tabs before starting automation.

### Can Hermes handle CAPTCHAs?

Generally no — CAPTCHAs are designed to block automated tools. Hermes can alert you when it encounters a CAPTCHA so you can solve it manually, then resume automation. Some community members have had success with computer_use for visual CAPTCHAs (using screenshot analysis), but this is unreliable and not recommended for production automation.

### How does CUA compare to AppleScript/Automator on macOS?

CUA-driver works across macOS, Windows, and Linux with the same interface. AppleScript is macOS-only. CUA uses accessibility APIs which work with most modern apps; AppleScript has deeper integration with Apple-native apps but poor support for cross-platform and Electron apps. For Hermes, CUA is the right default; fall back to AppleScript via terminal for Mac-specific tasks.

### Can multiple browser windows/tabs be used simultaneously?

Yes. Use `browser_cdp` with `Target.getTargets` to list all open tabs, then target specific tabs by `target_id`. This lets Hermes monitor one tab while interacting with another.

---

## Next Steps

**Automation that controls the real world:**

1. **[Cron Jobs & Automation →](wiki/cron-jobs-automation)** Schedule browser and desktop automations to run 24/7
2. **[Telegram Gateway Setup →](wiki/telegram-gateway-setup)** Trigger browser automations from your phone
3. **[Skills Guide →](wiki/skills-guide)** Package browser automation workflows as reusable skills

**Also see:** [Start Here](wiki/start-here) · [Multi-Machine Setup](wiki/multi-machine-setup) · [50 Use Cases](wiki/use-cases) · [Official Docs](https://hermes-agent.nousresearch.com/docs)
