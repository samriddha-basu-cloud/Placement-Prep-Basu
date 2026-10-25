---
tags: [machine-learning, tier1, ai]
area: Machine Learning
topic: "Generative AI & LLM Foundations for Managers"
tier: Tier 1
roles: All roles
status: complete
subtopics: 12
---
# Generative AI & LLM Foundations for Managers

⬅ [[220 Responsible AI, Explainability & Model Governance]] · [[_Index - Machine Learning|Machine Learning]] · [[229 Agentic AI & Intelligent Automation in Operations]] ➡

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** All roles (Consulting, PM, Operations, Project)

**Why this note exists:** in 2025-26 almost every MBA interview panel asks at least one AI question, and most of them are not technical: "How does ChatGPT actually work?", "Will AI replace planners?", "Where would you use GenAI in our company?". This note gives the manager-level mental model; [[219 NLP, Embeddings & LLM Applications for Analysts]] goes into the analyst-level mechanics and [[166 AI Product Management - LLM Products, Evals & Economics]] into the product lens.

## Sub-topics in this note
1. [[#1. AI, ML, Deep Learning and Generative AI: Getting the Vocabulary Right]]
2. [[#2. How a Large Language Model Works: Next-Token Prediction]]
3. [[#3. Tokens, Context Windows and Why They Matter Commercially]]
4. [[#4. How LLMs Are Built: Pre-training, Fine-tuning and Alignment]]
5. [[#5. Reasoning Models and Test-Time Compute]]
6. [[#6. Multimodal Models: Text, Images, Audio, Video and Documents]]
7. [[#7. Sampling, Temperature and Why Answers Vary]]
8. [[#8. Hallucination: Why It Happens and How Businesses Control It]]
9. [[#9. Closed vs Open-Weight Models, and the Model Landscape]]
10. [[#10. Where GenAI Creates Value: The Task-Fit Test]]
11. [[#11. Cost Arithmetic: Pricing a GenAI Use Case]]
12. [[#12. ⭐ Advanced: Explaining GenAI to a CXO in Two Minutes]]

## 📰 News box
> [!news] Shared news hook for this topic (2025–2026): adoption is broad, value is concentrated (checked 25 October 2026)
> **Use is near-universal; scaled value is rare.** McKinsey's *State of AI 2025* (5 Nov 2025) found 88% of organisations use AI in at least one function (78% a year earlier), but only about one-third have begun scaling AI across the enterprise, 39% report any EBIT impact (mostly under 5%), and about 6% qualify as "AI high performers" attributing at least 5% of EBIT to AI. ([McKinsey](https://www.mckinsey.com/featured-insights/artificial-intelligence/the-state-of-ai-2025))
>
> **The "GenAI divide".** MIT NANDA's *The GenAI Divide: State of AI in Business 2025* (based on 150 leader interviews, a 350-employee survey and 300 public deployments) reported that about 95% of corporate GenAI pilots stall without measurable P&L impact; purchased tools succeeded about two-thirds of the time versus about one-third for internal builds, and back-office automation beat sales and marketing for returns. ([Computing](https://computing.co.uk/news/2025/ai/mit-report-95pc-corporate-generative-ai-pilots-fail))
>
> **India builds its own models.** At the India AI Impact Summit (concluded 20 Feb 2026, New Delhi Declaration endorsed by 88 countries and organisations), Sarvam AI showed 30B and 105B-parameter models and BharatGen (IIT Bombay-led) a 17B mixture-of-experts model covering all 22 scheduled languages. ([All India Radio](https://www.newsonair.gov.in/india-ai-impact-summit-2026-adopts-new-delhi-declaration); [Free Press Journal](https://www.freepressjournal.in/amp/tech/ai-summit-2026-meet-the-3-sovereign-ai-llm-models-that-were-unveiled-in-delhi-to-rival-global-tech-giants))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. AI, ML, Deep Learning and Generative AI: Getting the Vocabulary Right
> 🔴 Tier 1 · _Key points:_ Nested sets; predictive vs generative; foundation model; LLM is one kind of GenAI

### Definition
- **Artificial intelligence (AI):** any system that performs tasks we associate with human intelligence (perceiving, deciding, predicting, generating). Includes rules engines and optimisation solvers.
- **Machine learning (ML):** AI that learns patterns from data instead of hand-written rules ([[094 ML Fundamentals & Workflow]]).
- **Deep learning:** ML using multi-layer neural networks ([[101 Deep Learning Basics]]); dominant for images, speech and text.
- **Generative AI (GenAI):** deep-learning models that **produce new content** (text, code, images, audio) rather than only a label or a number.
- **Foundation model:** a very large model trained on broad data that can be adapted to many tasks. **Large language models (LLMs)** are foundation models for text (and increasingly images and audio).

| Type | Output | Typical business use | Example |
|---|---|---|---|
| Predictive ML | number / class / score | forecast, churn, fraud, credit | XGBoost demand forecast |
| Optimisation (OR) | best decision under constraints | routing, scheduling, network design | LP for production mix ([[146 Operations Research - Linear Programming]]) |
| Generative AI | text, code, image, summary | drafting, extraction, search, assistants | LLM summarising supplier contracts |
| Agentic AI | actions across tools | multi-step workflows | agent that chases late POs ([[229 Agentic AI & Intelligent Automation in Operations]]) |

### Example
A tyre company (think of a CEAT-type plant) uses all four: a predictive model forecasts replacement-tyre demand by district, an LP decides the production mix across plants, a GenAI assistant drafts dealer communications and summarises quality complaints, and an agent reconciles transporter invoices against trip data. Saying "we will use AI" without naming which type is the classic weak answer.

### In the news
See news box. Most of the 88% "AI use" in surveys is GenAI assistants; most of the measurable EBIT still comes from classic predictive and optimisation models.

### Interview angle
> [!question] How it is asked
> "What is the difference between AI, ML and generative AI?" or "Is a demand forecast AI?"

> [!tip] Strong answer includes
> - The nested definition in one line each, then the predictive vs generative distinction
> - One operations example of each
> - The point that optimisation and rules are still the backbone of operations decisions; GenAI sits on top of them

---
## 2. How a Large Language Model Works: Next-Token Prediction
> 🔴 Tier 1 · _Key points:_ Predicts the next token; transformer with attention; parameters; emergent abilities from scale

### Definition
An LLM is trained to **predict the next token** (a word piece) given all previous tokens. Repeated token by token, this produces fluent text. The architecture is the **transformer** (2017), whose **attention** mechanism lets each token weigh every other token in the context, so the model can track who "it" refers to across a long document.

Key terms:
- **Parameters (weights):** the learned numbers; modern models have billions to trillions. More parameters plus more data plus more compute generally gives better models (**scaling laws**).
- **Training vs inference:** training builds the model once at very high cost; **inference** is each use of the model, paid per token.
- **Emergent capability:** skills such as translation, coding or arithmetic that are not explicitly programmed but appear with scale.
- **Knowledge cutoff:** the model knows only what was in its training data unless given documents or a search tool at run time.

The manager's mental model: an LLM is a **very well-read autocomplete that has compressed patterns of language, facts and reasoning**. It is not a database lookup and not a calculator, which explains both its strengths (flexible language, reasoning over messy text) and its weaknesses (confident errors, arithmetic slips).

### Example
Prompt: "The supplier missed the delivery date, so the plant had to …". The model assigns probabilities to candidate next tokens, for instance "stop" 0.31, "expedite" 0.22, "reschedule" 0.18, "use" 0.09, and so on, picks one (see sampling, sub-topic 7), appends it and repeats. Ask it "What is 4,837 × 2,961?" and it may produce a plausible but wrong number because it predicts digits rather than computing them; modern assistants avoid this by calling a calculator or code tool.

### In the news
See news box. The sovereign models shown at the Delhi summit are the same architecture trained with far more Indian-language data, which is why tokenisation and language coverage were their selling points.

### Interview angle
> [!question] How it is asked
> "Explain how ChatGPT works to a non-technical plant head."

> [!tip] Strong answer includes
> - Next-token prediction learned from huge text, in plain words
> - Why that makes it good at language and summarising but unreliable on exact facts and arithmetic
> - What companies do about it: give it documents (RAG), tools (calculator, database) and human review

---
## 3. Tokens, Context Windows and Why They Matter Commercially
> 🔴 Tier 1 · _Key points:_ ~0.75 English words per token; Indic scripts cost more tokens; context window = working memory; price is per token

### Definition
- **Token:** the unit the model reads and writes. Rule of thumb for English: 1 token ≈ 0.75 words, so 1,000 words ≈ 1,333 tokens. Hindi, Tamil or Bengali text has historically taken several times more tokens per word on global tokenisers, which raises cost and latency; Indian models advertise better Indic tokenisation for this reason.
- **Context window:** the maximum number of tokens (prompt plus response) the model can consider at once. Windows have grown from a few thousand tokens to hundreds of thousands or more. A 200,000-token window holds roughly 150,000 words, about 500 pages.
- **Input vs output tokens:** priced separately; output is usually several times dearer per token.
- **Latency:** time to first token plus generation speed; long outputs are slow.

Commercial consequences: long contracts can be read whole; but stuffing everything into the context is expensive and can dilute attention, so systems retrieve only relevant passages (RAG, [[219 NLP, Embeddings & LLM Applications for Analysts]]).

### Example
A procurement team wants every one of 400 supplier contracts (average 12,000 words) checked for a force-majeure clause. Tokens per contract ≈ 12,000 / 0.75 = 16,000. Total input ≈ 6.4 million tokens. Every contract fits comfortably in one call, so no chunking is needed; the cost driver is input tokens (worked cost in sub-topic 11).

### In the news
See news box. Language coverage and token efficiency for Indian languages were explicit design goals of the Sarvam and BharatGen models.

### Interview angle
> [!question] How it is asked
> "Why does an AI vendor charge per token, and what drives the bill?"

> [!tip] Strong answer includes
> - Token definition and the 0.75-words rule
> - Bill = volume × (input tokens × input price + output tokens × output price)
> - Levers: shorter prompts, retrieval instead of full documents, smaller models for easy steps, batching and caching

---
## 4. How LLMs Are Built: Pre-training, Fine-tuning and Alignment
> 🟠 Tier 2 · _Key points:_ Pre-training on web-scale text; supervised fine-tuning; preference training (RLHF); system prompts; enterprise fine-tuning is rarely the first step

### Definition
1. **Pre-training:** next-token prediction on trillions of tokens of text and code; costs tens to hundreds of millions of dollars of compute for frontier models. Output: a **base model** that continues text but does not follow instructions well.
2. **Supervised fine-tuning (SFT):** training on curated instruction-response pairs so the model behaves as an assistant.
3. **Preference alignment:** **RLHF** (reinforcement learning from human feedback) or related methods train the model towards answers humans rate as more helpful, honest and harmless. Some labs use written principles and AI feedback as well.
4. **Deployment layer:** a **system prompt** (instructions from the deploying company), safety filters and tools.

For enterprises the adaptation ladder is: **prompting → retrieval (RAG) → fine-tuning → training your own model**, in rising cost and falling frequency. Most business value comes from the first two ([[166 AI Product Management - LLM Products, Evals & Economics]], sub-topic 10).

### Example
An FMCG company wants a chatbot that answers distributors' scheme queries. Fine-tuning on last year's schemes would bake in stale information; RAG over the live scheme circulars is cheaper, auditable (it can cite the circular) and updated by simply replacing documents. Fine-tuning would make sense only for a stable style or format, such as always producing a specific claim-note template.

### In the news
See news box. India's IndiaAI Mission funds pre-training of domestic foundation models because pre-training is the step that needs subsidised GPU capacity ([[231 AI Industry Landscape, Economics & India AI Ecosystem]]).

### Interview angle
> [!question] How it is asked
> "Should we fine-tune our own model on company data?"

> [!tip] Strong answer includes
> - The adaptation ladder and its cost order
> - Fine-tune for stable style/format or narrow high-volume tasks; RAG for changing knowledge
> - Data rights, privacy and evaluation before any training

---
## 5. Reasoning Models and Test-Time Compute
> 🟠 Tier 2 · _Key points:_ Model "thinks" before answering; better at maths, planning, code; slower and costlier; choose per task

### Definition
**Reasoning models** spend extra computation at answer time ("test-time compute"), generating intermediate reasoning steps before the final answer. Since late 2024 this has become the main way frontier labs improve maths, coding, planning and multi-step analysis. Trade-off: more tokens, more latency and higher cost per answer, so a router often sends simple questions to a fast model and hard ones to a reasoning model.

Manager's rule: **match the model to the task**: classification, extraction and short drafting → small fast model; multi-step analysis, planning, code → reasoning model; critical numbers → always tool-computed and human-checked.

### Example
Task: "Given this 40-line bill of materials and lead times, which components are on the critical path for the November build?" A fast model may list plausible items; a reasoning model works through the dependencies and is far more likely to be right, at perhaps 5 to 20 times the tokens. For 50 such questions a week the extra cost is trivial relative to a planner's time; for 5 million customer-support classifications a month it is not.

### In the news
See news box. Reasoning ability is one reason agent projects moved from demos to pilots in 2025-26 ([[229 Agentic AI & Intelligent Automation in Operations]]).

### Interview angle
> [!question] How it is asked
> "Would you use the most powerful model for everything?"

> [!tip] Strong answer includes
> - No: cost, latency and diminishing returns on easy tasks
> - Routing by task difficulty, with evaluation to prove the cheap model is good enough
> - Accuracy target set by the business consequence of an error

---
## 6. Multimodal Models: Text, Images, Audio, Video and Documents
> 🟠 Tier 2 · _Key points:_ Reads images/PDFs/charts; speech in and out; image and video generation; operations uses in inspection and documents

### Definition
**Multimodal** models take and/or produce more than text: images, scanned documents, charts, audio, video. Main business uses:
- **Document understanding:** invoices, e-way bills, bills of lading, handwritten delivery challans, without template-based OCR ([[219 NLP, Embeddings & LLM Applications for Analysts]], sub-topic 8).
- **Visual inspection and site audits:** describe defects in a photo, check 5S compliance from shop-floor images; dedicated computer-vision models remain better for high-speed line inspection ([[099 ML for Operations & SCM]]).
- **Voice:** speech-to-text and text-to-speech in Indian languages for call centres, field sales and farmer advisory.
- **Generation:** product images, ad creatives, training videos.

### Example
A 3PL receives 3,000 proof-of-delivery photos a day. A multimodal model reads the consignee signature box, stamp and date, flags missing or illegible ones (say 4%, i.e. 120 per day) for human follow-up, and posts the rest to the TMS. Billing cycles shorten because invoices no longer wait for manual POD checks ([[125 Transportation Management Deep Dive]]).

### In the news
See news box. Gnani.ai's voice models at the Delhi summit (speech in 12 Indian languages) show where Indian demand is: voice-first, multilingual interfaces.

### Interview angle
> [!question] How it is asked
> "Give a non-chatbot use of GenAI in logistics or manufacturing."

> [!tip] Strong answer includes
> - Document or image use case with a volume number
> - Human review of exceptions and a measurable KPI (cycle time, error rate, DSO)
> - Integration point (TMS, ERP), not just the model

---
## 7. Sampling, Temperature and Why Answers Vary
> 🟡 Tier 3 · _Key points:_ Probabilistic output; temperature controls randomness; low for extraction, higher for ideation; reproducibility

### Definition
Because the model outputs a probability distribution over the next token, the system **samples** from it. **Temperature** scales randomness: near 0 the model almost always picks the most likely token (consistent, conservative); higher values give more varied, creative text and more risk of errors. Other knobs: top-p (sample only from the most likely tokens covering probability p), maximum output length, stop sequences, and **structured output** (forcing JSON matching a schema).

Business rule: extraction, classification and calculations → low temperature plus structured output; brainstorming, naming, ad copy → higher temperature with human selection.

### Example
Using the sub-topic 2 probabilities ("stop" 0.31, "expedite" 0.22, "reschedule" 0.18…), temperature near 0 always continues with "stop"; at a higher temperature the model will sometimes write "expedite" or "reschedule". For an invoice-extraction pipeline you want the same answer every time; for 20 tagline ideas for a cold-chain brand you want variety.

### In the news
See news box. Reproducibility matters for audit: regulated users log prompts, settings and model versions ([[220 Responsible AI, Explainability & Model Governance]]).

### Interview angle
> [!question] How it is asked
> "Why did the AI give my colleague a different answer to the same question?"

> [!tip] Strong answer includes
> - Probabilistic generation and temperature in one sentence
> - Differences in prompt, context, model version or tools
> - For business processes: fix settings, use templates, structured outputs and evaluations

---
## 8. Hallucination: Why It Happens and How Businesses Control It
> 🔴 Tier 1 · _Key points:_ Fluent but false; caused by next-token objective and missing knowledge; controls: grounding, citations, tools, abstention, human review

### Definition
A **hallucination** is a fluent, confident output that is false or unsupported. Causes: the model optimises plausibility, not truth; the fact is missing or rare in training data; the question is ambiguous; or the model is pushed to answer when it should abstain. Controls, in order of impact:
1. **Grounding:** supply the source documents (RAG) and instruct "answer only from these; say 'not found' otherwise".
2. **Citations:** require the source passage for each claim; check that it exists.
3. **Tools:** calculator, database query, search; never let the model "remember" a price or a stock level.
4. **Constrained outputs:** schemas, allowed values, validation rules.
5. **Evaluation:** golden test sets, groundedness scoring ([[166 AI Product Management - LLM Products, Evals & Economics]]).
6. **Human-in-the-loop** where the error cost is high, and clear accountability (Air Canada ruling, [[220 Responsible AI, Explainability & Model Governance]]).

### Example
A supplier-onboarding assistant is asked "What is the payment term for vendor V-1023?" Ungrounded, it may say "45 days" because that is common. Grounded with a tool that reads the vendor master from SAP (field ZTERM, see [[080 SAP MM — Materials Management]]), it returns "Z030: 30 days net" with the source field. The fix is architectural, not a better prompt.

### In the news
See news box. The MIT NANDA study attributes failed pilots mainly to tools that do not fit workflows and do not learn from feedback, rather than model quality; ungrounded answers are a big part of why users stop trusting a pilot.

### Interview angle
> [!question] How it is asked
> "How would you stop an AI assistant giving wrong answers to customers?"

> [!tip] Strong answer includes
> - Grounding, citations, tools, abstention, then human review by risk tier
> - A metric (groundedness or error rate on a test set) and a launch threshold
> - Escalation path and accountability; the company owns what its bot says

---
## 9. Closed vs Open-Weight Models, and the Model Landscape
> 🟠 Tier 2 · _Key points:_ API-only frontier models vs downloadable weights; trade-offs in capability, cost, control, data residency

### Definition
- **Closed (proprietary) models:** accessed through an API or app; weights not released. Typically the most capable; vendor handles scaling and safety; data handling governed by contract.
- **Open-weight models:** weights downloadable (licence terms vary); can run on your own cloud or on-premise, fine-tune freely, keep data in India; you carry hosting, security and evaluation effort.
- **Small language models (SLMs):** a few billion parameters; run cheaply, even on laptops or edge devices; good for narrow tasks.

| Criterion | Closed API | Open-weight self-hosted |
|---|---|---|
| Capability at the frontier | usually higher | close behind, gap varies by task |
| Time to start | hours | weeks |
| Data residency / control | contract-based | full |
| Cost at low volume | low (pay per use) | high (idle GPUs) |
| Cost at very high volume | can be high | can be lower |
| Customisation | prompting, some fine-tuning | full |

Main providers to name (status changes fast, re-check before interviews): US frontier labs (OpenAI, Anthropic, Google DeepMind), Meta and Mistral (open-weight families), Chinese labs (DeepSeek, Alibaba's Qwen), and Indian efforts (Sarvam AI, BharatGen). See [[231 AI Industry Landscape, Economics & India AI Ecosystem]].

### Example
A public-sector bank wants an internal policy assistant. Constraints: customer data must stay in India and under its control. Option A: a closed model through a cloud region in India with contractual no-training terms. Option B: an open-weight model on its own GPUs. If query volume is modest (say 20,000 a day), A is faster and cheaper; B makes sense if regulators require on-premise processing or volume becomes very large.

### In the news
See news box. Sarvam released its 30B and 105B models under the Apache 2.0 licence (March 2026), adding Indian open-weight options. ([Open Source For You](https://www.opensourceforu.com/2026/03/sarvam-releases-30b-and-105b-llms-under-apache-2-0/))

### Interview angle
> [!question] How it is asked
> "Open-source or proprietary AI for a bank / hospital / defence PSU?"

> [!tip] Strong answer includes
> - Criteria first (capability needed, data residency, volume, skills, cost), then the choice
> - Hybrid answer is usually right: closed for low-risk productivity, open/self-hosted for sensitive data
> - Exit plan: avoid lock-in with an abstraction layer and portable evaluations

---
## 10. Where GenAI Creates Value: The Task-Fit Test
> 🔴 Tier 1 · _Key points:_ Language-heavy, high-volume, error-tolerant or verifiable tasks; augment before automate; five-question screen

### Definition
A quick **task-fit test** for any proposed GenAI use case:
1. **Is the work language or document heavy?** (emails, contracts, tickets, reports, code)
2. **Is it high volume and repetitive?** (value scales with volume)
3. **Is the output verifiable or the error tolerable?** (a human or a rule can check it; or mistakes are cheap)
4. **Is the data accessible and permitted?** (DPDP, confidentiality, systems access)
5. **Is there a workflow owner who will change the process?** (adoption is the real constraint)

Pattern library: **draft** (emails, reports), **summarise** (calls, meetings, complaints), **extract** (fields from documents), **classify/route** (tickets, spend categories), **search/answer** (policies, SOPs), **code** (SQL, Python, Excel formulas), **converse** (customer and employee assistants), **act** (agents). Bad fits: exact numerical optimisation (use OR), safety-critical decisions without verification, tasks with tiny volume.

### Example
Scoring three ideas for an auto-component maker, 1 to 5 on each test (higher is better):

| Use case | Language | Volume | Verifiable | Data | Owner | Total |
|---|---|---|---|---|---|---|
| 8D report drafting from complaint data ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]) | 5 | 3 | 4 | 4 | 4 | **20** |
| Spend classification of 2 lakh PO lines ([[122 Spend Analysis, Savings & Procurement Maturity]]) | 4 | 5 | 4 | 5 | 4 | **22** |
| AI deciding weekly production plan | 1 | 2 | 2 | 3 | 2 | **10** |

Spend classification goes first; production planning stays with optimisation plus planners.

### In the news
See news box. The MIT study's finding that back-office automation beats sales and marketing for returns is consistent with this test: high volume, verifiable, workflow-owned tasks.

### Interview angle
> [!question] How it is asked
> "Where would you use GenAI in our supply chain?"

> [!tip] Strong answer includes
> - Two or three specific use cases scored on clear criteria, not a list of buzzwords
> - A KPI per use case and a pilot plan
> - Saying where you would **not** use GenAI shows judgement

---
## 11. Cost Arithmetic: Pricing a GenAI Use Case
> 🔴 Tier 1 · _Key points:_ Tokens × price × volume; batch and caching discounts; compare with human cost; model cost is usually the small line

### Definition
$$\text{Monthly model cost} = N \times \left(\frac{T_{in}\,P_{in} + T_{out}\,P_{out}}{10^6}\right)$$
where $N$ = number of requests, $T$ = tokens per request, $P$ = price per million tokens. Add retrieval/search costs, hosting, monitoring, human review time and change management. Discounts: batch processing (often about 50% off for non-urgent work) and prompt caching for repeated context. Current list prices are in the news box of [[219 NLP, Embeddings & LLM Applications for Analysts]]; treat them as snapshots.

### Example
Extract 12 fields from **10,000 invoices a month**, 1,500 input tokens and 200 output tokens each, on a mid-tier model priced at \$2 input and \$10 output per million tokens:
- Input: 10,000 × 1,500 = 15 M tokens × \$2 = **\$30**
- Output: 10,000 × 200 = 2 M tokens × \$10 = **\$20**
- Total **\$50/month**; with a 50% batch discount **\$25**. At about ₹96 per dollar, ₹4,800 a month, roughly **₹0.48 per invoice**.

Compare: a data-entry associate processing 400 invoices a day costs far more per invoice than this. The model bill is rarely the constraint; **accuracy, exception handling and integration** are. Budget the human review of the 5 to 10% exceptions and the ERP integration project instead.

### In the news
See news box. Falling per-token prices are why the economics shifted from "is it affordable?" to "will the workflow actually change?".

### Interview angle
> [!question] How it is asked
> "Estimate the cost of using an LLM to process all our invoices." (often as a mini-guesstimate)

> [!tip] Strong answer includes
> - The formula, explicit assumptions (volume, tokens, price) and the arithmetic
> - Comparison with the current cost per transaction
> - The real cost drivers: review, integration, monitoring, change management

---
## 12. ⭐ Advanced: Explaining GenAI to a CXO in Two Minutes
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A structure for executive-level AI questions (also usable in GDs, [[177 Group Discussions & Extempore for MBA Placements]]):
1. **What it is** (one sentence): "A model that has learned language patterns from enormous text, so it can read, write and reason over documents, but it does not know your data unless connected to it, and it can be confidently wrong."
2. **Where it pays** (two examples from their industry, with numbers).
3. **What it needs**: clean data access, workflow redesign, people who own adoption, guardrails.
4. **What it costs**: small model bill, larger integration and change cost.
5. **Risks**: errors, data leakage, regulation (DPDP, EU AI Act), vendor lock-in.
6. **How to start**: two or three pilots with baselines and kill criteria, then scale what works ([[230 AI Strategy, Use-Case Prioritisation & ROI]]).

### Example
"For your FMCG distribution network, I would start with two things: classifying and auto-answering distributor claim queries, about 30,000 a month today handled by eight people, and summarising secondary-sales anomalies for area managers every Monday. Both are text-heavy, high-volume and easy to verify. The model cost would be a few thousand rupees a month; the work is connecting the DMS and claims system and redesigning the claim desk. I would run eight-week pilots with turnaround time and first-contact resolution as the metrics, and stop if accuracy on the test set is below 95%."

### In the news
See news box. With only about 6% of firms capturing large EBIT gains, interviewers reward candidates who sound like the 6%: specific, measured and workflow-focused.

### Interview angle
> [!question] How it is asked
> "Our CEO keeps hearing about GenAI. What should we actually do?"

> [!tip] Strong answer includes
> - Plain-language definition with its limits
> - Industry-specific use cases with volumes and a KPI
> - Pilot plan, costs, risks and a stop rule
