#!/usr/bin/env python3
"""
qiuyuan-skill · 质量自检脚本
用法：python3 quality_check.py <生成的SKILL.md路径>

功能：
  检查交付前的关键结构完整性，逐项输出 PASS / WARN / FAIL，并给出改进建议。
  目标不是评判内容真假，而是避免交付结构空心、逻辑断裂的 Skill。
"""

import os
import re
import sys
from pathlib import Path

AGENT_SUFFIXES = [
    "space",
    "decision",
    "physical",
    "system",
    "media",
    "social",
    "moments",
    "career",
]


def count_agent_reports(skill_dir: str) -> int:
    """扫描 references/research/，统计 8 路 Agent 报告存在数量"""
    research_dir = Path(skill_dir) / "references" / "research"
    if not research_dir.exists():
        return 0

    count = 0
    for index, suffix in enumerate(AGENT_SUFFIXES, start=1):
        report_name = f"{index:02d}-{suffix}.md"
        if (research_dir / report_name).exists():
            count += 1
    return count


def check_skill(path: str) -> dict:
    """对生成的 SKILL.md 执行结构检查"""
    if not os.path.exists(path):
        return {"error": f"文件不存在: {path}"}

    content = Path(path).read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()
    results = []

    model_items = re.findall(
        r'(?:^|\n)(?:\d+\.|[-*])\s*.*?(?:模型|原则|规则)',
        content,
        re.MULTILINE,
    )
    model_count = len(model_items)
    if 3 <= model_count <= 5:
        results.append(("战术模型数量", "PASS", f"{model_count} 个，符合 3-5 个目标"))
    elif model_count < 3:
        results.append(("战术模型数量", "WARN", f"仅 {model_count} 个，建议至少 3 个"))
    else:
        results.append(("战术模型数量", "WARN", f"{model_count} 个，偏多，建议压缩到 3-5 个核心模型"))

    anti_pattern_count = content.count("禁区行为") + content.count("绝对不会") + content.count("反模式") + content.count("❌")
    if anti_pattern_count >= 3:
        results.append(("禁区行为数量", "PASS", f"找到 {anti_pattern_count} 处禁区描述"))
    else:
        results.append(("禁区行为数量", "FAIL", f"仅 {anti_pattern_count} 处，建议至少 3 条具体反模式"))

    has_physical_section = bool(re.search(r'身体极限|身体条件|极限边界|身体与极限', content))
    physical_lines = [line for line in lines if re.search(r'速度|爆发|耐力|伤病|对抗|体能', line) and len(line.strip()) > 5]
    if has_physical_section and len(physical_lines) >= 3:
        results.append(("身体极限边界", "PASS", f"找到 {len(physical_lines)} 条具体描述"))
    else:
        results.append(("身体极限边界", "WARN", "缺少身体极限边界 section 或内容不足"))

    media_lines = [
        line for line in lines
        if any(keyword in line for keyword in ["媒体叙事", "舆论", "热梗", "争议", "社媒", "更衣室"]) and len(line.strip()) > 5
    ]
    if len(media_lines) >= 3:
        results.append(("生态背景", "PASS", f"找到 {len(media_lines)} 条生态相关描述"))
    else:
        results.append(("生态背景", "WARN", "媒体叙事 / 社交动态内容偏少，可能影响生态层覆盖"))

    honest_lines = [
        line for line in lines
        if any(keyword in line for keyword in ["局限", "捕捉不到", "做不到", "无法", "偏差", "截止"]) and len(line.strip()) > 8
    ]
    if len(honest_lines) >= 3:
        results.append(("诚实边界", "PASS", f"找到 {len(honest_lines)} 条具体边界"))
    else:
        results.append(("诚实边界", "FAIL", f"仅 {len(honest_lines)} 条，建议至少 3 条"))

    dna_rules = re.findall(r'表达DNA.*规则|确定性规则|情绪规则|词汇规则|团队.*规则|话题禁区|幽默规则', content)
    dna_count = len(dna_rules)
    if dna_count >= 5:
        results.append(("表达DNA规则覆盖", "PASS", f"找到 {dna_count} 条表达 DNA 规则"))
    else:
        results.append(("表达DNA规则覆盖", "FAIL", f"仅 {dna_count} 条，建议至少 5 条具体说话方式规则"))

    has_identity = bool(re.search(r'## 身份卡|## Identity', content))
    identity_lines = [line for line in lines if re.search(r'我是|身份卡|identity', line, re.IGNORECASE)]
    if has_identity and len(identity_lines) >= 2:
        results.append(("身份卡", "PASS", "身份卡 section 存在"))
    else:
        results.append(("身份卡", "WARN", "缺少身份卡 section，建议补充"))

    ai_phrases = ["综上所述", "总而言之", "作为一个", "值得注意的是", "从以上", "可以发现"]
    ai_hits = sum(1 for phrase in ai_phrases if phrase in content)
    if ai_hits == 0:
        results.append(("AI模板味检测", "PASS", "未发现明显 AI 口癖"))
    else:
        results.append(("AI模板味检测", "WARN", f"发现 {ai_hits} 处疑似模板表达，建议替换为球员语气"))

    cross_count = content.count("印证") + content.count("矛盾") + content.count("涌现")
    if cross_count >= 3:
        results.append(("跨维度发现", "PASS", f"找到 {cross_count} 处跨维度连接"))
    else:
        results.append(("跨维度发现", "WARN", "跨维度发现不足，建议先补足交叉矩阵再提炼"))

    skill_dir = os.path.dirname(path)
    agent_count = count_agent_reports(skill_dir)
    if agent_count >= 6:
        results.append(("Agent调研覆盖", "PASS", f"{agent_count}/8 路报告存在"))
    elif agent_count >= 4:
        results.append(("Agent调研覆盖", "WARN", f"仅 {agent_count}/8 路，建议至少 6 路"))
    else:
        results.append(("Agent调研覆盖", "FAIL", f"仅 {agent_count}/8 路，调研严重不足"))

    return {"checks": results, "file": path}


def print_results(result: dict) -> None:
    if "error" in result:
        print(f"❌ {result['error']}")
        return

    print(f"\n{'=' * 60}")
    print(" qiuyuan-skill 质量自检报告")
    print(f" 文件: {result['file']}")
    print(f"{'=' * 60}\n")

    print(f"{'检查项':<20} {'状态':<8} {'说明'}")
    print(f"{'-' * 20} {'-' * 8} {'-' * 30}")

    pass_count = fail_count = warn_count = 0
    for name, status, desc in result["checks"]:
        icon = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️"}[status]
        print(f"{name:<20} {icon} {status:<6} {desc}")
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
        else:
            warn_count += 1

    print(f"\n{'=' * 60}")
    print(f" 通过: {pass_count}  |  警告: {warn_count}  |  失败: {fail_count}")

    if fail_count > 0:
        print("\n🔴 有失败项，建议修复后再交付")
    elif warn_count > 2:
        print("\n🟡 有多处警告，建议继续优化")
    else:
        print("\n🟢 质量基本合格，可交付")

    print(f"{'=' * 60}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 quality_check.py <SKILL.md路径>")
        print("示例: python3 quality_check.py ~/.claude/skills/leao-perspective.skill/SKILL.md")
        sys.exit(1)

    skill_md = os.path.expanduser(sys.argv[1])
    result = check_skill(skill_md)
    print_results(result)
