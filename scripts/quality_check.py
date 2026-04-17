#!/usr/bin/env python3
"""
qiuyuan-skill · 质量自检脚本
用法：python3 quality_check.py <生成的SKILL.md路径>

功能：
  检查 Phase 4 质量验证的 6 项标准，逐项输出 PASS / FAIL，并给出改进建议。
  在提交前执行，不要等到用户发现问题。
"""

import sys, re, os
from pathlib import Path

def count_agents_referenced(skill_dir: str) -> int:
    """扫描 references/research/，统计有多少路 Agent 报告存在"""
    research_dir = Path(skill_dir) / "references" / "research"
    if not research_dir.exists():
        return 0
    count = 0
    for i in range(1, 9):
        fname = f"0{i}-{['space','decision','physical','system','media','social','moments','career'][i-1]}.md"
        if (research_dir / fname).exists():
            count += 1
    return count

def check_skill(path: str) -> dict:
    """对生成的 SKILL.md 执行 6 项检查"""
    if not os.path.exists(path):
        return {"error": f"文件不存在: {path}"}

    content = open(path, encoding="utf-8", errors="ignore").read()
    lines = content.split('\n')

    results = []

    # ── 检查1：战术模型数量（3-5个）──────────────────────────────
    model_sections = re.findall(r'#{1,3} 战术模型|/#{1,3} 模型|#{1,3}.*模型', content)
    # 找 "1. xxx" 或 "## xxx" 格式的模型条目
    model_items = re.findall(r'(?:^|\n)(?:\d+\.|\*\*)[\s【\[].{4,40}?(?:模型|原则|规则)', content, re.MULTILINE)
    model_count = len(model_items)
    if 3 <= model_count <= 7:
        results.append(("战术模型数量", "PASS", f"{model_count}个，符合3-7个要求"))
    elif model_count < 3:
        results.append(("战术模型数量", "WARN", f"仅{model_count}个，建议至少3个"))
    else:
        results.append(("战术模型数量", "PASS", f"{model_count}个，数量充足"))

    # ── 检查2：每个模型有失效条件（禁区行为/诚实边界）────────────
    anti_pattern_count = content.count("禁区行为") + content.count("绝对不会") + content.count("❌")
    if anti_pattern_count >= 3:
        results.append(("禁区行为数量", "PASS", f"找到{anti_pattern_count}处禁区描述"))
    else:
        results.append(("禁区行为数量", "FAIL", f"仅{anti_pattern_count}处禁区描述，建议至少3条具体反模式"))

    # ── 检查3：身体极限边界section存在且有具体内容 ───────────────
    has_physical = bool(re.search(r'身体极限|身体条件|极限边界|身体与极限', content))
    physical_lines = [l for l in lines if re.search(r'速度|爆发|耐力|伤病|对抗|体能', l) and len(l.strip()) > 5]
    if has_physical and len(physical_lines) >= 3:
        results.append(("身体极限边界", "PASS", f"找到{len(physical_lines)}条具体边界描述"))
    else:
        results.append(("身体极限边界", "WARN", "缺少身体极限边界section或内容不足"))

    # ── 检查4：生态层信息（媒体叙事/社交动态有具体内容）──────────
    media_lines = [l for l in lines if any(kw in l for kw in ["媒体叙事", "舆论", "热梗", "争议", "社媒", "更衣室"]) and len(l.strip()) > 5]
    if len(media_lines) >= 3:
        results.append(("生态背景", "PASS", f"找到{len(media_lines)}条生态相关描述"))
    else:
        results.append(("生态背景", "WARN", "媒体叙事/社交动态内容偏少，可能影响生态层覆盖"))

    # ── 检查5：诚实边界section存在且≥3条 ─────────────────────────
    honest_sections = re.findall(r'诚实边界|数据边界|数据局限|做不到|无法捕捉', content)
    honest_lines = [l for l in lines if any(kw in l for kw in ["局限", "捕捉不到", "做不到", "无法", "偏差", "截止"]) and len(l.strip()) > 8]
    if len(honest_lines) >= 3:
        results.append(("诚实边界", "PASS", f"找到{len(honest_lines)}条具体边界"))
    else:
        results.append(("诚实边界", "FAIL", f"仅{len(honest_lines)}条诚实边界，建议至少3条"))

    # ── 检查6：表达DNA推导规则（Phase 2.3→Phase 3的链路）─────────────
    dna_rules = re.findall(r'表达DNA.*规则|确定性规则|情绪规则|词汇规则|团队.*规则|话题禁区|幽默规则', content)
    dna_count = len(dna_rules)
    if dna_count >= 5:
        results.append(("表达DNA规则覆盖", "PASS", f"找到{dna_count}条表达DNA推导规则"))
    else:
        results.append(("表达DNA规则覆盖", "FAIL", f"仅{dna_count}条，建议至少5条具体说话方式规则"))

    # ── 检查7：身份卡存在且有内容 ─────────────────────────────────
    has_identity = bool(re.search(r'## 身份卡|## Identity', open(path, encoding="utf-8", errors="ignore").read()))
    identity_lines = [l for l in lines if re.search(r'我是|身份卡|identity', l, re.IGNORECASE)]
    if has_identity and len(identity_lines) >= 2:
        results.append(("身份卡", "PASS", "身份卡section存在"))
    else:
        results.append(("身份卡", "WARN", "缺少身份卡section，建议添加"))

    # ── 检查7：是否有 AI 模板味（检测 ChatGPT 口癖）────────────────
    ai_phrases = ["综上所述", "总而言之", "作为一个", "值得注意的是", "值得注意的是", "从以上", "可以发现"]
    ai_hits = sum(1 for p in ai_phrases if p in content)
    if ai_hits == 0:
        results.append(("AI模板味检测", "PASS", "未发现明显AI口癖"))
    else:
        results.append(("AI模板味检测", "WARN", f"发现{ai_hits}处疑似AI模板表达，建议替换为球员真实语气"))

    # ── 检查9：跨维度矩阵引用 ─────────────────────────────────────
    has_cross = bool(re.search(r'跨维度|印证|矛盾|涌现', content))
    cross_count = content.count("印证") + content.count("矛盾") + content.count("涌现")
    if cross_count >= 3:
        results.append(("跨维度发现", "PASS", f"找到{cross_count}处跨维度连接"))
    else:
        results.append(("跨维度发现", "WARN", "跨维度发现不足，建议在Phase 1.4生成矩阵后提炼"))

    # ── Agent覆盖（额外指标）──────────────────────────────────────
    skill_dir = os.path.dirname(path)
    agent_count = count_agents_referenced(skill_dir)
    if agent_count >= 6:
        results.append(("Agent调研覆盖", "PASS", f"{agent_count}/8路报告存在"))
    elif agent_count >= 4:
        results.append(("Agent调研覆盖", "WARN", f"仅{agent_count}/8路，建议至少6路"))
    else:
        results.append(("Agent调研覆盖", "FAIL", f"仅{agent_count}/8路，调研严重不足"))

    return {"checks": results, "file": path}

