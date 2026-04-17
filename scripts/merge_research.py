#!/usr/bin/env python3
"""
qiuyuan-skill · 调研合并脚本
用法：python3 merge_research.py <skill目录>

功能：
  扫描 references/research/ 目录下的 8路报告 + 跨维度矩阵，
  自动统计来源数量、一手/二手占比，生成 Phase 1.5 质量检查点表格。

输出：直接打印 Markdown 格式的检查点表格，可重定向保存。
"""

import os, sys, re
from pathlib import Path

AGENT_FILES = {
    "01-space.md":     "① 空间决策",
    "02-decision.md":  "② 技术决策库",
    "03-physical.md":  "③ 身体与极限",
    "04-system.md":    "④ 体系契合",
    "05-media.md":     "⑤ 媒体叙事",
    "06-social.md":    "⑥ 社交动态",
    "07-moments.md":   "⑦ 关键时刻",
    "08-career.md":    "⑧ 生涯轨迹",
}

def count_sources(file_path: str) -> dict:
    """分析一个 md 文件的来源情况"""
    if not os.path.exists(file_path):
        return {"total": 0, "primary": 0, "secondary": 0, "links": 0, "key_findings": []}

    content = open(file_path, encoding="utf-8", errors="ignore").read()
    lines = content.split('\n')

    links = len(re.findall(r'https?://[^\s）\)）\]]+', content))

    # 一手来源：采访字幕/比赛记录/本人社媒/球员本人说法
    primary_kw = ["采访", "字幕", "本人说", "本人说", "我在", "srt", "transcript",
                  "instagram", "twitter", "微博", "更衣室", "赛后", "球员本人"]
    # 二手来源：媒体报道/二手转述/集锦/分析
    secondary_kw = ["媒体报道", "记者", "虎扑", "ESPN", "The Athletic", "解说",
                    "二手", "据说", "外界评价", "外界认为", "据悉", "数据平台",
                    "FBref", "Transfermarkt", "wyscout"]

    primary_hits = sum(1 for kw in primary_kw if kw in content)
    secondary_hits = sum(1 for kw in secondary_kw if kw in content)

    # 提取关键发现（## 标题行）
    findings = [l.strip().lstrip('#').strip() for l in lines if l.startswith('## ')]
    findings = [f for f in findings if f and not f.startswith('跨维度') and not f.startswith('矛盾')]

    return {
        "total": links,
        "primary": primary_hits,
        "secondary": secondary_hits,
        "links": links,
        "key_findings": findings[:3],  # 最多取3个
    }

def build_table(skill_dir: str) -> str:
    """生成 Phase 1.5 检查点表格"""
    research_dir = Path(skill_dir) / "references" / "research"
    if not research_dir.exists():
        return f"❌ 目录不存在: {research_dir}"

    rows = []
    total_primary = 0
    total_secondary = 0
    total_links = 0
    agents_with_data = 0

    for fname, agent_name in AGENT_FILES.items():
        fpath = research_dir / fname
        stats = count_sources(str(fpath))
        links = stats["links"]
        primary = stats["primary"]
        secondary = stats["secondary"]
        findings = stats["key_findings"]

        if links > 0 or primary > 0:
            agents_with_data += 1
        total_primary += primary
        total_secondary += secondary
        total_links += links

        finding_text = "; ".join(findings[:2]) if findings else ""
        rows.append(f"| {agent_name} | {links}条 | {primary} | {secondary} | {finding_text} |")

    # 跨维度矩阵
    matrix_path = research_dir / "09-cross-matrix.md"
    matrix_status = "✅ 已生成" if matrix_path.exists() else "❌ 缺失"

    # 矛盾点统计
    contradictions = 0
    if matrix_path.exists():
        content = open(matrix_path, encoding="utf-8", errors="ignore").read()
        contradictions = content.count("矛盾")

    table = f"""## Phase 1.5 调研质量检查点

| Agent | 来源数 | 一手 | 二手 | 关键发现 |
|-------|-------|------|------|---------|
"""
    table += "\n".join(rows)

    ratio = int(total_primary / (total_primary + total_secondary) * 100) if (total_primary + total_secondary) > 0 else 0

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
        summary += "⚠️ **提示**：未发现矛盾点——真实的球员几乎都有内在张力，核实是否所有维度都被充分调研\n"
    else:
        summary += f"✅ 发现 {contradictions} 处矛盾点，已记录在矩阵中\n"

    return table + summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 merge_research.py <skill目录>")
        print("示例: python3 merge_research.py ~/.claude/skills/leao-perspective")
        sys.exit(1)

    skill_dir = os.path.expanduser(sys.argv[1])
    print(build_table(skill_dir))
