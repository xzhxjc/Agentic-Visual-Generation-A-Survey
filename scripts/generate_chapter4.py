from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "agentic_visual_generation_literature" / "metadata" / "paper_taxonomy.tsv"
BIB = ROOT / "acmart_template" / "package" / "acmart" / "references.bib"
CHAPTER = ROOT / "acmart_template" / "package" / "acmart" / "sections" / "04_modalities.tex"
if False:
    """
SPLIT_CHAPTERS = {
    "鍥惧儚鐢熸垚/缂栬緫": ROOT / "acmart_template" / "package" / "acmart" / "sections" / "04_image_generation.tex",
    "瑙嗛/鍔ㄧ敾": ROOT / "acmart_template" / "package" / "acmart" / "sections" / "05_video_animation.tex",
    "3D/CAD/涓栫晫": ROOT / "acmart_template" / "package" / "acmart" / "sections" / "06_3d_cad_world.tex",
    "绉戝鍥捐〃/鏁版嵁鍙鍖?": ROOT / "acmart_template" / "package" / "acmart" / "sections" / "07_scientific_visualization.tex",
    "缁撴瀯鍖栬瑙?鏂囨。": ROOT / "acmart_template" / "package" / "acmart" / "sections" / "08_structured_documents.tex",
    "UI/Web瑙嗚": ROOT / "acmart_template" / "package" / "acmart" / "sections" / "09_ui_web.tex",
}
CROSS_DOMAIN_CHAPTER = ROOT / "acmart_template" / "package" / "acmart" / "sections" / "10_cross_domain.tex"

DOMAIN_LABELS = {
    "鍥惧儚鐢熸垚/缂栬緫": "sec:image-generation",
    "瑙嗛/鍔ㄧ敾": "sec:video-animation",
    "3D/CAD/涓栫晫": "sec:3d-cad-world",
    "绉戝鍥捐〃/鏁版嵁鍙鍖?": "sec:scientific-visualization",
    "缁撴瀯鍖栬瑙?鏂囨。": "sec:structured-documents",
    "UI/Web瑙嗚": "sec:ui-web",
}
    """

SPLIT_FILENAMES = [
    ROOT / "acmart_template" / "package" / "acmart" / "sections" / "04_image_generation.tex",
    ROOT / "acmart_template" / "package" / "acmart" / "sections" / "05_video_animation.tex",
    ROOT / "acmart_template" / "package" / "acmart" / "sections" / "06_3d_cad_world.tex",
    ROOT / "acmart_template" / "package" / "acmart" / "sections" / "07_scientific_visualization.tex",
    ROOT / "acmart_template" / "package" / "acmart" / "sections" / "08_structured_documents.tex",
    ROOT / "acmart_template" / "package" / "acmart" / "sections" / "09_ui_web.tex",
]
CROSS_DOMAIN_CHAPTER = ROOT / "acmart_template" / "package" / "acmart" / "sections" / "10_cross_domain.tex"
DOMAIN_LABELS = [
    "sec:image-generation",
    "sec:video-animation",
    "sec:3d-cad-world",
    "sec:scientific-visualization",
    "sec:structured-documents",
    "sec:ui-web",
]
COVERAGE = ROOT / "agentic_visual_generation_literature" / "metadata" / "chapter4_coverage.tsv"
DESCRIPTIONS = ROOT / "agentic_visual_generation_literature" / "metadata" / "chapter4_descriptions.tsv"

AUTO_BIB_START = "% BEGIN AUTO-GENERATED CHAPTER 4 REFERENCES"
AUTO_BIB_END = "% END AUTO-GENERATED CHAPTER 4 REFERENCES"


TASK = {
    "图像生成与视觉叙事": "compositional image synthesis and visual storytelling",
    "图像编辑": "instruction-based and multi-turn image editing",
    "图像恢复与质量增强": "mixed-degradation image restoration and quality enhancement",
    "视频、电影或叙事影像生成": "video, film, and narrative moving-image generation",
    "视频编辑与后期制作": "video editing and post-production",
    "动画生成与制作": "animation planning and production",
    "3D场景、资产或世界生成": "3D scene, asset, and world construction",
    "CAD生成与编辑": "CAD generation and editable solid modeling",
    "科学图表、示意图或数据可视化生成": "scientific figures, diagrams, charts, and data visualization",
    "海报、幻灯片或演示生成": "posters, slides, and presentation generation",
    "多模态报告或结构化视觉内容生成": "multimodal reports and structured visual content",
    "界面或网页生成": "interface and Web generation",
}

