# Agentic Visual Generation: A Survey

[English README](README.md)

本仓库仅包含综述论文 **Agentic Visual Generation: A Survey** 的当前可编译源码。

本文关注这样一类视觉创作系统：运行时对正在演化的视觉产物、任务环境或交互历史的观察，会改变之后的视觉创作决策。

> 实用判据：若运行时证据会改变后续视觉创作动作，该过程就是 agentic 的。

## 论文源码

所有必要文件均位于 [`paper/`](paper/)：

```text
paper.tex              # 主入口
sections/              # 各章正文
figures/               # 正文实际引用的图片与 TikZ 图源
references.bib         # 参考文献
hust.cls, assets/      # 排版、字体与标识依赖
```

内容覆盖图像生成与编辑、视频与动画、3D/CAD/world、科学可视化、结构化文档、UI/Web、跨域系统，以及训练、评估和研究前沿。

## 构建

在 `paper/` 目录中使用 XeLaTeX 与 BibTeX 执行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error paper.tex
```

使用 Overleaf 时，上传 `paper/` 的全部内容，并将 `paper.tex` 设为主文档。

## 状态

这是持续更新的综述。作者信息、投稿版本和公开发布版本确定后，将添加正式引用记录。
