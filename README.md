# ⌨️ Keyboard Event Monitor

> **Educational Use Only** — Built as part of a Cybersecurity Internship to demonstrate OS-level keyboard event handling in Python. Designed to run only on your own device, with your own knowledge and consent.

---

## 📋 Overview

This tool demonstrates how Python can listen to operating system keyboard events using the `pynput` library. It is a core topic in cybersecurity education — understanding how keyboard event monitoring works at the code level helps security professionals identify malicious behaviour, write SIEM detection rules, and understand attack vectors in order to defend against them.

### Key design decision

This tool logs **that** a key was pressed — not **which** key. The log file records event types and timestamps only, never actual character values. This means the log contains zero sensitive data by design, even during testing.

---

## ✨ Features

- Detects and logs keyboard press and release events in real time
- Classifies events as alphanumeric or special key (Shift, Enter, Ctrl, etc.) without recording actual key values
- Timestamps every event to millisecond precision (`YYYY-MM-DD HH:MM:SS`)
- Saves all events to a local log file — nothing is transmitted over a network
- Prints every event to the terminal in real time — fully transparent operation
- Tracks and displays total events logged per session
- Press `ESC` at any time to cleanly stop the monitor

---

## 🔒 What this tool deliberately does NOT do

These are not missing features — they are deliberate design decisions:

| Property                     | This tool | A malicious keylogger |
| ---------------------------- | --------- | --------------------- |
| Logs actual key values       | ❌ No     | ✅ Yes                |
| Sends data over a network    | ❌ No     | ✅ Yes                |
| Runs at system startup       | ❌ No     | ✅ Yes                |
| Hides from the user          | ❌ No     | ✅ Yes                |
| Requires elevated privileges | ❌ No     | ✅ Often              |

Understanding these differences is precisely what makes this an educational tool — and what helps defenders detect the real thing.

---

## 🛠️ Requirements

- Python 3.8+
- `pynput` library

```bash
pip install pynput
```

> **macOS users:** Grant Terminal permission under System Preferences → Security & Privacy → Accessibility.

> **Linux users:** You may need to run with appropriate input group permissions depending on your distribution.

---

## ▶️ Usage

```bash
python task4_keylogger.py
```

**Sample terminal output:**

```
==================================================
EDUCATIONAL KEYBOARD EVENT MONITOR
==================================================
Recording events to: /home/user/project/keyboard_events.txt
Press 'ESC' to stop monitoring.
Monitor is running... Keyboard events will be recorded.

[2026-06-01 14:32:01] Keyboard press event detected
[2026-06-01 14:32:01] Keyboard release event detected
[2026-06-01 14:32:02] Keyboard press event detected
[2026-06-01 14:32:02] Keyboard release event detected
[2026-06-01 14:32:05] Stop event detected. Total events recorded: 4

Events saved to: /home/user/project/keyboard_events.txt
Total events recorded: 4
```

**Sample log file (`keyboard_events.txt`):**

```
==================================================
Session started at: 2026-06-01 14:32:00
==================================================
[2026-06-01 14:32:01] Keyboard press event detected
[2026-06-01 14:32:01] Keyboard release event detected
[2026-06-01 14:32:02] Keyboard press event detected
[2026-06-01 14:32:02] Keyboard release event detected
[2026-06-01 14:32:05] Stop event detected. Total events recorded: 4
```

---

## 📁 Project Structure

```
.
├── task4_keylogger.py       # Main program
├── .gitignore               # Prevents log files from being committed
└── README.md                # This file
```

---

## 🙈 .gitignore

This file is essential. The log file generated during testing must never be committed to a public repository.

```gitignore
keyboard_events.txt
*.log
*.txt
__pycache__/
*.pyc
.env
```

Always verify with `git status` before pushing that no log files are staged.

---

## 🧠 What I Learned

**Technical:**

- How operating systems expose keyboard input through asynchronous event listeners
- Event-driven programming — writing `on_press` and `on_release` handlers called by the OS, not by your own loop
- Using `try/except AttributeError` to distinguish `key.char` (regular keys) from `key.name` (special keys) in pynput
- Timestamped file logging with `datetime` and append-mode file I/O — a foundational skill for any security tool or SIEM integration

**Security engineering:**

- What specifically separates a legitimate monitoring tool from a malicious keylogger: network transmission, persistence, stealth, and privilege escalation
- Why security tools must be designed with data minimisation in mind — logging only what is necessary for the stated purpose
- Why `.gitignore` is a security control, not just a housekeeping step — log files from testing can contain sensitive information

---

## ⚠️ Legal & Ethical Notice

- **Only run this on your own device.**
- **Never run this on a device you do not own or have explicit written permission to monitor.**
- Keyboard monitoring software used on another person's device without consent is illegal under the Computer Fraud and Abuse Act (CFAA, USA), the Computer Misuse Act (CMA, UK), and equivalent legislation in most countries.
- This project contains no obfuscation, no network transmission, no persistence mechanism, and logs no sensitive key data — by design and by choice.

---

## 📜 License

Built as part of a Cybersecurity Internship learning exercise — 2026.
