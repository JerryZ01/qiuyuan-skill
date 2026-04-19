#!/usr/bin/env bash
# 球探 · 字幕下载脚本
# 优先顺序：中文人工字幕 → 英文人工字幕 → 自动字幕
# 用法: bash download_subtitles.sh <YouTube_URL> [输出目录]

set -euo pipefail

URL="${1:?用法: bash download_subtitles.sh <YouTube_URL> [输出目录]}"
OUT_DIR="${2:-.}"

mkdir -p "$OUT_DIR"

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "❌ 未安装 yt-dlp，无法下载字幕"
  echo "   安装后重试，或改为手动下载字幕文件"
  exit 1
fi

echo "🔍 获取视频信息..."
VIDEO_ID="$(python3 - <<'PY' "$URL"
import re, sys
url = sys.argv[1]
match = re.search(r'(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})', url)
print(match.group(1) if match else 'video')
PY
)"
TITLE="$(yt-dlp --get-title --no-warnings "$URL" 2>/dev/null || true)"
if [ -n "$TITLE" ]; then
  echo "📺 $TITLE"
fi

echo "📥 尝试下载人工字幕..."
yt-dlp --write-subs --sub-langs "zh-Hans,zh-Hant,zh,en" \
  --skip-download --convert-subs srt \
  --output "$OUT_DIR/${VIDEO_ID}" \
  --no-warnings "$URL" 2>/dev/null || true

if compgen -G "$OUT_DIR/*.srt" >/dev/null; then
  FIRST_SRT="$(python3 - <<'PY' "$OUT_DIR"
from pathlib import Path
import sys
files = sorted(Path(sys.argv[1]).glob('*.srt'))
print(files[0] if files else '')
PY
)"
  echo "✅ 字幕下载成功: $FIRST_SRT"
  echo "📝 下一步: python3 scripts/srt_to_transcript.py \"$FIRST_SRT\" [output.txt]"
  exit 0
fi

echo "⚠️ 未找到人工字幕，尝试自动字幕..."
yt-dlp --write-auto-subs --sub-langs "zh-Hans,zh-Hant,zh,en" \
  --skip-download --convert-subs srt \
  --output "$OUT_DIR/${VIDEO_ID}_auto" \
  --no-warnings "$URL" 2>/dev/null || true

if compgen -G "$OUT_DIR/*.srt" >/dev/null; then
  FIRST_SRT="$(python3 - <<'PY' "$OUT_DIR"
from pathlib import Path
import sys
files = sorted(Path(sys.argv[1]).glob('*.srt'))
print(files[0] if files else '')
PY
)"
  echo "✅ 自动字幕下载成功: $FIRST_SRT"
  echo "📝 下一步: python3 scripts/srt_to_transcript.py \"$FIRST_SRT\" [output.txt]"
  exit 0
fi

echo "❌ 未找到可用字幕文件"
echo "💡 建议："
echo "   1. 在浏览器确认视频本身是否带字幕"
echo "   2. 更换视频源，优先找采访或媒体发布的长视频"
echo "   3. 手动下载字幕后，再用 srt_to_transcript.py 清洗"
exit 1
