<div align="center">

<img src="assets/ai4gc-logo.png" alt="AI4GC Lab" height="72">

# Agentic Visual Generation
## A Survey

<p><strong>From single-pass rendering to observation-dependent visual creation</strong></p>

<p>
  <a href="https://www.zju.edu.cn/english/">Zhejiang University</a> ·
  <a href="https://ai4gc.org/">AI4GC Lab</a>
</p>

<p>
  <strong>Zihan Xing</strong><sup>1,*+</sup> ·
  <strong>Jin Wang</strong><sup>1,*</sup> ·
  <strong>Rong Xia</strong><sup>1,*</sup> ·
  <strong>Keming Ye</strong><sup>1,5</sup> ·
  <strong>Zhan Qu</strong><sup>1,5</sup> ·
  <strong>Biao Yi</strong><sup>1,5</sup> ·
  <strong>Tianqi Liu</strong><sup>1,5</sup> ·
  <strong>Junhao Chen</strong><sup>1,5</sup> ·
  <strong>Jie Yang</strong><sup>1,5</sup> ·
  <strong>Zhibo Zhu</strong><sup>1,5</sup> ·
  <strong>Zhouzhou Shen</strong><sup>1,5</sup> ·
  <strong>Honghui Sheng</strong><sup>1,5</sup> ·
  <strong>Yurun Chen</strong><sup>1,5</sup> ·
  <strong>Yuqing Zhang</strong><sup>1,5</sup> ·
  <strong>Shuanghe Zhu</strong><sup>1,5</sup> ·
  <strong>Wenkai Wang</strong><sup>1,5</sup> ·
  <strong>Tao Xiong</strong><sup>1,5</sup> ·
  <strong>Kuncheng Lin</strong><sup>1,5</sup> ·
  <strong>Qihang Yu</strong><sup>1,5</sup> ·
  <strong>Kui Chen</strong><sup>1,5</sup> ·
  <strong>Yufan Xiong</strong><sup>1,5</sup> ·
  <strong>Juncheng Li</strong><sup>5</sup> ·
  <strong>Wenqiao Zhang</strong><sup>5</sup> ·
  <strong>Zheqi Lv</strong><sup>3</sup> ·
  <strong>Chengxi Zang</strong><sup>3</sup> ·
  <strong>Long Chen</strong><sup>2</sup> ·
  <strong>Zhou Zhao</strong><sup>4</sup> ·
  <strong>Shengyu Zhang</strong><sup>1,5,#</sup> ·
  <strong>Fei Wu</strong><sup>4,#</sup>
</p>

<p><sup>1</sup> AI4GC Lab, Zhejiang University · <sup>2</sup> Hong Kong University of Science and Technology · <sup>3</sup> Cornell University · <sup>4</sup> College of Artificial Intelligence, Zhejiang University · <sup>5</sup> School of Software Technology, Zhejiang University</p>

<p>
  <a href="PAPERS.md#browse-by-field">Browse the paper index</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="references.bib">BibTeX records</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README_zh-CN.md">中文说明</a>
</p>

<p>
  <img src="https://img.shields.io/badge/status-living%20survey-2f855a?style=flat-square" alt="Living survey">
  <img src="https://img.shields.io/badge/source-curated%20index-2563eb?style=flat-square" alt="Curated index">
  <img src="https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square" alt="MIT license">
</p>

<p>
  <a href="https://ai4gc.org/">Lab</a>
  &nbsp;·&nbsp;
  <a href="https://www.zju.edu.cn/english/">Institution</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/xzhxjc/Agentic-Visual-Generation-A-Survey">Repository</a>
</p>

<p>
  <a href="#at-a-glance">Overview</a>
  &nbsp;·&nbsp;
  <a href="PAPERS.md#browse-by-field">Field Index</a>
  &nbsp;·&nbsp;
  <a href="#research-map">Research Map</a>
  &nbsp;·&nbsp;
  <a href="#survey-structure">Chapters</a>
  &nbsp;·&nbsp;
  <a href="#public-contents">Contents</a>
  &nbsp;·&nbsp;
  <a href="#living-survey">Contribute</a>
