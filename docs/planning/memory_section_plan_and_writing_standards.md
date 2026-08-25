# Memory Section Plan and Shared Writing Standards

This document governs the rewrite of `\subsubsection{Memory}` in
`overleaf_agentic_visual_generation/sections/03_operating_loop.tex`. It is a
planning and review document; creating it does not modify the chapter正文.

## Goal

Rewrite the `Memory` subsection as a clear, evidence-grounded account of how
agentic visual-generation systems retain, organize, and reuse task-relevant
information. The subsection must explain the mechanism at an abstract level,
then use concrete visual-generation papers as evidence. It must remain
consistent with Chapter 2, the six-component framework, the neighboring
`Goal Understanding, Specification, and Planning` subsection, and the
following `Tool-Augmented Action and Execution` subsection.

## Scope and boundaries

The subsection uses `Memory` as its only general module name. It discusses
information retained for later decisions, including task-local records and
records reused after an interaction or task. It may distinguish memory from
the current context, interaction history, an artifact's editable
representation, and provenance when that distinction is needed to explain
what is retained and how it is used.

The subsection does not redefine:

- goal interpretation, specification construction, or plan construction;
- tool schemas, tool routing, API execution, or executor architecture;
- observation, diagnosis, verification, or feedback generation;
- repair, rollback, stopping, escalation, or human authority;
- cross-task self-improvement as a separate component.

Those mechanisms may be mentioned only when a memory record is read or
written at their interface. The text must not turn Memory into a second
description of the full operating loop.

## Required four-part structure

The final subsection should use four direct, descriptive parts. Paragraph
labels may be used if they improve navigation, but they must not introduce
new modules or an artificial taxonomy.

### 1. What Memory is

Begin with the principle. Define Memory as retained, task-relevant
information that can be read by a later decision in the current trajectory or
in a later interaction/task. Explain the read/write relation at an abstract
level:

1. an interaction produces information;
2. the system selects information with expected later utility;
3. the selected record is stored in a representation that can be addressed;
4. a later decision retrieves a relevant record and uses it with the current
   task information.

Clarify the boundary between a transient context window and Memory. A full
interaction history is not automatically a useful memory record; a memory
record is selected, represented, or retained for later use. Keep this
explanation concise and factual. Do not introduce `state and memory` as a
combined component, and do not create labels such as `distributed state` or
`factorized state`.

After the principle, give at least three visual-generation examples. Each
paper must be used for a claim that its original paper actually supports.
Possible evidence candidates from the current Bib are `avg260626907`
(Qwen-Image-Agent), `wang2024lave` (LAVE), `avg260708497` (Cognitive-structured
Multimodal Agent), and `avg260721594` (World State Registers). The final
selection must be checked against the local paper or an authoritative record;
do not use a candidate merely because its title contains a memory-related
word.

### 2. Memory types and their characteristics

Explain the dimensions separately. They are different ways to describe a
record and are not mutually exclusive architectural modules.

#### Temporal scope

- **Short-term memory:** information retained during the current turn or
  trajectory, such as active requirements, recent intermediate results,
  unresolved decisions, and recent feedback.
- **Long-term memory:** information retained across turns or tasks, such as
  user preferences, reusable references, prior attempts, successful or
  failed procedures, and learned skills.

State explicitly that the distinction concerns retention and access over
time. It does not require two physically separate stores.

#### Functional role

- **Working memory:** the active workspace used to choose the next operation
  in the current task.
- **Factual memory:** relatively stable facts about the user, task domain,
  environment, references, or visual entities.
- **Episodic memory:** records of particular attempts, outcomes, failures,
  repairs, or interaction trajectories.
- **Procedural/skill memory:** reusable action patterns, tool procedures, or
  skills distilled from prior work.

Use these labels only when the cited source or the survey definition supports
the corresponding function. Do not imply that every visual-generation system
implements all four roles.

#### Representation form

Describe the information carrier rather than inventing a component name:

- textual or token-level summaries;
- visual or multimodal records;
- structured records, tables, key-value entries, or graphs;
- executable or artifact-linked records, such as code, workflows, or source
  representations linked to rendered outputs;
- parametric or latent memory when the original paper explicitly uses those
  terms.

Do not equate an editable artifact representation with Memory automatically.
It becomes memory evidence when the system retains and later retrieves it for
decision-making. Keep `context`, `interaction history`, `artifact
representation`, and `provenance` distinct from Memory unless the paper
explicitly treats them as memory.

#### Access and information channel

Where evidence permits, mention private versus shared memory for
multi-component systems and textual, visual, structured, executable, or
multimodal channels. These are access or representation dimensions, not
additional top-level sections. Use `multimodal memory` when the retained
record combines visual information with text, code, geometry, or other
modalities and the paper demonstrates that behavior.

This part must contain at least three papers not used in Part 1 or any other
part of this subsection. Prefer papers that naturally cover different
dimensions, for example `sarkar2026storystate` (StoryState),
`cheng2024autostudio` (AutoStudio), `huang2026vimax` (ViMax), and
`xie2024anywhere` (Anywhere), subject to global citation checks and direct
paper verification.

### 3. What Memory does in agentic visual generation

Explain the functions before listing papers. Memory can support:

1. continuity of requirements, identities, references, and constraints across
   operations or turns;
2. access to intermediate artifacts, source representations, and execution
   records needed for later editing or inspection;
3. cross-step dependency tracking so a later decision can locate the record
   related to an observed result;
4. reuse of prior attempts, repairs, tool traces, or skills when a related
   request appears;
5. coordination when several roles or agents need a shared task record.

State the functional test directly: a record matters as Memory when its
availability changes what a later operation can select, construct, edit,
verify, or stop. Do not claim improved quality or autonomy unless the paper
reports evidence for that claim. Do not confuse episodic reuse with
cross-task self-improvement. The latter requires evidence that retrieved
experience changes later behavior on a new task; storing or retrieving a
record alone is not sufficient.

Use at least three new papers in this part. Candidate evidence includes
`ye2026agentbanana` (Agent Banana) for structured interaction-history reuse,
`hu2026itercad` (IterCAD) for program and multimodal-feedback continuity,
`xie2024dreamfactory` (DreamFactory) for carrying visual attributes across a
long-form generation process, and `avg260517969` (Generation Navigator) for
state-aware generation if its paper supports the intended claim. Verify each
mechanism before retaining it and ensure none was cited in Parts 1--2 or the
neighboring subsections.

### 4. How Memory is formed, updated, compressed, deleted, and retrieved

Explain the lifecycle in this order:

1. **Formation:** information comes from task requests, references, actions,
   artifact outputs, observations, feedback, and user corrections. The
   system selects candidates according to relevance, expected future utility,
   reliability, scope, and provenance. It need not store every interaction
   token or every rendered image.
2. **Update and evolution:** new information can append a record, revise an
   existing record, resolve a conflict, consolidate related records, or
   change the scope/version of a record. Explain that updates should preserve
   provenance and dependencies where later editing or attribution requires
   them.
3. **Compression:** summaries, abstractions, deduplication, hierarchical
   records, or learned representations reduce storage and retrieval cost while
   retaining the information needed for a later decision. State the risk of
   losing detail, localization, or evidence when compression is too strong.
4. **Deletion and expiry:** records can be removed when they are obsolete,
   low-utility, contradictory, unsafe to retain, outside their scope, or too
   costly to maintain. Deletion should be described as a memory-management
   operation, not as recovery or stopping.
5. **Retrieval:** a current task/specification and current observation form a
   query; the system selects relevant records and formats them for the next
   decision. Retrieval may be triggered at initialization, intermittently, or
   whenever the current task requires it. Relevance, recency, reliability,
   modality, scope, and dependency can affect selection when the paper
   reports them.

