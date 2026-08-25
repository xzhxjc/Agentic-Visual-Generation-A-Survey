# Agentic Visual Generation 术语规范

## 核心概念

| English | 中文 | 解释 |
|---|---|---|
| Agentic Visual Generation (AVG) | 智能体式视觉生成（AVG） | 目标驱动的闭环视觉创作系统；运行时观测能够改变后续创作动作。 |
| agentic visual generation | 智能体式视觉生成 | 正文中的普通名词；首次写全称并给出 AVG。 |
| closed-loop visual creation | 闭环视觉创作 | 中间产物、任务环境或交互历史的运行时信息影响后续决策的创作过程。 |
| single-pass rendering | 单次渲染 | 从初始条件产生一次结果，未进行任务级修订决策。 |
| open-loop sampling | 开环采样 | 运行时产物或环境信息不改变后续动作选择的生成过程。 |
| visual creation trajectory | 视觉创作轨迹 | 围绕一个目标展开的状态、动作、观测和决策序列。 |
| creation control | 创作控制 | 对约束、状态、观测、修正、恢复和终止的任务级管理。 |
| observation--action dependency | 观测—动作依赖 | 运行时信息以可追踪的方式改变后续动作选择；AVG 的核心行为判定。 |
| state-dependent control | 状态依赖控制 | 后续决策依赖当前任务状态、观测或历史，而非仅依赖初始输入。 |
| state-dependent creation decision | 状态依赖的创作决策 | 由任务状态或运行时证据条件化的后续创作决策。 |

## 对象与系统组件

| English | 中文 | 解释 |
|---|---|---|
| visual generation | 视觉生成 | 根据任务信息产生或修改视觉结果的能力或操作。 |
| visual creation | 视觉创作 | 包含生成、编辑、检验、修正、协作等步骤的目标导向过程。 |
| visual artifact | 视觉产物 | 系统创建、编辑或交付的对象；正文优先使用此词。 |
| visual product | 视觉产品 | 跨领域归类时使用的总称；描述单个对象时优先用 `visual artifact`。 |
| editable visual environment | 可编辑视觉环境 | 可保留并继续修改的场景、应用、世界或界面状态。 |
| generator | 生成器 | 产生或编辑视觉结果的模型、渲染器或执行器；不等同于 controller。 |
| controller | 控制器 | 根据目标、状态和证据选择后续动作的功能实体。 |
| agent | 智能体 | 具有可识别决策职责的实体；具体角色应说明其职责。 |
| executor | 执行器 | 实际执行已选动作的模型、软件、API、代码运行时或环境。 |
| task environment | 任务环境 | 返回状态或证据、并影响创作结果的外部环境。 |
| execution interface | 执行接口 | 控制器可调用的具体操作及其输入、输出、错误、代价和可逆性；它把决策转为可执行动作。 |
| action space | 动作空间 | 当前系统可执行的动作及其输入、输出、错误、成本和可逆性。 |
| artifact representation | 产物表征 | 视觉产物在系统中被保存、检查和修改的形式。 |
| editable representation | 可编辑表征 | 可被定位和修改的表示，如图层、参数、源数据、代码或层级结构。 |

## 输入、规格与状态

| English | 中文 | 解释 |
|---|---|---|
| condition / conditioning input | 条件 / 条件输入 | 某一次生成或编辑操作开始前可用的信息；可来自原始请求、当前产物、已验证状态或用户澄清。 |
| prompt | 提示词 | 一类文本条件输入；不代替完整任务规格、状态或计划。 |
| task goal | 任务目标 | 用户或任务规定的最终意图和目标产物。 |
| constraint | 约束 | 需满足或检查的要求，如身份、关系、数据、功能或安全要求。 |
| invariant | 不变量 | 在一段轨迹或一组操作中必须保持的约束。 |
| operational specification | 操作性规格 | 将目标、参考、约束、假设和验收条件转化为可执行、可验证承诺的表示。 |
| task-relevant state | 任务相关状态 | 后续决策需要读取、保留或更新的信息。 |
| persistent state | 持久状态 | 跨多个步骤或轮次保留并可访问的任务相关状态。 |
| interaction history | 交互历史 | 用户指令、系统动作、工具返回和人工决策的历史记录。 |
| provenance | 溯源信息 | 记录资产、状态或决策的来源、版本、依赖和适用范围。 |
| addressable state | 可寻址状态 | 可定位到对象、区域、帧、组件、操作或依赖节点的状态。 |

