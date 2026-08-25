# AVG Reading Version

This folder is a separate single-column reading-version prototype for the Agentic Visual Generation survey. The original ACM project remains in `../overleaf_agentic_visual_generation` and is not modified by this template migration.

## Template

- Base template: [HUST-ArXiv-Template](https://github.com/Shulin-Li22/HUST-ArXiv-Template)
- Original template lineage: [OneThree arXiv Template](https://github.com/choucisan/arXiv-Template)
- Template license: see `LICENSE`
- Local customized class: `hust.cls`
- Customization: HUST colors and header marks were replaced with AI4GC Lab / Zhejiang University reading-version styling.

## Logos

- AI4GC Lab logo: `assets/ai4gc-logo.png`
  - Source: `https://ai4gc.org/content-assets/ai4gclab/AI4GC.png`
- Zhejiang University mark: `assets/zju-logo.svg`
  - Source: `https://ai4gc.org/content-assets/zju/zju.svg`
- Browser-rendered PNG used by the PDF prototype: `assets/zju-logo-crop.png`
  - The source SVG is retained for future higher-resolution conversion.

## Build

```powershell
python <path-to-your-latex-compiler> .\paper.tex --output-directory .\build_final --json
```

The current prototype uses a placeholder overview figure. Replace it with the approved AVG operating-trajectory or overview figure after the visual design is finalized.
