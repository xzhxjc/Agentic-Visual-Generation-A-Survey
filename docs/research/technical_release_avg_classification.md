# 技术报告与模型发布的 AVG 属性核查

核查日期：2026-08-24。本报告采用论文对智能体式视觉生成（Agentic Visual Generation, AVG）的行为定义：系统围绕视觉产物的创作过程保留可访问的任务相关状态，并且原始来源能够证明运行时观测、验证结果或执行结果改变了后续创作动作。模型名称、内部多步采样、工具 API、带有 “Agent” 的产品名称，以及用户多轮输入，都不能单独证明该条件。

本报告判断的是 `technical_reports_and_model_releases_inventory.md` 所记录**一手来源中的证据**，不判断某个模型未来能否被另一个闭环系统用作生成器、编辑器或执行器。

| 标签 | 判定标准 |
|---|---|
| **明确具有 AVG 式闭环能力** | 一手来源明确说明：可识别的决策过程根据运行时观测、验证、执行结果或留存状态，改变后续视觉创作动作。这里的结论针对发布的产品/API 工作流，不表示模型的每一次调用都会自动运行完整闭环。 |
| **明确不属于 AVG** | 一手来源描述的是生成器、编辑器、表征模型、固定语法/运行时或单次产品操作，且没有任务级的“观测—后续动作”决策过程。 |
| **现有来源无法判定** | 产品可能含多步辅助、代码执行或“Agent”品牌，但当前记录的一手来源没有给出足以判定 AVG 的轨迹级证据。 |

## 核查结果

| 分类 | 条目数 | 结论 |
|---|---:|---|
| 明确具有 AVG 式闭环能力 | 5 | Nano Banana 2/Pro/旧版 Nano Banana 的 Gemini 图像 API 工作流、GPT Image 2 的 Responses API 图像工具工作流、ChatGPT Advanced Data Analysis / OpenAI Code Interpreter 的迭代代码执行工作流，以及 Bolt.new 的自动测试、重构和迭代工作流，均有官方页面对运行时工具/执行结果与后续动作的明确描述。 |
| 明确不属于 AVG | 115 | 这些条目是视觉生成器、编辑器、表征模型、世界模拟器、固定可视化语法或运行时，可作为 AVG 的基础模型或执行接口。 |
| 现有来源无法判定 | 15 | 这些产品可能支持智能体工作流，但当前产品页未清楚记录运行时证据如何改变后续视觉创作决策。 |

## 明确不属于 AVG 的条目

- **图像生成、编辑与修复中的 41 项**：图像表格中的 43 项里，除 Nano Banana 2/Pro/旧版 Nano Banana 的 Gemini API 工作流和 GPT Image 2 的 Responses API 工作流外，其余 41 项明确不属于 AVG。其来源描述图像生成、条件控制、编辑、个性化或可调用 API。扩散模型和自回归模型内部的迭代采样不构成任务级后续动作选择；Nano Banana 2 Lite 和单次 GPT Image Image API 调用也归入此类。
- **视频、电影与动画的全部 31 项**：Video GAN 至 Veo 3。其来源描述视频合成、动画、编辑、模型控制或发布可用性。动作条件化的视频/世界模型在不自行选择下一项创作动作时仍属于生成器。
- **3D、CAD 与世界生成的全部 26 项**：3D-GAN 至 GameNGen。其来源描述三维表征、重建、资产生成、CAD 序列生成或生成式环境预测。除非独立系统论文说明闭环控制器，论文中应将它们作为生成器或执行环境处理。
- **科学图形与可视化中的 5 项**：Vega、Vega-Lite、Data2Vis、NL4DV、Chart-to-Text。它们是图形语法、方法或分析/生成模型；引用的报告没有描述控制器根据运行时证据修订后续视觉动作。
- **跨领域与统一多模态模型的全部 10 项**：Unified-IO、CM3leon、GPT-4o、Chameleon、Emu3、Show-o、Janus、OmniGen、Transfusion、Janus-Pro。统一模型可以产生或解释视觉 token，但模型报告本身没有建立 AVG 创作轨迹。