ARCH = {
    "规划或推理型单智能体": "a planning or reasoning controller",
    "工具使用型单智能体": "a tool-using controller",
    "人机协同单智能体": "a human-in-the-loop controller",
    "角色分工式多智能体": "a team of role-specialized agents",
    "层级式/编排式多智能体": "a hierarchical multi-agent orchestrator",
    "生成者-批评者/验证者": "a generator--critic or generator--verifier pair",
    "模型级多智能体协作": "model-level communicating generators",
    "原生/统一生成智能体": "a unified generation-native agent",
}

METHOD = {
    "多智能体分工与协同生成": "role specialization and collaborative generation",
    "生成-评价-修正闭环": "artifact-conditioned generation, evaluation, and revision",
    "单智能体推理与生成控制": "single-controller reasoning over generation actions",
    "学习与自我改进型生成": "experience-driven policy or skill improvement",
    "规划、检索与提示优化": "planning, retrieval, and executable prompt refinement",
    "工具/代码编排式生成": "tool and code orchestration",
}

CAP = {
    "目标理解": "interpreting the requested outcome",
    "任务分解": "decomposing the task",
    "规划": "constructing an executable plan",
    "工具调用": "selecting and invoking tools",
    "代码生成与执行": "writing and executing code",
    "检索与外部知识": "retrieving external evidence",
    "记忆与状态": "maintaining state and memory",
    "视觉观察": "inspecting intermediate artifacts",
    "批评与评价": "critiquing candidate outputs",
    "反思与修正": "diagnosing failures and revising actions",
    "规则与物理验证": "checking rule-based or physical constraints",
    "多智能体协作": "coordinating specialized roles",
    "人机协作": "preserving user intervention and authority",
    "学习与自我改进": "learning from prior trajectories",
}

DOMAIN_ORDER = [
    "图像生成/编辑",
    "视频/动画",
    "3D/CAD/世界",
    "科学图表/数据可视化",
    "结构化视觉/文档",
    "UI/Web视觉",
]

DOMAIN_TITLES = {
    "图像生成/编辑": "Image Generation, Editing, and Restoration",
    "视频/动画": "Video, Film, and Animation",
    "3D/CAD/世界": "3D, CAD, and World Construction",
    "科学图表/数据可视化": "Scientific Figures, Charts, and Data Visualization",
    "结构化视觉/文档": "Structured Visual Documents and Presentations",
    "UI/Web视觉": "UI and Web Generation",
}

# Use a consistent Agentic <domain> Generation form for the standalone chapters.
DOMAIN_TITLES = dict(
    zip(
        DOMAIN_ORDER,
        [
            "Agentic Image Generation, Editing, and Restoration",
            "Agentic Video, Film, and Animation Generation",
            "Agentic 3D, CAD, and World Generation",
            "Agentic Scientific Figure and Visualization Generation",
            "Agentic Structured Visual Document and Presentation Generation",
            "Agentic UI and Web Generation",
        ],
    )
)

GROUP_ORDER = {
    "图像生成/编辑": [
        "Image planning and execution",
        "Editing control",
        "Restoration control",
        "Image feedback",
        "Cross-trajectory learning and evidence",
    ],
    "视频/动画": [
        "Video planning",
        "Video execution",
        "Video editing",
        "Video feedback",
        "Video learning and evaluation",
    ],
    "3D/CAD/世界": ["World control", "CAD control", "3D evidence"],
    "科学图表/数据可视化": ["Data visualization", "Scientific figures", "Scientific evidence"],
    "结构化视觉/文档": ["Structured documents", "Presentation control", "Document evidence"],
    "UI/Web视觉": ["Web execution", "Web evidence"],
}

