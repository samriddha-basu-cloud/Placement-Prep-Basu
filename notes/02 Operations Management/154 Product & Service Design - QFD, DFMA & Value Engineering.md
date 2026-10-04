---
tags: [operations-management, tier2]
area: Operations Management
topic: "Product & Service Design - QFD, DFMA & Value Engineering"
tier: Tier 2
roles: Operations / PM / Consulting
status: complete
subtopics: 13
---
# Product & Service Design - QFD, DFMA & Value Engineering

⬅ [[153 Aggregate Planning Models & Workforce Strategy]] · [[_Index - Operations Management|Operations Management]] · [[155 Reliability Engineering & Maintenance Optimisation]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / PM / Consulting

## Sub-topics in this note
1. [[#1. New Product Development Process and Stage-Gate]]
2. [[#2. Voice of the Customer and the Kano Model]]
3. [[#3. Quality Function Deployment and the House of Quality]]
4. [[#4. Target Costing and Design-to-Cost]]
5. [[#5. Design for Manufacture and Assembly (DFMA)]]
6. [[#6. Value Analysis and Value Engineering]]
7. [[#7. Concurrent Engineering and Early Supplier Involvement]]
8. [[#8. Taguchi Robust Design and the Loss Function]]
9. [[#9. Design for Reliability, Serviceability and Sustainability]]
10. [[#10. Modular Design, Platforms and Variety Management]]
11. [[#11. Prototyping, Pilot Lots and Ramp-up]]
12. [[#12. Product Lifecycle Cost and Total Cost of Ownership]]
13. [[#13. ⭐ Advanced: Service Design with QFD, Blueprinting and Robustness]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): design decisions fix cost, and the market punishes design that misses the customer
> **Gigacasting: a DFMA case at industrial scale.** Tesla's Giga Press approach replaces a vehicle underbody assembled from many stamped parts with a large single casting: for the Model Y rear underbody, **over 70 parts became one casting**, and the cycle is about **80-90 seconds per casting**. Volvo ordered two 9,000-tonne machines for Slovakia (November 2023) and Toyota announced large-casting plans for EVs (June 2023). Yet in **May 2024 Tesla reportedly retreated from single-piece casting for some designs**, reverting to a three-piece structure, a reminder that part-count reduction trades off against tooling cost (about **$1.5 million** per mold, per the source), repairability and scale. ([Wikipedia: Giga Press](https://en.wikipedia.org/wiki/Giga_Press))
>
> **Tata Nano: target costing without a market fit.** Launched 10 January 2008 at a target of ₹1 lakh, the Nano cut cost through design choices (one wiper, one wing mirror on base models, three wheel nuts instead of four, no airbags or air conditioning in the base variant). Sales peaked at **74,527 units in FY2011-12**, fell to **7,591 in FY2016-17**, and production wound down in 2018. The page attributes the failure to a "poor man's car" perception, safety and quality concerns and long waits. ([Wikipedia: Tata Nano](https://en.wikipedia.org/wiki/Tata_Nano))
>
> **Dyson: persistence in prototyping, discipline at the gate.** Dyson built **5,127 prototypes between 1979 and 1984** before its cyclonic bagless vacuum worked, and discontinued its electric-car project in **October 2019**, calling it technically sound but "not commercially viable"; 2025 revenue is reported at **£6.13 billion**. ([Wikipedia: Dyson](https://en.wikipedia.org/wiki/Dyson_(company)))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. New Product Development Process and Stage-Gate
> 🟠 Tier 2 · _Key points:_ Idea to launch; gates; attrition funnel; expected commercial value

### Definition
**New product development (NPD)** is the sequence from idea to market launch. Cooper's **Stage-Gate** model divides it into stages (discovery, scoping, build business case, development, testing and validation, launch) separated by **gates**, decision points where a cross-functional panel applies criteria (strategic fit, market attractiveness, technical feasibility, financial return, risk) and chooses go, kill, hold or recycle. Good gates kill weak projects early, when spend is low. Newer variants (Agile-Stage-Gate, spirals) use short sprints inside stages.

A common financial gate metric is **expected commercial value (ECV)**:
$$ECV = \left[ PV_{\text{commercial}} \times P_{cs} - C_{\text{commercialisation}} \right] \times P_{ts} - D$$
with $P_{ts}$ the probability of technical success, $P_{cs}$ the probability of commercial success given technical success, $D$ the remaining development cost. Link to NPV ([[109 Valuation Basics (NPV, IRR, DCF)]]) and capital budgeting ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]). Product management view: [[037 PM Fundamentals & Lifecycle]], [[164 Product Discovery & User Research]].

### Example
Funnel: 100 ideas, 40 scoped, 16 get a business case, 8 enter development, 5 reach testing, 4 launch. Stage costs per project (₹ lakh): screen 0.05, scoping 0.2, business case 0.6, development 4.0, testing 2.0, launch 6.0. Total spend $= 100(0.05) + 40(0.2) + 16(0.6) + 8(4.0) + 5(2.0) + 4(6.0) = 5 + 8 + 9.6 + 32 + 10 + 24 = ₹88.6$ lakh, so **₹22.15 lakh per launched product**, and only about 25% of the spend ($5 + 8 + 9.6 = ₹22.6$ lakh) is committed before the expensive development stage begins. ECV example (₹ crore): $PV = 60$, $P_{cs} = 0.7$, commercialisation 8, $P_{ts} = 0.8$, $D = 5$: $ECV = (60 \times 0.7 - 8) \times 0.8 - 5 = ₹22.2$ crore, positive, so go.

### In the news
See news box. Dyson's EV cancellation is a late kill, expensive in hindsight but still better than launching a product the company judged not commercially viable.

### Interview angle
> [!question] How it is asked
> "How would you decide which of five new-product ideas to fund?"

> [!tip] Strong answer includes
> - Stage-gate with explicit criteria and kill rules
> - ECV or risk-adjusted NPV at each gate, with probabilities stated as estimates
> - Cheap learning first (customer research, prototypes), costly commitments later
> - Portfolio view: balance risk, strategic fit and resource constraints

---

## 2. Voice of the Customer and the Kano Model
> 🟠 Tier 2 · _Key points:_ Must-be, one-dimensional, attractive, indifferent; satisfaction coefficients

### Definition
Design starts with **voice of the customer (VOC)**: interviews, observation, complaints, surveys, field data and analytics. **Kano** (1984) classifies needs by their effect on satisfaction:
- **Must-be (basic):** expected; absence causes dissatisfaction, presence does not delight (brakes work).
- **One-dimensional (performance):** more is better, linear (fuel economy, battery life).
- **Attractive (delighters):** unexpected, no dissatisfaction if absent (a smart feature nobody asked for).
- **Indifferent / reverse:** no effect or some customers dislike it.
Needs drift: today's delighter is tomorrow's must-be (touchscreens, ABS). The **Kano questionnaire** asks a functional ("how would you feel if the feature were present") and dysfunctional question for each feature. Berger's coefficients, with counts of attractive $A$, one-dimensional $O$, must-be $M$, indifferent $I$:
$$\text{Better} = \frac{A + O}{A + O + M + I}, \qquad \text{Worse} = -\frac{O + M}{A + O + M + I}$$
See also [[033 Design Thinking & UX]] and the prioritisation methods in [[034 Prioritization Frameworks]].

### Example
100 respondents rate a "one-tap reorder" feature: $A = 30$, $O = 25$, $M = 35$, $I = 10$. Better $= 55/100 = 0.55$; Worse $= -60/100 = -0.60$. High on both: customers punish absence and reward presence, so it is a must-have, not a delighter. If instead $A = 55$, $M = 5$, $O = 15$, $I = 25$: Better $= 0.70$, Worse $= -0.20$, a delighter to fund if cost is small.

### In the news
See news box. The Nano met a cost-and-price need but missed an emotional "status" need that Kano-style research on the buyer segment would likely have flagged as a must-be for car buyers moving up from two-wheelers (an interpretation, not a quoted finding).

### Interview angle
> [!question] How it is asked
> "How would you prioritise features using customer input?"

> [!tip] Strong answer includes
> - Kano categories and the questionnaire method with a numeric example
> - Fund must-be first, then performance, then selected delighters
> - Reclassify over time (delighters decay)
> - Combine with cost and feasibility (QFD, next)

---

## 3. Quality Function Deployment and the House of Quality
> 🟠 Tier 2 · _Key points:_ Customer needs to engineering characteristics; 9-3-1 matrix; roof; four houses

### Definition
**QFD** (Akao, Japan, 1960s; Mitsubishi Kobe shipyard, then Toyota) translates the voice of the customer into design and process targets. The **House of Quality (HoQ)** has these rooms:
1. **Whats:** customer needs with **importance weights** (1-5).
2. **Hows:** measurable engineering characteristics.
3. **Relationship matrix:** strength of link (9 strong, 3 medium, 1 weak, blank none).
4. **Roof:** correlation among hows (positive or negative trade-offs).
5. **Competitive assessment** (customer perception vs competitors) and **targets** ("how much").
6. **Importance rating** of each how: $\sum_i w_i \times r_{ij}$, then relative weight.
QFD cascades through four houses: product planning, part deployment, process planning, production planning. It connects to [[011 Quality Management (TQM)]] and APQP ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### Example
Pressure cooker for Indian kitchens. Needs and weights: cooks fast 5, safe 5, easy to clean 3, lightweight 2, long life 4. Hows: time to full pressure, safety-valve and lid-lock reliability, inner-surface finish, body weight, gasket life. Relationship scores (rows are needs):

| Need (weight) | Time to pressure | Safety reliability | Surface finish | Weight | Gasket life |
|---|---|---|---|---|---|
| Fast (5) | 9 | 0 | 0 | 3 | 0 |
| Safe (5) | 3 | 9 | 0 | 0 | 3 |
| Easy to clean (3) | 0 | 0 | 9 | 1 | 0 |
| Lightweight (2) | 3 | 0 | 0 | 9 | 0 |
| Long life (4) | 0 | 3 | 3 | 1 | 9 |
| **Importance** | **66** | **57** | **39** | **40** | **51** |
| Relative weight | 26.1% | 22.5% | 15.4% | 15.8% | 20.2% |

Time to pressure: $5 \times 9 + 5 \times 3 + 2 \times 3 = 66$; safety reliability: $5 \times 9 + 4 \times 3 = 57$; gasket life: $5 \times 3 + 4 \times 9 = 51$. Priority engineering effort: time to pressure, safety reliability, gasket life. Roof: lighter body (thin walls) conflicts with safety strength, a negative correlation to resolve with material choice.

### In the news
See news box. A house of quality for a ₹1 lakh car would have made the trade-off between "low price" and "safety and status" explicit before the specification was frozen (interpretation, not a source claim).

### Interview angle
> [!question] How it is asked
> "Walk me through how you would use QFD to design a new product."

> [!tip] Strong answer includes
> - Whats, hows, relationship matrix, roof, importance score, targets
> - A numeric example with weights and 9-3-1
> - Handling conflicts (roof) and benchmarking
> - Limits: subjective scores, large matrices; use as a communication tool

---

## 4. Target Costing and Design-to-Cost
> 🟠 Tier 2 · _Key points:_ Price minus margin; allocate by function; close the gap

### Definition
**Target costing** (Toyota; Japanese manufacturers) works backwards from the market:
$$\text{Target cost} = \text{Target selling price} - \text{Target profit margin}$$
The team compares the **current estimated cost** with the target, then closes the **cost gap** by design change, value engineering, supplier collaboration and process improvement, allocating the target to subsystems by function importance. It contrasts with cost-plus pricing (cost first, then price). Related: **design-to-cost** (hard cost target per unit as a design requirement), **kaizen costing** (post-launch reductions) and **frugal innovation** (Indian examples: low-cost vehicles, cooking stoves, devices). See [[110 Cost Accounting for Operations]] and [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]].

### Example
Target price ₹1,00,000 and target margin 8%: target cost $= 1{,}00{,}000 \times (1 - 0.08) = ₹92{,}000$. Current estimate ₹1,06,000: gap ₹14,000 (13.2% of current cost). Closing the gap: design simplification ₹6,000, materials substitution ₹3,500, supplier price-down through volume commitments ₹2,500, process cost ₹2,000 = ₹14,000. Track each line as a project with an owner. A gap closed by deleting something customers value (the Nano's lesson) is a loss, so protect functions with high importance and cut those with low worth.

### In the news
See news box. The Nano's published design cuts show target costing in action, and its market outcome shows the limits when the cuts erode perceived value or safety.

### Interview angle
> [!question] How it is asked
> "Your product costs ₹1,200 and the market will pay ₹1,000 at 15% margin. What do you do?"

> [!tip] Strong answer includes
> - Target cost $= 1{,}000 \times 0.85 = ₹850$; gap ₹350 (29% of cost)
> - Breakdown of the gap by BOM, process, logistics, packaging; VE on low-worth functions
> - Question the price positioning and volume if the gap cannot be closed
> - Protect the features customers value; check regulatory minimums

---

## 5. Design for Manufacture and Assembly (DFMA)
> 🟠 Tier 2 · _Key points:_ Part-count reduction; Boothroyd-Dewhurst efficiency; poka-yoke

### Definition
**DFM** simplifies making each part (tolerances, materials, processes, standard components); **DFA** simplifies putting parts together; **DFMA** does both early. Principles: minimise part count; standardise parts and fasteners; modular subassemblies; design for symmetry or clear orientation; self-locating, snap-fit, one-direction assembly (top-down); avoid tight tolerances unless needed; mistake-proof (poka-yoke). The Boothroyd-Dewhurst test for a theoretical minimum part count asks of each part: does it move relative to others, must it be of a different material, must it be separate for assembly or service? If none, merge it.

$$\text{Design efficiency} = \frac{3\, N_{\min}}{t_a}$$
where $N_{\min}$ is the theoretical minimum number of parts and $t_a$ the total assembly time in seconds (3 seconds is the ideal time per part). Part reduction cuts inventory, suppliers, quality risk and assembly labour (see [[007 Lean Manufacturing]]).

### Example
Original design: 30 parts, $N_{\min} = 12$, assembly time 150 s: efficiency $= 3 \times 12/150 = 24\%$. Redesign: 14 parts, assembly 60 s: efficiency $= 3 \times 12/60 = 60\%$. Time saved 90 s; at ₹300 per hour (₹0.0833 per second) that is $90 \times 300/3600 = ₹7.5$ per unit; at 10 lakh units a year, ₹75 lakh in assembly labour alone, before savings on 16 fewer part numbers to buy, stock and inspect. Offset: if the merged parts need a ₹1.2 crore tool, payback on labour alone is about 1.6 years ($1.2/0.75$).

### In the news
See news box. Gigacasting is DFMA taken to the limit (70+ parts to 1), with the trade-off of high tooling cost, scrap risk when a large casting fails inspection, and repair difficulty.

### Interview angle
> [!question] How it is asked
> "How would you reduce assembly cost for a product with 80 parts?"

> [!tip] Strong answer includes
> - Minimum part-count analysis and design efficiency
> - Merge, standardise, simplify fastening, orientation, poka-yoke
> - Business case: labour, inventory, quality, tooling and repairability
> - Involve suppliers and manufacturing early (concurrent engineering)

---

## 6. Value Analysis and Value Engineering
> 🟠 Tier 2 · _Key points:_ Function-cost-worth; Miles at GE; FAST; value index

### Definition
**Value analysis (VA)** examines an existing product; **value engineering (VE)** applies the same method at the design stage (Lawrence Miles, General Electric, 1940s). Value is the ratio of function (performance) to cost:
$$\text{Value} = \frac{\text{Function (or performance)}}{\text{Cost}}, \qquad \text{Value index} = \frac{\text{Cost}}{\text{Worth}}$$
**Worth** is the lowest cost at which the function can be reliably provided. A value index well above 1 flags overspend. Steps (job plan): information; **function analysis** (describe each function as verb plus noun, classify primary or secondary, build a **FAST** diagram); creativity (brainstorm alternatives for each function); evaluation; development; presentation and implementation. Rules: challenge every cost with "does it contribute to value?", use standard parts, consider cheaper materials and processes, and involve suppliers (see [[122 Spend Analysis, Savings & Procurement Maturity]]). VE reduces cost without reducing function or quality, which is different from plain cost cutting.

### Example
Electric kettle, costs and worth by function (₹):

| Function | Cost | Worth | Value index | Savings potential |
|---|---|---|---|---|
| Hold water | 120 | 100 | 1.20 | 20 |
| Heat water | 200 | 130 | 1.54 | 70 |
| Switch off at boil | 90 | 35 | 2.57 | 55 |
| Pour safely | 60 | 45 | 1.33 | 15 |
| Look attractive | 130 | 60 | 2.17 | 70 |
| **Total** | **600** | **370** | **1.62** | **230 (38%)** |

Targets: "switch off at boil" (index 2.57: replace a custom assembly with a standard bimetal thermostat) and "look attractive" (2.17: fewer colours and moulded-in finish). Saving 230 would be ideal; a practical target might be ₹120-150 after trials. Customer-valued functions (safe pouring, boil-dry protection) are protected.

### In the news
See news box. Nano and Giga Press are both VE stories: one removed functions customers valued, the other redesigned a function (structure) with fewer parts but risked repair cost.

### Interview angle
> [!question] How it is asked
> "Difference between value engineering and cost cutting?"

> [!tip] Strong answer includes
> - Function-based thinking: cost versus worth for each function, not part by part
> - Process: function analysis, creativity, evaluation, with FAST
> - Maintains quality and customer-valued functions, supplier input
> - Quantified example with value index and savings

---

## 7. Concurrent Engineering and Early Supplier Involvement
> 🟠 Tier 2 · _Key points:_ Cross-functional teams; overlap; cost committed early; DSM

### Definition
**Concurrent (simultaneous) engineering** runs design, process, tooling, sourcing and service planning in parallel using cross-functional teams, instead of "throwing the design over the wall" to manufacturing. Elements: integrated product teams, **early supplier involvement (ESI)**, design reviews against DFMA and VE, shared digital models (PLM/CAD), and clear interface management. A widely quoted rule of thumb says that the **majority of a product's lifecycle cost (often cited as 70-80%) is determined in the design stage**, though the exact share varies by product, so design changes are cheapest early. The **design structure matrix (DSM)** shows task dependencies and highlights iteration loops to be decoupled.

Risks: coordination overhead, premature freeze of interfaces, rework when assumptions change. Mitigations: set-based design (keep options open), modular interfaces, staged freezes. Project-scheduling view: [[039 Scheduling Tools (CPM-PERT-Gantt)]].

### Example
Sequential schedule: concept 3 months, detailed design 6, tooling 6, pilot 3 = 18 months. With concurrent engineering, tooling starts after 3 months of design (overlap of 3) and the pilot starts 2 months before tooling ends (overlap of 2): 18 − 5 = 13 months. If every month of delay costs ₹30 lakh in lost contribution, the 5 months saved are worth ₹1.5 crore; extra cost of the dedicated team and some tool rework ₹40 lakh, net ₹1.1 crore. If rework risk rises with overlap, check the downside case (say 2 months of rework wipes out 40% of the saving).

### In the news
See news box. Large-casting programmes need design, tooling and process to be developed together; the reported 2024 step back shows how a bold bet can still be reversed when economics change.

### Interview angle
> [!question] How it is asked
> "How can you cut time-to-market without hurting quality?"

> [!tip] Strong answer includes
> - Cross-functional teams, overlap, ESI, early DFMA reviews
> - Cost of delay quantified against the extra cost
> - Interfaces and decision freezes managed with DSM or gates
> - Risk plan for rework and a fallback design

---

## 8. Taguchi Robust Design and the Loss Function
> 🟠 Tier 2 · _Key points:_ Loss grows quadratically from target; control and noise factors; S/N ratio

### Definition
Genichi Taguchi's idea: quality is the **loss imparted to society** after shipment; any deviation from the target $m$ costs something, not only items outside specification. The **quadratic loss function**:
$$L(y) = k\,(y - m)^2, \qquad k = \frac{A_0}{\Delta_0^2}$$
where $A_0$ is the cost at the tolerance limit $m \pm \Delta_0$ (scrap, rework or repair). For a population with mean $\mu$ and variance $\sigma^2$, the **average loss** is
$$E[L] = k\left[\sigma^2 + (\mu - m)^2\right]$$
Variants: smaller-the-better $L = k y^2$; larger-the-better $L = k/y^2$.

**Robust design:** choose levels of **control factors** so the response is insensitive to **noise factors** (temperature, wear, material variation, user behaviour) using orthogonal-array experiments (details in [[213 Design of Experiments - Factorial, Fractional & Taguchi]]). **Signal-to-noise ratios** for nominal-the-best: $S/N = 10 \log_{10}(\bar y^2/s^2)$; smaller-the-better: $-10\log_{10}(\sum y^2/n)$; larger-the-better: $-10\log_{10}\left(\sum (1/y^2)/n\right)$. Three design stages: system design, **parameter design** (cheap, set nominal values for robustness), **tolerance design** (tighten tolerances only where needed). Links: [[008 Six Sigma & Quality Tools]], [[091 Statistical Quality Control (SQC)]].

### Example
Shaft target $m = 20.00$ mm, tolerance $\pm 0.05$ mm, cost at the limit ₹400. $k = 400/0.05^2 = ₹1{,}60{,}000$ per mm². Three processes, all inside tolerance on average:
- A: centred, $\sigma = 0.02$: $E[L] = 160{,}000 \times 0.02^2 = ₹64$ per part.
- B: mean 20.02, $\sigma = 0.01$: $160{,}000(0.01^2 + 0.02^2) = ₹80$.
- D: centred, $\sigma = 0.01$: $₹16$.
Process B has half the spread of A but costs more, because it is off target; recentring it gives ₹16, a 80% reduction in loss. A part at 20.03 mm (inside spec) already carries a loss of $160{,}000 \times 0.03^2 = ₹144$: the goalpost view (zero loss anywhere inside spec) misses this.

### In the news
See news box. With a single large casting, one out-of-tolerance part scraps what used to be many small parts, so robust design and process control matter more (a design implication, not a claim from the source).

### Interview angle
> [!question] How it is asked
> "Why is meeting the specification not enough, according to Taguchi?"

> [!tip] Strong answer includes
> - Quadratic loss and the numeric $k$ from the cost at the tolerance limit
> - Average loss splits into variance plus bias squared: reduce both
> - Robust design via control vs noise factors and parameter design before tolerance design
> - Link to process capability and Six Sigma

---

## 9. Design for Reliability, Serviceability and Sustainability
> 🟠 Tier 2 · _Key points:_ Series/parallel; MTTR; right-to-repair; lifecycle materials

### Definition
**Design for reliability (DfR):** specify a reliability target (probability of survival to time $t$), use derating, redundancy for critical functions, FMEA, accelerated life tests and burn-in. For $n$ independent components in series, $R_s = \prod R_i$; for two in parallel, $R_p = 1 - (1 - R_1)(1 - R_2)$. See [[155 Reliability Engineering & Maintenance Optimisation]] and [[211 Reliability & Survival Analysis]].

**Design for serviceability / maintainability:** easy access, standard tools, modular replaceable units, diagnostics, labelled test points, low MTTR; supports uptime in [[018 Capacity Management & OEE]] and [[022 Maintenance Management (TPM-RCM)]].

**Design for sustainability / environment:** material selection, recyclability and disassembly, energy efficiency in use, lighter packaging, remanufacturability; in India, **Extended Producer Responsibility (EPR)** rules for plastics, e-waste and batteries make end-of-life a design input (see [[135 Reverse Logistics, Remanufacturing & EPR in India]]).

### Example
A product has 10 critical components in series. If all ten have reliability 0.99 over the warranty, $R_s = 0.99^{10} = 0.904$. Now suppose nine parts have 0.99 and one weak part has 0.90: $R_s = 0.99^9 \times 0.90 = 0.9135 \times 0.90 = 0.822$, so 17.8% fail in warranty. Duplicating only the weak part in parallel gives $1 - 0.1^2 = 0.99$ for that function and $R_s = 0.9135 \times 0.99 = 0.904$: a gain of 8 points from one cheap change, which beats trying to raise all ten parts a little.

### In the news
See news box. Fewer parts and joints can help reliability, but a damaged large casting is harder to repair than a replaceable panel: a serviceability trade-off to weigh (a design implication, not a claim from the source).

### Interview angle
> [!question] How it is asked
> "How would you improve reliability in a design without raising cost much?"

> [!tip] Strong answer includes
> - Find the weakest link in the series model and fix or duplicate only that
> - FMEA, derating and testing; reliability targets tied to warranty cost
> - Serviceability (MTTR, modularity) and end-of-life (EPR) as design goals
> - Cost-benefit using warranty and lifecycle cost

---

## 10. Modular Design, Platforms and Variety Management
> 🟠 Tier 2 · _Key points:_ Modules; platform commonality; mass customisation; postponement

### Definition
**Modular design** builds products from standard modules with standard interfaces so many variants arise from a small set of modules: variety for the customer, commonality for operations. A **platform** shares architecture and key components across a product family (automotive platforms, electronics, appliances). Benefits: lower design and tooling cost, economies of scale in components, faster launches, easier service and upgrade, **postponement** (delay differentiation to the final step; see [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]). Risks: over-standardisation (products feel the same), performance penalty from carry-over, platform lock-in, and higher up-front investment. Indian carmakers use shared platforms across several models to spread development cost over volume.

### Example
A hatchback offered with 5 body colours, 4 engine-gearbox options and 3 trim levels: 60 customer variants but only $5 + 4 + 3 = 12$ modules to design, stock and manage if the interfaces are standard. If each variant instead needed a unique design costing ₹50 lakh, 60 variants cost ₹30 crore; with modular design the 12 modules cost ₹40 lakh each ($= ₹4.8$ crore) plus ₹5 crore for the platform: ₹9.8 crore, a saving of about 67% (illustrative figures).

### In the news
See news box. Gigacasting is an integral (non-modular) architecture decision, with the opposite trade-off: fewer parts, but less flexibility for variants and repair.

### Interview angle
> [!question] How it is asked
> "How would you reduce complexity in a product range with 500 SKUs?"

> [!tip] Strong answer includes
> - Variety analysis (Pareto of sales and cost-to-serve), commonality and modularity
> - Platform and postponement strategies
> - Cost vs customer value of each option
> - Governance: option rules, phase-out discipline

---

## 11. Prototyping, Pilot Lots and Ramp-up
> 🟠 Tier 2 · _Key points:_ Fail early; EVT/DVT/PVT; pilot build; yield and learning curve

### Definition
**Prototyping** reduces uncertainty cheaply: sketches and mock-ups (looks-like), functional rigs (works-like), full prototypes, and rapid prototyping or 3D printing; digital twins and simulation reduce physical iterations. Hardware programmes often follow engineering, design and production validation builds (EVT, DVT, PVT). A **pilot lot** (limited production on the real line with real tooling) tests process capability, assembly time, supplier parts, packaging and quality before **ramp-up** to volume. Automotive and industrial programmes use APQP and PPAP ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]) to prove process capability before full-rate production. **Ramp-up** is the period from first saleable unit to target volume and yield; early weeks carry lower yield and slower cycle times, following the learning curve ([[152 Learning Curves, Work Measurement & Productivity]]).

### Example
Launch plan for 10,000 units a month at 95% first-pass yield. Weekly yield: 70%, 80%, 88%, 93%, then 95%; weekly line output capacity 2,500 units. Good units in the first four weeks: $2{,}500 \times (0.70 + 0.80 + 0.88 + 0.93) = 2{,}500 \times 3.31 = 8{,}275$ against a plan of 9,500 ($2{,}500 \times 4 \times 0.95$): shortfall 1,225 units. If contribution is ₹800 per unit, the ramp-up costs ₹9.8 lakh in month one. A pilot lot that finds the first two problems earlier is worth that much in avoided shortfall. Cost of delay: a product earning ₹40 crore a year contribution delayed 3 months loses ₹10 crore, which usually exceeds the cost of an extra prototype iteration.

### In the news
See news box. Dyson's 5,127 prototypes show learning through many cheap iterations; Giga Press moulds cost about $1.5 million each per the source, which is why the industry invests in simulation and prototyping before cutting steel.

### Interview angle
> [!question] How it is asked
> "How would you manage a new product launch so the factory ramp-up is smooth?"

> [!tip] Strong answer includes
> - Prototype series, pilot lot, design freeze and supplier PPAP before volume
> - Ramp plan with yield and rate targets by week; war-room and quick response
> - Learning-curve expectations and staffing, with a cost-of-delay view
> - Contingency (safety stock, dual source) and lessons learned

---

## 12. Product Lifecycle Cost and Total Cost of Ownership
> 🟠 Tier 2 · _Key points:_ Acquisition plus operating plus end-of-life; discounting; design locks cost

### Definition
**Lifecycle cost (LCC)** or **total cost of ownership (TCO)** sums all costs over a product's life: development, acquisition, installation, operation (energy, labour, consumables), maintenance, downtime, and disposal, less salvage, discounted to present value at the cost of capital:
$$LCC = C_0 + \sum_{t=1}^{n} \frac{C_t^{\text{operate}} + C_t^{\text{maintain}}}{(1+r)^t} - \frac{\text{Salvage}}{(1+r)^n}$$
Designers use it to choose between a cheaper-to-buy and cheaper-to-run option; buyers use it in tenders (L1 on price alone can be a poor decision). The **product lifecycle (PLC)** view (introduction, growth, maturity, decline) shapes design: early designs for flexibility, mature products for cost. See [[042 Cost & Budget Management]] and [[109 Valuation Basics (NPV, IRR, DCF)]].

### Example
Two machines over 8 years at 10% discount rate (annuity factor 5.335), in ₹ lakh: A: price 10, energy 1.8 a year, maintenance 0.8 a year, salvage 1 (discounted $1/1.1^8 = 0.466$): $LCC_A = 10 + (1.8 + 0.8) \times 5.335 - 0.466 = ₹23.40$ lakh. B: price 14, energy 1.0, maintenance 0.5, salvage 2 (0.933): $LCC_B = 14 + 1.5 \times 5.335 - 0.933 = ₹21.07$ lakh. B costs ₹4 lakh more up front but is ₹2.33 lakh cheaper over life. Annual operating saving of B $= (1.8 + 0.8) - (1.0 + 0.5) = ₹1.1$ lakh, so simple payback of the extra ₹4 lakh is $4/1.1 = 3.6$ years, within the 8-year life. Check: $1.1 \times 5.335 - 4 + (0.933 - 0.466) = ₹2.33$ lakh.

### In the news
See news box. Part-count and casting choices affect lifecycle cost through repair as well as factory cost (a design implication, not a figure from the source).

### Interview angle
> [!question] How it is asked
> "Why not just buy the lowest-priced option in a tender?"

> [!tip] Strong answer includes
> - TCO or LCC with discounting and all cost categories
> - A numeric comparison, with sensitivity to usage and energy price
> - Design stage locks in most lifecycle cost
> - Non-cost criteria: reliability, service support, compliance

---

## 13. ⭐ Advanced: Service Design with QFD, Blueprinting and Robustness
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Services are designed with the same logic, adapted to intangible, co-produced outputs (see [[151 Service Operations Management]]):
- **Service QFD:** whats are customer needs (shorter wait, trust, transparency); hows are process and capability measures (turnaround time, first-contact resolution, staffing ratio).
- **Service blueprint** shows front-stage, backstage and support processes with fail points and time standards.
- **Kano for services:** reliability and respect are must-be, personalisation is often a delighter.
- **Robust service design:** use **poka-yoke** (error-proofing, such as mandatory fields), design the process to tolerate customer variability (Taguchi noise = arrival and request variability), and set tolerance on the **critical-to-quality (CTQ)** metrics (waiting time, accuracy).
- **Design thinking and prototyping:** service prototypes (role plays, pilot branches, A/B tests) before roll-out ([[033 Design Thinking & UX]]).

### Example
Design of an inpatient discharge process. Whats: fast, clear, correct bill, medicines in hand. Hows with targets: discharge-to-exit time under 90 minutes (currently 180), billing error rate under 1% (currently 4%), single desk for pharmacy plus billing. Taguchi view: target 90 minutes with cost at limit (120 minutes) of ₹600 per patient in goodwill and bed-blocking cost: $k = 600/30^2 = ₹0.667$ per minute squared. Current mean 180, $\sigma = 30$: $E[L] = 0.667 \times (30^2 + 90^2) = 0.667 \times 9{,}000 = ₹6{,}000$ per patient (an illustrative figure from a stylised loss function). Cutting mean to 100 and $\sigma$ to 15: $0.667 \times (225 + 100) = ₹217$, a 96% fall, showing the value of reducing both the average and the variation.

### In the news
See news box. Products and services converge in connected devices; the same design disciplines (target costing, DFMA, robust design) apply to the software-plus-hardware offers behind many Indian consumer products.

### Interview angle
> [!question] How it is asked
> "How would you design a better customer onboarding service for a bank?"

> [!tip] Strong answer includes
> - Needs (VOC, Kano) to measurable targets (QFD), blueprint with fail points
> - Error-proofing and capacity for variability
> - Prototype and pilot at a few branches, measure, then roll out
> - KPIs: completion time, error rate, NPS, cost-to-serve
