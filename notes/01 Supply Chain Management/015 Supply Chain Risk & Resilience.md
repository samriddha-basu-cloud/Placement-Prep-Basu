---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Supply Chain Risk & Resilience"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 12
---
# Supply Chain Risk & Resilience

⬅ [[014 Global SCM & Sustainability]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[016 Digital Supply Chain & Industry 4.0]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Types of SC Risk]]
2. [[#2. Risk Identification Tools]]
3. [[#3. Risk Mitigation Strategies]]
4. [[#4. Business Continuity Planning]]
5. [[#5. Supply Chain Visibility]]
6. [[#6. Supplier Risk Assessment]]
7. [[#7. Disruption Management]]
8. [[#8. SC Insurance & Contracts]]
9. [[#9. Control Tower Concept]]
10. [[#10. Reshoring & Redundancy]]
11. [[#11. ⭐ Advanced: Supply Chain Mapping and Time-to-Recover Analysis]]
12. [[#12. ⭐ Advanced: Resilience Economics and the Risk-Adjusted Network]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): single points of failure — Red Sea and Nexperia
> **Red Sea / Suez rerouting (from late 2023, analysed Jul 2024).** Maersk reports that going around the Cape of Good Hope raised average cargo travel distance by **9%**, Suez crossings fell by **66%**, and available shipping capacity was estimated **15–20% lower in Q2 2024**. ([Maersk](https://www.maersk.com/insights/resilience/2024/07/09/effects-of-red-sea-shipping))
> 
> **Nexperia chip crisis (Oct 2025).** The Dutch government seized Nexperia from its Chinese parent Wingtech in early Oct 2025; on 29 Oct Nexperia suspended wafer supply to its Dongguan facility. By 31 Oct ZF had cut shifts at its main electric-drivetrain plant and Nissan said its chip stock would last only until the first week of November. A cheap, concentrated component stopped car lines. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nexperia-conflict-spills-overseas-as-it-halts-exports-to-china-german-automotive-manufacturers-slow-production-due-to-semiconductor-shortages-from-dutch-chipmaker))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Types of SC Risk
> 🟠 Tier 2 · _Tracker hint:_ Demand, supply, process, environment, control risks

### Definition
Supply chain risk is the possibility of an event that stops the chain from meeting demand at acceptable cost. A common taxonomy (Christopher & Peck; Manuj & Mentzer) groups it into five areas:

| Type | What goes wrong | Examples |
|---|---|---|
| **Demand risk** | Forecast error, demand shocks, bullwhip | Sudden fall in orders, a viral spike |
| **Supply risk** | Supplier failure, quality, price, lead-time variation | Single-source part, supplier bankruptcy |
| **Process (internal) risk** | Breakdown of own operations | Machine failure, IT outage, strike |
| **Environmental risk** | External events | Floods, earthquakes, pandemics, war, tariffs |
| **Control risk** | Poor rules and decisions | Wrong order-batch rules, badly set safety stocks |

Risks are also split into **operational (frequent, low impact)** and **disruption (rare, high impact)** risks. Overall exposure $= P(\text{event}) \times \text{Impact}$, but rare-high-impact events need separate treatment because averages hide them.

### Example
An Indian two-wheeler maker: festive-season demand miss (demand), a single supplier of ECU chips (supply), paint-shop fire (process), Chennai floods cutting the port (environment), and a reorder point set from last year's average without adjusting for lead time (control).

### In the news
See news box. Red Sea is environmental/geopolitical risk; Nexperia is supply risk with a geopolitical trigger.

### Interview angle
> [!question] How it is asked
> "What kinds of risks does a supply chain face?" or "Classify the risks in this company's chain and prioritise."

> [!tip] Strong answer includes
> - Five categories with one example each, from the case company
> - Operational vs disruption risk distinction
> - Prioritisation by likelihood and impact, not a flat list
> - A link from each risk to a mitigation lever

---

## 2. Risk Identification Tools
> 🟠 Tier 2 · _Tracker hint:_ Risk matrix, FMEA for SC, bow-tie analysis

### Definition
- **Risk matrix (heat map):** score each risk for likelihood (1–5) and impact (1–5); score $= L \times I$; act first on the red cells.
- **FMEA (Failure Mode and Effects Analysis):** for each failure mode rate **Severity (S), Occurrence (O), Detection (D)**, each 1–10 (10 = worst, hardest to detect). 
$$RPN = S \times O \times D$$
Rank by RPN and attack the highest; recalculate after the fix.
- **Bow-tie:** centre = the top event (e.g., stock-out of critical part). Left side: causes and **preventive barriers**. Right side: consequences and **recovery barriers**. Good for communicating with non-specialists.
- Others: supply chain mapping to tier-n, scenario analysis, stress tests.

### Example
FMEA for a sole-source resin supplier: S = 8 (line stops), O = 4, D = 5 (we only learn at delivery). RPN $= 8 \times 4 \times 5 = 160$. After adding supplier-side inventory alerts D falls to 2: RPN $= 8 \times 4 \times 2 = 64$.

### In the news
See news box. Most carmakers could not see tier-2/3 exposure to Nexperia until supply stopped: a detection (D) failure in FMEA terms.

### Interview angle
> [!question] How it is asked
> "How would you identify and prioritise supply chain risks?"

> [!tip] Strong answer includes
> - Map the chain first (tiers, single points of failure)
> - Risk matrix for quick triage, FMEA RPN for ranking
> - Notes that RPN has flaws (equal weight to S, O, D; severity should dominate)
> - Moves from identification to owner, action and review date

---

## 3. Risk Mitigation Strategies
> 🟠 Tier 2 · _Tracker hint:_ Dual sourcing, safety stock, nearshoring, contracts

### Definition
Four classic responses: **avoid, reduce, transfer, accept**. Typical levers:
- **Dual / multi-sourcing:** split volume (e.g., 70/30) so a second supplier is already qualified.
- **Safety stock / strategic buffer:** $SS = z\,\sigma_d\sqrt{L}$ (demand variability); with lead-time variability add the lead-time term.
- **Nearshoring / regionalisation:** shorter, more controllable lead times.
- **Flexible capacity and postponement:** delay differentiation until demand is known.
- **Contracts:** capacity reservation, supply guarantees, penalty clauses, options.
- **Transfer:** insurance, hedging.
Mitigation costs money, so judge it by expected loss avoided versus cost.

### Example
Daily demand σ = 100 units, lead time 9 days, service level 95% (z = 1.65): $SS = 1.65 \times 100 \times \sqrt{9} = 495$ units. If lead time becomes 16 days (rerouting): $1.65 \times 100 \times 4 = 660$ units, i.e. +33% buffer.

### In the news
See news box. After a 9% longer route and 15–20% less capacity, firms raised buffers; after Nexperia, carmakers discussed standardising chips and qualifying second sources.

### Interview angle
> [!question] How it is asked
> "A key component comes from one supplier. What do you do?"

> [!tip] Strong answer includes
> - Quantify the exposure first (spend, revenue at risk, time to recover)
> - Mix of levers: second source, buffer, contract, redesign
> - Cost-of-insurance logic: pay for resilience where impact is highest
> - Qualification lead time for a new supplier (months) as a constraint

---

## 4. Business Continuity Planning
> 🟠 Tier 2 · _Tracker hint:_ BCP, disaster recovery, BC lifecycle

### Definition
**Business Continuity Planning (BCP)** keeps critical operations running (or restores them within an acceptable time) during and after a disruption. **Disaster Recovery (DR)** is the IT/data subset: restoring systems and data.

Key terms: **RTO** (Recovery Time Objective: maximum tolerable downtime), **RPO** (Recovery Point Objective: maximum tolerable data loss), **MTPD** (maximum tolerable period of disruption).

BC lifecycle (ISO 22301 style): understand the organisation → **Business Impact Analysis (BIA)** and risk assessment → choose continuity strategies → write plans (roles, call trees, alternate sites) → **test and exercise** → maintain and review. 

### Example
A pharma distributor's BIA shows the cold-chain control system's RTO is 2 hours and RPO 15 minutes; the BCP therefore needs a hot-standby server and a manual temperature-logging fallback at each depot.

### In the news
See news box. Firms with a pre-written playbook for a port or supplier loss reacted in days; others took weeks.

### Interview angle
> [!question] How it is asked
> "How would you build a business continuity plan for a plant?"

> [!tip] Strong answer includes
> - BIA first: which processes are critical and how fast must they recover (RTO)
> - Distinguish BCP vs DR
> - Alternate sites, supplier, labour, communication plan
> - Regular drills; a plan never tested is a hypothesis

---

## 5. Supply Chain Visibility
> 🟠 Tier 2 · _Tracker hint:_ Track-and-trace, control towers, real-time dashboards

### Definition
Visibility is knowing **where inventory, orders and shipments are, and their status, across tiers, in time to act**. Layers: **track-and-trace** (GPS, barcodes/RFID, carrier APIs, e-ways), **inventory visibility** (multi-node stock), **event visibility** (ETA changes, delays), **supplier visibility** (tier-2/3 mapping, financial and capacity signals).

Benefit comes only if data triggers action: visibility without response playbooks is only a dashboard. Key metrics: % shipments with live tracking, ETA accuracy, time-to-detect a disruption.

### Example
A Bengaluru electronics importer integrates carrier and port data. When a vessel is delayed by 6 days, the system flags the affected orders; the planner books partial air freight for the 10% of SKUs with stock below 4 days' cover.

### In the news
See news box. Nexperia exposed how little visibility exists beyond tier 1; Red Sea made ETA unpredictable and pushed visibility spending.

### Interview angle
> [!question] How it is asked
> "How can technology improve supply chain resilience?"

> [!tip] Strong answer includes
> - Visibility = data + analytics + decision rights
> - Beyond tier 1 mapping
> - Metrics: time-to-detect, time-to-recover
> - Cost-benefit and data-sharing incentives with suppliers

---

## 6. Supplier Risk Assessment
> 🟠 Tier 2 · _Tracker hint:_ Financial health, geographic concentration, dependency ratio

### Definition
Score suppliers on: **financial health** (liquidity, leverage, Altman-type Z-score, payment delays), **operational capability** (quality, capacity headroom, single plant), **geographic concentration** (share of spend in one country/region, natural-hazard exposure), **geopolitical/compliance** and **dependency**.

Dependency ratios (two-way):
- Our dependency $= \dfrac{\text{Spend with supplier on a part}}{\text{Total spend on that part}}$
- Their dependency $= \dfrac{\text{Our purchases}}{\text{Supplier's revenue}}$ (high = we have leverage but also may be their lifeline).
Combine with item criticality (Kraljic matrix, see [[002 Procurement & Strategic Sourcing]]).

### Example
A part is bought 85% from Supplier A in one industrial cluster. Our purchases are 40% of A's revenue and A's debt/EBITDA is 5.5×. Concentration high, supplier fragile, we are a big customer: a candidate for financial support, a second source, and a monitored early-warning list.

### In the news
See news box. Nexperia is the textbook case of one supplier and one geography behind a low-value part.

### Interview angle
> [!question] How it is asked
> "How would you assess the risk of your top 20 suppliers?"

> [!tip] Strong answer includes
> - Criteria set with weights (financial, operational, geography, ESG)
> - Segment by spend and criticality; focus on high-impact few
> - Early-warning triggers and monitoring cadence
> - Actions: dual source, contracts, supplier development

---

## 7. Disruption Management
> 🟠 Tier 2 · _Tracker hint:_ COVID-19 lessons, semiconductor shortage case study

### Definition
Disruption management is how a firm **detects, responds and recovers**. Useful concepts: the **disruption profile** (performance drops, then recovers over time); **time-to-recover (TTR)** and **time-to-survive (TTS)**: if TTR > TTS at a node, that node is critical. Resilience = ability to **resist, recover and adapt**.

Response phases: detect → assess impact → stabilise (allocate scarce supply to key customers, expedite, re-source) → recover → learn.

**COVID-19 lessons:** lean/JIT chains with single sourcing and long lead times failed; demand whipsawed (PPE, then consumer goods); visibility and flexible capacity mattered. **2020–23 chip shortage:** automakers cancelled orders in 2020, then found foundry capacity taken by electronics; the resulting production losses were large across the industry. Lesson: long-term agreements and direct relationships with chip suppliers.

### Example
During the shortage, carmakers prioritised chips for high-margin models; this is allocation based on contribution per scarce chip, a core disruption-response logic.

### In the news
See news box. Nexperia in 2025 re-opened the same lesson only five years after the first shortage.

### Interview angle
> [!question] How it is asked
> "What did COVID teach us about supply chains?" or "Walk me through how you would respond to a sudden supplier shutdown."

> [!tip] Strong answer includes
> - Structure: detect, assess, stabilise, recover, learn
> - TTR vs TTS concept to find critical nodes
> - Allocation rules for scarce supply
> - Lessons turned into permanent policy (buffers, dual source), not only a one-off fix

---

## 8. SC Insurance & Contracts
> 🟠 Tier 2 · _Tracker hint:_ Force majeure, penalties, SLAs, insurance coverage

### Definition
- **Force majeure:** clause excusing a party from performance for events beyond control (war, flood, pandemic). It depends on the wording: list of events, notice period, proof, duration after which termination is allowed. Under the Indian Contract Act, Section 56 (frustration/impossibility) is the fallback.
- **Penalties / liquidated damages (LDs):** pre-agreed compensation for delay or shortfall (e.g., 0.5% of contract value per week, capped at 10%).
- **SLAs:** measurable service levels (OTIF, lead time) with credits/penalties.
- **Insurance:** marine cargo, property, **business interruption (BI)** and **contingent BI (CBI)** that covers loss from a supplier's/customer's premises being damaged. Many policies need physical damage as the trigger, so pandemics and cyber events are often excluded or need special cover.
Contract design allocates risk to the party that can control it best.

### Example
A buyer's LD clause is 0.5% per week capped at 10% of a ₹2 crore order. A 6-week delay costs the supplier $6 \times 0.5\% = 3\%$ = ₹6 lakh; the cap would stop at 20 weeks.

### In the news
See news box. Nexperia cited non-payment under contract terms when suspending supplies; Red Sea raised disputes on who bears extra freight and war-risk premiums.

### Interview angle
> [!question] How it is asked
> "How can contracts reduce supply chain risk?"

> [!tip] Strong answer includes
> - Force majeure scope and its limits
> - SLAs with measurable KPIs and remedies
> - Insurance vs self-insurance (buffer) economics
> - Contract is a backstop; relationships and visibility prevent the loss

---

## 9. Control Tower Concept
> 🟠 Tier 2 · _Tracker hint:_ Centralized monitoring, alert management, response playbooks

### Definition
A **supply chain control tower** is a central capability (people + process + technology) that gives end-to-end visibility, detects exceptions, and **drives coordinated decisions**. Three levels of maturity: **see** (visibility) → **analyse/predict** (alerts, ETA prediction, impact simulation) → **act** (prescribed or automated actions).

Building blocks: integrated data (ERP, WMS, TMS, supplier, carrier), **alert rules** with thresholds and severity, **response playbooks** (who does what within how long), governance, and KPIs (alert-to-action time, % exceptions resolved within SLA).

### Example
Rule: if an inbound container ETA slips by more than 48 hours and cover is below 5 days, alert the planner; Severity 1 (cover below 2 days) goes to the head of supply chain with a playbook: air-freight 20% or reallocate stock from a nearby DC.

### In the news
See news box. Red Sea rerouting generated thousands of delayed ETAs at once, exactly the exception volume a control tower prioritises.

### Interview angle
> [!question] How it is asked
> "What is a control tower and how would you set one up?"

> [!tip] Strong answer includes
> - Visibility is not enough: alerts and playbooks
> - Data integration challenge and phased scope (start with top lanes/SKUs)
> - Clear roles and authority
> - KPIs and benefits (fewer expedites, faster response)
> - See also [[016 Digital Supply Chain & Industry 4.0]] for the technology view

---

## 10. Reshoring & Redundancy
> 🟠 Tier 2 · _Tracker hint:_ Cost vs resilience; strategic inventory; buffer capacity

### Definition
**Reshoring/nearshoring** moves production closer to home or demand; **redundancy** adds spare capacity, stock or suppliers that are idle in normal times. The core trade-off: efficiency (lean) vs resilience (slack). Total-cost view:
$$TCO = \text{price} + \text{freight} + \text{duties} + \text{inventory carrying} + \text{risk cost}$$
where risk cost $= P(\text{disruption}) \times \text{loss per event}$.

Forms of redundancy: **strategic inventory** (for critical, long-lead items), **buffer capacity** (spare shifts, surge contracts), **backup suppliers/sites**. Redundancy is worth it where impact is high and cost is low: tailor by SKU criticality, not blanket.

### Example
Offshore unit cost ₹100 + freight/duty/carrying ₹18 = ₹118; local supplier ₹125. Add an expected disruption loss of ₹10 per unit for the offshore source (probability times loss, spread over annual volume): effective offshore cost is 118 + 10 = ₹128 vs ₹125 local, so local wins despite the higher quoted price.

### In the news
See news box. India's push for local electronics and chips is reshoring/China+1 in action (also see [[019 Facility Layout & Location]]).

### Interview angle
> [!question] How it is asked
> "Should the company bring manufacturing back home?"

> [!tip] Strong answer includes
> - Total cost with risk term, not unit price alone
> - Selective redundancy for critical items
> - Non-cost factors: skills, ecosystem, incentives (PLI), time to build
> - Hybrid answer: dual footprint (China+1)

---

## 11. ⭐ Advanced: Supply Chain Mapping and Time-to-Recover Analysis
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Supply chain mapping** documents suppliers beyond tier 1 for critical products (who makes the sub-component, where, with what alternatives). **Time-to-Recover (TTR)** is how long a node takes to be back at full function; **Time-to-Survive (TTS)** is how long the chain can keep fulfilling demand without that node (Simchi-Levi, MIT Risk Exposure Index). Risk Exposure Index $= \max_i \text{(impact when node } i \text{ is down)}$ considering TTR vs TTS.

Rule: if $TTR_i \le TTS_i$, the node is not an immediate threat; if $TTR_i > TTS_i$, loss begins. Mitigation is ranked by the gap $TTR - TTS$ and the revenue per day.

### Example
Part X: inventory covers 21 days of demand (TTS = 21). The single supplier needs 60 days to restart (TTR). Gap = 39 days of lost output. Mitigation options: raise buffer by 39 days (costly) or qualify a second source in 25 days, cutting the gap to $\max(0, 25-21) = 4$ days with a modest top-up.

### In the news
See news box. Nexperia: carmakers had only days to weeks of chip stock against an uncertain restart time, a negative TTS-TTR gap.

### Interview angle
> [!question] How it is asked
> "How would you decide which supplier risks to fix first?"

> [!tip] Strong answer includes
> - TTR vs TTS comparison per node
> - Revenue at risk per day times the gap
> - Differentiate "high-probability, low-impact" from "low-probability, high-impact"
> - Mapping depth: tier-2/3 for critical parts only

---

## 12. ⭐ Advanced: Resilience Economics and the Risk-Adjusted Network
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Resilience investments are justified by **expected loss avoided** (and by option value). Basic framework:

$$\text{Net benefit} = \sum_{events} P_e \times (\text{Loss without} - \text{Loss with mitigation}) - \text{annual mitigation cost}$$

Include: lost margin, expediting, penalties, and long-term customer loss. **Segment** the portfolio: for each SKU class pick efficient, buffered or dual-sourced strategy by criticality and volatility. Also consider **Value-at-Risk (VaR)** style stress tests ("what if the top port closes for 30 days?") and **scenario planning**, because probabilities are unknown for rare events.

### Example
Mitigation (second source + extra stock) costs ₹80 lakh/year. A disruption with 8% annual probability would cost ₹12 crore without it and ₹3 crore with it. Expected benefit $= 0.08 \times (12 - 3) = ₹0.72$ crore = ₹72 lakh < ₹80 lakh: marginally not worth it on expectation alone. But adding reputation loss of ₹2 crore (benefit +₹16 lakh) turns it positive (₹88 lakh), so the decision is sensitive to assumptions.

### In the news
See news box. Both shocks show how a cheap, concentrated link can carry very large losses; the probability and loss numbers in any business case remain judgement, so test them with sensitivity analysis.

### Interview angle
> [!question] How it is asked
> "Is it worth paying more for a resilient supply chain?"

> [!tip] Strong answer includes
> - Expected-loss framework and key assumptions
> - Sensitivity analysis on probability and impact
> - Segmented approach, not blanket buffering
> - Mention of option value and intangible loss

---
## 🔗 Go deeper: expansion notes
- [[141 Supply Chain Disruption Case Library (2011-2026)|Supply Chain Disruption Case Library (2011-2026)]]
- [[137 Supply Chain Contracts & Game Theory|Supply Chain Contracts & Game Theory]]
- [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies|Outsourcing, Supplier Partnerships & Kraljic Strategies]]