DOMAIN_OPENERS = {
    "图像生成/编辑": (
        "Image work exposes the distinction between choosing a capable renderer and controlling an evolving artifact. "
        "The relevant state ranges from object--attribute relations and masks to identity references, degradation estimates, edit history, and user preferences. "
        "The literature below is therefore organized by the control problem that is made explicit, not by the underlying diffusion or editing backbone."
    ),
    "视频/动画": (
        "Video changes both the horizon and the unit of correction. A system may reason over scripts, shots, keyframes, motion trajectories, audio, camera state, or an editable timeline, while an apparently local change can disturb identity and causality much later in the sequence. "
        "The central comparison is consequently between systems that merely distribute production stages and those that preserve temporal state, diagnose a failed segment, and revise it without restarting the whole work."
    ),
    "3D/CAD/世界": (
        "Three-dimensional creation makes state more explicit but also makes visual plausibility an insufficient success criterion. Geometry, topology, dimensions, joints, scene graphs, operation histories, collisions, and simulator outcomes can all be inspected, so agents can act on executable structure rather than pixels alone. "
        "This section separates appearance-oriented world construction from editable CAD and from verification-driven refinement."
    ),
    "科学图表/数据可视化": (
        "Scientific and data-grounded graphics bind visual communication to source fidelity. Here the artifact is simultaneously an image, a structured specification, an executable program, and an argument about data. "
        "Agentic control must therefore coordinate analytical intent, chart or diagram structure, code execution, visual inspection, and checks that the rendered claim remains supported by the source."
    ),
    "结构化视觉/文档": (
        "Structured visual documents couple long-range narrative decisions with page-level geometry. Their state includes source material, section hierarchy, slide or page roles, assets, layout constraints, style, citations, and edit history. "
        "The relevant systems are compared by whether they keep these representations connected when content is retrieved, composed, rendered, inspected, and revised."
    ),
    "UI/Web视觉": (
        "Interface generation joins visual appearance to executable behavior. Component trees, style rules, screenshots, browser state, and interaction traces provide complementary views of the same artifact, making this domain a stringent test of whether visual feedback can be translated into code-level repair."
    ),
}


def latex_escape(text: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
        "_": r"\_",
        "–": "--",
        "—": "---",
        "’": "'",
        "“": "``",
        "”": "''",
        "ı": r"{\i}",
        "ß": r"{\ss}",
        "ø": r"{\o}",
        "Ø": r"{\O}",
        "ł": r"{\l}",
        "Ł": r"{\L}",
    }
    accents = {
        "\u0300": "`",
        "\u0301": "'",
        "\u0302": "^",
        "\u0303": "~",
        "\u0304": "=",
        "\u0306": "u",
        "\u0307": ".",
        "\u0308": '"',
        "\u030a": "r",
        "\u030b": "H",
        "\u030c": "v",
        "\u0327": "c",
        "\u0328": "k",
    }
    result = []
    for char in text:
        if char in replacements:
            result.append(replacements[char])
            continue
        if ord(char) < 128:
            result.append(char)
            continue
        decomposed = unicodedata.normalize("NFD", char)
        if len(decomposed) >= 2 and decomposed[0].isascii() and decomposed[1] in accents:
            result.append("{\\" + accents[decomposed[1]] + "{" + decomposed[0] + "}}")
            continue
        ascii_fallback = unicodedata.normalize("NFKD", char).encode("ascii", "ignore").decode("ascii")
        if ascii_fallback:
            result.append(ascii_fallback)
        else:
            raise ValueError(f"Unsupported non-ASCII character in BibTeX field: {char!r}")
    return "".join(result)


def key_for_id(paper_id: str) -> str:
    return "avg" + re.sub(r"[^A-Za-z0-9]", "", paper_id).lower()


def normalized(text: str) -> str:
    text = re.sub(r"\\[A-Za-z]+", "", text)
    text = re.sub(r"[^A-Za-z0-9]+", "", text)
    return text.lower()


def existing_entries(bib_text: str) -> list[tuple[str, str]]:
    clean = re.sub(
        re.escape(AUTO_BIB_START) + r".*?" + re.escape(AUTO_BIB_END),
        "",
        bib_text,
        flags=re.S,
    )
    entries = []
    for match in re.finditer(r"(?ms)^@(\w+)\{([^,]+),(.*?)(?=^\}\s*$)", clean):
        start = match.start()
        end_match = re.search(r"(?m)^\}\s*$", clean[match.end() :])
        if not end_match:
            continue
        end = match.end() + end_match.end()
        block = clean[start:end]
        entries.append((match.group(2).strip(), block))
    return entries