</p>

</div>

<p align="center">
  <img src="assets/ch3_components.jpg" alt="Six components of agentic visual generation" width="92%">
</p>

<p align="center"><em>Agentic visual generation organized as a closed loop over goals, memory, tools, perception, action, and cross-task improvement.</em></p>

<p align="center">
  <table>
    <tr>
      <td align="center"><strong>389</strong><br>records</td>
      <td align="center"><strong>12</strong><br>chapters</td>
      <td align="center"><strong>6</strong><br>components</td>
      <td align="center"><strong>5</strong><br>autonomy levels</td>
    </tr>
  </table>
</p>

> **Project snapshot · September 2, 2026**
>
> A living survey and public paper index for visual creation systems that plan, use tools, inspect intermediate results, and revise their behavior.

## News

| Date | Update |
| --- | --- |
| **2026-09-02** | Reorganized all 389 bibliography records into a field-first, collapsible index with complete metadata and direct links. |
| **2026-08-30** | Reorganized the repository homepage around taxonomy, paper discovery, and field navigation. |
| **Ongoing** | Metadata, publication status, figures, and chapter coverage are being checked against primary sources. |

<p align="center">
  <a href="PAPERS.md"><img src="https://img.shields.io/badge/Explore%20paper%20index-111827?style=for-the-badge&logo=readme&logoColor=white" alt="Explore paper index"></a>
  <a href="references.bib"><img src="https://img.shields.io/badge/Browse-BibTeX-2563eb?style=for-the-badge&logo=academia&logoColor=white" alt="Browse BibTeX"></a>
</p>

<details>
<summary><strong>Contents at a glance</strong></summary>

