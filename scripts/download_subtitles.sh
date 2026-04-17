#!/usr/bin/env bash
#────────────────────────────────────────────────────────────
# 球探 · 字幕下载脚本
# 优先顺序：中文人工字幕 → 英文人工字幕 → 自动字幕
# 用法: bash download_subtitles.sh <YouTube_URL> [输出目录]
#────────────────────────────────────────────────────────────
set -e

URL="${1:?用法: bash download_subtitles.sh <YouTube_URL> [输出目录]}"
OUT_DIR="${2:-.}"

mkdir -p "$OUT_DIR"

echo "🔍 获取视频信息..."
VIDEO_ID=$(echo "$URL" | grep -oP '(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})')
TITLE=$(yt-dlp --get-title --no-warnings "$URL" 2>/dev/null | head -1)
echo "📺 $TITLE"

# ── 优先找字幕 ──────────────────────────────────────────
echo "🎯 查找字幕..."
SUBTITLE_FILE=""

# 方法1：youtube-transcript-api（无需key，自动字幕）
if command -v python3 &>/dev/null; then
  PYTHON=$(python3 -c "import yt_dlp; print('ok')" 2>/dev/null && echo "yt-dlp" || echo "missing")
else
  PYTHON="missing"
fi

# 尝试用 yt-dlp 提取字幕
echo "📥 尝试下载字幕..."
SUBTITLE_FILE="$OUT_DIR/${VIDEO_ID}.srt"

# 中文字幕
yt-dlp --write-subs --sub-langs "zh-Hans,zh-Hant,zh,en" \
  --skip-download --convert-subs srt \
  --output "$OUT_DIR/${VIDEO_ID}" \
  --no-warnings "$URL" 2>/dev/null && echo "✅ 字幕下载成功" || {
  echo "⚠️ yt-dlp 字幕提取失败，尝试备用方式..."
  
  # 备用：yt-dlp 自动字幕（英文优先）
  yt-dlp --write-auto-subs --sub-langs "en" \
    --skip-download --convert-subs srt \
    --output "$OUT_DIR/${VIDEO_ID}_auto" \
    --no-warnings "$URL" 2>/dev/null && {
    mv "$OUT_DIR/${VIDEO_ID}_auto.en.srt" "$SUBTITLE_FILE" 2>/dev/null || true
    echo "✅ 自动字幕（英文）下载成功"
  }
}

# 输出结果
if ls "$OUT_DIR"/*.srt 1>/dev/null 2>&1; then
  SRT=$(ls "$OUT_DIR"/*.srt | head -1)
  LINES=$(wc -l < "$SRT")
  echo ""
  echo "✅ 字幕文件: $SRT ($LINES 行)"
  echo "📝 下一步: python3 srt_to_transcript.py $SRT [output.txt]"
else
  echo "❌ 未找到字幕文件"
  echo "💡 提示: 如果视频没有字幕，尝试用 -A 标志获取自动字幕"
  echo "   yt-dlp --write-auto-subs --sub-langs en ..."
fi
