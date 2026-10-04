---
tags: [product-management, tier1]
area: Product Management
topic: "AI Product Management - LLM Products, Evals & Economics"
tier: Tier 1
roles: Product Manager
status: complete
subtopics: 13
---
# AI Product Management - LLM Products, Evals & Economics

⬅ [[165 Platform & Marketplace Product Strategy]] · [[_Index - Product Management|Product Management]] · [[167 PRDs, Stakeholder Management & Product Operations]] ➡

> **Area:** Product Management · **Priority:** 🔴 Tier 1 · **Target roles:** Product Manager

## Sub-topics in this note
1. [[#1. The AI Product Lifecycle]]
2. [[#2. When to Use AI vs Rules vs Classic ML]]
3. [[#3. LLM Product Patterns: Chat, RAG, Copilots, Agents]]
4. [[#4. Evaluation I: Offline Evals and Golden Sets]]
5. [[#5. Evaluation II: LLM-as-Judge, Human Review and Online Metrics]]
6. [[#6. Hallucination, Safety and Security Mitigations]]
7. [[#7. Latency, Cost and Quality Trade-offs]]
8. [[#8. Token Economics: A Worked Example]]
9. [[#9. Data Flywheels and Defensibility]]
10. [[#10. Build vs Buy vs Fine-Tune]]
11. [[#11. Prompt Management, Versioning and LLMOps]]
12. [[#12. Responsible AI and Regulation: DPDP Act 2023, IT Rules, EU AI Act]]
13. [[#13. ⭐ Advanced: AI PM Interview Questions and Agent Reliability]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI products now carry legal and unit-cost obligations
> **India notifies the DPDP Rules, 2025 (November 2025).** The Government's press release says the Rules fully operationalise the Digital Personal Data Protection Act, 2023 and give organisations an **18-month phased compliance timeline**. Commencement dates reported for the Act: **13 November 2025** (Data Protection Board provisions), **13 November 2026** (some provisions, reported to include consent managers) and **13 May 2027** (remaining obligations). Data principals can access, correct and erase personal data; breach notification and verifiable parental consent for children's data apply. The Act's Schedule sets maximum penalties of **₹250 crore** (failure of reasonable security safeguards), **₹200 crore** (failure to notify a breach; children's data obligations), **₹150 crore** (significant data fiduciary duties) and ₹50 crore (residual). ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014), [MeitY text of the Act](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf), [Wikipedia timeline](https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Act,_2023))
>
> **India amends IT Rules for AI-generated content (10 February 2026), and hosts the India AI Impact Summit (February 2026).** Per a secondary summary, the amendment requires labelling and metadata for synthetically generated content and tighter takedown procedures for intermediaries; India still has no standalone AI statute. The IndiaAI Mission was approved on 7 March 2024 with an outlay of **₹10,371.92 crore**, including ₹4,563.36 crore for compute. ([Wikipedia: regulation of AI](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence), [Wikipedia: AI in India](https://en.wikipedia.org/wiki/Artificial_intelligence_in_India))
>
> **EU AI Act timeline.** In force 1 August 2024; prohibitions applied from February 2025, general-purpose AI obligations from August 2025, most other obligations from August 2026 and some high-risk obligations from August 2027. Fines reach **€35 million or 7% of worldwide turnover** for prohibited practices. Timelines may be adjusted by later EU measures; check the current position before quoting. Indian products serving EU users are in scope. ([Wikipedia: AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act))
>
> **Token prices and cost levers (Anthropic pricing page, checked October 2026).** Illustrative list prices per million input/output tokens: Claude Sonnet 5.5 **$2 / $10**, Haiku 4.5 **$1 / $5**, Opus 5.5 **$4 / $20**. **Batch** processing is a 50% discount; **prompt-cache reads** cost 0.1× the base input price (5-minute cache writes 1.25×); discounts stack. Prices change often, so any worked example here is a method, not a quote. ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The AI Product Lifecycle
> 🔴 Tier 1 · _Key points:_ Problem framing, feasibility, data, prototype, eval, launch, monitor, iterate

### Definition
AI products differ from deterministic software because output quality is **probabilistic**, depends on **data and models**, and **degrades or shifts** after launch. A usable lifecycle:

| Stage | Key questions | Typical artefacts |
|---|---|---|
| **1. Problem framing** | Is the user problem real and valuable? What is the cost of a wrong answer? | Problem statement, success metric, risk tier |
| **2. Feasibility** | Can a model do this at acceptable quality, cost and latency? Is data available and permitted? | Quick prototype, data audit, DPDP check |
| **3. Prototype and eval design** | What does "good" look like? | Golden set, rubric, baseline (rules or humans) |
| **4. Build** | Prompting, retrieval, tools, guardrails, UX for uncertainty | Prompts, pipelines, fallbacks |
| **5. Offline evaluation** | Does it beat the baseline on key slices? | Eval report, error analysis |
| **6. Limited launch** | Real users, human-in-the-loop, kill switch | Shadow mode, staged rollout |
| **7. Online evaluation** | Does it move product and business metrics? | A/B test, guardrail dashboard |
| **8. Monitor and improve** | Drift, new failure modes, cost | Feedback loops, regression evals, versioned prompts |

Compared with classic product development ([[030 Product Fundamentals & Strategy]], [[037 PM Fundamentals & Lifecycle]]): the PRD needs **acceptance thresholds** and failure-mode handling, the data and eval work is on the critical path, and discovery (see [[164 Product Discovery & User Research]]) includes testing whether users trust and verify AI output. Model quality alone does not equal product quality; **UX design for uncertainty** (citations, edit, undo, escalation) often matters more.

### Example
Support-reply drafting tool for an Indian e-commerce firm. Stage 1: 40% of tickets are "where is my order". Stage 2: order data via API; customer data subject to consent and purpose limits. Stage 3: golden set of 300 historical tickets with agent-approved answers. Stage 6: the tool drafts and the agent clicks "send"; acceptance rate and edit distance are logged. Stage 7: average handle time falls from 6.0 to 4.2 minutes in a randomised comparison. Stage 8: monthly eval re-runs catch a regression when the refund policy changes.

### In the news
See news box. DPDP and the EU AI Act add compliance steps (consent, purpose, breach readiness, risk classification) to stages 1-2 and 8, not just at the end.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would take an LLM feature from idea to launch."

> [!tip] Strong answer includes
> - Starts from user problem and cost of errors, not from the model
> - Defines eval and acceptance thresholds before building
> - Staged launch with human-in-the-loop, kill switch and monitoring
> - Mentions data, privacy and cost as first-class constraints

---

## 2. When to Use AI vs Rules vs Classic ML
> 🔴 Tier 1 · _Key points:_ Simplest tool that works; cost of error; data; explainability; hybrid designs

### Definition
Choose the **simplest approach that meets the need**.

| Approach | Use when | Weakness |
|---|---|---|
| **Rules / deterministic code** | Logic is known, stable, auditable (tax calculation, eligibility, validations) | Brittle to variety; hard to scale to unstructured input |
| **Classic ML (classification, regression, ranking)** | Structured data, abundant labels, need predictions with measurable accuracy (churn, demand, fraud), see [[094 ML Fundamentals & Workflow]], [[100 ML for Product Management]] | Needs labelled data and feature work |
| **LLM / generative AI** | Unstructured language or images; open-ended generation; variety of inputs; limited labelled data | Non-deterministic, costly per call, hallucination, harder to test |
| **Hybrid** | LLM for language understanding, rules for policy and calculation, humans for exceptions | More moving parts |

Decision filter: (1) **Is the output verifiable** cheaply? (2) **What is the cost of a wrong answer** (low: draft text; high: medical or credit decisions)? (3) **Is the task well-defined with a right answer** (use rules or classic ML) or open-ended (LLM)? (4) **Latency and unit cost budget**? (5) **Regulatory or explainability requirements** (see [[220 Responsible AI, Explainability & Model Governance]])? (6) **Do you have data and a baseline to beat**? Prefer **LLM for understanding and drafting; code for computing and deciding** (never ask an LLM to do exact arithmetic or enforce policy when code can).

### Example
Refund eligibility at a retailer: rules decide eligibility from order date, category and delivery status (deterministic, auditable); an LLM reads the customer's free-text message and extracts "item damaged on arrival" into structured fields; the reply is drafted by the LLM but includes the refund amount computed by code. A pure-LLM design would sometimes promise refunds the policy forbids; a pure-rules design could not parse messages like "kapde ka rang alag aaya, wapas karna hai" in Hinglish.

### In the news
See news box. As token prices change, the boundary moves; but regulatory exposure (explainability under sector rules, DPDP data minimisation) pushes high-stakes decisions toward deterministic components.

### Interview angle
> [!question] How it is asked
> "Should we use an LLM for fraud detection on payments?"

> [!tip] Strong answer includes
> - Classic ML (tabular, labelled, low-latency) fits; LLM may help with investigation notes and narrative
> - Cost of false positives and false negatives, latency, explainability and regulators
> - Hybrid design with rules, ML scores and human review
> - A baseline to beat and a measurement plan

---

## 3. LLM Product Patterns: Chat, RAG, Copilots, Agents
> 🔴 Tier 1 · _Key points:_ Prompted features, RAG, copilots, agents/tools, workflow vs agent; UX trade-offs

### Definition
| Pattern | What it is | Good for | Main risks |
|---|---|---|---|
| **Prompted feature / workflow** | Fixed steps calling an LLM (summarise, classify, extract, rewrite) | Predictable, testable tasks | Edge-case inputs |
| **Chat assistant** | Open dialogue with context | Exploration, FAQs | Scope creep, hallucination |
| **RAG (retrieval-augmented generation)** | Retrieve relevant documents (via embeddings, keyword or hybrid search) and give them to the model to answer with citations | Enterprise knowledge, policies, catalogues; fresher or private data | Bad retrieval gives bad answers; stale documents; permissions leakage |
| **Copilot** | AI assists inside a user's workflow (drafts, suggestions) with the user in control | Productivity, high-skill tasks | Over-reliance, automation bias |
| **Agent** | LLM chooses tools/actions in a loop to reach a goal (search, call APIs, write to systems) | Multi-step tasks | Compounding errors, cost, security (prompt injection), harder evals |
| **Fine-tuned / small specialised model** | Model adapted to a domain or format | Tight tasks at scale | Training data, maintenance |

**RAG pipeline:** ingest → chunk → embed and index → retrieve (top-k, rerank) → build prompt → generate with citations → evaluate retrieval and answer separately. Retrieval metrics: **recall@k** (is the relevant chunk in the top k?), **MRR**, **precision@k**; generation metrics: **faithfulness/groundedness** (is every claim supported by the retrieved text?) and answer relevance. See [[219 NLP, Embeddings & LLM Applications for Analysts]]. Technical vocabulary: tokens, context window, temperature, embeddings, tool/function calling, structured outputs; for APIs and integration see [[035 Technical Understanding (APIs, SDLC)]].

Principle: **start with the least autonomous pattern that solves the problem** (workflow before agent) and add autonomy as evals and guardrails mature.

### Example
HR-policy assistant for a 20,000-employee company: RAG over 400 policy PDFs. First version scored recall@5 of 71%: leave-policy answers were wrong because chunks split tables. Fixes: table-aware chunking, adding metadata (policy version and effective date), and reranking: recall@5 rose to 90% and groundedness (human-rated on 200 questions) from 78% to 92%. Permissions: retrieval filters by employee's grade and location, since the policy for contract staff differs.

### In the news
See news box. Obligations under DPDP (purpose limitation, access control, erasure) affect RAG indexes, since personal data in embeddings and logs must also be deletable.

### Interview angle
> [!question] How it is asked
> "How would you design an AI assistant for a bank's customer support?"

> [!tip] Strong answer includes
> - Picks pattern by risk: RAG with citations for FAQs; tools only for read-only actions at first; escalation to a human
> - Separate evaluation of retrieval and generation
> - Guardrails (scope limits, PII handling, refusal) and fallbacks
> - Metrics: resolution, deflection, CSAT, escalation quality, cost per resolved query

---

## 4. Evaluation I: Offline Evals and Golden Sets
> 🔴 Tier 1 · _Key points:_ Eval before build; golden dataset; slices; metrics; regression; confidence intervals

### Definition
An **eval** is a repeatable test of AI quality on representative inputs. **Offline evals** run before release on a fixed dataset. Building blocks:

- **Golden set:** curated inputs with reference outputs or rubrics, drawn from real usage (not invented), covering common cases, **hard cases, adversarial inputs, languages and rare-but-costly scenarios**. Start with 50-100 well-chosen examples, grow to several hundred; version it and keep a held-out part not used for prompt tuning (to avoid overfitting).
- **Rubric:** explicit criteria (correct, grounded, complete, tone, safe, format), scored pass/fail or 1-5 with examples.
- **Metrics by task:** classification and extraction: accuracy, precision, recall, F1 (see [[096 Classification Algorithms]]); retrieval: recall@k, MRR; generation: rubric score, groundedness, citation accuracy; safety: refusal and violation rates; operational: latency, cost per request.
- **Slices:** report by segment (language, intent, customer type); an average can hide a failing slice.
- **Error analysis:** read failures, label them (retrieval miss, wrong tool, policy misread), and fix the largest bucket first.
- **Regression suite:** every production bug becomes a new test; run on every prompt or model change, like unit tests.
- **Statistical care:** on $n$ cases the pass rate has uncertainty $\approx \pm 1.96\sqrt{p(1-p)/n}$ (use Wilson intervals for small $n$, see [[089 Hypothesis Testing]]); to detect a 5-point improvement (85% to 90%) at 5% significance and 80% power you need about **683 cases per variant** for independent samples (paired comparisons on the same cases need fewer).

### Example
Golden set of 200 tickets; the new prompt passes 180 (90%). Wilson 95% interval: **85.1% to 93.4%**. The old prompt passed 170 (85%): intervals overlap, so the evidence of improvement is weak with 200 cases. With 1,000 cases and 900 passes (90%) the interval narrows to **88.0% to 91.7%**. Practical rule: use paired comparison on the same cases and look at which cases flipped, not only the average.

### In the news
See news box. Regulators emphasise documented testing and monitoring for high-risk AI; a versioned eval suite is the evidence trail.

### Interview angle
> [!question] How it is asked
> "How would you evaluate a new LLM feature before launch? How big should your test set be?"

> [!tip] Strong answer includes
> - Golden set from real data with hard cases, slices and a held-out portion
> - Metric choices matched to the task and cost of errors
> - Statistical honesty about confidence intervals and sample size
> - Regression suite and error analysis loop

---

## 5. Evaluation II: LLM-as-Judge, Human Review and Online Metrics
> 🔴 Tier 1 · _Key points:_ Calibrate judges with humans; kappa; A/B tests; guardrail metrics; implicit feedback

### Definition
**LLM-as-judge** uses a model to grade outputs against a rubric; it scales evals but has biases (verbosity, position, self-preference). Calibrate it:

1. Have humans label 100-200 items.
2. Compare judge and humans using agreement and **Cohen's kappa**: $\kappa = \frac{p_o - p_e}{1 - p_e}$, where $p_o$ is observed agreement and $p_e$ agreement expected by chance. Rough reading: below 0.4 weak, 0.4-0.6 moderate, 0.6-0.8 substantial.
3. Fix the rubric, add examples, use pairwise comparisons with order swapped, and re-check periodically.

**Human review:** subject-matter experts for high-stakes content; clear guidelines; double-labelling a sample; budget the reviewer time (cost per labelled item).

**Online evaluation:** after launch measure outcomes. Metrics include **acceptance rate** (suggestions used), **edit distance**, task completion, resolution without escalation, thumbs up/down, retention, revenue per user, plus **guardrail metrics** (complaints, escalations, refunds, latency, cost per task, safety flags). Run randomised **A/B tests** (see [[214 Causal Inference & Experimentation Beyond A-B Tests]], [[092 Sampling & Experimental Design]]); beware novelty effects, non-stationary models, and measuring clicks instead of outcomes. Implicit feedback (copy, regenerate, abandonment) is noisy; explicit feedback has selection bias.

### Example
Judge versus human on 100 answers: both pass 70, human pass/judge fail 10, human fail/judge pass 5, both fail 15. Observed agreement $p_o = (70+15)/100 = 0.85$. Judge says pass for 75, human pass for 80, so $p_e = 0.80 \times 0.75 + 0.20 \times 0.25 = 0.65$. Then $\kappa = (0.85 - 0.65)/(1 - 0.65) = 0.57$: **moderate**, so the judge is acceptable for trend monitoring but not for approving a release without human spot-checks. Note the judge is lenient (5 false passes) which is the riskier direction.

### In the news
See news box. As labelling and transparency rules grow (for example synthetic-content labelling), logging which model and prompt version produced each output becomes an evidence requirement.

### Interview angle
> [!question] How it is asked
> "Can you rely on an LLM to evaluate another LLM? What would you do?"

> [!tip] Strong answer includes
> - Calibrates the judge against human labels with a numeric agreement (kappa), then monitors drift
> - Knows judge biases and mitigations (position swap, rubric, examples)
> - Combines offline evals, human review and online A/B with guardrails
> - Measures outcomes (resolution, retention), not just thumbs

---

## 6. Hallucination, Safety and Security Mitigations
> 🔴 Tier 1 · _Key points:_ Grounding, citations, abstention, guardrails, prompt injection, PII, human-in-the-loop

### Definition
**Hallucination** is a fluent but unsupported or false output. Mitigations form layers:

- **Grounding:** retrieve trusted sources (RAG), require citations, instruct to answer only from context and to say "I don't know".
- **Constrain outputs:** structured output schemas, enumerated choices, tool calls to compute or fetch facts, validation of outputs in code (amounts, IDs, dates).
- **Abstention and thresholds:** route low-confidence or out-of-scope queries to a human or a safe fallback. Choose the threshold on the **cost of errors**: if a wrong answer costs ₹500 and an escalation costs ₹60, abstain when the expected error probability exceeds $60/500 = 12\%$.
- **Verification:** second-pass checking of claims against sources; self-consistency for high-stakes cases.
- **UX design:** show sources, confidence cues, edit/undo, "report a problem"; set user expectations.
- **Human-in-the-loop** for consequential actions (payments, medical, legal).
- **Content safety:** filters on inputs/outputs for harmful content; refusals; red-teaming.
- **Security:** **prompt injection** (malicious text in a web page, document or email instructs the model), data exfiltration and over-privileged tools. Apply least-privilege tool permissions, separate trusted instructions from untrusted content, require confirmation for sensitive actions, sandbox, log. The OWASP Top 10 for LLM Applications lists these threats.
- **Privacy:** minimise and redact personal data sent to models; contractual controls with providers; retention limits; consent and purpose limitation under DPDP.

### Example
Insurance-claims assistant: hallucination rate on a red-team set of 150 adversarial questions was 9.3% (14 cases). After adding "answer only from retrieved policy text with citation" and a code check that quoted clause numbers exist in the document, it fell to 2% (3 cases). Remaining risk is handled by routing to a human whenever no citation is returned. Expected cost: with 1 million queries a month, 2% wrong is 20,000 wrong answers, and at ₹500 each that is ₹1.0 crore a month. Even a 2% rate is expensive at scale, hence the abstain-and-escalate design.

### In the news
See news box. The DPDP Schedule's penalties for security-safeguard failures (₹250 crore) and breach non-notification (₹200 crore) raise the stakes on logging, redaction and incident response for AI features that touch personal data.

### Interview angle
> [!question] How it is asked
> "Your customer-facing bot gave a wrong refund policy and a user complained on social media. What do you do now and later?"

> [!tip] Strong answer includes
> - Immediate: contain (fallback, disable path), fix customer, root-cause
> - Layered mitigations (grounding, validation in code, abstention, human review)
> - A regression test added to the eval suite
> - Quantified error costs and a threshold-based escalation policy

---

## 7. Latency, Cost and Quality Trade-offs
> 🔴 Tier 1 · _Key points:_ Model tiers, routing, caching, batching, context length, streaming; Pareto thinking

### Definition
Every AI feature sits on a **quality-latency-cost** frontier. Levers:

| Lever | Effect |
|---|---|
| **Smaller/faster model** for easy tasks | Lower cost and latency, lower ceiling quality |
| **Model routing / cascades** | Cheap model first, escalate hard cases to stronger model |
| **Prompt caching** | Re-used prefix (system prompt, documents) billed at a fraction (for example 0.1× on cache reads) and faster |
| **Batch APIs** | About 50% discount for non-urgent jobs (overnight summaries, labelling) |
| **Shorter prompts / smarter retrieval** | Fewer input tokens; output tokens are typically priced several times higher than input |
| **Limit output length / structured outputs** | Cuts decode time and cost |
| **Streaming** | Improves perceived latency (time to first token) |
| **Parallel calls / speculative approaches** | Lower end-to-end latency |
| **Fine-tuning or distillation** | Smaller model for a narrow task at lower cost |

Latency ≈ time to first token + output tokens ÷ tokens per second (plus retrieval and tool time). Set **SLOs** per use case: chat answers under 3 seconds to first token, voice under about 1 second, back-office batch hours. Trade-offs must be decided by **value per interaction**: a ₹2 answer is fine for a ₹5,000 insurance claim and not for a free search query.

### Example
Latency for a 350-token answer at 60 tokens a second: 350/60 = **5.8 seconds** of generation, plus 0.6 s to first token = about 6.4 s; streaming makes the first words visible at 0.6 s. At 100 tokens/s the same reply takes 3.5 s (+0.5 s). Cutting the verbose answer to 180 tokens saves about 2.8 s at 60 tokens/s and halves output cost: often a better lever than changing the model.

### In the news
See news box. Published pricing shows the lever sizes: batch halves price and cache reads cost 0.1× of input; models differ by 2-4× in price across tiers.

### Interview angle
> [!question] How it is asked
> "Our AI feature is too slow and too expensive. What would you do?"

> [!tip] Strong answer includes
> - Measure first: tokens in/out, cache hit, p50/p95 latency, cost per task by step
> - Apply levers in order: prompt/retrieval trimming, caching, routing, batching, then model change
> - Evaluate quality after every change on the golden set
> - Tie targets to value per interaction and user tolerance

---

## 8. Token Economics: A Worked Example
> 🔴 Tier 1 · _Key points:_ Cost per request, caching and routing savings, human baseline, error cost, net value

### Definition
Cost per call (USD) with $p_{in}, p_{out}$ in dollars per million tokens:

$$\text{cost} = \frac{T_{in}\, p_{in} + T_{out}\, p_{out}}{10^{6}}$$

Include cached-prefix discounts ($0.1 \times$ for cache reads in the example prices), batch discounts (0.5×), retries, tool-call overheads and **agent loops**, where each step resends the growing context. Then compute **unit economics**: cost per **resolved** task (not per call), vs the human or existing baseline, plus **error cost** and **fixed costs** (engineering, evals, monitoring).

### Example
Support bot, 1,000,000 queries a month. Per query: 3,500 input tokens (800 system prompt + 2,200 retrieved context + 500 history/question) and 350 output tokens. Illustrative prices (Sonnet-tier $2/$10, Haiku-tier $1/$5 per million tokens; ₹88 per US dollar assumed):

| Design | Cost per query | Monthly (USD) |
|---|---|---|
| Sonnet-tier, no caching | (3,500×2 + 350×10)/1e6 = $0.0105 | $10,500 |
| Sonnet-tier, system prompt cached (0.1×) | $0.00906 | $9,060 |
| Haiku-tier, cached | $0.00453 | $4,530 |
| **Routing: 70% Haiku-tier, 30% Sonnet-tier, cached** | 0.7×0.00453 + 0.3×0.00906 = **$0.00589** | **$5,889** |
| Same routing for offline batch jobs (50%) | $0.00294 | $2,944 |

In rupees, routed cost = 0.00589 × 88 ≈ **₹0.52 per query**, about ₹5.2 lakh a month. Business case: a human agent ticket costs about ₹60 (assumption). If the bot resolves 60% of queries, a hallucination error rate of 3% costs ₹500 each (refund, escalation, goodwill). Net saving per query = 0.60 × 60 − 0.52 − 0.03 × 500 = 36 − 0.52 − 15 = **₹20.5**, or about ₹2.05 crore a month for 1 million queries. Notice that **error cost (₹15 per query) dwarfs token cost (₹0.52)**: spend effort on quality and escalation before shaving model price. At 1.5% error (₹7.5 per query) net rises to about ₹28.

Agent loops: an 8-step agent with context growing from 4,000 by 1,500 tokens per step resends 74,000 input tokens in total and generates 8 × 400 = 3,200 output tokens: at $2/$10 that is 0.148 + 0.032 = **$0.18** (about ₹16) per task, around 17 times a single-call design. Cache the prefix, summarise history and cap steps.

### In the news
See news box for the price levers (batch 50%, cache read 0.1×) used above; prices are illustrative and change frequently.

### Interview angle
> [!question] How it is asked
> "Estimate the monthly cost of an LLM assistant with 1 million queries and decide whether it is worth it."

> [!tip] Strong answer includes
> - Tokens in/out per query and prices, with caching and routing levers
> - Compares to the human baseline and includes error costs and fixed costs
> - Cost per resolved task, sensitivity to resolution and error rates
> - Notes price changes and that quality dominates cost

---

## 9. Data Flywheels and Defensibility
> 🔴 Tier 1 · _Key points:_ Usage generates data that improves the product; proprietary data; eval sets; feedback loops

### Definition
A **data flywheel**: more usage creates more data (queries, corrections, outcomes), which improves the model or retrieval, which improves the product, which attracts more usage. Not all AI products have one; many wrap general models and have **no moat** except distribution, workflow integration and proprietary data. Conditions for a real flywheel:

- Feedback is captured **at low friction** (accept/edit/reject; outcome labels like resolved or refunded).
- The data is **proprietary and relevant** (your customers' domain, languages, edge cases), and you have **rights to use it** (consent under DPDP, contracts).
- You turn it into improvements: updated retrieval content, few-shot examples, fine-tuning data, **a growing golden/eval set**, better routing.
- Quality improvement is **visible to users** and measurable.
- It is not defeated by a general model's improvement or by competitors' similar data.

Related: **data network effects** in [[165 Platform & Marketplace Product Strategy]] and model improvement from labelled data in [[094 ML Fundamentals & Workflow]]. Risks: feedback loops that reinforce bias, **model collapse** from training on AI-generated data, privacy and consent, and low-quality signals (thumbs-ups from lazy users).

### Example
A Hindi/English voice-based loan-collection assistant logs the outcome of every call (promise to pay, kept or broken). Each month the team (a) adds 500 hard transcripts to the eval set, (b) updates objection-handling examples, (c) fine-tunes a small model on approved transcripts with consent. Promise-kept rate rises from 41% to 52% over 6 months in the A/B test; competitors without call outcome data cannot reproduce it. The moat is the **outcome-labelled data and workflow**, not the base model.

### In the news
See news box. DPDP consent and purpose limitation define what feedback and call data can legitimately be reused for training or evaluation.

### Interview angle
> [!question] How it is asked
> "What is the moat of an AI startup built on top of a foundation model?"

> [!tip] Strong answer includes
> - Moat candidates: proprietary outcome data, workflow integration, distribution, trust/compliance, domain evals
> - Describes the specific feedback loop and rights to the data
> - Notes that base-model upgrades commoditise thin wrappers
> - Metrics showing improvement from the loop

---

## 10. Build vs Buy vs Fine-Tune
> 🔴 Tier 1 · _Key points:_ API vs open-weight self-host; prompting → RAG → fine-tune ladder; TCO; sovereignty and privacy

### Definition
Decide along two axes: **where the model runs** and **how it is adapted**.

**Adaptation ladder** (try in order): **prompting** → **few-shot examples** → **RAG** (adds knowledge) → **tool use** → **fine-tuning** (changes behaviour, style, format; cheaper small models on narrow tasks) → **pre-training** (almost never justified). Fine-tuning does not reliably add facts; RAG is better for changing knowledge.

| Option | Pros | Cons | Fits |
|---|---|---|---|
| **Buy / API from a frontier provider** | Best quality, fastest start, no infra | Per-token cost, vendor dependency, data-sharing and residency questions | Most v1 products |
| **Buy a packaged AI product** | Zero build | Limited differentiation | Commodity workflows |
| **Self-host open-weight model** | Control, privacy, cost at high volume, customisation | GPUs, MLOps, security patching, usually lower quality ceiling | High volume, sensitive data, offline use |
| **Fine-tune** | Domain style, lower latency/cost via small models | Data, eval and retraining effort | Stable narrow tasks at scale |
| **Sovereign / local models** | Language and data-locality fit (see IndiaAI Mission) | Maturity varies | Public sector, regulated, Indic languages |

Break-even logic: self-hosting wins when **fixed cost < API spend** and you have capability to operate it. Total cost of ownership includes engineers, GPUs, monitoring, evals and upgrade cycles. Keep an **abstraction layer** to switch models, and re-run evals on every model change (vendors deprecate models).

### Example
API cost for the support bot is $5,889 a month (previous sub-topic). Self-hosting assumption: 2 GPUs at $2.5 an hour × 730 hours = $3,650 plus engineering and monitoring of $4,000 a month = **$7,650**, which is higher than the API bill, and likely a lower quality model. Self-hosting only wins if volume is about 1.3× higher or if data residency forces it (7,650 / 5,889 = 1.30). Decision: start with the API, keep prompts and evals portable, revisit when volume or regulation changes.

### In the news
See news box. IndiaAI Mission funding (₹10,371.92 crore, including ₹4,563.36 crore for compute) and the DPDP phase-in make local compute and data governance a live buy-vs-build question for Indian enterprises.

### Interview angle
> [!question] How it is asked
> "Would you use an API or fine-tune your own model for a legal-document review product?"

> [!tip] Strong answer includes
> - The adaptation ladder (prompt, RAG, fine-tune) and the evidence needed to climb it
> - TCO and break-even with volume assumptions
> - Privacy, residency, vendor risk and switching cost
> - Eval-driven decision, not preference

---

## 11. Prompt Management, Versioning and LLMOps
> 🟠 Tier 2 · _Key points:_ Prompts as code; versioning; eval gates; observability; model upgrades; cost monitoring

### Definition
In an LLM product the **prompt, retrieval config, model choice, tools and guardrails are the software**. Good practice:

- **Version everything:** prompts, system messages, retrieval parameters, model IDs, tool schemas, eval datasets. Tag each production response with versions for traceability.
- **Change control:** review prompts like code; run the eval suite on every change; **gate releases** on thresholds (for example no slice below 85% pass, no increase in unsafe rate).
- **Environments and rollouts:** dev → staging → canary → full; feature flags; shadow mode; quick rollback.
- **Observability:** trace each request (inputs, retrieved docs, tool calls, outputs, tokens, latency, cost); sample for human review; alert on drift, cost spikes, refusal-rate changes.
- **Model upgrades and deprecations:** vendors retire models; plan migrations with side-by-side evals; avoid prompts tuned to quirks.
- **Separation of concerns:** keep policy and business rules in code or configuration, not hidden in prompts.
- **Documentation:** model cards / system cards, known limitations, owner and review dates (see [[220 Responsible AI, Explainability & Model Governance]]).
- **Security hygiene:** secrets, access control for prompt edits, logs with PII minimised.

### Example
A prompt change shortens refund explanations. The eval run shows overall pass rate up from 91% to 92%, but the "Hindi/Hinglish" slice drops from 88% to 79% (n = 60). Release gate (no slice more than 3 points lower) blocks the change; the prompt is revised to include Hinglish examples, re-tested at 90% on that slice, then canaried to 5% of traffic for 48 hours with cost and escalation guardrails.

### In the news
See news box. Compliance regimes (DPDP breach duties, EU AI Act documentation) reward teams that can show which version produced which output.

### Interview angle
> [!question] How it is asked
> "How do you make sure a prompt tweak does not break the product?"

> [!tip] Strong answer includes
> - Prompts under version control with owners and review
> - Automated eval gates including slices
> - Canary rollout and observability with rollback
> - Planning for model deprecation and regression tests

---

## 12. Responsible AI and Regulation: DPDP Act 2023, IT Rules, EU AI Act
> 🔴 Tier 1 · _Key points:_ Consent, purpose limitation, breach notification, children, fairness, transparency, risk tiers

### Definition
**Responsible AI** principles: fairness, transparency/explainability, privacy, safety, accountability and human oversight (see [[220 Responsible AI, Explainability & Model Governance]]). PM obligations by regime:

**India: DPDP Act 2023 and DPDP Rules 2025**
- Roles: **Data Principal** (individual), **Data Fiduciary** (decides purpose and means; your company), **Data Processor**, **Significant Data Fiduciary** (extra duties such as DPO, audits, impact assessment).
- **Consent** must be free, specific, informed, unambiguous, with a clear notice, and withdrawable; certain legitimate uses exist without consent. **Purpose limitation and data minimisation**; **accuracy**; **reasonable security safeguards**; **breach notification** to the Board and affected persons; **erasure** when purpose is served or consent withdrawn; **children** (under 18) need verifiable parental consent and tracking/targeted advertising to children is restricted; grievance redressal; rights to access and correct.
- **Penalties** up to ₹250 crore (security safeguards), ₹200 crore (breach notice; children), ₹150 crore (significant fiduciary duties).
- **Phasing:** Board provisions from 13 Nov 2025; some provisions from 13 Nov 2026; most obligations from 13 May 2027 (as reported for the 18-month schedule).
- AI implications: lawful basis and notice for using personal data in prompts, logs, RAG indexes and training; deletion across vector stores and logs; vendor/processor contracts; cross-border handling per notifications.

**India: IT Rules amendment (Feb 2026)** on synthetically generated content: labelling and metadata; platforms' takedown duties (as summarised in secondary sources, verify text). **Sector regulators** (RBI, SEBI, IRDAI, ICMR for health) issue AI guidance for their regulated entities.

**EU AI Act** for products serving EU users: risk tiers (unacceptable, high, limited, minimal) plus general-purpose AI obligations; high-risk use cases include employment, credit, education and essential services; fines up to €35 million or 7% of turnover.

**Practical PM checklist:** data map and lawful basis → DPIA or risk assessment for sensitive uses → bias testing on slices → human oversight for consequential decisions → disclosure that users interact with AI → logging, retention and deletion → incident response.

### Example
A recruiting-screening tool for an Indian staffing firm ranks CVs using an LLM. Risks: bias by gender, region or college tier; automated decisions affecting livelihoods; personal data of 50,000 applicants. Controls: remove protected attributes and proxies, test pass rates by group (flag if a group's selection rate is below 80% of the highest group: the "four-fifths" heuristic from US employment practice), keep humans making final decisions, log reasons, notify applicants, retain data only for the stated period, and allow erasure. If the same tool were offered in the EU it would likely be **high-risk** under the AI Act (employment).

### In the news
See news box for the DPDP Rules and timeline, penalties, the IT Rules amendment and the EU Act dates.

### Interview angle
> [!question] How it is asked
> "What would you do differently when building an AI feature that uses customer data under India's DPDP Act?"

> [!tip] Strong answer includes
> - Roles (fiduciary, processor), consent and purpose limitation, minimisation, breach notification
> - Deletion across logs, indexes and training sets; vendor contracts
> - Penalty magnitude and phased timeline stated with care
> - Fairness testing and human oversight for consequential decisions

---

## 13. ⭐ Advanced: AI PM Interview Questions and Agent Reliability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Typical AI PM interview prompts** and what the evaluator looks for:

| Prompt | What is being tested |
|---|---|
| "Design an AI feature for X" | Problem choice, AI vs rules, pattern, eval and rollout |
| "How do you decide if an AI feature is good enough to launch?" | Thresholds, slices, human review, guardrails, staged rollout |
| "Hallucination in production: what now?" | Incident handling, layered mitigation, regression tests |
| "Estimate the cost of AI feature Y" | Token maths, levers, unit economics |
| "Build vs buy vs fine-tune?" | Adaptation ladder, TCO, risk |
| "How do you measure success of a copilot?" | Acceptance, edit rate, outcome metrics, causal testing |
| "Is this a good use of AI?" | Cost of error, verifiability, data, baseline |
| "Trade-offs of agents" | Autonomy, reliability, permissions, cost |

**Agent reliability:** per-step success compounds. If each step succeeds with probability $p$, an $n$-step task succeeds with probability $p^n$: with $p = 0.95$ and $n = 8$, $0.95^8 = 0.66$; with $p = 0.99$, $0.99^8 = 0.92$. So: shorten chains, add checkpoints and verification, constrain tools, ask for confirmation on irreversible actions, use idempotent operations and design clear **stop conditions**. Evaluate agents on **task success, steps, cost, time, tool-call correctness and safety violations** across a scenario suite, with trajectory review of failures. Protocols for exposing tools (for example MCP, the Model Context Protocol) make integration easier but widen the **prompt-injection and permission surface**, so treat tool outputs as untrusted. Interview frame: **Users → Problem → Pattern → Quality bar → Risks → Metrics → Rollout → Economics** (see [[163 PM Interview Types & Answer Frameworks]] and [[167 PRDs, Stakeholder Management & Product Operations]] for documenting this in a PRD).

### Example
Answer outline for "Design an AI assistant for kirana owners to reorder stock via WhatsApp": users (small shop owners, Hindi/regional voice), problem (stock-outs, 3 phone calls per order), pattern (workflow with LLM parsing orders into structured cart; rules for credit limits and pricing; human fallback via salesman), quality bar (95% line-item accuracy on a 300-order golden set including Hinglish and voice notes; 100% price correctness via code), risks (misheard quantities, wrong SKU, data privacy under DPDP), metrics (orders per week, order error rate, time to order, repeat rate, cost per order under ₹3), rollout (50 shops in one city, shadow mode, then 10% traffic), economics (token cost per order about ₹0.5-1 vs savings from fewer calls).

### In the news
See news box. Regulation (DPDP, EU AI Act) and price levers turn up as constraints in nearly every AI PM case.

### Interview angle
> [!question] How it is asked
> "Would you give an AI agent permission to issue refunds up to ₹5,000 without human approval?"

> [!tip] Strong answer includes
> - Quantifies error probability compounding and the cost of a wrong refund
> - Starts with human approval above a small limit, expands as evals prove reliability
> - Controls: scoped permissions, audit logs, fraud checks in code, kill switch
> - Success metric and a staged expansion plan
