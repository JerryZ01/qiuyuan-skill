#!/usr/bin/env python3
"""
球探 · SRT字幕转纯文本
去除时间戳、序号、HTML标签、连续重复行
用法: python3 srt_to_transcript.py <input.srt> [output.txt]
"""
import sys, re
from pathlib import Path

def clean_text(text: str) -> str:
    """清理单条字幕文本"""
    # 去HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    # 去格式标签（如颜色、音乐符号）
    text = re.sub(r'♪|♫|♬|▶|■|●|▸', '', text)
    # 规范化空白
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def srt_to_transcript(srt_path: str, out_path: str = None) -> str:
    """
    读取SRT文件，输出干净的可阅读文本。
    保留说话人标签（如果有）和字幕内容。
    """
    content = Path(srt_path).read_text(encoding='utf-8', errors='replace')
    blocks = re.split(r'\n\n+', content.strip())

    lines = []
    prev_text = ""
    repeat_count = 0

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # 解析时间轴行（第2行通常是时间轴）
        block_lines = block.split('\n')
        timestamp_line = None
        text_lines = []

        for i, line in enumerate(block_lines):
            line = line.strip()
            if re.match(r'\d{2}:\d{2}:\d{2}', line):
                timestamp_line = line
            elif re.match(r'^\d+$', line):
                continue  # 跳过序号
            elif line:
                text_lines.append(line)

        if not text_lines:
            continue

        # 合并文本行（同一时间轴可能有多个字幕行）
        combined = ' '.join(text_lines)
        cleaned = clean_text(combined)

        if not cleaned or len(cleaned) < 3:
            continue

        # 去连续重复（足球解说常重复词句）
        if cleaned == prev_text:
            repeat_count += 1
            continue
        else:
            if repeat_count > 2:
                # 之前有重复段，加一行分隔
                lines.append('───')
            repeat_count = 0

        # 说话人标签（如果有格式 <Speaker Name>）
        speaker_match = re.search(r'^【(.+?)】', cleaned)
        if speaker_match:
            speaker = speaker_match.group(1)
            text = cleaned[speaker_match.end():].strip()
            lines.append(f"[{speaker}] {text}")
        else:
            lines.append(cleaned)

        prev_text = cleaned

    result = '\n'.join(lines)

    if out_path:
        Path(out_path).write_text(result, encoding='utf-8')
        print(f"✅ 已保存: {out_path} ({len(result)} 字)")
        print(f"   有效行数: {len([l for l in lines if l.strip() and l != '───'])}")

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 srt_to_transcript.py <input.srt> [output.txt]")
        sys.exit(1)

    srt_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None

    if not Path(srt_file).exists():
        print(f"❌ 文件不存在: {srt_file}")
        sys.exit(1)

    result = srt_to_transcript(srt_file, out_file)
    if not out_file:
        print("\n─── 预览（前20行）───")
        preview = '\n'.join(result.split('\n')[:20])
        print(preview)
        print(f"\n（共 {len(result)} 字）")
