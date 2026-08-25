# Tool Definition, Selection, and Execution: Section Planning Document

## 1. Purpose and scope

This document plans the subsection `Tool Definition, Selection, and Execution` in Chapter 3. The subsection should explain how a current plan and task state become executable operations, how the selected operation is represented by an execution interface, and what the executor returns to the later components. It should cover image, video, 3D/CAD, scientific visualization, structured visual documents, and UI/Web creation without turning into a general survey of agent architectures.

The subsection should remain separate from the other five Chapter 3 components:

- `Goal Understanding, Specification, and Planning` defines the task specification and plans.
- `Memory` defines the information retained for later decisions.
- `Perception` obtains and interprets signals, including observation, diagnosis, and verification.
- `Action` performs artifact, information, execution, coordination, feedback, recovery, stopping, and human-facing operations.
- `Cross-Task Self-Improvement` handles updates that transfer to later tasks.

The tool subsection supplies the callable interface, execution result, error, cost, and reversibility information that Perception and Action use. It should not redefine the broader Action taxonomy.

## 2. Evidence status

### Local sources inspected

1. `paper_writing_preferences.md`
2. `agentic_visual_generation_terminology_standard.md`
3. `overleaf_agentic_visual_generation/sections/02_foundations.tex`
4. `overleaf_agentic_visual_generation/sections/03_operating_loop.tex`
5. `Agentic_Visual_Generation综述详细结构与写作指引.md`
6. `2402.15116_Large_Multimodal_Agents_A_Survey.pdf`
7. `2504.18875_Generative_to_Agentic_AI_Survey_Conceptualization_and_Challenges.pdf`
8. `2505.19101_Agentic Visualization_ Extracting Agent-based Design Patterns from Visualization Systems.pdf`

The local surveys provide complementary organizations:

- The large multimodal-agent survey separates action types into tool use, embodied actions, and virtual actions, and separately discusses prompt-based action specification and action-data fine-tuning.
- The generative-to-agentic survey separates tools into tool creation, tool selection, and tool use, then treats interaction with environments, humans, and other agents separately.
- The agentic-visualization survey separates role patterns, communication patterns, and coordination patterns.

The current Bib file contains the relevant visual-generation references, including `qin2024diffusionagent`, `ye2026genclaw`, `gong2026toolcad`, `mallis2024cadassistant`, `zhao2024lightva`, `namgoong2025amace`, `goswami2025plotgen`, `li2025metal`, `gupta2025costa`, `gupta2025fasta`, `yuan2024mora`, and `huang2024genmac`.

### Online-search limitation

An attempted search through Google Scholar and the arXiv metadata endpoint was blocked by the current in-app browser security policy. No online search result, author list, venue, DOI, or mechanism claim is added here as verified evidence. The local PDFs and current Bib entries remain the evidence base. Before final submission, each citation used in the subsection should be checked against an authoritative publication page or the original paper record.

## 3. Literature-derived organization

The local agent surveys support several related but non-identical views of tools. The
`Generative to Agentic AI` survey explicitly separates `Tool Creation`, `Tool Selection`,
and `Tool Use`, and then discusses interaction with virtual worlds, humans, and other
agents as a separate topic. The `Large Multimodal Agents` survey organizes multimodal
agents around perception, planning, action, and memory; within action it distinguishes
tool use, embodied actions, and virtual actions, and separately discusses prompt-based
action specification and action-data fine-tuning. The agentic-visualization survey
organizes multi-component systems through agent roles, communication, and coordination.

These sources support the following five-part organization for this AVG subsection:

1. **Tool definition**: what a tool is, what boundary it exposes, and how a callable operation is represented by inputs, outputs, execution status, errors, side effects, cost, and reversibility when those fields are available.
2. **Tool types**: what kinds of visual-creation operations tools provide, organized by their function and execution substrate rather than by a universal agent taxonomy.
3. **Tool creation**: how an agent or system constructs, wraps, composes, or extends a callable tool, including generated code or a documented interface when the paper actually reports this mechanism.
4. **Tool selection and routing**: how the current task information, state, or execution evidence selects a tool, model, role, or tool path.
5. **Tool use across operating contexts**: how tools are invoked and how their outputs are handed off in single-agent and multi-agent systems, and how the pattern changes across image, video, 3D/CAD, scientific visualization, structured visual documents, and UI/Web creation.

