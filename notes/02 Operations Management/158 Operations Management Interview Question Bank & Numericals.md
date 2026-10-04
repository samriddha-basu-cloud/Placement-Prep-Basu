---
tags: [operations-management, tier1]
area: Operations Management
topic: "Operations Management Interview Question Bank & Numericals"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Operations Management Interview Question Bank & Numericals

⬅ [[157 Business Excellence Models & Quality Awards]] · [[_Index - Operations Management|Operations Management]]

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Operations Strategy and Performance Objectives]]
2. [[#2. Capacity, Bottlenecks and OEE]]
3. [[#3. Process Flow, Little's Law and Line Balancing]]
4. [[#4. Lean, TPS and Kanban]]
5. [[#5. Quality, Six Sigma and Process Capability]]
6. [[#6. Layout and Location]]
7. [[#7. Scheduling and Sequencing]]
8. [[#8. Queueing and Service Operations]]
9. [[#9. Inventory, Forecasting and Planning]]
10. [[#10. Maintenance and Reliability]]
11. [[#11. Operations Research, Projects, Learning and Break-even]]
12. [[#12. Plant-Visit and Shop-Floor Scenario Questions]]
13. [[#13. ⭐ Advanced: Case-Style Operations Problems and How to Answer]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the numbers behind operations interviews are in the headlines
> **Maruti Suzuki Hansalpur Plant D (reported 30 Jul 2026).** The Gujarat plant reached **1 million vehicles a year** of installed capacity, which the report describes as the first Suzuki site globally to do so and India's largest single-location passenger-vehicle plant. Plant D cost about **₹3,900 crore**, cumulative Hansalpur investment is **₹25,288.7 crore**, Maruti's total capacity is **2.9 million units a year**, and Hansalpur accounted for nearly **47% of FY 2025-26 export shipments**. Capacity, utilisation and mix questions in this note use exactly this kind of data. ([Evo India](https://www.evoindia.com/news/car-news/maruti-suzuki-hansalpur-reaches-1-million-capacity-587590))
>
> **Nexperia chip halt (31 Oct 2025).** Nexperia suspended wafer supplies to its Dongguan (China) plant on 29 Oct 2025; ZF reduced shifts at its main electric-drivetrain plant and Nissan said internal chip stocks would last only until early November. A single low-cost part stopped capacity worth billions: the bottleneck and risk-pooling questions below. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nexperia-conflict-spills-overseas-as-it-halts-exports-to-china-german-automotive-manufacturers-slow-production-due-to-semiconductor-shortages-from-dutch-chipmaker))
>
> **Cost of unplanned downtime (Siemens, 2024).** Fortune Global 500 firms lose about **$1.4 trillion a year (11% of revenue)** to unplanned downtime; automotive plants about **$2.3 million per hour**. Survey-based estimates. ([Siemens / Senseye PDF](https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/tcod-2024_original.pdf))
>
> Sub-topics that say **"See news box"** reuse these items. How to use this note: each sub-topic lists model-answer questions under *Definition* and a fully worked numerical under *Example*. 70+ questions and 18 numericals are included; practise aloud with a 60 to 90 second target per answer.

---
## 1. Operations Strategy and Performance Objectives
> 🔴 Tier 1 · _Key points:_ competitive priorities; order winners; trade-offs; positioning

### Definition
Teaching notes: [[020 Operations Strategy]], [[017 Process Management & Optimization]], [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]].

**Q1. What is operations strategy?** The pattern of decisions on capacity, facilities, technology, vertical integration, workforce, quality and planning that builds the capabilities the business strategy needs. It translates market requirements into operations capabilities.
**Q2. What are the competitive priorities?** Cost, quality, delivery (speed and reliability), flexibility (mix, volume, new product) and, increasingly, sustainability and innovation. Prioritise by **order winners** (what wins the order) versus **order qualifiers** (the entry ticket).
**Q3. Cost and quality seem to conflict; do they?** In the traditional view yes, but cumulative-capability models (sand cone) argue quality first, then dependability, speed, then cost, because defects, delays and rework are themselves costs. Real trade-offs remain at the frontier (for example, flexibility versus efficiency).
**Q4. Compare Zara and Maruti Suzuki operations strategy.** Zara: speed and flexibility (short lead times, small batches, some local sourcing). Maruti: cost leadership, quality and scale through lean production and dealer network. Different order winners lead to different layouts, inventory and supplier choices.
**Q5. How does product-process matrix help?** It matches product volume and variety to the process type (project, job shop, batch, line, continuous). Moving off the diagonal gives inefficiency (high-volume product in a job shop) or inflexibility (custom product on a rigid line).
**Q6. Make versus buy: how do you decide?** Strategic importance and capability (core), cost including switching and risk, capacity, quality control, supplier base and IP. A core differentiator is generally kept in-house; a commodity is bought ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]]).

### Example
**Scenario answer (no numbers):** "A premium bicycle brand's customers value delivery in 3 days and customisation. The plant makes 60 variants in large batches with 3-week lead time. What would you change?" Answer: the order winner (speed plus variety) conflicts with the process (batch, make-to-stock). Move to postponement: standard sub-assemblies in stock and final assembly to order, cut changeovers (SMED), a mixed-model assembly line with heijunka and a regional assembly node. Say what you give up: some unit cost and more finished-component inventory.

### In the news
See news box. Hansalpur's investments show a cost-and-scale strategy; Nexperia shows how that strategy is exposed to single-source risk.

### Interview angle
> [!question] How it is asked
> "What are your company's competitive priorities, and how do operations decisions support them?"

> [!tip] Strong answer includes
> - Priorities named, ranked and tied to the customer segment
> - Order winners vs qualifiers
> - Concrete operations decisions (process choice, inventory position, supplier model)
> - Acknowledgement of trade-offs and what is deliberately sacrificed

---
## 2. Capacity, Bottlenecks and OEE
> 🔴 Tier 1 · _Key points:_ bottleneck sets output; utilisation; OEE three factors

### Definition
Teaching notes: [[018 Capacity Management & OEE]], [[017 Process Management & Optimization]], [[022 Maintenance Management (TPM-RCM)]].

**Q7. Design capacity vs effective capacity vs actual output?** Design is the ideal maximum, effective is after planned losses, actual is what was made. Utilisation = actual/design; efficiency = actual/effective.
**Q8. How do you find the bottleneck?** Compare each resource's capacity with demand (lowest capacity per unit of flow), find where queues build up in front and starving occurs behind, and check utilisation at 100%. Capacity must be measured in a common unit and include setups and yield.
**Q9. How do you raise capacity of the bottleneck cheaply?** Never let it wait (buffer in front, protect breaks), reduce its changeovers, offload work to non-bottlenecks, improve quality upstream so scrap is not processed, add shifts, improve OEE; only then capex. An hour lost at the bottleneck is an hour lost for the system.
**Q10. Define OEE and why 85% is called world class.** OEE = Availability x Performance x Quality. 85% is a widely quoted benchmark (for example 90% x 95% x 99.9%) that depends on the industry and on how planned stops are treated, so quote it as rule of thumb.
**Q11. OEE is 70%. What do you do first?** Break it into three components, then the six big losses, and Pareto the largest loss by minutes (not by opinion). Typical biggest are changeover, minor stops and speed loss.
**Q12. Capacity at 95% utilisation: good or bad?** Good for cost, dangerous for service: queueing delay rises steeply as utilisation approaches 100%, so variable-demand operations need a cushion (see [[149 Queueing Theory & Waiting-Line Analysis]]).

### Example
**Numerical 1 (bottleneck).** Line: station A takes 2.0 min per unit (1 machine), B takes 3.0 min (2 identical machines in parallel), C takes 2.5 min (1 machine). Find capacity, bottleneck and utilisation, and daily output (8 h).
Capacities per hour: A $60/2=30$; B $2\times60/3=40$; C $60/2.5=24$. **Bottleneck C, line capacity 24 units/h**, daily output $24\times8=192$. Utilisation at that output: A $24/30=80\%$, B $24/40=60\%$, C $100\%$. To reach 30/h, C needs another machine or time reduction: with C at 2.0 min the line becomes limited by A at 30/h.

**Numerical 2 (OEE).** Shift planned time 480 min; downtime 60 min (40 breakdown, 20 changeover); ideal cycle time 0.5 min/unit; produced 700 units, of which 21 rejected.
Run time $=420$; Availability $=420/480=87.5\%$; Performance $=0.5\times700/420=83.3\%$; Quality $=679/700=97.0\%$.
$$OEE=0.875\times0.8333\times0.97=\mathbf{70.7\%}$$
Check: good units x ideal cycle $=679\times0.5=339.5$ min of fully productive time, $339.5/480=70.7\%$. Largest loss in minutes: performance loss $420-350=70$ min versus downtime 60 min and rejects 10.5 min.

### In the news
See news box. Hansalpur's 1 million figure is installed capacity; actual output depends on utilisation and model mix, which is why "design vs actual" is a standard first question.

### Interview angle
> [!question] How it is asked
> "A plant runs three shifts at 70% OEE and wants 20% more output. What would you do before approving capex?"

> [!tip] Strong answer includes
> - Establish bottleneck and loss tree; a $1.2\times$ target equals $70\%\to84\%$ OEE if nothing else changes
> - Quick wins: changeover, minor stops, speed; maintenance and quality at the bottleneck
> - Check demand: more output has no value without orders
> - Capex only after the loss recovery; cost-benefit via [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]

---
## 3. Process Flow, Little's Law and Line Balancing
> 🔴 Tier 1 · _Key points:_ WIP = throughput x flow time; takt; balance efficiency

### Definition
Teaching notes: [[017 Process Management & Optimization]], [[006 Manufacturing Systems]], [[019 Facility Layout & Location]].

**Q13. State Little's Law and use it.** $WIP=\text{Throughput}\times\text{Flow time}$ ($L=\lambda W$) for any stable system. To cut lead time at constant throughput, cut WIP; it also converts inventory into days of cover.
**Q14. Cycle time vs takt time vs lead time?** Cycle time is time per unit at a station; takt is available time per unit of demand; lead time is order to delivery. A station is feasible when its cycle time is at most takt.
**Q15. What is line-balancing efficiency?** $\dfrac{\sum t_i}{N\times CT}$, with $N$ stations and cycle time $CT$ (balance delay is $1-\text{efficiency}$). Theoretical minimum stations $=\lceil\sum t_i/CT\rceil$.
**Q16. Why do high-variability processes need buffers?** Variability in arrivals and process times causes queues even at utilisation below 100%; buffers (time, inventory or capacity) absorb it; lean attacks the sources, not just the buffer.
**Q17. What is process cycle efficiency?** Value-added time divided by total lead time, typically very low (5% or lower) in unmanaged flows; the target of lean value-stream work.

### Example
**Numerical 3 (line balancing).** Eight tasks (seconds): A20, B30, C25, D35, E40, F25, G30, H35; total 240 s. Precedence: A before B and C; B and C before D; D before E and F; E and F before G; G before H. Demand 480 a day in 8 h: takt $=28{,}800/480=60$ s. Minimum stations $=240/60=4$. Using the largest-candidate rule within cycle time 60 s: S1 {A, B} 50 s; S2 {C, D} 60 s; S3 {E} 40 s (F 25 would fit after E? E+F=65 > 60, so no); S4 {F, G} 55 s; S5 {H} 35 s. Five stations; efficiency $=240/(5\times60)=\mathbf{80\%}$, idle time 60 s. A search over all precedence-feasible assignments shows 4 stations is impossible at a 60 s cycle (it would need every station to be loaded to exactly 60 s), so **5 stations is optimal** here; in general the heuristic does not guarantee the optimum.

**Numerical 4 (Little's Law).** A cell has 120 units of WIP and throughput of 40 units/h. Flow time $=120/40=\mathbf{3\ h}$. Cutting WIP to 90 units (via kanban cap) at the same throughput gives $90/40=2.25$ h, a 25% lead-time reduction with no capacity change. Check: ensure throughput does not fall when WIP falls (above the critical WIP level).

### In the news
See news box. The Siemens finding that average recovery time per incident grew to 81 minutes shows how flow time is shaped by waiting, not working.

### Interview angle
> [!question] How it is asked
> "Lead time on this line is 3 weeks and customers want 1 week. How would you attack it?"

> [!tip] Strong answer includes
> - Little's Law: lead time = WIP/throughput; map the value stream and find where the time sits
> - Waiting, batching and changeover as primary levers; PCE as the measure
> - Pull systems and WIP caps; level the mix
> - Verify the bottleneck and keep throughput stable

---
## 4. Lean, TPS and Kanban
> 🔴 Tier 1 · _Key points:_ 8 wastes; pull; kanban sizing; jidoka; standard work

### Definition
Teaching notes: [[007 Lean Manufacturing]], [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]], [[117 Demand-Driven MRP (DDMRP) & Buffer Management]].

**Q18. Name the 8 wastes (DOWNTIME).** Defects, Overproduction, Waiting, Non-utilised talent, Transportation, Inventory, Motion, Extra processing. Overproduction is "the worst" because it causes the others.
**Q19. Push vs pull?** Push produces to a forecast or schedule (MRP); pull produces when a downstream consumer signals (kanban). Pull caps WIP and exposes problems; it needs stable, levelled demand and short changeovers.
**Q20. How is the number of kanbans set?** $N=\dfrac{D\times L\times(1+\alpha)}{C}$ with demand rate $D$, replenishment lead time $L$, safety factor $\alpha$ and container size $C$, rounded up.
**Q21. What is jidoka and what is an andon?** Autonomation: machines and people stop on abnormality so defects do not travel; an andon is the signal. Together with just-in-time they make the two pillars of TPS.
**Q22. What is heijunka and why is it needed?** Production levelling by volume and mix (a repeating mixed sequence), so upstream demand is smooth and pull works. Without it kanban oscillates.
**Q23. How do you start lean in a plant that never did?** Gemba walk, value-stream map, safety and 5S as a base, pick a model line, standard work and visual management, tier meetings, then expand. Avoid cost-cutting messaging ([[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]]).

### Example
**Numerical 5 (kanban).** Downstream demand 120 units/h; replenishment lead time 30 min (0.5 h); container holds 20; safety factor 10%.
$$N=\frac{120\times0.5\times1.1}{20}=3.3\ \to\ \mathbf{4\ kanbans}$$
WIP ceiling $=4\times20=80$ units. If the lead time halves via SMED to 15 min: $N=120\times0.25\times1.1/20=1.65\to2$ cards, WIP cap 40: lean improvement shrinks the inventory the system needs.

### In the news
See news box. The Nexperia halt reminds that JIT with single-source parts has no slack; lean needs supply-risk buffers for critical parts.

### Interview angle
> [!question] How it is asked
> "Is lean still relevant after COVID and chip shortages exposed JIT's fragility?"

> [!tip] Strong answer includes
> - Lean removes waste, not resilience; keep strategic buffers for single-source or long-lead items
> - Segment items by criticality and variability
> - Kanban sizing with safety factor, supplier collaboration, dual sourcing
> - Examples from the news (chip shortage)

---
## 5. Quality, Six Sigma and Process Capability
> 🔴 Tier 1 · _Key points:_ DMAIC; sigma level; RTY; Cp and Cpk; control charts

### Definition
Teaching notes: [[008 Six Sigma & Quality Tools]], [[011 Quality Management (TQM)]], [[091 Statistical Quality Control (SQC)]], [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]], [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]].

**Q24. What is DMAIC?** Define, Measure, Analyse, Improve, Control: Six Sigma's data-driven problem-solving cycle. Control means sustaining via control plans and SPC.
**Q25. What does "six sigma" mean numerically?** 3.4 defects per million opportunities with the conventional 1.5-sigma long-term shift. DPMO = defects / (units x opportunities) x $10^6$.
**Q26. Cp vs Cpk?** $C_p=\dfrac{USL-LSL}{6\sigma}$ measures potential (spread only); $C_{pk}=\min\!\left(\dfrac{USL-\mu}{3\sigma},\dfrac{\mu-LSL}{3\sigma}\right)$ includes centring. $C_p=C_{pk}$ when centred.
**Q27. Common vs special cause variation?** Common is inherent to the system (needs process redesign); special is assignable (find and remove). Control charts separate them; reacting to common cause as if special (tampering) increases variation.
**Q28. Control limits vs specification limits?** Control limits come from process data (voice of the process, $\mu\pm3\sigma$ of the plotted statistic); specs come from the customer (voice of the customer). They are unrelated.
**Q29. What is rolled throughput yield?** Product of step yields; hidden factory of rework shows up here, not in final yield.

### Example
**Numerical 6 (DPMO and RTY).** 1,500 units inspected, each with 4 opportunities, 45 defects. $DPMO=45/(1500\times4)\times10^6=\mathbf{7{,}500}$, yield $99.25\%$, sigma level $\approx3.93$ (with 1.5 shift). A three-step process with yields 98%, 95% and 99% has $RTY=0.98\times0.95\times0.99=\mathbf{92.2\%}$, although each step looks good.

**Numerical 7 (Cpk).** Shaft diameter spec $50.0\pm0.5$ mm; process mean 50.2, $\sigma=0.15$. $C_p=1.0/0.9=1.11$; $C_{pk}=(50.5-50.2)/0.45=\mathbf{0.667}$, so about 22,750 ppm (2.3%) are out of spec. Centring at 50.0 gives $C_{pk}=1.11$ and about 860 ppm without reducing variation; reaching $C_{pk}=1.33$ when centred needs $\sigma\approx0.125$. Lesson: centre first, then reduce spread.

### In the news
See news box. The Siemens/Senseye report ties quality, maintenance and downtime; the NTSB door-plug findings (see [[155 Reliability Engineering & Maintenance Optimisation]]) show a missing inspection step as a root cause.

### Interview angle
> [!question] How it is asked
> "Your process has $C_p=1.5$ but $C_{pk}=0.8$. What does it tell you and what do you do?"

> [!tip] Strong answer includes
> - Spread is fine, the mean is off-centre: adjust the process mean first
> - Formula and arithmetic of $C_{pk}$
> - Why re-centring is cheap compared with reducing variation
> - Monitor via control charts to keep the mean on target

---
## 6. Layout and Location
> 🔴 Tier 1 · _Key points:_ layout types; cells; weighted factor rating; centre of gravity

### Definition
Teaching notes: [[019 Facility Layout & Location]], [[113 Network Design & Facility Location Modelling]], [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

**Q30. Name the layout types and when each fits.** Process (functional) layout for low-volume high-variety; product (line) for high volume; cell (group technology) for families; fixed-position for large immovable products; hybrid. Choose by volume, variety, flexibility and material-handling cost.
**Q31. What is a U-shaped cell good for?** Operators can serve several machines and rebalance as takt changes; shorter walking, better communication, easier standard work.
**Q32. How do you choose a plant location?** Quantitative: weighted factor rating, cost-volume breakeven, centre of gravity, network models; qualitative: incentives, talent, risk, ports, supplier base, regulation, power and water. Look at total landed cost and risk, not only labour cost.
**Q33. Why are many Indian auto and electronics plants clustered?** Supplier ecosystems, ports and state incentives (see policy note); clusters cut logistics and raise supplier responsiveness, with the risk of concentration.

### Example
**Numerical 8 (weighted factor rating).** Weights: labour cost 0.30, supplier proximity 0.25, logistics/ports 0.25, incentives 0.20. Scores (1 to 10): Pune [7, 9, 8, 6], Hosur [8, 7, 7, 8], Sanand [6, 7, 9, 9].
Pune $=0.3(7)+0.25(9)+0.25(8)+0.2(6)=2.1+2.25+2.0+1.2=7.55$. Hosur $=2.4+1.75+1.75+1.6=7.50$. Sanand $=1.8+1.75+2.25+1.8=\mathbf{7.60}$. Sanand ranks first, but the margins (0.05 to 0.10) are within scoring noise, so do a sensitivity analysis on the weights and a landed-cost comparison before choosing. If the labour-cost weight rises to 0.40 (others scaled pro rata to 0.214, 0.214, 0.171), the ranking flips: Hosur 7.57, Pune 7.47, Sanand 7.37.

### In the news
See news box. Hansalpur holds about 47% of Maruti's exports and Gujarat's port access is one reason such a cluster makes sense.

### Interview angle
> [!question] How it is asked
> "Where would you set up a new plant for an export-oriented product and why?"

> [!tip] Strong answer includes
> - Criteria and weights tied to the strategy (cost, speed, risk)
> - Quantitative score plus a total landed-cost comparison
> - Sensitivity on key weights and policy incentives
> - Risks: concentration, labour availability, climate, regulatory approvals

---
## 7. Scheduling and Sequencing
> 🔴 Tier 1 · _Key points:_ dispatching rules; Johnson's rule; Gantt; flow vs job shop

### Definition
Teaching notes: [[021 Scheduling & Sequencing]], [[005 Production & Operations Planning]], [[081 SAP PP — Production Planning]].

**Q34. SPT, EDD and FCFS: what does each optimise?** SPT minimises mean flow time and average WIP (but starves long jobs); EDD minimises maximum lateness; FCFS is fair but poor on all measures. Slack and critical ratio rules look at urgency.
**Q35. Johnson's rule?** For two machines in series, minimises makespan: pick the smallest time across both machines; if on machine 1 place the job first, else last; repeat.
**Q36. Why is finite-capacity scheduling better than MRP's infinite capacity?** MRP assumes unlimited capacity and fixed lead times; finite scheduling respects machine availability, setups and sequence, so promised dates are realistic.
**Q37. Make-to-stock vs make-to-order scheduling?** MTS schedules by inventory targets and replenishment signals; MTO by due dates and customer priorities with capacity checks; hybrid uses a decoupling point.
**Q38. How would you reduce changeover loss in scheduling?** Sequence by similarity (colour light to dark, size small to large), campaign production, SMED, and trade off with inventory and lateness.

### Example
**Numerical 9 (Johnson).** Five jobs, (machine 1, machine 2) times in hours: J1 (5, 2), J2 (1, 6), J3 (9, 7), J4 (3, 8), J5 (10, 4).
Jobs with $t_1\le t_2$: J2 (1), J4 (3): put first, ascending in $t_1$: J2, J4. Remaining: J3 (9, 7), J5 (10, 4), J1 (5, 2): put last, descending in $t_2$: J3 (7), J5 (4), J1 (2). **Sequence: J2, J4, J3, J5, J1.**
Machine 1 finishes at 1, 4, 13, 23, 28; machine 2 finishes at 7, 15, 22, 27, **30**. Makespan 30 h, versus 34 h in the order J1 to J5. Machine 2 idles for 1 h at the start and 1 h before J1.

### In the news
See news box. Missing a single part (chips) blows up even a perfect schedule: scheduling needs material availability checks (clear-to-build).

### Interview angle
> [!question] How it is asked
> "A job shop has late orders and high WIP. What scheduling changes would you consider?"

> [!tip] Strong answer includes
> - Identify the bottleneck and schedule it first (drum), buffering it
> - Dispatching rule fit (EDD/critical ratio for due dates, SPT for WIP)
> - Frozen horizon, clear-to-build and setup-based sequencing
> - Measure on-time delivery and flow time before and after

---
## 8. Queueing and Service Operations
> 🔴 Tier 1 · _Key points:_ M/M/1; utilisation vs wait; pooling; psychology of waiting

### Definition
Teaching notes: [[149 Queueing Theory & Waiting-Line Analysis]], [[151 Service Operations Management]], [[173 Process Mining & Operations Intelligence]].

**Q39. Why do queues form when capacity exceeds average demand?** Variability: random arrivals and service times create temporary overloads. Waiting grows non-linearly with utilisation ($\propto\rho/(1-\rho)$ for M/M/1).
**Q40. M/M/1 formulas?** $\rho=\lambda/\mu$, $L=\rho/(1-\rho)$, $L_q=\rho^2/(1-\rho)$, $W=1/(\mu-\lambda)$, $W_q=\lambda/[\mu(\mu-\lambda)]$, $P(N>k)=\rho^{k+1}$.
**Q41. Would you rather have one fast server or two slow ones of the same total capacity?** Usually the single fast server gives lower mean time in system (service time is shorter), while two servers give lower waiting time and better robustness to breakdown; pooling a common queue beats separate queues.
**Q42. How do you reduce waiting without adding capacity?** Cut variability (appointments, standard work), pool queues, triage and segment (express lanes), shift demand (pricing), manage perception (information, occupied time), and use self-service.
**Q43. Why do hospitals and call centres plan for occupancy well below 100% (figures near 85% are often quoted as a rule of thumb)?** Beyond high utilisation delays explode and emergencies find no slack; the right target depends on variability and service-level goals.

### Example
**Numerical 10 (M/M/1 and M/M/2).** A counter receives $\lambda=8$ customers/h; one clerk serves $\mu=10$/h.
$\rho=0.8$; $L=4$; $L_q=3.2$; $W=1/(10-8)=0.5$ h $=30$ min; $W_q=8/(10\times2)=0.4$ h $=24$ min; $P(N>5)=0.8^6=\mathbf{26.2\%}$.
Alternative: two clerks each with $\mu=5$/h (same total capacity), $a=\lambda/\mu=1.6$, $\rho=0.8$ per server. $P_0=1/(1+1.6+1.6^2/(2\times0.2))=0.111$; $L_q=P_0\,a^2\rho/[2(1-\rho)^2]=2.84$; $W_q=2.84/8=0.355$ h $=21.3$ min; $W=W_q+1/5\text{ h}=33.3$ min. Result: **waiting in line is shorter (21.3 vs 24 min) but total time in system is longer (33.3 vs 30 min)** because each service is twice as slow.

### In the news
See news box. Plant maintenance desks and spare-parts counters also behave as queues; Siemens' longer recovery time (81 minutes) is partly queueing.

### Interview angle
> [!question] How it is asked
> "A bank branch has long queues at lunchtime but idle tellers in the morning. What do you do?"

> [!tip] Strong answer includes
> - Measure arrival pattern and service-time variability by hour
> - Match staffing to the arrival pattern (flexible shifts, cross-training)
> - Pooling, triage, digital substitution, appointments
> - Quantify with a queueing model and set a service-level target

---
## 9. Inventory, Forecasting and Planning
> 🔴 Tier 1 · _Key points:_ EOQ; safety stock; ROP; forecast error; S&OP

### Definition
Teaching notes: [[003 Inventory Management]], [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]], [[004 Demand Forecasting & Planning]], [[153 Aggregate Planning Models & Workforce Strategy]], [[143 SCM Interview Question Bank]].

**Q44. EOQ formula and assumptions?** $Q^*=\sqrt{2DS/H}$: constant demand, instantaneous replenishment, no discounts or stock-outs; at the optimum, ordering cost equals holding cost.
**Q45. Safety stock?** $SS=z\sigma_d\sqrt{L}$ (demand variability, fixed lead time); with lead-time variability $z\sqrt{L\sigma_d^2+d^2\sigma_L^2}$. $z$ is set by the target cycle-service level.
**Q46. Which forecasting method for which demand?** Naive and moving average for stable; exponential smoothing for level; Holt for trend; Holt-Winters for seasonality; regression or ML with causals. Judge by out-of-sample error (MAD, MAPE, bias).
**Q47. MAD vs MAPE vs bias?** MAD: average absolute error in units; MAPE: percent error (undefined at zero demand and biased on low volumes); bias (mean error) shows systematic over- or under-forecasting.
**Q48. What is aggregate planning?** Medium-term plan of production, workforce and inventory by month using chase, level or hybrid strategies, minimising total cost (regular, overtime, hiring and layoffs, inventory, backlog).
**Q49. How do ABC and XYZ analysis combine?** ABC by value and XYZ by variability: AX items get tight control and low safety stock; CZ items are managed with simple rules and bulk buying.
**Q50. S&OP in one line?** A monthly cross-functional process aligning demand, supply and finance plans to one set of numbers ([[120 Integrated Business Planning (IBP) & S&OP Maturity]]).

### Example
**Numerical 11 (EOQ, safety stock, ROP).** Annual demand $D=24{,}000$ units, ordering cost $S=₹500$, holding cost $H=₹20$/unit/year, 300 working days, lead time 10 days, daily demand standard deviation 12 units, 95% service ($z=1.65$).
$Q^*=\sqrt{2\times24000\times500/20}=\mathbf{1{,}095}$ units; orders per year $=21.9$; ordering cost $=₹10{,}954$; holding $=Q/2\times20=₹10{,}954$; total $=₹21{,}909$ (₹0.91/unit). Daily demand $=80$; $SS=1.65\times12\times\sqrt{10}=62.6$; $ROP=80\times10+62.6=\mathbf{863}$ units. Average inventory is $Q/2+SS=610$ units (about 7.6 days of cover).

**Numerical 12 (forecasting).** Demand for six periods: 100, 110, 104, 120, 118, 125. Exponential smoothing with $\alpha=0.3$ and $F_2=D_1=100$: $F_3=0.3(110)+0.7(100)=103.0$; $F_4=103.3$; $F_5=108.31$; $F_6=111.22$; next period $F_7=0.3(125)+0.7(111.22)=\mathbf{115.35}$. Errors for periods 4 to 6: 16.7, 9.69 and 13.78, MAD $=13.39$. A 3-period moving average over the same periods gives forecasts 104.67, 111.33, 114.0, errors 15.33, 6.67, 11.0, MAD $=\mathbf{11.0}$. On this short, trending series, the moving average does slightly better; smoothing lags a trend, so Holt's method would be considered. (Compare methods on identical periods.)

### In the news
See news box. Both Nexperia and Hansalpur items bear on safety stock and capacity planning: where supply is lumpy and lead time uncertain, the $\sqrt{L}$ rule understates risk.

### Interview angle
> [!question] How it is asked
> "How would you reduce inventory by 20% without hurting service levels?"

> [!tip] Strong answer includes
> - Segmentation (ABC/XYZ) and policy by segment
> - Reduce variability and lead time (they drive safety stock), improve forecast accuracy
> - Fix slow movers and excess; review parameters in ERP
> - Report service level, turns and cash effect together

---
## 10. Maintenance and Reliability
> 🔴 Tier 1 · _Key points:_ MTBF/MTTR; availability; TPM; PM vs PdM; spares

### Definition
Teaching notes: [[022 Maintenance Management (TPM-RCM)]], [[155 Reliability Engineering & Maintenance Optimisation]], [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]].

**Q51. Types of maintenance and when each is used?** Corrective (run to failure, for non-critical), preventive (calendar or usage, for wear-out), predictive (condition-based, for detectable degradation), proactive (root-cause elimination).
**Q52. MTBF, MTTR and availability?** $A=MTBF/(MTBF+MTTR)$; MTBF is the reliability lever, MTTR the maintainability lever; for non-repairable items use MTTF.
**Q53. What is TPM and why does it include operators?** Total Productive Maintenance makes production and maintenance jointly responsible for equipment effectiveness; autonomous maintenance catches minor issues and frees technicians for planned work.
**Q54. How do you decide between preventive and predictive?** If the hazard rate rises with age and a failure costs much more than a planned stop, use time-based replacement; if a degradation signal gives a P-F interval longer than the response time, use condition monitoring; if neither applies, run to failure or redesign.
**Q55. Critical spares policy?** Segment by criticality, lead time and cost; stock insurance spares for critical long-lead items sized on a Poisson demand over lead time; share and pool across sites.
**Q56. Which KPIs show maintenance health?** Planned vs reactive work %, MTBF, MTTR, schedule compliance, backlog, maintenance cost as % of replacement asset value, OEE availability.

### Example
**Numerical 13 (availability).** Three machines in series with MTBF (h) 100, 150, 200 and MTTR (h) 5, 6, 4. Availabilities: $100/105=95.24\%$, $150/156=96.15\%$, $200/204=98.04\%$. System availability $=0.9524\times0.9615\times0.9804=\mathbf{89.8\%}$. Adding an identical standby for machine 1 (parallel pair) gives $1-(0.0476)^2=99.77\%$ for that stage and a system availability of $0.9977\times0.9615\times0.9804=\mathbf{94.1\%}$, a 4.3-point gain. Compare the cost of the extra machine with the output value of 4.3% of production time.

### In the news
See news box. At $2.3 million an hour (automotive, Siemens estimate) the standby machine in the example would pay back quickly; in low-cost industries (FMCG about $36,000 an hour) it would not.

### Interview angle
> [!question] How it is asked
> "Breakdowns are 12% of production time. How would you cut them?"

> [!tip] Strong answer includes
> - Pareto of breakdown causes by minutes and equipment
> - Quick wins: basic conditions (cleaning, lubrication), autonomous maintenance
> - Strategy by criticality: PM, condition monitoring, redesign
> - Spares and skills for MTTR; measure MTBF and MTTR monthly

---
## 11. Operations Research, Projects, Learning and Break-even
> 🔴 Tier 1 · _Key points:_ LP; assignment; CPM/PERT; learning curve; break-even

### Definition
Teaching notes: [[146 Operations Research - Linear Programming]], [[147 Operations Research - Transportation, Assignment & Transshipment]], [[148 Operations Research - Network Models & Integer Programming]], [[039 Scheduling Tools (CPM-PERT-Gantt)]], [[152 Learning Curves, Work Measurement & Productivity]], [[077 Solver, Goal Seek & What-If Analysis]].

**Q57. How do you formulate an LP?** Define decision variables, an objective (max profit or min cost), linear constraints (capacity, demand, material) and non-negativity. Solve graphically (2 variables), by simplex or Solver.
**Q58. What is a shadow price?** The change in the optimal objective per unit increase in a constraint's right-hand side, valid within the allowable range; it tells which resource is worth expanding.
**Q59. Assignment vs transportation problem?** Assignment is a one-to-one special case of transportation with unit supplies and demands; solved by the Hungarian method.
**Q60. What is the critical path and float?** The longest path through the network sets project duration; critical activities have zero float; total float $=LS-ES$.
**Q61. CPM vs PERT?** CPM uses deterministic (often cost-time trade-off) durations; PERT uses three estimates $(o,m,p)$, $t_e=(o+4m+p)/6$, variance $((p-o)/6)^2$, and a normal approximation for project duration.
**Q62. Learning curve in one sentence?** Unit time falls by a constant percentage every doubling of cumulative output: $T_n=T_1n^{b}$, $b=\log(\text{rate})/\log2$.
**Q63. Break-even and make-vs-buy?** Break-even quantity $=F/(p-v)$; make vs buy where $F+vQ=cQ$.

### Example
**Numerical 14 (LP product mix).** Maximise profit $Z=40x+30y$ (₹ per unit) subject to machine hours $2x+y\le100$, labour hours $x+y\le80$, demand cap $x\le40$, $x,y\ge0$. Corner points: (0, 0) gives 0; (40, 0) 1,600; (40, 20) 2,200; (20, 60) **2,600** (intersection of the two resource lines); (0, 80) 2,400. **Optimum $x=20$, $y=60$, profit ₹2,600**; both machine and labour hours are binding, the demand cap is slack. Check: $2(20)+60=100$ ✓, $20+60=80$ ✓.

**Numerical 15 (assignment).** Cost matrix (rows jobs 1-4, columns machines 1-4): [9, 11, 14, 11], [6, 15, 13, 13], [12, 13, 6, 8], [11, 9, 10, 12]. Hungarian method (verified with a solver): Job 1 to Machine 4 (11), Job 2 to Machine 1 (6), Job 3 to Machine 3 (6), Job 4 to Machine 2 (9): **total cost 32**.

**Numerical 16 (CPM and PERT).** Activities (days, predecessors): A 3 (none), B 4 (A), C 2 (A), D 5 (B), E 3 (C), F 4 (D, E), G 2 (F). Forward pass: EF A3, B7, C5, D12, E8, F16, G18. **Project duration 18 days; critical path A-B-D-F-G**; float of C and E is 4 days. PERT version with three-point estimates on the critical path: A (2,3,4), B (3,4,5), D (4,5,12), F (3,4,5), G (1,2,3): $t_e=3,4,6,4,2$, total **19 days**, variance $0.111\times4+1.778=2.222$, SD $=1.49$. $P(T\le21)=\Phi(1.34)=0.91$; $P(T\le20)=\Phi(0.67)=0.75$. Skewed D lifts the expected time by 1 day over the CPM figure; near-critical paths should be checked in a full simulation.

**Numerical 17 (learning curve).** 80% curve, first unit takes 100 h: unit 2 takes 80 h, unit 4 takes 64 h, unit 8 takes $100\times8^{-0.322}=51.2$ h. Total for the first 8 units $=534.6$ h, an average of **66.8 h/unit**. Use it for bid pricing and labour planning for new products.

**Numerical 18 (make vs buy break-even).** Make: fixed cost ₹6,00,000 a year plus ₹40 per unit; buy: ₹70 per unit. $Q=600{,}000/(70-40)=\mathbf{20{,}000}$ units. At 15,000 units make costs ₹12.0 lakh vs buy ₹10.5 lakh (buy); at 25,000 make costs ₹16.0 lakh vs buy ₹17.5 lakh (make). Beyond cost: quality control, IP, flexibility, risk.

### In the news
See news box. Maruti's Plant D decision is a capacity and make-versus-buy investment decision of this form, though it was made with far more detail.

### Interview angle
> [!question] How it is asked
> "A manager says an extra machine hour is worth ₹200. How would you check that with data?"

> [!tip] Strong answer includes
> - Linear programme and its shadow price, within the allowable range
> - Sensitivity analysis and what changes when other constraints bind
> - Reality checks: changeovers, integer units, demand
> - Translate the answer into an action and a decision threshold

---
## 12. Plant-Visit and Shop-Floor Scenario Questions
> 🔴 Tier 1 · _Key points:_ observe, quantify, prioritise; safety first; speak to operators

### Definition
Core operations roles often include a plant visit or case discussion about the shop floor. A reliable method: **safety first**, **observe before judging**, **quantify with the simplest data**, **talk to operators** and **propose a sequence of small experiments** rather than a big project. Teaching notes: [[007 Lean Manufacturing]], [[022 Maintenance Management (TPM-RCM)]], [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]], [[026 Case Interview — Operations Cases]].

**S1. You enter a plant for the first time. What do you look at in the first hour?** Safety (PPE, guarding, walkways), 5S condition, material flow and WIP piles, visible boards and who reads them, where the line stops, operator behaviour, and the state of the bottleneck. Ask "what is the biggest problem today?" to operators and supervisors.
**S2. A machine that "always breaks" is blamed for low output. First steps?** Check its role (bottleneck or not), collect breakdown logs by cause and duration, look for the top 2 failure modes, inspect basic conditions (lubrication, cleanliness), and test whether operators and maintenance agree on the root cause. Then apply a Pareto-based fix and monitor MTBF.
**S3. Rework is 8% on a key line. Where do you begin?** Define the defect and map where it is created and found; Pareto by type and shift; check gauge R&R; examine the process parameters; mistake-proof the top cause; add in-station checks to stop defects travelling.
**S4. The line stops every hour for 3 to 5 minutes. What is happening?** Typical minor-stop causes: sensor misreads, feeder jams, material starvation, changeover adjustments. Record stops with a count sheet for two shifts; the top two causes usually explain more than half.
**S5. Stores show 3 months of raw material but production still halts for shortages. Why?** Wrong parts in stock (ABC and demand mismatch), poor record accuracy, ineffective kitting or location control, supplier variability; check cycle count, MRP parameters and shortage causes ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]]).
**S6. Shift handover causes quality escapes. Fix?** Standard handover sheet, open abnormalities on the board, a short overlap with a face-to-face briefing, and accountability for the checks.
**S7. The plant manager wants +20% output without capex. How?** Find the bottleneck, recover OEE (changeovers, minor stops), improve the bottleneck's uptime and yield, level the mix, extend working hours, remove non-bottleneck waste only if it relieves the constraint; verify demand and quality.
**S8. You spot an unsafe act on the floor during the visit. What do you do?** Stop the activity politely, ensure the person is safe, inform the supervisor, and raise it later with the plant head; safety is non-negotiable and acting shows judgement.
**S9. Operators resist a new standard work sheet. How do you respond?** Understand why (is it wrong, slower, an extra burden?), involve them in redesigning, trial on one shift, show the benefit, and let the supervisor own the audit.
**S10. Where would you look for a 10% cost reduction in a plant?** Scrap and rework, energy, yield and material usage, overtime and downtime, inventory carrying cost, procurement price, logistics; rank by size and ease of capture ([[110 Cost Accounting for Operations]]).

### Example
**Worked scenario S7 with numbers.** A bottleneck line is scheduled for 480 min per shift. Recorded losses per shift: changeover 50 min, breakdowns 40, minor stops 45, slow cycles 30, rejects 10, i.e. 175 min of loss, leaving 305 productive-equivalent minutes (OEE $305/480=63.5\%$). Target: +20% output, i.e. at least 366 min. Plan: halve changeover (SMED, saves 25), halve minor stops (stop-code system and fixes, 22.5), cut breakdowns by a quarter (10), halve slow-cycle loss (15): total recovered 72.5 min, giving $377.5/305=\mathbf{+23.8\%}$ output and OEE $78.6\%$ with no capex. Keep the extra 3.8 points as contingency because loss reductions are rarely achieved in full; confirm demand exists and that downstream stations can absorb the volume. Track weekly OEE and output.

### In the news
See news box. Siemens' finding that plants lose about 27 hours a month to unplanned downtime provides a benchmark for what S2 and S7 can achieve.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would spend your first week as a production engineer on a line that misses its targets."

> [!tip] Strong answer includes
> - Safety and standard checks, then observing flow
> - Quantification with simple tools (stop sheets, Pareto, takt vs cycle)
> - Operator involvement and respect for the floor
> - Small experiments, quick wins, A3 or kata cadence

---
## 13. ⭐ Advanced: Case-Style Operations Problems and How to Answer
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Consulting and operations-leadership interviews use operations cases (improve a plant, design a network, fix a service process). Framework: **clarify and structure, quantify the gap, find root causes, generate and rank levers, size impact, plan, risks.** Teaching notes: [[026 Case Interview — Operations Cases]], [[024 Consulting Frameworks]], [[162 Structured Communication - SCQA, Storylines & Case Delivery]], [[143 SCM Interview Question Bank]].

**C1. "A plant's profit has fallen 15%." Structure?** Revenue (volume, price, mix) versus cost (material, labour, overhead, quality), by product and line; benchmark against history and peers; then operations drivers (OEE, yield, labour productivity, energy, logistics).
**C2. "Reduce lead time for a custom product from 12 to 6 weeks."** Map the end-to-end process, split touch time and queue time, find where the time sits, then levers: parallel work, batch size, bottleneck, approvals, supplier lead time, modular design.
**C3. "Should we build a second plant?"** Demand growth and utilisation of the existing plant, capacity cushion, debottleneck options, location, capex and return ($NPV$), risk and timing.
**C4. "Improve a hospital's emergency department."** Flow from arrival to discharge, triage, bottlenecks (imaging, beds), arrival patterns, staffing and queueing; safety and clinical quality are constraints.
**C5. Answer structure.** Say the structure first, ask for data, compute out loud, state the answer first and the supporting points after, and check sanity (does ₹X crore saving fit in a ₹Y crore cost base?).

### Example
**Case numbers.** A plant with sales ₹600 crore and contribution 28% wants ₹10 crore more EBITDA. Levers: scrap 4% to 3% on material cost ₹300 crore saves $0.01\times300=₹3$ crore; OEE up 3 points on a sold-out line worth ₹200 crore sales at 28% contribution: $3/70\times200\times0.28\approx₹2.4$ crore (if OEE base is 70%); energy 5% on ₹40 crore saves ₹2 crore; procurement 1% on ₹300 crore saves ₹3 crore. Total about ₹10.4 crore, so the target is feasible but needs all four levers, and the OEE benefit depends on demand. A consultant states which levers are low-risk (energy, scrap) and which depend on the market.

### In the news
See news box. Hansalpur's expansion and the Nexperia halt are good "capacity and risk" case anchors for a discussion.

### Interview angle
> [!question] How it is asked
> "We make 1 million units a year at 65% utilisation. Should we expand?"

> [!tip] Strong answer includes
> - Demand forecast and target utilisation; expansion triggers
> - Debottleneck and OEE options before capex; capacity in the right location
> - Economics: contribution, capex, payback, NPV; risk (supply, regulatory)
> - A clear recommendation with conditions and next steps
