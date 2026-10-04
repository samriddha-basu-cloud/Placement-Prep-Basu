---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Warehouse Labour, WES-WCS & Yard Management"
tier: Tier 2
roles: Operations
status: complete
subtopics: 13
---
# Warehouse Labour, WES-WCS & Yard Management

⬅ [[127 Warehouse Engineering - Racking, Sizing & Material Handling]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[129 E-commerce & Quick-Commerce Fulfilment]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Labour Planning and Engineered Standards]]
2. [[#2. Productivity KPIs: Lines per Hour, Units per Hour, Cost per Line]]
3. [[#3. Slotting and Layout Effects on Labour]]
4. [[#4. Incentive Schemes and Gamification]]
5. [[#5. WMS vs WES vs WCS: The Software Stack]]
6. [[#6. Wave, Waveless and Batch Order Release]]
7. [[#7. Voice, Vision, Pick-to-Light and Other Pick Technologies]]
8. [[#8. Yard Management and Dock Appointment Scheduling]]
9. [[#9. Peak Season Planning]]
10. [[#10. 3PL Warehouse Commercial Models]]
11. [[#11. Contract and SLA Design]]
12. [[#12. Safety Management and Culture]]
13. [[#13. ⭐ Advanced: Labour Model Simulation and Workforce Flexibility]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Robot orchestration, India's new labour codes and warehouse cost benchmarks
> **Amazon's fleet-coordination model "DeepFleet" (Jul 2025).** With its 1 millionth warehouse robot, Amazon unveiled a generative-AI model that plans robot traffic and is projected to make the robot fleet about **10% faster**; the same report said roughly **75% of Amazon deliveries** are assisted by robots in some way. It is a live example of the **execution layer** (WES/WCS software) deciding productivity, not just the machines. ([TechCrunch](https://techcrunch.com/2025/07/01/amazon-deploys-its-1-millionth-robot-releases-generative-ai-model/))
>
> **India's Occupational Safety, Health and Working Conditions Code in force (21 Nov 2025).** Wikipedia records that the OSH Code, which received assent on 28 Sep 2020, was enforced on **21 November 2025** and repeals older laws including the Contract Labour (Regulation and Abolition) Act, 1970 and the Inter-State Migrant Workmen Act, 1979. Warehouse operators and 3PLs should check current rules on contract labour, hours and safety for their state before fixing labour plans (the Code on Social Security 2020 page also lists 21 Nov 2025 among its commencement dates). ([Wikipedia: OSH Code](https://en.wikipedia.org/wiki/Occupational_Safety,_Health_and_Working_Conditions_Code,_2020), [Wikipedia: Code on Social Security](https://en.wikipedia.org/wiki/Code_on_Social_Security,_2020))
>
> **Warehousing and logistics cost benchmarks (DPIIT-NCAER, 23 Sep 2025).** Logistics cost was **7.97% of GDP (₹24.01 lakh crore) in FY2023-24**; warehousing averaged **₹30 per sq ft per month** and cold storage **₹58.50**; small firms spent **16.9% of output** on logistics versus **7.6%** for large firms. ([Logistics Insider](https://www.logisticsinsider.in/indias-logistics-cost-at-7-9-of-gdp-report/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Labour Planning and Engineered Standards
> 🟠 Tier 2 · _Key points:_ Standard time, PF&D allowance, utilisation, headcount

### Definition
**Engineered labour standards (ELS)** state how long a task should take when performed by a trained worker using the standard method at a normal pace, plus allowances. They are built from **time study** (stopwatch or video), **predetermined motion-time systems (MTM-type)** or work sampling; see [[152 Learning Curves, Work Measurement & Productivity]].

$$\text{Standard time} = \text{Basic time}\times(1 + \text{PF\&D allowance})$$

PF&D stands for personal, fatigue and delay allowances (often about 10-20%). **Labour planning** converts volume into hours:

$$\text{Hours} = \frac{\text{Volume}\times\text{Standard time}}{\text{Utilisation}},\qquad \text{Headcount} = \frac{\text{Hours}}{\text{Productive hours per shift}}$$

Utilisation (percentage of paid time spent on standard work) is typically 80-90% in a managed operation. **Performance** = standard hours earned / actual hours worked.

### Example
A pick line (travel 0.50 min, search 0.10, pick 0.25, scan/verify 0.12, admin 0.08) has basic time 1.05 min. With 15% PF&D, standard = 1.05 x 1.15 = **1.2075 min**, so a worker at 100% performance does **49.7 lines per hour**. At 85% utilisation the planning rate is **42.2 lines per paid hour**. A day of 30,000 lines needs 30,000 / 42.2 = **710 hours**, which is 710 / 7 = **101.5 picker-shifts** at 7 productive hours of an 8-hour shift. At ₹26,000 per month CTC (assumed, 26 working days, 8-hour shift) the hourly cost is ₹125, so **cost per order line = ₹125 / 42.2 = ₹2.96**.

### In the news
See news box. Under the new OSH Code regime, hours, overtime and contract-labour practice must be re-checked, so plans built on engineered standards should be stress-tested against the updated rules.

### Interview angle
> [!question] How it is asked
> "A DC picks 30,000 lines a day. How many pickers do you need and how do you know the number is right?"

> [!tip] Strong answer includes
> - Standard time per line, allowance, utilisation, and productive hours per shift
> - A check against actual data (lines per hour by shift) and peak-day logic
> - Separation of direct, indirect and supervisory labour
> - Notes that the standard must reflect layout and slotting, not only worker speed

---
## 2. Productivity KPIs: Lines per Hour, Units per Hour, Cost per Line
> 🟠 Tier 2 · _Key points:_ Lines/hour, units/hour, cost per order line, utilisation, accuracy

### Definition
Core labour KPIs ([[012 Supply Chain Analytics & KPIs]]):
- **Lines per hour (LPH)** = order lines picked / picker hours (the best pick KPI because units per line vary).
- **Units per hour (UPH)** = units processed / labour hours; useful for pack, receiving and e-commerce each-picking.
- **Cost per order line / per order / per unit shipped** = total labour (and where relevant, total warehouse) cost / volume.
- **Labour utilisation** and **performance vs standard** (earned hours / worked hours).
- **Pallets per hour** at dock and in put-away.
- **Quality:** pick accuracy (lines correct / lines picked, with a customer-visible target such as 99.5-99.9%), dock-to-stock time, order cycle time.
- **Safety and attendance:** LTIFR, absenteeism, attrition (high in Indian warehouse labour, which affects training cost).

Do not read LPH alone: a high LPH with low accuracy simply moves cost to returns and re-shipments. Present a **balanced scorecard** per shift, and report **by zone** (each-pick, case-pick, pallet) since the mix drives the average.

### Example
Zone A (small items, each-pick) picks at 55 LPH with 99.7% accuracy; zone B (bulky cartons) at 28 LPH with 99.9%. A blended day of 20,000 lines in A and 10,000 in B needs 20,000/55 + 10,000/28 = 364 + 357 = **721 hours**, a blended **41.6 LPH**. Management who compare this blended 41.6 to a benchmark of 50 LPH conclude "productivity is poor" when the mix is the cause; the correct comparison is each zone to its own standard.

### In the news
See news box. Amazon's robotics claim (about 10% faster fleet from DeepFleet) is a throughput-per-asset claim; internal labour KPIs still need normalisation by mix and by task.

### Interview angle
> [!question] How it is asked
> "A warehouse manager says productivity is 38 lines per hour against a 45 target. What do you check before blaming the team?"

> [!tip] Strong answer includes
> - Mix, order profile (lines per order), zone and equipment effects
> - Utilisation: waiting for replenishment, congestion, system latency
> - Slotting and travel distance; accuracy and rework trade-off
> - Decomposes into travel, search, pick and admin time

---
## 3. Slotting and Layout Effects on Labour
> 🟠 Tier 2 · _Key points:_ Travel share, golden zone, replenishment, congestion

### Definition
In manual picking, **travel is typically the largest component of picker time** (a commonly cited share is about half; it depends on the operation). **Slotting** (putting fast movers in the golden zone, family grouping, ABC by picks) therefore converts directly into labour hours; see [[010 Warehouse Management]] for slotting rules. Other layout levers: pick-path design (S-shape, return, largest gap), zone picking with pass-through, wave and batch picking to share travel, forward pick area with reserve replenishment, and congestion control (one-way aisles, limit pickers per aisle).

$$\text{Labour saving} \approx \text{Lines} \times \frac{\Delta \text{travel time}}{60}\times\text{Hourly cost}$$

### Example
Continuing from sub-topic 1: re-slotting the top 20% SKUs cuts travel per line from 0.50 to 0.35 min. Basic time falls to 0.90 min; standard time = 0.90 x 1.15 = 1.035 min, i.e., 58.0 lines/hour at 100% (**+16.7%**), 49.3 at 85% utilisation. Cost per line falls from ₹2.96 to ₹125/49.3 = **₹2.54 (−14%)**. On 30,000 lines a day, 300 days, that saves 30,000 x 300 x ₹0.42 = about **₹38 lakh a year**. Re-slotting costs labour for the move and temporary productivity loss; a repeated re-slot every season usually pays back within weeks when the SKU mix shifts.

### In the news
See news box. Because warehouse rent averages about ₹30 per sq ft per month, firms trade off compact layouts (low rent) against congestion (higher labour); the right answer is found by modelling, not by rules of thumb.

### Interview angle
> [!question] How it is asked
> "Pick productivity has fallen 10% after a new SKU launch. Where do you look first?"

> [!tip] Strong answer includes
> - Slotting drift (new fast movers in the wrong zone), travel per line and replenishment delays
> - Congestion and wave design
> - Quantifies savings per minute of travel and compares to the re-slot cost
> - Mentions seasonal and promotional re-slotting

---
## 4. Incentive Schemes and Gamification
> 🟠 Tier 2 · _Key points:_ Standards-based incentive, quality gates, team vs individual, gamification

### Definition
An **incentive scheme** pays for output above a standard. Design principles: (1) base the target on **engineered standards**, not history; (2) set a **threshold** (e.g., 85-90% of standard) below which no incentive is paid and a **cap** (e.g., 130%) to protect safety and quality; (3) apply **quality gates** (accuracy, damage, safety compliance) so an incentive can be forfeited; (4) choose **individual vs team** based on whether work is separable (team incentives suit pass-and-sort flows); (5) keep the formula simple enough for a worker to compute; (6) check statutory wage rules and bonus law with HR before launch.

Typical formula: **incentive per hour = share x (performance − 1) x base hourly rate** above the threshold.

**Gamification** adds leaderboards, badges, streaks, team challenges and real-time screens (often through voice or RF terminals), aimed at engagement and retention. Evidence for long-run effects is mixed, so use it to complement, not replace, a fair pay design, and avoid public ranking that pushes unsafe speed.

### Example
Standard 50 LPH, base pay ₹125 per hour. A picker reaches 62.5 LPH (125% performance). With a 50% sharing formula, incentive = 0.5 x 0.25 x 125 = **₹15.6 per hour**, so the worker earns about 12.5% more. Cost per line falls from ₹125/50 = ₹2.50 at 100% to (125 + 15.6) / 62.5 = **₹2.25 (−10%)**. The employer saves 10% per line and the worker gains 12.5% pay. If accuracy falls from 99.7% to 99.0%, the extra errors (0.7% of 62.5 lines per hour) cost more than the saving if each error costs ₹400 to resolve: 62.5 x 0.007 x 400 = ₹175 per hour. Hence quality gates are essential.

### In the news
See news box. As robots take repetitive travel, incentives shift towards exception handling, quality and safety measures; and new labour codes make documentation of working hours and wage components more important.

### Interview angle
> [!question] How it is asked
> "Would you introduce a productivity incentive in a warehouse with 40% attrition? How would you design it?"

> [!tip] Strong answer includes
> - Measure first, with engineered standards and a fair threshold
> - Quality and safety gates and a cap; team vs individual logic
> - Costs and benefits quantified, including attrition effects
> - Addresses root causes of attrition (pay, shift pattern, supervision) not only incentives

---
## 5. WMS vs WES vs WCS: The Software Stack
> 🟠 Tier 2 · _Key points:_ System of record vs execution vs equipment control

### Definition
| Layer | Role | Time horizon | Examples of what it does |
|---|---|---|---|
| **WMS (Warehouse Management System)** | System of record and planning for inventory, orders, locations, tasks, billing | Minutes to days | Receiving, put-away rules, allocation, wave planning, inventory control, labour management, interfaces to ERP and carriers |
| **WES (Warehouse Execution System)** | Real-time orchestration across the building | Seconds to minutes | Balances work across zones and automation, dynamically releases and prioritises tasks, manages order streaming, load balancing between picking, packing and sortation |
| **WCS (Warehouse Control System)** | Direct control of machines | Milliseconds to seconds | Routes totes on conveyors, controls sorters, ASRS cranes, shuttles, PLC communication, diverts and scanners |

In practice the boundaries blur: some modern WMS include execution features, and some automation vendors bundle WCS plus WES. A typical architecture is **ERP → WMS → WES → WCS → equipment**, with labour, yard, transport and robotics systems (AMR fleet manager) plugged in. Interface design (APIs and events) and master data quality ([[175 Data Quality, Master Data & Data Governance]]) decide success. See [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]] and [[083 SAP WM-EWM — Warehouse]] for an ERP-embedded example and [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]] for the landscape.

### Example
A sorter-based e-commerce site receives 8,000 orders that must cut off at 16:00. The WMS decides which orders are released and allocates stock. The WES watches pack stations and sorter chutes and **releases work in the sequence that keeps all stations busy**: if station 3 starves, it releases a batch to it. The WCS only moves totes: it reads the barcode, diverts the tote to lane 5 and confirms. If the WES is missing, the WMS often releases in large waves, creating bursts at the sorter and idle time between waves.

### In the news
See news box. Amazon's DeepFleet is a fleet-level orchestration model in the WES/WCS space: it improves throughput by sequencing movement rather than by changing equipment.

### Interview angle
> [!question] How it is asked
> "What is the difference between a WMS and a WES, and when does a client need a WES?"

> [!tip] Strong answer includes
> - Clear layering and time horizon: plan (WMS), orchestrate (WES), control (WCS)
> - WES pays when there is automation, multiple flows and a need for dynamic load balancing
> - Mentions integration, data quality and vendor options
> - Does not recommend a WES for a simple manual operation

---
## 6. Wave, Waveless and Batch Order Release
> 🟠 Tier 2 · _Key points:_ Wave picking, continuous release, cut-off time, balancing

### Definition
- **Discrete picking:** one order at a time. Simple, travel heavy.
- **Batch picking:** group orders for the same SKUs and pick together, then sort.
- **Zone picking:** pickers stay in zones, orders pass through.
- **Wave picking:** release a defined set of orders at a scheduled time (by carrier cut-off, route, priority); good for planning labour and dock loads; creates peaks and tail effects.
- **Waveless (continuous or dynamic) release:** orders release as they arrive and resources allow, constrained by cut-offs and capacity; reduces order waiting time, smooths load, and suits e-commerce and quick turn orders but needs real-time visibility (a WES).

Wave design parameters: **wave size**, **release frequency**, **sequence by cut-off**, **replenishment completion before release**, and **capacity limit** per zone.

### Example
A carrier collects at 16:00 and pick-pack-load takes about 3.5 hours for a wave, so the last wave must release by 12:30 and orders after that miss the day. With waveless release and a sorter keeping work-in-process low, the process lead time falls to about 2.5 hours (illustrative), moving the effective order cut-off to 13:30. The business gains an extra hour of order intake, which at 800 orders per hour is **800 extra same-day orders**. Not every site can achieve that; if replenishment or the sorter is the bottleneck, waves remain safer.

### In the news
See news box. Same-day delivery promises push e-commerce networks toward waveless release; see [[129 E-commerce & Quick-Commerce Fulfilment]].

### Interview angle
> [!question] How it is asked
> "When would you choose wave over waveless picking?"

> [!tip] Strong answer includes
> - Compares by order profile, automation level, carrier schedule and system maturity
> - Wave: predictable cut-offs, manual operations; waveless: e-commerce, real-time system, automation
> - Mentions hybrid (priority waves plus continuous release)
> - Quantifies the cut-off extension or cycle-time benefit

---
## 7. Voice, Vision, Pick-to-Light and Other Pick Technologies
> 🟠 Tier 2 · _Key points:_ RF scan, voice, pick-to-light, put-to-light, vision/AR

### Definition
| Technology | How it works | Best fit | Watch-outs |
|---|---|---|---|
| **RF scanning / handheld** | Scan location and item, confirm quantity | Baseline for most DCs | One hand busy, eyes on the screen |
| **Voice picking** | Headset instructions, spoken confirmation | Hands-free case and piece picking, cold stores, loose picking | Noise, accents/language set-up, training |
| **Pick-to-light / put-to-light** | Lights show location and quantity; put walls for sorting | High-velocity small items, order consolidation | Capex per location, rigid layout |
| **Vision / AR glasses** | Screens or glasses show pick, with camera verification | Complex picks, new staff | Cost, ergonomics, pilot results vary |
| **Robot-assisted picking (AMR, goods-to-person)** | Robots bring shelves or totes | High lines per hour, labour scarcity | See [[127 Warehouse Engineering - Racking, Sizing & Material Handling]] |

Vendors report accuracy above 99.5% and productivity gains of roughly 10-30% for the right use cases; these are vendor claims, and results vary with the baseline, so require a pilot with a control group.

### Example
A site of 100 pickers at 42 LPH moves to pick-to-light in the fast zone. Suppose (illustrative) productivity rises 20% to 50.4 LPH for 40 pickers and capex is ₹1.2 crore. Labour avoided: the same volume of 40 x 42 x 7 = 11,760 lines per day needs 33.3 pickers instead of 40, so 6.7 fewer, around 7 people x ₹3.12 lakh a year (₹26,000 x 12) = **₹21.8 lakh a year**. Simple payback is 1.2 crore / 21.8 lakh = **5.5 years**, too long unless the quality gain is valued: if errors fall from 0.5% to 0.1% on 11,760 lines a day, avoided error cost at ₹400 each is 11,760 x 0.004 x 400 x 300 = **₹56 lakh a year**; payback then falls to about 1.5 years. The decision rests on how the cost of errors is valued.

### In the news
See news box. Robot coordination and AI models in the fleet (Amazon DeepFleet) show the same logic: software sequencing yields a double-digit throughput gain without new hardware.

### Interview angle
> [!question] How it is asked
> "Would you invest in pick-to-light for a DC that handles 12,000 lines a day?"

> [!tip] Strong answer includes
> - Considers volume, SKU velocity and fixed layout; recommends a pilot
> - Values both productivity and accuracy
> - Compares with cheaper changes (slotting, zone picking, RF)
> - Considers attrition and training effects

---
## 8. Yard Management and Dock Appointment Scheduling
> 🟠 Tier 2 · _Key points:_ YMS, appointments, detention, queueing at the gate

### Definition
**Yard management** controls trucks and trailers between the gate and the dock: gate check-in/out, trailer location, dock assignment, driver communication and detention tracking. A **Yard Management System (YMS)** uses gate scanning, ANPR cameras, RFID and a yard map; a **dock appointment scheduling (DAS)** tool lets carriers or suppliers book time slots against dock capacity. Benefits: shorter truck turnaround, fewer detention claims, better dock use and lower congestion. The leading KPIs are **truck turn-around time (TAT)**, **dock-to-stock time**, **on-time slot adherence**, **detention cost**, and **door utilisation**.

For doors modelled as servers, random arrivals produce queues even when utilisation is below 100%; **Erlang-C** gives the probability of waiting and the mean wait. See [[149 Queueing Theory & Waiting-Line Analysis]] and [[127 Warehouse Engineering - Racking, Sizing & Material Handling]] for door counts.

### Example
6 doors, 1 hour per truck. If **5 trucks per hour** arrive randomly in the peak (utilisation 83%), Erlang-C gives a waiting probability of **59%** and a mean wait of **0.59 h (about 35 minutes)**. If appointments spread arrivals to **4 per hour** (utilisation 67%) the waiting probability falls to **28%** and the mean wait to **0.14 h (about 8.5 minutes)**; at **3 per hour** (50%) the mean wait is about **2 minutes**. At ₹100 per truck-hour of detention (assumed), moving from 5 to 4 per hour in the peak saves roughly (0.59 x 5 − 0.14 x 4) x 100 = about **₹237 per peak hour** in detention alone, plus lower driver idle time and less congestion. In reality appointments do better than the random-arrival model because arrivals are controlled.

### In the news
See news box. With logistics costs at 7.97% of GDP and a push to cut truck dwell times under national logistics policy ([[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]), yard visibility and appointments are an inexpensive lever.

### Interview angle
> [!question] How it is asked
> "Trucks wait 4 hours outside a plant gate. How do you diagnose and fix it?"

> [!tip] Strong answer includes
> - Maps the process: gate, document check, weighing, dock, unload, exit; finds the bottleneck
> - Arrival profile (peak spikes), door count, unloading time and paperwork
> - Fixes: appointments, pre-advice and e-documents, extra shifts at peak, yard staging
> - Quantifies detention and productivity cost

---
## 9. Peak Season Planning
> 🟠 Tier 2 · _Key points:_ Forecast, capacity, temps, overtime, training, contingency

### Definition
**Peak planning** matches labour, space and equipment to seasonal surges (Diwali, Big Billion Day and end-of-season sales, quarter-end, festival or wedding seasons). Steps: (1) forecast peak volume and its shape ([[004 Demand Forecasting & Planning]]); (2) compute the capacity gap by process (pick, pack, dock, returns); (3) choose levers: **temporary labour, overtime, extra shifts, temporary space, automation or more waves, pre-built inventory (pre-positioning)**, order cut-off changes, and slower SLAs; (4) plan **training and ramp-up** (new workers are less productive for days); (5) run a **readiness review** and war-room during the peak; (6) plan returns, which follow the peak.

Overtime in India is typically paid at twice the ordinary rate under the Factories Act; check current rules and any state exemptions, including those under the new labour codes.

### Example
Permanent capacity is 24,000 lines per day (82 pickers x 42.2 LPH x 7 h = 295 lines each). Peak is 60,000 lines a day for 10 days, a gap of 36,000. Temporary pickers ramp: 60% of permanent productivity on days 1-2, 80% on days 3-5, 90% on days 6-10, an average of **81%**, or **239 lines per day** each. Temps needed = 36,000 / 239 = **151**. Cost at ₹1,000 per day plus a 15% agency fee = 151 x 10 x 1,150 = **₹17.4 lakh**, or **₹4.82 per extra line**. Overtime alternative: 2 hours per day at twice the rate costs ₹250 per hour for 42.2 lines = **₹5.92 per line** and adds only 28.6% of capacity, so it cannot close the gap alone. Normal cost per line is ₹2.96, so the peak line costs 63% to 100% more.

### In the news
See news box. NCAER's data show small firms bear much higher logistics costs; peak spikes make that worse because fixed capacity is small and variable capacity is expensive.

### Interview angle
> [!question] How it is asked
> "Your DC must handle 2.5 times normal volume for 10 days. What is your plan?"

> [!tip] Strong answer includes
> - Quantifies the gap per process and compares levers by cost per line and risk
> - Includes learning-curve loss of temps, supervision ratio and training
> - Looks at demand-side levers: cut-offs, promised dates, order caps
> - Mentions a contingency and a post-peak return plan

---
## 10. 3PL Warehouse Commercial Models
> 🟠 Tier 2 · _Key points:_ Cost-plus, per pallet, per order line, hybrid, volume risk

### Definition
Common 3PL pricing models:
- **Open-book cost-plus (management fee):** client pays actual costs plus a fee (percentage or fixed). Transparent, shifts cost risk to the client, needs audit rights.
- **Transactional (per unit) pricing:** rates per pallet stored per month, per pallet in/out, per order line, per order or per unit shipped, plus value-added service (VAS) rates. Aligns price with volume; the 3PL carries utilisation risk.
- **Fixed plus variable (hybrid):** a fixed monthly fee for dedicated space, equipment and a baseline team, plus per-unit fees above a threshold; volume bands and **minimum guaranteed volume** protect the 3PL.
- **Gain-share and productivity guarantees:** savings are shared with the client.
- **Dedicated vs multi-client (shared) warehouse:** dedicated is more cost-plus, shared more transactional.

Key contract terms: term and lock-in, volume bands, indexation for wage and rent changes, asset ownership (racking, automation, IT), liability and insurance, stock accuracy and shrinkage allowance, audit rights, data ownership and exit. See [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]] and [[137 Supply Chain Contracts & Game Theory]].

### Example
The 3PL's monthly cost at 60,000 order lines is ₹39 lakh (₹18 lakh labour of which 70% varies with volume). **Cost-plus** with an 8% fee gives ₹42.12 lakh. **Transactional**: ₹300 per pallet position x 5,000 = ₹15 lakh, in/out handling ₹60 x 5,000 = ₹3 lakh, ₹40 per line x 60,000 = ₹24 lakh, total **₹42 lakh**, about equal. Now volume moves:
- Lines 90,000 (+50%): cost rises to ₹45.3 lakh; transactional revenue ₹54 lakh, 3PL margin ₹8.7 lakh (16%); cost-plus revenue ₹48.9 lakh. The client pays **₹5.1 lakh more under transactional**.
- Lines 42,000 (−30%): cost ₹35.2 lakh; transactional revenue ₹34.8 lakh, a **loss of ₹0.4 lakh**; cost-plus revenue ₹38.0 lakh.
So transactional rewards the 3PL for volume growth and exposes it on falls; cost-plus does the reverse. A hybrid with a fixed base and volume bands shares the risk.

### In the news
See news box. As warehousing rents (₹30 per sq ft per month average) and wages move, indexation clauses in 3PL contracts decide who bears the cost.

### Interview angle
> [!question] How it is asked
> "Which pricing structure would you propose to a start-up client with highly uncertain volumes?"

> [!tip] Strong answer includes
> - Compares risk allocation under each model, using numbers
> - Suggests hybrid or banded pricing with minimum volume and exit terms
> - Mentions open-book audit and indexation
> - Addresses incentives: what behaviour each model rewards

---
## 11. Contract and SLA Design
> 🟠 Tier 2 · _Key points:_ KPIs, targets, service credits, measurement, governance

### Definition
A good **Service Level Agreement (SLA)** specifies **measurable KPIs, definitions, measurement method, data source, target, tolerance, and the consequence**. Typical warehouse SLAs: inbound receipt-to-available within 24 hours, order accuracy (lines) 99.5%, on-time dispatch 98-99%, inventory accuracy 99.5%, damage and shrinkage limits, return processing time, safety incidents, and system uptime. Mechanisms: **service credits** (a percentage of the fee for misses, often capped), **bonus** for beating targets, root-cause and corrective action, **excused events** (client forecast deviation, force majeure), and joint governance (monthly reviews, quarterly business reviews, a continuous-improvement plan).

Pitfalls: KPI definitions that differ between parties; unmeasurable targets; credits so small that they are ignored, or so large that the 3PL cannot accept; SLAs that ignore client inputs (late forecasts, bad master data).

### Example
SLA: order-line accuracy 99.5%, credit 2% of the monthly fee for each 0.5-point shortfall (rounded up), cap 10%. Monthly fee ₹42.12 lakh. Measured accuracy 98.9%, a 0.6-point shortfall, so 2 steps and a **4% credit = ₹1.68 lakh**. The 3PL's cost of improving accuracy (extra scan checks costing ₹0.5 lakh a month) is below the credit, so the SLA changes behaviour. Had the credit been 0.5%, the 3PL would rationally ignore the miss.

### In the news
See news box. The OSH Code and state rules make safety and working-hours compliance a growing contractual item between clients and 3PLs, increasingly audited.

### Interview angle
> [!question] How it is asked
> "A client complains about 3PL performance. How do you restructure the SLA to improve it?"

> [!tip] Strong answer includes
> - Clear KPI definitions and data source, and joint measurement
> - Credits and bonuses sized to change behaviour
> - Joint root-cause process and governance cadence
> - Fair treatment of client-caused deviations (forecast accuracy, master data)

---
## 12. Safety Management and Culture
> 🟠 Tier 2 · _Key points:_ LTIFR, near-miss, forklift safety, ergonomics, heat

### Definition
Warehouse hazards: forklift and pedestrian collisions, falls from height, manual handling injuries, rack collapse, fire, heat stress and fatigue. Controls: **segregated pedestrian routes**, speed limits, forklift licensing and refresher training, **physical guards for rack uprights**, load-limit labels, PPE, ergonomic design and job rotation, heat and hydration controls in summer, near-miss reporting and **Hierarchy of Controls** (eliminate, substitute, engineer, administer, PPE). Metrics:

$$\text{LTIFR} = \frac{\text{Lost-time injuries}\times 10^6}{\text{Hours worked}}$$

(Some organisations use 200,000 or 100,000 hours as the base; state the base clearly.) Lead indicators (near misses reported, safety observations, training coverage) are better predictors than injuries. **Safety versus productivity** needs balance: speed targets without safety gates cause incidents.

### Example
A site with 300 staff working 2,400 hours each a year has 720,000 hours. Six lost-time injuries give an LTIFR of 6 x 10^6 / 720,000 = **8.3 per million hours** (or 1.67 per 200,000 hours). After a programme of rack guards, pedestrian segregation and forklift speed limits, injuries fall to 2: LTIFR **2.8**. If each injury costs ₹2.5 lakh in direct and indirect costs (medical, lost time, investigation, compensation), annual savings are 4 x ₹2.5 lakh = **₹10 lakh**, before counting reputational and client-audit benefits.

### In the news
See news box. With the OSH Code now enforced (21 Nov 2025 per the source cited) and clients auditing safety, 3PLs that cannot show safety data risk losing contracts.

### Interview angle
> [!question] How it is asked
> "A forklift near-miss rate is rising at your DC. What do you do?"

> [!tip] Strong answer includes
> - Investigates root causes: layout, traffic flow, training, speed, fatigue, equipment
> - Applies the hierarchy of controls (segregation first, PPE last)
> - Uses lead and lag indicators and sets targets; engages workers
> - Balances productivity incentives with safety gates

---
## 13. ⭐ Advanced: Labour Model Simulation and Workforce Flexibility
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A deterministic labour plan can fail because demand and productivity vary. Better planning treats volume as a distribution and uses **simulation or optimisation**: input hourly arrival profiles (orders by hour), task standards, shift patterns and equipment, and output queue lengths, cut-off misses and labour cost. Techniques: discrete-event simulation ([[068 Operations-Specific Python (PuLP, SimPy)]]), shift-scheduling integer programs, and cross-training matrices that let workers move between pick, pack and dock. Related theory: [[153 Aggregate Planning Models & Workforce Strategy]] (chase vs level workforce) and [[018 Capacity Management & OEE]].

Workforce flexibility levers: cross-trained pool, split shifts, part-time and gig-style staffing (check legal status), annualised hours, and flexible 3PL labour contracts. The trade-off is **flexibility cost vs cost of missing a cut-off**.

### Example
Hourly demand is 600 lines at base but peaks at 1,200 for 4 hours of the 16-hour two-shift day (flat average 750). Staff at the average (750 lines per hour at 42.2 LPH = 17.8 pickers) and the peak backlog is (1,200 − 750) x 4 = **1,800 lines**, which clears only if later demand is light, so cut-offs are missed. Staff at the peak (1,200 / 42.2 = 28.4 pickers) for all 16 hours and you pay 454 picker-hours, with about 14 pickers idle in the 12 off-peak hours. A flexible plan uses 20 permanent pickers (844 lines per hour, enough for the 600 base) plus 9 cross-trained pickers from packing for the 4 peak hours: 20 x 16 + 9 x 4 = 356 picker-hours. That saves 98 picker-hours a day, about **₹12,250 a day** at ₹125 per hour, while still covering the peak (29 x 42.2 = 1,224 lines per hour). Simulation checks whether the cross-trained pool can actually transfer in time.

### In the news
See news box. Robot fleets and AI orchestration (Amazon) show that the same logic of flexible capacity is being automated; in India labour flexibility is also a regulatory question under the new codes.

### Interview angle
> [!question] How it is asked
> "Demand varies 2x within the day. How would you plan labour?"

> [!tip] Strong answer includes
> - Models hourly demand, not just the daily total
> - Compares level, chase and flexible pools by cost and service
> - Mentions cross-training, shift design and technology to flatten peaks
> - Tests plans with simulation before committing
