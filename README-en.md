<div align="center">

# qiuyuan-skill

> *"Football is a game of space: whoever creates space and whoever uses it better, wins."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude%20Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Enter any player's name, run 8-way parallel research in Claude Code, distill tactical patterns, and generate a runnable player-perspective Skill.**

<br>

This is not highlight-reel imitation.
It is a distillation of **the player's footballing operating system**.

[Preview](#preview) · [Install](#install) · [System Architecture](#system-architecture) · [8-Track Research Framework](#8-track-research-framework) · [Honest Boundaries](#honest-boundaries)

</div>

---

## Preview

After distillation, load the generated player Skill in Claude Code. The interaction is meant to feel closer to a CLI interface like this:

```bash
╭─ Claude Code · leao-perspective.skill ───────────────────────────────╮
│ mode: chat   model: claude   skill: loaded                           │
╰───────────────────────────────────────────────────────────────────────╯

$ leao, against Inter, if their fullback pushes high, what do you do?

> Easy. My first thought is to attack the space behind him,
> but not by just running the touchline — I cut inside.
> The moment he steps up, the space behind is there.
>
> Honestly, in Serie A there are not many fullbacks who can match me for speed,
> but Inter are different, they have legs.
> So I read the timing: before he fully commits,
> I raise the tempo first.

────────────────────────────────────────────────────────────────────────

$ What is the biggest difference between you and mbappe?

> He is fast, really fast. In pure top speed, I do not beat him.
> He is straight-line acceleration. I am more about change of direction.
>
> But inside the box, one-on-one, I am calmer.
> My body helps me hold off defenders.
> Against very strong defenders, he can suffer more.
>
> Who is better? I do not judge that.
> His game does not need teammates to create width for him.
> Mine does.

────────────────────────────────────────────────────────────────────────

$ What was the toughest match you ever played?

> Away at Tottenham in 2022.
> I had gastro problems that day and threw up twice before kickoff.
> The medical staff asked if I could play. I said yes.
>
> For the first 60 minutes I was basically walking.
> When the ball came to me, I did not want to drive with it.
> But once they equalized, I woke up.
> If you do not let me breathe, I do not let you breathe either.
>
> Sometimes when your body is not right,
> your technique becomes cleaner.
> You stop overthinking. Your body decides for you.
```

This is not roleplay for its own sake. Every answer is built from **tactical models + expression DNA** distilled through 8-track research. What gets captured is **how the player plays**, not just **what the player once said**.

---

## Install

```bash
npx skills add JerryZ01/qiuyuan-skill
```

Then trigger it in Claude Code:

```text
> distill leao
> analyze how haaland plays
> make a tactical perspective for leao
> analyze this match from mbappe's perspective
```

---

## System Architecture

```text
                        ┌──────────────────────────────────────┐
                        │        Phase 0 · Entry Routing        │
                        │                                      │
                        │  “distill leao” → Phase 0A Clarify   │
                        │  “I need a...” → Phase 0B Recommend  │
                        └──────────────────┬───────────────────┘
                                           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                 Phase 1 · 8-Track Parallel Research                          │
│                                                                              │
│  Playing Layer (core)      Context Layer          Background Layer           │
│  ┌────────────┐           ┌────────────┐         ┌────────────┐              │
│  │① Space     │           │⑤ Media     │         │⑦ Big Moments│             │
│  │② Decisions │           │⑥ Social    │         │⑧ Career Arc │             │
│  │③ Physical  │           └────────────┘         └────────────┘              │
│  │④ System    │                                                     ╲        │
│  └────────────┘                                                      ╲       │
└───────────────────────────────────────────────────────────────────────╲──────┘
                                                                        ╲
┌────────────────────────────────────────────────────────────────────────────┐
│                 Phase 2 · Cross-Dimensional Matrix ← core design          │
│                                                                            │
│   Main session reads all 8 reports and looks for connections:             │
│                                                                            │
│   ① Space ↔ ② Decision Library ↔ ③ Physical Limits                        │
│        ↕             ↕                    ↕                                │
│   ⑤ Media ↔ ④ System Fit ↔ ⑧ Career Arc                                    │
│        ↕             ↕                                                     │
│   ⑥ Social Dynamics ↔ ⑦ Key Moments                                        │
│                                                                            │
│   Three connection types: confirmation / contradiction / emergence         │
│                                                                            │
│   Output: 09-cross-matrix.md (generated by the main session)              │
└────────────────────────────────────────────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                    Phase 3 · Distillation and Review                       │
│                                                                            │
│   ┌────────────┐ ┌────────────┐ ┌──────────────┐ ┌──────────┐ ┌──────────┐ │
│   │Tactical    │ │Scenario     │ │Physical       │ │Context    │ │Anti-      │ │
│   │Models      │ │Decision Lib │ │Boundaries     │ │Background │ │patterns   │ │
│   │3-5 items   │ │5-8 items    │ │5 dimensions   │ │media+team │ │negative   │ │
│   └────────────┘ └────────────┘ └──────────────┘ └──────────┘ └──────────┘ │
│                       + Expression DNA + Honest Boundaries                 │
└────────────────────────────────────────────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                      Phase 4 · Skill Construction                          │
│                                                                            │
│   Generate a runnable SKILL.md containing:                                │
│   ⚡ role rules · answer workflow · tactical models · scenario library    │
└────────────────────────────────────────────────────────────────────────────┘
                   │
                   ▼
                 ✅ Delivery
```

The most important step is not "more searching" but the **Phase 2 cross-dimensional matrix**.
A valid conclusion should, as much as possible, be supported across tactical, contextual, and background layers — or preserve the contradiction explicitly instead of flattening it away.

---

## 8-Track Research Framework

A footballer is both a decision-maker on the pitch and a person inside a larger environment. Research is split into three layers:

| Layer | Dimensions | Purpose |
|:------|:-----------|:--------|
| **Playing Layer** | ① Space ② Decision Library ③ Physical Limits ④ System Fit | The core: how he plays |
| **Context Layer** | ⑤ Media Narrative ⑥ Social Dynamics | The environment: what situation he is inside |
| **Background Layer** | ⑦ Key Moments ⑧ Career Arc | The backstory: why he became this player |

The **playing layer** answers *how he plays* — space usage, technical choices, physical boundaries, and system influence.  
The **context layer** answers *what environment he currently lives in* — public labels versus reality, off-pitch pressure, controversy response.  
The **background layer** answers *why he became this version of himself* — defining moments and evolution over time.

Core design: **Phase 2 Cross-Dimensional Matrix**. Once the 8 reports are done, the main session reads them together and produces `09-cross-matrix.md`. The goal is to identify confirmations, contradictions, and emergent patterns — not just pile up isolated facts.

---

## Honest Boundaries

**What this Skill can do:**
- Analyze matches and player comparisons through the player's tactical framework
- Simulate his characteristic speaking style and decision logic
- Infer the limits of his game from physical and contextual constraints

**What it cannot do:**

| Dimension | Explanation |
|----------|-------------|
| Latest updates | Network limitations may leave gaps around transfers, injuries, or recent events |
| Replace the real person | His exact current state and private personality cannot be reproduced |
| Obscure players | If public information is too thin, the generated Skill quality will drop |
| Be fully objective | Every distillation is interpretive; contradictions should be preserved, not force-resolved |

**A Skill that hides its limits is a Skill you should not trust.**

---

## Repository Structure

```text
qiuyuan-skill/
├── SKILL.md                  # Main distillation workflow entry for Claude Code
├── README.md                 # Chinese project overview
├── README-en.md              # English project overview
├── LICENSE                   # MIT license
└── scripts/
    ├── download_subtitles.sh # YouTube subtitle downloader
    ├── srt_to_transcript.py  # Subtitle cleaner (SRT → plain text)
    ├── collect_sources.py    # Player source and metadata collection helper
    ├── merge_research.py     # Research merge + quality checkpoint generator
    ├── quality_check.py      # Pre-delivery quality checker
    └── MANUAL_COLLECTION.md  # Collection guide
```

Note: `references/` is **not** a permanent directory shipped with this repository. It is generated inside each target player Skill directory during distillation, for example:

```text
~/.claude/skills/leao-perspective.skill/
├── SKILL.md
├── references/
│   ├── research/
│   └── sources/
└── scripts/
```

This keeps the repository focused on **methodology + tools**, while actual player outputs live inside their own target Skill directories.

---

## Author

GitHub: [JerryZ01](https://github.com/JerryZ01)

---

<div align="center">

**Highlights** tell you what goals he scored.  
**qiuyuan-skill** helps you watch the game the way he does.

*Football is a game of space.*

MIT License &copy; [JerryZ01](https://github.com/JerryZ01)

</div>
