---
tags: [machine-learning, tier2, ai, current-affairs]
area: Machine Learning
topic: "AI Industry Landscape, Economics & India AI Ecosystem"
tier: Tier 2
roles: Consulting / PM / All roles (GD and current affairs)
status: complete
subtopics: 12
---
# AI Industry Landscape, Economics & India AI Ecosystem

⬅ [[230 AI Strategy, Use-Case Prioritisation & ROI]] · [[_Index - Machine Learning|Machine Learning]] · [[232 AI Productivity Toolkit for MBA Work - Excel, SQL, Decks & Research]] ➡

> **Area:** Machine Learning · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / PM / All roles (GD and current affairs)

**Use this note for:** GD topics ("Is AI a bubble?", "Will AI kill Indian IT jobs?"), current-affairs questions, consulting cases on tech, semiconductors or data centres, and "Why this company?" answers for tech recruiters. Figures are dated; re-check anything market-related before an interview ([[180 Current Affairs & Economy Briefing for MBA Interviews (2025-26)]]).

## Sub-topics in this note
1. [[#1. The AI Value Chain: Chips to Applications]]
2. [[#2. Chips and Compute: GPUs, Custom Silicon, Foundries and Memory]]
3. [[#3. Hyperscalers and the Capex Race]]
4. [[#4. Model Labs and Their Business Models]]
5. [[#5. China, Open Models and the DeepSeek Shock]]
6. [[#6. The Application Layer and What Happens to SaaS]]
7. [[#7. Energy, Data Centres and Physical Supply Chains]]
8. [[#8. India's AI Policy Stack: IndiaAI Mission, Governance Guidelines, Summit]]
9. [[#9. Big Tech Investment in India and the Data-Centre Build-out]]
10. [[#10. Indian IT Services and GCCs in the AI Era]]
11. [[#11. AI and Jobs: The Evidence and a Balanced View]]
12. [[#12. ⭐ Advanced: "Is AI a Bubble?" A Two-Sided GD Brief]]

## 📰 News box
> [!news] Shared news hook for this topic (2025–2026): record capex, India's sovereign push, and an IT-services reset
> **Hyperscaler capex 2026 ≈ \$730 billion.** Latest guidance (July 2026): Amazon about \$220 billion, Alphabet \$195-205 billion, Microsoft roughly \$175 billion (calendar 2026, incl. finance leases), Meta \$130-145 billion; combined 2025 spend was about \$410 billion. ([Analysis Atlas](https://analysis-atlas.com/research/hyperscaler-ai-capex-2026/))
>
> **India.** MeitY released the **India AI Governance Guidelines** on 5 Nov 2025 (seven principles, no new AI law for now, existing laws to be strengthened) ([AZB & Partners](https://www.azbpartners.com/bank/meity-releases-india-ai-governance-guidelines-with-deliberate-focus-on-enabling-innovation-over-restraint/)). The **IndiaAI Mission** (₹10,372 crore) had over 38,000 GPUs on its compute portal by March 2026 ([TelecomTalk](https://telecomtalk.info/?p=1005751)). The **AI Impact Summit** (concluded 20 Feb 2026) produced the New Delhi Declaration, endorsed by 88 countries and organisations ([All India Radio](https://www.newsonair.gov.in/india-ai-impact-summit-2026-adopts-new-delhi-declaration)).
>
> **Big Tech bets on India (Dec 2025):** Amazon over \$35 billion by 2030, Microsoft \$17.5 billion over 2026-29, Google \$15 billion for an AI hub and data-centre campus in Visakhapatnam with AdaniConneX and Airtel; \$67.5 billion in total. ([IANS](https://ianslive.in/amazon-microsoft-google-bet-big-on-india-with-massive-675-billion-investments--20251210143735))
>
> **IT services reset:** the five largest IT firms' combined headcount fell by 7,389 in FY26 (gain of 12,718 in FY25); TCS announced about 12,000 job cuts and plans about 25,000 fresher hires in FY27, down from 40,000-42,000 earlier. ([IANS](https://ianslive.in/top-it-firms-hiring-turns-negative-as-headcount-falls-over-7000-in-fy26--20260425104000))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The AI Value Chain: Chips to Applications
> 🔴 Tier 1 · _Key points:_ Six layers; profits concentrated at chips and cloud today; Porter-style analysis

### Definition
| Layer | What it does | Example players (2026) | Economics |
|---|---|---|---|
| 1. Semiconductor equipment and foundry | lithography, manufacturing | ASML, TSMC, Samsung | extreme scale and entry barriers |
| 2. Chips and memory | GPUs, accelerators, high-bandwidth memory | Nvidia, AMD, Broadcom (custom chips), SK hynix, Micron | currently the highest margins |
| 3. Cloud and data centres | rent compute, run models | AWS, Microsoft Azure, Google Cloud, Oracle, CoreWeave; Indian DC operators | very high capex, utility-like returns |
| 4. Foundation models | train and serve frontier models | OpenAI, Anthropic, Google DeepMind, Meta, xAI, Mistral, DeepSeek, Alibaba Qwen; Sarvam, BharatGen (India) | huge training cost, falling price per token |
| 5. Platforms and tools | MLOps, vector databases, agent frameworks, data platforms | Databricks, Snowflake, open-source tools | competitive, consolidating |
| 6. Applications and services | AI features in software, AI-native apps, consulting and IT services | Microsoft 365 Copilot, Salesforce, start-ups; Accenture, TCS, Infosys | value capture still being decided |

Porter's five forces ([[023 Business Fundamentals & Strategy]]) at each layer explain where profits sit: chips have few substitutes and high switching costs; models face intense rivalry and falling prices; applications face low entry barriers but can own customer relationships and data.

### Example
Follow one rupee of enterprise AI spend on a copilot licence: part goes to the software vendor (application), which pays a model provider per token, which pays a cloud provider for GPU hours, which bought the GPUs from a chip designer, who paid a foundry. Today, in this chain, the chip and cloud layers report the most visible profits, while many application and model companies are still loss-making.

### In the news
See news box. The \$730 billion of hyperscaler capex flows mostly into layers 1-3.

### Interview angle
> [!question] How it is asked
> "Who makes money in AI?" or a GD on "AI's winners and losers".

> [!tip] Strong answer includes
> - The layered value chain in a sentence each
> - Where profits sit now and why (scarcity, switching costs)
> - How that could shift (custom chips, cheaper models, application lock-in)

---
## 2. Chips and Compute: GPUs, Custom Silicon, Foundries and Memory
> 🟠 Tier 2 · _Key points:_ GPUs dominate training; custom ASICs rising for inference; TSMC and HBM bottlenecks; export controls

### Definition
- **GPU (graphics processing unit):** parallel processors ideal for neural-network maths; Nvidia leads, helped by its CUDA software ecosystem (a switching cost).
- **Custom accelerators (ASICs):** Google TPU, Amazon Trainium/Inferentia, Microsoft and Meta in-house chips, often designed with Broadcom or Marvell; aim to cut cost and dependence on Nvidia, especially for inference.
- **Foundry:** TSMC manufactures most leading-edge AI chips; advanced packaging capacity has been a bottleneck.
- **High-bandwidth memory (HBM):** stacked memory beside the GPU; supplied by SK hynix, Samsung, Micron; often a constraint.
- **Geopolitics:** US export controls limit advanced chips to China; India is building fabrication and assembly capacity under its semiconductor mission ([[134 Electronics & Semiconductor Supply Chain]], [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]).

### Example
Supply-chain lens: an AI server needs GPUs (TSMC), HBM (Korea), networking (switches, optical modules), power equipment and cooling. Lead times on any one component can delay a data centre by quarters, a classic bottleneck/theory-of-constraints problem ([[017 Process Management & Optimization]]).

### In the news
See news box. Microsoft noted a \$25 billion component-price impact within its April 2026 capex guidance, a sign of memory and component inflation.

### Interview angle
> [!question] How it is asked
> "Why is Nvidia so valuable?" or "Can India become a semiconductor hub?"

> [!tip] Strong answer includes
> - Hardware plus software ecosystem as the moat
> - Supply bottlenecks (foundry, packaging, memory) and geopolitics
> - India's realistic entry points: assembly, testing, packaging, design talent

---
## 3. Hyperscalers and the Capex Race
> 🔴 Tier 1 · _Key points:_ ~\$730 bn in 2026; depreciation and return questions; capacity as competitive weapon

### Definition
**Hyperscalers** are the largest cloud providers (Amazon, Microsoft, Google) plus Meta for its own use. They are spending record amounts on AI data centres because they believe demand for AI compute will keep rising and because capacity is a competitive weapon. Investor questions: will revenue grow fast enough to earn a return on this capex; how long will GPUs stay economically useful (depreciation life); and is demand real or circular (vendors investing in customers who buy their products).

Useful arithmetic: capex intensity = capex / revenue; payback depends on utilisation and price per GPU-hour, which falls as supply grows.

### Example
Rough return check: \$730 billion of annual capex, if depreciated over about 5 years, implies roughly \$146 billion of annual depreciation across the four firms. To earn, say, a 10% return on the cumulative investment, AI-related revenue must grow by hundreds of billions of dollars a year within a few years. This is the core of the bubble debate (sub-topic 12).

### In the news
See news box. Guidance rose through 2026 (Alphabet from \$175-185 billion in February to \$195-205 billion in July; Amazon from about \$200 billion to \$220 billion).

### Interview angle
> [!question] How it is asked
> "Is the AI capex boom sustainable?"

> [!tip] Strong answer includes
> - Scale of spending with a date
> - The return logic (depreciation, utilisation, pricing)
> - Both sides: real usage growth vs overbuild risk

---
## 4. Model Labs and Their Business Models
> 🟠 Tier 2 · _Key points:_ Consumer subscriptions, enterprise licences, API per token, cloud partnerships; falling prices, rising usage

### Definition
Revenue models for foundation-model companies:
1. **Consumer subscriptions** (monthly plans for chat assistants).
2. **Enterprise and team plans** (per seat, with admin and data controls).
3. **API usage** (per million tokens), sold directly and through clouds.
4. **Partnerships and distribution** (models embedded in office suites, phones, ERP).
5. **Open-weight releases** (strategic: ecosystem, talent, standard-setting) monetised indirectly.

Dynamics: **price per unit of capability falls quickly**, so volume must grow faster; training costs rise with each frontier generation; differentiation shifts to reliability, tools, agents, enterprise trust and distribution. Unit economics of AI products are in [[166 AI Product Management - LLM Products, Evals & Economics]].

### Example
If token prices for a given capability fall 50% a year while a company's token volume grows 4×, revenue still doubles (0.5 × 4 = 2). If volume grows only 1.5×, revenue falls 25% (0.5 × 1.5 = 0.75). Price elasticity of demand decides the outcome ([[236 Economics Essentials - Micro, Macro & Policy for Interviews]]).

### In the news
See news box. The donation of MCP to a neutral foundation (Dec 2025) shows labs competing on ecosystems and standards as well as models ([[229 Agentic AI & Intelligent Automation in Operations]]).

### Interview angle
> [!question] How it is asked
> "How do AI companies make money?" (PM and consulting)

> [!tip] Strong answer includes
> - The revenue streams
> - The falling-price, rising-volume dynamic with numbers
> - Where differentiation is moving

---
## 5. China, Open Models and the DeepSeek Shock
> 🟠 Tier 2 · _Key points:_ Efficient open models narrow the gap; 27 Jan 2025 market shock; export controls; implications for buyers

### Definition
Chinese labs (DeepSeek, Alibaba's Qwen, others) released strong **open-weight** models trained with notable efficiency despite restricted access to top chips. Implications: (1) capability gaps can close fast; (2) cheap open models put pressure on prices; (3) enterprises gain options but must weigh data-security and regulatory concerns about model origin; (4) export-control policy is contested.

### Example
**27 January 2025:** after DeepSeek's R1 reasoning model drew attention for performing well at low reported cost, Nvidia's shares fell 17% in a day, a loss of about \$560 billion of market value, and the Nasdaq fell 3%. ([YourStory](https://yourstory.com/2025/01/nvidia-560b-loss-deepseek-ai-disruption-tech-news)) The market later recovered as investors concluded that cheaper AI could raise total demand for compute (a Jevons-paradox argument: efficiency gains increase total use).

### In the news
See news box. Open-weight releases from India (Sarvam under Apache 2.0, BharatGen's Param2) are part of the same open-model trend.

### Interview angle
> [!question] How it is asked
> "What did DeepSeek teach us?" or "Should Indian firms use Chinese open models?"

> [!tip] Strong answer includes
> - Efficiency shock, price pressure and the Jevons argument
> - Risk lens: data security, regulation, supply of updates
> - Recommendation by use case, with evaluation and governance

---
## 6. The Application Layer and What Happens to SaaS
> 🟠 Tier 2 · _Key points:_ AI-native apps vs incumbents adding AI; per-seat pricing under pressure; outcome-based pricing

### Definition
Enterprise software (SaaS) firms are embedding copilots and agents; AI-native start-ups attack specific workflows (legal drafting, customer support, coding). Pricing is shifting from **per seat** (fewer seats needed if AI does the work) to **usage** or **outcome-based** pricing (per resolved ticket, per processed invoice). Incumbent advantages: distribution, data, workflow integration and trust; AI-native advantages: speed and design built around AI.

### Example
A support-software vendor charging ₹6,000 per agent-seat per month sells to a company with 100 agents: ₹6 lakh/month. If AI resolves 60% of tickets and the customer cuts to 50 agents, revenue halves under seat pricing. Switching to ₹40 per AI-resolved ticket on 30,000 resolved tickets yields ₹12 lakh/month, so the vendor's revenue rises while the customer's total cost (₹3 lakh seats + ₹12 lakh = ₹15 lakh) may still be below the old cost of 100 human agents plus seats. Pricing redesign decides who captures the value ([[160 Case Interview - Cost Reduction, Turnaround & Pricing]]).

### In the news
See news box. Microsoft's Agent Mode in Excel became generally available in early 2026 on web and Windows, with a choice of OpenAI and Anthropic models, an example of incumbents embedding agents in core apps. ([SumProduct](https://sumproduct.com/news/agent-mode-in-excel-is-now-generally-available-on-the-desktop/))

### Interview angle
> [!question] How it is asked
> PM: "How should a SaaS company price its AI features?"

> [!tip] Strong answer includes
> - Seat cannibalisation logic with numbers
> - Usage/outcome pricing options and their risks (predictability for buyers)
> - Value-based pricing anchored on customer savings

---
## 7. Energy, Data Centres and Physical Supply Chains
> 🟠 Tier 2 · _Key points:_ Power is the binding constraint; cooling and water; long-lead equipment; India's renewable advantage

### Definition
AI data centres need large, reliable power (hundreds of megawatts per campus), cooling (increasingly liquid cooling), water, land, fibre connectivity and long-lead equipment (transformers, switchgear, gensets, chillers). Constraints have shifted from chips to **power and grid connections** in many markets. Operations relevance: data-centre construction is a large project-management and EPC market ([[168 Project Procurement, Contracts & EPC Delivery]]); power purchase agreements and renewables matter for cost and sustainability ([[014 Global SCM & Sustainability]]).

### Example
Rule-of-thumb sizing: a 100 MW IT-load campus with a power usage effectiveness (PUE) of 1.3 draws 130 MW. Running all year: 130 MW × 8,760 h ≈ 1.14 billion kWh (1.14 TWh). At ₹6 per kWh that is about ₹683 crore of electricity a year (1.14 billion kWh × ₹6), for one campus, which is why tariffs, renewable PPAs and PUE are central to data-centre economics.

### In the news
See news box. Google's Visakhapatnam campus is planned around clean energy and new subsea cable landings, linking AI to India's energy transition ([[180 Current Affairs & Economy Briefing for MBA Interviews (2025-26)]], sub-topic 11).

### Interview angle
> [!question] How it is asked
> Guesstimate or case: "Size the electricity demand of India's data centres" or "Where should a data centre be located?"

> [!tip] Strong answer includes
> - Capacity × PUE × hours, with stated assumptions
> - Location factors: power cost and reliability, renewables, water, fibre, land, incentives, latency
> - Link to facility-location methods ([[113 Network Design & Facility Location Modelling]])

---
## 8. India's AI Policy Stack: IndiaAI Mission, Governance Guidelines, Summit
> 🔴 Tier 1 · _Key points:_ ₹10,372 crore mission; compute, datasets, foundation models, skills; principles-based governance; DPDP for data

### Definition
- **IndiaAI Mission (approved 2024, ₹10,372 crore):** pillars include subsidised compute (GPU portal), IndiaAI datasets platform, foundation models, application development, skills (IndiaAI FutureSkills), start-up financing and safe and trusted AI.
- **India AI Governance Guidelines (MeitY, 5 Nov 2025):** seven principles: Trust; People First; Innovation over Restraint; Fairness and Equity; Accountability; Understandable by Design; Safety, Resilience and Sustainability. The approach relies on **existing laws** (IT Act, DPDP Act, consumer protection, sectoral regulators) rather than a new AI law, with new institutions (an AI Governance Group and expert committees) and an action plan.
- **Data protection:** DPDP Act 2023 and DPDP Rules notified 14 Nov 2025 with phased timelines ([[220 Responsible AI, Explainability & Model Governance]]).
- **AI Impact Summit (Feb 2026):** New Delhi Declaration (88 endorsers) with "People, Planet, Progress" and seven pillars of cooperation; a voluntary charter for the democratic diffusion of AI.

Contrast: the **EU AI Act** is a risk-tiered binding law; the US relies largely on sector rules and executive policy; India chose principles plus existing law. Good GD comparison.

### Example
A start-up building a Hindi voice agent for farmer advisory could use IndiaAI compute at subsidised rates, train on IndiaAI datasets, must follow DPDP consent rules for farmers' voice data, and would be judged against the governance principles (people first, understandable by design) if it partners with government programmes.

### In the news
See news box. Over 38,000 GPUs were on the compute portal by March 2026; the mission had approved 190 projects across government, start-ups, MSMEs and academia.

### Interview angle
> [!question] How it is asked
> "Should India regulate AI like the EU?" (GD favourite)

> [!tip] Strong answer includes
> - India's principles-plus-existing-law approach vs EU risk-tier law
> - Trade-off: innovation and speed vs certainty and protection
> - A balanced view: sectoral rules for high-risk uses (credit, health), light touch elsewhere

---
## 9. Big Tech Investment in India and the Data-Centre Build-out
> 🟠 Tier 2 · _Key points:_ \$67.5 bn announced Dec 2025; why India; what it means for jobs, power and supply chains

### Definition
Why global firms invest in Indian AI infrastructure: large and fast-growing digital user base, data-localisation and sovereignty preferences, renewable-energy potential, engineering talent, government incentives, and India as a hub for South Asia, the Middle East and Africa. Second-order effects: demand for power, construction, electrical equipment, cooling, fibre, and skilled operations staff; state competition for projects (Andhra Pradesh, Tamil Nadu, Maharashtra, Telangana, Uttar Pradesh).

### Example
Consulting-style question: "Which Indian sectors benefit from \$67.5 billion of AI infrastructure investment?" Structure by layer: construction and EPC (civil, electrical), power (renewables, transmission, storage), electrical equipment (transformers, switchgear, cables), cooling and HVAC, real estate (land, industrial parks), telecom (fibre, subsea landing stations), and services (facility management, security). Then pick two with numbers and constraints (transformer lead times; grid connection approvals).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "What does Google's Vizag AI hub mean for India?"

> [!tip] Strong answer includes
> - Facts with dates (amount, partners, location)
> - Direct and indirect economic effects
> - Constraints and risks (power, water, land, concentration of benefits)

---
## 10. Indian IT Services and GCCs in the AI Era
> 🔴 Tier 1 · _Key points:_ Pyramid model under pressure; fresher hiring down; GCCs growing; reskilling; MBA roles shift to AI delivery and transformation

### Definition
- **IT services model:** revenue linked to headcount (time and materials, fixed-price projects) with a broad pyramid of junior engineers. AI coding and testing tools reduce effort per project, pressuring the pyramid and pricing; clients ask for productivity pass-through.
- **Responses:** outcome-based contracts, AI platforms and accelerators, reskilling at scale, smaller fresher intakes, focus on AI transformation consulting and data engineering.
- **GCCs (global capability centres):** multinationals' own Indian centres for technology, analytics, finance, procurement and supply-chain operations. They are growing and taking higher-value work, including AI.

### Example
Effect on a ₹1,000-crore application-maintenance contract: if AI tools cut effort by 25% and the client demands 15% price reduction, revenue falls to ₹850 crore but cost falls more (say headcount cost from ₹700 crore to ₹525 crore), so margin can **rise** from 30% to about 38% (₹325 crore on ₹850 crore). The catch: fewer people, and the vendor must win more scope to grow revenue.

### In the news
See news box. GCC data (July 2026): over 2,100 GCCs with more than 3,700 units, about \$98.4 billion revenue and over 2.36 million employees. ([NewsBytes](https://www.newsbytesapp.com/news/business/indias-global-capability-centers-hit-984b-revenue-over-236-million-jobs/tldr)) NASSCOM put net tech-sector additions at about 1.35 lakh in FY26 even as the top five IT firms shrank.

### Interview angle
> [!question] How it is asked
> "Will AI kill Indian IT jobs?" or, at an IT/GCC recruiter, "How will AI change our business?"

> [!tip] Strong answer includes
> - Mechanism: effort per project falls; pricing and pyramid change
> - Data: top-5 headcount down 7,389 in FY26 while GCCs and the wider sector grew
> - Opportunity: transformation, data, AI operations, domain consulting (where MBAs fit)

---
## 11. AI and Jobs: The Evidence and a Balanced View
> 🔴 Tier 1 · _Key points:_ Tasks not jobs; augmentation vs automation; entry-level squeeze; new roles; policy responses

### Definition
Framework for any "AI and jobs" question:
1. **Tasks, not jobs:** most jobs are bundles of tasks; AI automates some, augments others, and creates new ones.
2. **Exposure ≠ loss:** high exposure can raise productivity and demand (as spreadsheets did for accountants).
3. **Who is affected first:** routine cognitive and entry-level tasks (drafting, data processing, basic coding, support); physical and interpersonal work less so in the short run.
4. **Distribution:** gains may concentrate; displaced workers need reskilling; geography matters (India's services exports).
5. **Policy:** skilling (IndiaAI FutureSkills), social protection, labour codes ([[178 HR Round, Offers & Salary Negotiation in India]] covers the codes), education reform.

### Example
A supply-chain analyst's week (40 hours): data gathering and cleaning 14 h, report building 8 h, analysis 8 h, meetings and stakeholder work 10 h. With AI tools: gathering 6 h, reports 3 h, analysis 8 h (deeper), meetings 10 h, freeing 13 hours for scenario planning, supplier development or a second category. Whether that becomes a smaller team or a more capable one is a management choice.

### In the news
See news box. In McKinsey's 2025 survey, 32% expected AI to cut their workforce by 3% or more over the next year, 43% expected little change and 13% expected increases.

### Interview angle
> [!question] How it is asked
> GD: "AI will create more jobs than it destroys." Or HR: "Are you worried AI will replace you?"

> [!tip] Strong answer includes
> - Task-based framework and both effects
> - Indian data points (IT headcount, GCC growth)
> - Personal angle: how you use AI to be more valuable ([[232 AI Productivity Toolkit for MBA Work - Excel, SQL, Decks & Research]])

---
## 12. ⭐ Advanced: "Is AI a Bubble?" A Two-Sided GD Brief
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Arguments that it is a bubble:** capex far ahead of revenue; circular deals (suppliers investing in customers); many loss-making model and application companies; falling token prices; high failure rate of enterprise pilots (95% per MIT, 40%+ agent cancellations per Gartner); historical parallel with the 1990s telecom fibre overbuild; short useful lives of GPUs.

**Arguments that it is not (or not only):** real and fast-growing usage; hyperscalers fund capex from strong cash flows, not mainly debt; productivity gains visible in coding, support and back office; costs falling expand the market (Jevons); infrastructure tends to be useful even after a correction (fibre built in the 1990s carried the later internet).

**Balanced position:** "Parts of the market may be overvalued and some investment will be written off, but the underlying technology is real. As with railways and the internet, a financial correction could coexist with long-term transformation. For firms, the lesson is to invest where returns are measurable and keep flexibility."

### Example
GD opening (60 seconds, using PEEL from [[177 Group Discussions & Extempore for MBA Placements]]): "Point: AI shows classic bubble signs but also real economics. Evidence: the four hyperscalers will spend about \$730 billion on capex in 2026, up from about \$410 billion in 2025, while MIT found 95% of corporate GenAI pilots had no P&L impact; yet McKinsey finds 88% of firms already use AI and a small group earns over 5% of EBIT from it. Explanation: valuations may correct, as in the dot-com era, but infrastructure and adoption will remain. Link: for Indian companies, the question is not whether to use AI but how to invest in measurable use cases."

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> GD or extempore: "AI: bubble or revolution?"

> [!tip] Strong answer includes
> - Both sides with dated numbers
> - A historical analogy used carefully
> - A clear, moderate conclusion with implications for business
