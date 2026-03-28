#!/usr/bin/env python3
"""
GitHub Radar - GitHub 趋势分析 CLI 工具
用法: python3 github_radar.py [--daily|--weekly|--new] [--top 10] [--lang python]
"""
import json
import sys
import argparse
from datetime import datetime, timedelta, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError

def fetch_json(url):
    req = Request(url, headers={"User-Agent": "GitHubRadar/1.0"})
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except URLError as e:
        print(f"❌ 请求失败: {e}")
        sys.exit(1)

def trending_repos(days=1, top=10, lang=None, only_new=False):
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    query = f"created:>{since}" if only_new else f"pushed:>{since}+stars:>100"
    if lang:
        query += f"+language:{lang}"
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={top}"
    data = fetch_json(url)
    return data.get("items", [])[:top]

def format_repo(r, idx, show_new=False):
    desc = r.get("description") or "无描述"
    if len(desc) > 100:
        desc = desc[:100] + "..."
    stars = r["stargazers_count"]
    forks = r.get("forks_count", 0)
    lang = r.get("language") or "N/A"
    topics = ", ".join(r.get("topics", [])[:4]) or "无"
    license_name = (r.get("license") or {}).get("spdx_id") or "N/A"
    created = r.get("created_at", "")[:10]

    lines = [
        f"{'🆕 ' if show_new else ''}{idx}. {r['full_name']}",
        f"   ⭐{stars} | 🍴{forks} | 💻{lang} | 📜{license_name}",
        f"   📝 {desc}",
        f"   🏷️ {topics}",
        f"   🔗 {r['html_url']}",
    ]
    if show_new:
        lines.insert(2, f"   📅 创建于 {created}")
    return "\n".join(lines)

def run(mode="daily", top=10, lang=None):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"📊 GitHub Radar — {today}\n")

    if mode in ("daily", "both"):
        print("🔥 过去24小时 Stars 增长最快 Top", top)
        print("=" * 50)
        repos = trending_repos(days=1, top=top, lang=lang)
        for i, r in enumerate(repos, 1):
            print(format_repo(r, i))
            print()

    if mode in ("new", "both"):
        print("🆕 过去24小时新建项目 Top", top)
        print("=" * 50)
        repos = trending_repos(days=1, top=top, lang=lang, only_new=True)
        for i, r in enumerate(repos, 1):
            print(format_repo(r, i, show_new=True))
            print()

    if mode == "weekly":
        print("📈 过去7天 Stars 增长最快 Top", top)
        print("=" * 50)
        repos = trending_repos(days=7, top=top, lang=lang)
        for i, r in enumerate(repos, 1):
            print(format_repo(r, i))
            print()

def main():
    parser = argparse.ArgumentParser(description="GitHub Radar - 趋势分析工具")
    parser.add_argument("--daily", action="store_true", help="过去24小时热门")
    parser.add_argument("--weekly", action="store_true", help="过去7天热门")
    parser.add_argument("--new", action="store_true", help="新建项目热门")
    parser.add_argument("--top", type=int, default=10, help="显示数量 (默认10)")
    parser.add_argument("--lang", type=str, default=None, help="按语言过滤 (python, javascript, etc.)")
    args = parser.parse_args()

    if args.weekly:
        mode = "weekly"
    elif args.new:
        mode = "new"
    elif args.daily:
        mode = "daily"
    else:
        mode = "both"

    run(mode=mode, top=args.top, lang=args.lang)

if __name__ == "__main__":
    main()
