# Agentic Visual Generation Frontier：高层重构建议

## 权威综述如何组织 Frontier

代表性的 Agent 与多模态综述通常不把 planning、memory、tool use、verification、rollback 等组件分别写成一级研究前沿。它们先提出系统级的发展轴，再在每个发展轴中讨论相关机制。

- *Large Multimodal Agents: A Survey* 将未来方向概括为 framework、evaluation 和 application。Framework 进一步区分单智能体的统一化与多智能体的协作问题。
- *Agent AI: Surveying the Horizons of Multimodal Interaction* 以 integration、paradigm、learning、cross-modality/domain/reality、continuous self-improvement、dataset and leaderboard 等系统能力组织全文。
- *Generative to Agentic AI* 将具体模块放在能力分析中，而在 Challenges 中讨论 cumulative errors、interpretability、dynamic environments、observability、safety、evaluation、human alignment 和 control。
- *LLMs Meet Multimodal Generation and Editing* 的未来部分使用 technical prospects、applications 和 world models 等宽维度，而不是重复前文组件分类。
- *Visual Generation in the New Era* 把 frontier 表述为 visual reasoning、closed-loop agents、tool-augmented rendering、visual self-play、world simulation、data-centric intelligence 和 evaluation。其中最核心的能力终点是从可控生成进入可交互、具备因果约束的世界模拟。
- *Memory in the Age of AI Agents* 以能力转变组织前沿，例如从 retrieval 到 memory generation、从人工管理到自动管理、从单模态到多模态和共享记忆，以及 memory 与 RL、world models 和 trustworthiness 的结合。

这些组织方式包含三个共同原则：一级方向描述能力跃迁；组件机制作为实现条件；评测与安全作为证明和部署条件。

## 扩展阅读后的判断

进一步对照本地的多模态 Agent、Agentic AI、视觉生成、视频一致性、Agent memory 和视觉生成路线图后，四方向方案仍有一个不足：`Generalist Visual Creation Agents` 的范围过宽，容易把视觉推理、规划、工具使用和跨域迁移重新混成一个大类；同时，权威视觉路线图反复单独强调的 visual chain-of-thought、结构化中间状态和可验证推理没有被明确保留。

更稳妥的抽象方式是使用五个能力轴。它们不是第三章六模块的平行版本，而是描述系统能力将达到的更高层级：

1. 视觉推理与结构化控制；
2. 持久且可交互的视觉世界；
3. 持续学习与自我演化创作；
4. 人本且可部署的开放世界协作；
5. 评测与科学基础设施。

在这个结构中，通用视觉创作智能体不再单独作为一个含义过宽的 Frontier，而作为前四个能力轴共同指向的系统形态。

## 建议的五个高层方向

### 1. Visual Reasoning and Structured Control

这一方向讨论系统如何在渲染之前和渲染过程中形成能够约束后续视觉结果的中间状态。状态可以表达空间关系、对象身份、时序关系、结构约束、数据关系或可执行操作。权威视觉路线图将 visual chain-of-thought、structured reasoning 和 tool-augmented rendering 视为从被动渲染走向 agentic generation 的关键过渡。

现有工作已经使用布局、编辑程序、节点图、CAD 程序、数据图表和视觉轨迹等中间表示。尚未解决的问题是中间状态是否忠实约束最终结果，是否能够被检查和修改，以及系统能否在不同视觉领域中复用同一种结构化控制原则。文本形式的推理长度、模型规模或工具数量本身不构成这一 Frontier 的进展证据。

### 2. Persistent and Interactive Visual Worlds

这一方向讨论视觉生成对象从一次性输出发展为能够持续存在、接受局部修改并响应行动的视觉世界。它包含两层能力：持久且可编辑的视觉状态，以及在干预下保持一致的动态演化。前者覆盖身份、关系、结构、版本和来源；后者覆盖动作条件、物理约束、多视角一致性和因果结果。

图像编辑状态、长视频记忆、可执行 CAD、结构化文档和节点图是这一方向的早期形式。WorldAgents、MultiWorld、MetaWorld、ShareVerse、NEWTON 和 PhysAgent 等工作进一步把生成扩展到多视角、物理或动作条件。长期目标是连接创作智能体与世界模型，使生成结果成为可操作和可验证的持续环境。

