# Revised Plan: Goal Understanding, Specification, and Planning

## 1. Scope

This subsection should answer one question:

> How does a visual-generation request become a task representation and a plan that can guide later creation actions?

The subsection includes four closely related stages:

1. understanding the intended goal and identifying unresolved information;
2. constructing an operational specification;
3. forming a plan from that specification;
4. revising the remaining plan when new task information changes the commitments or dependencies.

The subsection should not become a general description of the AVG loop. It should not explain how tools execute, how verifiers diagnose an artifact, how recovery rolls back a branch, how a system stops, or how completed tasks update future policies. Those topics belong to the other five components.

## 2. Evidence base

### Local project documents

- `paper_writing_preferences.md`
- `agentic_visual_generation_terminology_standard.md`
- `overleaf_agentic_visual_generation/sections/02_foundations.tex`
- `overleaf_agentic_visual_generation/sections/03_operating_loop.tex`
- `Agentic_Visual_Generation综述详细结构与写作指引.md`
- 本地文献归档（未随公开包上传）中的分类与综合报告

### Local survey papers

The local `Large Multimodal Agents: A Survey` organizes planning through planner models, plan formats, inspection and reflection, and planning methods. It distinguishes natural-language plans, program-like plans, and hybrid plans. It also compares plans formed from the initial input with plans formed from current environmental information or feedback.

The local `Generative to Agentic AI: Conceptualization and Challenges` discusses decomposition, reflection, and planning/search as adjacent reasoning capabilities. It describes decomposition as splitting a task into subtasks, planning as finding an action sequence, and hierarchical planning as refining high-level steps into lower-level actions.

The local `Agentic Visualization: Extracting Agent-based Design Patterns from Visualization Systems` organizes systems by role, communication, and coordination patterns. This is useful for the later architecture discussion, but it should not determine the organization of this goal-and-planning subsection.

### Local original papers relevant to this subsection

The strongest directly relevant examples currently available in the project are:

- `From Idea to CAD` (arXiv:2503.04417): interactive requirements elicitation precedes a coarse CAD modeling plan;
- `Divide and Conquer` (arXiv:2401.15688): complex compositional prompts are decomposed before planning and tool use;
- `GenArtist` (arXiv:2407.05600): the agent decomposes a request and represents planned generation/editing operations in a tree;
- `LightVA` (arXiv:2411.05651): high-level analytical goals are decomposed into executable data and visualization tasks;
- `NEWTON` (arXiv:2605.18396): underspecified physical conditioning is treated as a specification bottleneck, and a planner selects conditioning tools and later replans from verifier scores;
- `SearchGen` (the project key `wang2026searchgen`): the system decides when missing generator-specific knowledge justifies external search;
- `MetaPoint` (the project key `zhou2026metapoint`): the system converts free-form spatial requests into structured object-level commands.

These examples support different claims. They should not be presented as if all papers use the same explicit specification object or the same planner architecture.

### Public-source search status

Google Scholar and direct arXiv web access were attempted during preparation but were blocked by the current in-app browser security policy. No web search snippet is treated as verified evidence here. The paper identifiers above come from the local original PDFs and Bib entries. Before submission, the title, authors, year, venue, DOI, and arXiv identifier for every retained citation should be checked against Google Scholar, the publisher page, ACL Anthology, or the official arXiv record when access is available.

## 3. What the literature suggests about organization

The literature does not provide a single standard taxonomy named `Goal Understanding, Specification, and Planning`. Instead, related surveys place the concepts in a process:

`goal or task information -> decomposition and representation -> plan construction -> inspection or reflection -> action and possible replanning`.

For this survey, `operational specification` is the useful bridge between the first and third stages. It states what the task requires in a form that can be used to construct and revise a plan. It should be introduced as the survey's analytical term, not as a claim that every cited paper uses that exact name.

The current four labels `semantic decomposition`, `production planning`, `tool planning`, and `reactive planning` should therefore not be presented as a literature-standard four-way classification. They can remain as internal comparison dimensions only if the text explicitly says that they are dimensions used by this survey. A shorter and clearer organization is preferable:

