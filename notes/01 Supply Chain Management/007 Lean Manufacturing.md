---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Lean Manufacturing"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 16
---
# Lean Manufacturing

⬅ [[006 Manufacturing Systems]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[008 Six Sigma & Quality Tools]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Lean Principles]]
2. [[#2. 7 Wastes (Muda)]]
3. [[#3. Value Stream Mapping (VSM)]]
4. [[#4. Kaizen]]
5. [[#5. 5S Methodology]]
6. [[#6. Kanban System]]
7. [[#7. Poka-Yoke (Error Proofing)]]
8. [[#8. Jidoka (Autonomation)]]
9. [[#9. Takt Time]]
10. [[#10. SMED (Single Minute Exchange of Die)]]
11. [[#11. Total Productive Maintenance (TPM)]]
12. [[#12. Heijunka (Production Leveling)]]
13. [[#13. Gemba Walk]]
14. [[#14. Lean Metrics]]
15. [[#15. ⭐ Advanced: Little's Law and Flow Variability]]
16. [[#16. ⭐ Advanced: Theory of Constraints and Lean]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): lean meets AI at Toyota, and quality lapses cost Boeing its growth
> **Toyota gives plant staff AI for kaizen (reported Nov 2025).** Toyota built an in-house platform on Google Cloud so shop-floor workers can create machine-learning models without writing code. Reported figures: **1,200+ factory workers across 10 plants**, **10,000+ models built by workers**, **10,000+ man-hours saved annually** and roughly **20% faster model creation**. The point for lean: respect for people and continuous improvement, with digital tools in the hands of the people closest to the process. ([Lean Tomatoes, 19 Nov 2025](https://leantomatoes.com/2025/11/19/toyota-using-ai-to-reinvent-kaizen-and-boost-productivity/))
>
> **Boeing: quality lapses cap the production rate (Jan 2024 to Oct 2025).** After a door-sized panel detached from an Alaska Airlines 737 MAX in January 2024, the FAA capped 737 MAX output at **38 aircraft per month**; Boeing reached 38 in May 2025 and on **17 Oct 2025** the FAA allowed an increase to **42 per month**. Boeing posted a Q2 2025 net loss of **$612 million** (vs $1.4 billion a year earlier). A reminder that building quality in (jidoka, poka-yoke, standard work) is cheaper than inspecting or fixing late. ([Spokesman-Review](https://www.spokesman.com/stories/2025/oct/17/after-months-of-limits-faa-allows-boeing-to-increa/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Lean Principles
> 🔴 Tier 1 · _Tracker hint:_ 5 Lean principles: value, value stream, flow, pull, perfection

### Definition
**Lean** is a management system built on the Toyota Production System that maximises customer value while minimising waste. Womack and Jones (*Lean Thinking*, 1996) set out five principles:

1. **Specify value** from the *customer's* point of view: what they will pay for.
2. **Identify the value stream**: all steps (value-adding and not) from raw material to customer; remove steps that add no value.
3. **Make value flow**: one-piece or small-batch flow without queues, stops or rework.
4. **Establish pull**: produce only what the downstream customer signals (see kanban).
5. **Pursue perfection**: continuous improvement (kaizen); the other four repeat in a loop.

Two pillars of the TPS "house": **Just-in-Time** and **Jidoka**, resting on stability (heijunka, standardised work, kaizen) and a culture of **respect for people**. Distinguish lean from cost-cutting: lean reduces waste *and* builds capability.

### Example
Toyota's chain: the customer order triggers a body-shop signal, which pulls parts from suppliers through kanban; every operation can stop the line (andon) to fix a defect at source. Numerically, a plant that cuts lead time from 10 days to 2 days with the same demand needs 80% less WIP by Little's Law (WIP = throughput x lead time).

### In the news
See news box. Toyota's AI for kaizen is principle five applied with new tools; Boeing's rate cap shows what happens when value (a safe aircraft) is not protected at every step.

### Interview angle
> [!question] How it is asked
> "What is lean manufacturing?" or "Can lean be applied to a bank, a hospital or a consulting firm?"

> [!tip] Strong answer includes
> - The five principles in order, with value defined by the customer
> - JIT and Jidoka as the two pillars; respect for people as the foundation
> - Application beyond factories (information flow, waiting, rework are waste everywhere)
> - Pitfall: lean as a cost-cutting tool or a toolbox without culture

---

## 2. 7 Wastes (Muda)
> 🔴 Tier 1 · _Tracker hint:_ TIMWOOD: Transport, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects

### Definition
**Muda** is any activity that consumes resources but adds no value the customer will pay for. The seven wastes (Taiichi Ohno) spell **TIMWOOD**:

| Waste | Meaning | Typical sign |
|---|---|---|
| **T**ransport | Unnecessary movement of material | Long forklift routes between departments |
| **I**nventory | Excess raw material, WIP, finished goods | Piles between stations, obsolete stock |
| **M**otion | Unneeded movement by people | Searching, bending, walking to tools |
| **W**aiting | Idle people, machines or material | Waiting for approval, parts, repair |
| **O**verproduction | Making more or earlier than needed | The worst waste: causes the others |
| **O**verprocessing | More work than the spec needs | Tight tolerances, extra inspections |
| **D**efects | Rework, scrap, returns | Repair loops, warranty claims |

An **eighth waste** often added: unused talent/creativity. Related terms: **Mura** (unevenness) and **Muri** (overburden) make up the "3Ms" of waste.

### Example
A packing line's operators walk 12 m to fetch cartons: 4 trips per hour x 8 hours x 12 m x 2 (return) = 768 m per shift per operator. Moving cartons to a point-of-use shelf removes that motion and transport, giving about 25 minutes per shift at 0.5 m/s, a 5% productivity gain from one change.

### In the news
See news box. Boeing's rework and delays in the 737 MAX factory are textbook defect and waiting waste, at huge cost.

### Interview angle
> [!question] How it is asked
> "Name the seven wastes and identify them in this process." (often with a picture or a short process description)

> [!tip] Strong answer includes
> - All seven named correctly, and why overproduction is "the mother of all wastes"
> - Link of each waste to a visible symptom and a fix (5S, pull, layout, SMED, poka-yoke)
> - Prioritise by impact instead of listing everything
> - Mention Mura and Muri and the "8th waste" for completeness

---

## 3. Value Stream Mapping (VSM)
> 🔴 Tier 1 · _Tracker hint:_ Current vs future state map; value-added vs non-value-added time

### Definition
**VSM** draws the flow of material and information for one product family from supplier to customer, with data boxes at each step: **cycle time (C/T)**, changeover time (C/O), uptime, number of operators, batch size, inventory.

Steps: (1) select the product family, (2) draw the **current-state map** by walking the process (gemba), (3) compute **lead time** (total elapsed) and **process/value-added time**, (4) design the **future-state map** (flow, pull, supermarkets, heijunka, takt), (5) action plan with owners and dates.

Key metrics:
- Lead time $LT$ = sum of process times + waiting/queue times (inventory days)
- **Process cycle efficiency** $PCE = \dfrac{\text{Value-added time}}{\text{Total lead time}}$
Typical PCE in discrete manufacturing is under 5%; world-class lean is 25% or more. Information flow symbols show how production is scheduled (push or pull).

### Example
Four steps with cycle times 2, 5, 3, 4 min = 14 min value-added. Inventory between steps adds up to 9 working days of 480 min = 4,320 min lead time. $PCE = 14/4{,}320 = 0.32\%$. Future state with a supermarket and smaller batches cuts inventory to 1 day: LT = 480 + 14 = 494 min, $PCE = 14/494 \approx 2.8\%$, almost 9 times better, without touching machine speed.

### In the news
See news box. At Boeing the constraint is not speed but flow and quality; VSM would show where aircraft wait for rework rather than where they are built.

### Interview angle
> [!question] How it is asked
> "How would you find where the time goes in this order-to-delivery process?" or "What is VSM and what is process cycle efficiency?"

> [!tip] Strong answer includes
> - Current vs future state and the walk-the-process method
> - Lead time vs value-added time arithmetic and PCE
> - Information flow (how orders are scheduled) as well as material flow
> - Turn the map into a prioritised kaizen plan with metrics

---

## 4. Kaizen
> 🔴 Tier 1 · _Tracker hint:_ Continuous improvement events (Kaizen Blitz), employee involvement, incremental change

### Definition
**Kaizen** ("change for the better") is continuous, incremental improvement involving **everyone**, from operators to executives. Forms:
- **Daily kaizen**: small ideas from the workers (suggestion systems; Toyota gets large numbers per employee).
- **Kaizen event / Blitz**: a focused 3–5 day, cross-functional team improves one process, using data and gemba observation, then standardises.
- **Kaikaku**: radical change (contrast with kaizen).
- **PDCA cycle** (Plan-Do-Check-Act) is the engine; improvements are locked in by **standard work** (SDCA), the base for the next cycle.

Success factors: management support, visual management, quick implementation, recognition, follow-up audits. Failure causes: one-off events without sustainment, ideas ignored, no time released for improvement.

### Example
Kaizen event on a fastening station: operator reaches 40 cm for each screw; moving the bin 20 cm closer saves 4 seconds per cycle. At 600 cycles a day, savings $= 4 \times 600 = 2{,}400$ s $= 40$ min per day per operator, worth about 8% of a 480-min shift for a cost of a few hundred rupees.

### In the news
See news box. Toyota's AI platform for kaizen: workers build their own models, a modern version of the suggestion system.

### Interview angle
> [!question] How it is asked
> "How would you create a continuous improvement culture in a plant?"

> [!tip] Strong answer includes
> - Kaizen vs kaikaku, daily kaizen vs events, PDCA
> - Governance: visual boards, gemba walks, suggestion handling, recognition
> - Standardise gains and quantify results (time, cost, quality)
> - Cultural point: blame the process, not the person

---

## 5. 5S Methodology
> 🔴 Tier 1 · _Tracker hint:_ Sort, Set in order, Shine, Standardize, Sustain — with audit process

### Definition
**5S** is a workplace organisation method (Japanese: Seiri, Seiton, Seiso, Seiketsu, Shitsuke):

| 5S | Action |
|---|---|
| **Sort** (Seiri) | Remove what is not needed (red-tag unneeded items) |
| **Set in order** (Seiton) | A place for everything: shadow boards, labelling, "first-in, first-out" locations |
| **Shine** (Seiso) | Clean and inspect; cleaning finds leaks and faults |
| **Standardize** (Seiketsu) | Visual standards, checklists, who does what and when |
| **Sustain** (Shitsuke) | Discipline, training, audits, leadership habits |

**Audit process:** a cross-functional team scores each "S" on a checklist (for example 0–4 per question or per S), photographs, publishes the score on a board, assigns corrective actions, and re-audits. A sixth S, **Safety**, is common.

5S is the base for lean: it makes abnormalities visible and enables standard work.

### Example
Audit of one area: Sort 3, Set in order 2, Shine 3, Standardize 2, Sustain 1, each out of 4. Score $= 11/20 = 55\%$. Target 80% in 90 days, so focus on Sustain and Standardize: daily 5-minute checks, shift-end cleaning and a monthly audit.

### In the news
See news box. Boeing's 2024 door-panel incident exposed "production lapses" in its Renton factory; lapses of that kind (work not done to a visible standard) are what 5S, visual control and standard work exist to prevent. (The link is an analytical reading, not an investigation finding.)

### Interview angle
> [!question] How it is asked
> "How would you implement 5S in a warehouse?" or "Why does 5S fail after three months?"

> [!tip] Strong answer includes
> - Five steps with a real example (labelled bins, shadow boards, floor markings)
> - An audit mechanism with scoring and follow-up
> - Sustain: leadership routines, ownership by area, links to KPIs
> - Benefits: safety, search time, quality, space

---

## 6. Kanban System
> 🔴 Tier 1 · _Tracker hint:_ Signal-based pull; kanban card, e-kanban, supermarket concept

### Definition
**Kanban** (signal card) is a pull system: downstream consumption triggers upstream production or replenishment. Types: **production kanban** (authorises making a container), **withdrawal/move kanban** (authorises taking one from the **supermarket**, the controlled stock of parts), **supplier kanban**. **E-kanban** replaces cards with barcode scans or ERP triggers across supplier sites. Rules: no production without a card, never pass on a defect, limit WIP to the number of cards, smooth demand (heijunka), refine over time.

Number of kanban containers:

$$N = \frac{D \times L \times (1 + \alpha)}{C}$$

where $D$ is demand rate, $L$ is replenishment lead time, $\alpha$ is a safety factor, $C$ is container size. More cards = more inventory; reducing cards exposes problems (like lowering the water level to reveal rocks). Works best with repetitive, stable demand and short lead times; poor for lumpy, high-variety, long lead-time items.

### Example
$D = 60$ units/h, $L = 0.5$ h, $\alpha = 10\%$, $C = 12$: $N = 60 \times 0.5 \times 1.1 / 12 = 33/12 = 2.75$, so **3 cards**. The inventory ceiling is $3 \times 12 = 36$ units. The same logic is used in the two-bin system for fasteners at an assembly line.

### In the news
See news box. Toyota's digital tools are layered on top of kanban and andon; the cards still rule the pull system.

### Interview angle
> [!question] How it is asked
> "How many kanbans do you need?" or "When does kanban not work?"

> [!tip] Strong answer includes
> - The signal logic and the supermarket concept
> - The $N$ formula with a numeric example, rounded up
> - Conditions: stable demand, small lots, reliable lead time
> - Alternatives for lumpy demand: CONWIP, MRP, min-max rules

---

## 7. Poka-Yoke (Error Proofing)
> 🔴 Tier 1 · _Tracker hint:_ Prevention vs detection; checklists, fixtures, sensors, interlocks

### Definition
**Poka-yoke** (Shigeo Shingo) is any device or method that makes errors impossible or immediately visible. Two types:
- **Prevention** (control): the process cannot proceed wrongly: asymmetrical fixtures, keyed connectors, interlocks.
- **Detection** (warning): the error is caught at once: sensors, counters, checklists, alarms, go/no-go gauges.

Methods (Shingo): **contact** (shape/size sensing), **fixed-value** (counting, e.g. all 8 screws used), **motion-step** (sequence checking). Best practice: error-proof at the source (source inspection), rather than inspect later; cost is low relative to scrap. Hierarchy: eliminate, prevent, detect, mitigate.

Link with quality: poka-yoke reduces defects toward zero and is a key improvement action in FMEA ([[008 Six Sigma & Quality Tools]]), where it lowers the **Detection** and **Occurrence** scores.

### Example
Diesel nozzles are wider than petrol car fill necks so diesel cannot enter a petrol tank: a physical poka-yoke. Numeric: an assembly with a 1.2% mis-fit defect rate on 50,000 units produces 600 defects; a fixture that blocks wrong orientation (95% effective) leaves 30, saving 570 reworks at, say, ₹150 each = ₹85,500.

### In the news
See news box. Boeing's 2024 incident exposed factory "production lapses"; error-proofing and verification at the source is the lean answer to such lapses (analytical reading).

### Interview angle
> [!question] How it is asked
> "How would you reduce mis-picks in a warehouse?" or "What is poka-yoke? Give an example."

> [!tip] Strong answer includes
> - Prevention vs detection and why prevention is better
> - A concrete example in the context (barcode scan confirms location and SKU; weight check at pack)
> - Where in the process (source) and the cost-benefit
> - Link to FMEA: raises detectability, lowers occurrence

---

## 8. Jidoka (Autonomation)
> 🔴 Tier 1 · _Tracker hint:_ Auto-detect + stop; andon cord; human intervention triggers

### Definition
**Jidoka** ("automation with a human touch") means machines and operators **detect an abnormality and stop** automatically so defects never pass downstream. Origin: Sakichi Toyoda's loom that stopped when a thread broke. It is the second pillar of the TPS (with JIT).

Four steps: (1) detect the abnormality, (2) stop, (3) fix the immediate problem, (4) investigate and correct the root cause. **Andon** (light/board, pull cord or button) signals the problem and location; the team leader responds within seconds. Separation of man and machine: operators supervise several machines instead of watching one, so productivity rises *and* quality is built in.

Human intervention triggers: quality alarm, tool wear, missing part, safety issue, cycle time over takt. Cost of stopping is accepted because defects found later cost more (the "1-10-100 rule" is a rule of thumb).

### Example
Before jidoka a loom needs one weaver per machine; with auto-stop one operator can run several machines. Illustrative: if 30 looms need 30 workers before and 5 after (1:6), labour falls 83% while defects are caught instantly, instead of at the end of the shift.

### In the news
See news box. Toyota's workers train AI to detect abnormalities, extending jidoka (machines that sense) into software; Boeing's case is the failure mode where a defect continued down the line.

### Interview angle
> [!question] How it is asked
> "What is jidoka and how is it different from automation?" or "Should a worker be allowed to stop the line?"

> [!tip] Strong answer includes
> - Detect, stop, fix, investigate: the four steps
> - Andon and the policy that anyone can stop the line without blame
> - Separation of man and machine
> - Trade-off: short-term output loss against long-term quality, and why the economics favour stopping

---

## 9. Takt Time
> 🔴 Tier 1 · _Tracker hint:_ Available time / Customer demand; sets production rhythm

### Definition
**Takt time** (German: beat) is the pace of production needed to meet customer demand:

$$T_{takt} = \frac{\text{Net available production time}}{\text{Customer demand (units)}}$$

Net time excludes breaks, planned maintenance and meetings. Takt is set by the *customer*, not by the machine. Related terms: **cycle time** (actual time per unit at a station; must be $\le$ takt), **pitch** (takt x pack-out quantity), **required staff** $= \dfrac{\text{Total work content}}{T_{takt}}$.

If cycle time > takt, the line cannot meet demand (add capacity, split work, reduce time); if much less, the station idles or overproduces (overproduction waste). Takt is recalculated when demand changes (monthly or quarterly), and operators adjust staffing in U-cells.

### Example
Single shift 450 min of net time = 27,000 s; daily demand 900 units: $T_{takt} = 27{,}000 / 900 = 30$ s. Total work content 150 s per unit means $150/30 = 5$ operators. If demand rises to 1,125 units, takt $= 24$ s and staff $= 150/24 = 6.25$, so about 7 operators or reduce content.

### In the news
See news box. Boeing's cap is a regulator-set "takt": 38 then 42 aircraft per month, forcing quality and flow to match the permitted rhythm.

### Interview angle
> [!question] How it is asked
> "A customer wants 1,000 units per day. Compute takt time and the staff you need."

> [!tip] Strong answer includes
> - Formula using net available time, with the numeric answer
> - Difference between takt, cycle time and lead time
> - Staffing formula and what to do when cycle time exceeds takt
> - Update takt when demand changes; heijunka to stabilise it

---

## 10. SMED (Single Minute Exchange of Die)
> 🔴 Tier 1 · _Tracker hint:_ Internal vs external setup; parallel activities; standardize

### Definition
**SMED** (Shigeo Shingo) cuts changeover time to **under 10 minutes** (single-digit minutes). Changeover time is measured from the **last good piece of product A to the first good piece of product B**.

Steps:
0. **Observe** the current changeover (video, time every element).
1. **Separate** internal (machine must be stopped) from external (can be done while running: fetching tools, pre-heating, pre-staging material).
2. **Convert** internal elements to external wherever possible.
3. **Streamline** internal elements: quick-release clamps, standard heights, eliminate adjustments (settings by numbers), one-turn fasteners.
4. **Parallelise** activities with several people; use pit-crew style choreography.
5. **Standardise** and sustain with checklists.

Benefits: smaller batches, shorter lead time, higher flexibility and OEE availability, lower inventory.

### Example
Changeover 90 min: 60 internal, 30 external (but done with the machine stopped). Step 1-2: move the 30 external out, now machine stops 60 min. Step 3-4: improvements halve internal time to 30 min, and a second operator cuts 5 more, so 25 min. Four changeovers a day: saved $4 \times (90 - 25) = 260$ min per day, over 4 hours of extra capacity, or the same changeover loss supporting batches about 72% smaller ($65/90$).

### In the news
See news box. Toyota's variety of models on one line relies on very fast changeovers: the kaizen AI tools are aimed at removing such time losses.

### Interview angle
> [!question] How it is asked
> "A press line takes 2 hours to change dies and the batches are huge. What do you do?"

> [!tip] Strong answer includes
> - Internal vs external distinction and the conversion step
> - Measure first (video), then the steps with an arithmetic example
> - Link to batch size, EPQ and lead time ([[006 Manufacturing Systems]])
> - Sustain: standard checklists and operator ownership

---

## 11. Total Productive Maintenance (TPM)
> 🔴 Tier 1 · _Tracker hint:_ 8 pillars; OEE = Availability × Performance × Quality

### Definition
**TPM** (from Japan Institute of Plant Maintenance) makes **operators and maintenance jointly responsible** for equipment effectiveness, targeting zero breakdowns, zero defects and zero accidents. The **8 pillars**: (1) Autonomous maintenance (Jishu Hozen), (2) Planned maintenance, (3) Focused improvement (Kobetsu Kaizen), (4) Quality maintenance, (5) Early equipment management, (6) Training and education, (7) Safety, health and environment, (8) TPM in administration (office TPM).

**OEE** (Overall Equipment Effectiveness):

$$OEE = \text{Availability} \times \text{Performance} \times \text{Quality}$$

- Availability = run time / planned production time (losses: breakdowns, changeovers)
- Performance = (ideal cycle time x total count) / run time (losses: slow cycles, minor stops)
- Quality = good count / total count (scrap, rework)
Benchmark: 85% is often called world class; typical plants are 40–60%. Six big losses map into the three factors. **TEEP** uses calendar time.

### Example
Planned time 480 min; downtime 48 min so run time 432 min: $A = 432/480 = 90\%$. Ideal cycle 1 min; made 410 parts: $P = 410/432 = 94.9\%$. Good parts 402: $Q = 402/410 = 98.0\%$. $OEE = 0.90 \times 0.949 \times 0.980 = 83.7\%$ (check: $402 \times 1 / 480 = 83.75\%$).

### In the news
See news box. Toyota's workers building ML models target availability and minor stoppages, the largest hidden OEE losses.

### Interview angle
> [!question] How it is asked
> "Calculate OEE from this shift data and tell me where to focus."

> [!tip] Strong answer includes
> - Formula and the three components with the six big losses
> - Worked calculation, identifying the weakest factor
> - TPM pillars, especially autonomous maintenance and planned maintenance
> - Caution: do not chase OEE on non-bottleneck machines (overproduction)

---

## 12. Heijunka (Production Leveling)
> 🔴 Tier 1 · _Tracker hint:_ Volume and mix leveling; reduces bullwhip; heijunka box

### Definition
**Heijunka** levels production in **volume** and **mix** over time so the plant makes a steady rhythm of every product, instead of building in big batches according to order arrival. It converts uneven customer orders into a stable schedule at the **pacemaker process**, which lowers inventory, overtime, and the "whip" passed to suppliers.

Tools: **Heijunka box** (a grid with rows of products and columns of time slots, holding kanban cards released every pitch), **EPEI** (every part every interval: how often a product repeats; shorter with SMED), levelled sequence, finished-goods supermarket to absorb demand swings.

Link to the **bullwhip effect** ([[001 SCM Introduction & Fundamentals]]): levelling reduces order-variability transmitted upstream, enabling suppliers to plan capacity and stock. Trade-off: needs finished stock or flexible capacity to absorb actual demand swings.

### Example
Monthly demand 600 A, 300 B, 100 C (20 working days): daily 30 A, 15 B, 5 C = 50 units, a 6:3:1 mix. Repeat a 10-unit pattern **A B A C A B A A B A** (6 A, 3 B, 1 C). Without levelling the plant would run A for 12 days, then B for 6, then C for 2, creating long waits and uneven supplier demand.

### In the news
See news box. Boeing's "rate" increases (38 to 42 a month) are gradual and stepwise, which resembles levelled ramp-ups to protect quality and suppliers.

### Interview angle
> [!question] How it is asked
> "What is heijunka and why does Toyota use it?"

> [!tip] Strong answer includes
> - Volume vs mix levelling, with a numeric sequence example
> - Heijunka box and pitch
> - Benefits: stable labour and supplier demand, less inventory, bullwhip reduction
> - Costs: more changeovers (needs SMED), finished-goods buffer

---

## 13. Gemba Walk
> 🔴 Tier 1 · _Tracker hint:_ Go-and-see leadership; observation, questioning, respect

### Definition
**Gemba** ("the real place") is where value is created: shop floor, ward, site, call-centre. A **gemba walk** is a structured visit by leaders to *observe the work*, talk with the people doing it, and understand problems with first-hand facts (genchi genbutsu: go and see). It is *not* a surprise audit.

Good practice:
- Prepare a **theme** (safety, flow, quality) and a route; announce the purpose.
- **Observe** process, not people; look for the 7 wastes and abnormalities against standards.
- **Ask** open questions (Why? Show me), use 5 Whys, listen.
- **Respect**: never blame; leave coaching and recognition; do not give instant orders.
- **Follow up**: record observations, assign actions, close the loop.
Ohno's "Ohno circle" (standing in a chalk circle to watch for an hour) is the classic exercise.

### Example
A plant head walks the packing line at shift start for 30 minutes weekly. She notices operators wait 6 min for cartons after every 2 hours. Question: "What happens before this?" Result: delivery route redesigned; waiting of 6 min x 4 per shift x 3 operators = 72 operator-minutes per day recovered.

### In the news
See news box. Gemba is where Toyota's AI-built models get their problems from, and where Boeing's quality lapses would have been visible earlier. (Analytical reading, not a reported fact.)

### Interview angle
> [!question] How it is asked
> "How would you, as a new plant manager, understand the problems in your first 30 days?"

> [!tip] Strong answer includes
> - Go and see, ask, respect (the three elements) and a clear theme
> - What to look for: waste, standard work deviations, visual controls
> - Behaviours that fail: criticising, taking over the work, no follow-up
> - Tie to KPIs and the kaizen board

---

## 14. Lean Metrics
> 🔴 Tier 1 · _Tracker hint:_ Cycle time, lead time, first pass yield, OEE, scrap rate

### Definition
Lean metrics make flow and quality visible.

| Metric | Formula / meaning |
|---|---|
| **Cycle time** | Time to complete one unit at a step (must be $\le$ takt) |
| **Lead time** | Order-to-delivery elapsed time (includes waiting) |
| **Process cycle efficiency** | Value-added time / lead time |
| **First pass yield (FPY)** | Good units first time / units entering step |
| **Rolled throughput yield (RTY)** | $\prod FPY_i$ across steps |
| **Scrap rate** | Scrapped units / units produced |
| **OEE** | Availability x Performance x Quality |
| **WIP and inventory turns** | WIP count; COGS / average inventory |
| **On-time delivery, DPMO, changeover time** | Service and quality |

**Little's Law:** $WIP = Throughput \times Lead\ time$. Metrics must be **visual, near real time, owned by the team**, and drive action, not reporting. Beware local optimisation (a high OEE on a non-bottleneck builds WIP).

### Example
Three steps with FPY 98%, 95%, 97%: $RTY = 0.98 \times 0.95 \times 0.97 = 0.903$, so only 90.3% of units are good first time, even though each step looks fine. Scrap/rework 9.7% of units. Improving the worst step to 98%: $0.98^2 \times 0.97 = 0.932$ (+2.9 points).

### In the news
See news box. Toyota's reported 10,000+ hours saved is a cycle/availability style benefit; Boeing's recovery is tracked by rate (aircraft per month) and defects.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track to judge a lean transformation in this plant?"

> [!tip] Strong answer includes
> - A balanced set: flow (lead time, WIP), quality (FPY, RTY), equipment (OEE), delivery (OTD), people (safety, kaizen count)
> - RTY multiplication and why FPY hides rework
> - Little's Law
> - Targets, owners, frequency and avoiding gaming or local optima

---

## 15. ⭐ Advanced: Little's Law and Flow Variability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Little's Law** (1961): in a stable system, average inventory (WIP) $= $ average throughput $\times$ average time in system:

$$WIP = TH \times CT$$

It holds for any stable process (factory, hospital, call-centre, a ticket queue), no matter the distribution. To cut lead time without changing throughput, **cut WIP** (kanban limits, CONWIP). Corollaries: lead time $= WIP / TH$; at fixed WIP, raising throughput shortens lead time.

**Kingman's approximation** shows queue time rises sharply with **utilisation** $\rho$ and **variability**:

$$W_q \approx \frac{\rho}{1-\rho} \times \frac{c_a^2 + c_s^2}{2} \times t_s$$

At 95% utilisation queues are far longer than at 80%. That is why lean aims for stable, levelled flow and spare capacity at the bottleneck rather than 100% utilisation.

### Example
WIP of 120 units and throughput 30 units/h: $CT = 120/30 = 4$ h. Reduce WIP to 60 with the same throughput: $CT = 2$ h. Utilisation effect with $c_a = c_s = 1$ and $t_s = 1$ h: at $\rho = 0.8$: $W_q = 4 \times 1 \times 1 = 4$ h; at $\rho = 0.95$: $19 \times 1 \times 1 = 19$ h, nearly five times as long.

### In the news
See news box. Boeing's cap shows a system pushed beyond its control capability: when variability (quality issues) is high, running a factory at maximum rate lengthens lead time and creates rework.

### Interview angle
> [!question] How it is asked
> "A hospital/plant has long waiting times; utilisation is 95%. What do you suggest?"

> [!tip] Strong answer includes
> - Little's Law with numbers; WIP caps as the lever
> - Utilisation-variability-queue relationship (Kingman), and why 100% utilisation is a trap
> - Reduce variability (levelling, SMED, standard work) before adding capacity
> - Apply to services as well as to factories

---

## 16. ⭐ Advanced: Theory of Constraints and Lean
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Theory of Constraints (TOC, Goldratt)**: a system's output is limited by its **constraint (bottleneck)**; improving non-constraints gives no system benefit. **Five focusing steps:** (1) Identify the constraint, (2) Exploit it (keep it busy on valuable work, never starved or blocked), (3) Subordinate everything else to it, (4) Elevate it (add capacity), (5) Repeat: find the next constraint (avoid inertia).

**Drum-Buffer-Rope (DBR):** drum = constraint's pace; buffer = time or stock protecting it; rope = release of material tied to the drum. **Throughput accounting:** maximise throughput $T$ (sales minus truly variable cost), minimise inventory $I$ and operating expense $OE$; net profit $= T - OE$.

Complements lean: lean removes waste everywhere (flow, pull), TOC focuses on the one place where an hour saved is worth an hour of system output.

### Example
Stations A 10/h, B 6/h, C 8/h: bottleneck B, system output 6/h. An hour lost at B loses 6 units for the whole system; an extra hour of A gives nothing. Elevating B to 8/h lifts output to 8 (C becomes the constraint): +33% ($8/6 - 1$). If each unit contributes ₹500 throughput, 2 more units an hour over 2,000 hours is ₹20 lakh a year ($2 \times 2{,}000 \times 500$).

### In the news
See news box. For Boeing the 737 line's constraint shifted from fuselage supply to quality sign-off and regulator approval: the FAA rate cap *was* the constraint, and relieving it needed process confidence.

### Interview angle
> [!question] How it is asked
> "Output is below target but all machines show high utilisation. Where do you start?"

> [!tip] Strong answer includes
> - Find the bottleneck first (lowest capacity or longest queue before it)
> - Five focusing steps in order, and DBR
> - Exploit before investing: reduce changeovers and breaks at the bottleneck, add quality checks before it
> - Link to lean: pull, takt and OEE on the bottleneck only

---
## 🔗 Go deeper: expansion notes
- [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work|Lean Management Systems - A3, Hoshin Kanri & Standard Work]]
- [[152 Learning Curves, Work Measurement & Productivity|Learning Curves, Work Measurement & Productivity]]