### 3. Continual Learning and Self-Evolving Creation

这一方向讨论智能体如何把创作经历转化为后续任务中的能力变化。其范围包括经验抽象、策略更新、技能形成、工具创建、路由学习、个性化以及多智能体共享经验。任务内反思和反复采样属于闭环执行；只有跨任务保留并改变后续决策的更新才属于这一方向。

GenEvolve、SIDiffAgent、OctoT2I、COMFYCLAW、VideoWeaver、EvoIR-Agent、SEAR 和 DataEvolver 已展示经验、技能或策略更新的不同形式。未来研究需要回答经验如何选择、错误如何避免被固化、技能如何组合与迁移，以及系统如何在长期更新中控制遗忘、污染和能力退化。

### 4. Human--Agent Co-Creation in Open Environments

这一方向讨论 AVG 如何在开放、长期和高后果的真实创作环境中与人协作。视觉创作具有主观目标、版权与来源要求、不可逆发布动作、隐私数据和领域责任。系统需要根据任务风险分配人类权限，并让用户能够理解、修改、拒绝或撤销关键决策。通用 Agent 综述把 human interaction、open-world interaction、observability、safety 和 alignment 作为 Agentic AI 的系统级挑战，这些问题在视觉创作中会通过图像、声音、页面和外部工具进一步放大。

来源记录、权限、资源效率和安全是这一方向的部署条件，而不是独立的生成机制。该方向关注可持续的人机创作关系，以及系统在不完全可观测、含有不可信输入和外部副作用的环境中保持可控的能力。

### 5. Evaluation and Scientific Infrastructure

这一方向讨论如何使 Frontier 主张可以被比较、复现和证伪。通用 Agent 综述普遍将 evaluation、datasets 和 leaderboards 作为独立的发展方向；视觉生成路线图也强调结构、物理、身份和因果压力测试，因为单一感知质量分数无法反映这些能力。

AVG 需要记录目标、状态、行动、观察、验证、成本、人工干预、失败分支和停止条件，并在不同视觉产物上设置可对照的过程测试。这个方向的成果是可复用的基准、数据、轨迹协议和审计方法，它们为其他 Frontier 提供证据基础。

## 以科学问题为中心的最终组织方案

Frontier 章节不应回答“有哪些模块”或“有哪些热门系统”，而应回答“现有 AVG 系统在哪些关键问题上仍无法稳定工作”。每个一级小节只讨论一个问题，并按照相同的论证顺序推进：

1. 说明问题及其在 AVG 中的具体含义；
2. 说明现有系统已经达到的边界；
3. 指出跨论文反复出现的缺口；
4. 解释缺口为什么不能靠更多采样、更多工具或更大的模型直接解决；
5. 给出能够判断进步的实验条件。

第三章中的六模块只在第二段或第三段作为实现条件出现。它们不应成为 Frontier 的标题，也不应在本章重新定义。

## 更高层的最终抽象

如果 Frontier 需要真正“高屋建瓴”，一级标题还应继续上移。`Structured Visual Understanding`、`Persistent State`、`Closed-Loop Reliability` 和 `Evaluation Infrastructure` 仍然是中层研究主题。它们应当服务于以下三个根本问题：

### 1. What Does It Mean for a Visual Agent to Understand?

这个问题讨论视觉生成系统是否从“产生符合统计外观的结果”发展为“理解它正在构造的对象、关系、过程和后果”。空间关系、身份、结构、物理、事实和时序只是这个问题在不同领域的表现。布局、记忆、程序、场景图和验证器是实现理解的不同载体。

真正的缺口是视觉生成系统能否形成对任务和产物的可检验理解，并让这种理解约束后续生成。重点不应写成“需要哪些中间表示”，而应写成：生成结果是否反映了系统对任务结构和世界关系的理解。

### 2. How Can Visual Creation Become a Sustained Form of Agency?

这个问题讨论视觉创作是否能够从一次性输出发展为持续的行动过程。系统需要在变化的状态中理解、决策、执行、观察、修正和结束。规划、工具、感知、恢复、预算和人类干预都是这个持续行动过程的实现条件。

