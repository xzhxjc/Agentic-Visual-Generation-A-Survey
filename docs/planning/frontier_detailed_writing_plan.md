# Frontier 章节详细写作规划

## 一、章节目标

本章讨论 Agentic Visual Generation（AVG）未来真正需要解决的高层问题。章节重点是研究范围、智能提升、可靠评测和更广泛的理论与社会条件，不再重复第三章的六个运行模块。

第三章回答“一个 AVG 系统如何运行”，说明目标理解、规格与规划、记忆、工具、感知、行动和跨任务自我改进如何形成运行闭环。本章回答“AVG 还要解决什么”，说明视觉创作的应用边界如何扩大、系统智能如何提升、研究进展如何被证明，以及这些系统进入真实世界后会遇到什么问题。

本章不把具体组件直接写成 Frontier。Memory、Tool Use、Verification、Recovery、Budget、Stopping、Skill 和 Human Feedback 都是实现高层能力的机制。它们只在解释某个研究问题时出现。

本章不写成论文列表，不按“论文 A 做了什么、论文 B 做了什么”的顺序展开。论文只作为现象、趋势、局限和研究缺口的证据载体；本规划阶段不放引用，正式写正文时再逐条核对原文和 Bib。

## 二、总论点

章节开头建立以下判断：

视觉生成系统已经能够产生高质量的视觉结果，但高质量的单次结果不等于视觉智能体已经能够理解、控制、学习和负责。Agentic Visual Generation 的 Frontier 位于以下四个层面：

1. 创作系统能够覆盖多么复杂、多么开放和多么高后果的场景；
2. 视觉智能体能够达到多高的理解、规划、行动和学习水平；
3. 研究者如何可靠地区分真正的能力提升与额外采样、更多工具或更高预算；
4. 视觉智能体如何在真实人类环境中处理作者性、权限、责任、来源和安全。

全文围绕一条发展主线推进：

```text
single-pass rendering
    -> complex visual workflows
    -> sustained agentic creation
    -> continual visual intelligence
    -> open-world human-agent systems
```

这条主线描述系统能力的扩展，不是新的自主性等级。L1--L5 仍然是全文唯一的自主性等级体系；本章的一级标题描述研究问题和发展方向。

## 三、章节层级

```latex
\section{Challenges and Research Frontiers}

% Opening: What the Frontier chapter studies

\subsection{I. Expanding the Scope of Visual Agency}
\subsubsection{From Single Artifacts to Multimodal Creative Workflows}
\subsubsection{From Short Tasks to Long-Horizon Projects}
\subsubsection{From Closed Toolchains to Open Environments}
\subsubsection{From Digital Creation to Embodied and High-Consequence Domains}

\subsection{II. Increasing the Intelligence of Visual Agents}
\subsubsection{Generative and Multimodal Foundation Models}
\subsubsection{Agent Architecture and Control}
\subsubsection{Visual Reasoning and World Knowledge}
\subsubsection{Agentic Reinforcement Learning and Process Training}
\subsubsection{Memory, Continual Learning, and Self-Evolution}
\subsubsection{Multi-Agent Collaboration and Human Co-Creation}
\subsubsection{Efficiency and Scalable Deployment}

\subsection{III. Establishing Reliable Evaluation}
\subsubsection{Beyond Final-Artifact Quality}
\subsubsection{Process, Causal, and Counterfactual Evaluation}
\subsubsection{Long-Horizon and Cross-Task Evaluation}
\subsubsection{Multidimensional Visual Correctness}
\subsubsection{Human, Cost, Safety, and Provenance Evaluation}

\subsection{IV. Broader Questions}
\subsubsection{What Counts as Visual Agency?}
\subsubsection{What Does Intelligence Mean in Visual Creation?}
\subsubsection{Authorship, Responsibility, and Human Control}
\subsubsection{From Individual Models to Creative Ecosystems}

% Closing: Conditions for claiming progress
```

