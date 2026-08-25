# AVG Definition Extraction and Alignment Audit

## Purpose and scope

This note extracts passages that directly define, delimit, formalize, or operationalize Agentic Visual Generation (AVG) from the abstract and Chapters 1--3 of the current synchronized project. It then checks whether the abstract and Introduction use the same definition.

Sources:

- `agentic_visual_generation_survey.tex` (abstract)
- `sections/01_introduction.tex`
- `sections/02_foundations.tex`
- `sections/03_operating_loop.tex`

This is an editorial audit only. It does not modify the manuscript.

## A. Abstract: concise definition and motivation

> Meeting these requirements depends on preserving constraints and usable state across intermediate artifacts, diagnosing deviations, and directing later actions toward the creation goal; it is therefore a problem of creation control.

> Model scaling, prompt refinement, additional conditioning, and repeated sampling can improve individual outputs, while the process remains open-loop whenever observations of the current artifact do not influence subsequent actions.

> Under this condition, deviations, verified constraints, and evolving state do not inform the remaining trajectory, allowing early errors to persist or propagate across later artifacts and actions.

> Addressing this control problem requires a closed-loop organization in which runtime evidence can revise the remaining creation trajectory; agentic visual generation provides such an organization.

> Agentic visual generation (AVG) denotes goal-driven closed-loop visual creation in which a system maintains accessible task-relevant state and uses runtime evidence to select later creation actions.

> Its defining evidence is that runtime observations materially alter later action selection.

> AVG is relevant across diverse visual-creation domains, although their state representations, action spaces, and sources of evidence differ substantially.

> Evidence for dependable control remains fragmented, especially in state persistence, verifier reliability, causal diagnosis, rollback, adaptive budgeting, transfer, and safety.

> Evaluation similarly emphasizes final appearance more often than constraint satisfaction, state consistency, repair, resource use, stopping quality, human workload, and robustness under controlled failures.

## B. Introduction: expanded definition and review boundary

### B.1 Why a closed loop is needed

> Meeting these requirements calls for creation control: constraint persistence, usable intermediate state, diagnosis, repair, and other forms of trajectory management.

> A visual creation process remains open-loop when runtime evidence from the evolving artifact or task environment does not alter subsequent decisions.

> Under this condition, the system cannot use intermediate outcomes to determine whether the current plan remains appropriate, which constraints have been satisfied or violated, where a failure has occurred, or when the task should stop.

> Local errors and changes in task state may therefore persist or propagate across later edits, frames, components, and other dependent outputs.

> Multi-step visual creation requires goal-directed control over the creation trajectory.

> The system must maintain task-relevant state, inspect intermediate artifacts and execution outcomes, and use the resulting evidence to determine subsequent actions.

> These developments illustrate a transition from open-loop sampling toward closed-loop visual creation, in which observations of the evolving artifact and task environment inform later action selection.

### B.2 Introduction definition

> In this survey, *agentic visual generation* refers to goal-driven visual creation that operates through a closed loop.

> Such a system maintains accessible, task-relevant state for an evolving visual artifact, its task environment, and interaction history, then uses runtime observations to select subsequent creation actions.

> These observations may arise from intermediate artifacts, execution outcomes, external information, user feedback, and other task-relevant sources.

> The defining behavioral criterion is a demonstrable observation--action dependency: runtime information changes later action selection.

### B.3 Review motivation and contribution statements tied to the definition

> Across the related surveys identified in our search, we did not find one devoted to agentic visual generation as a class of systems in which runtime observations demonstrably influence subsequent visual-creation decisions.

> This survey uses that behavioral property to organize the literature, then compares how the resulting control mechanisms and supporting evidence vary across visual-creation domains.

> It develops a unified account of agentic visual generation as closed-loop visual creation and specifies a behavioral boundary based on state-dependent creation decisions.

> It synthesizes a six-module operating architecture that connects goal specification and planning, state and memory, tool-augmented execution, observation and decision evidence, recovery and human authority, and cross-task self-improvement.

## C. Foundations: operational definition, boundary, and formalization

### C.1 Visual-creation context that supports the definition

> The transition from single-pass rendering to closed-loop visual creation depends on how a creation task represents its goal, artifact, and constraints.

