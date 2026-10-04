---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP QM & PM"
tier: Tier 2
roles: Operations
status: complete
subtopics: 9
---
# SAP QM & PM

⬅ [[083 SAP WM-EWM — Warehouse]] · [[_Index - SAP ERP|SAP ERP]] · [[085 SAP Reporting & Analytics]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. QM Integration]]
2. [[#2. Inspection Lot]]
3. [[#3. Control Charts in QM]]
4. [[#4. Calibration (PM-QM)]]
5. [[#5. Plant Maintenance (PM)]]
6. [[#6. PM Order Types]]
7. [[#7. MTBF/MTTR Tracking in SAP]]
8. [[#8. TPM in SAP PM Context]]
9. [[#9. ⭐ Advanced: Condition-Based and Predictive Maintenance Strategy (RCM and FMEA)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Predictive maintenance moves from pilot to plant floor
> **JSW Steel (article dated Dec 2025).** An iFactory case-study blog reports that JSW Steel's AI-based predictive maintenance programme (2019–2024) monitors **2,900+ assets across 10 plants**, with about **85% prediction accuracy**, and removed roughly **25,000 hours of unplanned downtime a year** (from a baseline of 32,000+ hours), worth **₹200 crore+** in avoided production losses. These are vendor-published figures, not audited company results, so quote them as "reported". ([iFactory](https://ifactoryapp.com/blog/jsw-steel-ai-predictive-maintenance-case-study))
>
> **SAP's analytics direction (Feb 2025).** SAP launched Business Data Cloud on 13 Feb 2025 (general availability planned April 2025), bundling Datasphere, SAP Analytics Cloud, BW and managed Databricks. Machine and sensor data landing in such platforms is what feeds condition-based triggers for maintenance. ([SAP Community FAQ](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-business-data-cloud-faqs/ba-p/14022781))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. QM Integration
> 🟠 Tier 2 · _Tracker hint:_ QM integrates with MM (GR inspection), PP (in-process), SD (customer returns)

### Definition
**SAP QM (Quality Management)** is not a stand-alone module: it hooks into the logistics flow so inspections are triggered by business events.

| Module | Trigger | Inspection type (typical) |
|---|---|---|
| MM | Goods receipt against a PO (MIGO) | 01 Goods receipt inspection |
| PP | Goods receipt from a production order (in-process inspections are configured separately) | 04 Goods receipt from production order (confirm codes in customising; see [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]]) |
| SD | Delivery or customer return | 10 Inspection for delivery |
| PM | Equipment / test equipment | Calibration and equipment inspection |

Set-up needs: the **QM view** of the material master (inspection type active, inspection setup), an **inspection plan** (QP01) with task list and master inspection characteristics (QS21), and a **QM control key** for vendors (QI01 quality info record). Stock moves between **unrestricted, quality inspection (QI) and blocked** stock depending on the result.

### Example
A pharma plant in Baddi buys an API. Posting the GR in MIGO puts the batch in quality-inspection stock; QM creates a lot, the lab records assay and moisture results, and the usage decision moves stock to unrestricted or to blocked. Production cannot consume it until released.

### In the news
See news box. Sensor and lab data feeding QM and PM from one data platform is the logical next step of this integration.

### Interview angle
> [!question] How it is asked
> "How does quality management fit into the procure-to-pay and make-to-stock flows in SAP?"

> [!tip] Strong answer includes
> - The three integration points (GR, in-process, delivery/return) with the stock-type change
> - Master data prerequisites (QM view, inspection plan, characteristics)
> - How a rejected lot blocks stock and triggers a vendor complaint
> - Link to vendor rating and supplier quality KPIs

---

## 2. Inspection Lot
> 🟠 Tier 2 · _Tracker hint:_ Automatically created on GR; results recording; usage decision (accept/reject)

### Definition
An **inspection lot** is the unit of work that says "inspect this quantity of this material against this plan". Life cycle:
1. **Creation**: automatic on a trigger such as GR (inspection type 01), or manual with QA01.
2. **Sample determination**: sample size from sampling procedure (fixed, 100%, AQL-based).
3. **Results recording**: QE01 (by operation), QE11 (by characteristic); accepts/rejects each characteristic, supports defect recording.
4. **Usage decision (UD)**: QA11 / QVM; the final accept or reject with a **UD code** (A accepted, R rejected); it triggers **stock posting** from QI stock to unrestricted, blocked or scrap and can create a quality notification.

Inspection lot status controls what can follow: results must be complete before the UD.

### Example
A GR of 10,000 bearings creates a lot with sample size 80 (from an AQL plan). Two are out of tolerance; the acceptance number is 3, so the lot is accepted and QA11 posts all 10,000 to unrestricted stock. If 4 had failed the UD would be "R" and stock would be returned to the vendor.

### In the news
See news box. Automated capture of measurements (instruments sending data to results recording) removes manual entry errors in this step.

### Interview angle
> [!question] How it is asked
> "Walk me through what happens in SAP from goods receipt of a raw material to its release for production."

> [!tip] Strong answer includes
> - GR → lot creation → sample → results → UD → stock posting, in order
> - Distinguish the stock types (QI, unrestricted, blocked)
> - Mention sampling plans/AQL and the acceptance number
> - What follows a reject: notification, return delivery, vendor score

---

## 3. Control Charts in QM
> 🟠 Tier 2 · _Tracker hint:_ Statistical process control; quality notifications; defect recording

### Definition
SAP QM supports **statistical process control (SPC)**: results recorded against a characteristic can be plotted on **control charts** (X-bar/R, X-bar/s, individual-moving range, attribute charts such as p and c) with control limits and rules for out-of-control signals.

For an X-bar chart with subgroup size $n$: 
$$UCL = \bar{\bar{x}} + A_2\bar{R}, \qquad LCL = \bar{\bar{x}} - A_2\bar{R}$$
(for $n=5$, $A_2 = 0.577$). Points outside limits, runs of 7 on one side, or trends signal assignable causes.

**Defects** are recorded per characteristic during results recording (defect class, code), and a **quality notification** (QM01; types such as Q1 customer complaint, Q2 vendor complaint, Q3 internal problem) tracks root cause, tasks and corrective action. See [[086 Descriptive Statistics]] for the underlying mean/spread ideas.

### Example
A shaft diameter has target 25.00 mm. Over 20 subgroups of 5: $\bar{\bar{x}}=25.002$, $\bar{R}=0.020$. UCL = 25.002 + 0.577×0.020 = **25.0135**; LCL = 25.002 − 0.0115 = **24.9905**. A subgroup mean of 25.020 is outside; a Q3 notification is raised and the tool is checked.

### In the news
See news box. AI-driven monitoring extends the SPC idea from sampled measurements to continuous sensor streams.

### Interview angle
> [!question] How it is asked
> "How would you detect that a process is drifting before it produces scrap?"

> [!tip] Strong answer includes
> - Control limits are from the process (±3σ), not from the customer's spec limits
> - Common vs special cause variation
> - SAP route: results recording feeds control chart, signal raises a notification
> - Capability indices (Cp, Cpk) as the next step

---

## 4. Calibration (PM-QM)
> 🟠 Tier 2 · _Tracker hint:_ Test equipment management; calibration orders; due date monitoring

### Definition
Measuring instruments (gauges, scales, thermometers) are **production resources/tools or equipment** whose accuracy must be verified at intervals. SAP combines PM and QM:
- The instrument is a **PM equipment master** (IE01) marked as test equipment, with a **maintenance plan** (IP01) set to calibration cycle (for example every 6 months).
- When due, scheduling (IP10) generates a **calibration inspection lot** (QM) and a maintenance order.
- The inspector records measured values against reference standards; the **usage decision** can **lock** the instrument or set a new due date.
- A **due-date monitoring** list shows overdue instruments.

Regulators (ISO 9001, ISO/IEC 17025, GMP) require traceable calibration records.

### Example
A torque wrench in an automotive plant is on a 6-month cycle. Calibration shows 4% error against a 2% tolerance; the UD rejects it, the wrench is blocked, and a notification triggers a review of all assemblies built since the last good calibration.

### In the news
See news box. Predictive maintenance does not remove calibration; accurate sensors are a precondition for any condition-based trigger.

### Interview angle
> [!question] How it is asked
> "How do you make sure measurement instruments on the shop floor can be trusted?"

> [!tip] Strong answer includes
> - Calibration plan per instrument, traceable to a standard
> - System-driven due dates, not memory
> - What to do on failure: block, back-trace affected output
> - Link to audit readiness (ISO/GMP)

---

## 5. Plant Maintenance (PM)
> 🟠 Tier 2 · _Tracker hint:_ Functional location → Equipment → Maintenance Plan → Orders

### Definition
**SAP PM** manages the upkeep of technical assets. Core objects:
- **Functional location** (IL01): where something is installed, in a hierarchy (Plant > Line > Station). Persists when equipment is swapped.
- **Equipment** (IE01): the physical item (pump, motor) with serial number, history, warranty; installed at a functional location.
- **Bill of material** for spare parts; **task list** (IA05 general maintenance task list) describing steps.
- **Maintenance plan** (IP01): time-based, performance-based (counter, e.g. running hours) or condition-based schedule; scheduled with IP10.
- **Notification** (IW21) and **maintenance order** (IW31); **confirmation** (IW41); technical completion; settlement to cost centre.

### Example
A packaging line has a functional location PL1-LINE2-FILLER. Equipment "Filler pump P-204" is installed there. A maintenance plan generates a lubrication order every 500 running hours; when the pump is replaced, the history stays with the location while the equipment history moves with the pump.

### In the news
See news box. Asset-heavy firms (steel, power, auto) are using the PM master data structure as the backbone to which sensor data is attached.

### Interview angle
> [!question] How it is asked
> "What is the difference between a functional location and equipment in SAP PM?"

> [!tip] Strong answer includes
> - Location = place/function, equipment = physical object that moves
> - The chain: plan → call → order → confirmation → settlement
> - Three plan types (time, counter, condition)
> - Why clean master data drives MTBF and cost analysis

---

## 6. PM Order Types
> 🟠 Tier 2 · _Tracker hint:_ Preventive, Corrective, Investment; notifications → work orders → confirmations

### Definition
Order types are configured per company, but the standard set is: **PM01** (maintenance order, usually corrective or general), **PM02** (planned/preventive order from a maintenance plan), **PM03** (refurbishment of spare parts). Maintenance types in practice:

| Type | Trigger | Example |
|---|---|---|
| Corrective / breakdown | Failure, malfunction notification (M2) | Motor burnt out |
| Preventive | Maintenance plan call | Monthly lubrication |
| Predictive / condition-based | Measurement document or counter reaching a limit | Vibration above threshold |
| Investment / capital | Internal order or WBS-linked | New conveyor |

Flow: **notification** (M1 request, M2 malfunction, M3 activity report) → **order** with operations, components, planned cost → release → **time confirmation** → **technical completion** → cost settlement.

### Example
Operator reports a leaking hydraulic press (M2 notification). Planner creates order with 2 operations and a seal kit reservation; technician confirms 3 h and 1 kit; order is completed and settled, so the actual cost (₹ labour plus ₹ material) appears under the machine's cost centre.

### In the news
See news box. Condition-based orders are the form of PM order that sensor analytics creates automatically.

### Interview angle
> [!question] How it is asked
> "What is the difference between preventive and corrective maintenance, and how does SAP handle each?"

> [!tip] Strong answer includes
> - Notification is the request, order is the execution document
> - Plan-generated vs failure-generated orders
> - Cost capture and settlement
> - The shift target: reduce corrective share, raise planned maintenance %

---

## 7. MTBF/MTTR Tracking in SAP
> 🟠 Tier 2 · _Tracker hint:_ Breakdown notifications; system availability reports

### Definition
$$MTBF = \frac{\text{Total operating time}}{\text{Number of failures}}, \quad MTTR = \frac{\text{Total repair time}}{\text{Number of repairs}}$$
$$\text{Availability} = \frac{MTBF}{MTBF + MTTR}$$

SAP captures the inputs on the **malfunction notification (M2)**: breakdown indicator, **malfunction start and end date/time**, and the object (equipment or functional location). Notification lists (IW28/IW29) and the Plant Maintenance Information System (a Logistics Information System, LIS, area) summarise failure counts and downtimes by equipment, damage code and cause code. Accuracy depends on discipline in entering start/end times and codes.

### Example
A conveyor ran 720 hours in a month with 4 breakdowns totalling 12 hours of repair. MTBF = 720/4 = **180 h** (using total operating time as given), MTTR = 12/4 = **3 h**, availability = 180/183 ≈ **98.4%**.

### In the news
See news box. JSW Steel's reported downtime cut is, in these terms, a higher MTBF through earlier fault detection.

### Interview angle
> [!question] How it is asked
> "How would you reduce downtime on a critical machine, and how would you measure the improvement?"

> [!tip] Strong answer includes
> - Formulas for MTBF, MTTR and availability, and what each reflects (reliability vs maintainability)
> - Data source in SAP and data-quality caveats
> - Pareto of failure causes to prioritise
> - Levers: preventive plans, spare parts, training (lower MTTR), design-out (higher MTBF)

---

## 8. TPM in SAP PM Context
> 🟠 Tier 2 · _Tracker hint:_ Maintenance plans; task lists; predictive maintenance triggers from IoT sensors

### Definition
**Total Productive Maintenance (TPM)** aims at zero breakdowns through operator-led care, planned maintenance and continuous improvement; its metric is **OEE** = Availability × Performance × Quality. Eight pillars include autonomous maintenance, planned maintenance, focused improvement, quality maintenance and training.

SAP PM supports TPM mechanically: **task lists** standardise operator checks and routines, **maintenance plans** schedule them, **measuring points and documents** record readings (temperature, vibration) and can trigger notifications when limits are exceeded. With **IoT** (SAP Asset Performance Management / predictive asset insights, or third-party platforms) sensor streams and ML models generate **predictive alerts** that create notifications in PM automatically.

### Example
OEE: availability 90%, performance 95%, quality 98% gives $0.90 \times 0.95 \times 0.98 = 0.838$, i.e. **83.8%**. A vibration threshold on a motor bearing raises an M2 notification before failure; the order is planned for the next scheduled stop instead of a breakdown.

### In the news
See news box. This is exactly the pattern in the JSW Steel report: sensor-based prediction, then maintenance orders ahead of failure.

### Interview angle
> [!question] How it is asked
> "What is TPM and how can ERP data support it?" or "How would you improve OEE on a packaging line?"

> [!tip] Strong answer includes
> - OEE decomposition and the six big losses
> - Operator autonomous maintenance plus planned maintenance
> - ERP/IoT role: standard task lists, measurement documents, alerts
> - Start with the bottleneck machine and measure before/after

---

## 9. ⭐ Advanced: Condition-Based and Predictive Maintenance Strategy (RCM and FMEA)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Choosing a maintenance strategy per asset is a risk decision. **FMEA** scores each failure mode on Severity (S), Occurrence (O) and Detection (D), 1–10 each, and ranks by **RPN = S × O × D**. **Reliability-Centred Maintenance (RCM)** then picks: run-to-failure (low criticality), time-based preventive, condition-based, or redesign.

**Condition-based** uses a measured parameter crossing a threshold; **predictive** forecasts remaining useful life. Failure patterns: only a minority of failures are age-related, so blanket time-based replacement often wastes good parts. Economic rule: preventive replacement pays when the cost of failure is much higher than planned replacement and failure risk rises with age.

In SAP, the criticality (ABC indicator) sits on equipment, strategies are modelled as maintenance strategies and plans, and measurement documents drive condition triggers.

### Example
Pump A: S=8, O=4, D=5 gives RPN 160; Pump B: S=5, O=3, D=2 gives 30. Put A on a condition-based vibration plan, B on run-to-failure with a spare on the shelf.

### In the news
See news box. Reported predictive programmes (JSW Steel) rest on first ranking which assets deserve sensors.

### Interview angle
> [!question] How it is asked
> "You have 500 machines and a limited maintenance budget. Where do you start?"

> [!tip] Strong answer includes
> - Criticality ranking (ABC/RPN) before technology
> - Match strategy to failure pattern and cost of failure
> - Pilot, measure MTBF/availability gain, then scale
> - Data readiness: clean equipment master, failure codes

---

---
## 🔗 Go deeper: expansion notes
- [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications|SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]]
- [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies|SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]]
