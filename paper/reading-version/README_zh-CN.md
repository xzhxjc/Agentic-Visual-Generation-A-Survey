# HUST arXiv 模板

一个面向华中科技大学（HUST）的非官方 LaTeX arXiv 论文与技术报告模板。主题色采用 HUST 蓝 `#004B84`、HUST 红 `#D20B17` 和灰色 `#575757`。

## 快速开始

在项目根目录执行：

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

编译结果为 `paper.pdf`。正式使用前，请替换标题、作者、单位、摘要、链接、图片和章节中的占位文本。

## 单栏与双栏

默认使用单栏：

```tex
\documentclass[]{hust}
```

如果需要双栏正文，将 `paper.tex` 开头改为：

```tex
\documentclass[twocolumn]{hust}
```

双栏模式下，标题、作者信息、摘要、Paper Overview 和 Contents 保持跨栏；正文从 `Introduction` 开始分为双栏。

## 作者信息

在 `paper.tex` 中修改作者元信息：

```tex
\author[1]{First Author}
\affiliation[1]{School of XXX, Huazhong University of Science and Technology}
\email{who1@hust.edu.cn}
\contribution{\textsuperscript{*} Equal Contribution}
\correspondence{who1@hust.edu.cn}
```

多个单位会分别占一行。每位作者可以添加一个 `\email{...}`。

## Logo 与图片

默认使用简化版 Logo：`assets/hust-logo2.pdf`。如需完整校徽，在 `paper.tex` 中取消以下注释：

```tex
\renewcommand{\hustlogo}{assets/hust-logo1.pdf}
\renewcommand{\hustlogowidth}{24mm}
```

正文示例图片已经替换为 LaTeX 绘制的占位框，以避免打包示例照片。添加自己的图片时，将 `paper.tex` 或 `sections/` 中的 `\templatefigure{...}` 替换为：

```tex
\includegraphics[width=0.9\linewidth]{path/to/your-figure.pdf}
```

请确保图片具有合适的使用授权。

## 表格、算法与参考文献

表格使用 `booktabs` 三线表风格；伪代码使用 `algorithm` 和 `algpseudocode`。参考文献采用数字型 IEEE 格式：

```tex
\cite{sample_reference}
```

```tex
\bibliographystyle{IEEEtran}
\bibliography{main}
```

## 目录结构

- `paper.tex`：主文档入口和论文元信息。
- `hust.cls`：主题色、版式、标题块、作者信息和页面样式。
- `sections/`：论文各章节及示例。
- `assets/`：字体、Logo、图标和其他资源。
- `main.bib`：BibTeX 参考文献数据库。
- `LICENSE`：MIT 许可证。

## 版权与致谢

Copyright (c) 2026 HUST arXiv Template contributors.

本项目是非官方社区模板，与华中科技大学不存在隶属、授权或赞助关系。项目基于 [choucisan/arXiv-Template](https://github.com/choucisan/arXiv-Template) 改编，模板设计参考 ByteDance Seed。字体、Logo 和其他第三方资源可能受其各自许可条款约束，请在发布和再分发前单独确认。
