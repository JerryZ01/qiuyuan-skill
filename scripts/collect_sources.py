#!/usr/bin/env python3
"""
球探 · 球员信息来源采集脚本

用途：
- 为指定球员创建标准化素材目录
- 记录 YouTube / B站 / 数据平台的搜索结果摘要
- 输出后续人工筛选与补充的建议

说明：
- 这是“采集助手”，不是保证成功的全自动爬虫。
- 视频平台、接口可用性和网络环境差异很大，失败时可直接转为手动采集。

使用方法：
  python3 collect_sources.py <球员名> [输出目录]
  python3 collect_sources.py 梅西 ./messi_sources
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus


def ensure_structure(output_dir: Path) -> None:
    """创建标准化目录结构"""
    for subdir in ["videos", "transcripts", "data", "social", "notes"]:
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)


def search_youtube(query: str, max_results: int = 5) -> list[dict]:
    """用 yt-dlp 搜索 YouTube，返回视频列表"""
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--flat-playlist",
                "--print",
                "%(id)s|%(title)s|%(duration)s|%(webpage_url)s",
                "--match-filter",
                "duration > 60",
                "--",
                f"ytsearch{max_results}:{query}",
            ],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except FileNotFoundError:
        print("⚠️ yt-dlp 未安装，跳过 YouTube 搜索")
        return []
    except Exception as exc:
        print(f"⚠️ YouTube 搜索失败: {exc}")
        return []

    videos = []
    for line in result.stdout.strip().splitlines():
        if "|" not in line:
            continue
        parts = line.split("|", 3)
        if len(parts) != 4:
            continue
        video_id, title, duration, url = parts
        videos.append(
            {
                "id": video_id,
                "title": title,
                "duration": duration,
                "url": url,
            }
        )
    return videos


def search_bilibili(keyword: str, max_results: int = 10) -> list[dict]:
    """生成 B站搜索入口；请求失败时退化为可手动打开的链接"""
    search_url = (
        "https://search.bilibili.com/all?keyword="
        f"{quote_plus(keyword)}&from_source=webtop_search&spm_id_from=333.1007"
    )

    try:
        import requests

        response = requests.get(
            "https://api.bilibili.com/x/web-interface/search/type",
            params={
                "keyword": keyword,
                "search_type": "video",
                "page": 1,
                "order": "totalrank",
            },
            headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://www.bilibili.com",
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        videos = []
        for item in data.get("data", {}).get("result", [])[:max_results]:
            bvid = item.get("bvid") or ""
            videos.append(
                {
                    "bvid": bvid,
                    "title": item.get("title", "")
                    .replace('<em class="keyword">', "")
                    .replace("</em>", ""),
                    "author": item.get("author", ""),
                    "duration": item.get("duration", ""),
                    "url": f"https://www.bilibili.com/video/{bvid}" if bvid else search_url,
                }
            )
        if videos:
            return videos
    except Exception as exc:
        print(f"⚠️ B站搜索接口不可用，保留手动搜索链接: {exc}")

    return [
        {
            "title": f"手动搜索：{keyword}",
            "author": "browser",
            "duration": "",
            "url": search_url,
        }
    ]


def search_player_stats(name: str) -> dict:
    """返回公开数据平台入口，而不是假装抓到了完整数据"""
    encoded_name = quote_plus(name)
    return {
        "fbref_search": f"https://fbref.com/en/players/search/search.fcgi?search={encoded_name}",
        "transfermarkt_search": f"https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={encoded_name}",
        "sofascore_search": f"https://www.sofascore.com/search?query={encoded_name}",
        "note": "建议人工打开以上入口，记录关键数据到 data/ 目录。",
    }


def collect_for_player(name: str, output_dir: str | None = None) -> dict:
    """为指定球员采集可用的信息入口与目录结构"""
    output_path = Path(output_dir or f"./sources/{name}")
    ensure_structure(output_path)

    print(f"\n🎯 开始为「{name}」准备采集结构...")
    print(f"   输出目录: {output_path.resolve()}")
    print()

    results = {
        "player": name,
        "collected_at": datetime.now().isoformat(),
        "output_dir": str(output_path.resolve()),
        "videos": [],
        "stats": {},
        "manual_next_steps": [],
    }

    print("📺 搜索 YouTube 采访...")
    interview_videos = search_youtube(f"{name} 球员 采访", max_results=5)
    for video in interview_videos:
        print(f"   ▶ {video['title'][:60]} ({video['duration']}) {video['url']}")
    results["videos"].extend([{"platform": "youtube_interview", **video} for video in interview_videos])

    print("\n⚽ 搜索 YouTube 比赛 / 高光...")
    match_videos = search_youtube(f"{name} 全场 高光 战术分析", max_results=5)
    for video in match_videos:
        print(f"   ▶ {video['title'][:60]} ({video['duration']}) {video['url']}")
    results["videos"].extend([{"platform": "youtube_match", **video} for video in match_videos])

    print("\n📺 搜索 B站入口...")
    bilibili_videos = search_bilibili(f"{name} 球员 采访", max_results=5)
    for video in bilibili_videos:
        print(f"   ▶ {video['title'][:60]} {video['url']}")
    results["videos"].extend([{"platform": "bilibili", **video} for video in bilibili_videos])

    print("\n📊 生成数据平台入口...")
    stats = search_player_stats(name)
    print(f"   FBref: {stats['fbref_search']}")
    print(f"   Transfermarkt: {stats['transfermarkt_search']}")
    print(f"   SofaScore: {stats['sofascore_search']}")
    results["stats"] = stats

    results["manual_next_steps"] = [
        "从 videos 列表里挑 2-3 个高质量采访/比赛素材，优先处理字幕。",
        "把清洗后的文本放入 transcripts/ 或 notes/。",
        "把数据平台的关键数字手工整理到 data/。",
        "把社媒与争议事件整理到 social/。",
    ]

    report_path = output_path / "collection_report.json"
    report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✅ 采集报告已保存: {report_path}")

    print("\n📋 下一步建议：")
    print("   1. 选取高质量视频，尝试下载字幕或手动转录")
    print("   2. 用 srt_to_transcript.py 清洗字幕")
    print("   3. 将文本归档到 transcripts/、notes/、data/、social/")
    print("   4. 素材够用后，再进入 8 路研究和交叉矩阵阶段")

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 collect_sources.py <球员名> [输出目录]")
        print("示例: python3 collect_sources.py 梅西 ./messi_sources")
        sys.exit(1)

    player_name = sys.argv[1]
    destination = sys.argv[2] if len(sys.argv) > 2 else None
    collect_for_player(player_name, destination)
