# Goal Understanding, Specification, and Planning: Literature-Based Review Plan

## 1. Review target

This document reviews the organization of `Goal Understanding, Specification, and Planning` in Chapter 3. It is a planning document for a later revision of the subsection; it does not replace the current TeX text.

The subsection must explain how a visual-generation request becomes an operational basis for later actions. It should cover the transition from user information to a task representation, from that representation to a plan, and from new information to a revised remaining plan. It should keep state storage, tool execution, verification, recovery, stopping, and cross-task learning in their designated modules.

## 2. Sources and verification status

### Local surveys and project documents

- `paper_writing_preferences.md`
- `agentic_visual_generation_terminology_standard.md`
- `overleaf_agentic_visual_generation/sections/02_foundations.tex`
- `overleaf_agentic_visual_generation/sections/03_operating_loop.tex`
- `Agentic_Visual_Generation综述详细结构与写作指引.md`
- `2402.15116_Large_Multimodal_Agents_A_Survey.pdf`
- `2504.18875_Generative_to_Agentic_AI_Survey_Conceptualization_and_Challenges.pdf`
- `2505.19101_Agentic Visualization_ Extracting Agent-based Design Patterns from Visualization Systems.pdf`
- 本地文献归档（未随公开包上传）中的分类与综合报告

### What the local surveys actually organize

The local `Large Multimodal Agents` survey organizes planning through four perspectives: planner model, plan format, inspection and reflection, and planning method. It distinguishes natural-language plans, program-like plans, and hybrid plans; it also distinguishes plans that remain fixed after initial decomposition from plans formulated from current environmental information or feedback.

The local `Generative to Agentic AI` survey places decomposition, reflection, and planning/search next to one another. It describes decomposition as breaking a task into subtasks, planning as finding an action sequence, hierarchical planning as refining high-level steps into lower-level actions, and tool selection as a separate tools topic.

The local `Agentic Visualization` paper organizes agentic systems through role patterns, communication patterns, and coordination patterns. This is an architecture and interaction organization, not a task-specification taxonomy.

The project's terminology standard defines the following terms for this subsection:

- `operational specification`: a representation that turns goals, references, constraints, assumptions, and acceptance conditions into executable and verifiable commitments;
- `semantic decomposition`: splitting a complex goal into checkable subgoals;
- `production planning`: arranging production stages and their order;
- `tool planning`: selecting an executor and constructing its required input;
- `reactive planning`: modifying the remaining trajectory after a failure, new observation, or new user instruction.

These definitions are useful analytical fields for this survey. They should be presented as the survey's organizing vocabulary, not as a four-part taxonomy claimed to be standard across the literature.

### Online-search status

An attempted Google Scholar search and an attempted arXiv search were blocked by the current in-app browser security policy. No unverified web snippet, author list, venue, DOI, or mechanism claim is included in this document. The evidence below comes from local survey PDFs, local original PDFs, the project's evidence reports, and the current Bib entries. Before submission, the citation metadata should still be checked against Google Scholar, the publisher page, ACL Anthology, or the official arXiv record when access is available.

## 3. Main finding about the current organization

The current order is directionally correct:

`task information and unresolved items -> operational specification -> specification update -> planning -> representative systems`.

This order agrees with the strongest local primary evidence. `From Idea to CAD` explicitly separates interactive requirements elicitation from CAD planning. `LightVA` separates high-level analytical goals, task decomposition, and execution planning. `Divide and Conquer` separates prompt decomposition from planning and tool use. `GenArtist` separates requirement decomposition from a planning tree. `NEWTON` identifies a specification bottleneck before describing a planner that selects tools and later replans from verifier scores.

The current text nevertheless needs four conceptual corrections:

1. It presents four planning forms as if they were an established literature classification. They should be introduced as recurring analytical dimensions used in this survey.
2. It mixes specification representation with state representation and execution-interface properties. Provenance and persistent availability belong primarily to `State Representation and Memory`; executable inputs and returned statuses belong primarily to `Tool-Augmented Action and Execution`.
3. It places verification-triggered backtracking and repair details inside the planning paragraph. The planning subsection may describe the plan revision interface, but the verification result and recovery action belong to the later modules.
4. Several representative papers are reused in later subsections. A final revision should assign each paper a primary analytical role and repeat it only when a different, non-duplicated claim is necessary.

## 4. Recommended paragraph organization

### 4.1 Task information and goal understanding

**Function.** Explain what the component receives and what must be resolved before a plan can be formed. The input may include a user request, references, interaction history, domain requirements, and information retrieved during the task. Goal understanding identifies the intended outcome, relevant entities or operations, and unresolved information that affects later choices.

**Keep abstract.** Do not enumerate camera parameters, shot lists, CAD dimensions, chart encodings, or interface events in the general definition. Those details belong in paper-specific descriptions.

**Evidence candidates.** `From Idea to CAD` provides explicit requirement elicitation and ambiguity clarification. `SearchGen` addresses missing generator-specific knowledge and the decision to retrieve external information. `MetaPoint` converts free-form spatial instructions into structured object-level commands.

**Boundary.** Goal understanding is not yet a plan, tool call, verification result, or memory store. It identifies what the task requires and what remains unclear.

### 4.2 Operational specification

**Function.** Define the representation produced after goal understanding. It records the goal, references, constraints, priorities, assumptions, and acceptance conditions in a form that later planning and checking can use.

**Evidence candidates.** `From Idea to CAD` passes clarified requirements to the CAD engineer. `NEWTON` frames underspecified physical conditioning as a specification bottleneck and evaluates whether the conditioning covers the variables needed for physical generation. `Divide and Conquer` converts complex compositional text into object and relation information used by later layout generation.

**Boundary.** The specification is a task commitment record. It is not the persistent memory architecture itself, and it is not the executable program produced by a tool. Do not claim that every paper explicitly constructs an operational specification; use the term as the survey's abstraction when the paper provides equivalent records.

### 4.3 Specification updates and unresolved information

**Function.** Explain how missing or uncertain information is handled before or during planning. The component may request clarification, record a provisional assumption, retrieve information, or defer a dependency until later evidence is available. A specification update can change the remaining subgoals, dependencies, or acceptance conditions.

**Evidence candidates.** `From Idea to CAD` iteratively resolves requirements ambiguities with the user. `SearchGen` decides when search is needed and reports risks from indiscriminate retrieval. `NEWTON` obtains additional physics-related conditioning through specialized tools and uses verifier results in a later planning cycle.

**Boundary.** A clarification request is an input action in the trajectory; it is not evidence of autonomous diagnosis. A retrieved fact is not automatically a verified constraint. A specification update is not cross-task self-improvement.

### 4.4 Plan construction

**Function.** Explain how a current specification is converted into a structured remaining trajectory. The plan can contain subgoals, action order, dependencies, executor choices, required inputs, and intended observation points.

**Recommended analytical dimensions.** Introduce the following as dimensions of plan content, not as a universal taxonomy:

- **Semantic decomposition:** what subgoals or units must be addressed;
- **Production ordering:** in what order the operations are carried out;
- **Executor assignment:** which available operation or executor is associated with each step;
- **Dependency structure:** which steps require results, conditions, or references from earlier steps;
- **Observation points:** where the trajectory expects a result or check before continuing.

**Evidence candidates.** `Divide and Conquer` decomposes compositional prompts and plans layout-oriented operations. `GenArtist` represents operations and alternative tools in a planning tree. `LightVA` recursively decomposes analytical requests into executable data and visualization tasks. `From Idea to CAD` turns clarified requirements into a coarse modeling plan. `T2I-Copilot` structures prompt interpretation and model routing across specialized agents.

**Boundary.** The plan states intended actions and dependencies. It does not itself establish that a result satisfies a constraint. Verification and diagnosis are separate functions.

