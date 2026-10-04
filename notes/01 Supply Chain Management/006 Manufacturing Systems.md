---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Manufacturing Systems"
tier: Tier 2
roles: Operations
status: complete
subtopics: 14
---
# Manufacturing Systems

⬅ [[005 Production & Operations Planning]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[007 Lean Manufacturing]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Job Production]]
2. [[#2. Batch Production]]
3. [[#3. Mass Production]]
4. [[#4. Continuous Production]]
5. [[#5. Cellular Manufacturing]]
6. [[#6. Flexible Manufacturing System (FMS)]]
7. [[#7. Industry 4.0 Technologies]]
8. [[#8. Digital Twin]]
9. [[#9. Smart Manufacturing]]
10. [[#10. Additive Manufacturing (3D Printing)]]
11. [[#11. Automation & Robotics]]
12. [[#12. Industrial IoT (IIoT)]]
13. [[#13. ⭐ Advanced: Product-Process Matrix (Hayes and Wheelwright)]]
14. [[#14. ⭐ Advanced: Assembly Line Balancing]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): robots, AI and digital twins reach the shop floor
> **Record robot installs, India in the top 6 (2024 data, released Sep 2025).** The International Federation of Robotics (World Robotics 2025, released 25 Sep 2025) reports **542,000 industrial robots installed worldwide in 2024**, an operational stock of **4.664 million (+9%)**. China installed a record **295,000 (54% of the world)**. India installed **9,100 units (+7%)**, ranking **6th globally**, with automotive driving **45%** of Indian demand. ([IFR](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years))
>
> **Toyota puts AI in workers' hands for kaizen (reported Nov 2025).** Toyota built an in-house platform on Google Cloud that lets plant staff build machine-learning models without coding. Reported figures: **1,200+ factory workers across 10 plants**, **10,000+ models built**, **10,000+ man-hours saved a year** and about **20% faster model creation**. ([Lean Tomatoes, 19 Nov 2025](https://leantomatoes.com/2025/11/19/toyota-using-ai-to-reinvent-kaizen-and-boost-productivity/))
>
> **Foxconn's digital-twin factories (NVIDIA case study, 2025).** Foxconn uses NVIDIA Omniverse digital twins to validate a new factory (e.g. its Houston, Texas facility) virtually before building; the case study claims AI thermal simulations that are **150x faster** and a **~50% cut in time-to-revenue** for factory set-up. These are vendor-published claims, and the page gives no dates. ([NVIDIA](https://www.nvidia.com/en-us/case-studies/foxconn-develops-physical-ai-enabled-smart-factories-with-digital-twins/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Job Production
> 🟠 Tier 2 · _Tracker hint:_ Custom orders, high flexibility, low volume, high skill

### Definition
**Job production** (job shop, "one-off" production) makes a single, customised product or very small order to a customer's specification. Each job has its own routing through general-purpose machines grouped by function (a **process layout**: all lathes together, all welders together).

| Feature | Job production |
|---|---|
| Volume / variety | Very low volume, very high variety |
| Equipment | General purpose, flexible |
| Labour | Highly skilled, multi-task |
| Unit cost | High |
| Flow | Jumbled, long queues, high WIP |
| Scheduling | Hard: every job differs |
| Strategy fit | Make-to-order or engineer-to-order |

Strengths: flexibility, customisation, premium pricing. Weaknesses: low utilisation, long lead times, difficult costing and scheduling. Typical performance levers: priority rules (EDD, SPT), finite-capacity scheduling, group technology (see Cellular Manufacturing).

### Example
A tool-and-die shop in Pune makes an injection mould for an auto supplier: one unit, 6 weeks, passing through CNC milling, EDM, grinding, polishing and trials. Machines are shared among 20 jobs, so a job spends most of its 6 weeks (about 1,008 hours) waiting. If actual processing is 80 hours, flow efficiency is $80/1008 \approx 7.9\%$.

### In the news
See news box. IFR counts only installed robots, but job shops are the segment where flexible cobots and AI-assisted programming are now being tried because fixed automation does not pay for one-off work.

### Interview angle
> [!question] How it is asked
> "What type of production system would you recommend for a company making customised industrial machinery?" or "Why is scheduling hard in a job shop?"

> [!tip] Strong answer includes
> - Link to the volume-variety trade-off (low volume, high variety) and the process layout
> - Why utilisation and flow efficiency are low (queues and set-ups) and what to do (priority rules, scheduling, cells)
> - Pricing logic: customisation justifies premium; costing is by job
> - A reference to the CODP: make-to-order or engineer-to-order

---

## 2. Batch Production
> 🟠 Tier 2 · _Tracker hint:_ Groups of similar items, changeover time, economies of scale

### Definition
**Batch production** makes a limited quantity (a lot) of an identical product, then changes the set-up to the next product. It sits between job and mass production: moderate volume and variety. Machines are flexible but not fully general; the main cost is **changeover (set-up) time**, which is a non-productive loss spread across the batch.

Per-unit time with batch size $Q$, set-up $S$ and run time $r$ per unit:

$$t_{unit} = \frac{S}{Q} + r$$

Larger batches dilute set-up but raise WIP, lead time and risk of obsolescence. The optimum is the **economic production quantity** $EPQ = \sqrt{\dfrac{2DS_c}{h(1 - d/p)}}$, where $D$ is annual demand, $S_c$ set-up cost, $h$ holding cost, $d$ demand rate and $p$ production rate. Lean answer: shrink the set-up (SMED) rather than accept big batches. Examples of batch industries: bakeries, pharma tablets, paints, garments, auto components.

### Example
A bottler has set-up $S = 2$ hours and run time $r = 0.1$ hour per unit.
- $Q = 500$: total $= 2 + 50 = 52$ h, so $0.104$ h per unit.
- $Q = 100$: total $= 2 + 10 = 12$ h, so $0.12$ h per unit (15.4% worse).
Cutting set-up to 0.5 h makes $Q = 100$ cost $0.105$ h per unit, nearly the same as a batch of 500. That is the business case for SMED. See [[007 Lean Manufacturing]].

### In the news
See news box. Toyota's AI-for-kaizen programme targets exactly this kind of plant-floor loss (set-ups, downtime, minor stoppages) in a batch/mass hybrid environment.

### Interview angle
> [!question] How it is asked
> "A plant produces 40 SKUs in batches and customers complain about long lead times. What would you do?"

> [!tip] Strong answer includes
> - Identify set-up time as the driver of batch size and lead time
> - Quantify with $S/Q + r$ or EPQ logic
> - Remedies: SMED, smaller lot sizes, sequencing by similarity, heijunka, cellular layout
> - Trade-off: smaller batches raise changeover frequency, so utilisation can fall unless set-up is cut

---

## 3. Mass Production
> 🟠 Tier 2 · _Tracker hint:_ Dedicated lines, high standardization, low unit cost

### Definition
**Mass production** makes large volumes of a standardised product on a **dedicated, paced line** (product layout). Work is divided into short, repetitive tasks (division of labour) with interchangeable parts, special-purpose machines and moving material handling. The aim is the lowest unit cost through **economies of scale**: fixed costs spread over huge volume and learning effects.

Key design variable is **line balance** (see the advanced section on line balancing). Weaknesses: inflexibility (model changes are expensive), vulnerability to a single breakdown stopping the line, monotony for workers, and risk if demand shifts. Modern variants are **mixed-model lines** and **mass customisation**, which combine flexibility with scale.

Unit cost model: $C_{unit} = v + F/Q$, with variable cost $v$, fixed cost $F$ and volume $Q$.

### Example
Henry Ford's moving assembly line (1913) cut the time to assemble a Model T chassis from roughly 12.5 hours to about 1.5 hours, and the Model T price fell from $850 in 1908 to about $260 by the mid-1920s. Numerically, with $v = ₹3{,}00{,}000$ per car and $F = ₹600$ crore: at 1,00,000 cars per year, $F/Q = ₹60{,}000$ so $C = ₹3{,}60{,}000$; at 2,00,000 cars, $F/Q = ₹30{,}000$ so $C = ₹3{,}30{,}000$. Volume cut cost by 8.3%.

### In the news
See news box. India's rank (6th) and the 45% auto share in IFR's numbers show mass-production sectors remain the main buyers of industrial robots.

### Interview angle
> [!question] How it is asked
> "Why is Maruti able to price cars so low?" or "What are the risks of a dedicated high-volume line?"

> [!tip] Strong answer includes
> - Economies of scale with a simple $v + F/Q$ cost curve
> - Standardisation, line balancing, takt time
> - Risks: inflexibility, high fixed cost, breakdown propagation
> - Modern fix: mixed-model lines, modular platforms, flexible automation

---

## 4. Continuous Production
> 🟠 Tier 2 · _Tracker hint:_ Flow production, chemical/steel/paper, 24/7 operation

### Definition
**Continuous (process/flow) production** turns bulk, non-discrete materials (liquids, gases, powders, molten metal) through a fixed sequence of connected equipment that runs **24/7**, with products not individually identifiable between stages. Examples: refining, cement, steel, fertiliser, paper, glass, power.

Characteristics: very high volume, near-zero variety, extremely capital-intensive, automated (DCS/SCADA control), highly standardised, long start-up/shut-down (a blast furnace or cracker is not stopped lightly). Economics hinge on **capacity utilisation** because fixed cost dominates. Key metrics: yield, throughput, uptime, energy per tonne, **OEE**. Maintenance is planned in long shutdowns (turnarounds).

Contrast: *discrete* manufacturing (cars, phones) counts distinct units; *process* manufacturing measures by weight/volume and uses recipes or formulas.

### Example
A cement plant: capacity 1,000 t/day, fixed cost ₹60 lakh/day. At 100% utilisation fixed cost per tonne $= 60{,}00{,}000/1000 = ₹6{,}000$. At 80% utilisation (800 t), $= 60{,}00{,}000/800 = ₹7{,}500$, 25% higher. That is why plants chase utilisation and why unplanned stoppages are so costly.

### In the news
See news box. Continuous plants are the strongest case for digital twins and predictive maintenance because one unplanned stop of a 24/7 line costs days of output.

### Interview angle
> [!question] How it is asked
> "How is managing a steel plant different from managing an automobile assembly plant?"

> [!tip] Strong answer includes
> - Process vs discrete: product nature, flow, variety, capital intensity
> - Utilisation and uptime as the central KPIs
> - Planned turnaround maintenance; safety and environmental compliance
> - Where analytics help: yield optimisation, energy, predictive maintenance

---

## 5. Cellular Manufacturing
> 🟠 Tier 2 · _Tracker hint:_ Group technology, U-shaped cells, multi-skilled operators

### Definition
**Cellular manufacturing** groups machines needed to make a *family* of similar parts into a compact **cell**, so a part is completed inside the cell. Families are formed by **group technology (GT)**: parts with similar shape, size or process routing are coded and clustered (for example by **production flow analysis** or a rank-order clustering of a machine-part matrix).

**Benefits:** shorter lead time, less WIP and transport, easier scheduling, quality ownership, faster feedback. **U-shaped cells** place operators inside the U so one person can run several machines, and the cell's **staffing flexes with takt time** (more operators when demand rises). Operators must be **multi-skilled**. Limits: needs sufficient volume per family, duplicates some machines (lower utilisation), and demands cross-training.

### Example
A batch of 50 parts has 4 operations of 3 min each.
- Functional (batch-and-queue) layout: each operation completes all 50 before the batch moves, so lead time $\approx 4 \times 50 \times 3 = 600$ min.
- Cell with one-piece flow: first part exits after $4 \times 3 = 12$ min, then one every 3 min, so batch done in $12 + 49 \times 3 = 159$ min.
Lead time fell about 73%.

### In the news
See news box. Toyota's kaizen AI tooling is aimed at the line and cell level, where multi-skilled workers diagnose and fix problems themselves.

### Interview angle
> [!question] How it is asked
> "A job shop has 6-week lead times. Would you move to cells?" or "What is group technology?"

> [!tip] Strong answer includes
> - Part-family identification (GT, routing similarity) and minimum volume condition
> - Lead-time arithmetic (one-piece flow vs batch-and-queue)
> - U-shape and flexible staffing against takt
> - Costs: machine duplication, cross-training, rebalancing when mix changes

---

## 6. Flexible Manufacturing System (FMS)
> 🟠 Tier 2 · _Tracker hint:_ CNC machines, automated material handling, reconfigurable

### Definition
An **FMS** is a computer-controlled group of **CNC machines**, linked by **automated material handling** (AGVs, conveyors, robots), automated tool changers and a central controller, able to process many part types with near-zero changeover. It fills the gap between the high flexibility of job shops and the high productivity of transfer lines.

Components: (1) workstations (CNC machining centres); (2) automated handling and storage (AGV, pallets, AS/RS); (3) central computer control (scheduling, routing, tool management); (4) operators for loading, maintenance and supervision.

Types of flexibility: **machine** (switch jobs fast), **routing** (alternate paths), **volume** (profitable at varied volumes), **product mix**, **expansion**. Drawbacks: very high capital cost, complex software, tooling and fixtures needed. A **reconfigurable manufacturing system (RMS)** goes further: hardware and software modules can be added or removed as the product family changes.

### Example
Illustrative: a plant machines 6 variants of gearbox housings. With stand-alone CNCs, changeover is about 90 min per variant switch; with an FMS (pallets with fixtures, auto tool change) it is under 5 min, so machines cut metal about 85% of the shift instead of about 55%. Payback is then judged on additional output: 30 percentage points of 8,000 annual hours $= 2{,}400$ more spindle-hours per machine.

### In the news
See news box. Foxconn-style digital twins let a company validate an FMS layout and cell flow virtually before spending on hardware.

### Interview angle
> [!question] How it is asked
> "When is an FMS worth the investment?"

> [!tip] Strong answer includes
> - Components and types of flexibility
> - Justification logic: medium volume, high variety, high part value, short product life
> - Costs and risks: capital, software, skills, single point of failure
> - Comparison with job shop, transfer line and cell

---

## 7. Industry 4.0 Technologies
> 🟠 Tier 2 · _Tracker hint:_ IoT, AI, robotics, AR, 3D printing, digital twin, cloud

### Definition
**Industry 4.0** (the 4th industrial revolution, term from Germany, 2011) is the integration of digital and physical production into connected, data-driven, increasingly autonomous systems. Sequence: 1.0 steam and mechanisation; 2.0 electricity and mass production; 3.0 electronics, PLCs and automation; 4.0 cyber-physical systems.

| Technology | Role in the factory |
|---|---|
| IIoT / sensors | Real-time machine and product data |
| Cloud and edge | Storage, compute, low-latency decisions |
| Big data and AI/ML | Prediction, quality inspection, optimisation |
| Robotics and cobots | Flexible automation |
| AR/VR | Guided work instructions, remote support, training |
| Additive manufacturing | Tooling, spares, complex parts |
| Digital twin and simulation | Virtual testing and planning |
| Cybersecurity, 5G | Safe, connected operation |

Design principles: interoperability, virtualisation, decentralisation, real-time capability, service orientation, modularity. Value comes from use cases (OEE, quality, energy, planning), not from technology adoption in itself. India context: SAMARTH Udyog Bharat 4.0 centres and PLI schemes.

### Example
A packaging plant with 12 lines installs IIoT sensors on filling machines. If OEE rises from 62% to 68% on a plant that produces ₹200 crore of output at 62%, extra output $\approx 200 \times (68/62 - 1) \approx ₹19.4$ crore a year, against a one-time sensor and analytics cost, say ₹3 crore. (Illustrative.)

### In the news
See news box. IFR installs, Toyota's AI, and Foxconn's digital twins show three layers of Industry 4.0: hardware (robots), human-AI problem solving, and virtual planning.

### Interview angle
> [!question] How it is asked
> "How would you take an old plant toward Industry 4.0?" or "Which Industry 4.0 technology gives the best ROI?"

> [!tip] Strong answer includes
> - Start from the business problem (downtime, quality, lead time), not the technology
> - A sequence: digitise and connect first, then analyse, then automate
> - Quick wins (OEE monitoring, e-kanban) versus long projects
> - Data quality, skills, cybersecurity and change management as the real obstacles

---

## 8. Digital Twin
> 🟠 Tier 2 · _Tracker hint:_ Virtual replica; real-time sync, predictive maintenance use cases

### Definition
A **digital twin** is a virtual model of a physical asset, process or system that is **kept in sync with its real counterpart through live data** and used to simulate, predict and optimise. Distinguish: a *model* has no live link; a *shadow* receives data one way; a *twin* exchanges data **both ways** (insights flow back to control the asset).

Levels: **component/asset** (a pump or motor), **process** (a production line), **system** (whole plant), **supply chain** twin (network, inventory, flows). Architecture: sensors → connectivity (IIoT, edge) → data platform → physics-based and/or ML model → visualisation and decision layer → actuation.

Use cases: **predictive maintenance** (estimate remaining useful life), virtual commissioning, layout and throughput what-if tests, energy optimisation, operator training, supply chain scenario testing. Challenges: data quality, model fidelity, integration with MES/ERP, cost, IP security.

### Example
Illustrative: a compressor line loses ₹50,000 per hour when it stops; it had 20 unplanned hours a year, so ₹10 lakh. A twin-based predictive programme that avoids 30% of those hours saves $0.3 \times 20 \times 50{,}000 = ₹3$ lakh a year, which must exceed the cost of sensors and software, so twins pay on high-value or critical assets.

### In the news
> [!news] Foxconn builds factories virtually first (NVIDIA case study, 2025)
> Per NVIDIA's case study, Foxconn validates new facilities (such as one in Houston, Texas) in a digital twin before construction, and claims about **150x faster** AI-driven thermal simulation and a **~50% cut in time-to-revenue** for factory set-up. Treat as vendor-reported. ([NVIDIA](https://www.nvidia.com/en-us/case-studies/foxconn-develops-physical-ai-enabled-smart-factories-with-digital-twins/))

### Interview angle
> [!question] How it is asked
> "What is a digital twin and where would it give value in a manufacturing company?"

> [!tip] Strong answer includes
> - Model vs shadow vs twin (two-way, real-time)
> - One concrete use case with the economics (downtime avoided, commissioning time cut)
> - Prerequisites: sensors, data pipeline, a trusted model
> - Honest limitations: cost, fidelity and data quality; where not to use it

---

## 9. Smart Manufacturing
> 🟠 Tier 2 · _Tracker hint:_ Cyber-physical systems, real-time data, autonomous decisions

### Definition
**Smart manufacturing** uses **cyber-physical systems (CPS)**, real-time data and advanced analytics so that production **senses, decides and adapts with minimal human intervention**. It is the operational outcome of Industry 4.0. It spans the **ISA-95 automation pyramid**: field devices (sensors, actuators) → PLC/SCADA → **MES** (execution) → ERP (planning), now increasingly connected end to end.

Capabilities: self-optimising process parameters, AI vision inspection, dynamic scheduling in response to breakdowns or rush orders, closed-loop quality, track-and-trace, energy management, autonomous material flow (AGV/AMR). Maturity path: connected → visible → transparent (why did it happen) → predictive → adaptive/autonomous. KPIs: OEE, first-pass yield, schedule adherence, energy per unit, lead time, changeover time.

### Example
Machine vision checks 100% of solder joints on a PCB line at 0.5 s per board instead of human sampling of 5%. If 600 defective boards a month previously escaped to customers at ₹800 warranty cost each, escapes cost ₹4.8 lakh a month; reducing escapes by 90% saves ₹4.32 lakh a month ($600 \times 800 \times 0.9$).

### In the news
See news box. Toyota's worker-built ML models are a "smart manufacturing from the bottom up" example: decisions pushed to the people closest to the process.

### Interview angle
> [!question] How it is asked
> "What is smart manufacturing and how does it differ from automation?"

> [!tip] Strong answer includes
> - Automation executes fixed rules; smart manufacturing senses and adapts
> - CPS and the layers MES/ERP integration
> - Concrete use case with benefit estimate
> - Human role: exception handling, governance and skills

---

## 10. Additive Manufacturing (3D Printing)
> 🟠 Tier 2 · _Tracker hint:_ Rapid prototyping, tooling, spare parts, supply chain impact

### Definition
**Additive manufacturing (AM)** builds parts **layer by layer** from a digital (CAD/STL) file, in contrast to subtractive machining or forming. Main processes: FDM (extruded polymer), SLA (resin), SLS/MJF (polymer powder), **SLM/DMLS** (metal powder), binder jetting, DED.

**Economics:** high cost per unit but **no tooling and almost no set-up**, so it wins at low volume and high complexity; cost per part is roughly flat with volume, while conventional (injection moulding, casting) has a big fixed tooling cost. Break-even volume:

$$Q^* = \frac{F_{tool}}{c_{AM} - c_{conv}}$$

**Applications:** rapid prototyping, jigs and fixtures, tooling, customised parts (dental, implants), part consolidation, and **spare parts on demand**.

**Supply chain impact:** digital inventory instead of physical stock, local/distributed production, fewer suppliers and shorter lead times, lower obsolescence; risks include material cost, slow build rates, post-processing, certification and IP.

### Example
GE Aviation's LEAP engine fuel nozzle is 3D printed as one part replacing 20 welded/brazed parts, and is about 25% lighter. Break-even: tooling ₹20 lakh, AM part ₹4,000, conventional part ₹1,500: $Q^* = 20{,}00{,}000/(4{,}000 - 1{,}500) = 800$ units. Below 800 units AM is cheaper overall.

### In the news
See news box. Spare-part twins plus printing are the end of the chain: a digital twin flags wear, and AM produces the replacement near the site.

### Interview angle
> [!question] How it is asked
> "Will 3D printing replace traditional manufacturing? What does it do to supply chains?"

> [!tip] Strong answer includes
> - Where AM wins (low volume, complexity, customisation, spares) and where not (high volume)
> - Break-even logic with tooling cost
> - Supply chain effects: digital inventory, localisation, fewer suppliers
> - Constraints: speed, material cost, certification, post-processing

---

## 11. Automation & Robotics
> 🟠 Tier 2 · _Tracker hint:_ RPA, collaborative robots (cobots), pick-and-place

### Definition
Automation replaces or assists human effort with machines or software. Distinguish:
- **Fixed (hard) automation**: dedicated machinery for high volume (transfer lines).
- **Programmable automation**: reprogrammable equipment for batches (CNC, robots).
- **Flexible automation**: switches products with negligible time (FMS).
- **Industrial robots**: articulated, SCARA, delta (fast **pick-and-place**), Cartesian; usually fenced for safety.
- **Cobots (collaborative robots)**: lower payload and speed, force-limited, working beside people without fences; easy to redeploy (ISO/TS 15066 for safety).
- **AGV/AMR**: autonomous vehicles moving materials (AMRs navigate dynamically).
- **RPA (robotic process automation)**: software bots that automate rule-based office tasks (invoice matching, order entry); not physical robots.

Business case: payback $= \dfrac{\text{Investment}}{\text{Annual savings}}$, including quality, safety and uptime benefits. Human factors: reskilling, redeployment.

### Example
Illustrative: a cobot cell costs ₹25 lakh and replaces repetitive palletising work of 4 operators across shifts costing ₹4 lakh each a year: savings ₹16 lakh a year, payback $25/16 \approx 1.56$ years (about 19 months), before maintenance and programming costs.

### In the news
> [!news] Robots in India: 9,100 installs in 2024, 6th globally (IFR, Sep 2025)
> IFR's World Robotics 2025 puts India's 2024 installations at **9,100 (+7%)** versus **295,000 in China** and 542,000 worldwide, with automotive at 45% of Indian demand: India is a top-six market but a small fraction of China's volume, which frames both the opportunity and the gap. ([IFR](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years))

### Interview angle
> [!question] How it is asked
> "A mid-size manufacturer wants to automate packing. How would you decide?"

> [!tip] Strong answer includes
> - Choose the right type: fixed, programmable, cobot, AMR; match to volume and variety
> - Payback and sensitivity (labour cost, utilisation, quality)
> - Process fixes before automation ("don't automate waste")
> - People impact: safety, reskilling and change management

---

## 12. Industrial IoT (IIoT)
> 🟠 Tier 2 · _Tracker hint:_ Sensors, edge computing, predictive analytics in manufacturing

### Definition
**IIoT** connects industrial machines, sensors and systems to collect and analyse operational data. Layers: **sensors/actuators** (vibration, temperature, current, pressure, vision) → **edge gateways** (pre-process data close to the machine for low latency and bandwidth savings) → **connectivity** (OPC UA, MQTT, 5G, Wi-Fi) → **cloud/data platform** → **analytics/AI** → **applications** (dashboards, alerts, MES, ERP).

Core use cases: **condition monitoring and predictive maintenance**, real-time OEE, energy monitoring, quality prediction, asset tracking, remote operations. Maintenance maturity: reactive → preventive (time-based) → condition-based → predictive.

Useful reliability formulas: availability $A = \dfrac{MTBF}{MTBF + MTTR}$. Challenges: legacy machines (retrofit sensors), interoperability, cybersecurity (IT/OT convergence), data volume, ROI proof.

### Example
A line has MTBF = 100 h and MTTR = 4 h, so $A = 100/104 = 96.2\%$. IIoT alerts allow planned repairs, cutting MTTR to 2 h: $A = 100/102 = 98.0\%$, a gain of 1.8 percentage points of availability. At 6,000 scheduled hours that is about 108 extra productive hours.

### In the news
See news box. Toyota's workers use plant data to build models; the same sensor streams feed digital twins such as Foxconn's.

### Interview angle
> [!question] How it is asked
> "How would IIoT help reduce downtime in a plant?"

> [!tip] Strong answer includes
> - Layers: sensor, edge, connectivity, cloud, analytics
> - Predictive vs preventive maintenance with an availability calculation
> - Retrofit strategy for old machines and OT cybersecurity
> - Start with the highest-downtime assets, prove ROI, then scale

---

## 13. ⭐ Advanced: Product-Process Matrix (Hayes and Wheelwright)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
The **product-process matrix** maps the **product structure** (low volume, one-of-a-kind → high volume, standardised) against the **process structure** (job shop → batch → assembly line → continuous flow). Strategically healthy firms lie on the **diagonal**: job shop with customised product, batch with moderate volume, line with high-volume standard products, continuous flow with commodities.

Off-diagonal positions create problems: a job shop making high-volume products carries excessive cost; a rigid assembly line making customised items has poor service and idle capacity. Moving along the diagonal changes cost structure (fixed cost up, variable cost down), flexibility (down) and cost per unit (down at volume). Matching choices relate to **order-winning criteria** (flexibility vs cost) and the CODP: job shops are make/engineer-to-order, lines are make-to-stock.

Extension: **mass customisation** (e.g. modular design plus postponement) tries to operate off the diagonal profitably.

### Example
A firm sells 200 units a year of an automation system on a flexible job layout. Demand takes off to 20,000 units. Staying in the job shop keeps unit cost high at that volume; moving to a dedicated line cuts unit cost but locks in design and needs capital. The diagonal logic says: change the process as the product matures, and keep a flexible cell for custom variants.

### In the news
See news box. Robots and flexible automation shift the diagonal: cobots make low-volume work cheaper, so firms can sit "below" the old diagonal.

### Interview angle
> [!question] How it is asked
> "Which process type suits product X, and what should we do when volume grows?"

> [!tip] Strong answer includes
> - The diagonal and the cost of being off it
> - Link volume/variety to process type, CODP and order-winning criteria
> - Product life-cycle: process changes as volume rises
> - Role of technology (flexible automation, 3D printing, modularity) in shifting the diagonal

---

## 14. ⭐ Advanced: Assembly Line Balancing
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Line balancing** assigns tasks to workstations so each has roughly equal work content, meeting the **cycle time** $C$ set by demand.

- Takt/cycle time: $C = \dfrac{\text{Available time per period}}{\text{Required output}}$
- Theoretical minimum stations: $N_{min} = \left\lceil \dfrac{\sum t_i}{C} \right\rceil$
- **Balance efficiency** $= \dfrac{\sum t_i}{N \times C}$ and balance delay $= 1 - \text{efficiency}$
- Heuristic (**Ranked positional weight**, or longest-task-time): assign tasks in order of precedence, filling each station up to $C$.

The **bottleneck station** sets line output; unbalanced lines accumulate WIP before slow stations and starve downstream ones. Mixed-model lines use weighted average times. Link: [[007 Lean Manufacturing]] (takt time, heijunka).

### Example
Total task time $\sum t_i = 54$ s; demand requires $C = 12$ s (for example 28,800 s per day / 2,400 units). $N_{min} = \lceil 54/12 \rceil = \lceil 4.5 \rceil = 5$ stations. Suppose a feasible assignment uses 5 stations: efficiency $= 54/(5 \times 12) = 90\%$. If precedence forced 6 stations: $54/(6 \times 12) = 75\%$.

### In the news
See news box. Cobots and AMRs are used to rebalance lines quickly when product mix or demand changes, which static lines cannot do.

### Interview angle
> [!question] How it is asked
> "Output of an assembly line is stuck at 80% of target. How would you analyse it?"

> [!tip] Strong answer includes
> - Compute takt/cycle time; find the bottleneck station by task time per station
> - $N_{min}$ and balance efficiency calculation
> - Levers: rebalance tasks, split or parallelise the bottleneck, reduce task time, add buffers, reduce stoppages
> - Check variability (breakdowns, quality) and not only averages

---
## 🔗 Go deeper: expansion notes
- [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity|Product Design & Supply Chain - DFSC, Postponement & Complexity]]
- [[131 Automotive Supply Chain - JIT, Tiers & EVs|Automotive Supply Chain - JIT, Tiers & EVs]]
- [[134 Electronics & Semiconductor Supply Chain|Electronics & Semiconductor Supply Chain]]