> A visual artifact may therefore contain rendered appearance together with temporal relations, geometry, parameters, source data, hierarchy, or interaction state. These representations give the product properties that can persist across operations instead of being recreated from a final rendering at every step.

> Conditions specify the information and requirements for an operation, whereas execution interfaces specify how that operation can be carried out. Together, these properties define the action space and the execution evidence available at each point in a visual creation process.

### C.2 Operational boundary and formal definition

> The operational boundary of agentic visual generation is defined through decision behavior.

> A system exhibits agency when observations of a developing artifact, its environment, or the interaction history condition subsequent creation actions.

> Relevant actions include clarification, planning, retrieval, model or tool selection, generation, editing, verification, revision, recovery, human escalation, and termination.

> *Agentic Visual Generation is goal-conditioned sequential control of a visual creation trajectory in which an identifiable decision-making entity uses observations of the evolving artifact, environment, and interaction history to select subsequent creation actions and determine when to revise, recover, escalate, or stop.*

### C.3 Minimum conditions

> The definition imposes three minimum conditions. First, a visual artifact or editable visual environment is a substantive task objective. Second, an identifiable controller can select among alternative creation actions. Third, information produced during the task has a demonstrable effect on a later decision.

> The controller may be a single model, a learned policy, a search procedure, a hierarchy of specialized agents, or a human-supervised program. The behavioral requirement remains the same across these implementations.

### C.4 Boundary against adjacent systems

> Tasks outside this scope do not govern the construction or editing of a visual artifact.

> Fixed cascades remain visual workflows when their stages and control decisions are predetermined.

> Some workflows add agent components for routing or critique while retaining a mostly prescribed path.

> Closed-loop visual agents use intermediate evidence to change actions, revise state, recover from failure, or terminate.

> Systems that retain validated experience across tasks add a further learning dimension to this trajectory-level control.

> This boundary is an engineering criterion that can be evaluated from trajectories. Its evidence includes the state available at a decision point, the alternatives considered, the observation that triggered a change, the resulting action, and the stopping or escalation decision.

### C.5 L1--L5 autonomy continuum

> Agentic visual systems exhibit different spans of state-dependent control. We use five cumulative levels to record the strongest behavior supported by available evidence.

| Level | Name | Operational criterion |
| --- | --- | --- |
| L1 | Fixed mapping or pipeline | The output and control path are predetermined. |
| L2 | Tool or role assistance | The system selects tools, models, or roles without a demonstrated artifact-dependent feedback loop. |
| L3 | Feedback adaptation | Intermediate evidence causes one or more subsequent revisions. |
| L4 | Long-horizon autonomy | Persistent state supports dynamic replanning, failure recovery, authority management, and adaptive stopping. |
| L5 | Continual self-improvement | Experience changes reusable memory, skills, verifiers, policy, or model behavior across tasks. |

> L3 requires an observable dependency between intermediate evidence and a later revision. L4 extends this dependency across multiple operations through persistent state, replanning, recovery, escalation, and stopping. L5 additionally requires transfer: experience from earlier tasks changes later behavior under held-out evaluation.

### C.6 Formalization of closed-loop visual creation

> We model visual creation as a partially observable, goal-conditioned control process. Let $g$ denote the task goal and constraints, $s_t$ the relevant environment state, $x_t$ the current visual artifact or editable representation, $m_t$ the controller's memory, and $\mathcal{H}_t$ the action--observation history.

> An observation is a task-dependent projection of the current state and artifact. The controller uses that observation, its memory, and the interaction history to select an action:

$$
o_t = O(g,s_t,x_t,m_t,\mathcal{H}_t),
\qquad
a_t = \pi_{\theta}(g,o_t,m_t,\mathcal{H}_t,\toolset).
$$

> The selected action and executor update the environment, artifact, and memory:

$$
(s_{t+1},x_{t+1},m_{t+1})
= U(g,s_t,x_t,m_t,a_t;\tau_t).
$$

> One or more task-specific verifiers assess the updated state. A control policy then determines whether execution continues, returns to planning, restores a prior state, requests human authority, or stops.

