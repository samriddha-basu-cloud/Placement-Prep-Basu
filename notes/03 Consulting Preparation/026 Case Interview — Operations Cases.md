---
tags: [consulting-preparation, tier1]
area: Consulting Preparation
topic: "Case Interview — Operations Cases"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 10
---
# Case Interview — Operations Cases

⬅ [[025 Case Interview — Profitability]] · [[_Index - Consulting Preparation|Consulting Preparation]] · [[027 Case Interview — Market Entry]] ➡

> **Area:** Consulting Preparation · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Operations Case Types]]
2. [[#2. Operations Case Structure]]
3. [[#3. Lean in Operations Cases]]
4. [[#4. Capacity Case Approach]]
5. [[#5. Supply Chain Case Structure]]
6. [[#6. Quality Improvement Cases]]
7. [[#7. Digital Operations Cases]]
8. [[#8. Automotive SCM Cases]]
9. [[#9. ⭐ Advanced: Little's Law, Utilisation and Queuing in Process Cases]]
10. [[#10. ⭐ Advanced: Supply Risk and Resilience Cases (Dual Sourcing, Buffers, Visibility)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): a single chip halts car lines; CEAT scales via acquisition; Blinkit rebuilds its inventory model
> **Nexperia chip crisis (Oct 2025).** After the Dutch government took control of chipmaker Nexperia from its Chinese parent Wingtech (early Oct 2025), Nexperia suspended wafer supply to its Dongguan plant on 29 Oct; by 31 Oct suppliers such as ZF were cutting shifts and Nissan said its chip stock lasted only "until the first week of November". A cheap, single-sourced component stopped car lines. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nexperia-conflict-spills-overseas-as-it-halts-exports-to-china-german-automotive-manufacturers-slow-production-due-to-semiconductor-shortages-from-dutch-chipmaker))
>
> **CEAT Q2 FY26 (Jul–Sep 2025).** Revenue **₹3,772.7 crore (+14.2%)**, EBITDA margin **13.5%**, driven by OEM and international demand; CEAT acquired **Camso's Off-Highway tyre and tracks business in Sept 2025**, lifting finance costs **30.9% to ₹87 crore**. Capex in the quarter **₹423 crore**. ([HDFC Sky](https://hdfcsky.com/news/ceat-q2fy26-profit-jumps-52-9-percent-yoy-to-rs-185-7-crore))
>
> **Blinkit Q3 FY26.** Adjusted EBITDA **₹4 crore profit vs ₹156 crore loss** the quarter before; **2,027 dark stores**; about **90% of net order value on company inventory** (an inventory-led model). ([Inc42](https://inc42.com/buzz/eternal-q3-blinkit-hyperpure-achieve-adjusted-ebitda-profitability/))
>
> **Tata Steel and Google Cloud (reported Sept 2025).** AI-based predictive maintenance using IoT sensors at European sites; improved reliability reported but without quantified savings. ([WebProNews](https://www.webpronews.com/tata-steel-teams-up-with-google-cloud-for-ai-driven-predictive-maintenance/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Operations Case Types
> 🔴 Tier 1 · _Tracker hint:_ Cost reduction, process improvement, supply chain, capacity

### Definition
Operations cases test your ability to improve how a business produces and delivers. Common types:
| Type | Typical question | Core tools |
|---|---|---|
| **Cost reduction** | "Cut unit cost by 15%" | Cost tree, benchmark, procurement, lean |
| **Process improvement** | "Cycle time is too long / defects too high" | Process map, bottleneck, lean, Six Sigma |
| **Supply chain** | "Fix stock-outs / design the network" | Network, inventory, supplier, logistics levers |
| **Capacity** | "Should we expand? Make or buy?" | Utilisation, demand forecast, break-even |
| **Quality** | "Defects rising" | DMAIC, cost of quality |
| **Digital / automation** | "Should we automate / implement ERP?" | ROI, change management |
| **Location / entry** | "Where to build the plant?" | Cost, access, risk |
Cross-cutting: quantify, find the **bottleneck**, consider **people and change**, and sanity-check feasibility (cost to implement, time, risk).

### Example
Prompts and the first move: "A bakery chain's delivery costs have risen 25%": cost tree (fuel, drivers, vehicles, routes, volume). "A hospital's discharge takes 6 hours": process map and bottleneck. "A tyre maker faces stock-outs in replacement channel": supply chain (forecast, plant scheduling, distribution inventory).

### In the news
See news box. Each news item is a case type: Nexperia (supply chain risk), CEAT (capacity/expansion through acquisition), Blinkit (network and inventory model), Tata Steel (maintenance/digital).

### Interview angle
> [!question] How it is asked
> "Our client, a manufacturer, is losing money on a plant. What would you do?" (type is not announced; you identify it)

> [!tip] Strong answer includes
> - Identify the case type and adapt the structure
> - Operational metrics (cost per unit, OEE, lead time, OTIF)
> - Quantify the opportunity and the cost to capture it
> - Include people, change and risk in the recommendation

---

## 2. Operations Case Structure
> 🔴 Tier 1 · _Tracker hint:_ Process map → identify bottleneck → quantify impact → solution

### Definition
Four-step skeleton:
1. **Clarify and map the process** end to end (inputs, steps, outputs), with volumes, cycle times, and resources at each step.
2. **Identify the bottleneck** (lowest capacity step, longest queue, highest utilisation) and the metrics gap (cost, time, quality). Throughput of the line equals the bottleneck's capacity.
3. **Quantify the impact:** how much output, cost or revenue is lost? Use rate × time × value.
4. **Solutions and implementation:** options (eliminate, simplify, add capacity, automate, re-sequence), evaluate on impact, cost, time, risk; plan a pilot and KPIs.
Capacity of a step = (number of resources × available time) / time per unit. **Utilisation** = demand rate / capacity; above ~85% queues grow fast. Add checks on quality (yield) and upstream/downstream effects (moving the bottleneck).

### Example
Order-processing line: entry takes 10 min/order (2 staff), checking 15 min (2 staff), packing 25 min (2 staff). Capacities per hour: entry 2 × 6 = 12; checking 2 × 4 = 8; packing 2 × 60/25 = 4.8. **Bottleneck = packing, 4.8 orders/h.** Demand is 6 orders/h: lost 1.2 orders/h; at ₹500 margin and 8 hours = 1.2 × 8 × 500 = ₹4,800 per day. Options: add a packer (3 staff: 7.2/h) — then checking (8/h) is next; cost of a packer ₹1,000/day vs gain ₹4,800: worth it.

### In the news
See news box. Blinkit's store-level process (receive, put-away, pick, pack, dispatch) has a bottleneck at picking during peaks; moving to company inventory shifts the constraint to purchasing and replenishment.

### Interview angle
> [!question] How it is asked
> "A plant produces 800 units a day against capacity of 1,000. Why?"

> [!tip] Strong answer includes
> - Process map with times and capacities
> - Bottleneck identification with numbers
> - Value of one unit of lost throughput
> - Solutions ranked, with the next bottleneck anticipated

---

## 3. Lean in Operations Cases
> 🔴 Tier 1 · _Tracker hint:_ 7 wastes identification; VSM in case context

### Definition
**Lean** maximises customer value by eliminating **waste (muda)**. The **7 wastes (TIMWOOD):** **T**ransport, **I**nventory, **M**otion, **W**aiting, **O**verproduction, **O**ver-processing, **D**efects. Some add an eighth: unused talent (skills).

**Value Stream Mapping (VSM):** map material and information flow from supplier to customer; for each step record cycle time, changeover, uptime, inventory/WIP (in days) between steps. Totals: **Value-added time** (VA) and **total lead time** (LT). **Process cycle efficiency** = VA / LT; typical is under 5–10% in unimproved processes. Create a **future-state map** with flow, pull (kanban), levelled production (heijunka), standard work.

In a case: ask "where does the product wait?" The queues (inventory) usually hold most of the lead time; attack waiting and batch size, not only worker speed.

### Example
A job takes 6 days (48 working hours) from order to dispatch; actual hands-on time = 2.4 hours. PCE = 2.4 / 48 = **5%**. Waiting between steps is 45.6 hours. Cutting batch size and adding a pull signal between steps reduces waiting by half to ~22.8 hours; new lead time = 25.2 hours; PCE = 2.4/25.2 = 9.5%; customer lead time falls from 6 to ~3 days.

### In the news
See news box. Nexperia showed the weakness of lean without resilience: lean inventories left car lines with days, not weeks, of chip stock (Nissan's cited stock "until the first week of November").

### Interview angle
> [!question] How it is asked
> "A factory has long lead times and high WIP. How would you apply lean?"

> [!tip] Strong answer includes
> - Name wastes and map where they occur
> - Use VSM numbers (VA vs lead time)
> - Pull, batch-size reduction, 5S, standard work
> - Balance lean with resilience; people and change management

---

## 4. Capacity Case Approach
> 🔴 Tier 1 · _Tracker hint:_ Utilization analysis; make vs buy; outsource decision

### Definition
1. **Demand:** forecast by product/segment; peak vs average; seasonality.
2. **Capacity:** nameplate vs effective capacity (after downtime, changeovers, yield): effective = nameplate × OEE.
3. **Utilisation** = demand / effective capacity. Under 70% means idle fixed cost; above 90% means little flexibility.
4. **Options:** debottleneck, add shifts, add machines or plant, outsource/subcontract, change product mix, reduce demand variability.
5. **Make vs buy:** relevant costs only. Break-even volume $Q^*=\dfrac{FC_{make}}{P_{buy}-VC_{make}}$; above $Q^*$ make, below buy. Add strategic factors: quality, IP, supplier risk, flexibility, lead time, capacity availability.
6. **Capex decision:** payback, NPV, risk (demand shortfall), phasing of capacity.

### Example
Annual demand 120,000 units. Buy price ₹100. Make: fixed cost ₹20 lakh per year, variable ₹80 per unit.
- Break-even: 20,00,000 / (100 − 80) = **100,000 units**.
- At 120,000 units: make = 20,00,000 + 120,000 × 80 = ₹1.16 crore; buy = 120,000 × 100 = ₹1.20 crore. Make saves ₹4 lakh.
If demand were 80,000: make = 20L + 64L = ₹84 lakh; buy = ₹80 lakh, so buy. Qualitative check: supplier reliability and quality; making holds the capacity risk.

### In the news
See news box. CEAT's Q2 FY26 capex of ₹423 crore and the Camso acquisition are capacity decisions (build vs buy capacity), with a visible finance-cost trade-off.

### Interview angle
> [!question] How it is asked
> "Should the client build a second plant or outsource the extra volume?"

> [!tip] Strong answer includes
> - Effective capacity and utilisation, not just nameplate
> - Break-even analysis for make vs buy
> - Qualitative: control, risk, flexibility, IP, lead time
> - Phasing and a downside scenario

---

## 5. Supply Chain Case Structure
> 🔴 Tier 1 · _Tracker hint:_ Network design, inventory, supplier, logistics levers

### Definition
Structure by supply chain stages and levers (**Plan, Source, Make, Deliver, Return** from SCOR) or by the six drivers (facilities, inventory, transportation, information, sourcing, pricing):
- **Network design:** number and location of plants/DCs; cost vs service; centralise or decentralise.
- **Inventory:** safety stock, service level, SKU segmentation (ABC/XYZ), turns, obsolescence. Safety stock $SS=z\sigma_d\sqrt{L}$.
- **Suppliers:** concentration, dual sourcing, lead time, quality, cost, risk.
- **Logistics:** mode, routes, load factor, last mile, warehouse productivity.
- **Planning:** forecast accuracy, S&OP, information sharing.
Diagnose with KPIs: OTIF, fill rate, inventory days, cost to serve, cash-to-cash. Always trade off cost and service level, and quantify.

### Example
Daily demand standard deviation 50 units, lead time 9 days, service level 95% ($z=1.65$): $\sigma_L=50\sqrt9=150$; SS = 1.65 × 150 = **247.5 ≈ 248 units**. Raising the service level to 99% ($z=2.33$) makes SS = 350 units (+41%) for 4 points more availability. The case answer: segment SKUs: 99% only for the top A-items, 95% for the rest.

### In the news
See news box. Nexperia is a supply-chain case in miniature: single-sourced low-cost component, thin buffer, tier-2 visibility gap; Blinkit's move to company inventory changes who holds the inventory risk.

### Interview angle
> [!question] How it is asked
> "A retailer has frequent stock-outs and high inventory at the same time. Why, and what do you do?"

> [!tip] Strong answer includes
> - Structured by network, inventory, supplier, logistics, planning
> - Likely cause: wrong inventory in wrong place; poor forecast and segmentation
> - Quantified levers (safety stock, service level targets)
> - Data requests: demand variability, lead times, SKU-level service levels

---

## 6. Quality Improvement Cases
> 🔴 Tier 1 · _Tracker hint:_ DMAIC application; cost of quality framework

### Definition
**DMAIC** (Six Sigma): **D**efine (problem, scope, customer CTQ), **M**easure (baseline defect rate, DPMO, measurement-system check), **A**nalyse (Pareto, fishbone, 5 Whys, regression to find root cause), **I**mprove (solutions, DOE, poka-yoke, pilot), **C**ontrol (control charts, SOPs, audits). $DPMO=\dfrac{defects}{units\times opportunities}\times10^6$; 3.4 DPMO is "six sigma" (with the 1.5-sigma shift convention).

**Cost of Quality (COQ):** conformance costs = **prevention** (training, design, planning) + **appraisal** (inspection, testing); non-conformance = **internal failure** (scrap, rework) + **external failure** (returns, warranty, recalls, reputation). Heuristic "1-10-100": the cost of fixing a defect rises roughly tenfold at each later stage. Invest more in prevention to reduce failure costs.

### Example
Plant makes 100,000 units; defect rate 4%; rework cost ₹150 per defect. COQ (internal failure) = 4,000 × 150 = ₹6 lakh. DMAIC finds a misaligned fixture causing 60% of defects. Fixing it (₹1 lakh one-off): defect rate falls to 1.6% (4% × 0.4), rework cost = 1,600 × 150 = ₹2.4 lakh; saving ₹3.6 lakh a year, payback = 1/3.6 ≈ 0.28 years (about 3.3 months).

### In the news
See news box. Predictive maintenance (Tata Steel, Indian Railways) is a quality and reliability prevention cost; and CEAT's product mix (premium tyre launches) relies on process capability for OEM acceptance.

### Interview angle
> [!question] How it is asked
> "Defect rates at a plant doubled. How would you approach it?"

> [!tip] Strong answer includes
> - Define and measure first; Pareto the defect types
> - Root cause tools (5 Whys, fishbone, data)
> - Cost of quality logic and payback
> - Sustain: control plan, training, supplier quality

---

## 7. Digital Operations Cases
> 🔴 Tier 1 · _Tracker hint:_ Automation ROI; ERP implementation case

### Definition
**Automation ROI:** $ROI=\dfrac{\text{annual benefit}-\text{annual operating cost}}{\text{investment}}$, **payback** = investment / net annual benefit, plus NPV for multi-year. Include benefits (labour saved, yield, quality, throughput, safety) and costs (capex, integration, maintenance, training, downtime during installation). Consider flexibility, technology risk, and redeployment of staff.

**ERP implementation cases** (e.g. SAP S/4HANA): business case (integrated data, process standardisation, visibility), phases (blueprint, build, test, data migration, cut-over, hypercare), risks (scope creep, bad master data, customisation overload, resistance, go-live disruption, cost overrun). Principles: process first, clean data, strong sponsorship, fit-to-standard, phased rollout, change management and training. Failure example class: stock-out and billing problems at go-live.

### Example
Automate packing: investment ₹2 crore. Saves 10 operators × ₹4 lakh = ₹40 lakh and reduces errors by ₹10 lakh; maintenance and licences ₹8 lakh per year. Net benefit = 40 + 10 − 8 = ₹42 lakh. Payback = 200/42 = **4.8 years**. Marginal, so test throughput gains, or phase automation to bottleneck lines.

### In the news
See news box. Tata Steel's predictive maintenance and Blinkit's inventory-led tech stack are digital operations moves; for the Tata Steel item, the source gives no quantified benefit, so ROI there is unverified.

### Interview angle
> [!question] How it is asked
> "Should the client invest ₹X crore in automation?" or "How would you de-risk an ERP rollout?"

> [!tip] Strong answer includes
> - ROI/payback with all costs and benefits
> - Process before technology; data readiness
> - Risks and change management (training, resistance, downtime)
> - Phased pilot with measurable KPIs

---

## 8. Automotive SCM Cases
> 🔴 Tier 1 · _Tracker hint:_ JIT, tier supplier management; CEAT/JBM context

### Definition
Automotive supply chains are tiered: **OEM → Tier 1 (modules/systems) → Tier 2 (components) → Tier 3 (materials)**. Practices: **JIT/JIS** (just-in-time, just-in-sequence), **kanban** pull, milk runs, supplier parks near OEM plants, vendor-managed inventory, long-term contracts with annual price-downs, supplier development and quality (PPAP, IATF 16949).

$$\text{Takt time}=\frac{\text{available time}}{\text{customer demand}},\qquad \text{Kanbans}=\frac{D\times L\times(1+\alpha)}{C}$$
($D$ demand rate, $L$ replenishment lead time, $\alpha$ safety factor, $C$ container size.)

Trade-offs: JIT cuts inventory but increases exposure to disruption; single sourcing cuts cost but concentrates risk (see Nexperia). **Context:** CEAT (tyre maker; supplies OEMs and the replacement market, which differ in volume predictability and margin) and JBM (auto components and buses): in cases, OEM business needs delivery reliability and price-downs; replacement needs wide distribution.

### Example
Plant demand 900 units per shift; available time 450 minutes = 27,000 s: takt = 27,000 / 900 = **30 s**. Kanban for a part: demand 60/hour, replenishment lead time 0.5 hour, safety factor 10%, container 10: kanbans = 60 × 0.5 × 1.1 / 10 = 3.3, so **4 cards**. A one-day disruption at a single-source supplier with 2 hours of line-side stock stops the line in 2 hours, so critical parts need buffer or dual sourcing.

### In the news
See news box. Nexperia: a low-value chip stopped lines because of single sourcing and thin buffers; CEAT's OEM growth and Camso deal add scale but also finance cost.

### Interview angle
> [!question] How it is asked
> "An auto OEM faces frequent line stoppages due to supplier delays. What would you do?" or "How should a tyre maker balance OEM and replacement channels?"

> [!tip] Strong answer includes
> - Tier structure and where the failure sits (supplier, logistics, planning)
> - JIT trade-offs: buffer for critical or single-source parts
> - Supplier development, dual sourcing, visibility to tier 2
> - Channel differences (OEM: reliability and price-downs; replacement: distribution and inventory)

---

## 9. ⭐ Advanced: Little's Law, Utilisation and Queuing in Process Cases
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Little's Law:** $WIP = Throughput \times Cycle\ time$ (flow time). It holds for any stable system. **Utilisation** $\rho=\lambda/\mu$; queue delay grows non-linearly: for M/M/1, average time in queue $W_q=\dfrac{\rho}{\mu(1-\rho)}$ and number in system $L=\dfrac{\rho}{1-\rho}$. Therefore, running a resource at 95% rather than 80% multiplies waiting about 4.75 times. **Implications:** cut cycle time by cutting WIP (smaller batches, pull), reduce variability, and keep buffer capacity at constraints. Also **Kingman's formula** (waiting time ~ utilisation/(1−utilisation) × variability).

### Example
A hospital: 40 patients/hour discharged on average (throughput), 200 patients in the system (WIP): flow time = 200 / 40 = **5 hours**. Target 3 hours at the same throughput requires WIP = 40 × 3 = 120: cut 80 patients (reduce queues at pharmacy and billing). Utilisation: M/M/1 at ρ = 0.8, L = 0.8/0.2 = 4; at ρ = 0.95, L = 19.

### In the news
See news box. Blinkit's operating model (10-minute promise) depends on keeping dark-store pick capacity well below saturation; a rise in utilisation raises waiting non-linearly.

### Interview angle
> [!question] How it is asked
> "Why does adding 10% more demand double our waiting times?"

> [!tip] Strong answer includes
> - Little's Law and the utilisation-delay curve
> - Reduce variability; add flexible capacity at peaks
> - Quantified example
> - Cost of buffer vs cost of waiting

---

## 10. ⭐ Advanced: Supply Risk and Resilience Cases (Dual Sourcing, Buffers, Visibility)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Risk case structure: **Identify** (map tiers, find single points of failure, concentration by country/supplier), **Assess** (probability × impact; criticality of part; time to recover, TTR; time to survive, TTS), **Mitigate** (dual or multi-sourcing, buffer stock for critical low-cost items, qualify alternates, regional diversification/China+1, contract clauses, visibility tools), **Monitor** (early-warning, scenario drills). Compare **expected loss avoided** against **cost of mitigation**: Expected annual loss = probability × impact. Resilience gap exists when TTR > TTS. Segment parts (Kraljic matrix): bottleneck/critical items justify buffers even if cheap.

### Example
A chip with a 5% yearly chance of a 3-week stoppage, loss of ₹200 crore per event: expected loss ₹10 crore/year. Mitigation: qualify a second supplier (₹1.5 crore/yr extra cost) and hold 4 weeks of buffer (inventory ₹6 crore at 12% carrying cost = ₹0.72 crore/yr). Total ≈ ₹2.2 crore/yr, far below ₹10 crore, so mitigation is worthwhile even though the chip itself is cheap. (Illustrative numbers.)

### In the news
See news box. Nexperia (Oct 2025) is the live example: stock cover of days, tier-2 exposure not mapped, single-source dependence.

### Interview angle
> [!question] How it is asked
> "How would you protect a carmaker against chip shortages?"

> [!tip] Strong answer includes
> - Map and rank critical parts; TTR vs TTS
> - Options with cost-benefit: buffer, dual source, redesign
> - Visibility into tier-2 and tier-3
> - Governance: risk owner and regular stress tests

---
## 🔗 Go deeper: expansion notes
- [[158 Operations Management Interview Question Bank & Numericals|Operations Management Interview Question Bank & Numericals]]
- [[149 Queueing Theory & Waiting-Line Analysis|Queueing Theory & Waiting-Line Analysis]]
- [[160 Case Interview - Cost Reduction, Turnaround & Pricing|Case Interview - Cost Reduction, Turnaround & Pricing]]