这一层级是完整的 brainstorming 结果。正式写作前仍需根据篇幅合并小节。最少保留三个一级部分：场景扩大、智能提升、可靠评测。第四部分用于提升理论高度，可压缩为结尾讨论。

## 四、开头段落规划

### 1. 说明现有进展

先概括当前系统已经具备的能力：系统可以组合生成器、编辑器、代码环境、检索服务、模拟器、视觉评估器和人类交互，并处理图像、视频、3D、CAD、科学图表、文档、网页和交互界面等产物。

这一段只说明研究范围已经扩大，不列举具体论文和具体工具名称，不讨论模型内部结构。

### 2. 指出当前描述方式的不足

说明最终图像质量、工具数量、Agent 数量和执行步数不能充分描述 AVG 的发展。一个长流程可能只是固定工作流，一个高分结果可能来自更多候选采样，一个带有反馈模块的系统也可能没有真正改变后续行动。

这一段要直接陈述比较问题，不写防御性解释，不写“我们并不是说……”等句式。

### 3. 给出本章的分析维度

说明本章从三个主要问题展开：

- 场景范围如何扩大；
- 智能程度如何提升；
- 如何建立可信评测。

随后用一段说明第四部分的作用：讨论 AVG 作为一种新型创作系统的理论边界、作者关系和生态条件。

### 4. 说明 Frontiers 的判断标准

一个方向只有同时满足以下条件时，才适合作为 Frontier：

- 在多个视觉领域或多个系统中反复出现；
- 暴露的是系统能力缺口，而不是单一实现细节；
- 需要新的表示、架构、训练方式、交互模式或评测方法；
- 可以通过对照、干预、迁移、长期运行或开放环境测试进行验证。

## 五、第一部分：Expanding the Scope of Visual Agency

这一部分回答“AVG 将在哪里运行”。重点是场景空间、任务复杂度、环境开放程度和责任范围的扩大。

### 5.1 From Single Artifacts to Multimodal Creative Workflows

#### 讨论对象

从单一图像或单一视频扩展到多个视觉与非视觉产物共同构成的创作过程。产物可以包括文本、图像、音频、视频、布局、源代码、数据、几何结构、网页和交互状态等。

#### 需要说明的变化

- 多模态内容之间存在依赖关系；
- 一个产物的变化可能影响其他产物；
- 不同产物使用不同的生成、编辑和验证方式；
- 用户可能只希望修改其中一部分；
- 系统需要协调内容、结构、时序和交互。

#### 需要提出的问题

- AVG 是否能够协调不同模态，而不只是依次调用多个模型；
- 不同模态之间的状态和意图如何传递；
- 多模态创作中哪些内容应该共同更新，哪些内容应该保持不变；
- 如何评价跨模态一致性、互补性和局部可编辑性。

#### 写作边界

不要把这一节写成 image、video、audio、text 的并列介绍。重点是“多模态工作流”作为一种更复杂的创作场景，以及它带来的状态、依赖和评价问题。

### 5.2 From Short Tasks to Long-Horizon Projects

#### 讨论对象

从一次生成、一次编辑和短对话扩展到多轮修改、长视频、多场景叙事、长期设计项目和持续用户合作。

#### 需要说明的变化

任务变长后，系统必须面对累积误差、身份漂移、结构漂移、目标变化、版本分支、历史决策和有限资源。长程任务的难点不是简单增加步骤，而是每一步都会改变后续任务的条件。

#### 需要提出的问题

- 系统能否保持早期决定与后期动作的一致；
- 能否在长程任务中局部修改而不破坏已确认部分；
- 能否处理用户中途改变目标或约束；
- 能否在任务没有明显终点时判断何时停止；
- 长期运行中的经验是否会提升系统，还是只积累噪声。

#### 写作边界

不要只写“支持更多轮对话”或“生成更长视频”。必须说明长程任务改变了控制问题的性质。

### 5.3 From Closed Toolchains to Open Environments