## 轨迹与动作

| English | 中文 | 解释 |
|---|---|---|
| artifact action | 产物动作 | 直接改变产物的动作，如生成、编辑、合成、渲染、模拟或执行。 |
| control action | 控制动作 | 改变轨迹如何继续的动作，如选工具、更新计划、分配预算、回滚或终止。 |
| execution outcome | 执行结果 | 动作对产物、环境、错误、成本或状态产生的可观察结果。 |
| state transition | 状态转移 | 动作执行后任务、产物、记忆或环境发生的变化。 |
| checkpoint | 检查点 | 可恢复的可信状态或产物版本。 |
| semantic decomposition | 语义分解 | 将复杂目标拆分为可检查的子目标。 |
| production planning | 制作规划 | 安排资产、布局、生成、整合和审查等生产阶段。 |
| tool planning | 工具规划 | 选择执行器并构造其所需输入。 |
| reactive planning | 反应式规划 | 根据失败、新观测或新用户指令修改余下轨迹。 |
| execution contract | 执行契约 | 对步骤记录前置条件、允许动作、观测点、预期状态转移和后置条件。 |

## Perception and evidence

| English | 中文 | 解释 |
|---|---|---|
| observation | 观测 | 获取任务相关信号，如渲染图、日志、测试、仿真输出或人工意见。 |
| diagnosis | 诊断 | 将观测关联到失败假设、受影响对象、可能原因和修复范围。 |
| verification | 验证 / 校验 | 检验一个显式约束是否满足的过程。 |
| verifier | 验证器 / 校验器 | 提供验证结果的规则、程序、模型、模拟器或人工程序。 |
| validator | 校验器 / 验证组件 | 文献原称为 validator 时保留；泛指约束检查时优先统一为 verifier。 |
| judge | 评判器 | 进行评分、比较或偏好判断的学习模型或人工组件；结果不默认是真值。 |
| decision evidence | 决策证据 | 可支撑后续动作选择的结构化信息。 |
| feedback action | 反馈行动 | 将观测、诊断、验证或用户输入传递或应用到后续动作的行动。 |
| feedback | 反馈 | 可被后续动作使用的观测、诊断、验证、用户意见或执行结果。 |
| critique | 评议 / 批评 | 文本、分数或结构化形式的评审结果。 |
| failure localization | 故障定位 | 标识失败对应的对象、区域、帧、组件、操作或依赖链。 |
| heterogeneous verification | 异构验证 | 按不同约束组合规则、参考比较、学习评判、执行测试、模拟和人工审查。 |
| verifier portfolio | 验证器组合 | 与产物语义和约束类型对应配置的多类验证器。 |
| evidence fusion | 证据融合 | 汇聚多个验证结果，并在聚合前保留不一致和不确定性。 |

## 修订、恢复与人类参与

| English | 中文 | 解释 |
|---|---|---|
| revision | 修订 / 修正 | 根据新信息对计划、输入、工具、产物或状态作出的后续改动。 |
| local repair | 局部修复 | 在已定位范围内修改，并保留不受影响的已满足约束。 |
| replanning | 重新规划 | 修改余下目标分解、执行顺序、依赖关系或工具路径。 |
| tool substitution | 工具替换 | 以另一具有兼容输入输出语义的执行器替代当前工具。 |
| recovery | 恢复 | 在失败、冲突或损坏状态下回到可接受轨迹的控制过程。 |
| rollback | 回滚 | 恢复到可信检查点或较早状态版本。 |
| stopping | 终止 / 停止决策 | 判断任务已完成、继续收益不足或需要中止的控制动作。 |
| adaptive stopping | 自适应终止 | 基于约束、置信度、成本、风险和不确定性决定是否停止。 |
| human-in-the-loop | 人在回路中 | 人参与某一环节；应进一步说明具体输入和权限。 |
| mixed-initiative control | 混合主动式控制 | 人与系统都可发起、修改或接管部分创作决策。 |
| human authority | 人类权限 | 人对澄清目标、批准计划、授权高风险动作或接受结果拥有的正式权限。 |
| human escalation | 请求人类决策 / 人类升级 | 系统将未决或高风险状态交由人处理的动作。 |
| human computation | 人类计算 | 人工候选选择、提示修复、标注或编辑等实际贡献。 |

