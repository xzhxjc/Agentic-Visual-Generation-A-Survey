# Perception, Action, and Cross-Task Self-Improvement Section Plan

> **For writing agents:** Use this plan to rewrite the later operating-loop modules in `overleaf_agentic_visual_generation/sections/03_operating_loop.tex`. Complete the citation ledger and source checks before drafting the正文. Steps use checkbox syntax for tracking.

**Goal:** Reorganize the last three operating-loop modules as `Perception`, `Action`, and `Cross-Task Self-Improvement`, with explicit paragraph-level content, source assignments, cross-module boundaries, and shared writing rules.

**Architecture:** `Perception` obtains and interprets information about the artifact, execution process, environment, references, and interaction. `Action` performs operations that change an artifact, environment, available information, interaction history, or control trajectory; feedback is treated as an ordinary evidence-conditioned action inside this module. `Cross-Task Self-Improvement` turns completed trajectories into reusable cases, strategies, skills, routers, verifiers, or other future-task behavior updates.

**Tech Stack:** LaTeX source in `sections/03_operating_loop.tex`, BibTeX in `references.bib`, and a separate local literature archive that is not included in the public package.

---

## 1. Scope and final module map

The current Chapter 3 opening uses six components:

1. Goal Understanding, Specification, and Planning
2. Memory
3. Tool Definition, Selection, and Execution
4. Observation, Diagnosis, Verification, and Feedback
5. Recovery, Stopping, and Human Authority
6. Cross-Task Self-Improvement

The revised opening should use:

1. Goal Understanding, Specification, and Planning
2. Memory
3. Tool Definition, Selection, and Execution
4. Perception
5. Action
6. Cross-Task Self-Improvement

The new names are an analytical organization authored by this survey. They must not be described as a universal architecture adopted by all agent papers.

### 1.1 Module boundaries

**Goal Understanding, Specification, and Planning** defines the task target, constraints, assumptions, dependencies, subgoals, and intended order of work.

**Memory** defines information retained and later retrieved, including task-local records, prior attempts, provenance, and reusable records.

**Tool Definition, Selection, and Execution** defines callable interfaces and their inputs, outputs, execution status, errors, and interface metadata.

**Perception** obtains and interprets signals. It includes observation, diagnosis, and verification as successive functions:

- observation acquires task-relevant signals;
- diagnosis relates signals to possible causes and affected locations;
- verification checks stated requirements or acceptance conditions.

**Action** performs the operation selected at a decision point. It includes artifact changes, information acquisition, code and application operations, environment interaction, coordination, evidence-conditioned feedback, recovery, replanning, stopping, and human-facing actions.

**Cross-Task Self-Improvement** updates reusable behavior for later tasks. It includes experience selection, abstraction, skill or strategy construction, retrieval, policy/router/verifier updates, and transfer evaluation.

Feedback follows the same Action analysis: content from Perception is sent or applied through an operation such as a prompt update, editor request, routing input, role message, or human-facing report.

### 1.2 Tool and Action boundary

Tool describes the callable boundary. Action describes what the system does through a tool, application, runtime, simulator, communication channel, or other execution substrate and what changes as a result. A tool call is therefore one kind of Action; Action also includes operations that do not require a separately named tool interface.

## 2. Literature basis for the reorganization

### 2.1 General agent surveys

`Large Multimodal Agents: A Survey` presents four core elements: perception, planning, action, and memory. Its action discussion covers tool use, physical or embodied operations, and virtual interface operations. Its diagrams connect environment results back to perception and planning. Use this survey to support the broad Perception/Action split, not to claim that its action categories are the only valid taxonomy for visual generation.

`Generative to Agentic AI: Survey, Conceptualization, and Challenges` organizes agentic AI around reasoning, memory, tools, and interaction. Reasoning contains decomposition, reflection, planning/search, and learning to reason. Tools contain creation, selection, and use. Interaction contains virtual worlds, humans, and other agents. Its reflection discussion separates verification, which assesses intermediate or final results, from refinement, which changes later outputs using available feedback.

`Agentic Visualization` organizes visual-analytics systems through role, communication, and coordination patterns. Monitoring, provenance logs, progress indicators, insight timelines, scouting, and consolidation provide evidence for treating information acquisition, communication, and coordination as operational actions around a visual artifact.

### 2.2 Agent-memory survey