## 明确具有 AVG 式闭环能力的条目

| 领域 | 条目 | 一手证据与边界 |
|---|---|---|
| 图像生成与编辑 | Nano Banana 2 / Nano Banana Pro / 旧版 Nano Banana（Gemini 图像 API） | Google API 文档明确支持多轮连续图像编辑，并将多轮对话作为图像迭代方式；文档还给出 `google_search` 工具参与图像生成交互的示例，说明外部检索结果可以进入后续图像生成。Nano Banana 2 Lite 的同一文档明确说明其不针对多轮连续编辑，因此不共享该标签。 |
| 图像生成与编辑 | GPT Image 系列（当前文档列出 `gpt-image-2`）/ Responses API 的 `image_generation` 工具工作流 | OpenAI 图像生成文档正式列出 `gpt-image-2`，并明确说明 Responses API 支持对话和多步流程、内置图像生成工具、上下文中的图像输入输出以及多轮高保真编辑。该标签针对 Responses API 工作流；工具自身使用独立的 GPT Image 模型选择，单次 Image API 调用仍是生成器操作。 |
| 科学可视化 | ChatGPT Advanced Data Analysis / OpenAI Assistants Code Interpreter | OpenAI Code Interpreter 文档明确说明模型可写代码并运行；代码失败时继续改写和运行直到成功，并可生成图表图像。该标签针对代码执行与图表生成工作流，不表示每个数据分析请求都需要多轮修复。 |
| UI 与 Web 生成 | Bolt.new | 官方产品页明确写出 Bolt 会自动测试、重构和迭代，以减少错误。该执行结果驱动后续代码/应用修改，符合本综述的观测—动作依赖；其证据针对应用生成工作流，不代表 Bolt 的每个操作都包含视觉验证。 |

## 现有来源无法判定的条目

以下产品在功能上可能参与智能体工作流。现有来源不足以将它们作为 AVG 案例引用，后续需要系统卡、详细产品文档、执行轨迹或技术报告。

| 领域 | 条目 | 当前证据缺口 |
|---|---|---|
| 科学可视化 | Gemini in Looker / Google Cloud Conversational Analytics | 当前来源说明了自然语言分析/可视化能力，未说明运行时结果怎样改变后续视觉创作决策。ChatGPT Advanced Data Analysis 与 OpenAI Assistants Code Interpreter 已移入“明确具有 AVG 式闭环能力”。 |
| 文档与演示 | Canva Magic Design；Microsoft Designer；Microsoft 365 Copilot；Gamma；Tome；Gemini for Google Workspace；Adobe Firefly Boards | 记录的页面证明了创作或编辑功能，没有说明同一视觉创作轨迹中的持久任务状态及其证据条件化后续动作。 |
| UI 与 Web | v0；Replit Agent；Lovable；WebSim；Claude Artifacts；Figma Make；Stitch | v0 官方产品页明确使用 “Agentic by default”，并说明会规划、创建任务和连接数据库，但当前页面没有给出运行时证据改变后续视觉创作动作的轨迹。Figma Make 官方页支持动态数据与交互测试、实时反馈，仍未说明系统自主依据这些结果改变动作。Replit Agent 的产品页说明了环境配置、依赖安装和代码执行，仍未给出满足 AVG 判据的轨迹。pix2code 与 Screenshot-to-code 是截图到代码生成，归为明确不属于 AVG；Bolt.new 已移入“明确具有 AVG 式闭环能力”。 |

## 对论文的使用规则

1. 将“明确不属于 AVG”的条目用于第二章或领域章节的生成器、表征与执行接口背景。
2. 在找到合适的一手系统来源前，不将“现有来源无法判定”的 15 项作为规划、验证、恢复、记忆、跨任务自我改进或 L3--L5 自主性等级的证据。
3. 新条目只有在一手来源中能定位到演化中的产物/任务状态、运行时证据、发生变化的后续动作，以及四者之间的联系时，才能标为“明确具有 AVG 式闭环能力”。
4. 领域章节关于智能体机制和自主性等级的论断继续以系统论文为主要依据，不以模型发布公告替代系统证据。
