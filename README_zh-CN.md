<div align="center">

<img src="paper/assets/ai4gc-logo.png" alt="AI4GC Lab" height="72">

# Agentic Visual Generation
## A Survey

<p><strong>从单次渲染走向依赖运行时观察的视觉创作</strong></p>

<p>
  <a href="paper/paper.tex">阅读论文源码</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="paper/">浏览源码</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">English</a>
</p>

<p>
  <img src="https://img.shields.io/badge/status-living%20survey-2f855a?style=flat-square" alt="持续更新">
  <img src="https://img.shields.io/badge/source-LaTeX-2563eb?style=flat-square" alt="LaTeX 源码">
  <img src="https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square" alt="MIT 许可证">
</p>

<p>
  <a href="#一眼了解">项目概览</a>
  &nbsp;·&nbsp;
  <a href="#研究地图">研究地图</a>
  &nbsp;·&nbsp;
  <a href="#论文导航">章节导航</a>
  &nbsp;·&nbsp;
  <a href="#论文源码">源码</a>
  &nbsp;·&nbsp;
  <a href="#持续更新">参与维护</a>
</p>

</div>

<p align="center">
  <img src="paper/figures/ch3_components.jpg" alt="Agentic Visual Generation 六个核心组件" width="92%">
</p>

<p align="center"><em>以目标、记忆、工具、感知、行动和跨任务自我改进为核心的视觉创作闭环。</em></p>

> **项目快照 · 2026 年 8 月**
>
> 一个持续更新的视觉生成综述与公开 LaTeX 仓库，关注能够规划、调用工具、检查中间结果并调整行为的视觉创作系统。

## 最新进展

| 更新 | 内容 |
| --- | --- |
| **框架** | 用行为定义和五级自主性体系组织全文。 |
| **覆盖范围** | 当前覆盖图像、视频、3D/CAD、科学可视化、结构化文档、UI/Web、训练与评估。 |
| **仓库结构** | 保持源码目录紧凑，便于直接阅读、编译和扩展。 |

<p align="center">
  <a href="paper/paper.tex"><img src="https://img.shields.io/badge/阅读论文-111827?style=for-the-badge&logo=readme&logoColor=white" alt="阅读论文"></a>
  <a href="paper/sections/03_operating_loop.tex"><img src="https://img.shields.io/badge/查看框架-0f766e?style=for-the-badge&logo=diagram&logoColor=white" alt="查看框架"></a>
  <a href="paper/references.bib"><img src="https://img.shields.io/badge/浏览-BibTeX-2563eb?style=for-the-badge&logo=academia&logoColor=white" alt="浏览 BibTeX"></a>
</p>

<details>
<summary><strong>内容速览</strong></summary>