1. goal understanding and unresolved information;
2. operational specification;
3. plan construction through subgoals, dependencies, and order;
4. plan revision when new information changes the remaining task.

## 4. Recommended paragraph sequence

### Paragraph 1: Component scope and output

**Principle first.** This component interprets task information, forms an operational specification, and organizes a plan for the remaining creation trajectory. Its direct outputs are the current task commitments, unresolved assumptions, subgoals, dependencies, planned action order, and any conditions that must be settled before the next step.

**Keep out.** Do not mention persistent storage, execution logs, verifier design, rollback, stopping, or cross-task policy updates in this opening.

### Paragraph 2: Goal understanding

**Principle first.** Goal understanding identifies the intended visual outcome, relevant task information, and unresolved parts of the request. It may use the user instruction, references, interaction context, and domain requirements. The result is a clarified task target and a set of questions or assumptions that affect subsequent specification.

**Paper evidence.** `From Idea to CAD` explicitly uses a requirements role to clarify ambiguities in sketches and text. `SearchGen` provides a case in which the system identifies a missing knowledge source and decides whether external search is needed. `MetaPoint` can be used only for the narrower claim that a free-form spatial request is converted into structured object-level commands.

**Boundary.** Understanding the goal is not the same as executing a tool, storing a long-term state, or verifying the final artifact.

### Paragraph 3: Operational specification

**Principle first.** An operational specification records the commitments that later planning must preserve: the intended goal, references, constraints, priorities, assumptions, and acceptance conditions. It distinguishes supplied information from assumptions or unresolved items and can be updated when the task information changes.

**Paper evidence.** `From Idea to CAD` passes clarified requirements to the CAD construction role. `NEWTON` explicitly identifies a specification bottleneck in physically grounded video generation and argues that conditioning must contain information sufficient for the intended physical behavior. `Divide and Conquer` supplies a task-specific example in which object and relation information is made explicit for subsequent layout generation.

**Boundary.** Do not describe the specification as a memory architecture. Do not discuss provenance versions, persistent records, or representation retrieval here except when needed to state what information the specification contains.

### Paragraph 4: Plan construction

**Principle first.** Planning converts the current specification into an ordered and dependency-aware set of subgoals and intended actions. A plan may state which subgoal is addressed, what must precede it, what information or operation it requires, and where the remaining task should be reconsidered. The plan can be textual, program-like, hierarchical, or tree-structured.

**Paper evidence.** `Divide and Conquer` decomposes compositional requests and plans operations for the resulting object and relation structure. `GenArtist` represents generation and editing operations in a planning tree with alternative operation nodes. `LightVA` recursively decomposes an analytical request into data and visualization tasks. `From Idea to CAD` produces a coarse modeling plan after requirements clarification.

**Boundary.** The paragraph may state that a plan specifies intended operations or executor requirements, but it should not explain interface schemas, tool execution, returned errors, or actual artifact changes. Those details belong to `Tool-Augmented Action and Execution`.

### Paragraph 5: Plan revision

**Principle first.** Planning remains revisable when new user information or task evidence changes a commitment, dependency, or expected next step. The relevant claim is that the remaining plan changes; the subsection need not explain how the evidence was generated or how a failed artifact is repaired.

**Paper evidence.** `NEWTON` is the clearest example because verifier scores are returned to the planner and affect another planning cycle. `GenArtist` can support a narrower statement about selecting an alternative planned operation after a node-level result. `Divide and Conquer` can support feedback-guided refinement when the paper's exact feedback path is stated.

**Boundary.** Do not explain the verifier score, diagnosis, backtracking implementation, subtree deletion, local repair, rollback, or stopping rule here. Those mechanisms are analyzed in the later modules.

## 5. Citation allocation

Each paper should have one primary role in this subsection whenever possible.

