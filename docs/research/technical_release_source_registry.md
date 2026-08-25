# Official Source Registry for the Technical-Release Audit

This registry identifies the first-party archives that must be searched before claiming coverage of a release family.  It is a reproducibility aid for the inventory; it does not turn a vendor's product catalogue into academic evidence.

| Release family | First-party archive or model hub | What to capture |
|---|---|---|
| OpenAI image and video | https://openai.com/news/ ; https://platform.openai.com/docs/models | Exact API ID, announcement date, capability, availability |
| Google Gemini, Imagen and Veo | https://blog.google/technology/ai/ ; https://deepmind.google/models/ ; https://ai.google.dev/gemini-api/docs | Model identifier, model-card or API documentation, release channel |
| Meta visual and multimodal models | https://ai.meta.com/research/publications/ ; https://ai.meta.com/blog/ | Report version, code/weight availability, explicitly described modalities |
| Adobe Firefly | https://news.adobe.com/ ; https://www.adobe.com/products/firefly.html | Product/model family, date, supported creation operation |
| Stability AI | https://stability.ai/news ; https://github.com/Stability-AI | Report, repository tag, weights/license state |
| Black Forest Labs | https://blackforestlabs.ai/ | Exact FLUX version and deployment/weights status |
| Runway | https://runwayml.com/research/ | Exact Gen version and documented input/output operations |
| Luma AI | https://lumalabs.ai/ ; https://lumalabs.ai/blog | Model name, date, supported controls |
| Tencent Hunyuan | https://github.com/Tencent-Hunyuan | Paper/repository correspondence and version tag |
| Alibaba Qwen/Wan | https://github.com/QwenLM ; https://github.com/Wan-Video | Model-card/repository release and paper correspondence |
| Microsoft Research / product releases | https://www.microsoft.com/en-us/research/ ; https://blogs.microsoft.com/ | Research release versus Microsoft 365 feature |
| Figma, Vercel, Replit, Canva, Google Labs | Official engineering/product blogs and product documentation | Product release date, build/deploy capability, evidence that visual artifact creation is in scope |

## Per-entry evidence checklist

1. Save the publisher URL and the date on which it was checked.
2. Record the formal title and model identifier exactly as the publisher gives it.
3. Record one capability sentence that the source explicitly states.  Do not infer planning, verification, memory, autonomy, or tool use.
4. Record whether the source is a technical report, model card/repository, API documentation, or user-facing product announcement.
5. When a paper has a stable publisher record, add its Bib entry separately and rerun duplicate-key and undefined-citation checks.
6. Mark retired pages, renamed endpoints, and informal nicknames in Notes instead of silently replacing earlier release names.
