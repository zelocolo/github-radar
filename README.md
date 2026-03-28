# 🛰️ GitHub Radar

一个轻量级的 GitHub 趋势分析 CLI 工具，零依赖，开箱即用。

## 功能

- 📊 **每日热门** — 过去 24 小时 Stars 增长最快的项目
- 📈 **每周热门** — 过去 7 天最火的项目
- 🆕 **新建项目** — 新创建的项目中最受欢迎的
- 🔍 **语言过滤** — 按编程语言筛选

## 安装

```bash
# 克隆即用，无需安装
git clone https://github.com/yourname/github-radar.git
cd github-radar
```

## 使用

```bash
# 每日热门（默认显示前10）
python3 github_radar.py

# 指定数量
python3 github_radar.py --daily --top 5

# 按语言过滤
python3 github_radar.py --lang python --top 5

# 仅新建项目
python3 github_radar.py --new --top 5

# 每周趋势
python3 github_radar.py --weekly --top 10
```

## 示例输出

```
📊 GitHub Radar — 2026-03-28

🔥 过去24小时 Stars 增长最快 Top 3
==================================================
1. openclaw/openclaw
   ⭐338672 | 🍴66582 | 💻TypeScript | 📜MIT
   📝 Your own personal AI assistant. 🦞
   🏷️ ai, assistant, crustacean, molty
   🔗 https://github.com/openclaw/openclaw
```

## 特点

- ✅ **零依赖** — 只用 Python 标准库
- ✅ **轻量** — 单文件，4KB
- ✅ **快速** — 秒级响应
- ✅ **可集成** — 适合接入 cron、CI/CD、聊天机器人

## License

MIT
