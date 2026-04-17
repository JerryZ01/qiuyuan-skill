# 球探 · 球员信息来源采集指南

> ⚠️ **网络环境说明**：WSL2 下 YouTube/B站/API 部分平台存在访问限制，
> 建议在 **Windows 浏览器** 或配置 **VPN/代理** 后使用。
> 脚本负责组织结构和处理已下载的文件。

---

## 信息来源优先级（足球领域）

| 优先级 | 来源 | 类型 | 覆盖维度 |
|--------|------|------|---------|
| 🥇 最高 | 球员本人采访字幕 | 视频字幕 | 表达DNA、战术哲学 |
| 🥈 高 | 比赛解说/高光字幕 | 视频字幕 | 场景决策、技术动作 |
| 🥉 中 | 球员社交媒体 | 文本/图片 | 表达风格、公众形象 |
| 📊 低 | 数据平台（FBref/Wyscout） | 统计数据 | 数据画像、能力边界 |
| 📰 辅助 | 专业媒体（The Athletic等） | 文章 | 外部视角、生涯轨迹 |

---

## 快速采集流程

### Step 1: 创建球员目录

```bash
# 在 skill 目录下创建球员专属目录
mkdir -p ~/.claude/skills/qiuyuan.skill/references/sources/梅西
cd ~/.claude/skills/qiuyuan.skill/references/sources/梅西

# 子目录结构
mkdir -p transcripts/ interviews/ matches/ social/ data/
```

### Step 2: 获取采访/高光视频 → 字幕

**方式A: YouTube（推荐）**

在 Windows 浏览器打开 YouTube，搜索：
- `梅西 球员 采访`
- `Messi interview tactics`
- `梅西 全场 比赛 高光`

下载字幕（任意方式）：
```
# 推荐：yt-dlp（WSL2 下需代理）
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890

yt-dlp --write-subs --write-auto-subs \
  --sub-langs "zh-Hans,zh-Hant,zh,en" \
  --convert-subs srt \
  --output "./%(title)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

**方式B: B站（B站有大量足球内容）**

1. 打开 B站，搜索球员采访/战术分析视频
2. 用 **B站下载器**（Downkyi/唧唧）下载，导出字幕
3. 将 `.srt` 文件复制到 `transcripts/` 目录

### Step 3: 清洗字幕 → 纯文本

```bash
python3 ~/.claude/skills/qiuyuan.skill/scripts/srt_to_transcript.py \
  ./梅西采访.srt \
  ./梅西采访_清洗.txt
```

### Step 4: 采集数据（手动）

访问以下公开数据网站：

| 网站 | 内容 | 访问方式 |
|------|------|---------|
| FBref | 进球/传球/防守数据 | https://fbref.com 搜索球员 |
| Transfermarkt | 转会/身价/履历 | https://transfermarkt.com 搜索球员 |
| SofaScore | 场均数据/热力图 | https://sofascore.com 搜索球员 |
| Opta | 战术数据/对抗数据 | The Athletic 等媒体引用 |

### Step 5: 采集社交媒体

| 平台 | 球员账号 | 内容 |
|------|---------|------|
| Instagram | @leomessi 等 | 日常、赛后感言 |
| Twitter/X | @teammessi 等 | 即时反应、观点 |
| 微博 | 球员官方账号 | 中文受众内容 |

---

## 快速检查清单

```
references/sources/球员名/
├── transcripts/           ← 视频字幕（.srt 或 .txt）
│   ├── 2022世界杯采访.txt
│   └── 巴萨更衣室采访.srt
├── interviews/            ← 文字采访记录
│   └── the-athletic-2023.txt
├── matches/               ← 比赛分析片段
│   └── 2022世界杯决赛分析.srt
├── social/                ← 社交媒体内容
│   └── 世界杯夺冠instagram.txt
└── data/                  ← 统计数据截图/导出
    ├── fbref_2024.txt
    └── transfermarkt_profile.txt
```

---

## 快速使用流程（Claude Code 里）

有了素材后，直接告诉 Claude Code：

```
"梅西的采访记录在 ./transcripts/ 目录下，
数据在 ./data/ 目录下，
帮我蒸馏梅西的球员Skill"
```

Claude Code 会读取这些素材，按 qiuyuan.skill 的框架生成球员 Skill。


## 配套脚本说明

### merge_research.py — 调研合并 + Phase 1.5 生成



自动扫描 ，统计：
- 每路Agent的来源数量（一手/二手）
- 跨维度矩阵是否已生成
- 矛盾点数量
- 输出 Phase 1.5 质量检查点表格

### quality_check.py — SKILL.md 质量自检



在交付前执行，逐项检查：
- 战术模型数量（3-7个）
- 禁区行为（≥3条）
- 身体极限边界
- 生态背景覆盖
- 诚实边界（≥3条）
- 身份卡存在性
- AI模板味检测
- 跨维度发现覆盖