This order begins with the object being analyzed, then describes its functional types and
construction, and ends with selection and use in concrete operating contexts. Execution
outcomes remain part of the tool boundary and the context-specific discussion. Diagnosis,
verification, recovery, stopping, and human authority remain in their own components.

## 4. Proposed subsection structure

### 4.1 Tool definition

**Principle to explain first.** A tool is a callable capability that performs a bounded
operation for the current visual-creation task or task environment. The tool boundary
specifies what the decision process can request and what the executor returns. Its record
can include accepted inputs, produced artifacts or state changes, execution status, errors,
side effects, latency, cost, and reversibility, but the text must attribute only the fields
that a paper exposes.

**Candidate evidence.** Use `GenClaw` for addressable code-driven image operations,
`TOOLCAD` and `CAD-Assistant` for executable CAD actions, and `LightVA` for
planner-to-executor visual-analytics operations.

**Required boundary.** Do not make typed schemas, preconditions, explicit costs, or
reversibility universal requirements. Do not place diagnosis, verification, rollback, or
termination in the definition of a tool.

### 4.2 Tool types

**Principle to explain first.** Tool types describe the operation supplied by a tool and
the substrate in which it runs. For AVG, the working types should cover: visual
generation and editing; visual perception and analysis; retrieval and external
information access; code, application, and rendering execution; and simulation or other
task-environment execution. The list is an analytical grouping for this survey, not a
claim that agent literature uses one universal taxonomy. A tool can belong to more than
one functional group when its interface combines operations.

**Candidate evidence.** Use the multimodal-agent survey's tool, embodied-action, and
virtual-action distinction as background, then use `GenClaw`, `LightVA`, `AMACE`,
`PlotGen`, `METAL`, `TOOLCAD`, and `CAD-Assistant` to ground the AVG-specific groups.

**Required boundary.** Keep verifier and diagnostic interpretation in
`Perception`; describe a perception or
analysis tool here only as an executor that returns an output. Do not infer a tool type
from the number of calls or from the presence of multiple agents.

### 4.3 Tool creation

**Principle to explain first.** Tool creation constructs a new callable capability or
changes an existing interface so that a later decision can invoke it. It may generate
code, wrap an existing model or API, compose several operations, or attach a documented
input-output contract. The paper must show that the resulting object is callable as a
tool; a generated intermediate artifact alone is insufficient.

**Candidate evidence.** The local agent survey provides examples of generated Python
utilities and tool wrappers as background for this mechanism. For AVG, add a visual-
generation paper only when its original paper explicitly constructs a reusable callable
interface; a paper that merely generates an executable artifact, prompt, workflow, or
skill should remain evidence for tool use or memory instead.

**Required boundary.** Separate creating a tool from selecting or invoking it. Do not
describe a skill or memory record as a newly created tool unless the source defines it
as executable and callable.

### 4.4 Tool selection and routing

**Principle to explain first.** Tool selection chooses an available tool, model, role, or
tool path for the current subgoal. Routing may be fixed by the initial request or
conditioned on current task information and execution evidence. It is feedback
adaptation only when an observed result changes the later selection.

**Candidate evidence.** Use `DiffusionAgent` for expert-model routing and
`CoSTA*`/`FaSTA*` for tool-path selection under editing objectives and resource
constraints. Use `GenArtist` here only if it is not reserved for the Observation or
Recovery discussion, and only for the paper's explicit tool-choice mechanism.

**Required boundary.** Do not call a fixed classifier route a feedback-driven change. Do not use
tool count, agent count, or call count as autonomy evidence. Do not move adaptive
stopping, rollback, or cross-task policy updates into this subsection.

### 4.5 Tool use across operating contexts

**Principle to explain first.** Tool use is the invocation of a selected capability and
the handoff of its returned artifact, state, status, or error to the next operation. The
same interface can support different execution arrangements: one decision process can
select and invoke tools directly; specialized roles can divide selection, execution, and
handoff; and a tool can operate on an artifact, a code or application environment, or a
simulator. The comparison should track what is invoked, what is returned, and which
later operation receives it.

**Operating contexts and candidate evidence.**

