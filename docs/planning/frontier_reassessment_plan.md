# Frontier Reassessment Plan

## Scope

This reassessment covers the current `sections/06_frontiers.tex`, the local literature corpus and its taxonomy files, the verified PDF reports, the background surveys, and an external search of recent discussions and surveys on agentic multimodal systems, visual generation, and interactive world models.

The frontier section should identify unresolved research problems supported by repeated evidence. A new module, a longer execution trace, or a higher final-image score is not sufficient evidence of a frontier. The relevant question is whether the system can maintain a visual state, choose an action from evidence, recover from a diagnosed failure, allocate resources, transfer experience, or remain accountable under realistic conditions.

## Evidence Summary

The local taxonomy contains many L2 tool-orchestration and L3 feedback-adaptation systems, fewer long-horizon systems, and a smaller group reporting persistent cross-task updates. This distribution indicates that the immediate research boundary is the transition from feedback loops to dependable long-horizon control. World-modeling generation is a more distant boundary because it requires action-faithful and causally consistent future states.

The local corpus repeatedly exposes the following gaps:

- feedback is often available but its effect on the next action is weakly demonstrated;
- visual judgments often detect a problem without identifying the responsible representation or repair scope;
- memory and context records preserve text or summaries without preserving editable visual state and provenance;
- retries and re-generation are common, while causal diagnosis, rollback, and collateral-change measurement are rare;
- additional calls and samples can improve results without showing adaptive budget allocation or calibrated stopping;
- self-improvement systems retain experiences or skills, but evidence of held-out transfer and no-forgetting remains limited;
- physical and interactive world systems improve action-conditioned prediction, but long-horizon causal fidelity and multi-agent consistency remain open;
- process-level benchmarks and public trajectory records are still less standardized than final-artifact evaluation.

The background surveys support the same direction. The multimodal-agent surveys organize open issues around perception, planning, action, memory, tool use, rationality, and evaluation. The visual-generation roadmap places agentic generation at the planner--render--verify boundary and treats world-modeling generation as a future level characterized by physical rules, intervention, and causal faithfulness. The agent-memory survey identifies multimodal memory, shared memory, automation-oriented memory design, and reinforcement-learning integration as active memory frontiers.

## Audit of Current Sections

### Keep as Core Frontiers

`From Orchestration to Evidence-Based Autonomy` identifies the central AVG gap: a system must change its later action when the current state or evidence changes. This is the right opening problem, although the title should be more direct and the section should use fewer hypothetical examples.

`Calibrated and Heterogeneous Verification` is a genuine frontier. The local papers include learned judges, CAD measurements, simulator checks, inverse parsing, and domain-specific evaluators, but there is no general evidence contract connecting detection, localization, diagnosis, correction, and acceptance.

`Persistent, Editable, and Causally Structured State` is a genuine frontier. Story state, image-generation state, presentation source/render pairs, CAD programs, and editable figures provide partial solutions. The focus should be on representations that preserve identity, dependencies, editability, uncertainty, and provenance across interventions.

`Diagnosis, Credit Assignment, and Reversible Recovery` is a genuine frontier. PhysAgent, CADSmith, IterCAD, PreGenie, PlotGen, and related systems provide partial mechanisms, but a general failure record and reversible recovery contract is not established.

`Budget-Aware Planning, Adaptive Computation, and Stopping` is a valid systems frontier. CoSTA, FaSTA, METAL, AMACE, VISTA, and state-aware generation systems show that cost and stopping matter. General test-time-compute work can provide background, but visual-agent evidence should remain primary.

`Interactive World Models and Physically Grounded Generation` is a valid long-term frontier. NEWTON, PhysAgent, WorldAgents, MultiWorld, MetaWorld, and ShareVerse show concrete progress toward action-conditioned, multi-view, or physically grounded generation. The section should clearly label this as a distant boundary beyond the dominant L2--L4 AVG evidence.

`Cross-Task Learning and Safe Self-Evolution` is a valid frontier. GenEvolve, SIDiffAgent, OctoT2I, COMFYCLAW, EvoIR-Agent, SEAR, DataEvolver, VideoWeaver, and related systems demonstrate experience, routing, or skill updates. The frontier is verified transfer, update attribution, no-forgetting, contamination control, and reversible activation.

`Benchmarks, Data, and Reproducible Trajectory Evidence` is a genuine enabling frontier. It should be framed as the measurement infrastructure required to establish progress, not as another model capability.

### Merge, Downgrade, or Remove

`Human Authority, Provenance, Copyright, and Security` currently combines four different issues. Tool permissions, prompt injection, provenance, copyright, and human workload are important deployment constraints, but they should not be presented as a single core AVG capability frontier. Keep them as a short final subsection titled `Deployment Constraints and Human Authority`, or move the detailed security discussion to evaluation/safety. C2PA is a provenance standard, not evidence that an AVG system is autonomous.

The large frontier table should be removed or reduced. It repeats the paragraph sections, makes broad claims look equally established, and encourages a checklist style. Each frontier subsection should instead state its current evidence, unresolved gap, required mechanism, and decisive experiment in prose.

The current `Grounded generation` wording should be split. World knowledge and structured-data grounding concern factual and structural correctness; interactive world modeling concerns intervention and causal dynamics. They can be discussed in adjacent paragraphs, but they should not be collapsed into one vague category.