真正的缺口是系统是否能够对自己的行动后果负责：它是否知道当前状态、是否能根据证据改变行为、是否能保留正确部分、是否能处理失败，并判断何时停止。这里的核心不是“闭环组件是否齐全”，而是视觉创作是否真正成为一个可控制的过程。

### 3. How Can Visual Agents Accumulate Intelligence?

这个问题讨论智能体是否能够超越单个任务，在持续经验中形成可迁移的创作能力。经验可以改变理解、规划、工具选择、验证、修复或与人的协作方式，但这些变化都属于同一个更高层问题：系统能否把过去的创作经历转化为未来的能力。

真正的缺口是系统能否在新任务和新环境中稳定迁移，同时保持原有能力、避免错误固化并接受审计和撤销。技能库、路由更新、经验记忆、合成数据和自我训练只是不同实现路径。

### 4. How Should Visual Agency Exist in the Human World?

这个问题讨论视觉智能体如何进入真实的人类活动、开放环境和具有责任后果的工作流。人类目标通常不完全形式化，视觉信息可能不可信，创作行为可能改变外部状态，结果还可能涉及版权、隐私、医疗、教育或公共传播。

真正的缺口是如何让系统在开放世界中保持可理解、可干预和可追责。权限、来源、安全、评测和人机协作是这个问题的条件，而不是独立的技术模块。

这四个问题构成比“五个能力轴”更高的组织层级：

```text
1. Understanding: 视觉智能体究竟理解什么？
2. Agency: 视觉创作如何成为持续行动？
3. Accumulation: 视觉智能如何跨任务积累？
4. Situatedness: 视觉智能如何存在于人类世界？
```

其中前三个是 AVG 的核心科学问题，第四个说明这些能力进入真实环境时必须满足的条件。第三章的模块、领域论文和评测协议都作为证据嵌入这四个问题，而不再另列为 Frontier。

### 开头：Frontier 的判断标准

开头先建立一个高层判断：AVG 的研究前沿位于“视觉结果是否能够被持续理解、操作、修复和迁移”的边界。一个方向只有在以下条件下才构成 Frontier：

- 现有论文在多个视觉领域反复暴露同一类失败；
- 失败涉及系统在状态、行动、证据或迁移上的能力缺口；
- 缺口需要新的表示、控制方式、学习过程或评测协议；
- 进步可以通过干预、对照、迁移或长期测试得到验证。

这一段还应说明：工具数量、Agent 数量、最终图像分数、单纯的额外采样和更长的执行轨迹都不能单独构成 Frontier 证据。

### 第一节：Structured Visual Understanding and Control

**核心问题：**

视觉生成系统能否把用户意图转化为可检查、可执行并能约束最终视觉结果的结构化状态？

本节先说明视觉生成中的困难不是只有语义理解，还包括空间关系、对象身份、属性绑定、时序关系、结构约束、数据关系和可编辑操作。随后说明现有系统已经使用布局、编辑程序、节点图、CAD 程序、数据结构、点级空间标记和视觉轨迹，但这些中间结构与最终结果之间仍可能脱节。

本节真正关注的缺口是：

- 中间推理是否忠实地约束最终产物；
- 结构化状态是否可以被观察、修改和验证；
- 同一种控制原则能否跨图像、视频、3D、文档和 UI 复用；
- 失败时系统能否知道是理解错误、表示错误还是执行错误。

代表文献可以综合 GenArtist、Divide and Conquer、MetaPoint、GenClaw、LightVA、SciFig、Node-Based Editing、NEWTON 等。不要逐篇介绍，而是按“文本或视觉推理—结构化中间状态—可执行表示—结果验证”的演化关系组织。

本节的终点不是提出更多规划器，而是提出一个更高层的判断：

> 视觉推理只有在中间状态能够约束、解释和修改最终视觉结果时，才构成可用的创作控制。

### 第二节：Persistent and Operable Visual State

**核心问题：**

视觉创作系统能否在长期交互中维护一个持续存在、可定位、可编辑和可追溯的视觉状态？

