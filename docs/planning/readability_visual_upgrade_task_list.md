# Agentic Visual Generation Survey: Readability and Visual Upgrade Task List

## 0. Task Definition

### Teacher's goal

Transform the survey from a text-dense manuscript into a visually navigable survey that readers can skim quickly, locate their research area, understand representative pipelines, learn basic concepts, and obtain concise research takeaways before reading the full discussion.

### Design reference

- Main reference URL: `https://arxiv.org/pdf/2303.18223`
- Reference project: `https://github.com/rucaibox/llmsurvey`
- Local reference PDF: the reference survey PDF used during drafting (not included in the public package)
- Local inspection currently reports 62 pages, while the teacher described the reference as 144 pages. Confirm that the downloaded/local PDF is the intended version before copying its layout decisions or estimating page targets.

### Current manuscript baseline

- Main project: `overleaf_agentic_visual_generation`
- Current manuscript: approximately 123 pages after compilation
- Current chapter structure: Foundations; Analytical Components; Image; Video; 3D/CAD/World; Scientific Visualization; Structured Documents; UI/Web; Cross-Domain; Training; Evaluation; Frontiers; Conclusion
- Current analytical components: Goal Understanding, Specification, and Planning; Memory; Tool; Perception; Action; Cross-Task Self-Improvement

### Non-goals

- Do not start a new large-scale literature collection before the visual reorganization is complete.
- Do not add figures merely to increase the page count.
- Do not copy third-party figures without checking the source, license, attribution, and venue requirements.
- Do not turn every paragraph into a box or every sentence into a bullet list.
- Do not introduce new terminology that conflicts with the six-component framework.

## 1. Acceptance Criteria

- A reader can identify the paper's topic, definition of AVG, six components, visual domains, training, evaluation, and frontiers from the table of contents and overview figures.
- A reader who opens a random page can identify the local topic within a few seconds through the section heading, lead sentence, figure/table, or takeaway box.
- Each long chapter has a visual summary or pipeline figure and a compact comparison table.
- Each major chapter has a clear internal hierarchy. Second-level headings remain the default; third-level headings are added where a section is long or contains several independent themes.
- The cover, abstract, contents page, figures, tables, callout boxes, headers, footers, and references share one visual language.
- Every figure has a readable caption, source attribution where needed, and a clear connection to the surrounding text.
- Every key takeaway is supported by the reviewed literature or explicitly marked as the survey's synthesis.
- The final PDF compiles without unresolved citations or references. Representative pages are rendered and visually inspected.

## 2. Workstream A: Confirm the Reference and Establish the Visual System

### A1. Confirm the design reference

- [ ] Compare the URL version, GitHub project, and local PDF.
- [ ] Record the actual page count, cover structure, contents-page style, heading levels, figure density, table style, and callout style.
- [ ] Decide which design principles are transferable to an AVG survey and which depend on the reference paper's subject matter.
- [ ] Keep a short reference audit in `reference_visual_audit.md`.

### A2. Define the survey visual language

- [ ] Choose one primary color for section navigation and one restrained accent color for takeaways.
- [ ] Define typography for section titles, subsection titles, figure titles, table captions, body text, and box titles.
- [ ] Define a consistent visual grammar for diagrams: artifact, state, action, evidence, decision, and cross-task update.
- [ ] Define figure widths, minimum font size, line thickness, arrow style, border radius, and caption spacing.
- [ ] Define the visual treatment for cited reused figures, redrawn figures, original figures, tables, and key takeaway boxes.
- [ ] Check that the selected colors remain readable in grayscale and in printed form.

### A3. Define page-level navigation

- [ ] Add consistent running headers or section markers so a reader can identify the current chapter without returning to the contents page.
- [ ] Make the contents page show all major sections and the important third-level headings in long chapters.
- [ ] Add a short chapter-opening orientation paragraph to long chapters.
- [ ] Add concise lead sentences at the beginning of major subsections. The lead sentence should state the topic and purpose directly.
- [ ] Keep paragraph-level paper descriptions compact and visually scannable through consistent lead labels.