- **Single-agent visual creation:** `GenClaw`, `DiffusionAgent`, `AMACE`, `PlotGen`,
  and `METAL` for direct tool invocation or code-oriented visual execution.
- **Single-agent code, application, or simulated environments:** `TOOLCAD`,
  `CAD-Assistant`, `CADSmith`, and `IterCAD` for executable programs, sandbox or
  CAD operations, and returned execution states.
- **Multi-agent role specialization:** `Mora`, `GenMAC`, and `Kubrick` for the
  division and handoff of generation, editing, programming, rendering, or related
  execution responsibilities.
- **Domain variation:** image generation and editing, video and animation, 3D/CAD
  and world construction, scientific visualization, structured visual documents, and
  UI/Web creation. The text should compare how the artifact and execution substrate
  change the tool interface and returned outcome, without turning the subsection into
  a domain-by-domain survey.

**Required boundary.** Do not infer stronger autonomy from multi-agent organization.
Do not introduce an unnamed `coordinator`, `manager`, or `controller`; use the exact
role name from the paper or `this component` for the general mechanism. Keep
verification, diagnosis, recovery, stopping, human authority, and cross-task learning
in their designated components.

## 5. Citation allocation and duplication control

Use one primary paragraph for each paper in this subsection whenever possible:

| Subsection role | Primary citations | Avoid repeating here if already used elsewhere |
|---|---|---|
| Tool definition | GenClaw; TOOLCAD; CAD-Assistant; LightVA | PreGenie; PhysAgent; IterCAD |
| Tool types | GenClaw; LightVA; AMACE; PlotGen; METAL; TOOLCAD | Papers reserved for State or Observation |
| Tool creation | Only papers that explicitly create callable tools or wrappers | GenClaw and skill or memory papers without an executable tool |
| Tool selection and routing | DiffusionAgent; CoSTA*; FaSTA* | GenArtist if it is reserved for verification/recovery |
| Tool use across contexts | AMACE; PlotGen; METAL; TOOLCAD; CADSmith; IterCAD; Mora; GenMAC; Kubrick | PreGenie, PhysAgent, Anywhere, AutoStudio when reserved for other modules |

This allocation is a planning preference, not a claim that a paper belongs to only one mechanism. If a paper is cited in more than one subsection, each occurrence must support a distinct claim and should not repeat the same sentence-level fact.

## 6. Terminology and style constraints

- Keep the exact module name `Tool Definition, Selection, and Execution`.
- Use `execution interface`, `action space`, `routing`, `orchestration`, `executor`, and `execution outcome` according to the terminology standard.
- Use `controller` only when referring to the cross-module function already defined in Chapter 2. For general statements, prefer `this component` or `the decision process`.
- Every paragraph should begin with the abstract mechanism, then introduce papers as evidence.
- Avoid defensive contrasts such as `rather than`, `not only`, and `does not by itself`.
- Avoid broad lists of all possible tools or application types. Use `and related executors` for open-ended categories.
- Do not use tool count, agent count, or call count as an autonomy argument.
- Keep diagnosis, verification, artifact actions, recovery, stopping, human authority, and cross-task learning in their own modules.

## 7. Verification checklist before editing

1. Check each cited paper's original PDF for the exact operation, interface, executor, and returned result described.
2. Check the Bib entry in `overleaf_agentic_visual_generation/references.bib` against the original paper record.
3. Confirm that every citation key exists and that no citation is duplicated without a distinct claim.
4. Check that the paragraph's mechanism is stated before its examples.
5. Check that the same paper is not already carrying the identical claim in Perception, Action, or Cross-Task Self-Improvement.
6. Check that any evidence-conditioned action names the observed evidence and the changed later operation.
7. Compile the project after editing and inspect for unresolved citations.

## 8. Working conclusion

The subsection should be organized around the tool-centered path:

`tool definition -> tool types -> tool creation -> tool selection/routing -> tool use across operating contexts`.

The main boundary corrections are to define tools before discussing their selection,
keep tool types separate from agent architecture, distinguish tool creation from tool
invocation, and describe single-agent, multi-agent, and domain-specific use through the
same interface--outcome record. Planning supplies the current subgoal; this component
supplies the callable operation and execution outcome; Perception interprets returned
signals; Action performs the resulting operation and controls continuation; and
Cross-Task Self-Improvement updates reusable behavior for later tasks.