本节从一次性输出与持续创作的差异开始。图像、视频、CAD、图表、演示文档和 UI 都需要保留身份、关系、版本、依赖、来源和未解决约束。对话历史或文本摘要只能提供部分上下文，不能自动提供可操作的视觉状态。

本节应讨论四种持续性：

- 任务持续性：后续操作继续使用前面建立的要求和约束；
- 产物持续性：局部修改不破坏已确认的区域或结构；
- 关系持续性：对象、角色、镜头、数据和组件之间的依赖保持可追踪；
- 来源持续性：能够回到产生当前结果的源表示、工具调用或历史版本。

代表文献可以使用 StoryState、Agent Banana、Generation Navigator、PreGenie、DeepPresenter、CADSmith、IterCAD、SciFig 和 Cognitive-structured Multimodal Agent。这里不要把 memory 分类重新写一遍，而要说明它们共同面对的系统问题：如何把历史信息转化为可操作状态。

本节终点是：

> 长期视觉创作要求系统维护可操作的状态，而不仅是保留更多上下文。

### 第三节：Evidence-Grounded Closed-Loop Reliability

**核心问题：**

系统能否根据观察和验证证据选择正确的下一步行动，并在失败时修复而不是盲目重试？

这一节统一处理目前分散在 verification、diagnosis、recovery、rollback、stopping 和 budget 中的问题。先说明闭环的关键不是存在 critic 或 verifier，而是证据是否改变后续决策。然后讨论不同视觉产物需要不同证据：视觉、文字、结构、数值、几何、时序、物理和行为证据。

本节的缺口包括：

- 检测到错误但无法定位责任来源；
- 知道问题位置但无法选择合适的修复接口；
- 修复一个约束时破坏另一个已满足约束；
- 反复生成提高了分数，却没有证明系统理解失败原因；
- 系统不知道何时继续、停止、回滚或请求人类帮助。

代表文献可以综合 PhysAgent、CADSmith、IterCAD、GenArtist、PreGenie、PlotGen、CoSTA、FaSTA、AMACE、VISTA、Generation Navigator 和 Action Agent。不要把每种验证器单独列为 Frontier，而要把它们放入“证据如何改变行动”的主问题中。

本节应给出统一的证明标准：控制失败类型和资源预算，比较固定流程与自适应流程，记录证据、后续行动、修复范围、停止决定和副作用。

本节终点是：

> 闭环可靠性取决于证据是否能够支持诊断、修复和停止，而不取决于系统是否生成了更长的执行轨迹。

### 第四节：Cross-Task Learning and Self-Evolving Creation

**核心问题：**

系统能否从过去的视觉创作轨迹中获得能够迁移到新任务的行为能力？

本节先区分任务内反思、候选选择、检索历史案例和真正的跨任务自我改进。随后说明经验可以表现为案例、策略、技能、工具、路由知识或模型更新，但这些形式都必须最终改变后续任务中的决策。

本节重点不在于列举 self-evolving 系统，而在于解释学习链条：

完成轨迹 → 提取经验 → 归因成功或失败 → 形成可复用表示 → 在新任务中调用 → 验证行为变化。

代表文献可以使用 GenEvolve、SIDiffAgent、OctoT2I、COMFYCLAW、VideoWeaver、EvoIR-Agent、SEAR 和 DataEvolver。每篇只需说明它改变了什么后续行为，以及是否提供了跨任务证据。

本节需要明确的研究缺口是：

- 如何区分真正学习与更多检索、更多采样或更强生成器；
- 如何避免错误经验和评测偏差被固化；
- 如何在不同工具、领域和任务分布之间迁移；
- 如何检测遗忘、污染和能力退化；
- 如何版本化、审计和撤销更新。

本节终点是：

> 自我改进的 Frontier 是可验证的行为迁移，而不是单次轨迹中的质量提升。

### 第五节：Open-World Human--Agent Co-Creation

**核心问题：**

视觉创作智能体能否在不完全可观测、包含不可信信息和外部副作用的真实环境中与人类共同工作？

