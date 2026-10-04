---
tags: [analytics-tools, tier2]
area: Analytics & Tools
topic: "Process Mining & Operations Intelligence"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Process Mining & Operations Intelligence

⬅ [[172 Tableau & Looker Studio - BI Tool Comparison]] · [[_Index - Analytics & Tools|Analytics & Tools]] · [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]] ➡

> **Area:** Analytics & Tools · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. What Process Mining Is and Where It Fits]]
2. [[#2. Event Logs: Case ID, Activity, Timestamp]]
3. [[#3. Discovery: Process Models from Logs]]
4. [[#4. Conformance Checking]]
5. [[#5. Enhancement, Variant and Bottleneck Analysis]]
6. [[#6. Use Cases: Purchase-to-Pay, Order-to-Cash and Warehouse]]
7. [[#7. Tools Landscape: Celonis, SAP Signavio, UiPath, PM4Py and Others]]
8. [[#8. Worked Example: Event Log to Insights]]
9. [[#9. Automation Rate, Rework and Process KPIs]]
10. [[#10. Linking to RPA, Lean and Continuous Improvement]]
11. [[#11. Data Preparation, Limitations and Privacy]]
12. [[#12. Business Case and Implementation Roadmap]]
13. [[#13. ⭐ Advanced: Object-Centric Process Mining and Agentic Operations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Process mining becomes the "context layer" for enterprise AI
> **Celonis launches the Context Model and agrees to buy Ikigai Labs (12 May 2026).** Celonis announced the Celonis Context Model (CCM), described as a dynamic, real-time digital twin of operations that gives enterprise AI the operational context it lacks, and signed a definitive agreement to acquire Ikigai Labs (AI decision intelligence: planning, simulation, forecasting; MIT-founded). Deal size and ARR were not disclosed. The announcement positions process data, not just documents, as what AI agents need to act correctly. ([Celonis press release](https://www.celonis.com/news/press/celonis-launches-the-context-model-to-eliminate-enterprise-ais-operational-blind-spots-agrees-to-acquire-ai-decision-intelligence-leader-ikigai-labs))
>
> **A crowded, funded market.** Celonis (founded 2011 at TU Munich) raised $1 bn at an $11 bn valuation in June 2021 and a further $400 m at $13 bn in August 2022, about $1.77 bn in total funding as of 2026 according to a Wikipedia summary. The same summary notes that about 30 commercial process mining tools existed in 2018 and Gartner listed about 40 by 2025. SAP bought Signavio in March 2021 for EUR 950 million to fold process modelling and mining into its stack. ([Wikipedia: Celonis](https://en.wikipedia.org/wiki/Celonis), [Wikipedia: Process mining](https://en.wikipedia.org/wiki/Process_mining), [Wikipedia: Signavio](https://en.wikipedia.org/wiki/Signavio))
>
> **Mining feeds automation (vendor-reported results).** UiPath ties process mining and task mining to its automation platform and cites customer results such as Orange France (EUR 300 m business value over 4 years) and Isbank (26 processes mined, 116k hours saved, 61% of cases optimised). These are vendor case-study claims, not independent audits. ([UiPath](https://www.uipath.com/product/process-mining))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. What Process Mining Is and Where It Fits
> 🟠 Tier 2 · _Key points:_ Event data to process models; fact-based; vs BPM, BI, Six Sigma, RPA

### Definition
**Process mining** extracts knowledge from **event logs** recorded by information systems (ERP, CRM, WMS, ticketing) to **discover, monitor and improve** the real processes. Wil van der Aalst (Eindhoven) coined the term around 1999; the IEEE Task Force on Process Mining (founded 2009) published a manifesto and the IEEE **XES** standard for event data.

Where it sits relative to other tools:
- **Business Process Management (BPM):** designed processes ("as-is on paper"); mining shows the **as-executed** process from data.
- **Business intelligence:** aggregates KPIs; mining adds the **sequence and time** between events, so it explains *why* a KPI moved.
- **Lean and Six Sigma** ([[007 Lean Manufacturing]], [[008 Six Sigma & Quality Tools]]): value-stream maps and DMAIC rely on interviews and sampling; mining is a full-population, data-driven map for the Measure and Analyse phases.
- **RPA** (robotic process automation): bots execute tasks; mining finds which processes and variants are worth automating and measures the result.
- **Operations intelligence** (the term used by many vendors): continuous monitoring of process performance with alerts and actions, sometimes called a **process control tower** or **execution management system**.

Core value: **transparency** (see the true process), **diagnosis** (where time, cost, rework and non-compliance arise), **continuous monitoring** and **simulation or automation** of improvements. See process basics in [[017 Process Management & Optimization]] and the ERP data layer in [[013 ERP & Enterprise Systems (SAP-Oracle)]].

### Example
In an illustrative case, a manufacturer believes its purchase-to-pay takes 10 days because the SOP says so. Mining the ERP data of 250,000 purchase orders shows a median of 19 days with 14 distinct paths for the same process, 23% of POs created after the invoice was received, and a long wait before payment approvals. No interview surfaced this because each team saw only its own step.

### In the news
See news box. Celonis calls its Context Model a digital twin of operations for AI, and UiPath positions mining as the front end of automation: process mining is moving from analysis tool to infrastructure.

### Interview angle
> [!question] How it is asked
> "What is process mining and how is it different from a dashboard or a process map drawn in a workshop?"

> [!tip] Strong answer includes
> - Built from system event logs; shows as-is process with real sequences and times
> - Complements, not replaces, BI (what) and workshops (why people behave so)
> - Links to lean/Six Sigma (data for Measure/Analyse) and RPA (what to automate)
> - Gives one example with a number (cycle time, variants, rework)

---
## 2. Event Logs: Case ID, Activity, Timestamp
> 🟠 Tier 2 · _Key points:_ Minimal log; case notion; optional attributes; XES; tables in SAP

### Definition
An **event log** is a table where each row is an **event** with at least:
1. **Case ID:** the process instance that events belong to (purchase order, sales order line, invoice, shipment, ticket).
2. **Activity:** what happened (Create PO, Goods Receipt, Pay Invoice).
3. **Timestamp:** when it happened, ideally with time, not only date, to order events inside a day.

Optional but valuable: **resource/user** (person, system or bot), **organisation/plant**, **cost or amount**, **product**, **vendor**, **channel**. Case attributes (vendor, value) describe the whole case; event attributes describe one event. **XES** is the XML standard; CSV with these columns is more common in practice.

Choice of **case notion** drives results: in order-to-cash the case can be sales order, sales order item or delivery; picking the wrong level produces one-to-many distortions (an order with several deliveries repeats activities).

**Extraction in SAP:** purchase documents come from tables such as EKKO/EKPO (PO header and item) and EKBE (PO history: goods and invoice receipts), invoices from RBKP/RSEG, accounting documents from BKPF/BSEG, sales from VBAK/VBAP/LIKP/VBRK, and **change documents** from CDHDR/CDPOS (who changed which field, when), which supply events like "Change PO price" and "Block invoice". Related: [[080 SAP MM — Materials Management]], [[082 SAP SD — Sales & Distribution]], [[085 SAP Reporting & Analytics]].

### Example
Mini log in pandas-ready form (three of the cases used in the worked example later):

| case | activity | timestamp | resource |
|---|---|---|---|
| P1 | Create PR | 2026-07-01 09:00 | user |
| P1 | Approve PR | 2026-07-02 11:00 | user |
| P1 | Create PO | 2026-07-02 15:00 | user |
| P1 | Goods Receipt | 2026-07-09 10:00 | user |
| P1 | Invoice Receipt | 2026-07-10 10:00 | bot |
| P1 | Pay Invoice | 2026-07-20 10:00 | bot |
| P4 | Create PR | 2026-07-02 10:00 | user |
| P4 | Create PO | 2026-07-02 16:00 | user |
| P4 | Approve PR | 2026-07-05 10:00 | user |

Case P4 created the PO before the requisition was approved: visible only because the log keeps order and time.

### In the news
See news box. AI agents need exactly this kind of ordered, timestamped event data to understand what state a business process is in, which is what Celonis' Context Model builds on.

### Interview angle
> [!question] How it is asked
> "What data do you need to start a process mining project?"

> [!tip] Strong answer includes
> - Case ID, activity, timestamp as the minimum; resource and attributes as the enrichment
> - Case notion decision (order vs order item) and its consequences
> - Where the data comes from (ERP tables, change logs, WMS scans, ticket logs) and extraction effort
> - Data quality: timestamps, missing events, clock/time-zone issues

---
## 3. Discovery: Process Models from Logs
> 🟠 Tier 2 · _Key points:_ Directly-follows graph, variants, alpha/heuristic/inductive miners, filtering

### Definition
**Process discovery** builds a model of the real process from the log, with no prior model required. Output types:
- **Directly-follows graph (DFG):** nodes = activities, arcs = "A directly followed by B" with **frequency** and mean time. Simple, scalable and what most commercial tools show.
- **Petri net / process tree / BPMN:** formal models that express sequence, choice, parallelism and loops.
- **Variants:** unique activity sequences; each case belongs to one variant. A **variant explorer** ranks them by frequency and by throughput time.

Algorithms: **alpha miner** (2000; simple, sensitive to noise), **heuristic miner** (2001; frequency-based, handles noise), **inductive miner** (guarantees sound models, robust with filtering). Tools let users filter by **variant coverage** (for example keep the variants covering 95% of cases), **time window**, **attribute** (vendor, plant) and **activity frequency**, because the unfiltered "spaghetti" model of real processes is unreadable.

Key concepts: **happy path** (the intended sequence), **throughput time** (case start to end), **waiting vs processing time**, **loops** (rework), **skips**.

### Example
Eight purchase-to-pay cases (full data in the worked-example sub-topic) produce four variants:

| Variant | Cases | Share |
|---|---|---|
| Create PR, Approve PR, Create PO, Goods Receipt, Invoice Receipt, Pay Invoice | 5 | 62.5% |
| ... with one Change PO Price after Create PO | 1 | 12.5% |
| ... with two Change PO Price events | 1 | 12.5% |
| Create PR, **Create PO**, Approve PR, Goods Receipt, Invoice Receipt, Pay Invoice | 1 | 12.5% |

The happy path covers 5 of 8 cases (62.5%); the top three variants cover 7 of 8 (87.5%). In a real log of 200,000 POs with 14 variants, the first three variants often cover most volume while the tail hides compliance problems.

Python (open source **PM4Py**, installed with `pip install -U pm4py`; the library's README shows reading an XES log and discovering a Petri net):

```python
import pm4py

log = pm4py.read_xes("p2p.xes")
net, im, fm = pm4py.discover_petri_net_inductive(log)
pm4py.view_petri_net(net, im, fm, format="svg")
```

### In the news
See news box. With 40-odd tools listed by Gartner, the discovery view itself is a commodity; value is in what the vendor adds after discovery (connectors, process-specific KPIs, actions).

### Interview angle
> [!question] How it is asked
> "You get a log with 50 variants. How do you make sense of it?"

> [!tip] Strong answer includes
> - Variant frequency and coverage; start with the happy path and the top deviations
> - Filters by time, attribute and frequency to remove noise
> - Distinguishing legitimate variants (rush orders) from errors
> - Discovery gives hypotheses; validate with process owners

---
## 4. Conformance Checking
> 🟠 Tier 2 · _Key points:_ Compare log with reference model or rules; fitness, precision; deviations and root causes

### Definition
**Conformance checking** compares the event log with a **reference model** (BPMN or Petri net), or with **business rules**, to find deviations: skipped steps, wrong order, unauthorised activities, segregation-of-duties breaches. Techniques include **token-based replay** and **alignments** (minimal edits to make a trace fit the model).

Model-quality dimensions (van der Aalst): **fitness** (does the model replay the log?), **precision** (does the model allow much more than seen?), **generalisation** (does it avoid overfitting?) and **simplicity**.

Rule-based conformance examples in P2P: **three-way match** (PO, goods receipt, invoice) before payment; "PR must be approved before PO"; **segregation of duties** (the same user must not create and approve a PO); payments after due date; duplicate payments. In O2C: credit check before release, delivery before invoice. Results feed **internal audit** and **controls** (see [[190 SAP FI-CO Essentials for Operations Professionals]]).

Metric: **conformance rate** = conforming cases ÷ total cases; also **deviation cost** (value of non-conforming cases).

### Example
Rule: "Purchase requisition must be approved before the PO is created." In the eight-case log, only case P4 breaches it (PO created on 2 July, approval on 5 July), so conformance = 7/8 = **87.5%**. Value at stake: if P4 was a ₹18 lakh purchase, the retrospective approval is a control weakness, a candidate for blocking PO creation in the ERP until approval. In a real log, a conformance rate of 87.5% on 200,000 POs means 25,000 non-compliant POs, which an auditor would want to sample by value and vendor.

### In the news
See news box. As companies deploy AI agents that create or approve documents, conformance rules (what the agent may do and in what order) become guardrails; this is a stated use case for operational context models.

### Interview angle
> [!question] How it is asked
> "How can process mining help internal audit?"

> [!tip] Strong answer includes
> - Full-population testing instead of sampling; rules coded on the log
> - Examples: maverick buying, SoD, duplicate payment, approval bypass
> - Conformance rate and value at risk; follow-up controls in the ERP
> - Limits: only what is logged; off-system activities are invisible

---
## 5. Enhancement, Variant and Bottleneck Analysis
> 🟠 Tier 2 · _Key points:_ Performance overlays, waiting time between activities, resource and variant comparison

### Definition
**Enhancement (performance) analysis** projects timing and cost data onto the discovered model: **throughput time** (end to end), **service/processing time**, **waiting time** (between events), **frequency**, **cost** and **resource load**. A **bottleneck** is a step or hand-off with high waiting time, high frequency and thus large total delay (mean wait × number of cases).

Analyses:
- **Variant analysis:** compare fast vs slow variants, or vendor A vs vendor B, plant vs plant: where do the paths diverge, and how much time does the divergence cost?
- **Bottleneck analysis:** rank edges by **mean and total waiting time**; look for hand-offs between teams and queues; check by time of day, day of week and month-end peaks.
- **Resource analysis:** workload per user, hand-over networks, rework by resource.
- **Rework:** same activity repeated or a loop back; **rework rate** = cases with rework ÷ cases; **rework cost** = extra events × cost per event.
- **Root cause analysis:** attributes that correlate with delay (vendor, plant, order value, material group).
- **Root-cause to action:** convert findings to improvement levers (policy, automation, vendor terms), then monitor.

Relation to flow metrics: by Little's law ($WIP = \text{throughput rate} \times \text{cycle time}$; see [[003 Inventory Management]] and [[005 Production & Operations Planning]]) a long waiting time is also inventory of unfinished invoices or orders.

### Example
Mean waiting time between consecutive activities across the eight cases (days):

| Hand-off | Cases | Mean wait (days) |
|---|---|---|
| Invoice Receipt to Pay Invoice | 8 | **11.0** |
| Create PO to Goods Receipt | 5 | 6.9 |
| Change PO Price to Goods Receipt | 2 | 6.4 |
| Create PR to Approve PR | 7 | 1.9 |
| Goods Receipt to Invoice Receipt | 8 | 1.1 |
| Approve PR to Create PO | 7 | 0.1 |

Average throughput = 21.5 days (median 19.5); the Invoice-to-Payment wait is about **51%** of the average case time. Part of this is intended (payment terms) but cases P3 (26 days) and P6 (29 days, two price changes) show that **rework adds 7 to 10 days**. Action: decouple payment run from approval by auto-scheduling payments at the due date (to protect cash), and fix price master data to remove price changes.

### In the news
See news box. UiPath's "26 processes mined, 61% of cases optimised" claim is the type of bottleneck-driven improvement described here, though results come from a vendor case study.

### Interview angle
> [!question] How it is asked
> "Where would you look first to cut order-to-cash cycle time using process data?"

> [!tip] Strong answer includes
> - Waiting time between hand-offs rather than processing time; rank by total delay (mean × volume)
> - Variant and attribute comparison to find root causes
> - Rework loops and approval queues as typical culprits
> - Differentiates intended waits (payment terms) from unintended ones

---
## 6. Use Cases: Purchase-to-Pay, Order-to-Cash and Warehouse
> 🟠 Tier 2 · _Key points:_ KPIs per process; touchless rate; on-time; maverick buying; pick-pack-ship

### Definition
**Purchase-to-pay (P2P):** requisition, approval, PO, goods receipt, invoice, payment. KPIs: throughput time, **touchless (no-touch) PO or invoice rate**, maverick/off-contract spend, PO after invoice rate, rework (price/quantity changes), duplicate payments, early or late payment (discount capture, working capital). Links: [[002 Procurement & Strategic Sourcing]], [[192 SAP Sourcing & Procurement Deep Dive]].

**Order-to-cash (O2C):** order entry, credit check, delivery, goods issue, invoice, payment. KPIs: **OTIF** (on-time-in-full), order changes, blocked orders, days sales outstanding, **first-time-right** orders, reasons for delay. See [[195 SAP SD Advanced - Pricing, Output & Document Flow]], [[012 Supply Chain Analytics & KPIs]].

**Warehouse and logistics:** events from WMS scans and RF devices: receive, putaway, pick, pack, load, ship. KPIs: dock-to-stock time, pick cycle time, replenishment delays, order-to-ship, travel and waiting by zone, idle time, damage and exception loops. See [[010 Warehouse Management]], [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]]. Sensor and telematics data are also event sources (IoT, see [[016 Digital Supply Chain & Industry 4.0]]).

Other: **manufacturing** (order release to confirmation, using [[081 SAP PP — Production Planning]] data), **customer service** (ticket handling, SLA), **finance close**, **IT incident management**, **healthcare patient pathways**.

### Example
O2C KPI from a log: orders due = 1,300 across three warehouses; delivered on time and in full = 1,100; OTIF = 84.6%. Mining shows delivery delays concentrated in orders with a **credit block** (illustrative average block of 2.4 days) and **delivery date changed after confirmation**. Fixing credit-block hand-off with an auto-release rule for customers under limit removes one of the two main causes. In the warehouse, a scan log may show that **put-away to first pick** is 9 hours for one zone and 2 hours for another; the variant analysis reveals manual re-labelling in the slow zone.

### In the news
See news box. Vendors package these as ready-made process connectors for SAP and others because P2P and O2C are the two most commonly started use cases.

### Interview angle
> [!question] How it is asked
> "Pick a process in a company you know and say how you would improve it using process mining."

> [!tip] Strong answer includes
> - A defined process with the case ID, key events and 3 to 5 KPIs
> - A hypothesis about where delay or cost sits and the data to test it
> - A specific action (rule, automation, vendor term) and the metric to track
> - Realism about data access and change management

---
## 7. Tools Landscape: Celonis, SAP Signavio, UiPath, PM4Py and Others
> 🟠 Tier 2 · _Key points:_ Commercial platforms, open-source, task mining; selection criteria

### Definition
| Tool | Notes (checked in this session) |
|---|---|
| **Celonis** | Market-leading specialist (founded 2011); Execution Management System and Process Intelligence Graph; launched the Context Model in May 2026 |
| **SAP Signavio** | Process modelling plus Process Intelligence (mining); SAP bought Signavio in March 2021 for EUR 950m; strong in SAP landscapes (see [[079 SAP Fundamentals & Architecture]]) |
| **UiPath Process Mining / Task Mining** | Mining linked to RPA and orchestration; case studies on automation value |
| **Microsoft Power Automate Process Mining, IBM, Software AG ARIS, Apromore, Minit, Disco** | Other commercial options with different price and integration profiles |
| **PM4Py** | Open-source Python library (AGPL-3.0 on GitHub, with a commercial licence option) for discovery, conformance and more |
| **ProM, bupaR** | Academic and R-based open-source tools |

**Process mining vs task mining:** process mining uses system event logs; **task mining** records user desktop actions (clicks, keystrokes, application switches) to see manual work that systems do not log; used together for automation discovery.

Selection criteria: connectors for your ERP/WMS, scale and speed (millions of events), object-centric capability, governance and security, action layer (alerts, workflows, RPA triggers), price and total cost of ownership, vendor ecosystem, India data-residency and support, and skills (open-source needs data engineers).

Using pandas for small experiments is enough to learn: see [[064 Pandas — Data Manipulation]] and [[045 SQL for Operations Analytics]] (event logs are often built with SQL window functions: `LEAD` for next activity).

### Example
A mid-size Indian manufacturer with SAP ECC and about 40,000 POs a month shortlists three options. Criteria weights (agreed first): ERP connector 30%, usability 20%, time to value 20%, price 20%, AI/action layer 10%. Scores out of 10: platform A 8, 7, 6, 5, 9; platform B 9, 8, 7, 4, 7; PM4Py with an in-house team 5, 4, 4, 9, 3. Weighted: A = 2.4 + 1.4 + 1.2 + 1.0 + 0.9 = 6.9; B = 2.7 + 1.6 + 1.4 + 0.8 + 0.7 = 7.2; PM4Py = 1.5 + 0.8 + 0.8 + 1.8 + 0.3 = 5.2. Platform B wins on the criteria; a proof of value on one process confirms before a large contract.

### In the news
See news box. SAP owning Signavio and Celonis integrating deeply with SAP data show that mining is a battleground tied to ERP ecosystems; PM4Py shows open-source remains viable for teams with data skills.

### Interview angle
> [!question] How it is asked
> "Which process mining tool would you pick and why?"

> [!tip] Strong answer includes
> - Criteria: connectors, scale, usability, action layer, price, skills
> - Commercial vs open-source trade-off
> - Proof of value on one process before enterprise licences
> - Mentions task mining as a complement

---
## 8. Worked Example: Event Log to Insights
> 🟠 Tier 2 · _Key points:_ Eight P2P cases; variants, throughput, waiting time, rework, conformance, automation rate

### Definition
Procedure: (1) load the log; (2) sort by case and timestamp; (3) build variants; (4) compute throughput time per case; (5) compute the next activity and the waiting time per hand-off; (6) apply conformance rules; (7) compute rework and automation metrics; (8) summarise findings and actions.

```python
import pandas as pd

df = pd.read_csv("p2p_log.csv", parse_dates=["ts"]).sort_values(["case", "ts"])
variants = df.groupby("case").activity.apply(" > ".join).value_counts()
throughput = df.groupby("case").ts.agg(lambda s: (s.max() - s.min()).days)
df["next_act"] = df.groupby("case").activity.shift(-1)
df["next_ts"] = df.groupby("case").ts.shift(-1)
edges = df.dropna(subset=["next_act"]).assign(
    wait=lambda d: (d.next_ts - d.ts).dt.total_seconds() / 86400)
bottlenecks = edges.groupby(["activity", "next_act"]).wait.agg(["size", "mean"])
```

### Example
The eight-case log (51 events; resource "bot" = an automated posting). Computed results:

| Metric | Value | Reading |
|---|---|---|
| Variants | 4 (happy path 5 of 8 = 62.5%) | Process mostly standard |
| Throughput time | 19.0 to 29.0 days; mean 21.5; median 19.5 | Two slow outliers |
| Largest wait | Invoice Receipt to Pay Invoice 11.0 days, about 51% of average case time | Payment scheduling |
| Rework | 2 of 8 cases (25%), 3 extra "Change PO Price" events | Price master-data issue |
| Conformance (PR approved before PO) | 7 of 8 = 87.5% | One maverick case |
| Automation: events done by bot | 13 of 51 = 25.5% overall; 13 of 16 = 81% of the Invoice Receipt and Pay Invoice events | Automation concentrated in the back end |
| Clean cases (conforming and no rework) | 5 of 8 = 62.5% | "First-time-right" rate |

Interpretation: the cases that either reworked prices (P3, P6) or deviated in order (P4) are the slowest or weakest; fixing price master data and enforcing approval-before-PO would lift first-time-right from 62.5% towards 100% in this sample. With only eight cases the numbers are illustrative, not statistically reliable: real projects use thousands of cases and report confidence by variant and period.

### In the news
See news box. The same arithmetic, run continuously on the full event stream, is what vendors call operations intelligence, and it is the data that AI agents would rely on.

### Interview angle
> [!question] How it is asked
> "Here is an event log. Tell me what you see and what you would do."

> [!tip] Strong answer includes
> - Variants, throughput, biggest hand-off waits, rework and rule breaches, with numbers
> - Prioritised actions with owners and a metric for each
> - Caveat on sample size and data quality
> - Next step: validate with process owners, then monitor

---
## 9. Automation Rate, Rework and Process KPIs
> 🟠 Tier 2 · _Key points:_ Touchless rate, automation rate, rework, first-time-right, conformance, cost per case

### Definition
Define KPIs precisely before reporting; vendors differ.

| KPI | Definition | Formula |
|---|---|---|
| **Touchless (no-touch) rate** | Cases with no manual event from start to end | $\frac{\text{cases with only system/bot events}}{\text{total cases}}$ |
| **Automation rate** | Share of events (or activities) executed automatically | $\frac{\text{automated events}}{\text{all events}}$ |
| **Rework rate** | Cases with a repeated or loop-back activity | $\frac{\text{cases with rework}}{\text{total cases}}$ |
| **First-time-right (FTR)** | Cases that run the happy path without rework or deviation | $\frac{\text{clean cases}}{\text{total cases}}$ |
| **Conformance rate** | Cases meeting all rules | $\frac{\text{compliant cases}}{\text{total cases}}$ |
| **Throughput time** | Case start to end (median and P90) | $\text{end} - \text{start}$ |
| **Cost per case** | Handling hours × rate + system cost | |
| **On-time rate** | Cases completed within the target | |

Do not **average percentages** across sites; compute the ratio of sums (see [[172 Tableau & Looker Studio - BI Tool Comparison]]). Report **median and P90** for time, since averages hide long tails. The **automation potential** of a step is high when it is **frequent, rule-based, digital-input, stable and low-exception**; mining quantifies these properties from the log (frequency, variants, user variety).

Link to lean: rework and waiting are lean wastes (see [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]]); to quality: first-time-right is the process-level analogue of the yield measures in [[008 Six Sigma & Quality Tools]].

### Example
Illustrative case: a bank back-office process handles 80,000 cases a month. Mining shows: touchless 31%, rework 14%, median throughput 6 days, P90 15 days. Target: touchless 45%, rework 8%. Value: moving 14 points of cases (11,200 cases) from manual handling of 25 minutes to touchless saves 11,200 × 25 / 60 = 4,667 hours a month, about 29 FTE at 160 hours; cutting rework from 14% to 8% removes 4,800 cases a month of repeat work (80,000 × 6%). Each is validated against the log after go-live, not assumed.

### In the news
See news box. Vendor claims such as "116k hours saved" are typical outcomes of automation KPIs; ask how baseline and counting rules were defined.

### Interview angle
> [!question] How it is asked
> "How would you measure whether an automation or process change actually worked?"

> [!tip] Strong answer includes
> - Baseline from the log before change; same definition after
> - Touchless rate, automation rate, rework, FTR, throughput (median and P90)
> - Control for volume and mix changes; watch for shifted effort elsewhere
> - Translate to hours or money with stated assumptions

---
## 10. Linking to RPA, Lean and Continuous Improvement
> 🟠 Tier 2 · _Key points:_ Find-fix-monitor loop; fix the process before automating; DMAIC; control tower

### Definition
**Loop:** (1) **Discover** the process with mining; (2) **diagnose** waste: waiting, rework, over-processing, errors (the lean wastes); (3) **simplify** and standardise first (eliminate steps, fix master data, change rules); (4) **automate** what remains with RPA or workflow where the volume and rule clarity justify it; (5) **monitor** KPIs continuously with alerts; (6) **act** through task assignment or bot triggers. This is the process-level version of DMAIC ([[008 Six Sigma & Quality Tools]]) and kaizen ([[007 Lean Manufacturing]]).

Principle: **do not automate a broken process**; automating a 14-variant process hardcodes the exceptions. **Select RPA candidates** with mining: high volume, rule-based, structured inputs, few exceptions, stable system interfaces; use **task mining** to find manual copy-paste work between systems.

**Operations intelligence in practice:** monitoring boards by process owner with thresholds (for example PO-after-invoice above 5% triggers a review), **alerts** on stuck cases (invoice blocked more than 3 days), and **process simulation** to forecast the effect of a policy change before rollout. Combine with a **control tower** view for supply chains ([[047 MIS & Dashboard Design]]).

Governance: a **process owner** per end-to-end process, a **centre of excellence** (CoE), a benefits tracker (see benefits realisation in [[170 Programme, Portfolio & PMO Management]]) and change management so that findings turn into action instead of reports.

### Example
Illustrative invoice processing case: mining shows 14 variants, with 6 variants (9% of cases) caused by PO price mismatches. Step 1 fix price master data (reduces mismatches by half), step 2 define a tolerance rule (auto-approve differences below 1% or ₹500), step 3 automate three-way match with a bot for compliant cases, step 4 monitor "first-time-right invoices" weekly. Result in the model: FTR rises from 62% to 81%. Had the bot been built first, it would have processed 6 exception paths with manual fallbacks and cost more to maintain.

### In the news
See news box. UiPath's closed loop (mining insights to orchestration, execution data back to mining) and Celonis' agent-ready context reflect the same find-fix-monitor cycle.

### Interview angle
> [!question] How it is asked
> "How does process mining help decide what to automate with RPA?"

> [!tip] Strong answer includes
> - Candidates by volume, variability, rule clarity, digital inputs
> - Simplify first, then automate; rework and exceptions as the warning sign
> - Measure the effect with the same KPIs after rollout
> - Lean wastes and DMAIC as the improvement logic

---
## 11. Data Preparation, Limitations and Privacy
> 🟠 Tier 2 · _Key points:_ Extraction effort; case notion; timestamps; convergence/divergence; sampling; DPDP

### Definition
**Data preparation** is typically the largest part of a mining project: identify the process and tables, extract (full history or time window), **transform** into case-activity-timestamp form, clean (duplicate events, missing timestamps, time zones), **enrich** (master data: vendor, plant, value) and **validate** with business users (do the case counts match system reports?). See [[175 Data Quality, Master Data & Data Governance]] and cleaning methods in [[186 Python Data Cleaning & EDA Playbook]].

**Typical problems:**
- **Timestamp quality:** date-only fields (no order inside a day), batch postings (all events at midnight), system vs user time.
- **Case notion and one-to-many:** convergence (one event belongs to many cases) and divergence (the same activity repeated within one case); wrong choice distorts counts. **Object-centric** approaches handle multiple objects (order, item, delivery) at once.
- **Missing or off-system events:** phone approvals, email, paper steps are invisible.
- **Logging granularity:** too fine (every field edit) or too coarse; activity naming inconsistent.
- **Selection bias:** only completed cases included; ongoing cases and cancellations missing.
- **Spaghetti models** from unfiltered data; **over-interpretation** of correlation.
- **Performance and cost** of loading hundreds of millions of events.
- **Change management:** mining may be perceived as employee monitoring.

**Privacy and compliance:** event logs contain **user IDs**, so employee data is personal data. In India the **Digital Personal Data Protection Act, 2023** applies; use pseudonymised users, role-level analysis, defined purpose and retention, and works-council or HR consultation where needed (GDPR for European data). Check data-residency requirements.

### Example
Illustrative pilot: it extracts 6 months of SAP P2P data: 1.2 million events, 210,000 POs. Validation shows that mining counts 210,000 POs but the ERP report counts 214,500; the 4,500 gap (2.1%) are POs with deleted items and no goods-receipt events. After agreeing treatment, the team logs the exclusion rule. Another check: 18% of Goods Receipt events have midnight timestamps because of batch posting, so waiting times to GR are computed in whole days only. These caveats are documented on the dashboard so users do not over-read hourly differences.

### In the news
See news box. As process data becomes input to AI agents, data quality and privacy of event data become governance issues, not just analytics ones.

### Interview angle
> [!question] How it is asked
> "What are the risks or limits of process mining?"

> [!tip] Strong answer includes
> - Dependent on logged data; invisible off-system work; timestamp and case-notion problems
> - Data extraction effort and validation against system reports
> - Privacy: personal data in logs, DPDP Act 2023, pseudonymisation
> - Findings need process-owner interpretation and an action path

---
## 12. Business Case and Implementation Roadmap
> 🟠 Tier 2 · _Key points:_ Benefit levers, cost, payback, pilot-first, adoption

### Definition
**Benefit levers:** (1) **efficiency** (touchless rate, handling hours), (2) **working capital** (earlier cash collection, optimised payment timing, lower inventory from shorter lead times), (3) **cost avoidance** (duplicate payments, penalties, expedites), (4) **revenue** (higher OTIF, lower order loss), (5) **compliance** (audit effort, fines). **Costs:** licences, data engineering, implementation partner, internal time, change management, cloud.

**Roadmap:** (1) pick one process with executive sponsor and a measurable pain; (2) 8 to 12 week **pilot** with defined KPIs and baseline; (3) quantify the opportunity; (4) scale to adjacent processes and plants; (5) embed in operations (alerts, owners); (6) track benefits. Governance as in [[170 Programme, Portfolio & PMO Management]] and [[042 Cost & Budget Management]]. Use NPV or payback ([[109 Valuation Basics (NPV, IRR, DCF)]]).

### Example
P2P programme at a company with 200,000 POs a year (all in ₹ lakh):
- Rework cut from 18% to 10%: $200{,}000 \times 8\% \times ₹600 = ₹96$ lakh.
- Late-payment penalties and duplicate payments avoided: ₹40 lakh (estimate from an audit sample).
- Touchless rate up 20 points (40,000 POs) saving 12 minutes at ₹300 an hour: $40{,}000 \times 0.2 \times 300 = ₹24$ lakh.
- **Total benefit: ₹160 lakh per year.**
- Costs: year 1 ₹180 lakh (licence 120 + implementation 60), years 2 and 3 ₹120 lakh each.
Net: year 1 = -20, year 2 = +40, year 3 = +40; cumulative = -20, +20, +60. **Payback about 1.5 years**; 3-year ROI = (480 - 420) / 420 = **14.3%**. The case is modest on efficiency alone; improving it requires bigger levers (working capital release, revenue protection) or scaling to O2C. Sensitivity: if rework falls only to 14%, benefit falls by ₹48 lakh and the case turns negative (3 × 112 = 336 vs 420 cost).

### In the news
See news box. Vendors cite multi-million benefits, but the business case should come from your own baseline and a pilot, not a vendor slide.

### Interview angle
> [!question] How it is asked
> "Make a business case for a process mining investment."

> [!tip] Strong answer includes
> - Benefit levers with formulas and conservative assumptions
> - Costs including data engineering and change management
> - Payback, ROI and sensitivity to the biggest assumption
> - Pilot-first approach with success criteria and a benefit tracker

---
## 13. ⭐ Advanced: Object-Centric Process Mining and Agentic Operations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Classical process mining** assumes one case notion per analysis, which forces flattening. **Object-centric process mining (OCPM)** records events linked to **multiple objects** (order, order item, delivery, invoice, material) in an **object-centric event log** (the OCEL format) and builds a model of the interplay of objects; it removes convergence and divergence errors, and lets the same data answer questions at different levels without re-extracting. Celonis and academic tools (including PM4Py) support object-centric approaches; check the specific feature set of the version you use.

**Beyond discovery:**
- **Predictive process monitoring:** predict remaining time, outcome (late or not) or next activity for running cases, using ML ([[094 ML Fundamentals & Workflow]]).
- **Simulation and digital twin of the organisation:** test the effect of a rule, headcount or automation change before rollout.
- **Prescriptive actions:** recommend next best action; trigger bots or workflows.
- **Agentic AI:** AI agents act on processes; they need **context** (the current state, rules, exceptions) and **guardrails** (conformance rules, approval limits). Celonis' Context Model (May 2026) is a commercial example of supplying that context.
- **Causal analysis:** distinguishing correlation from cause (for example whether a vendor causes delay or only supplies particular materials).
- **Sustainability:** estimate emissions per process path using activity and distance data.

Challenges: governance of AI actions, auditability, explainability, data privacy, change management, vendor lock-in.

### Example
A single order has 3 items shipped in 2 deliveries and invoiced once. In a classical log with **order** as the case, "Create Delivery" appears twice and "Create Invoice" once, so counts are inflated or ambiguous; with **item** as the case, the invoice is duplicated across 3 items. An object-centric log links the order, 3 items, 2 deliveries and 1 invoice, and answers "which deliveries were invoiced late?" and "how long from item creation to payment?" from one dataset. A predictive monitor on running orders flags those with a delivery-block pattern and a 70% probability of delay, and an agent proposes an expedite or a customer message, subject to approval limits.

### In the news
See news box. The Context Model launch and Ikigai acquisition (12 May 2026) show Celonis shifting from analysing logs to supplying live operational context, simulation and forecasting for AI agents.

### Interview angle
> [!question] How it is asked
> "Where is process mining going, and how does AI change it?"

> [!tip] Strong answer includes
> - Object-centric data model resolving case-notion problems
> - Prediction, simulation and prescriptive action layers
> - Agents need context and guardrails; conformance rules as controls
> - Honest caveats: data quality, privacy, auditability, hype versus measured benefit