#### 讨论对象

从预先定义的工具集合、固定 API 和稳定执行环境扩展到开放工具生态。开放环境包括工具版本变化、接口差异、未知工具、外部信息服务、代码环境、应用程序、浏览器和模拟器等。

#### 需要说明的变化

开放环境要求 Agent 处理工具能力不确定、输入输出不兼容、权限差异、运行错误、资源限制和副作用。

#### 需要提出的问题

- Agent 能否理解新工具的能力和限制；
- 能否创建、组合或迁移工具；
- 能否在工具失败时寻找可解释的替代路径；
- 能否区分工具能力不足与任务理解错误；
- 工具生态扩大后，系统是否仍然可控和可审计。

#### 写作边界

不要把“工具数量更多”写成进步。Frontier 是 Agent 能否在不稳定工具环境中维持任务目标和可靠行动。

### 5.4 From Digital Creation to Embodied and High-Consequence Domains

#### 讨论对象

从屏幕中的数字创作扩展到机器人导航、物理模拟、交互式 3D 世界、医疗训练、教育、科学研究、工业设计、建筑和公共传播等场景。

#### 需要说明的变化

在这些领域，视觉结果不只是被观看，还可能指导行动、影响决策、进入生产或产生真实风险。错误的代价从“不好看”变成“不可执行、不安全、不合规或不可追责”。

#### 需要提出的问题

- 视觉生成结果能否满足领域约束；
- 行动后的未来状态是否符合物理和任务要求；
- Agent 是否需要不同等级的人类监督；
- 如何处理医疗、工程和公共传播中的责任；
- 不同领域是否需要不同的 autonomy target。

#### 写作边界

不要把应用领域写成简单的应用清单。每个领域只用于说明场景扩大后，正确性、风险和人类权限发生了变化。

## 六、第二部分：Increasing the Intelligence of Visual Agents

这一部分回答“AVG 如何变得更智能”。需要同时覆盖基础模型、Agent 架构、训练方式、记忆、协作、世界知识和部署效率。

### 6.1 Generative and Multimodal Foundation Models

#### 讨论对象

生成器、理解模型和统一多模态基础模型是 Agent 智能的底层基础。

#### 可讨论因素

- 图像、视频、3D、音频和文本的生成质量；
- 长文本、复杂指令和多模态输入理解；
- 统一理解与生成；
- 空间、时序、身份、关系和结构建模；
- 精细编辑和局部控制；
- 更长视频、更大场景和更高分辨率；
- 世界知识、事实 grounding 和物理先验；
- 训练数据、合成数据、蒸馏、偏好对齐和后训练；
- 推理速度、显存和规模化部署。

#### 核心问题

基础模型能力提升如何转化为 Agent 的真实创作能力？更强的单步生成是否能减少 Agent 的控制负担，还是会把错误隐藏得更深？

#### 写作边界

这一节不写成生成模型综述。只讨论基础模型如何支撑 AVG 的理解、控制、记忆、行动和评测。

### 6.2 Agent Architecture and Control

#### 讨论对象

讨论 Agent 如何组织理解、规划、工具、感知和行动。

#### 可讨论因素

- 外部编排式 Agent；
- 原生视觉生成 Agent；
- 统一理解、规划和生成架构；
- planner、executor、perception 和 verifier 的组合方式；
- 单 Agent、多 Agent、分层 Agent 和动态角色分配；
- 显式状态与隐式状态；
- 固定工作流与自适应控制；
- 模块化系统与端到端系统之间的取舍；
- 用户、工具、模型和环境之间的接口设计。

#### 核心问题

Agent 架构如何让视觉理解、行动和结果相互约束，而不是只增加组件数量？不同架构如何在可解释性、灵活性、效率和可靠性之间取舍？

### 6.3 Visual Reasoning, World Knowledge, and Causal Understanding

#### 讨论对象