## 3. Workstream B: Cover, Abstract, and Contents

### B1. Cover page

- [ ] Create a dedicated first page with the title `Agentic Visual Generation: A Survey`.
- [ ] Place the AI4GC Lab logo in the upper area after obtaining the correct logo file and usage permission.
- [ ] Add authors, affiliations, supervisor information, version/date, and a repository placeholder.
- [ ] Use a small original AVG overview graphic or visual creation trajectory on the cover. The cover graphic must be created for this paper or properly licensed.
- [ ] Use a repository placeholder such as `Repository: to be added`; do not invent a URL.
- [ ] Keep the cover clean and academic. Avoid a marketing-style hero page or excessive decoration.

### B2. Abstract

- [ ] Shorten the abstract after the layout is stabilized.
- [ ] Retain only the problem motivation, behavioral definition of AVG, six-component framework, cross-domain coverage, training, evaluation, and frontier contribution.
- [ ] Remove repeated lists of limitations already explained in the introduction.
- [ ] Target a compact abstract suitable for quick reading. Preserve precise claims and avoid promising a complete universal evaluation standard.

### B3. Contents page

- [ ] Use the reference survey's contents-page principle: make chapter and major subsection names immediately scannable.
- [ ] Keep third-level entries for long chapters such as Image, Video, Training, Evaluation, and Frontiers.
- [ ] Avoid displaying paragraph-level paper titles in the contents page.
- [ ] Check that the contents page does not become a dense wall of equally weighted titles.
- [ ] Verify page numbers after every major restructuring.

## 4. Workstream C: Core Overview Figures

These figures should be commissioned first because they define the visual language for the rest of the paper.

### C1. AVG evolution figure

- [ ] Show the progression from single-pass visual generation to observation-dependent, stateful, tool-using, long-horizon, and cross-task-improving creation.
- [ ] Use a small number of stages and one representative capability per stage.
- [ ] Avoid implying that every system passes through the same historical sequence.
- [ ] Add citations for named milestones if specific papers are shown.

### C2. AVG operating trajectory figure

- [ ] Draw the basic creation trajectory: goal/specification -> action/tool -> artifact or execution result -> perception/evidence -> later decision.
- [ ] Show branches for revision, recovery, clarification, stopping, and cross-task reuse.
- [ ] Use the exact current terminology from Chapter 3.
- [ ] Make the observation-dependent action change visually obvious.

### C3. Six-component framework figure

- [ ] Build the central overview figure for Chapter 3.
- [ ] Place the six components around the creation trajectory or in a structured pipeline.
- [ ] Show the relationship among planning, memory, tool, perception, action, and cross-task self-improvement.
- [ ] Keep the diagram analytical. It must not imply that every paper implements six independent software modules.
- [ ] Add a short caption explaining that the components are descriptive categories for cross-paper analysis.

### C4. Visual-domain map

- [ ] Map the domains covered by Chapters 4-10: image, video/animation, 3D/CAD/world, scientific visualization, structured documents, UI/Web, and cross-domain workflows.
- [ ] For each domain, show artifact representation, typical action space, main evidence source, and a representative pipeline.
- [ ] Use the same visual tokens for artifact, action, perception, and evaluation across all domains.

### C5. Training and improvement figure

- [ ] Show trainable targets and update paths: generator, controller, router, critic/verifier, memory/skills, integrated policy, and joint optimization.
- [ ] Show trajectory data, supervision, multimodal feedback, reinforcement learning, experience reuse, skill abstraction, and transfer.
- [ ] Mark the difference between within-trajectory adaptation, persistent reuse, and cross-task improvement.

### C6. Evaluation overview figure

- [ ] Show the four evaluation levels used in Chapter 12: artifact quality; goal and constraint satisfaction; trajectory and decision quality; and system and human-centered evaluation.
- [ ] Add the fifth subsection, `Remaining Evaluation Gaps`, as a synthesis or outer layer rather than a fifth main level.
- [ ] Connect each level to the evidence it needs, such as rendered artifacts, typed constraints, trajectory traces, resource records, user studies, safety checks, and provenance.