The local agent-memory survey uses two temporal domains and three functional pillars:

- short-term and long-term memory;
- factual memory for declarative information;
- experiential memory for prior cases, strategies, and skills;
- working memory for the active task context.

It further divides experiential memory by abstraction level:

- case-based memory retains prior episodes or trajectories;
- strategy-based memory distills rules, workflows, patterns, or heuristics;
- skill-based memory compiles executable procedures, functions, code, APIs, or standardized interfaces.

Use this taxonomy to organize the cross-task section. It is evidence about memory and experience abstraction in agent research; it does not show that every visual-generation system implements every category.

### 2.3 Local visual-generation evidence families

The local corpus provides evidence for the three revised modules:

- Perception and verification: GenArtist, PreGenie, CRAFT, Gen-n-Val, CAD-Judge, CADSmith, IterCAD, PhysAgent, NEWTON, PlotGen, METAL, AMACE, and related systems.
- Action: GenClaw, TOOLCAD, CAD-Assistant, LightVA, DiffusionAgent, AMACE, PlotGen, METAL, Mora, GenMAC, Kubrick, code/application systems, retrieval systems, and environment-based systems.
- Cross-task improvement: COMFYCLAW, GenEvolve, OctoT2I, DataEvolver, VideoWeaver, Maestro, SIDiffAgent, EvoIR-Agent, the self-evolving restoration papers, and the self-improving video papers.

These are candidate evidence families, not a license to cite every paper. Each retained paper must have one primary claim, one target module, and a verified source location.

## 3. Module 4: Perception

### 3.1 Opening definition paragraph

Begin the subsection with the input-process-output relation:

- input: rendered artifact, editable representation, execution result, task environment, reference, user interaction, or another task-relevant signal source;
- processing: acquisition, extraction, comparison, localization, interpretation, or requirement checking;
- output: structured evidence available to a later Action.

Define Perception as information processing for the running visual-creation trajectory. Keep the definition broad enough for images, video, 3D/CAD, scientific visualization, structured documents, UI/Web creation, and related visual products.

Do not define Perception as only pixel recognition. Code, geometry, data, compiler output, simulator state, application state, retrieval results, and human input can also be perception sources when the system uses them to understand the current task state.

### 3.2 Paragraph 1: Signal acquisition and observation

Explain how the system obtains signals before interpreting them. Cover the following mechanisms in a continuous paragraph:

- passive sampling of every output or a fixed interval;
- scheduled checks at known risk points;
- active selection of a crop, frame range, reference, test, or rollout;
- source-level inspection of code, layouts, scene graphs, geometry, or data;
- runtime inspection of compiler, renderer, browser, application, or simulator output;
- retrieval of external information when it supplies a needed reference.

Explain the comparison dimensions:

- coverage: which failure or requirement classes can be seen;
- timing: when the signal becomes available relative to dependent work;
- localization: whether it identifies a region, frame, object, component, or operation;
- cost: rendering, model calls, simulation, retrieval, or human time.

Use open-ended lists with `such as`, `among related channels`, or `and other task-relevant signals`.

Possible evidence candidates include CAMEO for conditional external guidance, SearchGen for knowledge-sensitive retrieval, Kubrick for render inspection, PreGenie for source/page inspection, and PhysAgent or NEWTON for simulation or physical evidence. Assign each paper only if its original report supports the exact observation claim and if the citation is not being used for the same fact elsewhere.

### 3.3 Paragraph 2: Interpretation and diagnosis

Explain how acquired signals become an interpretation of the current artifact or failure state. Diagnosis should connect a signal to:

- a requirement or property under consideration;
- an observed violation, uncertainty, or mismatch;
- an affected region, frame, object, component, or operation;
- a possible source or cause;
- confidence or competing hypotheses when reported.

Use symptom/cause examples after the mechanism:

- a low image-quality score indicates a problem but does not locate a repair target;
- a missing object localized to a region can support a region-level edit;
- a compiler message associated with a code block can support a source-level correction;
- a geometry report can distinguish a dimensional defect from a rendering defect.

Keep diagnosis separate from Action. Perception identifies and interprets the issue; Action chooses and performs the response.

### 3.4 Paragraph 3: Verification and acceptance evidence

Define verification as checking an explicit requirement, acceptance condition, or property of the current result. Organize targets by what is checked:

- perceptual and semantic correspondence;
- relational, spatial, and geometric validity;
- temporal continuity and identity consistency;
- data, factual, and numerical fidelity;
- executable behavior and structural validity;
- physical plausibility under a modeled environment;
- human acceptance when human review is part of the reported system.

Explain that different targets require different evidence. A visual-language judge, OCR test, compiler, geometry kernel, simulator, reference comparison, exact numerical test, and human review answer different questions. Describe verifier portfolios, uncertainty, disagreement, granularity, coverage, latency, and scheduling. Do not state that one verifier establishes all properties.

Candidate evidence includes Gen-n-Val, CAD-Judge, PreGenie, PhysAgent, NEWTON, PlotGen, METAL, and CRAFT. GenArtist may be used for intermediate verification only if its planning-tree fact is not duplicated from the earlier planning discussion; otherwise assign another verified paper.

### 3.5 Paragraph 4: Evidence output for later Action

End Perception by describing the output that becomes available to Action. It may contain a score, pass/fail or graded status, failed requirement, location, likely cause, uncertainty, supporting observation, or candidate target. Do not describe a repair or feedback operation in this paragraph. The next module uses this output to perform a selected action, which may modify an input, call a tool, edit a source, communicate a result, request more evidence, recover, continue, escalate, or stop.

### 3.6 Perception citation allocation

Build the ledger before drafting. Recommended primary claims are:

- CAMEO or SearchGen: conditional signal acquisition;
- Gen-n-Val: acceptance and rejection criteria for generated data;
- CAD-Judge: morphology and compiler evidence;
- PreGenie: source and rendered-page inspection;
- PlotGen or METAL: multimodal chart evidence and code review;
- PhysAgent or NEWTON: simulation and physical evidence;
- CRAFT: constraint-level visual assessment.

Use no citation when the sentence is the survey's own abstract definition. Do not reuse a paper already assigned to Goal, Memory, Tool, Action, or a domain section for the same sentence-level fact.

## 4. Module 5: Action

### 4.1 Opening definition paragraph

Define Action as an operation selected at a decision point that changes one or more of the following:

- the visual artifact or editable representation;
- the external environment or application state;
- the information available for later decisions;
- the interaction history or communication state;
- the control trajectory, including route, continuation, recovery, or stopping.

Action receives the current goal/specification, Memory records, artifact/environment state, available Tool interfaces, and Perception evidence. It returns a changed artifact or state, execution result, communication result, or control update.

State that the action space is open-ended. Tool invocation is one action substrate; code execution, application interaction, retrieval, simulator steps, role handoff, human requests, and control decisions are also actions when the system performs them.

### 4.2 Paragraph 1: Artifact actions

Describe actions that create or modify a visual artifact or its editable representation:

- generation, editing, restoration, inpainting, compositing, and transformation;
- rendering, compilation, export, and format conversion;
- geometry construction, parameter editing, scene assembly, and simulation-backed creation;
- chart, document, presentation, UI, and Web source modification.

Use examples that show input and output:

- prompt/reference image to generated image;
- source frame/region/edit instruction to revised frame;
- parametric CAD program to geometry and execution status;
- data/source code to figure and transformed data;
- presentation or Web source to rendered pages or updated interface state.

End open lists with `and related artifact operations`.

### 4.3 Paragraph 2: Information acquisition actions

Describe operations whose immediate output is information for a later action:

- search and retrieval of references or external knowledge;
- data queries and analysis calls;
- source-code, file, browser, application, or environment inspection;
- rendering crops, previews, frame ranges, or diagnostic views;
- invocation of perception or analysis services.

Keep the boundary explicit: the Action performs the retrieval, query, inspection, or call; Perception interprets the returned signal.

### 4.4 Paragraph 3: Execution and environment actions

Describe actions over execution substrates:

- model and API calls;
- code execution in a runtime or sandbox;
- application and browser operations;
- renderer and compiler invocation;
- simulator steps and task-environment interaction;
- physical or virtual environment operations when a visual-generation system reports them.

Use Tool section terminology for callable interfaces, but discuss here what the call does and what changes. Candidate evidence includes TOOLCAD, CAD-Assistant, LightVA, GenClaw, and domain systems that expose executable source or environment state. Avoid repeating the same sentence-level facts used in Tool Definition, Selection, and Execution.

### 4.5 Paragraph 4: Communication and coordination actions

Describe operations that move information between roles or authority boundaries:

- delegation, message passing, synchronization, aggregation, and role handoff;
- sending a generated artifact or structured state to the next role;
- requesting clarification, approval, rejection, or human override;
- reporting progress, status, or a result to a user.

Use Mora, GenMAC, Kubrick, Agentic Visualization, and verified human-in-the-loop systems only for the specific communication or coordination behavior they report.

### 4.6 Paragraph 5: Evidence-conditioned action and trajectory control

Explain how Perception evidence changes a subsequent action. Keep the prose direct and treat feedback naturally as part of this action flow:

- a critique can be sent to a prompt or code generator;
- a failed requirement can be applied to a local edit or revised input;
- an execution error can be passed to a retry or routing decision;
- a result can be communicated to another role or user;
- a verified state can support continuation;
- an unresolved or unsafe state can trigger clarification, escalation, recovery, or stopping.

Then define control actions:

- tool/model/role selection and routing;
- prompt, input, plan, dependency, or parameter update;
- retry, branch, continuation, or path substitution;
- local repair, replanning, rollback, and bounded relaxation;
- stopping, termination, or deferral;
- human authorization, override, or escalation.

Perception supplies the reason or evidence; Action performs the response. Keep the Perception diagnosis out of this paragraph and describe the operation that uses it.

### 4.7 Paragraph 6: Action execution record

Define the record used to compare actions across papers:

- selected operation or interface;
- input representation and parameterization;
- target artifact or environment;
- acting role or executor when reported;
- returned artifact, state, status, error, or communication result;
- cost, latency, reversibility, and side effects when available;
- later action or handoff when a closed-loop dependency is reported.

Do not use the number of tools, agents, calls, or steps as an autonomy claim. Use observed state-to-action changes and reported process evidence.

### 4.8 Action citation allocation

Potential primary assignments are:

- GenClaw: executable image-construction and editing operations;
- TOOLCAD and CAD-Assistant: language-to-CAD execution;
- DiffusionAgent: model selection as an action choice;
- LightVA: visual-analytics planning/execution handoff;
- AMACE, PlotGen, and METAL: chart-code, rendering, critique, and revision operations;
- Mora and GenMAC: multi-agent generation and role handoff;
- Kubrick: direction, programming, Blender execution, and video coordination;
- CADSmith and IterCAD: nested executable and geometric operations when not assigned to Perception or a domain section.

The ledger must prevent repeated citation of the same fact in Tool, Action, and domain sections.

## 5. Module 6: Cross-Task Self-Improvement

### 5.1 Opening definition paragraph

Define Cross-Task Self-Improvement as an update derived from earlier trajectories that changes reusable behavior for a later task. The update may affect a skill library, strategy, workflow, router, retrieval policy, verifier, prompt-construction policy, memory abstraction, or other future-task decision mechanism.

Separate temporal levels without making them rival modules:

- task-local correction changes the current trajectory;
- episodic reuse retrieves an earlier attempt, repair, artifact, or tool trace for a later request;
- cross-task self-improvement changes future behavior and is evaluated on later or held-out tasks.

A stored record, retrieved record, or single improved output is evidence of reuse or task-level adaptation; it becomes evidence of cross-task improvement only when the later behavior and evaluation support that claim.

### 5.2 Paragraph 1: Experience collection

Explain what a completed trajectory can contribute:

- prompt and requirement records;
- references and retrieved information;
- artifacts and editable representations;
- tool calls, execution results, errors, and costs;
- observations, diagnoses, verification results, and critiques;
- repairs, successful branches, failed branches, user corrections, and evaluator judgments.

The system selects records according to relevance, outcome, provenance, scope, reliability, and expected future reuse. It need not preserve every token, frame, or intermediate render.

### 5.3 Paragraph 2: Outcome attribution and update candidates

Explain how the system associates outcomes with actions or trajectories. Distinguish:

- final artifact quality from process evidence;
- a better candidate from a changed policy;
- extra sampling from experience-based improvement;
- same-task reflection from a future-task update.

An update candidate can be a successful case, failure explanation, repair rule, tool-path preference, verifier calibration, prompt-construction rule, workflow, or skill. Avoid causal claims unless the source reports ablation, intervention, held-out transfer, or another process comparison.

### 5.4 Paragraph 3: Abstraction levels of reusable experience

Use the agent-memory survey's abstraction levels as an organizing lens:

- case-based reuse preserves a prior episode for retrieval or replay;
- strategy-based reuse distills rules, workflows, patterns, or heuristics;
- skill-based reuse compiles an executable procedure, function, code fragment, API, or skill interface.

Translate the levels into visual-generation examples only when supported by the source:

- an image-generation workflow case;
- a strategy for reference selection or prompt construction;
- an editing subroutine;
- a chart-generation procedure;
- a CAD repair routine;
- a long-video composition skill.

Do not call a memory summary a skill unless the paper makes it executable or callable.

### 5.5 Paragraph 4: Storage and retrieval

Describe where reusable experience is stored and how later tasks query it. Possible forms include a skill library, experience memory, routing table, policy, prompt bank, executable code repository, or structured feedback library. Retrieval may use task similarity, state fingerprints, artifact properties, tool compatibility, temporal scope, or other query signals when reported.

Keep this paragraph distinct from the Memory subsection: Memory defines retained information generally; this paragraph addresses the cross-task update and reuse of behavior derived from experience.

### 5.6 Paragraph 5: Update and deployment

Explain how the update changes later behavior:

- test-time retrieval or prompt construction;
- external skill/workflow library updates;
- router or tool-path updates;
- verifier or critic updates;
- fine-tuning or reinforcement learning;
- distillation of visual experience into reusable records or procedures.

State the update target, timing, and evaluation setting. A prompt rewrite during the current task is Action; a persistent prompt-construction rule used on later tasks belongs here.

### 5.7 Paragraph 6: Transfer, governance, and evaluation

Explain evidence required for a cross-task claim:

- new requests or held-out task families;
- unseen tool combinations or environments;
- independent evaluators or human judgments;
- forgetting and harmful-update tests;
- ablations separating retrieval, policy update, generator changes, and extra compute;
- provenance, privacy, ownership, rollback, and update reversibility when reported.

The evaluation should identify which later decision changed, such as tool selection, reference retrieval, prompt construction, verification threshold, or repair strategy, in addition to final artifact metrics.

### 5.8 Cross-task evidence candidates

Candidate primary claims from the current Bib and local corpus:

- `avg260701709` COMFYCLAW: reusable skill harnesses for image-generation workflows;
- `chen2026genevolve` GenEvolve: tool-orchestrated visual experience distillation;
- `jiang2026octot2i` OctoT2I: self-evolving text-to-image routing;
- `avg260631537` DataEvolver: verification causes converted into reusable semantic feedback and later construction updates;
- `avg260608091` VideoWeaver: evaluation and evolution of long-video skills;
- `avg250910704` Maestro: self-improving text-to-image generation through agent orchestration;
- `avg260202051` SIDiffAgent: self-improving diffusion-agent behavior;
- `avg260522208` EvoIR-Agent and `avg260628971` self-evolving restoration: experience-driven restoration updates;
- `long2025vista` VISTA: test-time self-improvement for video generation.

Use only papers whose local source supports the exact update mechanism and transfer evidence. Do not force a citation if the source reports only task-local reflection.

## 6. Chapter-level transitions and retained sections

### 6.1 Opening overview update

Replace the current six-component overview with the new names and concise responsibilities. The overview should state that Planning defines intended work, Memory retains information, Tool defines callable interfaces, Perception interprets signals, Action performs operations, and Cross-Task Self-Improvement changes future behavior.

### 6.2 Transition from Memory/Tool to Perception

Use one direct sentence: the preceding modules specify what should be done, what information remains available, and which operations can be called; Perception examines the resulting artifact, execution process, and environment for task-relevant evidence.

### 6.3 Transition from Perception to Action

Use one direct sentence: Perception provides information about the current result and its requirements; Action uses that information to select and perform the next operation. Do not introduce a separate Feedback concept in the transition.

### 6.4 Transition from Action to Cross-Task Self-Improvement

Use one direct sentence: completed actions, outcomes, and associated evidence can be retained and transformed into reusable behavior for later tasks when the system reports such an update.

### 6.5 Cross-component failure modes

Rename old labels as follows:

- Planning-Action: intended subgoals lack executable operations or compatible inputs;
- Memory-Perception: required evidence or provenance is unavailable for interpretation;
- Perception-Action: evidence is unlocalized, ambiguous, or not connected to an available operation;
- Action-Perception: execution returns insufficient status or observation channels;
- Action-Human authority: consequential operations lack an approval or escalation path;
- Action-Cross-Task Self-Improvement: completed trajectories are not converted into a testable future-task update;
- Cross-Task Self-Improvement-Perception: verifier or evaluator updates are not independently assessed.