讨论 Agent 是否能理解视觉产物背后的结构、事实、关系、过程和行动后果。

#### 可讨论因素

- 空间和几何推理；
- 对象、属性和关系绑定；
- 时序和事件推理；
- 世界知识与外部检索；
- 结构化数据、代码和文档理解；
- 物理和因果推理；
- 不确定性和信息缺口识别；
- 视觉 chain-of-thought 和结构化中间表示；
- counterfactual reasoning 和 action-conditioned prediction。

#### 核心问题

系统是否真正理解了视觉任务，还是只生成了统计上合理的外观？视觉推理是否真实约束最终产物和后续行动？

### 6.4 Agentic Reinforcement Learning and Process Training

#### 讨论对象

讨论如何训练 Agent 学会连续决策，而不只是生成一个最终结果。

#### 可讨论因素

- 工具调用和轨迹监督；
- SFT、preference learning、RLHF、RLAIF 和 agentic RL；
- 过程奖励、轨迹奖励和结果奖励；
- 视觉反馈和环境反馈；
- 失败轨迹和负样本；
- 搜索、规划、分支和反事实训练；
- 视觉 self-play 和 synthetic trajectories；
- credit assignment；
- reward hacking 和 evaluator bias；
- 训练时策略与推理时策略的一致性。

#### 核心问题

如何让 Agent 学会在不同状态下选择不同动作，并且让奖励真正反映创作过程、资源消耗、约束满足和人类偏好？

#### 写作边界

不要把“用了 RL”直接写成智能提升。必须说明学习改变了什么行为，以及是否有跨任务和过程证据。

### 6.5 Memory, Continual Learning, and Self-Evolution

#### 讨论对象

讨论 Agent 如何从单任务信息和历史轨迹中形成未来可用的创作能力。

#### 可讨论因素

- 工作记忆与跨任务记忆；
- 视觉、结构化和多模态记忆；
- 经验、案例、策略和技能；
- memory formation、evolution 和 retrieval；
- 工具创建和工具路由学习；
- 多 Agent 共享记忆；
- 个性化和用户偏好；
- 遗忘、错误记忆、污染和安全更新；
- 参数更新、外部 memory 和混合形式。

#### 核心问题

如何让系统从经验中获得可迁移能力，同时防止错误策略固化、旧能力退化和评测污染？

### 6.6 Multi-Agent Collaboration and Human Co-Creation

#### 讨论对象

讨论多个 Agent 和人类如何共同形成创作目标、探索方案、评价候选和完成作品。

#### 可讨论因素

- 任务分配和角色设计；
- 通信协议和共享工作空间；
- 专业能力互补；
- debate、critique、consensus 和 competition；
- 主动性和 initiative control；
- divergent exploration 与 creative diversity；
- 人类在目标设定、选择、评价和编辑中的作用；
- 作者性、贡献归属和用户控制感；
- 人类负担、信任校准和适当依赖。

#### 核心问题

多 Agent 和人机协作是否真正提高了创作智能、探索空间和用户价值，还是只是增加了沟通和评价成本？

### 6.7 Efficiency and Scalable Deployment

#### 讨论对象

讨论智能提升如何在真实计算和用户预算下运行。

#### 可讨论因素

- 推理延迟；
- 多轮生成成本；
- 多 Agent 通信；
- 视频和 3D 的计算规模；
- 动态计算分配；
- early stopping；
- quality--cost 和 quality--latency trade-off；
- 端侧、云端和混合部署；
- 能源和环境成本；
- 大规模用户服务和可靠性。

#### 核心问题

更高智能是否能够在可接受的时间、计算、能源和人力成本下运行？

## 七、第三部分：Establishing Reliable Evaluation

这一部分回答“如何知道 AVG 真正进步了”。它不是简单罗列指标，而是分析现有评测为什么不足。

### 7.1 Beyond Final-Artifact Quality

说明当前评测通常关注最终图像、视频或任务成功率，但无法证明规划、反馈、记忆、工具选择和恢复真正发挥了作用。