def citation_map(rows: list[dict[str, str]], bib_text: str) -> tuple[dict[str, str], str]:
    clean_bib = re.sub(
        re.escape(AUTO_BIB_START) + r".*?" + re.escape(AUTO_BIB_END),
        "",
        bib_text,
        flags=re.S,
    ).rstrip() + "\n"
    entries = existing_entries(clean_bib)
    mapping: dict[str, str] = {}
    missing: list[dict[str, str]] = []
    for row in rows:
        paper_id = row["paper_id"]
        title_norm = normalized(row["title"])
        found = None
        for key, block in entries:
            if paper_id.lower() in block.lower():
                found = key
                break
            title_match = re.search(r"(?ms)\btitle\s*=\s*\{(.*?)\}\s*,", block)
            if title_match and normalized(title_match.group(1)) == title_norm:
                found = key
                break
        if found:
            mapping[paper_id] = found
        else:
            mapping[paper_id] = key_for_id(paper_id)
            missing.append(row)

    additions = ["", AUTO_BIB_START]
    for row in missing:
        authors = " and ".join(part.strip() for part in row["authors"].split(";") if part.strip())
        additions.extend(
            [
                f"@misc{{{mapping[row['paper_id']]},",
                f"  author = {{{latex_escape(authors)}}},",
                f"  title = {{{latex_escape(row['title'])}}},",
                f"  year = {{{row['year']}}},",
                f"  howpublished = {{{latex_escape(row['venue'])}}},",
                f"  url = {{{row['source_url']}}}",
                "}",
                "",
            ]
        )
    additions.append(AUTO_BIB_END)
    additions.append("")
    return mapping, clean_bib + "\n".join(additions)


def caps_phrase(raw: str) -> str:
    values = [CAP[x.strip()] for x in raw.split("；") if x.strip() in CAP]
    if not values:
        return "an agentic mechanism that remains only partially specified in the available evidence"
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} and {values[1]}"
    return ", ".join(values[:-1]) + f", and {values[-1]}"


def describe(row: dict[str, str], cite_key: str, index: int) -> str:
    body = row["chapter_description"].strip().rstrip(".")
    transitions = ["", "By contrast, ", "A complementary approach, ", "At the same control boundary, "]
    prefix = transitions[index % len(transitions)]
    return f"{prefix}{body}~\\cite{{{cite_key}}}."


def group_for(row: dict[str, str]) -> tuple[str, str]:
    modality = row["normalized_modality"]
    stage = row["pipeline_primary"]
    task = row["task_type"]
    title = row["title"].lower()

    if modality == "图像生成/编辑":
        if stage in {"策略层：学习与自我改进", "支撑层：评测、安全与方法论"}:
            return ("Learning, evaluation, and safety", "Cross-trajectory learning and evidence")
        if task == "图像恢复与质量增强":
            return ("Restoration as diagnosis and toolpath selection", "Restoration control")
        if task == "图像编辑":
            return ("Editing as state-preserving action", "Editing control")
        if stage in {"闭环：反馈迭代", "生成后：观察、评价与验证"}:
            return ("Artifact-conditioned verification and repair", "Image feedback")
        return ("Compositional planning, routing, and spatial control", "Image planning and execution")

    if modality == "视频/动画":
        if stage in {"策略层：学习与自我改进", "支撑层：评测、安全与方法论"}:
            return ("Skill evolution and diagnostic evidence", "Video learning and evaluation")
        if task == "视频编辑与后期制作":
            return ("Editable timelines and post-production", "Video editing")
        if stage in {"闭环：反馈迭代", "生成后：观察、评价与验证"}:
            return ("Temporal feedback, physical control, and local recovery", "Video feedback")
        if stage == "生成前：理解、分解与规划" or task == "动画生成与制作":
            return ("Scripts, storyboards, motion, and pre-production", "Video planning")
        return ("Multi-shot production and cross-modal orchestration", "Video execution")

    if modality == "3D/CAD/世界":
        if stage in {"生成后：观察、评价与验证", "策略层：学习与自我改进", "支撑层：评测、安全与方法论"}:
            return ("Geometry-aware verification, simulation, and learning", "3D evidence")
        if task == "CAD生成与编辑":
            return ("Executable CAD programs and editable solids", "CAD control")
        return ("Scene graphs, assets, layouts, and interactive worlds", "World control")

    if modality == "科学图表/数据可视化":
        if stage in {"闭环：反馈迭代", "生成后：观察、评价与验证", "支撑层：评测、安全与方法论"}:
            return ("Rendered feedback, semantic validation, and benchmarks", "Scientific evidence")
        if any(word in title for word in ["scientific", "diagram", "figure", "paper", "schematic"]):
            return ("Scientific figures and diagrams", "Scientific figures")
        return ("Data-to-chart analysis and executable visualization", "Data visualization")

    if modality == "结构化视觉/文档":
        if stage in {"闭环：反馈迭代", "策略层：学习与自我改进", "支撑层：评测、安全与方法论"}:
            return ("Rendering-grounded revision and document-level evidence", "Document evidence")
        if task == "海报、幻灯片或演示生成":
            return ("Presentation and poster composition", "Presentation control")
        return ("Interleaved reports and structured multimodal content", "Structured documents")

    if stage in {"闭环：反馈迭代", "支撑层：评测、安全与方法论"}:
        return ("Browser-grounded verification and repair", "Web evidence")
    return ("From visual specification to executable interface", "Web execution")


