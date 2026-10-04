---
tags: [operations-management, tier1]
area: Operations Management
topic: "Capacity Management & OEE"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 12
---
# Capacity Management & OEE

⬅ [[017 Process Management & Optimization]] · [[_Index - Operations Management|Operations Management]] · [[019 Facility Layout & Location]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Design vs Effective Capacity]]
2. [[#2. Utilization & Efficiency]]
3. [[#3. OEE Calculation]]
4. [[#4. Availability Loss]]
5. [[#5. Performance Loss]]
6. [[#6. Quality Loss]]
7. [[#7. Capacity Expansion Strategies]]
8. [[#8. Resource Allocation]]
9. [[#9. Constraint Management]]
10. [[#10. Overall Equipment Effectiveness (OEE) Improvement]]
11. [[#11. ⭐ Advanced: Capacity Planning with Product Mix and Break-even]]
12. [[#12. ⭐ Advanced: TEEP, OLE and Loss Trees]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): adding capacity, and losing it to a missing part
> **Maruti Suzuki Hansalpur Plant D (reported 30 Jul 2026).** Commercial production began at the fourth plant of Maruti Suzuki's Hansalpur (Gujarat) facility, lifting its annual capacity from 750,000 to **1 million vehicles**, which the company calls India's largest single-location passenger-vehicle plant. Maruti's total manufacturing capacity is now **2.9 million units a year**; cumulative Hansalpur investment is about **₹25,288.7 crore** (Plant D about ₹3,900 crore, estimated). The site makes e Vitara, Fronx, Baleno and Swift and handles about **47% of Maruti's export shipments**. ([Evo India](https://www.evoindia.com/news/car-news/maruti-suzuki-hansalpur-reaches-1-million-capacity-587590))
> 
> **Nexperia chip crisis (Oct 2025).** Nexperia suspended wafer supply to its Dongguan plant on 29 Oct 2025; by 31 Oct ZF had cut shifts at its main electric-drivetrain plant and Nissan said chip stock would last only to the first week of November. Installed capacity does not help when one low-value part is missing. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nexperia-conflict-spills-overseas-as-it-halts-exports-to-china-german-automotive-manufacturers-slow-production-due-to-semiconductor-shortages-from-dutch-chipmaker))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Design vs Effective Capacity
> 🔴 Tier 1 · _Tracker hint:_ Theoretical max vs realistic output; capacity cushion

### Definition
- **Design capacity:** the maximum output possible under ideal conditions (no breaks, no changeovers, no maintenance).
- **Effective capacity:** the maximum realistic output after planned losses (maintenance, changeovers, breaks, scheduling limits, product mix).
- **Actual output:** what is really produced, lower still because of breakdowns, defects, absenteeism, material shortages.

$$\text{Design} \ge \text{Effective} \ge \text{Actual}$$
**Capacity cushion** $= 100\% - \text{Average utilisation}$ (a buffer for demand surges); **capacity utilisation** and **efficiency** are in the next sub-topic. Industries with high fixed cost and low variability (steel, power) run small cushions; services with volatile demand (call centres) need larger ones. Capacity is measured in the output unit relevant to the **bottleneck**.

### Example
A line is designed for 1,000 units/day. Planned maintenance and changeovers reduce realistic output to 800 (effective). Actual output is 680. Implied cushion if demand is 680: effective capacity 800 vs demand 680 gives $1 - 680/800 = 15\%$ cushion.

### In the news
See news box. Hansalpur's 1 million figure is a design/rated annual capacity; real output depends on demand, shifts and model mix.

### Interview angle
> [!question] How it is asked
> "What is the difference between design and effective capacity?" or "How much spare capacity should a plant keep?"

> [!tip] Strong answer includes
> - Three levels: design, effective, actual
> - Capacity cushion and why (demand variability, lead time of expansion)
> - Capacity stated at the bottleneck
> - Trade-off: cushion cost vs lost sales

---

## 2. Utilization & Efficiency
> 🔴 Tier 1 · _Tracker hint:_ Utilization = Actual/Design; Efficiency = Actual/Effective

### Definition
$$\text{Utilisation} = \frac{\text{Actual output}}{\text{Design capacity}}, \qquad \text{Efficiency} = \frac{\text{Actual output}}{\text{Effective capacity}}$$
Utilisation measures how much of the theoretical maximum is used; efficiency measures performance against what is realistically possible. Efficiency is always the higher of the two (since effective $\le$ design).

Cautions: **100% utilisation is not the goal.** Queueing theory shows waiting time explodes as utilisation nears 100% (see [[017 Process Management & Optimization]]); also, high utilisation of non-bottlenecks creates inventory without more sales. Also note **TEEP** (Total Effective Equipment Performance) $= \text{OEE} \times \text{Loading}$, where loading $= \text{planned production time}/\text{calendar time}$.

### Example
Design 1,000, effective 800, actual 680 units/day. Utilisation $= 680/1000 = 68\%$; efficiency $= 680/800 = 85\%$. If planned production time is 16 of 24 hours, loading $= 66.7\%$; with OEE 75%, TEEP $= 0.75 \times 0.667 = 50\%$.

### In the news
See news box. After Nexperia, utilisation fell not because of capacity but because of a missing part: efficiency measured against effective capacity would drop sharply.

### Interview angle
> [!question] How it is asked
> "A plant reports 70% utilisation. Is that good?"

> [!tip] Strong answer includes
> - Both formulas and what each means
> - Compare with demand and bottleneck, not only to a benchmark
> - Warns that maximising utilisation raises WIP and lead time
> - TEEP as the broader view of asset use

---

## 3. OEE Calculation
> 🔴 Tier 1 · _Tracker hint:_ OEE = Availability × Performance × Quality; world-class = 85%

### Definition
**Overall Equipment Effectiveness (OEE)** measures how much of the planned production time is truly productive:
$$OEE = A \times P \times Q$$
$$A = \frac{\text{Run time}}{\text{Planned production time}},\quad P = \frac{\text{Ideal cycle time} \times \text{Total count}}{\text{Run time}},\quad Q = \frac{\text{Good count}}{\text{Total count}}$$
Run time = planned production time − stop time. **World-class OEE ≈ 85%** (typically A ≈ 90%, P ≈ 95%, Q ≈ 99.9%; $0.90 \times 0.95 \times 0.999 \approx 85\%$). Many plants run at 40–60%.

Three-loss view maps to the **Six Big Losses**: breakdowns and setups/adjustments (availability); minor stops and reduced speed (performance); startup rejects and production rejects (quality). OEE is applied to a machine or the bottleneck, not to every machine.

### Example
Shift 480 min planned; downtime 48 min → run time 432 min; $A = 432/480 = 90\%$. Ideal cycle time 1 min/unit; total produced 380 → $P = 1 \times 380/432 = 87.96\%$. Good units 361 → $Q = 361/380 = 95\%$. $OEE = 0.90 \times 0.8796 \times 0.95 = 75.2\%$. Check: good output at ideal speed $= 361 \times 1 = 361$ min of value over 480 min planned $= 75.2\%$ ✓.

### In the news
See news box. For a new plant such as Hansalpur D, OEE on the bottleneck (paint/assembly) governs how fast nameplate capacity becomes real output.

### Interview angle
> [!question] How it is asked
> "Calculate OEE from this data" or "A machine has 60% OEE; where do you start?"

> [!tip] Strong answer includes
> - Formula with A, P, Q and correct denominators
> - Six Big Losses mapping
> - Benchmarks: world-class 85%, typical 60%
> - Start with the biggest loss via Pareto; apply at the bottleneck

---

## 4. Availability Loss
> 🔴 Tier 1 · _Tracker hint:_ Planned vs unplanned downtime; MTBF, MTTR

### Definition
Availability loss is any time the machine is not running during planned production time. 
- **Unplanned (breakdowns, material shortages, tool failure)** and **planned stops that reduce run time (changeovers, setups, adjustments)** count against availability in OEE. Scheduled breaks, planned maintenance and no-demand time are usually excluded from planned production time (they appear in TEEP).
- **MTBF** (Mean Time Between Failures) $= \dfrac{\text{Operating time}}{\text{No. of failures}}$; **MTTR** (Mean Time To Repair) $= \dfrac{\text{Total repair time}}{\text{No. of repairs}}$.
$$\text{Inherent availability} = \frac{MTBF}{MTBF + MTTR}$$
Levers: preventive/predictive maintenance (raise MTBF), **SMED** (cut setup), spares and skills (cut MTTR), autonomous maintenance.

### Example
A press ran 200 hours with 4 failures and 20 hours of repair time: $MTBF = 200/4 = 50$ hr, $MTTR = 20/4 = 5$ hr; $A = 50/55 = 90.9\%$. Cutting MTTR to 2.5 hr gives $50/52.5 = 95.2\%$, a gain of 4.3 points.

### In the news
See news box. A part shortage (Nexperia) acts as unplanned downtime for the line. Many OEE systems log material starvation as a separate loss category, so check how it is classified.

### Interview angle
> [!question] How it is asked
> "How would you reduce downtime on a critical machine?"

> [!tip] Strong answer includes
> - Split downtime into planned/unplanned with a Pareto of causes
> - MTBF vs MTTR levers
> - SMED for changeovers
> - Spares, training, predictive maintenance

---

## 5. Performance Loss
> 🔴 Tier 1 · _Tracker hint:_ Speed losses, micro-stops, reduced speed; ideal cycle time

### Definition
Performance loss occurs when the machine runs, but slower than its **ideal (design) cycle time**. Two types: **minor/micro-stops** (jams, sensor trips, short waits, typically under 5 minutes, often not logged as downtime) and **reduced speed** (running below rated speed because of worn tools, poor material, or operator caution).
$$P = \frac{\text{Ideal cycle time} \times \text{Total count}}{\text{Run time}} = \frac{\text{Actual rate}}{\text{Ideal rate}}$$
Pitfalls: if the "ideal cycle time" is set from historical average rather than design, OEE looks falsely high. Typical causes: poor material, operator practice, minor equipment problems, upstream/downstream blocking. Levers: auto-detect stops, root-cause on the top 5 micro-stops, tool wear management, standard speeds in SOPs.

### Example
Rated 60 units/min (ideal cycle 1 s). Run time 400 min; produced 21,600. $P = 21{,}600 / (60 \times 400) = 90\%$. Eliminating jams worth 1,200 units lifts $P$ to $22{,}800/24{,}000 = 95\%$.

### In the news
See news box. In a ramp-up like Hansalpur D, speed losses at start are common as lines move toward rated takt.

### Interview angle
> [!question] How it is asked
> "A line shows 95% availability but low OEE. Why?"

> [!tip] Strong answer includes
> - Micro-stops and slow running hidden inside "running" time
> - Check ideal cycle time validity
> - Quantify with automatic data capture
> - Fix top causes, standardise speed

---

## 6. Quality Loss
> 🔴 Tier 1 · _Tracker hint:_ First pass yield, scrap, rework; cost of poor quality

### Definition
Quality loss = time spent making units that are rejected or reworked. In OEE, **only first-pass good units count**; reworked units are loss.
$$Q = \frac{\text{Good units (first time)}}{\text{Total units}}$$
**First Pass Yield (FPY)** for a single step $=$ good-first-time / units started. **Rolled Throughput Yield (RTY)** for several steps $= \prod FPY_i$.

**Cost of Poor Quality (COPQ)**: internal failure (scrap, rework), external failure (returns, warranty, lost customers), appraisal (inspection) and prevention. COPQ is often 10–30% of sales in poorly controlled processes (a common textbook range). Levers: poka-yoke, SPC, standard work, supplier quality, root cause (8D, 5 Why).

### Example
Three process steps: FPY 95%, 97%, 98%. $RTY = 0.95 \times 0.97 \times 0.98 = 90.3\%$, so about 10 of every 100 units need rework or are scrapped, even though each step looks good. If a rework costs ₹150 and 10,000 units a month are started: $\approx 970 \times 150 = ₹1.46$ lakh per month.

### In the news
See news box. At Hansalpur's scale, even a 0.5-point improvement in first-pass quality across 1 million vehicles matters, a reason plants run strict quality gates.

### Interview angle
> [!question] How it is asked
> "A plant has 98% yield at each of 5 steps. What is the overall yield?"

> [!tip] Strong answer includes
> - $0.98^5 \approx 90.4\%$ (rolled throughput yield)
> - First pass vs after rework
> - COPQ categories
> - Prevent at source rather than inspect

---

## 7. Capacity Expansion Strategies
> 🔴 Tier 1 · _Tracker hint:_ Overtime, outsourcing, subcontracting, investment

### Definition
Choices differ by speed, cost and reversibility:
| Option | Speed | Cost per unit | Reversible? |
|---|---|---|---|
| **Overtime / extra shifts** | Immediate | High (premium pay, fatigue) | Yes |
| **Outsourcing / subcontracting** | Fast | Medium-high, quality/IP risk | Yes |
| **Process improvement / debottlenecking / OEE** | Medium | Low | Permanent |
| **Capacity investment (new line/plant)** | Slow (months to years) | Low once built | No (sunk) |

**Timing strategies:** **lead** (build ahead of demand: secure share, risk idle assets), **lag** (build after demand is proven: lower risk, may lose sales), **match** (incremental steps). Decide using break-even analysis, NPV and demand uncertainty; expand in *modules* to keep flexibility.

### Example
Demand exceeds capacity by 20,000 units/month for 4 months. Overtime costs ₹40 above the standard variable cost per unit: $20{,}000 \times 4 \times 40 = ₹32$ lakh. A new line costs ₹5 crore (and lasts years). For a temporary peak, overtime/subcontracting wins; if the excess is permanent, the line wins.

### In the news
See news box. Maruti chose a permanent investment (Plant D at about ₹3,900 crore, an estimate) which is consistent with durable demand and export volumes (Hansalpur handles about 47% of Maruti's export shipments); the company's own investment rationale is not quoted here.

### Interview angle
> [!question] How it is asked
> "Demand is growing 15% a year. How should the company expand capacity?"

> [!tip] Strong answer includes
> - Short-term (overtime, outsourcing) vs long-term (investment) options
> - Lead/lag/match strategies and risk
> - Debottleneck existing assets first
> - Financials: NPV, payback, scenarios

---

## 8. Resource Allocation
> 🔴 Tier 1 · _Tracker hint:_ Resource leveling vs resource loading; critical chain

### Definition
- **Resource loading:** shows how much work is assigned to each resource per period (the demand profile), highlighting **overloads** versus available capacity.
- **Resource leveling:** adjust the schedule (delay tasks within float, or extend duration) to resolve overloads, **at the cost of a possibly longer project**. 
- **Resource smoothing:** adjust within float only, **without changing the end date**.
- **Critical Chain Project Management (CCPM, Goldratt):** the longest chain considering **both task and resource dependencies**. Remove padding from individual tasks (student syndrome, Parkinson's Law), pool it into a **project buffer** at the end and **feeding buffers** where non-critical paths join. Typical sizing: cut task estimates by about 50% and set the project buffer to about half of the removed time.

Multi-project: allocate scarce resources to the project/task on the constraint first; avoid bad multitasking.

### Example
A resource is needed 12 hours/day on days 3-4 against a capacity of 8. Loading shows an overload of 4 hours per day. Leveling moves a 4-hour non-critical task to day 5. Total project time is unchanged if that task has at least 1 day float; otherwise the end date slips.

### In the news
See news box. A large capacity ramp like Hansalpur D is a multi-resource project (construction crews, tooling, supplier readiness) where leveling matters.

### Interview angle
> [!question] How it is asked
> "How do you handle resource conflicts across projects?"

> [!tip] Strong answer includes
> - Loading, then leveling vs smoothing
> - Priority rules and the effect on the critical path
> - Critical chain buffers
> - Reduce multitasking; visibility of resource plan

---

## 9. Constraint Management
> 🔴 Tier 1 · _Tracker hint:_ DBR, buffer management; subordinate to constraint

### Definition
Manage the system by managing its **constraint** (Theory of Constraints, see [[017 Process Management & Optimization]]). **Drum-Buffer-Rope (DBR):**
- **Drum:** the constraint's schedule sets the pace of the whole plant.
- **Buffer:** a time buffer of work placed **before** the constraint (and shipping) so it never starves.
- **Rope:** a signal that releases raw material at the rate the constraint consumes it, which limits WIP.

**Buffer management:** divide the buffer into three zones: **green** (first third, ok), **yellow** (middle: watch), **red** (last third: expedite). Track which resources cause buffer penetrations, then fix those. **Subordinate:** other resources run only at the constraint's pace; their "idle" time is not waste. Measures: **throughput (T)**, **inventory (I)** and **operating expense (OE)**, with $\text{Net profit} = T - OE$.

### Example
Constraint (paint) runs 45 units/hr. Time buffer 12 hours before paint, split in 4-hour zones. When jobs due in 4 hours are still not at paint (red), the planner expedites them. Upstream shops are only released 12 hours before they are needed, so WIP stays low.

### In the news
See news box. After Nexperia, firms effectively treated one chip as the constraint and rationed it to the highest-margin models (throughput per constrained unit).

### Interview angle
> [!question] How it is asked
> "Explain drum-buffer-rope" or "How do you decide which product to make when one resource is scarce?"

> [!tip] Strong answer includes
> - Drum, buffer, rope with purpose
> - Subordination: don't maximise non-constraint utilisation
> - Product mix by throughput per constraint minute
> - Buffer zones for control

---

## 10. Overall Equipment Effectiveness (OEE) Improvement
> 🔴 Tier 1 · _Tracker hint:_ Pillar-wise TPM improvement plan

### Definition
**Total Productive Maintenance (TPM)** (JIPM) is the system for improving OEE with eight pillars:
1. **Autonomous maintenance (Jishu Hozen):** operators clean, inspect, lubricate.
2. **Focused (planned) improvement (Kobetsu Kaizen):** project teams attack the Six Big Losses.
3. **Planned maintenance:** preventive and predictive.
4. **Quality maintenance (Hinshitsu Hozen):** build quality into the machine (poka-yoke).
5. **Early equipment / product management:** design for maintainability.
6. **Training and education.**
7. **TPM in administration (office TPM).**
8. **Safety, health and environment.**

Plan: baseline OEE → Pareto of losses → assign pillars to losses → quick wins (5S, cleaning, lubrication standards) → deeper fixes (SMED, root cause) → standardise (SOPs/OPLs) → track weekly.

| Loss | Main pillar action |
|---|---|
| Breakdowns | Autonomous + planned maintenance |
| Setups | Focused improvement (SMED) |
| Minor stops/speed | Autonomous maintenance, focused improvement |
| Defects | Quality maintenance |

### Example
Baseline: A 85%, P 80%, Q 95%: $OEE = 0.85 \times 0.80 \times 0.95 = 64.6\%$. Target after TPM: A 90%, P 90%, Q 97%: $0.90 \times 0.90 \times 0.97 = 78.6\%$. If the machine sells all it makes at ₹500 contribution per unit and ideal output is 10,000 units/month, extra good units $\approx 10{,}000 \times (0.786 - 0.646) = 1{,}400$, i.e. ₹7 lakh per month without new capital.

### In the news
See news box. Squeezing OEE is "capacity you already paid for": 10 points of OEE equals about a 15% capacity gain at 65% base (0.10/0.65), versus a ₹3,900 crore plant investment (estimated) for Plant D.

### Interview angle
> [!question] How it is asked
> "Your plant's OEE is 55%. Build an improvement plan."

> [!tip] Strong answer includes
> - Baseline and Pareto of Six Big Losses
> - Pillar-wise actions mapped to losses
> - Operator ownership and standard work
> - Financial value of OEE points and sustaining via reviews

---

## 11. ⭐ Advanced: Capacity Planning with Product Mix and Break-even
> ⭐ Advanced · _Added beyond the tracker_

### Definition
When the bottleneck serves several products, decide the mix by **contribution per bottleneck minute**, not per unit:
$$\text{Contribution per constraint minute} = \frac{\text{Price} - \text{Truly variable cost}}{\text{Minutes on constraint}}$$
Rank products and fill the constraint's available time in that order until demand is met (a simple LP). Also use **break-even volume** $Q_{BE} = \dfrac{F}{p - v}$ for deciding whether capacity pays, and **capacity requirement** $= \dfrac{\text{Demand} \times \text{Processing time}}{\text{Available time} \times \text{Efficiency}}$.

### Example
Constraint available: 2,400 min/week. Product X: contribution ₹300, 10 min → ₹30/min, demand 150. Product Y: contribution ₹200, 5 min → ₹40/min, demand 300. Fill Y first: $300 \times 5 = 1{,}500$ min; remaining 900 min to X: 90 units. Contribution $= 300 \times 200 + 90 \times 300 = 60{,}000 + 27{,}000 = ₹87{,}000$. (X-first would give $150 \times 300 + 180 \times 200 = 45{,}000 + 36{,}000 = ₹81{,}000$.) Machines needed for demand: $(150 \times 10 + 300 \times 5)/2{,}400 = 3{,}000/2{,}400 = 1.25$, so 2 machines (or overtime).

### In the news
See news box. Allocation of scarce chips to highest-margin models after Nexperia is the same logic.

### Interview angle
> [!question] How it is asked
> "With limited machine hours, which products do you prioritise?"

> [!tip] Strong answer includes
> - Contribution per constraint unit, not per unit sold
> - Demand limits and sequencing
> - Check customer commitments and strategic products
> - Capacity requirement calculation and rounding to whole machines

---

## 12. ⭐ Advanced: TEEP, OLE and Loss Trees
> ⭐ Advanced · _Added beyond the tracker_

### Definition
OEE only covers **scheduled** time. **TEEP** shows asset utilisation against all calendar time:
$$TEEP = OEE \times \text{Utilisation (loading)}, \qquad \text{Loading} = \frac{\text{Planned production time}}{\text{Calendar time}}$$
**OLE (Overall Labour Effectiveness)** applies the same A×P×Q logic to people. A **loss tree** breaks 100% of calendar time into: not scheduled → planned stops → availability losses → speed losses → quality losses → fully productive time. Use to decide whether to **improve OEE** or **add shifts** (raise loading): if TEEP is 30% because machines run only one shift, adding a shift may be cheaper than a new plant.

### Example
A machine runs 1 shift of 8 hr in a 24-hr day (loading $= 33.3\%$) at OEE 75%: $TEEP = 25\%$. Adding a second shift at the same OEE raises TEEP to 50% with no new equipment; capex per extra unit is zero, only labour is added.

### In the news
See news box. Hansalpur's added plant (capex) vs squeezing existing assets via shifts/OEE: the TEEP view tells which is cheaper.

### Interview angle
> [!question] How it is asked
> "A CEO wants to build a second plant. What do you check first?"

> [!tip] Strong answer includes
> - TEEP and loss tree of existing plant
> - Cheapest capacity first: OEE, shifts, debottlenecking
> - Demand certainty and capex payback
> - Qualitative: customers, supply of skills, risk

---
## 🔗 Go deeper: expansion notes
- [[155 Reliability Engineering & Maintenance Optimisation|Reliability Engineering & Maintenance Optimisation]]
- [[149 Queueing Theory & Waiting-Line Analysis|Queueing Theory & Waiting-Line Analysis]]