### C7. Frontier roadmap

- [ ] Represent the three main frontier directions: expanding scope, increasing intelligence, and establishing reliable evaluation.
- [ ] Place the existing subtopics under these three directions without repeating the six-component framework.
- [ ] Keep the figure high-level and suitable for a reader who has not read the full survey.

## 5. Workstream D: Chapter-by-Chapter Visual Plan

### D1. Foundations and definition

- [ ] Add or refine a foundation map covering generator, artifact representation, conditioning inputs, and execution interfaces.
- [ ] Improve the AVG boundary table and L1-L5 table visually.
- [ ] Add a compact `Key Takeaway` box defining the behavioral criterion: runtime evidence changes later creation action selection.

### D2. Analytical Components

- [ ] Place the six-component framework figure near the beginning of the chapter.
- [ ] Add a one-page component comparison table with columns such as `Component`, `What it organizes`, `Typical records`, and `Evidence needed`.
- [ ] Add a short takeaway after the framework introduction, not after every paragraph.
- [ ] Use the same component colors in later domain figures.

### D3. Image generation and editing

- [ ] Add a chapter map covering compositional generation, iterative editing/restoration, planning/tool use, stateful creation, multi-agent systems, native/unified models, data/evaluation/safety.
- [ ] Add representative pipelines for: compositional correction, model/tool routing, stateful editing, multi-agent editing, and self-improvement.
- [ ] Add a compact method matrix with columns such as `Task`, `Main action`, `Evidence`, `Adaptation locus`, and `Reported outcome`.
- [ ] Preserve the detailed paper coverage while making each paper paragraph easier to scan.

### D4. Video, film, and animation

- [ ] Add a video production pipeline: script/storyboard -> shot or scene planning -> generation -> temporal inspection -> local correction -> assembly.
- [ ] Highlight identity, temporal continuity, audio-visual consistency, motion, and editable timeline state.
- [ ] Add a comparison table for planning, execution, diagnosis, temporal verification, recovery, and skill reuse.

### D5. 3D, CAD, and world generation

- [ ] Add an editable-representation figure showing scene graphs, CAD programs, geometry, renderings, and simulator evidence.
- [ ] Add a pipeline for executable CAD or world construction: intent -> program/scene representation -> execution/rendering -> geometry or simulation checks -> revision.
- [ ] Add a short comparison table distinguishing appearance evidence, structural evidence, geometric evidence, and executable evidence.

### D6. Scientific visualization

- [ ] Add a data-to-visualization pipeline: source data -> transformation -> chart/figure specification -> rendering -> semantic/data/visual checks -> revision.
- [ ] Highlight factual fidelity, data mapping, legibility, structural correctness, and domain expert review.
- [ ] Add one visual example only when the source and interpretation are verified.

### D7. Structured documents and presentations

- [ ] Add a document pipeline: requirements -> source/layout representation -> rendering -> parser/layout/content checks -> page-level revision.
- [ ] Show why source representations, rendered pages, and executable/parser feedback form different evidence channels.
- [ ] Add a table comparing page appearance, source structure, cross-page consistency, and delivery checks.

### D8. UI and Web generation

- [ ] Add a spec-to-interface pipeline: visual or textual specification -> code/component structure -> browser rendering -> DOM/interaction checks -> repair.
- [ ] Highlight screenshot fidelity, layout, interaction behavior, state transitions, and browser-grounded verification.
- [ ] Add a compact table separating visual evaluation from executable behavior evaluation.

### D9. Cross-domain workflows

- [ ] Keep this chapter short and use it as a visual synthesis chapter.
- [ ] Add one cross-domain matrix showing artifact, tool, state, evidence, and action differences.
- [ ] Add a figure showing how one AVG trajectory may cross media, tools, and execution environments.
- [ ] Avoid repeating all domain examples already discussed in Chapters 4-9.

### D10. Training

