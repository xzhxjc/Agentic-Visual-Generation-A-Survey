from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "acmart_template" / "package" / "acmart" / "agentic_visual_generation_survey.tex"
SECTIONS = ROOT / "acmart_template" / "package" / "acmart" / "sections"
OUTPUT = ROOT / "Agentic_Visual_Generation_Translation_Source.tex"

SECTION_FILES = [
    "01_introduction.tex",
    "02_foundations.tex",
    "03_operating_loop.tex",
    "04_image_generation.tex",
    "05_video_animation.tex",
    "06_3d_cad_world.tex",
    "07_scientific_visualization.tex",
    "08_structured_documents.tex",
    "09_ui_web.tex",
    "10_cross_domain.tex",
    "05_evaluation.tex",
    "06_frontiers.tex",
    "07_conclusion.tex",
]


def translation_ready(text: str) -> str:
    """Keep translatable content while removing document-assembly commands."""
    text = re.sub(
        r"(?ms)^\\begin\{figure\*?\}.*?^\\end\{figure\*?\}\s*",
        "",
        text,
    )
    text = re.sub(r"(?m)^\\label\{[^}]+\}\s*$\n?", "", text)
    text = re.sub(r"(?m)^\\FloatBarrier\s*$\n?", "", text)
    text = re.sub(r"(?m)^\\Needspace\{[^}]+\}\s*$\n?", "", text)
    text = text.replace(r"\AVG{}", "Agentic Visual Generation")
    text = text.replace(r"\toolset", r"\mathcal{T}")
    return text.strip()


def main() -> None:
    main_text = MAIN.read_text(encoding="utf-8-sig")
    abstract_match = re.search(r"(?s)\\begin\{abstract\}(.*?)\\end\{abstract\}", main_text)
    if not abstract_match:
        raise RuntimeError("Could not locate the abstract in the main TeX file.")

    parts = [r"\section*{Abstract}", translation_ready(abstract_match.group(1))]
    parts.extend(translation_ready((SECTIONS / filename).read_text(encoding="utf-8-sig")) for filename in SECTION_FILES)
    OUTPUT.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")

    section_count = sum(part.count(r"\section{") for part in parts)
    print(f"translation source sections: {section_count}")
    print(f"translation source: {OUTPUT}")


if __name__ == "__main__":
    main()
