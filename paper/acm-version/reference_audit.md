# Reference Audit

Date: 2026-08-15

## Scope

The audit compares every citation key found in the project's `.tex` sources with the keys defined in `references.bib`. It checks key presence and duplicate bibliography keys; it does not validate bibliographic metadata against a paper PDF.

## Result

- Citation keys found in `.tex` sources: 298
- Keys defined in `references.bib`: 299
- Missing cited keys: 0
- Duplicate bibliography keys: 0

## Repair

The nine missing keys cited by `sections/04_image_generation.tex` were added on 2026-08-15. The author lists, titles, publication status, and arXiv identifiers were cross-checked against the local paper PDFs, the literature manifest, and the pre-sync bibliography.

| Citation key | Verified record |
|---|---|
| `jaiswal2026iterative` | arXiv:2601.15286 |
| `kim2026fire` | arXiv:2604.13491 |
| `li2025iat2i` | arXiv:2505.15779 |
| `li2025mulan` | AAAI 2025; arXiv:2402.12741 |
| `nabati2025pasta` | ICML 2025; arXiv:2412.10419 |
| `wen2023compositional` | arXiv:2310.06311 |
| `wu2026visualprompter` | ICLR 2026; arXiv:2506.23138 |
| `yang2024idea2img` | ECCV 2024; arXiv:2310.08541 |
| `zhao2026toolartist` | arXiv:2608.04436 |