## 工作流、架构与自主性

| English | 中文 | 解释 |
|---|---|---|
| workflow | 工作流 | 面向任务的步骤安排。 |
| fixed workflow | 固定工作流 | 阶段、参数和控制决策预先规定的工作流。 |
| pipeline | 流水线 | 具有固定阶段和输入输出交接关系的工作流。 |
| orchestration | 编排 / 协同调度 | 对模型、工具、角色或阶段的组织与调度方式。 |
| routing | 路由 | 在模型、工具、角色或执行路径之间做选择的动作。 |
| multi-agent architecture | 多智能体架构 | 多角色分工、通信和协调的系统组织方式。 |
| agent-augmented workflow | 智能体增强工作流 | 含规划、路由、评价或角色组件的工作流。 |
| architecture | 架构 | 责任如何在单控制器、层级、专业角色和人机协同间分配。 |
| capability | 能力 / 可用操作 | 系统可提供的规划、工具调用、代码执行、观测、验证、记忆或学习操作。 |
| autonomy level | 自主性等级 | 后续决策实际依赖运行时状态的程度；全文仅用 L1--L5。 |
| evidence | 证据 | 支持行为判断的轨迹、消融、受控失败、验证输出、等预算比较或迁移实验。 |

## L1--L5 自主性等级

| Level | English | 中文 | 最低证据 |
|---|---|---|---|
| L1 | Fixed mapping or pipeline | 固定映射或流水线 | 输出和控制路径由初始条件或预设阶段决定。 |
| L2 | Tool or role assistance | 工具或角色辅助 | 使用工具、模型、角色或规划，但未展示中间证据触发的后续修订。 |
| L3 | Feedback adaptation | 反馈适应 | 中间证据改变后续 prompt、工具、区域、计划、代码或其他动作。 |
| L4 | Long-horizon autonomy | 长程自主 | 持久状态支持动态重新规划、故障恢复、人类权限管理和自适应终止。 |
| L5 | Continual self-improvement | 持续自我改进 | 已完成任务的经验更新可复用行为，并在跨任务留出评估中显示迁移。 |

## 六模块运行架构

| English | 中文 | 输出 |
|---|---|---|
| Goal Understanding, Specification, and Planning | 目标理解、规格构建与规划 | 操作性规格、依赖感知计划、未决假设和检查点。 |
| State Representation and Memory | 状态表征与记忆 | 具有版本、溯源、不确定性和依赖关系的任务状态。 |
| Tool Definition, Selection, and Execution | 工具定义、选择与执行 | 可调用操作、输入输出接口、产物转移、执行日志、错误、成本和可逆性信息。 |
| Perception | 感知 | 对产物、执行过程、环境、参考和交互信号的获取、解释、诊断与验证。 |
| Action | 行动 | 改变产物、环境、可用信息、交互历史或控制轨迹的行动，包括执行、协调、反馈、恢复、继续和停止。 |
| Cross-Task Self-Improvement | 跨任务自我改进 | 受治理的可复用更新及其迁移评估记录。 |

## 迭代、学习与评估