GROUP_INTROS = {
    "Image planning and execution": "The first problem is to convert compositional intent into spatially and semantically executable decisions. Model routing, prompt expansion, object decomposition, reference management, and code-mediated placement are useful only insofar as they expose decisions that can later be checked.",
    "Editing control": "Editing changes the objective from unrestricted synthesis to a constrained state transition: requested regions must change while identities, geometry, background, and prior edits remain stable. The systems in this group differ primarily in whether they plan toolpaths, reformulate instructions, or represent the canvas as an interactive state.",
    "Restoration control": "Restoration provides a diagnostic form of agency. The controller must infer interacting degradations, choose specialist models in an appropriate order, judge whether one operation has exposed or amplified another defect, and stop before over-processing the image.",
    "Image feedback": "A closed image loop requires more than sampling several candidates. The evaluator must localize the violated object, attribute, relation, or physical rule and translate that evidence into a targeted next action.",
    "Cross-trajectory learning and evidence": "The final image line asks what persists after a trajectory ends. Self-improving systems retain workflows, skills, rewards, or distilled experience, whereas benchmarks and red-team studies test whether such adaptation remains reliable and safe.",
    "Video planning": "Pre-production externalizes long-horizon intent as scripts, shot plans, storyboards, trajectories, or motion programs. This representation can reduce ambiguity, but only when downstream generators can preserve its entities and constraints.",
    "Video execution": "Production-oriented systems distribute work across directors, cinematographers, character or scene managers, audio agents, and specialized generators. Their scientific value depends on what state crosses role boundaries and whether coordination is conditional on evidence rather than fixed hand-offs.",
    "Video editing": "Editing systems operate over an existing timeline, so action locality, provenance, rhythm, and story-level comprehension become central. A useful agent must connect language to temporal spans and preserve unaffected material across nonlinear revisions.",
    "Video feedback": "Temporal feedback must identify where a failure begins and whether its cause is narrative, geometric, physical, camera-related, or model-specific. Segment-level recovery is therefore more informative than wholesale regeneration.",
    "Video learning and evaluation": "Long-video autonomy also depends on reusable skills and evaluators that can diagnose continuity, personalization, tool use, and resource costs over extended trajectories.",
    "World control": "World construction combines asset selection, spatial arrangement, scene-graph state, and sometimes simulation. The key distinction is whether an agent merely writes a scene description or can observe and revise the instantiated world.",
    "CAD control": "CAD makes action history and constraints first-class. Code, sketches, feature operations, and parametric edits provide precise interventions, while rendered views offer complementary visual evidence that the underlying solid remains meaningful.",
    "3D evidence": "Verification can inspect geometry, physics, compilation, and task function independently of appearance. These signals also make 3D a useful setting for reinforcement learning and self-corrective search.",
    "Data visualization": "Chart agents translate analytical intent into data transformations, encodings, and executable plotting code. Execution catches syntax failures, but factual and perceptual validity require additional checks against the data and communicative goal.",
    "Scientific figures": "Scientific figures and diagrams add domain semantics, symbolic structure, and source-document grounding. Their state must remain editable and traceable to evidence, not merely visually similar to a target style.",
    "Scientific evidence": "Evaluation in this domain can combine inverse parsing, code execution, rule checking, visual critique, and source consistency. The following work shows both the strength of heterogeneous evidence and the remaining difficulty of converting a diagnosis into a correct local repair.",
    "Presentation control": "Slides and posters require coordinated decisions about narrative role, information density, asset selection, typography, and page geometry. Treating each page as an isolated image loses the state needed for coherent revision.",
    "Structured documents": "Reports and interleaved content require the agent to decide when prose, images, tables, or diagrams should carry the argument, and to keep citations and retrieved evidence aligned with those decisions.",
    "Document evidence": "Rendered pages expose overflow, overlap, alignment, and readability failures that are invisible in an outline or source tree. Document-level feedback additionally tests cross-page consistency and the cost imposed on human reviewers.",
    "Web execution": "Visual-to-code and specification-to-interface systems must coordinate design intent with component structure and runtime behavior. A rendered screenshot is an observation of the program, not a substitute for functional state.",
    "Web evidence": "Browser-grounded systems can combine screenshots, DOM structure, interaction tests, and accessibility checks. This heterogeneous evidence makes precise repair possible but also reveals failures that a single image metric cannot capture.",
}