This part must use at least three papers not cited elsewhere in the Memory
subsection. Candidate evidence includes `ye2026agentbanana` for history
compression, `avg260626907` for multimodal/context retrieval,
`avg260708497` for cognitive-structured records, `avg260701709` (COMFYCLAW)
for skill/experience accumulation, `jiang2026octot2i` for experience-guided
routing, `chen2026genevolve` for visual-experience distillation, and
`avg260631537` (DataEvolver) for data/experience evolution. The final text
must use only papers whose original descriptions directly support the stated
formation, update, compression, deletion, or retrieval mechanism.

## Citation allocation and global de-duplication

The final subsection must cite at least three papers in each of the four
parts. More than three are allowed when they support distinct mechanisms.
Every citation must be unique across:

- all four Memory parts;
- the preceding `Goal Understanding, Specification, and Planning` subsection;
- the following `Tool-Augmented Action and Execution` subsection.

Before editing the TeX, build a citation ledger with one row per retained
paper: Bib key, paper title, local PDF/report path, primary claim, exact
location in the paper (section/page/figure when available), Memory part, and
whether the key is used elsewhere in Chapter 3. If a paper is useful in two
places, assign it to the section where its evidence is most specific and
replace it in the other section. Do not solve duplication by repeating the
same citation in multiple roles.

The following is a provisional non-overlapping allocation inside the Memory
subsection. It is a starting point for source checking, not permission to
reuse a key that is already assigned to a neighboring subsection:

| Memory part | Initial candidates (at least three) |
| --- | --- |
| What Memory is | `avg260626907`, `wang2024lave`, `avg260708497` |
| Memory types | `sarkar2026storystate`, `huang2026vimax`, `zhou2024storymaker` |
| What Memory does | `ye2026agentbanana`, `hu2026itercad`, `avg260517969` |
| Memory lifecycle | `chen2026genevolve`, `avg260701709`, `jiang2026octot2i`, `avg260631537` |

The candidates are deliberately drawn from the current project Bib file, but
their mechanisms still require source verification. If the global ledger
shows that a candidate is used in a neighboring subsection, replace it with a
verified unused paper; do not cite it twice. If a candidate does not support
the intended sentence after source inspection, remove it and leave the claim
out until a verified replacement is found.

Use existing project references first. Add a Bib entry only when a suitable
paper is absent and its authoritative metadata is available. A candidate
without a verified title, author list, year, venue or arXiv identifier must
remain unused; never infer missing metadata from a title, filename, or search
snippet.

## Evidence and BibTeX verification protocol

For every citation retained in the final text:

1. Read the local original PDF, report, or official project record.
2. Record the exact mechanism, input, output, and evaluation evidence used in
   the sentence.
3. Check that the sentence does not attribute a neighboring module's
   function, an unreported causal effect, or a stronger autonomy claim.
4. Compare the Bib entry with the paper's title page and an authoritative
   source such as the official arXiv record, publisher page, ACL Anthology,
   proceedings page, or DOI record.
5. Check key uniqueness, citation syntax, author spelling, year, venue,
   volume/issue/pages when applicable, DOI, and URL.
6. If any field or mechanism remains uncertain, omit the citation or state
   only the verified information. Do not fill gaps by inference.

## Shared writing standards

These rules apply to this section and to all later Chapter 3 revisions.

### Evidence, scope, and tone

- Use formal, objective, restrained academic language.
- Match claim strength to evidence. Use `reports`, `evaluates`, `describes`,
  or `uses` for single-paper facts; reserve causal language for explicit
  ablations, interventions, or process evidence.
- Do not use promotional adjectives or unsupported claims such as `novel`,
  `powerful`, `seamless`, `robust`, `comprehensive`, or `effective` as
  arguments.
- Do not convert a small local literature sample into a claim about the whole
  field.
- Keep facts, the survey's analytical interpretation, comparisons, and future
  suggestions distinguishable.

### Principle-first paragraph structure

- Each paragraph begins by stating what the mechanism is, what information it
  receives, how it operates, and what it produces or enables.
- Only after the abstract principle is clear should the paragraph introduce
  papers as evidence.