### 4.5 Plan adaptation

**Function.** Explain how new user information or runtime evidence changes the remaining plan. The change may affect subgoals, action order, executor selection, inputs, or the branch that remains active.

**Evidence candidates.** `GenArtist` provides a planning-tree example in which step-wise checks affect later traversal. `NEWTON` uses verifier scores to select another physics-conditioning cycle. `Divide and Conquer` uses feedback to refine a compositional result. These papers should be described with their precise evidence and should not be generalized into a universal recovery architecture.

**Boundary.** This paragraph describes the planning interface with observation and recovery. It should not repeat the verifier's scoring mechanism, the diagnosis taxonomy, rollback implementation, or stopping policy. Those belong to `Observation, Diagnosis, Verification, and Feedback` and `Recovery, Stopping, and Human Authority`.

## 5. Suggested paper allocation

| Analytical role | Preferred primary papers | Reason for use |
|---|---|---|
| Goal understanding and ambiguity | From Idea to CAD; SearchGen | Requirement clarification and information-gap handling |
| Operational specification | From Idea to CAD; NEWTON | Explicit requirements transfer and specification bottleneck |
| Semantic decomposition | Divide and Conquer; LightVA | Object/relation decomposition and recursive analytical decomposition |
| Plan structure | GenArtist; LightVA | Planning tree and executable task decomposition |
| Executor assignment | DiffusionAgent; T2I-Copilot | Model routing and specialized-agent routing |
| Plan adaptation | GenArtist; NEWTON; Divide and Conquer | Evidence-dependent traversal, replanning, or refinement |

Avoid using `AutoStudio` in this subsection if it is retained as a primary example in `State Representation and Memory`. Avoid using `From Idea to CAD`, `LightVA`, `GenArtist`, or `NEWTON` again in later sections unless the later sentence concerns a different mechanism and adds non-redundant evidence.

## 6. Recommended revision outline for the TeX subsection

The revised subsection should use the following sequence:

1. One short opening paragraph: input, processing, and output of the component.
2. `Task information and goal understanding`: identify the intended outcome and unresolved items.
3. `Operational specification`: define the task commitments used by later planning.
4. `Specification updates`: explain clarification, assumptions, retrieval, and unresolved dependencies.
5. `Plan construction`: define subgoals, order, dependencies, executor assignment, and observation points.
6. `Plan adaptation`: describe how new information changes the remaining plan, with a strict interface to observation and recovery.
7. A compact synthesis sentence only if needed; do not add a table or a mechanical preview of the next component.

## 7. Sentence-level constraints

- Start each paragraph with the abstract principle, then cite papers as evidence.
- Use `this component` or the exact paper role; do not introduce an unnamed `controller`, `planner`, or `manager` as a universal architecture.
- Keep `operational specification`, `semantic decomposition`, `production planning`, `tool planning`, and `reactive planning` consistent with the terminology standard.
- State that the four planning forms are analytical dimensions of this survey if they are retained.
- Avoid defensive contrasts such as `rather than`, `not only`, and `does not by itself`.
- Do not claim that a paper demonstrates planning merely because it produces a prompt, a chain of thought, or a fixed sequence of tool calls.
- Do not claim feedback adaptation unless a reported observation or user input changes a later action, plan, route, or branch.
- Do not treat tool count, agent count, or plan length as evidence of autonomy.
- Keep verification, diagnosis, recovery, stopping, human authority, and cross-task self-improvement in their assigned modules.

## 8. Final assessment

The current subsection has the correct high-level direction and a useful abstraction vocabulary. Its main weakness is not the order of the first two paragraphs; it is the presentation of a survey-specific planning vocabulary as if it were a settled literature taxonomy and the overlap with state, execution, verification, and recovery. The revision should retain the progression from task information to specification to planning, explicitly label the intermediate dimensions as analytical categories, and use literature examples only after each mechanism has been defined.