DOMAIN_CONCLUSIONS = {
    "图像生成/编辑": "Across image tasks, state accessibility determines the kind of correction that is possible. Masks, object tables, edit histories, degradation estimates, and reusable workflows support localized action; undifferentiated visual scores tend to produce repeated global resampling. The literature therefore progresses from model choice toward state-preserving control, but verifier calibration and causal credit remain limiting factors.",
    "视频/动画": "The video literature demonstrates that more production roles do not by themselves solve temporal control. Stronger systems externalize persistent entities and constraints, inspect localized temporal evidence, and revise segments or policies. The remaining gap is a reliable connection between long-range diagnosis, bounded recovery, and resource-aware stopping.",
    "3D/CAD/世界": "Three-dimensional domains offer unusually strong heterogeneous evidence, yet the evidence is split across rendered appearance, geometric validity, editability, and physical function. A convincing agent must preserve all four views of state and repair the underlying representation rather than optimizing only a camera projection.",
    "科学图表/数据可视化": "Executable code and structured specifications make scientific graphics comparatively auditable, but not automatically truthful. Reliable control requires provenance from source to transformation to mark, plus visual and semantic checks that can identify the responsible stage when the final claim is wrong.",
    "结构化视觉/文档": "Document agents become genuinely artifact-grounded when outline state, evidence state, layout state, and rendered observations remain synchronized. Current systems establish useful loops around rendering and revision, while source fidelity, cross-page memory, and human approval remain essential controls.",
    "UI/Web视觉": "UI and Web work provides the clearest opportunity to connect perception to executable repair because the same artifact can be inspected as pixels, a component tree, and runtime behavior. The principal challenge is to preserve this correspondence across long editing trajectories rather than optimizing isolated screenshots.",
}