- [ ] Add a training taxonomy figure based on update target and persistence: generator/controller/router/critic updates, trajectory supervision, preference learning, reinforcement learning, memory/skill updates, and cross-task transfer.
- [ ] Add a table distinguishing `what changes`, `where the update persists`, `what evidence supports the claim`, and `main risk`.
- [ ] Add one key takeaway stating that training claims require matched budgets and evidence of changed later behavior.

### D11. Evaluation

- [ ] Place the four-level evaluation figure at the chapter opening.
- [ ] Add a table mapping evaluation target to evidence source, typical metric, and known limitation.
- [ ] Add a short box summarizing why final-artifact quality cannot represent the complete creation process.
- [ ] Keep `Remaining Evaluation Gaps` as the chapter synthesis and avoid adding a fifth evaluation category.

### D12. Frontiers

- [ ] Keep the three top-level directions visually prominent.
- [ ] Use subsection headings that are easy to locate in the contents page.
- [ ] Add a roadmap figure, but keep the body prose focused on high-level problems.
- [ ] Do not add literature citations to the Frontier chapter unless the writing policy is changed explicitly.

## 6. Workstream E: Key Takeaway and Callout Boxes

### E1. Box types

Use a small, consistent set of boxes:

- `Key Takeaway`: a concise conclusion that a reader can retain.
- `Definition`: a formal or operational definition that readers may need to find quickly.
- `Evidence Boundary`: what a paper or category demonstrates according to the survey's criteria.
- `At a Glance`: a short chapter or subsection orientation.

### E2. Box rules

- [ ] Use at most one prominent box per major subsection unless the subsection is unusually long.
- [ ] Keep each box to 2-5 short points or a short paragraph.
- [ ] Give each box a specific title, such as `Key Takeaway: Observation-Dependent Control`.
- [ ] Put the box near the concept it summarizes.
- [ ] Avoid repeating the body paragraph verbatim.
- [ ] Use citations inside a box when the statement is paper-specific.
- [ ] Mark survey-level synthesis as synthesis; do not present it as a claim from one paper.

### E3. Suggested initial boxes

- [ ] AVG is defined by an observation--action dependency, not by the number of tools or agents.
- [ ] The same six analytical components can be realized through very different architectures.
- [ ] Editable representations expose evidence that pixel-only workflows cannot provide.
- [ ] Cross-task self-improvement requires a later-task behavior change and transfer evidence.
- [ ] Final-artifact quality and trajectory quality answer different evaluation questions.
- [ ] A useful frontier concerns the operating condition and evidence of control, not just a larger model.

## 7. Workstream F: Figures and Tables to Assign to Collaborators

Use role labels until collaborator names are confirmed.

### F1. Lead designer and visual editor

- Own the color palette, typography, box style, figure template, caption style, and cover page.
- Produce the AVG operating trajectory figure and the six-component framework figure.
- Maintain the source files and export consistent PDF/PNG assets.

### F2. Image, video, and animation figure owner

- Produce the image-generation/editing pipeline figure.
- Produce the video/animation production and temporal-verification pipeline.
- Prepare the method matrices for Chapters 4 and 5.
- Verify every named method and figure citation used in these visuals.

### F3. 3D/CAD, scientific visualization, and document figure owner

- Produce the editable-representation figure for 3D/CAD/world generation.
- Produce the data-to-visualization pipeline.
- Produce the structured-document/presentation pipeline.
- Prepare the evidence-source comparison tables for Chapters 6-8.

### F4. UI/Web, training, evaluation, and frontier figure owner

- Produce the spec-to-browser verification pipeline.
- Produce the training and cross-task improvement taxonomy.
- Produce the four-level evaluation overview.
- Produce the high-level frontier roadmap.

### F5. Citation and provenance checker

- Maintain a figure ledger with `figure ID`, `source paper`, `original/redrawn`, `license or permission`, `citation`, `creator`, and `version`.
- Check that every reused or adapted visual asset has a source and caption note.
- Check that statistics and timeline points have reproducible sources.

### F6. LaTeX integration and visual QA owner

- Integrate figures and boxes without changing the scientific wording.
- Check float placement, figure readability, table width, caption style, page breaks, and references.
- Compile the full PDF after every batch of changes.
- Render representative pages: cover, contents, Chapter 3, one domain chapter, Training, Evaluation, Frontiers, and references.