$$
z_{t+1}\in\{\text{continue},\text{replan},\text{rollback},\text{ask},\text{stop}\}.
$$

> Differences among systems can therefore be located in the state they preserve, the observations they obtain, the actions they can execute, the evidence they use, and the control decisions they support.

## D. Operating loop: implementation requirements of the definition

### D.1 Causal reading of AVG

> The preceding section defined agentic visual generation as state-dependent control over a visual creation trajectory.

> The organizing question is causal: what representation is available at a decision point, what action is selected from it, what evidence is obtained after execution, and how does that evidence alter the remainder of the trajectory?

> A plan constrains later actions, an observation exposes task-relevant state, a critique changes a subsequent decision, and retained experience improves future decisions under an appropriate evaluation split.

### D.2 Six-module operating architecture

> The mechanisms form a coupled control system organized into six modules. Goal specification and planning define the task commitments; state and memory preserve the variables needed across decisions; tool-augmented execution changes the artifact or environment; observation, diagnosis, verification, and feedback convert those changes into decision evidence; recovery, stopping, and human authority govern the continuation of the trajectory; and cross-task self-improvement updates reusable behavior.

> The modules are connected by explicit state, action, and evidence interfaces.

### D.3 Relation between the six modules and L1--L5

> The transition from L1 to L5 concerns the decisions that can change after the system observes a creation state.

> L1 and L2 retain a fixed or weakly adaptive control path, even when execution is distributed across several operations. L3 is reached when intermediate evidence changes a later revision. L4 adds persistent state, dynamic replanning, recovery, authority management, and adaptive stopping. L5 requires experience to change reusable behavior across tasks, with transfer evidence beyond longer context or task-local reflection.

> Repeated sampling remains at L1 or L2 when no state-dependent change in the action rule is shown.

### D.4 Three temporal scales of iteration

> *Candidate iteration* samples alternatives while leaving the control rule unchanged.

> *Feedback iteration* changes an input, tool, state, or plan after an observation.

> *Policy iteration* changes reusable behavior across tasks.

> Candidate iteration does not provide evidence of state-dependent control; feedback iteration provides the observation--action dependency required for a closed loop; policy iteration supports a self-improvement claim when transfer, independent evaluation, and update provenance are shown.

### D.5 State, action, observation, and feedback

> The state-and-memory module maintains the task variables that remain relevant after a single action. It links symbolic constraints, visual references, executable representations, intermediate artifacts, and provenance so that later decisions can identify dependencies, preserve invariants, and restore trusted states.

> The action space of AVG includes operations that directly change an artifact and operations that change how creation proceeds. Artifact actions generate, edit, composite, render, simulate, or execute. Control actions select a model, retrieve evidence, allocate a budget, inspect a state, update a plan, checkpoint an artifact, roll back, ask a person, or terminate.

> The evidence module converts the evolving artifact and execution state into decision evidence. Observation acquires task-relevant signals, diagnosis connects those signals to failure hypotheses, verification tests explicit requirements, and feedback carries the resulting verdict to the next action.

> Feedback closes the loop when it changes a later decision. A pipeline that produces an image and a textual critique without returning to a generator or editor provides observation and evaluation only. Adaptation is established when the critique changes the prompt, tool, plan, region, code, or stopping decision.

### D.6 Human authority and cross-task improvement

> Human participation can clarify a goal, approve a plan, provide a reference, resolve verifier disagreement, authorize a consequential action, or accept the final artifact. These interventions differ in information and authority.

> This module uses completed trajectories to update reusable behavior. It separates task-local correction from episodic reuse and policy-level updates, and it governs the provenance, evaluation, and reversibility of cross-task learning.

> Self-correction changes the current trajectory. Episodic reuse retrieves a previous attempt or repair for a later task. Self-improvement changes the policy, skill library, retrieval behavior, verifier, or memory used on future trajectories.

> Evidence for reliable cross-task self-improvement requires gains under independent evaluators or tools, held-out transfer, and reversible updates.

## E. Abstract--Introduction definition audit

### E.1 Conceptual consistency

The abstract and Introduction use the same five-part conceptual core:

| Definition element | Abstract | Introduction | Assessment |
| --- | --- | --- | --- |
| Goal orientation | `goal-driven` | `goal-driven` | Exact match. |
| Closed-loop organization | `closed-loop visual creation` | `visual creation that operates through a closed loop` | Same meaning; the abstract uses the preferred stable phrase more directly. |
| Accessible state | `accessible task-relevant state` | `accessible, task-relevant state for an evolving visual artifact, its task environment, and interaction history` | Consistent. The Introduction supplies the state objects omitted for brevity in the abstract. |
| Information driving control | `runtime evidence` | `runtime observations`, followed by sources of those observations | Consistent at the conceptual level. The Introduction makes the evidence sources concrete. |
| Behavioral criterion | `runtime observations materially alter later action selection` | `runtime information changes later action selection` | Same causal criterion. The abstract is slightly stronger because it includes `materially`; the Introduction is slightly broader because it says `information`. |

Conclusion: the abstract and Introduction are definitionally consistent. The Introduction is a valid expansion of the abstract rather than a second conceptual framework. It adds the artifact, environment, interaction history, and observation sources; none contradicts the abstract.

### E.2 Wording consistency

The wording is close but not fully normalized. The following variants occur:

| Concept | Abstract wording | Introduction wording | Editorial observation |
| --- | --- | --- | --- |
| Closed loop | `goal-driven closed-loop visual creation` | `goal-driven visual creation that operates through a closed loop` | Prefer the compact phrase `goal-driven closed-loop visual creation` in both places. |
| Runtime input | `runtime evidence`; `runtime observations` | `runtime evidence`; `runtime observations`; `runtime information` | These are related but not interchangeable in every sentence. Use `runtime observations` for the behavioral criterion, and use `runtime evidence` for the broader decision-relevant material derived from observations, execution outcomes, external information, or user feedback. Avoid `runtime information` in the defining sentence unless it is intentionally defined. |
| Later action | `later creation actions`; `later action selection` | `subsequent creation actions`; `later action selection` | No substantive difference. Choose `subsequent creation actions` for the system description and retain `later action selection` in the compact criterion if desired. |
| State scope | implicit in `task-relevant state` | artifact, environment, and interaction history | The Introduction appropriately expands the abstract. The same scope is also present in the Chapter 2 formal definition. |

### E.3 Relation to the Chapter 2 formal definition

The Chapter 2 definition preserves the abstract--Introduction core but adds two formal requirements:

1. An `identifiable decision-making entity` selects among alternatives.
2. The controller determines when to revise, recover, escalate, or stop.

It also uses `goal-conditioned sequential control` where the abstract and Introduction use `goal-driven` and `closed-loop visual creation`. The expressions are compatible, but they are not stylistically identical. `Goal-driven closed-loop visual creation` should remain the short, reader-facing formulation; `goal-conditioned sequential control of a visual creation trajectory` can remain the formalization-oriented formulation in Chapter 2.

### E.4 Recommended harmonized core wording

This is a proposed normalization, not a manuscript edit:

> Agentic visual generation (AVG) denotes goal-driven closed-loop visual creation in which an identifiable controller maintains accessible, task-relevant state for an evolving visual artifact, its task environment, and interaction history, and uses runtime evidence to select subsequent creation actions. Its defining behavioral criterion is a demonstrable observation--action dependency: runtime observations materially alter later action selection.

This sentence preserves the abstract's concise core, the Introduction's explicit state scope, and the Foundation's identifiable controller and behavioral criterion.

## F. Audit conclusion

The current manuscript has one stable conceptual definition:

1. AVG is goal-driven and closed-loop.
2. Its objective is visual creation or an editable visual environment.
3. A controller maintains accessible task-relevant state.
4. Runtime observations or other evidence affect subsequent creation decisions.
5. The observable proof is an observation--action dependency, not merely multiple stages, tools, models, or samples.
6. Persistent state, recovery, stopping, human authority, and cross-task learning distinguish higher spans of autonomy rather than define a separate concept.

No contradiction was found between the abstract and Introduction. The only editorial issue is minor terminology drift around `runtime evidence`, `runtime observations`, and `runtime information`, together with a less compact closed-loop phrase in the Introduction.