def print_results(result: dict):
    if "error" in result:
        print(f"❌ {result['error']}")
        return

    print(f"\n{'='*60}")
    print(f" qiuyuan-skill 质量自检报告")
    print(f" 文件: {result['file']}")
    print(f"{'='*60}\n")

    print(f"{'检查项':<20} {'状态':<8} {'说明'}")
    print(f"{'-'*20} {'-'*8} {'-'*30}")

    pass_count = fail_count = warn_count = 0
    for name, status, desc in result["checks"]:
        icon = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️"}[status]
        print(f"{name:<20} {icon} {status:<6} {desc}")
        if status == "PASS": pass_count += 1
        elif status == "FAIL": fail_count += 1
        else: warn_count += 1

    print(f"\n{'='*60}")
    print(f" 通过: {pass_count}  |  警告: {warn_count}  |  失败: {fail_count}")

    if fail_count > 0:
        print("\n🔴 有失败项，建议修复后再交付")
    elif warn_count > 2:
        print("\n🟡 有多处警告，建议优化")
    else:
        print("\n🟢 质量基本合格，可交付")

    print(f"{'='*60}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 quality_check.py <SKILL.md路径>")
        print("示例: python3 quality_check.py ~/.claude/skills/leao-perspective/SKILL.md")
        sys.exit(1)

    skill_md = os.path.expanduser(sys.argv[1])
    result = check_skill(skill_md)
    print_results(result)
