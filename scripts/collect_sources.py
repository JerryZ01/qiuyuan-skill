#!/usr/bin/env python3
"""
球探 · 球员信息来源采集脚本
支持：YouTube/B站视频字幕提取、球员数据拉取

使用方法：
  python3 collect_sources.py <球员名> <保存目录>
  python3 collect_sources.py 梅西 ./messi_sources

注意：视频字幕需要安装 yt-dlp（pip install yt-dlp）
"""
import os, sys, re, json, subprocess
from pathlib import Path
from datetime import datetime

# ── 球员数据 API（公开数据源）─────────────────────────────
FOOTBALL_APIS = {
    # FBref 统计（公开，无需key）
    "fbref": "https://fbref.com/en/players/search?q={name}",
    # Transfermarkt 搜索
    "transfermarkt": "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={name}",
    # YouTube 搜索（需 yt-dlp）
    "youtube": "ytsearch10:{name} 球员 采访 战术分析",
    "youtube_match": "ytsearch5:{name} 全场 比赛 高光",
    # B站搜索（需安装 you-get 或 curl）
    "bilibili": "https://search.bilibili.com/all?keyword={name}+球员+采访&order=totalrank&duration=0&page=1",
}

def search_youtube(query: str, max_results: int = 5) -> list[dict]:
    """用 yt-dlp 搜索 YouTube，返回视频列表"""
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "%(id)s|%(title)s|%(duration)s|%(webpage_url)s",
             "--match-filter", f"duration>60",  # 至少1分钟
             "--", f"ytsearch{max_results}:{query}"],
            capture_output=True, text=True, timeout=30
        )
        videos = []
        for line in result.stdout.strip().split('\n'):
            if '|' not in line:
                continue
            parts = line.split('|')
            if len(parts) >= 4:
                videos.append({
                    "id": parts[0],
                    "title": parts[1],
                    "duration": parts[2],
                    "url": parts[3],
                })
        return videos
    except FileNotFoundError:
        print("⚠️  yt-dlp 未安装，执行: pip install yt-dlp")
        return []
    except Exception as e:
        print(f"❌ YouTube搜索失败: {e}")
        return []

def search_bilibili(keyword: str, max_results: int = 10) -> list[dict]:
    """搜索B站，返回视频列表"""
    try:
        import requests
        url = f"https://api.bilibili.com/all?keyword={keyword}&page=1&pagesize={max_results}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Referer": "https://www.bilibili.com",
        }
        r = requests.get("https://api.bilibili.com/x/web-interface/search/type",
                        params={"keyword": keyword, "search_type": "video", "page": 1, "order": "totalrank"},
                        headers=headers, timeout=10)
        data = r.json()
        videos = []
        for item in data.get("data", {}).get("result", []):
            if item.get("duration", "").startswith("--"):
                continue
            videos.append({
                "bvid": item.get("bvid", ""),
                "title": item.get("title", "").replace("<em class=\"keyword\">", "").replace("</em>", ""),
                "author": item.get("author", ""),
                "duration": item.get("duration", ""),
                "url": f"https://www.bilibili.com/video/{item.get('bvid', '')}",
            })
        return videos[:max_results]
    except Exception as e:
        print(f"⚠️ B站搜索失败: {e}")
        return []

def download_video_subtitle(url: str, output_dir: str) -> list[str]:
    """下载视频字幕到指定目录，返回字幕文件列表"""
    import subprocess
    result_files = []
    try:
        # 下载字幕（中文优先，然后英文，最后自动字幕）
        result = subprocess.run([
            "yt-dlp",
            "--write-subs", "--write-auto-subs",
            "--sub-langs", "zh-Hans,zh-Hant,zh,en",
            "--skip-download",
            "--convert-subs", "srt",
            "--output", f"{output_dir}/%(id)s",
            "--no-warnings",
            url
        ], capture_output=True, text=True, timeout=60)
        
        # 找生成的字幕文件
        for f in Path(output_dir).glob("*.srt"):
            result_files.append(str(f))
        return result_files
    except Exception as e:
        print(f"⚠️ 字幕下载失败: {e}")
        return result_files

def search_player_stats(name: str) -> dict:
    """搜索球员公开统计数据（通过FBref）"""
    try:
        import requests
        # FBref 搜索
        search_url = f"https://fbref.com/en/players/search?q={name}"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; research bot)"}
        r = requests.get(search_url, headers=headers, timeout=15)
        return {
            "source": "fbref",
            "search_url": search_url,
            "status": "ok" if r.status_code == 200 else f"http_{r.status_code}",
            "note": "直接在浏览器打开 search_url 查看球员数据"
        }
    except Exception as e:
        return {"source": "fbref", "status": f"error: {e}"}

def collect_for_player(name: str, output_dir: str = None) -> dict:
    """
    为指定球员采集所有可用信息来源
    返回采集结果摘要
    """
    output_dir = Path(output_dir or f"./sources/{name}")
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "videos").mkdir(exist_ok=True)
    (output_dir / "transcripts").mkdir(exist_ok=True)
    (output_dir / "data").mkdir(exist_ok=True)

    print(f"\n🎯 开始为「{name}」采集信息...")
    print(f"   输出目录: {output_dir}")
    print()

    results = {
        "player": name,
        "collected_at": datetime.now().isoformat(),
        "videos": [],
        "transcripts": [],
        "stats": {},
    }

    # 1. YouTube 搜索（采访+分析）
    print("📺 搜索 YouTube 采访...")
    yt_results = search_youtube(f"{name} 球员 采访", max_results=5)
    for v in yt_results:
        print(f"   ▶ {v['title'][:50]} ({v['duration']}s) {v['url']}")
    results["videos"].extend([{"platform": "youtube", **v} for v in yt_results])

    # 2. YouTube 搜索（比赛+高光）
    print("\n⚽ 搜索 YouTube 比赛高光...")
    yt_match = search_youtube(f"{name} 全场 高光 进球", max_results=3)
    for v in yt_match:
        print(f"   ▶ {v['title'][:50]} {v['url']}")
    results["videos"].extend([{"platform": "youtube_match", **v} for v in yt_match])

    # 3. B站搜索
    print("\n📺 搜索 B站...")
    blbl = search_bilibili(f"{name} 球员 采访", max_results=5)
    for v in blbl:
        print(f"   ▶ {v['title'][:50]} by {v['author']}")
    results["videos"].extend([{"platform": "bilibili", **v} for v in blbl])

    # 4. 球员数据
    print("\n📊 球员统计数据...")
    stats = search_player_stats(name)
    print(f"   FBref: {stats.get('status')} → {stats.get('search_url', '')[:60]}...")
    results["stats"] = stats

    # 保存结果
    report = output_dir / "collection_report.json"
    report.write_text(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"\n✅ 采集报告已保存: {report}")

    print("\n📋 下一步操作：")
    print("   1. 用 yt-dlp 下载字幕：")
    for v in results["videos"]:
        if v.get("platform") == "youtube":
            print(f"      yt-dlp --write-subs --convert-subs srt {v['url']}")
    print("   2. 用脚本清洗字幕：")
    print("      python3 scripts/srt_to_transcript.py [字幕文件.srt] [输出.txt]")
    print("   3. 将清洗后的文本存入 references/sources/transcripts/ 目录")

    return results

# ── 主入口 ──────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 collect_sources.py <球员名> [输出目录]")
        print("示例: python3 collect_sources.py 梅西 ./messi_sources")
        print("       python3 collect_sources.py 哈兰德")
        sys.exit(1)

    name = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else None
    collect_for_player(name, out_dir)