The current `A development roadmap` paragraph is too general for the main frontier argument. It can become a short closing synthesis after the evidence-based sections, with no new claims.

## Recommended Chapter Structure

### Opening: What Counts as a Frontier

Define a frontier as a capability gap that recurs across the surveyed systems and can be tested by a change in state, evidence, action, transfer, or resource condition. State that the near-term boundary is dependable L3-to-L4 control and that interactive causal world modeling is a longer-term boundary.

### 1. State-Dependent Control Under Intervention

Define the problem as choosing a different next action when the artifact, observation, tool availability, user requirement, or environment changes. Use GenArtist, CoSTA, PhysAgent, Generation Navigator, VISTA, and Action Agent as evidence of partial solutions. Require matched fixed-workflow baselines, controlled failures, action-conditioned traces, and stopping decisions.

### 2. Heterogeneous Verification and Actionable Diagnosis

Connect verification to the evidence type required by the claim: visual, textual, structural, numerical, geometric, temporal, physical, or behavioral. Separate detection, localization, diagnosis, correction, and acceptance. Use MJ-Bench only after its bibliographic record and claims are independently verified; use CAD-Judge, SciFlow-Bench, SciVisAgentBench, DirectorBench, and domain-specific verifiers already supported by local PDFs.

### 3. Editable State, Intermediate Representations, and Provenance

Unify memory, source representations, visual state, and intermediate plans around one question: can a later operation address the representation that produced the observed result? Cover identity, relations, editable regions, source/render links, uncertainty, checkpoints, and provenance. Use Agent Banana, StoryState, Generation Navigator, PreGenie, DeepPresenter, CADSmith, IterCAD, and SciFig. Correct the current citation error: `avg260608402` is SceneConductor, while SciFig is `huang2026scifig`.

### 4. Causal Failure Attribution and Reversible Recovery

Explain why a critique alone is insufficient. The system must associate a failed claim with an action, dependency, or representation and select a repair with bounded collateral change. Use PhysAgent, CADSmith, IterCAD, GenArtist, PreGenie, PlotGen, and COMFYCLAW. Evaluate root-cause accuracy, rollback success, collateral changes, recurrence, and human intervention.

### 5. Budget-Aware Planning and Calibrated Stopping

Treat rendering, retrieval, verification, simulation, and human review as resources. Use CoSTA, FaSTA, METAL, AMACE, VISTA, and Generation Navigator. Evaluate quality--cost and quality--latency curves, equal-budget comparisons, value of information, stopping regret, and unnecessary-action rates.

### 6. Grounded, Structured, and Physically Interactive Generation

Use two linked but distinct problems. Structured and factual grounding connects external knowledge, data, source code, and constraints to the generated artifact. Physical and interactive grounding requires action-conditioned future states, multi-agent consistency, and counterfactual correctness. Use SearchGen, Qwen-Image-Agent, DataEvolver, NEWTON, PhysAgent, WorldAgents, MultiWorld, MetaWorld, and ShareVerse. Distinguish visual plausibility from action faithfulness and causal consistency.

### 7. Cross-Task Self-Improvement and Skill Transfer

Define the frontier as a persistent change in later-task decisions, not a better result within one trajectory. Use GenEvolve, SIDiffAgent, OctoT2I, COMFYCLAW, EvoIR-Agent, SEAR, DataEvolver, and VideoWeaver. Require held-out tasks, transfer across tools or domains, no-forgetting tests, update attribution, contamination controls, and reversible versioned updates.

### 8. Evaluation Infrastructure and Reproducible Trajectory Evidence

Specify the minimum record: goal and constraints, state checkpoints, actions, tool versions, observations, verifier outputs, costs, human interventions, failed branches, rollback, and stopping. Use domain benchmarks such as CAD-Judge, SciFlow-Bench, SciVisAgentBench, Vision2Web, GameDevBench, and DirectorBench as examples of partial coverage. Keep OTAP, AdaTurn, MJ1, and MIRAGE out of the final evidence set until their records are independently verified against authoritative sources.

### Closing Boundary: Deployment Constraints and Human Authority

Keep security, permissioned tools, indirect prompt injection, provenance, licensing, and human override as a short boundary paragraph. State that these conditions determine whether an otherwise capable controller can be deployed safely; do not present them as another internal AVG mechanism.

## Citation and Evidence Corrections

- Replace `avg260608402` in the current state section with `huang2026scifig`.
- Do not cite `huang2026scifig` for SceneConductor or `avg260608402` for SciFig.
- `kumar2026mj1`, `liang2026adaturn`, `barazandeh2026otap`, and `dai2026mirage` exist as Bib entries but were not found in the local PDF corpus during this audit. Their use should wait for an authoritative record check.
- `snell2024testtime` is a general LLM test-time-compute paper. Use it only as background for resource allocation, not as direct evidence for an AVG mechanism.
- `wu2026visualgeneration` is a roadmap/background source. It supports the distinction between agentic generation and future world-modeling generation, not empirical claims about individual AVG systems.
- All domain-specific claims should continue to use the local PDF reports and verified metadata as the primary source.

## Writing Requirements for the Rewrite

Each subsection should follow the same order: current evidence, unresolved gap, mechanism needed, decisive evaluation. Use direct descriptive titles and avoid checklist tables, generic future-work language, and unsupported claims that the field has already reached L4 or L5. Keep the distinction between a proposed research direction and a demonstrated system explicit.
