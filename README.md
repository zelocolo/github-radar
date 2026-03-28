# 🛰️ GitHub Radar

> Zero-dependency GitHub trending analysis CLI. One file. No install. Pure Python.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://python.org)

## What is this?

A single Python script that shows you what's trending on GitHub right now. No API keys, no dependencies, no BS.

```
$ python3 github_radar.py --daily --top 3

📊 GitHub Radar — 2026-03-28

🔥 过去24小时 Stars 增长最快 Top 3
1. openclaw/openclaw ⭐338672 | 🍴66582 | 💻TypeScript
   Your own personal AI assistant. 🦞
   https://github.com/openclaw/openclaw

2. torvalds/linux ⭐225354 | 🍴61241 | 💻C
   Linux kernel source tree
   https://github.com/torvalds/linux
```

## Quick Start

```bash
git clone https://github.com/zelocolo/github-radar.git
cd github-radar
python3 github_radar.py
```

That's it. No `pip install`. No config files. Just run it.

## Usage

```bash
# Daily trending (default)
python3 github_radar.py --daily

# Weekly trending
python3 github_radar.py --weekly

# New projects only
python3 github_radar.py --new

# Filter by language
python3 github_radar.py --lang python --top 5

# Combine options
python3 github_radar.py --daily --top 10 --lang rust
```

## Why?

- 🚀 **Zero dependencies** — Just Python 3.8+ and internet
- ⚡ **Fast** — Results in seconds
- 🔧 **Integrable** — Perfect for cron jobs, CI/CD, chatbots, newsletters
- 📦 **Single file** — 4KB, copy anywhere

## Use Cases

- 📰 **Daily tech newsletter** — Feed it into your newsletter pipeline
- 🤖 **Chat bot integration** — QQ, Telegram, Discord bots
- 📊 **Trend analysis** — Track what's hot over time
- 🔍 **Project discovery** — Find your next open source contribution

## Integrations

### Cron job (daily digest)

```bash
0 8 * * * python3 /path/to/github_radar.py --daily --top 10 >> /var/log/github-radar.log
```

### Pipe to file

```bash
python3 github_radar.py --daily > today-trending.md
```

## License

MIT — Do whatever you want with it.