def generate_chapter(rows: list[dict[str, str]], cites: dict[str, str]) -> tuple[str, list[dict[str, str]]]:
    out = [
        r"\section{Agentic Visual Generation Across Domains}",
        r"\label{sec:modalities}",
        "",
        "The operating loop in Section~\\ref{sec:loop} provides a common vocabulary, but its concrete meaning is determined by the artifact under control. A canvas, timeline, scene graph, CAD program, plotting specification, slide deck, and browser application expose different state variables, support different interventions, and admit different evidence. This chapter therefore organizes the literature by application domain while asking the same questions in each case: what state persists, which actions can change it, what observations are available, how verification becomes an actionable diagnosis, and what is learned across attempts.",
        "",
        "The discussion uses core studies to establish each domain's main trajectory, adjacent studies to identify transferable mechanisms or boundaries, and benchmark, safety, and methodological studies as evidence about reliability. Papers are grouped by the control problem they address rather than presented chronologically. Each study is assigned once to a primary domain argument, even when its mechanism is relevant elsewhere; cross-domain implications are synthesized at the end of the chapter.",
        "",
    ]
    coverage: list[dict[str, str]] = []

    for modality in DOMAIN_ORDER:
        domain_rows = [row for row in rows if row["normalized_modality"] == modality]
        out.extend([f"\\subsection{{{DOMAIN_TITLES[modality]}}}", "", DOMAIN_OPENERS[modality], ""])
        grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
        for row in domain_rows:
            group = group_for(row)
            grouped.setdefault(group, []).append(row)

        ordered_groups = sorted(
            grouped.items(),
            key=lambda item: GROUP_ORDER[modality].index(item[0][1]),
        )
        for (heading, group_id), group_rows in ordered_groups:
            group_rows.sort(
                key=lambda r: (
                    {"核心": 0, "邻接": 1, "支撑": 2}.get(r["scope_layer"], 3),
                    int(r["year"]),
                    r["title"].lower(),
                )
            )
            out.extend([f"\\paragraph{{{heading}.}}", GROUP_INTROS[group_id], ""])
            for scope in ["核心", "邻接", "支撑"]:
                scope_rows = [row for row in group_rows if row["scope_layer"] == scope]
                if not scope_rows:
                    continue
                if scope == "邻接":
                    out.extend([
                        "Adjacent studies extend this control problem or make one of its mechanisms independently testable; they are used here as boundary evidence rather than as equivalent end-to-end AVG systems.",
                        "",
                    ])
                elif scope == "支撑":
                    out.extend([
                        "Evaluation, methodological, and safety studies make the corresponding capability or failure mode observable without being counted as another generation architecture.",
                        "",
                    ])
                running_index = 0
                for batch_start in range(0, len(scope_rows), 4):
                    batch = scope_rows[batch_start : batch_start + 4]
                    paragraph = []
                    for row in batch:
                        paragraph.append(describe(row, cites[row["paper_id"]], running_index))
                        running_index += 1
                        coverage.append(
                            {
                                "paper_id": row["paper_id"],
                                "title": row["title"],
                                "normalized_modality": modality,
                                "chapter_group": heading,
                                "scope_layer": row["scope_layer"],
                                "citation_key": cites[row["paper_id"]],
                            }
                        )
                    out.extend([" ".join(paragraph), ""])
        out.extend([DOMAIN_CONCLUSIONS[modality], "", r"\FloatBarrier", ""])

    out.extend(
        [
            r"\Needspace{0.80\textheight}",
            r"\subsection{Cross-Domain Agentic Visual Generation}",
            "",
            r"\begin{table}[H]",
            r"  \caption{How domain artifacts change state, action, and verification in the agentic creation loop.}",
            r"  \label{tab:modalities}",
            r"  \small",
            r"  \begin{tabularx}{\textwidth}{@{}lXXX@{}}",
            r"    \toprule",
            r"    Domain & Persistent state & Corrective action & Strongest available evidence \\",
            r"    \midrule",
            r"    Image & Canvas, objects, masks, identities, edit and degradation history & Prompt/model routing, compositing, region edits, restoration toolpaths & Spatial and semantic checks, edit preservation, preference and safety judgments \\",
            r"    Video/animation & Script, shots, entities, keyframes, motion, camera, audio, timeline & Replanning, shot or segment regeneration, temporal editing, post-production & Event order, identity, motion, physics, cross-shot continuity, creator feedback \\",
            r"    3D/CAD/world & Geometry, topology, parts, constraints, scene graph, operation history & Modeling code, CAD operations, asset placement, simulation-grounded repair & Compilation, geometry, collision, physical function, multi-view rendering \\",
            r"    Scientific graphics & Data, transforms, marks, encodings, diagram structure, plotting code & Re-analysis, specification/code edits, layout and annotation repair & Execution, data lineage, inverse parsing, semantic and perceptual rules \\",
            r"    Documents/presentations & Sources, outline, narrative roles, page geometry, assets, citations, style & Retrieval, content and layout edits, page regeneration & Overflow, overlap, readability, source fidelity, cross-page consistency \\",
            r"    UI/Web & Requirements, component tree, styles, interaction and browser state & Code/component edits, rendering, interaction-level repair & Runtime tests, DOM and screenshot alignment, accessibility and function \\",
            r"    \bottomrule",
            r"  \end{tabularx}",
            r"\end{table}",
            r"\FloatBarrier",
            "",
            "Three cross-domain conclusions follow. First, autonomy is constrained by state representation: agents can make precise, reversible corrections only when persistent entities and operation histories remain addressable. Second, executable domains do not remove the need for visual observation; compilation and rule checks establish structural validity, whereas rendered evidence exposes legibility, composition, and human-facing failures. Third, verification is useful only when it is causally connected to an action and a stopping decision. These findings connect the domain evidence in this chapter to the evaluation dimensions developed in Section~\\ref{sec:evaluation}.",
            "",
        ]
    )
    return "\n".join(out), coverage


