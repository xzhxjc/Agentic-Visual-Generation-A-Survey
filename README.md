<div align="center">

# Agentic Visual Generation: A Survey

**From single-pass rendering to observation-dependent visual creation**

[中文说明](README_zh-CN.md)

</div>

![Survey literature growth and coverage](paper/figures/avg_literature_growth_by_year_domain_autonomy.jpg)

This repository contains the source of *Agentic Visual Generation: A Survey*. It studies visual creation systems in which runtime observations of an evolving artifact, task environment, or interaction history change later visual-creation decisions.

> A visual creation process is agentic when runtime evidence changes a later creation action.

## Paper Source

All files needed to build the current manuscript are in [`paper/`](paper/):

```text
paper.tex              # Main entry point
sections/              # Chapter sources
figures/               # Referenced manuscript figures and TikZ sources
references.bib         # Bibliography
hust.cls, assets/      # Local layout and font/logo dependencies
```

The manuscript covers image generation and editing, video and animation, 3D/CAD/world creation, scientific visualization, structured documents, UI/Web, cross-domain systems, training, evaluation, and research frontiers.

## Build

From `paper/`, compile with XeLaTeX and BibTeX:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error paper.tex
```

For Overleaf, upload the contents of `paper/` and set `paper.tex` as the main document.

## Status

This is a living survey. The manuscript and bibliography are updated as sources are verified. A citable release record will be added once the author list, venue, and public release version are finalized.
