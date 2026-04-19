# 球探 · 球员信息来源采集指南

> ⚠️ **网络环境说明**：YouTube、B站、公开数据平台在不同系统和网络环境下可达性差异很大。
> 建议优先在本机浏览器确认可访问，再决定是否使用脚本辅助。脚本的职责是**组织采集结果、清洗文本、做质量检查**，不是保证所有平台都能稳定抓取。

---

## 设计原则

采集不是“抓越多越好”，而是按优先级拿到**最能解释球员决策逻辑**的材料：

1. **一手表达**：采访、赛后发言、长对谈字幕
2. **一手比赛**：全场、集锦、战术拆解对应的字幕或笔记
3. **结构化数据**：FBref、Transfermarkt、SofaScore 等公开数据
4. **二手叙事**：媒体分析、球迷共识、舆论标签

最终目标不是堆链接，而是把素材放进下面这个结构里，方便 8 路研究复用。

---

## 推荐目录结构

蒸馏某位球员时，建议在**目标 Skill 目录**里建立素材目录，而不是堆在当前仓库：

```text
~/.claude/skills/球员名-perspective.skill/
└── references/
    └── sources/
        ├── transcripts/
        ├── interviews/
        ├── matches/
        ├── social/
        └── data/
```

例如：

```text
~/.claude/skills/leao-perspective.skill/
└── references/
    └── sources/
        ├── transcripts/
        ├── interviews/
        ├── matches/
        ├── social/
        └── data/
```

这样和 `SKILL.md` 里的输出路径规范保持一致：
- 调研报告放 `references/research/`
- 原始素材放 `references/sources/`
- 配套脚本放 `scripts/`

---

## 快速采集流程

### Step 1：创建球员目录

```bash
mkdir -p ~/.claude/skills/leao-perspective.skill/references/sources
mkdir -p ~/.claude/skills/leao-perspective.skill/references/research
mkdir -p ~/.claude/skills/leao-perspective.skill/scripts

mkdir -p ~/.claude/skills/leao-perspective.skill/references/sources/transcripts
mkdir -p ~/.claude/skills/leao-perspective.skill/references/sources/interviews
mkdir -p ~/.claude/skills/leao-perspective.skill/references/sources/matches
mkdir -p ~/.claude/skills/leao-perspective.skill/references/sources/social
mkdir -p ~/.claude/skills/leao-perspective.skill/references/sources/data
```

### Step 2：获取采访 / 高光 / 全场对应素材

**方式 A：浏览器手动找素材，再用脚本处理**

优先搜索：
- `球员名 interview`
- `球员名 tactics`
- `球员名 full match`
- `球员名 post match interview`
- `球员名 战术分析`
- `球员名 全场`

推荐保存策略：
- 采访字幕 / 转录文本 → `transcripts/`
- 比赛笔记 / 全场片段说明 → `matches/`
- 媒体长文 / 专栏摘录 → `interviews/`
- 社媒截图或整理文本 → `social/`
- 数据导出 / 手工摘录 → `data/`

**方式 B：YouTube 字幕辅助下载**

如果本地网络可访问 YouTube，可以使用：

```bash
bash scripts/download_subtitles.sh "https://www.youtube.com/watch?v=VIDEO_ID" "./tmp"
python3 scripts/srt_to_transcript.py "./tmp/VIDEO_ID.srt" "./tmp/VIDEO_ID.txt"
```

说明：
- `download_subtitles.sh` 只负责尽量下载可用字幕
- 下载失败通常是网络、区域、视频本身无字幕导致，不代表流程不可继续
- 采集工作本质上允许**手动补素材**，不要把流程绑死在单一平台

### Step 3：清洗字幕 → 纯文本

```bash
python3 scripts/srt_to_transcript.py "./某采访.srt" "./某采访_清洗.txt"
```

清洗后建议把文本移动到对应目录，例如：

```text
references/sources/transcripts/leao-post-match-2024.txt
```

### Step 4：采集公开数据

建议手动打开这些站点搜索球员，并把关键结论整理成 txt / md：

| 网站 | 内容 |
|------|------|
| FBref | 进球、传球、防守、持球等结构化数据 |
| Transfermarkt | 转会、履历、位置、伤病、身价 |
| SofaScore | 赛季评分、基础热区、比赛表现 |
| The Athletic / 专栏媒体 | 战术拆解、教练评价、队友视角 |

推荐保存方式：
- 手工摘录成 `data/fbref_2025.txt`
- 媒体摘要放 `interviews/the-athletic_profile_2024.txt`

### Step 5：采集社交媒体与舆论线索

可关注：
- Instagram / X / 微博 官方账号
- 赛后发言、长文、争议声明
- 高赞评论区的共识标签

这部分主要服务于：
- 表达 DNA
- 公众形象
- 争议应对方式
- 更衣室 / 团队生态的外部折射

---

## 快速检查清单

```text
references/sources/球员名/
├── transcripts/           ← 视频字幕或清洗后的纯文本
│   ├── 2022-world-cup-interview.txt
│   └── post-match-derby.srt
├── interviews/            ← 文字采访 / 专栏摘录
│   └── the-athletic-2024.txt
├── matches/               ← 全场观察笔记 / 战术片段记录
│   └── champions-league-quarterfinal-notes.txt
├── social/                ← 社媒内容 / 争议事件整理
│   └── instagram-post-title-run.txt
└── data/                  ← 统计数据摘录 / 手动整理
    ├── fbref_2024.txt
    └── transfermarkt_profile.txt
```

建议最低标准：
- 采访或长字幕 ≥ 2 份
- 比赛相关素材 ≥ 2 份
- 数据资料 ≥ 1 份
- 社媒 / 舆论线索 ≥ 1 份

如果低于这个量级，后续蒸馏时要明确标注边界，避免把猜测写成定论。

---

## 快速使用流程

有了素材后，可以直接告诉 Claude Code：

```text
leao 的采访记录在 references/sources/transcripts/，
比赛笔记在 references/sources/matches/，
数据资料在 references/sources/data/，
请按 qiuyuan 的 8 路框架继续蒸馏。
```

这样主流程会更顺：
1. 先读本地素材
2. 再补公开信息
3. 进入 8 路研究
4. 生成 `09-cross-matrix.md`
5. 再做 Skill 提炼

---

## 配套脚本说明

### `collect_sources.py` — 采集入口脚本

用途：
- 创建标准目录
- 记录视频 / 数据 / 平台搜索结果摘要
- 给后续人工筛选提供起点

它更像“采集助手”，不是全自动爬虫。

### `download_subtitles.sh` — YouTube 字幕下载

用途：
- 优先尝试人工字幕
- 失败时回退到自动字幕

适用场景：
- 本地网络可访问 YouTube
- 只是想尽快拿到一版可清洗文本

### `srt_to_transcript.py` — 字幕清洗

用途：
- 去掉时间轴、序号、HTML 标签
- 合并有效文本
- 清洗成可读纯文本

### `merge_research.py` — 调研合并与检查点生成

用途：
- 统计 8 路报告覆盖情况
- 估算一手 / 二手来源命中
- 检查 `09-cross-matrix.md` 是否存在
- 输出进入提炼前的检查表

### `quality_check.py` — 交付前质量自检

用途：
- 检查生成的 `SKILL.md` 是否满足结构要求
- 重点看战术模型、禁区行为、身体边界、生态层、诚实边界、表达 DNA 等模块是否具备

它不是“真理判定器”，而是避免交付明显空心 Skill 的最后一道门。