Keep each failure mode tied to a missing state, action, evidence type, or evaluation condition.

## 7. Shared writing standards

Apply these rules to every paragraph and every chapter revision.

### 7.1 Evidence and claim strength

- Use `reports`, `describes`, `uses`, `evaluates`, or `finds` for single-paper facts.
- Reserve causal wording for ablations, controlled failures, interventions, or explicit process evidence.
- Do not turn a small local literature sample into a whole-field claim.
- Keep a paper's mechanism, result, interpretation, and limitation in separate sentences when one citation would otherwise support unrelated claims.
- If the mechanism or metadata cannot be verified, omit the citation or narrow the sentence.

### 7.2 Principle-first paragraph structure

Every paragraph should proceed as:

1. what the mechanism is;
2. what input it receives;
3. how it processes or executes;
4. what output or state change it produces;
5. what condition or evidence makes the mechanism relevant;
6. paper examples supporting the preceding claim.

Do not begin with a paper name. Do not use papers to define a mechanism before the survey's abstract definition is clear.

### 7.3 Terminology consistency

- Use exact module names: `Goal Understanding, Specification, and Planning`, `Memory`, `Tool Definition, Selection, and Execution`, `Perception`, `Action`, and `Cross-Task Self-Improvement`.
- Use `controller` only for the cross-module decision function defined in Chapter 2.
- Use `executor`, `planner`, `verifier`, `critic`, `agent`, or `manager` only when Chapter 2 or the cited paper defines that role.
- Keep `Tool`, `Action`, `Perception`, `Memory`, `artifact representation`, `context`, `interaction history`, and `provenance` distinct.
- Treat feedback as a normal Action operation when the system sends or applies evidence to a later operation.

### 7.4 Avoid defensive and absolute writing

- Avoid `rather than`, `not only`, `does not by itself`, `not merely`, and repeated `not X but Y` constructions.
- Avoid absolute words such as `all`, `always`, `never`, `only`, `must`, `guarantee`, `prove`, and `ensure` unless the claim is a formal condition or directly supported by the source.
- State the positive mechanism, condition, or evidence requirement directly.
- Do not anticipate a reader's objection and answer it with multiple exclusions.
- Do not use tool count, agent count, call count, model size, or compute as direct evidence of autonomy.

### 7.5 Abstraction and examples

- Define mechanisms broadly enough to cover image, video, 3D/CAD, scientific visualization, structured documents, UI/Web, and related visual products.
- Add concrete examples after the mechanism, not instead of it.
- Use examples to clarify input, operation, output, or failure localization; do not add examples merely to increase length.
- Keep lists open with `and related operations`, `among others`, or `and other task-relevant ...`.
- Do not invent module names, taxonomies, or theoretical claims from a few implementation examples.

### 7.6 Citation and duplicate-use rules

- Use existing Bib entries first.
- Assign each citation a primary module and a primary sentence-level claim.
- Do not repeat a citation in Goal, Memory, Tool, Perception, Action, and Cross-Task Self-Improvement for the same fact.
- A paper may appear in a domain chapter for a distinct domain claim, but the operating-loop sentence must remain distinct.
- Do not add a citation to a pure survey-authored definition unless it directly supports the definition.
- Check citation key existence, BibTeX uniqueness, title, authors, year, venue, DOI, and URL before retaining a source.

### 7.7 Bilingual consistency

- English and Chinese must express the same mechanism, scope, uncertainty, and citation.
- Preserve `may`, `can`, `under the reported setting`, and equivalent qualifiers in both languages.
- Do not add an evaluation result or causal claim in one language only.

## 8. Citation ledger and verification workflow

Before editing the正文, create a ledger with these columns:

`Bib key | title | local PDF/report | exact source location | mechanism | input | output | evaluation evidence | primary module | duplicate status`

Freeze the current citations in the preceding modules before assigning new keys. The current active sections use these keys that must be considered during deduplication:

- Goal: `avg251121087`, `wang2026searchgen`, `wang2024genartist`, `wang2024divide`, `ocker2025ideatocad`, `zhao2024lightva`, `feng2026newton`, `avg260716352`, `avg260515181`, `avg260415917`, `avg260329602`, `zhou2026metapoint`.
- Memory: `ye2026agentbanana`, `xie2024dreamfactory`, `wang2024lave`, `huang2026vimax`, `avg260302697`, `avg260708497`, `avg260626907`, `avg260701709`, `avg260631537`, `avg260608091`, `avg260517969`, `avg260628971`.
- Tool: `ye2026genclaw`, `gong2026toolcad`, `mallis2024cadassistant`, `namgoong2025amace`, `goswami2025plotgen`, `li2025metal`, `qin2024diffusionagent`, `yuan2024mora`, `huang2024genmac`.

Because the current Memory section already uses several self-improvement-related papers, recheck and reassign those keys before drafting the new Cross-Task section. Do not reuse them automatically.

For each proposed paper:

1. Read the local original PDF, report, or official project record.
2. Record the exact operation, input, output, and evidence used by the planned sentence.
3. Check whether the same key already supports another module or domain claim.
4. Compare BibTeX metadata with the local paper and authoritative metadata available in the project.
5. Remove any claim that exceeds the source, especially claims about diagnosis, recovery, skill creation, policy update, or transfer.
6. Compile after drafting and inspect undefined citations, duplicate BibTeX keys, and bibliography warnings.

## 9. Planned file changes and drafting sequence

### Files

- Modify: `overleaf_agentic_visual_generation/sections/03_operating_loop.tex`
  - update the six-component overview;
  - replace the current Observation/Recovery material with Perception and Action;
  - rewrite Cross-Task Self-Improvement around experience-to-behavior transfer;
  - update cross-component failure modes and final references.
- Modify: `agentic_visual_generation_terminology_standard.md`
  - add exact entries for `Perception` and `Action`;
  - define evidence, diagnosis, verification, action space, artifact action, control action, coordination action, and cross-task improvement;
  - describe feedback as an Action operation without creating a separate module.
- Modify: `paper_writing_preferences.md`
  - replace the old six-module list;
  - update 主体、职责和跨模块 boundary rules;
  - add the principle that feedback actions belong inside Action.
- Review/update: `tool_augmented_action_execution_section_plan.md`
  - preserve Tool as interface-level analysis;
  - cross-reference Action as the broader operation layer.
- Create during drafting: citation ledger and source-evidence table in the project root or `tmp`.

### Drafting tasks

- [ ] Freeze the citation ledger for Goal, Memory, and Tool.
- [ ] Update the overview and module names in `03_operating_loop.tex`.
- [ ] Draft Perception in the order signal acquisition -> diagnosis -> verification -> evidence output.
- [ ] Draft Action in the order definition -> artifact actions -> information actions -> execution/environment actions -> coordination actions -> evidence-conditioned control actions -> action record.
- [ ] Draft Cross-Task Self-Improvement in the order experience collection -> attribution -> case/strategy/skill abstraction -> storage/retrieval -> update/deployment -> transfer/governance.
- [ ] Assign one primary claim and one source location to every retained citation.
- [ ] Remove repeated citations and repeated sentence-level facts across Goal, Memory, Tool, Perception, Action, and domain sections.
- [ ] Update shared terminology and writing rules.
- [ ] Update cross-component failure modes and conclusion references.
- [ ] Compile the project and inspect undefined citations, BibTeX warnings, and the rendered chapter.
- [ ] Perform the final absolute-language, defensive-writing, open-list, and bilingual-consistency audit.

## 10. Completion criteria

- The chapter overview names Perception, Action, and Cross-Task Self-Improvement consistently.
- Perception contains definitions and separate paragraphs for acquisition, diagnosis, verification, and evidence output.
- Action contains artifact, information, execution/environment, coordination, and control operations, with feedback naturally included among evidence-conditioned actions.
- Cross-Task Self-Improvement covers collection, attribution, abstraction, retrieval, update, transfer, and governance.
- Tool interfaces remain distinct from the broader Action layer.
- Every paragraph begins with a mechanism and then gives source-backed examples.
- No unsupported absolute, causal, defensive, or whole-field claim remains.
- Lists are open-ended where the category is not closed.
- No citation is duplicated for the same fact across the operating-loop modules.
- Every retained citation key exists and every BibTeX record has been checked against available source metadata.
- LaTeX compiles without undefined citations or BibTeX errors.