| Role in this subsection | Primary papers | Claim to make |
|---|---|---|
| Goal understanding | From Idea to CAD; SearchGen | Clarification or information-gap identification |
| Specification | From Idea to CAD; NEWTON | Explicit requirements transfer or specification bottleneck |
| Decomposition and plan structure | Divide and Conquer; GenArtist; LightVA | Subgoals, dependencies, ordered tasks, or plan trees |
| Plan revision | NEWTON; GenArtist; Divide and Conquer | New information changes the remaining plan |
| Structured spatial command | MetaPoint, only if needed | Free-form spatial intent becomes an object-level command |

Avoid reusing `AutoStudio` here if it remains in `State Representation and Memory`. Avoid repeating `T2I-Copilot` here if its routing and evaluator behavior is discussed in the action or observation section. Avoid using `PhysAgent` here for simulator diagnosis or targeted repair; those are execution and recovery evidence. Avoid repeating `LightVA` or `GenArtist` later unless the later sentence addresses a different mechanism.

## 6. What to change in the current TeX text

### Retain after tightening

- The opening idea that task information is transformed into an operational specification and a plan;
- the distinction between an incomplete request and an explicit specification;
- the definition of operational specification as goal, references, constraints, assumptions, priorities, and acceptance conditions;
- the distinction between specification and planning;
- the use of `From Idea to CAD`, `Divide and Conquer`, `GenArtist`, `LightVA`, and `NEWTON` as evidence.

### Remove or move to other subsections

- `checkpoints` in the opening output list unless it is clearly defined as a planned point for later reconsideration;
- `remain available as task state`, `provenance`, and persistent representation language, which belong to State Representation and Memory;
- `support observation and verification`, except for a brief statement that a plan may designate where a later check is expected;
- detailed GenArtist verification, backtracking, and affected-subtree removal, which belong to Observation and Recovery;
- T2I-Copilot's Quality Evaluator redirect, which belongs to Observation, Feedback, or Tool Routing;
- PhysAgent's simulator output, stage-specific diagnosis, and targeted program edits, which belong to Execution, Observation, or Recovery;
- detailed tool selection and input construction, which belong to Tool-Augmented Action and Execution.

### Replace the current four-form planning paragraph

Replace the claim that the literature has four recurring planning forms with a compact survey-specific formulation:

> We analyze plans through their decomposition of the goal, organization of dependencies and order, assignment of intended operations, and revision of the remaining trajectory when task information changes.

This sentence states the comparison dimensions without claiming that the literature has a settled four-way taxonomy.

## 7. Terminology and writing rules

- Keep the exact heading `Goal Understanding, Specification, and Planning`.
- Use `operational specification` for task commitments and `plan` for intended subgoals, dependencies, order, and revisions.
- Use `this component` for the general mechanism. Do not introduce an unnamed universal `planner`, `manager`, or `controller`.
- Describe a paper's named planner or role only when the original paper defines that role.
- Begin every paragraph with the abstract principle and then give papers as evidence.
- Do not use `rather than`, `not only`, or `does not by itself` as defensive comparisons.
- Do not use tool count, agent count, plan length, or model size as evidence of planning quality or autonomy.
- Do not call a fixed sequence of actions a feedback-adaptive plan unless later information changes the sequence.
- Do not let one citation support an entire paragraph containing unrelated mechanisms.
- Preserve uncertainty: a paper may provide a task-specific structured representation without implementing a general operational specification.

## 8. Final planned outline

The final TeX subsection should follow this compact structure:

1. **Scope and output:** task information becomes a specification and a plan.
2. **Goal understanding:** intended outcome and unresolved information.
3. **Operational specification:** goal, references, constraints, assumptions, priorities, acceptance conditions.
4. **Plan construction:** subgoals, dependencies, order, intended operations, and plan representation.
5. **Plan revision:** changed commitments or remaining actions after new information.
6. **Evidence synthesis:** a short comparison of the retained papers, with no detour into execution, verification, recovery, stopping, or self-improvement.

The core narrative is therefore:

`request -> clarified goal -> operational specification -> planned subgoals and dependencies -> revised remaining plan`.