- [项目概览](#一眼了解)
- [研究地图](#研究地图)
- [本文提供什么](#本文提供什么)
- [论文导航](#论文导航)
- [论文源码](#论文源码)
- [编译](#编译)
- [持续更新](#持续更新)

</details>

## 一眼了解

当运行时证据会改变后续视觉创作动作时，视觉生成过程具有 **agentic** 特征。证据可以来自不断演化的视觉产物、执行环境、验证器或交互历史；动作可以是修改提示词、选择工具、修复局部区域、重新规划流程或停止执行。

本文建立统一框架，覆盖以下视觉创作对象：

<table>
  <tr>
    <td align="center"><strong>图像</strong><br>生成 · 编辑 · 修复</td>
    <td align="center"><strong>视频</strong><br>叙事 · 动画 · 编辑</td>
    <td align="center"><strong>3D</strong><br>CAD · 资产 · 世界</td>
  </tr>
  <tr>
    <td align="center"><strong>可视化</strong><br>图表 · 科学图形</td>
    <td align="center"><strong>结构化文档</strong><br>幻灯片 · 布局 · 报告</td>
    <td align="center"><strong>交互界面</strong><br>UI · Web · 交互系统</td>
  </tr>
</table>

## 研究地图

<p align="center">
  <img src="paper/figures/avg_literature_autonomy.png" alt="文献增长、领域覆盖与自主性" width="92%">
</p>

本文从三个层次组织研究：

| 层次 | 核心问题 | 对应章节 |
| --- | --- | --- |
| **运行闭环** | 视觉 Agent 如何决定和执行？ | 第 1–3 章 |
| **创作领域** | 它可以创作哪些视觉产物？ | 第 4–10 章 |
| **学习与证据** | 它如何改进，又应如何评估？ | 第 11–12 章与前沿章节 |

<p align="center">
  <img src="paper/figures/avg_autonomy_staircase.jpg" alt="五级自主性阶梯" width="92%">
</p>

<p align="center"><em>自主性从固定生成逐步扩展到反馈适应、长时程控制和持续自我改进。</em></p>

<details>
<summary><strong>框架一览</strong></summary>

| 层次 | 范围 |
| --- | --- |
| **行为** | 基于观察调整动作，可以修订、分支、验证或终止视觉创作过程 |
| **自主性** | L1 固定执行 → L2 反馈适应 → L3 工具与流程控制 → L4 长时程运行 → L5 跨任务改进 |
| **组件** | 目标与规划 · 记忆 · 工具 · 感知 · 行动 · 跨任务自我改进 |
| **领域** | 图像 · 视频与动画 · 3D/CAD/世界 · 科学可视化 · 结构化文档 · UI/Web |

</details>

## 本文提供什么

- **行为定义：** 用观察–行动依赖关系识别 agentic 行为。
- **五级自主性：** 用 L1–L5 区分固定执行到持续适应的不同程度。
- **六组件框架：** 目标与规划、记忆、工具、感知、行动、跨任务自我改进。
- **跨领域比较：** 统一比较图像、视频、3D、可视化、文档和 UI/Web 系统。
- **评估视角：** 覆盖产物质量、目标与约束满足、轨迹与决策质量，以及系统和以人为中心的结果。

## 论文导航

| 章节 | 内容 |
| --- | --- |
| [01 · Introduction](paper/sections/01_introduction.tex) | 范围、动机与综述结构 |
| [02 · Foundations](paper/sections/02_foundations.tex) | 视觉生成器、多模态、结构化表示与自主性 |
| [03 · Operating Loop](paper/sections/03_operating_loop.tex) | 规划、记忆、工具、感知、行动与改进 |
| [04 · Image Generation](paper/sections/04_image_generation.tex) | 图像生成与编辑 Agent |
| [05 · Video & Animation](paper/sections/05_video_animation.tex) | 长视频、动画与时间控制 |
| [06 · 3D, CAD & Worlds](paper/sections/06_3d_cad_world.tex) | 结构化资产、可执行 CAD 与世界模型 |
| [07 · Scientific Visualization](paper/sections/07_scientific_visualization.tex) | 数据驱动的视觉分析与图形生成 |
| [08 · Structured Documents](paper/sections/08_structured_documents.tex) | 幻灯片、文档、布局与渲染反馈 |
| [09 · UI & Web](paper/sections/09_ui_web.tex) | 界面和网页生成 |
| [10 · Cross-Domain Systems](paper/sections/10_cross_domain.tex) | 跨视觉创作领域的综合系统 |
| [11 · Training](paper/sections/11_training.tex) | 轨迹监督、强化学习与适应 |
| [12 · Evaluation](paper/sections/12_evaluation.tex) | Benchmark、可靠性、安全性与人因 |
| [Frontiers](paper/sections/06_frontiers.tex) | 开放问题与研究方向 |

## 论文源码

[`paper/`](paper/) 是公开、可编译的论文源码目录：

```text
paper/
├── paper.tex                 # 主入口
├── sections/                 # 各章正文
├── figures/                  # 正文使用的图
├── references.bib            # 参考文献
├── agentic_visual_generation.cls # 本地文档类
└── assets/                   # 字体与标识
```

公开仓库保持聚焦：只保留论文源码及其编译所需依赖，不包含生成的构建产物和私人工作文件。

## 编译

在 `paper/` 目录执行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error paper.tex
```

使用 Overleaf 时，上传 [`paper/`](paper/) 的全部内容，并将 `paper.tex` 设置为主文档。

## 持续更新

本文将作为持续维护的研究项目，更新内容包括：

- 核实新的论文和项目；
- 调整领域覆盖范围和分类体系；
- 更新图表和形式化定义；
- 修正 BibTeX 与正式发表信息；
- 更新公开项目索引。

建议使用一手来源提交更新，并在 issue 或 pull request 中记录涉及章节、来源链接和修改内容。

### 更新检查清单

| 提交更新前 | 检查内容 |
| --- | --- |
| 新论文或项目 | 添加一手来源和稳定的 BibTeX 条目 |
| 新图或新表 | 核对图注、来源署名和本地路径 |
| 正文修改 | 保持框架术语与章节范围一致 |
| 版本发布 | 编译 `paper/paper.tex`，并从公开目录移除生成产物 |

## 引用

作者、投稿信息和公开版本确定后，将补充正式引用记录。

## 许可证

代码和 LaTeX 源码采用 [MIT License](paper/LICENSE)。使用论文中的具体图片时，请同时核对论文正文及其引用文献中的署名和再使用条件。
