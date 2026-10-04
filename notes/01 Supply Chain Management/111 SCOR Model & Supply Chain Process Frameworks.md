---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "SCOR Model & Supply Chain Process Frameworks"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SCOR Model & Supply Chain Process Frameworks

⬅ [[016 Digital Supply Chain & Industry 4.0]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Why Process Reference Models Exist]]
2. [[#2. SCOR: History and the Seven Processes of SCOR DS]]
3. [[#3. The Level Structure: From Scope to Practices]]
4. [[#4. Level 2 Thread Diagrams and Configuration Mapping]]
5. [[#5. Performance Attributes and Level 1 Metrics]]
6. [[#6. Metric Hierarchy and Diagnostic Decomposition]]
7. [[#7. Cost and Asset Metrics: Cash-to-Cash Worked Through]]
8. [[#8. Benchmarking and Gap Analysis with SCOR]]
9. [[#9. Applying SCOR in a Project: Scope, Analyse, Design, Implement]]
10. [[#10. GSCF Framework: Eight Cross-Functional Processes]]
11. [[#11. APQC Process Classification Framework and CSCMP Standards]]
12. [[#12. Gartner Top 25 and Maturity as an Outcome Benchmark]]
13. [[#13. ⭐ Advanced: Using Reference Models in a Consulting Diagnostic Case]]
14. [[#14. ⭐ Advanced: SCOR DS, Digital Data and Resilience Metrics]]

## 📰 News box
> [!news] Shared news hook for this topic (2022–2026): the SCOR standard went digital, and process excellence still decides who ranks at the top
> **Gartner Supply Chain Top 25 (17 June 2026).** Schneider Electric ranked first for the fourth consecutive year with a composite score of **7.05**, ahead of NVIDIA (**6.42**), Walmart (**5.78**) and Cisco (**5.77**). Gartner's published weighting: peer opinion 25%, Gartner expert opinion 25%, ESG 20%, inventory as % of revenue 10%, change in return on productive assets (ROPA) 10%, revenue growth 5%, change in gross margin 5%; Amazon, Apple, Procter & Gamble and Unilever sit in the "Masters" tier. The ranking mixes process capability (opinion scores) with hard asset and cost metrics, the same blend SCOR measures. ([Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2026-06-17-gartner-announces-2026-rankings-of-the-global-supply-chain-top-25); scores cross-checked in [Supply Chain 24/7](https://www.supplychain247.com/article/gartner-2026-global-supply-chain-top-25-rankings))
>
> **SCOR Digital Standard (ASCM, 19 September 2022).** ASCM released SCOR DS, described as the first major update since SCOR's 1996 launch. It adds **Orchestrate**, splits Deliver into **Order** and **Fulfill**, renames Make to **Transform**, replaces the linear chain picture with an infinity loop, and adds resilience, economic and sustainability metrics. The standard is free and open access (Creative Commons); the current document is labelled SCOR Version 14.0 (2025). ([PR Newswire](https://www.prnewswire.com/news-releases/ascm-releases-new-scor-digital-standard-301626710.html); [ASCM SCOR DS page](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/))
>
> **APQC Process Classification Framework v7.4 (August 2024).** The cross-industry PCF has 13 top-level categories; category 4.0 is "Manage Supply Chain for Physical Products" with process groups 4.1 plan and align supply chain resources, 4.2 procure materials and services, 4.3 produce/assemble/test product, 4.4 manage logistics and warehousing. ([APQC PCF 7.4 PDF](https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Why Process Reference Models Exist
> 🔴 Tier 1 · _Key points:_ common language, as-is mapping, benchmarking, design; reference model vs methodology

### Definition
A **process reference model** is a standard, pre-built description of the processes a function performs, together with standard metric definitions and best practices. It does three jobs: (1) **common language** between companies, functions and consultants (what counts as "on time"?); (2) **diagnosis**: map the as-is processes, measure them with standard metrics; (3) **benchmarking and design**: compare with peers and choose practices to close the gap.

It is **descriptive, not prescriptive**: it says what processes and metrics exist, not which strategy to choose. It is not a methodology like Six Sigma ([[008 Six Sigma & Quality Tools]]) or lean ([[007 Lean Manufacturing]]); those are used *inside* the gaps SCOR exposes. The main supply chain models are **SCOR** (ASCM), the **Global Supply Chain Forum (GSCF)** framework, **CSCMP process standards**, the **APQC PCF** (cross-functional) and **Gartner's Top 25** (outcome ranking, not a process model).

### Example
Two Indian FMCG distributors both report "OTIF 92%". One counts a delivery on time if it leaves the DC by the promised date; the other counts delivery at the customer's dock within a window, and ignores short-shipped lines. Without a common definition (see [[012 Supply Chain Analytics & KPIs]]) the numbers cannot be compared. SCOR fixes the definition of each metric (e.g. Perfect Order Fulfillment) so that benchmarking is like for like.

### In the news
See news box. The 2022 SCOR Digital Standard and the 2024 APQC v7.4 update show that reference models are revised every few years to absorb resilience, ESG and digital themes.

### Interview angle
> [!question] How it is asked
> "We want to benchmark our supply chain against peers. How would you start?"

> [!tip] Strong answer includes
> - Standard metric definitions first, otherwise the benchmark is meaningless
> - Choose the reference model by purpose: SCOR for supply chain operations, APQC PCF for enterprise-wide process comparison
> - As-is mapping, then metric baseline, then gap to a peer benchmark, then practice selection
> - Reference model is not strategy: tie gaps to the competitive priority (see [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]])

---

## 2. SCOR: History and the Seven Processes of SCOR DS
> 🔴 Tier 1 · _Key points:_ Plan, Order, Source, Transform, Fulfill, Return, Orchestrate; replaced Plan-Source-Make-Deliver-Return-Enable

### Definition
**SCOR (Supply Chain Operations Reference)** was created in **1996** by the consultancy PRTM and AMR Research for the **Supply Chain Council**, later merged into APICS and now **ASCM**. SCOR 12 (2017) had six processes: **Plan, Source, Make, Deliver, Return, Enable**. The **SCOR Digital Standard (SCOR DS)** reorganises these into **seven**:

| SCOR DS process | Scope | Old SCOR 12 equivalent |
|---|---|---|
| **Plan** | Roadmaps and balancing of demand and supply across the other processes | Plan |
| **Order** | Customer purchase transactions: order receipt, location, payment, status | part of Deliver |
| **Source** | Strategic sourcing, direct and indirect procurement | Source |
| **Transform** | Production, assembly, maintenance, repair, overhaul (MRO services too) | Make |
| **Fulfill** | Executing the order: scheduling, pick-pack-ship, transport, invoicing | part of Deliver |
| **Return** | Reverse logistics: diagnosis and circular disposition (repair, reuse, recycle) | Return |
| **Orchestrate** | Strategy, network design, analytics, risk and compliance, technology and people; sits across the loop | Enable |

The picture is an **infinity loop**, not a left-to-right chain, because modern supply chains are networks with asynchronous information flows (see [[016 Digital Supply Chain & Industry 4.0]]). Plan, Order, Source, Transform, Fulfill and Return are *operational* processes; Orchestrate is the *management* layer that sets rules and resources for them.

### Example
Amul (dairy cooperative): Plan = weekly milk-procurement and product-mix plan; Source = collection from village societies; Transform = pasteurising, converting to butter, cheese, powder; Order = distributor and retailer orders; Fulfill = cold-chain dispatch; Return = expiry returns and packaging take-back; Orchestrate = network design for plants and depots, compliance, IT.

### In the news
See news box. The reason for splitting Deliver into Order and Fulfill and for adding Orchestrate was to reflect digital ordering and platform-based networks, as ASCM's release states.

### Interview angle
> [!question] How it is asked
> "What are the SCOR processes? Has SCOR changed recently?"

> [!tip] Strong answer includes
> - Classic five/six (Plan, Source, Make, Deliver, Return, Enable) and the DS seven with the mapping
> - Why: digital, networked, circular economy, resilience
> - A one-line example per process using a company you know
> - Candour that most benchmark databases and many textbooks still use the SCOR 12 vocabulary

---

## 3. The Level Structure: From Scope to Practices
> 🔴 Tier 1 · _Key points:_ L1 scope, L2 configuration, L3 process elements, below L3 company-specific practices

### Definition
SCOR is a **top-down decomposition**:

| Level | What it defines | Example (SCOR 12 vocabulary) |
|---|---|---|
| **1: Process types** | Scope and competitive priority; the processes in scope; Level 1 metrics | Plan, Source, Make, Deliver, Return |
| **2: Process categories** | The *configuration* of the chain: how each process type is executed | Source stocked product (S1), make-to-order (M2), engineer-to-order (M3) |
| **3: Process elements** | Decomposed steps with inputs, outputs, Level 3 metrics, best practices | S1.1 Schedule Product Deliveries; M2.3 Schedule Production Activities |
| **Below L3** | Company-specific procedures, system transactions, work instructions | SAP transaction steps, SOPs |

Level 2 is where the **decoupling point** shows up: stocked (MTS), make-to-order (MTO) and engineer-to-order (ETO) are different configurations, and a company usually runs several at once (fast movers stocked, long tail made to order). Level 2 also separates **plan** categories (P1 plan supply chain, P2 plan source, P3 plan make, P4 plan deliver, P5 plan return). Detail below Level 3 is deliberately not standardised, because it is where firms differ and compete.

### Example
A bus-body builder in Pune makes standard school-bus bodies on a repeat basis (M1/M2 style: make to stock or order) and customised luxury coaches (M3, engineer to order). Its Level 2 "thread diagram" shows two configurations drawn on one map; planning, sourcing and delivery categories are chosen separately for each. Level 3 then decomposes M3 into engineer-specify, schedule production, issue material, produce and test, package, stage, release to deliver.

### In the news
See news box. SCOR DS publishes its levels, metrics and practices online under an open licence, so a consultant can pull the Level 3 metric definitions without a licence fee.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would use SCOR to describe a company's supply chain."

> [!tip] Strong answer includes
> - Levels 1 to 3 with an example of each
> - Level 2 as configuration (MTS/MTO/ETO) and how products map to configurations
> - Stop at Level 3; practices below are company-specific
> - Scope discipline: choose products, regions and customers first (a "line of sight" from supplier's supplier to customer's customer)

---

## 4. Level 2 Thread Diagrams and Configuration Mapping
> 🔴 Tier 1 · _Key points:_ one product family or channel per thread; MTS vs MTO vs ETO; geography overlay

### Definition
A **thread diagram** (supply chain map) strings together Level 2 process categories along the physical flow for **one product-channel combination**: supplier's supplier, supplier, internal, customer, customer's customer. Each node is labelled with its category code (e.g. sS1 for source stocked product at the supplier, M1, D1, sD2). The steps:
1. Pick a **segment** (product family × channel × region) that has a distinct competitive priority.
2. Draw **geography** (plants, DCs, ports, customers).
3. Assign Level 2 categories per node (stocked, MTO, ETO; retail D4 for stores).
4. Add **Plan** loops above (planning organisation and cadence) and **Return** loops below.
5. Attach **Level 1 metrics** and baseline values.

A thread diagram is deliberately about *flow structure*, not data; it shows, for instance, that three DCs are being used for a product that sells 20 units a day.

### Example
A consumer-durables maker sells a **mixer-grinder** (stocked at a central warehouse, then regional distributor, then retail: thread S1, M1, D1 and the customer's D4) and a **modular kitchen chimney** that is configured in the dealer showroom and shipped to order (S2 and M2, D2). Two thread diagrams, two different Level 2 mixes, and two different metric targets: fill rate and inventory days for the mixer; order cycle time and on-time-to-promise for the chimney.

### In the news
See news box. Large multinational chains rarely run one pipeline for every product; the thread diagram is the SCOR way to make each configuration explicit (an analytical point, not a claim from the Gartner ranking).

### Interview angle
> [!question] How it is asked
> "A client has one supply chain for 40,000 SKUs and says service is poor. What would you do?"

> [!tip] Strong answer includes
> - Segment first (value, volume, variability, channel), then one thread per segment
> - Different Level 2 configuration and different metric priority per segment
> - Cost-to-serve view, see [[138 Order Management, Customer Service & Cost-to-Serve]]
> - Avoid forcing a single KPI target on all segments

---

## 5. Performance Attributes and Level 1 Metrics
> 🔴 Tier 1 · _Key points:_ Reliability, Responsiveness, Agility, Cost, Profit, Assets, Environmental, Social

### Definition
SCOR separates **customer-facing** metrics (how well the chain serves) from **internal** metrics (what it costs and consumes). SCOR 12 had five **performance attributes**; SCOR DS groups **eight** attributes into **three categories**:

| Category | Attribute | Question | Typical Level 1 metric |
|---|---|---|---|
| **Resilience** (customer-focused) | **Reliability** | Do we perform as promised? | Perfect Order Fulfillment (POF) |
| | **Responsiveness** | How fast? | Order Fulfillment Cycle Time |
| | **Agility** | Can we absorb shocks and changes? | Upside/downside flexibility and adaptability (days or %) |
| **Economic** (internal) | **Cost** | What does running it cost? | Total supply chain management cost, % of revenue; cost of goods sold |
| | **Profit** | What do we earn? | Gross margin and operating-profit measures |
| | **Asset management** | How well do we use capital? | Cash-to-cash cycle time; return on fixed assets; return on working capital |
| **Sustainable** | **Environmental** | Footprint? | Emissions, energy, waste measures |
| | **Social** | Impact on people? | Safety, labour and community measures |

The SCOR DS documentation counts **twenty Level 1 metrics** across the eight attributes. The classic SCOR 12 set is the one most often quoted in interviews: POF, OFCT, upside supply chain flexibility, upside and downside adaptability, total SCM cost, COGS, cash-to-cash cycle time, return on supply chain fixed assets, return on working capital. In interviews, say the framework gives **one reliability, one speed, one cost and one asset headline** and that they trade off.

### Example
A pharma distributor in Hyderabad scores 98% on reliability but 7-day cycle time and rising cost: the board wants responsiveness without losing reliability. In SCOR terms, Level 1 shows the pain point; the next step is to decompose into Level 2 and 3 metrics (next sub-topic).

### In the news
See news box. Gartner's 2026 methodology gives ESG 20% and inventory/ROPA 20% (Gartner's own proxies), echoing SCOR DS's addition of environmental and social attributes next to asset management.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you use to judge a supply chain's health, and how do they trade off?"

> [!tip] Strong answer includes
> - One customer-facing KPI per attribute (reliability, responsiveness, agility) and an internal triplet (cost, profit, assets)
> - The trade-offs: responsiveness and agility cost money and assets; efficiency erodes agility
> - Add sustainability metrics per SCOR DS
> - Pick 6 to 10 headline metrics; see KPI-tree guidance in [[012 Supply Chain Analytics & KPIs]]

---

## 6. Metric Hierarchy and Diagnostic Decomposition
> 🔴 Tier 1 · _Key points:_ L1 outcome, L2 diagnostic, L3 root cause; Perfect Order as a product of components

### Definition
Metrics are **hierarchical**: a Level 1 metric is a strategic outcome, Level 2 metrics diagnose it, Level 3 metrics locate the cause. Perfect Order Fulfillment (POF) counts the share of orders that are **on time, in full, damage-free and with accurate documentation**. At order level, an order is perfect only if it passes all four tests. If the components were independent, the share of perfect orders would be the **product** of the component rates; because failures often overlap on the same orders, the true POF is at least the product.

$$POF \;\ge\; \prod_{i} p_i = p_{\text{on-time}} \times p_{\text{in-full}} \times p_{\text{damage-free}} \times p_{\text{docs-correct}}$$

Order fulfillment cycle time (OFCT) is the consistent average time from customer order to delivery; in a SCOR build it is analysed as the sum of **source, make and deliver cycle times** along the critical path (minus overlaps).

### Example
Month data for a Chennai auto-parts distributor: on-time 96%, in-full 94%, damage-free 99%, documents correct 98%. If failures were spread independently over orders, POF $\approx 0.96 \times 0.94 \times 0.99 \times 0.98 = 0.8755$, so about **87.6%**: the customer sees one bad order in eight even though every component looks above 94%. Rule: with $k$ components at $p$ each, POF is about $p^k$, so improving all four components matters more than any one. Cycle time check: source 5 days + make 8 + deliver 4 = **17 days** if sequential. Level 3 then asks: of the in-full failures, how many were *item accuracy* (wrong SKU) versus *quantity accuracy* (short shipped)?

### In the news
See news box. Gartner's inventory-to-revenue and ROPA components are the asset-attribute analogue of SCOR's cash-to-cash and return on fixed assets metrics.

### Interview angle
> [!question] How it is asked
> "On-time is 96% and in-full is 94%, yet customers complain. Why?"

> [!tip] Strong answer includes
> - Perfect order is a conjunction of conditions; separate component KPIs overstate customer experience
> - Compute (at least) the product of components; true value depends on overlap
> - Decompose to Level 3 (item vs quantity accuracy, date achievement) and fix the biggest leak
> - Relate to OTIF definitions and retailer fines in FMCG

---

## 7. Cost and Asset Metrics: Cash-to-Cash Worked Through
> 🔴 Tier 1 · _Key points:_ C2C = DIO + DSO - DPO; total SCM cost % revenue; return on working capital

### Definition
Asset-management and cost attributes translate the chain into rupees:

$$C2C = DIO + DSO - DPO,\quad DIO=\frac{\text{Inventory}}{COGS}\times 365,\; DSO=\frac{\text{Receivables}}{\text{Revenue}}\times 365,\; DPO=\frac{\text{Payables}}{COGS}\times 365$$

$$\text{Cash released} \approx \text{days saved} \times \frac{COGS}{365}$$

**Total SCM cost** in SCOR is built from planning, sourcing, order management, fulfilment, returns and risk/compliance costs, and is expressed as a % of revenue. Return on supply chain fixed assets and return on working capital connect supply chain actions to ROCE (see [[108 Financial Statements & Ratios]] and [[136 Supply Chain Finance & Working Capital]]).

### Example
Company with revenue ₹4,500 cr, COGS ₹3,600 cr, inventory ₹420 cr, receivables ₹560 cr, payables ₹380 cr:
DIO = 420/3,600 × 365 = **42.6 days**; DSO = 560/4,500 × 365 = **45.4 days**; DPO = 380/3,600 × 365 = **38.5 days**; C2C = 42.6 + 45.4 − 38.5 = **49.5 days**. Working capital tied up = 420 + 560 − 380 = ₹600 cr (13.3% of revenue). Cutting DIO by 8 days frees about 8 × 3,600/365 = **₹78.9 cr**, worth about ₹7.9 cr a year at a 10% cost of capital. If total SCM cost is ₹380 cr, it is 8.4% of revenue; closing a 1.4-point gap to a 7.0% benchmark is worth 0.014 × 4,500 = **₹63 cr**.

### In the news
See news box. Inventory as a share of revenue carries a 10% weight in Gartner's 2026 methodology, and ROPA change another 10%, so the ranking explicitly rewards asset-light excellence.

### Interview angle
> [!question] How it is asked
> "Where would you find cash in this supply chain?" (with a balance-sheet snippet)

> [!tip] Strong answer includes
> - Cash-to-cash with correct bases (DIO and DPO on COGS, DSO on revenue)
> - Convert days to rupees with COGS/365
> - Levers for each leg: inventory policy, payment terms, supply chain finance
> - Caveat: stretching DPO can hurt supplier health and resilience

---

## 8. Benchmarking and Gap Analysis with SCOR
> 🔴 Tier 1 · _Key points:_ peer groups, parity/advantage/superior, gap vs strategy, value of closing the gap

### Definition
**SCOR benchmarking** (ASCM's SCORmark programme) collects Level 1 and Level 2 metrics from many companies using the same definitions, then reports where a firm sits against a **peer group** (industry, size, region, supply chain type). Results are often framed as **parity** (around the median), **advantage** and **superior** (top-tier) performance; the exact percentile cut-offs depend on the dataset, so state them as "per the benchmark provider". The consulting use:
1. **Baseline** the metrics using standard definitions.
2. Choose the **target position** per attribute based on strategy: it is neither possible nor sensible to be superior on all (a price-led FMCG player may target superior cost, parity reliability).
3. **Gap** to target, then **value** the gap in rupees.
4. Map each gap to **practices** (e.g. demand sensing for reliability; postponement for agility) and sequence by value and effort.

### Example
Actual versus benchmark median: POF 87.6% vs 94%; OFCT 17 days vs 12; C2C 49.5 days vs 35; total SCM cost 8.4% vs 7.0% of revenue. Strategy: customer-intimacy for key accounts. So reliability and responsiveness are targeted superior, cost parity. Valuation: 14.5 days of C2C (mostly inventory and DSO) is roughly ₹143 cr if all on a COGS-days basis (14.5 × 3,600/365), cost gap ₹63 cr a year.

### In the news
See news box. Gartner's list is an *outcome* benchmark among large firms ($15 billion minimum revenue per the press release); SCOR benchmarking is a *process and metric* benchmark within peer sets.

### Interview angle
> [!question] How it is asked
> "The benchmark says we are below median on cost but top quartile on service. Is that a problem?"

> [!tip] Strong answer includes
> - It depends on the strategy: judge each gap against the chosen priority, not against the median
> - Check peer-group comparability and definitions before reacting
> - Quantify the gap in rupees, then rank initiatives by value and effort
> - Beware of Goodhart effects when targets are set on a single metric

---

## 9. Applying SCOR in a Project: Scope, Analyse, Design, Implement
> 🔴 Tier 1 · _Key points:_ project roadmap, as-is vs to-be, practices catalogue, change management

### Definition
SCOR is usually applied through a four-stage project roadmap (SCOR 12 wording, still used in practice):
1. **Scope and baseline:** define the supply chain (products, customers, geography), thread diagram, Level 1 baseline.
2. **Analyse:** benchmark, find the gap versus competitive requirements, diagnose with Level 2 and 3 metrics (perfect-order decomposition, cycle-time breakdown, cost build-up).
3. **Design:** pick **best practices** and to-be processes, integrate with technology (planning, WMS, TMS; see [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]), set target metrics and a roadmap.
4. **Implement:** pilots, governance, KPIs owners, tracking of benefits, sustain.

Strengths: neutral vocabulary, links strategy to metrics, quick to scope. Limitations: it does not cover sales, marketing, product design and after-sales service in depth; it prescribes few strategic choices; benchmark data may lag; heavy mapping can become an end in itself.

### Example
Mid-size tyre manufacturer in Gujarat: scoping covers three product families and 120 dealers; analysis shows POF 85% mostly from in-full failures on slow-moving SKUs; design adds a stock-keeping policy by segment (see [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]) and a weekly S&OP cycle (see [[120 Integrated Business Planning (IBP) & S&OP Maturity]]); implementation tracks POF monthly with a named owner.

### In the news
See news box. The free availability of SCOR DS lowers the cost of using it as a project backbone, but the 2022 ASCM release itself emphasises digital and networked supply chains, so teams should start with digital data flows in the analysis stage.

### Interview angle
> [!question] How it is asked
> "Describe a structured approach to improving a client's end-to-end supply chain."

> [!tip] Strong answer includes
> - Scope, baseline, benchmark, gap, design, implement, sustain
> - Use of a reference model to avoid reinventing definitions
> - Prioritisation of initiatives by value, effort and dependencies
> - Change management and owners, not just process diagrams

---

## 10. GSCF Framework: Eight Cross-Functional Processes
> 🔴 Tier 1 · _Key points:_ Lambert and Cooper, Global Supply Chain Forum; network, processes, management components

### Definition
The **Global Supply Chain Forum (GSCF)** framework, from Ohio State University researchers (Douglas Lambert, Martha Cooper and others), defines SCM as integrating **eight key business processes** across the chain, run cross-functionally and across firms, not by silos:
1. Customer relationship management
2. Customer service management
3. Demand management
4. Order fulfilment
5. Manufacturing flow management
6. Supplier relationship management
7. Product development and commercialisation
8. Returns management

It has three elements: the **supply chain network structure** (members, links, which links to manage), the **business processes** that cross the chain, and the **management components** that determine how well they work (planning and control, work structure, organisation structure, product-flow facility structure, information-flow structure, management methods, power and leadership, risk and reward structure, culture and attitudes). Compared with SCOR, GSCF includes **commercial** processes (CRM, product development) and **relationships**; SCOR goes deeper into **operational metrics and practices**.

### Example
A packaged-foods firm introduces a new product: GSCF says product development and commercialisation must run jointly with supplier relationship management (ingredient specification, co-packers), manufacturing flow (changeover and pack-size complexity) and customer relationship management (retailer listing, trade terms), not hand off sequentially from R&D to the factory. The cross-functional team and joint plan are the GSCF idea; the SCOR counterpart would measure the resulting POF and OFCT.

### In the news
See news box. Gartner's "Masters" tier and top 25 praise end-to-end orchestration; the 2026 release quotes Gartner on "orchestrating supply chains end-to-end", the idea at the core of GSCF integration.

### Interview angle
> [!question] How it is asked
> "How does SCOR differ from other supply chain frameworks you know?"

> [!tip] Strong answer includes
> - SCOR: operational process and metric standard; GSCF: relationship and cross-functional process management; APQC: enterprise-wide taxonomy
> - Name the eight GSCF processes or at least the commercial ones SCOR lacks
> - Say which you would choose for which job
> - Link to integration and collaboration themes in [[001 SCM Introduction & Fundamentals]]

---

## 11. APQC Process Classification Framework and CSCMP Standards
> 🔴 Tier 1 · _Key points:_ 13 categories, 5 levels, cross-industry taxonomy; CSCMP process standards and SCPro

### Definition
The **APQC Process Classification Framework (PCF)** is a cross-industry taxonomy of business processes with **five levels**: category, process group, process, activity, task. Version 7.4 (August 2024) has **13 categories**:

| No. | Category | No. | Category |
|---|---|---|---|
| 1.0 | Develop vision and strategy | 8.0 | Manage information technology |
| 2.0 | Develop and manage products and services | 9.0 | Manage financial resources |
| 3.0 | Market and sell products and services | 10.0 | Acquire, construct and manage assets |
| 4.0 | Manage supply chain for physical products | 11.0 | Manage enterprise risk, compliance, remediation and resiliency |
| 5.0 | Deliver service | 12.0 | Manage external relationships |
| 6.0 | Manage customer service | 13.0 | Develop and manage business capabilities |
| 7.0 | Develop and manage human capital | | |

Categories 1 to 6 are **operating** processes; 7 to 13 are **management and support** services. Supply chain sits mainly in **4.0** (plan, procure, produce, logistics and warehousing) but touches 2.0, 3.0, 6.0 and 9.0. APQC pairs the PCF with open **benchmarking** measures. **CSCMP** (Council of Supply Chain Management Professionals) publishes its own supply chain process standards and the **SCPro** certification; for the certification landscape see [[144 SCM Body of Knowledge Map - CSCP, CPIM, CLTD & SCPro]].

### Example
A bank's operations team and a manufacturer's supply chain team want to compare "procure to pay" cost per invoice. SCOR does not cover the finance side; APQC's PCF (9.0 financial resources, with accounts payable) and its benchmarking measures do. For a plant-level question (OFCT, POF) SCOR is the right tool. Rule of thumb: **SCOR for the physical chain, APQC for the whole enterprise**.

### In the news
See news box. APQC's v7.4 (August 2024) reflects the 2024 refresh; the category list above is as shown in that PDF.

### Interview angle
> [!question] How it is asked
> "Which process model would you use to compare shared-service costs across industries?"

> [!tip] Strong answer includes
> - APQC PCF for cross-industry enterprise processes; SCOR for supply chain-specific operations
> - Five levels of the PCF and its operating vs management split
> - Use of both: PCF for taxonomy, SCOR for metrics and practices
> - Do not claim CSCMP or APQC benchmark values you cannot cite

---

## 12. Gartner Top 25 and Maturity as an Outcome Benchmark
> 🔴 Tier 1 · _Key points:_ composite scoring, Masters, what it measures and what it misses

### Definition
The **Gartner Supply Chain Top 25** is an annual ranking of large companies (the 2026 release mentions a $15 billion revenue threshold) combining **opinion** scores (peers 25%, Gartner experts 25%) with **ESG** (20%) and **financial and asset** outcomes (inventory as % of revenue 10%, ROPA change 10%, revenue growth 5%, gross margin change 5%). Companies with long-term top performance enter the **Masters** tier (2026: Amazon, Apple, P&G, Unilever). Use it as a **proxy for best-in-class practice** and as a source of case examples; do not mistake it for a process standard: it does not tell you *how* to improve a particular metric.

Gartner also publishes **supply chain maturity** stages; maturity models are covered in [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]]. The ratios used in the ranking link to [[012 Supply Chain Analytics & KPIs]].

### Example
Interviewer: "Why is Schneider Electric repeatedly ranked first?" A structured answer: strong asset and financial outcomes (inventory, ROPA), high ESG score, peer reputation (opinion scores are half the weight) and digital and AI use. Then ask what part is transferable to a mid-size Indian manufacturer (planning discipline, end-to-end visibility) and what is not (scale, multinational footprint).

### In the news
See news box. 2026 scores: Schneider Electric 7.05, NVIDIA 6.42, Walmart 5.78, Cisco 5.77 (Gartner and Supply Chain 24/7); weights are as listed in Gartner's release.

### Interview angle
> [!question] How it is asked
> "What do the best supply chains in the world have in common?"

> [!tip] Strong answer includes
> - Ranking criteria (outcomes plus reputation) and a caution about their limits
> - Common traits: end-to-end orchestration, segmentation, digital planning, sustainability
> - A named example with one verifiable fact
> - Relevance to India: scale and network density differ, discipline is transferable

---

## 13. ⭐ Advanced: Using Reference Models in a Consulting Diagnostic Case
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Consultants rarely run a full SCOR project in an interview; they borrow its **logic**: (1) fix **definitions** and scope, (2) split performance into **customer-facing** (reliability, speed, flexibility) and **internal** (cost, assets), (3) **decompose** the outcome metric into drivers, (4) **benchmark** each driver, (5) **value** gaps, (6) recommend practices by value and effort. A SCOR-style **KPI tree** puts the Level 1 metric at the root:

$$POF \rightarrow \{\text{on-time},\ \text{in-full},\ \text{damage-free},\ \text{docs}\} \rightarrow \{\text{planning, capacity, inventory, transport, packing, systems}\}$$

Pitfalls: boiling the ocean (full mapping with no hypothesis), mixing definitions, treating median as target, ignoring trade-offs (service vs cost vs assets), and giving a model name without an insight.

### Example
Case: "A refrigerator maker's market share is stable but profit fell 3 points." Hypothesis-driven use of SCOR logic: Costs: total SCM cost 8.4% vs benchmark 7.0% (1.4 points of the 3). Assets: inventory days 42.6 vs best peers 35, tied capital charge. Reliability: POF 87.6%, with expedited freight for failures (cost link). Next step: decompose the cost gap into planning, sourcing, warehousing, transport and returns, then find that expedited freight caused by in-full failures is the biggest piece. Recommendation: fix forecast and stock segmentation before cutting freight rates.

### In the news
See news box. The SCOR DS has added resilience and sustainability attributes; a modern case answer should add a risk and ESG lens (see [[015 Supply Chain Risk & Resilience]] and [[141 Supply Chain Disruption Case Library (2011-2026)]]).

### Interview angle
> [!question] How it is asked
> "Structure how you would diagnose why this company's logistics costs and service are both worse than competitors."

> [!tip] Strong answer includes
> - Tree with definitions (POF, OFCT, cost % revenue, C2C)
> - A hypothesis ("both are caused by poor planning and too many SKUs") and a data request to test it
> - Valuing the gap in rupees and sequencing quick wins versus structural fixes
> - Awareness that SCOR is a vocabulary: the insight comes from the diagnosis, see [[024 Consulting Frameworks]] and [[026 Case Interview — Operations Cases]]

---

## 14. ⭐ Advanced: SCOR DS, Digital Data and Resilience Metrics
> ⭐ Advanced · _Added beyond the tracker_

### Definition
SCOR DS is **digital** in two senses: it is published as an online, searchable standard (processes, metrics, practices, features) and it is designed for **data-driven** supply chains where metrics are computed from event data rather than surveys. Practical consequences:
- **Orchestrate** includes analytics, technology and risk and compliance as managed processes (digital twins, control towers, [[173 Process Mining & Operations Intelligence]]).
- **Agility** and the **resilience** category keep metrics such as upside and downside adaptability (how well the chain absorbs a sudden change in volume or supply).
- **Sustainability** attributes bring emissions and social metrics into the same hierarchy as cost and reliability.
- Event data (ERP timestamps, WMS and TMS events) lets POF and OFCT be computed per order automatically, replacing sampled reports.

Limits: a standard definition still needs **data quality and master data** ([[175 Data Quality, Master Data & Data Governance]]); different ERP timestamps can make "on time" disagree between systems.

### Example
An Indian electronics assembler computes OFCT from SAP timestamps: order creation, delivery creation, goods issue, proof of delivery. Taking the median of 12 days and a 90th percentile of 21 days shows a long tail that an average hides; Level 3 drill-down finds the tail comes from orders awaiting a single imported component. Under the agility attribute the firm sets a target: absorb a 20% demand surge within a set number of days by pre-qualifying a second source.

### In the news
See news box. ASCM states SCOR DS now includes resilience, economic and sustainability metrics; Gartner's 2026 emphasis on AI and autonomous planning shows why event-level metric computation is becoming the norm.

### Interview angle
> [!question] How it is asked
> "How would you build a real-time supply chain KPI dashboard on a standard like SCOR?"

> [!tip] Strong answer includes
> - Metric definitions first, then event data model, then dashboards (see [[047 MIS & Dashboard Design]])
> - Per-order computation of POF and OFCT, with percentiles instead of just averages
> - Data governance: one timestamp definition per milestone
> - Link to resilience: track adaptability and flexibility, not only efficiency