需要区分：

- artifact quality；
- task and constraint satisfaction；
- state retention；
- action selection；
- diagnosis and recovery；
- stopping and escalation；
- transfer and self-improvement。

### 7.2 Process, Causal, and Counterfactual Evaluation

要求记录完整 trajectory：状态、动作、观察、验证、成本、失败、恢复和停止。

需要回答：

- feedback 是否真的改变后续行动；
- 不同观察是否导致不同决策；
- 修复是否改善失败约束并保持已满足约束；
- 成功来自真正理解还是来自额外采样；
- rollback 是否优于重新生成。

### 7.3 Long-Horizon and Cross-Task Evaluation

评测需要覆盖：

- 长对话和长项目；
- 多场景和多轮编辑；
- 跨工具和跨领域迁移；
- 新用户和新偏好；
- 工具变化和环境变化；
- 遗忘、污染和持续学习。

### 7.4 Multidimensional Visual Correctness

不能用单一 aesthetic score 代表视觉正确性。需要综合：

- 外观和感知质量；
- 语义和指令满足；
- 空间、几何和拓扑；
- 对象身份和属性绑定；
- 时序和跨镜头一致性；
- 结构和可编辑性；
- 数据、事实和引用；
- 物理和因果；
- 行动后的环境状态。

### 7.5 Human, Cost, Safety, and Provenance Evaluation

评测还要报告：

- 模型、工具、检索和 Agent 调用；
- 生成候选数量；
- 人工介入次数和时机；
- 用户等待时间和认知负担；
- 信任和依赖是否校准；
- 不可信输入、prompt injection 和工具副作用；
- 来源、授权和版本记录。

## 八、第四部分：Broader Questions

这一部分不宜过长，用于提升文章理论高度。

### 8.1 What Counts as Visual Agency?

讨论何时属于 Agentic Visual Generation：多轮生成、工具调用、反馈、环境交互和持续学习之间的边界是什么？

### 8.2 What Does Intelligence Mean in Visual Creation?

讨论视觉智能是否只包含质量和正确性，还是也包括理解、规划、创造性、适应性、主动性、风险意识和责任能力。

### 8.3 Authorship, Responsibility, and Human Control

讨论人类创作者、Agent、模型、工具和数据在创作中的角色、贡献、作者性和责任如何界定。

### 8.4 From Individual Models to Creative Ecosystems

讨论未来竞争单位是否从单个生成模型转向模型、Agent 架构、工具生态、数据闭环、评测体系、人类工作流和计算基础设施的整体系统。

## 九、每一节的统一写作顺序

每个小节严格按照以下顺序：

1. 先定义本节讨论的宏观问题；
2. 再说明这一问题为什么会随着 AVG 场景或智能程度扩大而出现；
3. 然后综合已有研究已经展示的能力，不逐篇流水账；
4. 再指出反复出现的未解决缺口；
5. 说明缺口需要哪些类型的模型、架构、数据、训练、交互或基础设施支持；
6. 最后说明什么样的实验可以证明真正进步。

## 十、写作规范

### 10.1 层级规范

- 一级部分讨论高层问题：场景范围、智能提升、评测可靠性和理论/社会条件。
- 二级小节讨论一个相对完整的研究方向。
- 不把第三章模块名称直接作为 Frontier 标题。
- 不把单个模型、单个算法、单个 benchmark 或单个工具命名为 Frontier。
- 不把“增加 Agent 数量”“增加调用次数”“增加采样预算”直接等同于智能提升。
- L1--L5 仍是全文唯一的自主性等级体系，本章不得引入另一套等级编号。

### 10.2 叙述规范

- 每段只推进一个宏观论点。
- 先讲问题，再讲现有进展，再讲缺口和研究条件。
- 不从某一篇论文直接推导领域共识。
- 综合判断使用“部分工作”“现有研究表明”“在所调查文献中”等有边界的表达。
- 不把未来建议写成当前事实。
- 不把路线图、综述或观点文章写成实验性证据。
- 不把邻接领域的成果直接写成 AVG 已经解决的问题。