| English | 中文 | 解释 |
|---|---|---|
| candidate iteration | 候选迭代 | 生成或排列多个候选，控制规则保持不变。 |
| feedback iteration | 反馈迭代 | 观测或验证结果改变当前任务的后续输入、工具、状态、计划或修订。 |
| policy iteration | 策略迭代 | 完成的轨迹更新未来任务的技能、检索、验证器、策略或其他行为。 |
| self-correction | 任务内自我修正 | 改变当前创作轨迹的动作。 |
| episodic reuse | 情景复用 | 为后续任务检索既往尝试、修复或经验。 |
| cross-task self-improvement | 跨任务自我改进 | 跨任务更新可复用行为并评估迁移的机制。 |
| test-time adaptation | 测试时适应 | 在当前任务或会话内调整状态、提示、搜索或策略。 |
| artifact-level outcome | 产物层结果 | 最终质量、任务成功、约束满足、可执行性或数据正确性。 |
| trajectory-level process evidence | 轨迹层过程证据 | 状态保持、观测—动作依赖、定位、修复、停止、资源和迁移记录。 |
| process-aware evaluation | 过程感知评估 | 同时评估产物结果和产生结果的轨迹控制行为。 |
| controlled failure | 受控失败 / 控制故障 | 注入已知故障并检验发现、定位和恢复能力。 |
| causal attribution | 因果归因 | 区分模型、采样、算力、人工、验证器和反馈控制的贡献。 |
| matched resource budget | 匹配资源预算 | 对齐生成器、调用次数、样本、时间、token、工具和人工成本后的比较。 |

## 领域与基础模型

| English | 中文 | 解释 |
|---|---|---|
| Agentic Image Generation, Editing, and Restoration | 智能体式图像生成、编辑与修复 | 图像领域章节名称。 |
| Agentic Video, Film, and Animation Generation | 智能体式视频、电影与动画生成 | 视频、电影和动画领域章节名称。 |
| Agentic 3D, CAD, and World Generation | 智能体式 3D、CAD 与世界生成 | 三维、参数化设计和世界构建领域章节名称。 |
| Agentic Scientific Figure and Visualization Generation | 智能体式科学图形与可视化生成 | 数据、科学状态、图形和分析表达领域章节名称。 |
| Agentic Structured Visual Document and Presentation Generation | 智能体式结构化视觉文档与演示文稿生成 | 文档、海报、演示文稿等结构化视觉产物领域章节名称。 |
| Agentic UI and Web Generation | 智能体式 UI 与 Web 生成 | 可执行界面、网页和 Web 应用领域章节名称。 |
| variational autoencoder (VAE) | 变分自编码器 | 使用近似推断学习潜变量分布的生成模型。 |
| generative adversarial network (GAN) | 生成对抗网络 | 通过生成器与判别器对抗训练的生成模型。 |
| autoregressive (AR) model | 自回归模型 | 依次预测像素、视觉 token 或尺度的生成模型。 |
| Visual Autoregressive Modeling (VAR) | 视觉自回归建模（VAR） | 通过 next-scale prediction 从粗到细预测视觉内容的范式。 |
| diffusion and score-based generative models | 扩散模型与基于分数的生成模型 | 同一技术脉络下的密切相关表述；不按“扩散=离散、score=连续”二分。 |
| flow matching / rectified flow | 流匹配 / 校正流 | 学习分布间连续传输路径的生成方法。 |
| consistency model | 一致性模型 | 面向一步或少步采样的生成模型；不等同于 temporal consistency。 |

## 缩写与英文形式

| Term | 规范 |
|---|---|
| AVG | 首次写 `Agentic Visual Generation (AVG)`；后文使用 AVG。 |
| LLM | 首次写 `large language model (LLM)`。 |
| VLM | 首次写 `vision-language model (VLM)`。 |
| LMM | 首次写 `large multimodal model (LMM)`。 |
| LVLM / MLLM | 仅在原论文术语或必须区分时使用；一般叙述优先 VLM 或 LMM。 |
| CAD / UI / API / MCP | 分别首次写 `computer-aided design`、`user interface`、`application programming interface`、`Model Context Protocol`。 |
| 连字符 | 使用 `closed-loop`、`state-dependent`、`tool-augmented`、`feedback-driven`、`long-horizon`、`cross-task`、`process-aware`。 |
| 非穷尽列举 | 英文使用 `and related operations`、`among others`、`and other ...`；中文使用“等”“以及其他相关……”。 |
