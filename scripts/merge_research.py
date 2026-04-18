#!/usr/bin/env python3
"""
qiuyuan-skill · 调研合并脚本
用法：python3 merge_research.py <skill目录>

功能：
  扫描 references/research/ 目录下的 8 路报告 + 跨维度矩阵，
  统计来源数量、一手 / 二手命中情况，生成进入提炼前的质量检查点表格。

输出：直接打印 Markdown 格式的检查点表格，可重定向保存。
"""

import os
import re
import sys
from pathlib import Path

AGENT_FILES = {
    "01-space.md": "① 空间决策",
    "02-decision.md": "② 技术决策库",
    "03-physical.md": "③ 身体与极限",
    "04-system.md": "④ 体系契合",
    "05-media.md": "⑤ 媒体叙事",
    "06-social.md": "⑥ 社交动态",
    "07-moments.md": "⑦ 关键时刻",
    "08-career.md": "⑧ 生涯轨迹",
}

PRIMARY_KEYWORDS = [
    "采访",
    "字幕",
    "本人说",
    "srt",
    "transcript",
    "instagram",
    "twitter",
    "微博",
    "更衣室",
    "赛后",
    "球员本人",
]

SECONDARY_KEYWORDS = [
    "媒体报道",
    "记者",
    "虎扑",
    "ESPN",
    "The Athletic",
    "解说",
    "二手",
    "据说",
    "外界评价",
    "外界认为",
    "据悉",
    "数据平台",
    "FBref",
    "Transfermarkt",
    "wyscout",
]


def count_sources(file_path: str) -> dict:
    """分析单个 md 文件的来源情况"""
    path = Path(file_path)
    if not path.exists():
        return {"primary": 0, "secondary": 0, "links": 0, "key_findings": []}

    content = path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()

    links = len(re.findall(r'https?://[^\s）\)\]]+', content))
    primary_hits = sum(1 for keyword in PRIMARY_KEYWORDS if keyword in content)
    secondary_hits = sum(1 for keyword in SECONDARY_KEYWORDS if keyword in content)

    findings = [line.strip().lstrip("#").strip() for line in lines if line.startswith("## ")]
    findings = [item for item in findings if item and not item.startswith("跨维度") and not item.startswith("矛盾")]

    return {
        "primary": primary_hits,
        "secondary": secondary_hits,
        "links": links,
        "key_findings": findings[:3],
    }


def build_table(skill_dir: str) -> str:
    """生成调研检查点表格"""
    research_dir = Path(skill_dir) / "references" / "research"
    if not research_dir.exists():
        return f"❌ 目录不存在: {research_dir}"

    rows = []
    total_primary = 0
    total_secondary = 0
    total_links = 0
    agents_with_data = 0

    for filename, agent_name in AGENT_FILES.items():
        stats = count_sources(str(research_dir / filename))
        links = stats["links"]
        primary = stats["primary"]
        secondary = stats["secondary"]
        findings = stats["key_findings"]

        if links > 0 or primary > 0 or secondary > 0:
            agents_with_data += 1

        total_primary += primary
        total_secondary += secondary
        total_links += links

        finding_text = "; ".join(findings[:2]) if findings else ""
        rows.append(f"| {agent_name} | {links} 条 | {primary} | {secondary} | {finding_text} |")

    matrix_path = research_dir / "09-cross-matrix.md"
    matrix_status = "✅ 已生成" if matrix_path.exists() else "❌ 缺失"

    contradictions = 0
    if matrix_path.exists():
        matrix_content = matrix_path.read_text(encoding="utf-8", errors="ignore")
        contradictions = matrix_content.count("矛盾")

    ratio = int(total_primary / (total_primary + total_secondary) * 100) if (total_primary + total_secondary) > 0 else 0

    table = """## Phase 1.5 调研质量检查点

| Agent | 来源数 | 一手 | 二手 | 关键发现 |
|-------|-------|------|------|---------|
"""
    table += "\n".join(rows)

    summary = f"""
### 汇总

| 指标 | 数值 |
|------|------|
| 有效 Agent 数 | {agents_with_data}/8 |
| 总链接数 | {total_links} |
| 一手来源命中 | {total_primary} |
| 二手来源命中 | {total_secondary} |
| 一手占比 | {ratio}% |
| 跨维度矩阵 | {matrix_status} |
| 矛盾点数量 | {contradictions} 处 |

### 通过判断

"""

    if agents_with_data < 5:
        summary += "⚠️ **警告**：有效 Agent < 5，建议补充调研\n"
    elif ratio < 50:
        summary += "⚠️ **警告**：一手来源占比 < 50%，信息质量可能受限\n"
    else:
        summary += "✅ **通过**：信息采集量和质量满足要求\n"

    if matrix_status == "❌ 缺失":
        summary += "⚠️ **阻断**：跨维度矩阵缺失，必须先生成再进入 Phase 2\n"
    elif contradictions == 0:
        summary += "⚠️ **提示**：未发现矛盾点，建议确认是否保留了真实张力，而不是把材料抹平\n"
    else:
        summary += f"✅ 发现 {contradictions} 处矛盾点，已记录在矩阵中\n"

    return table + summary


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 merge_research.py <skill目录>")
        print("示例: python3 merge_research.py ~/.claude/skills/leao-perspective.skill")
        sys.exit(1)

    target_skill_dir = os.path.expanduser(sys.argv[1])
    print(build_table(target_skill_dir))