### 10.3 防御性写作规范

完全避免为了预防质疑而加入的否定式辩护，尤其避免：

- `rather than ...`；
- `not only ... but also ...`；
- `does not by itself ...`；
- `the goal is not ... but ...`；
- `this is not merely ...`；
- `not a ... but a ...`。

需要界定边界时，直接陈述对象、条件和证据要求。不要先假设读者会误解，再用否定句解释作者没有声称什么。

### 10.4 避免虚浮和宣传式表达

删除没有事实内容的词语和句子，例如：

- `promising`；
- `powerful`；
- `seamless`；
- `comprehensive`；
- `transformative`；
- `groundbreaking`；
- `paradigm shift`；
- `opens a new era`；
- `paves the way`；
- `underscores the importance`。

如果必须表达价值，改成具体的任务、指标、资源条件、失败模式或部署影响。

### 10.5 列举规范

- 列举机制、领域、指标或应用时，应使用开放性表达，如 `among others`、`and related settings`、`and other ...`。
- 不把列举写成封闭集合，除非确实是形式定义或明确分类。
- 不连续罗列十几个模型、工具或领域来制造信息密度。
- 每次列举都要服务于当前高层论点。

### 10.6 引用规范

- 本规划阶段不放引用；正式正文阶段再逐条加入。
- 理论框架和作者自己的综合判断可以不逐句引用。
- 具体论文的方法、结果、数字、能力和限制必须引用原论文。
- 一条引用不能替整段不同类型的事实背书。
- 综述或路线图只能支持其明确提出的趋势和观点，不能代替原论文的实验依据。
- 尚未读取全文或无法确认的论文不用于支撑关键论断。
- Bib 的作者、题名、年份、venue、页码、DOI 和 URL 只填写已核验字段。
- 正文完成后必须检查 citation key 是否存在、是否重复、是否出现 undefined citation，并再次编译。

### 10.7 术语规范

全文统一使用：

- `Agentic Visual Generation`；
- `single-pass rendering`；
- `closed-loop visual creation`；
- `state-dependent decision`；
- `visual reasoning`；
- `continual learning`；
- `self-evolution`；
- `human--agent co-creation`；
- `trajectory-level evaluation`。

不要为了变换表达而频繁替换核心术语，也不要引入第三章没有定义的新模块名称。

## 十一、文献组织规范

正式写作时，每个高层小节只选取能够代表趋势、缺口或方法转变的文献。文献组织采用“问题簇”而不是时间顺序：

- 先写已有系统共同显示的能力；
- 再写它们共同暴露的缺口；
- 最后说明研究方向和验证条件。

同一篇论文可以在不同章节出现，但每次引用必须服务于不同的分析问题。不要为了满足篇数要求重复引用同一篇论文，也不要用一篇论文替整个领域背书。

## 十二、完成前检查清单

- 是否首先讲了高层问题，而不是组件或技术？
- 场景扩大、智能提升和评测是否被清楚区分？
- 是否覆盖了图像、视频、3D/CAD、科学可视化、文档、UI/Web、具身和高后果场景？
- 基础模型、架构、数据、训练、Agentic RL、记忆、协作和效率是否放在“智能提升”部分，而不是散落成多个重复 Frontier？
- 评测是否区分最终质量、过程控制、长期迁移、人类负担、成本和安全？
- 是否把 Future Work 写成了当前已经存在的能力？
- 是否存在具体但没有宏观作用的技术罗列？
- 是否出现防御性写作、空泛评价或宣传式语言？
- 是否保持 L1--L5 和第三章六模块术语一致？
- 是否所有正式引用和 Bib 信息都已经回到原文核验？
- 是否编译后检查了 undefined citation、重复引用和排版问题？