- [Overview](#at-a-glance)
- [News](#news)
- [Paper Collection](#paper-collection)
- [Field Index](PAPERS.md#browse-by-field)
- [Research Map](#research-map)
- [What the Survey Adds](#what-the-survey-adds)
- [Public Contents](#public-contents)
- [Living Survey](#living-survey)

</details>

## Paper Collection

The survey currently tracks **389 BibTeX records**. The homepage is organized by research field; publication year is retained in each field table as the `Date` column and used for within-field sorting.

| Field | Chapters | Records | Years |
| --- | --- | ---: | --- |
| [Foundations & Agentic Methods](PAPERS.md#foundations-methods) | 1-3, 11-12 | 33 | 2014-2026 |
| [Image Generation & Editing](PAPERS.md#image-generation) | 4 | 127 | 2016-2026 |
| [Video & Animation](PAPERS.md#video-animation) | 5 | 73 | 2018-2026 |
| [3D / CAD / World](PAPERS.md#three-d-cad-world) | 6 | 59 | 2015-2026 |
| [Scientific Visualization](PAPERS.md#scientific-visualization) | 7 | 31 | 2019-2026 |
| [Structured Documents & Diagrams](PAPERS.md#structured-documents) | 8 | 38 | 2014-2026 |
| [UI / Web Creation](PAPERS.md#ui-web) | 9 | 20 | 2001-2026 |
| [Cross-Domain Applications](PAPERS.md#cross-domain-applications) | 10 | 8 | 2025-2026 |

> Every field can be expanded or collapsed. Expanded tables provide the complete paper title, full author list, date, venue, volume/issue/pages when available, paper/DOI/project links, and BibTeX key.

Detailed index: [`PAPERS.md`](PAPERS.md) · Machine-readable metadata: [`references.bib`](references.bib)

## At A Glance

Visual generation becomes **agentic** when runtime evidence changes a later creation action. The evidence may come from the evolving artifact, an execution environment, a verifier, or the interaction history; the action may revise a prompt, select a tool, repair a region, re-plan a workflow, or stop.

This survey builds a common vocabulary for systems that create and edit:

<table>
  <tr>
    <td align="center"><strong>Images</strong><br>generation · editing · restoration</td>
    <td align="center"><strong>Video</strong><br>storytelling · animation · editing</td>
    <td align="center"><strong>3D</strong><br>CAD · assets · worlds</td>
  </tr>
  <tr>
    <td align="center"><strong>Visual Analytics</strong><br>charts · scientific figures</td>
    <td align="center"><strong>Documents</strong><br>slides · layouts · reports</td>
    <td align="center"><strong>Interfaces</strong><br>UI · Web · interactive systems</td>
  </tr>
</table>

## Research Map

<p align="center">
  <img src="assets/avg_literature_autonomy.png" alt="Survey literature growth, domain coverage, and autonomy" width="92%">
</p>

The paper connects five views of the field:

| View | Question | Chapters |
| --- | --- | --- |
| **Operating loop** | How does a visual agent decide and act? | 1–3 |
| **Creation domains** | What kinds of artifacts can it create? | 4–10 |
| **Training** | How are visual agents trained and adapted? | 11 |
| **Evaluation** | How should artifacts, decisions, and systems be evaluated? | 12 |
| **Frontiers** | What research directions remain open? | Frontiers |

<p align="center">
  <img src="assets/avg_autonomy_staircase.jpg" alt="Five-level autonomy scale" width="92%">
</p>

<p align="center"><em>The autonomy scale moves from fixed generation toward feedback adaptation, long-horizon control, and continual self-improvement.</em></p>

<details>
<summary><strong>Framework in one view</strong></summary>

| Layer | Scope |
| --- | --- |
| **Behavior** | Observation-dependent actions that can revise, branch, verify, or stop a visual creation process |
| **Autonomy** | L1 fixed execution → L2 feedback adaptation → L3 tool and workflow control → L4 long-horizon operation → L5 cross-task improvement |
| **Components** | Goals and planning · memory · tools · perception · action · cross-task self-improvement |
| **Domains** | Images · video and animation · 3D/CAD/worlds · scientific visualization · structured documents · UI/Web |

</details>

## What The Survey Adds

- **A behavioral definition:** agentic behavior is identified by an observation–action dependency.
- **A five-level autonomy scale:** L1–L5 separates fixed execution from increasingly adaptive visual creation.
- **A six-component framework:** goals and planning, memory, tools, perception, action, and cross-task self-improvement.
- **A cross-domain view:** the same control questions are compared across image, video, 3D, visualization, document, and UI/Web systems.
- **An evaluation lens:** artifact quality, goal and constraint satisfaction, trajectory and decision quality, and system or human-centered outcomes.

## Public Contents

| File | Purpose |
| --- | --- |
| [`PAPERS.md`](PAPERS.md) | Field-organized paper index with complete metadata and direct links |
| [`references.bib`](references.bib) | Machine-readable bibliography for the tracked records |
| [`assets/`](assets/) | Images used by the project homepage |

## Living Survey

The survey is maintained as a continuing research project. Updates may include:

- newly verified papers and projects;
- changes to domain coverage or taxonomy;
- revised figures, tables, and formal definitions;
- corrections to BibTeX and publication metadata;
- updates to the public project index.

Please use primary sources when proposing an update and record the affected section, source link, and change in the pull request or issue.

### Contribution Checklist

| Before opening an update | Check |
| --- | --- |
| New paper or project | Add a primary source and a stable BibTeX record |
| New figure or table | Confirm the caption, source attribution, and public link |
| Textual revision | Keep terminology consistent with the framework and chapter scope |
| Release update | Refresh `PAPERS.md`, validate links, and remove generated artifacts |

## Citation

The citable release record will be added after the author list, venue, and public version are finalized.

## License

Project materials are released under the [MIT License](LICENSE). Please check each cited work for figure-specific attribution and reuse conditions.