## 8. Workstream G: Content and Navigation Refinement

- [ ] Add a one-sentence orientation at the start of each major chapter.
- [ ] Add a short `At a Glance` table or box for long chapters.
- [ ] Review chapter titles for directness and consistency.
- [ ] Use third-level headings where a reader would otherwise need to search inside a 20-30 page chapter.
- [ ] Keep shorter chapters at the second-level heading when further subdivision would create noise.
- [ ] Make method categories visible before individual paper paragraphs.
- [ ] Use repeated comparison fields across domain chapters: artifact, state, action, evidence, adaptation, and evaluation.
- [ ] Shorten repeated explanations of the six components after the framework chapter.
- [ ] Move detailed paper-specific evidence into tables or compact method cards where prose becomes difficult to scan.
- [ ] Preserve the existing writing rules: no invented claims, no unsupported citations, no defensive filler, no uncontrolled terminology changes, and open-ended wording for non-exhaustive lists.

## 9. Workstream H: Responsible Figure Reuse

- [ ] Prefer original diagrams or clean redraws for classic pipelines.
- [ ] If a figure is copied or adapted, record the exact source, license, and required attribution before inclusion.
- [ ] Cite the original method in the caption and in the bibliography.
- [ ] Do not remove or alter a figure's factual labels in a way that changes its meaning.
- [ ] Keep a separate folder for source assets and editable redraw files.
- [ ] Use consistent notation across redrawn figures so the paper reads as one survey rather than a collage of unrelated figures.

## 10. Execution Order

### Phase 0: Baseline and reference audit

- [ ] Confirm the intended reference PDF/version.
- [ ] Freeze the current manuscript as a backup before layout changes.
- [ ] Inventory existing tables, figures, packages, fonts, and build settings.
- [ ] Create the figure ledger and naming convention.

### Phase 1: Visual system and navigation

- [ ] Implement cover-page structure.
- [ ] Define typography, colors, headers, captions, table rules, and box styles.
- [ ] Adjust contents-page depth and chapter-opening structure.
- [ ] Compile a short visual prototype containing the cover, contents, one box, one table, and one diagram.

### Phase 2: Core figures

- [ ] Produce the AVG evolution, operating trajectory, six-component, domain map, training, evaluation, and frontier figures.
- [ ] Review all core figures as a group for consistent notation and color semantics.

### Phase 3: Domain figures and tables

- [ ] Complete Chapters 4-10 figures and method matrices.
- [ ] Complete Training and Evaluation figures and tables.
- [ ] Add only the necessary chapter-level boxes.

### Phase 4: Content navigation pass

- [ ] Review headings and third-level divisions.
- [ ] Add or revise `At a Glance`, `Definition`, and `Key Takeaway` boxes.
- [ ] Shorten the abstract and remove duplicate navigation text.

### Phase 5: Integration and visual QA

- [ ] Compile the full document.
- [ ] Check all figure/table references and captions.
- [ ] Render representative pages and inspect readability at normal zoom and printed size.
- [ ] Check for overfull boxes, clipped figures, unreadable labels, float collisions, blank pages, and inconsistent section markers.
- [ ] Run a final citation, bibliography, and figure-provenance audit.

## 11. Definition of Done

- [ ] Cover page contains the lab logo, title, authors/affiliations, version/date, and a repository placeholder.
- [ ] Abstract is concise and matches the final paper structure.
- [ ] Contents page supports fast navigation to research domains and major themes.
- [ ] At least one overview figure explains AVG and one figure explains the six analytical components.
- [ ] Each long domain chapter has at least one useful pipeline or comparison table.
- [ ] Training, Evaluation, and Frontiers each have a clear visual overview.
- [ ] Key takeaways are present at high-value locations and do not duplicate the prose mechanically.
- [ ] All collaborators' figures use the shared template and notation.
- [ ] Every reused/adapted visual has a source and attribution record.
- [ ] Final PDF compiles successfully and representative pages pass visual inspection.