def split_chapter(chapter: str) -> dict[Path, str]:
    """Split the generated domain chapter into independently numbered sections."""
    cross_marker = r"\subsection{Cross-Domain Agentic Visual Generation}"
    cross_start = chapter.index(cross_marker)
    result: dict[Path, str] = {}

    for index, modality in enumerate(DOMAIN_ORDER):
        marker = f"\\subsection{{{DOMAIN_TITLES[modality]}}}"
        start = chapter.index(marker)
        end = cross_start
        for later_modality in DOMAIN_ORDER[index + 1 :]:
            later_marker = f"\\subsection{{{DOMAIN_TITLES[later_modality]}}}"
            end = min(end, chapter.index(later_marker))
        body = chapter[start + len(marker) : end].strip()
        section = [
            f"\\section{{{DOMAIN_TITLES[modality]}}}",
            f"\\label{{{DOMAIN_LABELS[index]}}}",
            "",
            body,
            "",
        ]
        result[SPLIT_FILENAMES[index]] = "\n".join(section)

    cross_body = chapter[cross_start + len(cross_marker) :].strip()
    result[CROSS_DOMAIN_CHAPTER] = "\n".join(
        [
            r"\section{Cross-Domain Agentic Visual Generation}",
            r"\label{sec:cross-domain}",
            "",
            cross_body,
            "",
        ]
    )
    return result


def main() -> None:
    with TAXONOMY.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != 264 or len({row["paper_id"] for row in rows}) != len(rows):
        raise RuntimeError("The taxonomy must contain 264 unique paper IDs before Chapter 4 is generated.")

    with DESCRIPTIONS.open("r", encoding="utf-8-sig", newline="") as handle:
        descriptions = {row["paper_id"]: row["description"] for row in csv.DictReader(handle, delimiter="\t")}
    missing_descriptions = sorted({row["paper_id"] for row in rows} - set(descriptions))
    extra_descriptions = sorted(set(descriptions) - {row["paper_id"] for row in rows})
    if missing_descriptions or extra_descriptions:
        raise RuntimeError(
            f"Description coverage mismatch: missing={missing_descriptions}, extra={extra_descriptions}"
        )
    for row in rows:
        row["chapter_description"] = descriptions[row["paper_id"]]

    bib_text = BIB.read_text(encoding="utf-8-sig")
    cites, updated_bib = citation_map(rows, bib_text)
    chapter, coverage = generate_chapter(rows, cites)

    BIB.write_text(updated_bib, encoding="utf-8", newline="\n")
    CHAPTER.write_text(
        "% Deprecated compatibility file. The domain chapters are generated as\n"
        "% 04_image_generation.tex through 10_cross_domain.tex.\n",
        encoding="utf-8",
        newline="\n",
    )
    for path, text in split_chapter(chapter).items():
        path.write_text(text, encoding="utf-8", newline="\n")
    with COVERAGE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(coverage[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(coverage)

    print(f"chapter papers: {len(coverage)}")
    print(f"unique chapter papers: {len({row['paper_id'] for row in coverage})}")
    print(f"citation keys: {len(set(cites.values()))}")
    print(f"bibliography auto-added: {updated_bib.count('@misc{avg')}")


if __name__ == "__main__":
    main()
