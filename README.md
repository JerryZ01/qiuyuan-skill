<div align="center">

# qiuyuan-skill

> *「足球是空间的博弈，谁制造空间、谁利用空间，谁就赢。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**输入任意球员名，自动深度调研8路信息 → 提炼战术框架 → 生成可运行的球员视角 Skill。**

<br>

不是复刻集锦，是提炼**他踢球的思维操作系统**。

[效果示例](#效果示例) · [安装](#安装) · [8路采集框架](#8路采集框架) · [诚实边界](#诚实边界)

</div>

---

## 效果示例



这不是角色扮演。每个回答都基于8路调研提炼的**战术模型 + 表达DNA**——捕捉的是他怎么踢球，不是他说了什么。

---

## 安装


[38;5;250m███████╗██╗  ██╗██╗██╗     ██╗     ███████╗[0m
[38;5;248m██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝[0m
[38;5;245m███████╗█████╔╝ ██║██║     ██║     ███████╗[0m
[38;5;243m╚════██║██╔═██╗ ██║██║     ██║     ╚════██║[0m
[38;5;240m███████║██║  ██╗██║███████╗███████╗███████║[0m
[38;5;238m╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝[0m

┌   skills 
│
│  Tip: use the --yes (-y) and --global (-g) flags to install without prompts.
[?25l│
◇  Source: https://github.com/JerryZ01/qiuyuan-skill.git
[?25h[?25l│
◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository...[999D[J◑  Cloning repository...[999D[J◒  Cloning repository...[999D[J◐  Cloning repository...[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository[999D[J◑  Cloning repository[999D[J◒  Cloning repository[999D[J◐  Cloning repository[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository.[999D[J◑  Cloning repository.[999D[J◒  Cloning repository.[999D[J◐  Cloning repository.[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..[999D[J◒  Cloning repository..[999D[J◐  Cloning repository..[999D[J◓  Cloning repository..[999D[J◑  Cloning repository..│
■  Failed to clone repository
│
│  Clone timed out after 60s. This often happens with private repos that require authentication.
│
│    Ensure you have access and your SSH keys or credentials are configured:
│
│    - For SSH: ssh-add -l (to check loaded keys)
│
│    - For HTTPS: gh auth status (if using GitHub CLI)
│
└  Installation failed

[999D[J■  Canceled
[?25h

然后在 Claude Code 里触发：



---

## 8路采集框架

球员是社会中人，也是场上决策者。采集分三层：



**踢球层**回答"他怎么踢的"——空间决策、技术选择、身体边界、体系统治力。**生态层**回答"他现在处于什么环境"——舆论标签 vs 真实表现、场下争议处理方式。**背景层**回答"他为什么会这样"——关键时刻表现、生涯演变轨迹。

核心设计：**Phase 1.4 跨维度交叉阅读**。每路 Agent 读其他7路报告，寻找印证、矛盾、涌现，发现球员多条因果链，而非孤立事实。

---

## 诚实边界

**这个Skill能做的：**
- 用球员的战术框架分析比赛和球员对比
- 模拟他特有的说话方式和决策逻辑
- 基于身体条件推导他的踢法边界

**做不到的：**

| 维度 | 说明 |
|------|------|
| 最新动态 | 联网受限，转会/伤病等最新信息可能有缺漏 |
| 替代本人 | 他的当下状态、私下性格无法被复制 |
| 低知名度球员 | 公开信息不足时，生成的Skill质量会受限 |
| 完全客观 | 所有提炼都是主观判断，保留矛盾点不强制调和 |

**一个不告诉你局限在哪的Skill，不值得信任。**

---

## 仓库结构



---

## 关于作者

GitHub: [JerryZ01](https://github.com/JerryZ01)

---

## 许可证

MIT — 随便用，随便改，随便蒸馏。

---

<div align="center">

**集锦** 告诉你他进过什么球。<br>
**qiuyuan-skill** 帮你用他的方式看比赛。<br><br>
*足球是空间的博弈。*

<br>

MIT License © [JerryZ01](https://github.com/JerryZ01)

</div>