- Keep one main claim per paragraph. Split paragraphs containing unrelated
  mechanisms.
- Add length through inputs, outputs, update conditions, interfaces, and
  evidence boundaries, not through repeated summaries or long task-specific
  lists.
- Use direct transitions that state a logical dependency. Delete mechanical
  previews of the next subsection and empty phrases such as `This highlights
  the importance` or `It is worth noting`.

### Abstraction and examples

- Cover image, video, 3D/CAD, scientific visualization, structured visual
  documents, and UI/Web creation at the mechanism level.
- Do not replace an abstract definition with a long enumeration of camera
  parameters, shot lists, geometry fields, slide layouts, or tool names.
- Keep concrete implementation names inside paper-specific evidence clauses.
- Open non-exhaustive lists with `and related ...`, `among others`, or the
  corresponding Chinese `等` where needed.
- Do not invent a taxonomy or module name that is absent from the framework or
  the cited paper.

### Terminology and cross-section consistency

- Use the exact six-component names established in the terminology standard.
- In general mechanism prose, use `this component` or `Memory`; do not invent
  an unnamed universal `memory manager`, `state manager`, `planner`, or
  `verifier`.
- Use `controller`, `agent`, `executor`, `planner`, or `verifier` only when
  Chapter 2 defines that role or the cited paper explicitly provides it.
- Keep `Memory`, `context`, `interaction history`, `artifact representation`,
  and `provenance` distinct. Do not combine `state and memory` in this
  subsection after the framework has adopted `Memory`.
- Verify every cross-reference against Chapters 1--3 word by word. Remove a
  cross-module sentence when it adds no necessary information.

### Defensive writing and unnecessary contrast

- Avoid defensive formulations such as `rather than`, `not only`, `does not
  by itself`, `not merely`, and repeated `not X but Y` constructions.
- State the positive mechanism, inclusion condition, or evidence requirement
  directly.
- Do not anticipate a reader's objection and answer it with a chain of
  exclusions. A boundary belongs in the shortest factual sentence that is
  needed for the analysis.
- Do not use comparison rhetoric to imply that a system is more autonomous
  because it has more agents, tools, steps, parameters, or compute.

### Bilingual and citation consistency

- English and Chinese text must make the same claim, preserve the same
  uncertainty, and use the same terminology and citation keys.
- A citation must be adjacent to the concrete fact it supports. Split a long
  sentence when one citation would otherwise appear to support unrelated
  claims.
- Do not cite a survey or paper as generic authority for a paragraph whose
  mechanisms it does not report.

## Planned editing and review sequence

1. Freeze the current neighboring-section citation ledger.
2. Read the current Memory text and mark sentences to retain, move, delete, or
   replace under the four-part structure.
3. Build and verify the candidate Memory citation ledger; remove every key
   already used in the two neighboring subsections.
4. Draft each part from principle to evidence, using at least three unique,
   verified papers per part.
5. Check every paper sentence against the original source and every Bib field
   against an authoritative metadata record.
6. Perform a word-level terminology check against Chapters 1--3 and remove
   newly invented module names or duplicated explanations.
7. Check for defensive writing, unsupported causal claims, closed lists,
   empty transitions, and English/Chinese mismatches.
8. Compile the LaTeX project and inspect undefined citations, duplicate keys,
   bibliography warnings, and the rendered Memory subsection.
9. Only after all checks pass, update `03_operating_loop.tex` and report the
   exact citations and verification status.

## Completion criteria

The rewrite is ready only when all of the following hold:

- The subsection is organized under the four required parts.
- Every part contains at least three unique citations.
- No citation is repeated within Memory or in the adjacent Chapter 3 sections.
- Every cited mechanism is supported by the original paper.
- Every retained Bib entry is present, syntactically valid, and metadata-checked.
- Each paragraph begins with an abstract mechanism explanation and then gives
  evidence.
- The text uses the established terminology, avoids defensive writing, and
  contains no unnecessary repetition or unsupported generalization.
- The project compiles without undefined citations or BibTeX errors.