本节把 human authority、开放环境、权限、来源、版权、安全和人类负担组织成一个系统问题。重点不是提出更多安全模块，而是说明真实创作中的目标通常由人和 Agent 共同形成，工具可能改变外部状态，视觉和音频内容可能携带误导性指令，生成结果还可能进入发布、医疗、设计或教育等高后果场景。

代表性背景可以来自 AgentDojo、VisualWebArena、OSWorld、C2PA、间接 prompt injection 和多模态安全研究，也可以结合个性化创作、医疗视频和科学可视化中的人机协作案例。

本节需要讨论：

- 系统如何请求澄清、授权、批准或接管；
- 人类如何理解 Agent 已经改变了什么；
- 来源、工具权限和责任如何贯穿整个创作轨迹；
- 如何衡量人类负担、信任校准和干预时机。

本节终点是：

> 开放环境中的 AVG 能力必须与人类权限、来源和可追责性一起定义。

### 收束段：How Progress Should Be Established

最后不再单独列一个“Benchmarks” Frontier，而用一段收束所有问题。说明不同 Frontier 都需要 trajectory-level evidence，包括目标、状态、行动、观察、验证、成本、人工干预、失败分支和停止条件。最终评测应同时覆盖视觉质量、约束满足、状态保持、行动选择、恢复、迁移、人类负担和安全。

这一段的作用是说明“如何知道 Frontier 被推进了”，而不是再增加一个研究方向。

## 最终标题结构

```latex
\section{Challenges and Research Frontiers}

% opening: what counts as a frontier
\subsection{Structured Visual Understanding and Control}
\subsection{Persistent and Operable Visual State}
\subsection{Evidence-Grounded Closed-Loop Reliability}
\subsection{Cross-Task Learning and Self-Evolving Creation}
\subsection{Open-World Human--Agent Co-Creation}

% closing: how progress should be established
```

## 不应作为一级 Frontier 的内容

- `Memory`、`Tool Use`、`Verification`、`Recovery`、`Budget`：它们是第三章机制或上述问题的内部条件。
- `Generalist Visual Creation Agents`：范围过宽，应作为五个问题共同指向的系统形态。
- `Human Authority`、`Security`、`Copyright`、`Provenance`：它们是开放部署条件，应放在人机共创问题中。
- `Benchmarks`、`Trajectory Logging`、`Reproducibility`：它们是证明前沿进展的科学基础，应放在结尾。
- `World Model`：只有在强调行动条件、干预结果和因果一致性时才是 Frontier；单纯更长视频或更多场景不构成世界模型前沿。

```latex
\section{Challenges and Research Frontiers}

\subsection{Visual Reasoning and Structured Control}
\subsection{Persistent and Interactive Visual Worlds}
\subsection{Continual Learning and Self-Evolving Creation}
\subsection{Human--Agent Co-Creation in Open Environments}
\subsection{Evaluation and Scientific Infrastructure}
```

章节开头应说明：这些方向描述 AVG 可能形成的系统能力，第三章的六模块是实现这些能力的机制。两者不能重复成平行分类。

每个小节建议采用三段结构：第一段定义能力方向及其意义；第二段综合本地代表工作已经展示的进展；第三段说明尚未解决的核心问题和能够证明进展的评测条件。具体论文用于支撑趋势和缺口，不逐篇排列。

## 现有 Frontier 内容的归并方式

- Evidence-based autonomy、planning、visual chain-of-thought、intermediate representations 和 tool-mediated control 归入 `Visual Reasoning and Structured Control`。
- Memory、editable state、provenance、physical grounding 和 interactive world models 归入 `Persistent and Interactive Visual Worlds`。
- Cross-task learning、skill acquisition、tool creation、visual self-play 和 safe self-evolution 归入 `Continual Learning and Self-Evolving Creation`。
- Human authority、copyright、security、cost、permission and open-world interaction 归入 `Human--Agent Co-Creation in Open Environments`。
- Evaluation、benchmarks、trajectory evidence、stress tests and reproducibility 归入 `Evaluation and Scientific Infrastructure`。

这样可以避免把第三章的运行机制重新复制为 Frontier，也能把章节重点从具体工程缺口提升到系统能力的发展方向。
