---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications

⬅ [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]] · [[_Index - SAP ERP|SAP ERP]] · [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. QM in the SAP Landscape and the Master-Data Map]]
2. [[#2. Material Master QM View and Inspection Setup]]
3. [[#3. Master Inspection Characteristics, Catalogs and Selected Sets]]
4. [[#4. Inspection Plans, Inspection Types and Lot Triggers]]
5. [[#5. Sampling Procedures and Dynamic Modification (AQL Worked)]]
6. [[#6. Inspection Lot Lifecycle and Results Recording]]
7. [[#7. Usage Decision, Stock Posting and Quality Score]]
8. [[#8. QM in Procurement: Info Records, Certificates, Source Inspection]]
9. [[#9. Quality Notifications and Corrective Actions]]
10. [[#10. Quality Costs and Reporting]]
11. [[#11. SPC, Control Charts and Process Capability]]
12. [[#12. Integration with MM, PP, SD, WM, PM and S/4HANA]]
13. [[#13. Worked Inbound Inspection Flow, End to End]]
14. [[#14. ⭐ Advanced: Digital Quality, Supplier Data Exchange and Predictive Quality]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Quality data is leaving the plant and moving across the supply chain
> **Catena-X and SAP target recall precision (SAP News Center, 27 Mar 2025).** SAP describes a Catena-X use case in which bilateral exchange of field data (from carmakers) and production data (from suppliers) narrowed a recall from **1.4 million vehicles to 14**. The article cites German carmakers reserving **€1.4–1.8 billion a year** for recalls, errors detected about **4 months earlier**, and roughly **200 Catena-X members** (up from 28 at the 2021 start); the network went live in **October 2023**. The page names SAP Quality Management as the reference capability and does not detail the exact product module. ([SAP News Center](https://news.sap.com/2025/03/catena-x-sap-efficient-quality-management-automotive-industry/))
>
> **ECC deadline reshapes where QM runs (SAP, 4 Feb 2025; e3mag, 23 Oct 2025).** On-premise ECC (where most QM implementations live) has mainstream maintenance to end-2027 and extended maintenance to end-2030; SAP's paid transition option (buy from 2028, use 2031–2033) is a cloud subscription, not a maintenance prolongation. ([SAP News Center](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/); [e3mag](https://e3mag.com/en/deadline-extension-for-ecc-6-0-until-2033/))
>
> Sub-topics that say **"See news box"** reuse these items. Foundations in [[084 SAP QM & PM]] and quality tools in [[008 Six Sigma & Quality Tools]].

---
## 1. QM in the SAP Landscape and the Master-Data Map
> 🟠 Tier 2 · _Key points:_ Planning, inspection, notifications; master data chain

### Definition
**SAP QM** supports the quality cycle in three parts:
1. **Quality planning:** define what to inspect and how (master inspection characteristics, inspection plans, sampling procedures, catalogs).
2. **Quality inspection:** inspection lots, results recording, usage decision, stock posting.
3. **Quality control and improvement:** quality notifications, corrective actions, statistical process control, quality costs, certificates, vendor evaluation.

The master-data chain that must exist before an inspection can run:

| Object | Role | Typical T-code |
|---|---|---|
| Material master, QM view | Activates inspection types, procurement key | `MM01`/`MM02` |
| Master inspection characteristic (MIC) | Reusable definition of what is measured | `QS21` |
| Catalogs, code groups, selected sets | Defect types, causes, valuation codes | Quality Planning > Basic Data > Catalog |
| Sampling procedure / scheme / dynamic modification rule | How many to inspect | `QDV1`, `QDP1`, `QDR1` |
| Inspection plan (task list) | Operations and characteristics per material | `QP01` |
| QM info record / control key (procurement) | Vendor-material QM agreement | `QI01` |

Ties to quality theory in [[011 Quality Management (TQM)]] and [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]].

### Example
A tyre plant buys steel bead wire. QM master data: MIC "wire diameter" (quantitative, 1.60 mm ± 0.02), MIC "surface defects" (qualitative, with a defect catalog); an inspection plan with these two characteristics; sampling by AQL; QM view active (inspection type 01 for goods receipt); and a QM info record with the vendor allowing 'inspection at goods receipt with skip-lot'. Without any one of these the lot cannot be created or processed.

### In the news
See news box. Catena-X-type data exchange requires the master data above to be clean: a characteristic that means different things in two plants cannot be compared across suppliers.

### Interview angle
> [!question] How it is asked
> "What master data do you need to set up QM for a purchased raw material?"

> [!tip] Strong answer includes
> - The chain: material QM view, MIC, inspection plan, sampling, QM info record
> - What each does and what breaks if missing
> - Reuse of MICs across plans, plants and suppliers
> - A concrete material and characteristics

---
## 2. Material Master QM View and Inspection Setup
> 🟠 Tier 2 · _Key points:_ Inspection type active, QM procurement, control key, post to inspection stock

### Definition
In the material master (QM view, plant level) the user:
- **Activates one or more inspection types** (with the **Active** flag; options include **Preferred inspection type** and **Post to inspection stock**). Stock posting to inspection stock is what puts received goods in QI stock instead of unrestricted.
- Sets **QM procurement active** (so QM data of vendors and info records is checked in purchasing) and a **QM control key** (for example whether a vendor must have a QM system, whether a certificate is required, or whether the vendor is blocked for QM reasons).
- Optionally assigns a **certificate type**, target QM system, and **inspection setup** (automatic assignment of the plan, sampling procedure, and whether lot creation is manual or automatic).
- Material type and the **QM-relevant** settings in customising (QM integration per movement) decide whether the QM view is offered at all.

Warning: if "post to inspection stock" is not set, an inspection lot may be created but stock is already unrestricted. If the inspection type is active but no plan exists, the lot is created without characteristics (a manual lot or a plan is needed).

### Example
For ROH material "Bead wire 1.6" in plant 1100: inspection type 01 Active, Post to inspection stock ticked, QM procurement active, QM control key "Vendor needs QM system and certificate". The first GR of 20 tonnes posts into QI stock; the lot is created automatically; because the vendor is flagged in the info record as "blocked", PO creation in `ME21N` would have raised a message earlier, at procurement.

### In the news
See news box. Moving from ECC to S/4HANA does not remove these master-data settings, but the material master is edited through Fiori or `MM02` and checked through migration cockpit objects; see [[200 SAP S-4HANA Migration, Data Migration & Testing]].

### Interview angle
> [!question] How it is asked
> "A goods receipt did not create an inspection lot. What do you check?"

> [!tip] Strong answer includes
> - QM view: inspection type active for the plant and origin (GR)
> - QM procurement/control key; movement type relevant for QM
> - Inspection plan assignment, "lot creation" settings, deletion flags
> - Check material document message and the lot list `QA32`

---
## 3. Master Inspection Characteristics, Catalogs and Selected Sets
> 🟠 Tier 2 · _Key points:_ MIC, quantitative vs qualitative, code groups, selected sets, plant-level copies

### Definition
A **master inspection characteristic (MIC)** (`QS21` create) defines one quality attribute once so that many plans can use it. Fields:
- **Quantitative** (measured value: target, upper and lower specification limits, decimals, unit) vs **qualitative** (attribute: accepted/rejected or code from a catalog).
- **Control indicators:** required characteristic, results recording (single, summarised, classed), **sampling procedure** assignment, **inspection scope** (mandatory, optional), **automatic valuation** (system evaluates against limits), **defects recording** (a defect can be recorded when rejected), **long-term inspection data**, and **control chart** type.
- **Versions and statuses** (created, released, locked) and **validity** dates.
- **Plant-specific MICs** vs **global MICs** with plant copies.

**Catalogs** store coded lists (defect types, defect locations, usage decision codes, characteristic attributes). A **code group** is a set of codes; a **selected set** is a plant-specific subset of one or more code groups released for use in a given context (for example the UD codes allowed for goods receipt inspection). Codes may carry a **quality score** and a **valuation** (accept or reject), which is how a qualitative result is valued.

### Example
MIC "Bead wire diameter": quantitative, target 1.60 mm, lower 1.58, upper 1.62, unit mm, 3 decimals, automatic valuation on, long-term data on. MIC "Visual surface": qualitative using a code group "Defects" with codes 01 rust (reject), 02 scratch minor (accept with remark), 03 oil film (reject). The selected set for plant 1100 allows only these three codes.

### In the news
See news box. For cross-company comparisons, controlled catalogs and common MIC definitions make Catena-X type exchange meaningful because the same code means the same defect.

### Interview angle
> [!question] How it is asked
> "What is a master inspection characteristic and why do we use it instead of defining characteristics in each plan?"

> [!tip] Strong answer includes
> - Reuse and consistency; change once, apply everywhere (with versioning)
> - Quantitative vs qualitative and how each is valued
> - Catalog, code group and selected set purpose
> - Control indicators that affect results recording and SPC

---
## 4. Inspection Plans, Inspection Types and Lot Triggers
> 🟠 Tier 2 · _Key points:_ Task list with operations, inspection types and origins, triggers

### Definition
An **inspection plan** (`QP01` create, `QP02` change, `QP03` display) is a task list (type Q) with a **header** (plan group, group counter, usage 5 for QM, status, valid-from), **operations** (work centre or inspection point), a **material assignment** (`MAPL`), and **characteristics** on each operation (MICs or plan-specific ones), each with its own sampling procedure and control data. In-process inspections can also be integrated into the production **routing** (inspection characteristics on operations).

**Inspection type** (set in the QM view) is tied to the **inspection lot origin**, which is the business event that creates the lot. Commonly used types and triggers:

| Typical type | Trigger | Lot created by |
|---|---|---|
| 01 | Goods receipt from purchase order | `MIGO` 101 |
| 04 | Goods receipt from production order (final inspection) | Production order GR / confirmation |
| 10 | Delivery to customer (SD) | Delivery creation or PGI |
| Stock/recurring | Re-testing of stock or batches (shelf-life, storage ageing) | Recurring inspection or transfer posting |
| In-process | Production operation completed (inspection point or operation result) | Production order release (lot per order) |

The exact numbering and extra origins (including stock-transfer-related types, shown as 03 or 08 in some default lists) come from customising; confirm in the inspection type configuration of the system you work on. Manual lots use `QA01`, lots list `QA32`, display `QA03`. Plan determination uses material, vendor or customer and the plan usage.

### Example
For ROH "Bead wire 1.6": Inspection plan group "BW-01" with operation 0010 "Incoming inspection": characteristic 1 diameter (sample size per AQL), characteristic 2 surface (visual), characteristic 3 tensile strength (destructive, sample 3, destructive samples are not returned to stock). GR of 5 batches creates one lot per batch (batch management) and posts quantities to QI stock.

### In the news
See news box. Plans written for ECC are migrated as task lists; custom QM reports reading `QALS` directly should be tested after conversion.

### Interview angle
> [!question] How it is asked
> "How does SAP decide which plan to use for an inspection lot, and what triggers a lot?"

> [!tip] Strong answer includes
> - Inspection type and lot origin as trigger, material-plan assignment, usage 5
> - Operations and characteristics structure
> - In-process inspection via routing vs separate QM plan
> - Fall-back when no plan is found (manual lot or default characteristics)

---
## 5. Sampling Procedures and Dynamic Modification (AQL Worked)
> 🟠 Tier 2 · _Key points:_ Sampling type, scheme, acceptance number, skip lot, OC curve

### Definition
A **sampling procedure** (`QDV1`) determines how many units to test per characteristic and when to accept the lot. Parts:
- **Sampling type:** fixed sample size, percentage, 100% inspection, **sampling scheme** (table lookup by lot size and AQL), or **inspection points**.
- **Valuation mode:** attributes ("number of defectives") with **acceptance number** (c) and rejection number; variables (mean and spread); manual.
- **Sampling scheme** (`QDP1`): lot size ranges mapped to sample size and accept/reject numbers for an inspection level and AQL, typically adapted from ISO 2859-1 style tables.
- **Dynamic modification rule** (`QDR1`): changes inspection stringency based on history, such as **normal, reduced, tightened** or **skip-lot** (inspect every n-th lot) after a run of accepted lots, and back to tightened after rejects. A quality level is kept per material, vendor and characteristic.
- **Inspection scope and inspection stage** link to the rule so a good vendor is inspected less.

Probability of accepting a lot with fraction defective $p$ for a plan $(n, c)$:
$$P_a(p) = \sum_{k=0}^{c} \binom{n}{k} p^k (1-p)^{n-k}$$
This is the operating characteristic (OC) curve; see [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]] and [[091 Statistical Quality Control (SQC)]].

### Example
Plan A: sample $n=80$, acceptance number $c=2$. Computed acceptance probabilities: $p=0.5\%$: 99.2%; $p=1\%$: 95.3%; $p=2\%$: 78.4%; $p=3\%$: 56.8%; $p=5\%$: 23.1%. Plan B: $n=200$, $c=5$: 1%: 98.4%; 2%: 78.7%; 3%: 44.3%; 5%: 6.2%. Both plans accept a 2% defective lot about 78% of the time, but Plan B is far tougher on 3% to 5% defective lots (44% and 6% acceptance versus 57% and 23%), at 2.5 times the inspection volume. Dynamic modification starts a new vendor on normal; after, say, 5 accepted lots in a row, a rule moves to reduced sampling, and a reject moves back to tightened.

### In the news
See news box. Earlier detection (about four months in the Catena-X example) comes from exchanging data upstream, which complements, but does not replace, incoming sampling.

### Interview angle
> [!question] How it is asked
> "What is a dynamic modification rule and when would you use skip-lot inspection?"

> [!tip] Strong answer includes
> - Sampling type, scheme, acceptance and rejection numbers
> - OC curve intuition: producer's and consumer's risk
> - Rules for normal, reduced, tightened and skip-lot with evidence (quality score history)
> - Do not skip for critical or safety characteristics

---
## 6. Inspection Lot Lifecycle and Results Recording
> 🟠 Tier 2 · _Key points:_ Lot statuses, results recording, characteristic valuation, defects, inspection points

### Definition
**Lifecycle:** **created** → **released** → **results recorded** (possibly in parts) → **usage decision made** → **stock posted** → closed. Key activities:
- **Results recording:** `QE51N` worklist (by inspection lot or operation, preferred), `QE01` (by lot/operation), `QE11` (by characteristic across lots). For **quantitative** characteristics the system calculates mean, standard deviation, and checks limits; for **qualitative** characteristics the inspector picks codes.
- **Valuation:** each characteristic is accepted/rejected automatically (by limits) or manually; the operation and lot valuation derive from them.
- **Defects recording:** record defect type, location and quantity; creates a defect record and can trigger a **quality notification** immediately.
- **Inspection points** for continuous production (record by time or by container) and **long-term characteristics** (monitored over time).
- **Sample management:** physical sample drawing and lab tracking; and **QM interfaces** to lab instruments and LIMS.
- **Skipping and re-inspection:** lots with skip rules need only a UD; a rejected lot can be re-inspected (repeat inspection).

Lot statuses block the UD until all required characteristics are complete.

### Example
Lot for 5,000 bearings: sample 125, 3 characteristics. In `QE51N` the inspector keys 125 diameter readings (mean 12.003 mm, within 12.000 ± 0.015), visually accepts the surface, finds 2 defective pieces on the noise test; defect code 14 "noise" recorded twice, which automatically accepts under acceptance number 3. The lot is ready for the UD.

### In the news
See news box. Automatic capture of measurements via instrument interfaces replaces manual keying and supports the earlier detection in the Catena-X case.

### Interview angle
> [!question] How it is asked
> "Describe how results are recorded and valued in SAP QM, including defects."

> [!tip] Strong answer includes
> - Worklist recording; quantitative vs qualitative valuation
> - Automatic vs manual valuation and defect recording
> - Statuses and prerequisites for UD
> - Instrument interfaces and sample management for labs

---
## 7. Usage Decision, Stock Posting and Quality Score
> 🟠 Tier 2 · _Key points:_ UD codes, QI to unrestricted/blocked/scrap, quality score, follow-up actions

### Definition
The **usage decision (UD)** (`QA11`, change `QA12`, display `QA13`) records the final decision for the lot using a **UD code** from the selected set (for example A accept, R reject, A with remarks). Effects:
- **Stock posting** from inspection stock to **unrestricted** (movement 321), **blocked**, **scrap** (551), **returned to vendor** (122 via return), or partial distribution, with quantities per category. For batch-managed items the **batch status** can be changed.
- **Quality score** (0–100 per UD code or lot) stored for **vendor evaluation** and reporting.
- **Follow-up actions** configured per UD code: create a **quality notification**, set a **notification type**, trigger a **batch status change**, **inspection lot lock**, or **inventory posting**, and (in procurement) update the **quality level** used by dynamic modification.
- **Automatic UD:** if all characteristics are accepted and the setup allows, the system makes the UD automatically (via an **automatic UD** selection) so that routine good lots do not wait for a human.

### Example
Lot 5,000 pieces, 2 defects found: UD "A" accepts the lot and posts 5,000 from QI to unrestricted (321); the quality score is 100 for an accepted lot or lower if remarks are entered. In another lot, 6 defects exceed acceptance number 3: UD "R" with follow-up creating a Q2 notification, and 5,000 are posted to blocked stock pending return; later 122 returns them. The vendor score for that lot is 0.

### In the news
See news box. Where inspection data is shared with suppliers upstream, the rejection and score history becomes input to supplier performance reviews.

### Interview angle
> [!question] How it is asked
> "What happens to stock after a usage decision, and what happens if only part of the lot is acceptable?"

> [!tip] Strong answer includes
> - Stock posting distribution (unrestricted, blocked, scrap, return)
> - Quality score and vendor evaluation link
> - Follow-up actions: notification, batch status
> - Auto-UD and exceptions for critical materials

---
## 8. QM in Procurement: Info Records, Certificates, Source Inspection
> 🟠 Tier 2 · _Key points:_ QM procurement key, QM info record, certificates, quality agreements, vendor evaluation

### Definition
Quality is checked before and during procurement:
- **QM info record** (`QI01`): per vendor-material-plant. States whether the vendor is **released for supply**, the **inspection control** (for example skip inspection, inspect only for certificate), the **required certificate**, **quality assurance agreement** reference, and the **external release** (for example a block pending audit). Blocking a source prevents POs.
- **QM control key** (material master): rules for vendor QM system, certificates, and technical delivery terms.
- **Quality certificates** (inspection certificates such as 3.1 mill certificates, certificates of analysis): required at GR; the lot can be released based on the vendor certificate where a **certificate-based** inspection is agreed.
- **Source inspection**: inspection at the vendor's site before shipment. Pre-shipment inspection results can be recorded and counted for the lot.
- **Vendor evaluation (`ME61`)**: quality criteria sourced from QM scores (goods receipt inspection, audits, complaints/rejections) combined with price, delivery and service into a vendor score.
- **QM agreements**, **technical delivery terms** (TDT) and **audit management** (supplier audits) support APQP/PPAP style controls ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### Example
Vendor X supplies bead wire. History: last 12 lots accepted; the QM info record allows reduced inspection with certificate-based release for the diameter. A rejection triggers the dynamic modification rule to return to normal inspection and a Q2 notification; two rejections in 6 months pull the vendor score for quality from 92 to 78, which lowers the overall vendor score and the vendor's share in quota arrangements ([[192 SAP Sourcing & Procurement Deep Dive]]).

### In the news
See news box. Catena-X relies on supplier data exchange; the QM info record and quality agreements in SAP are where those commitments are held in the ERP.

### Interview angle
> [!question] How it is asked
> "How would you integrate supplier quality performance into purchasing decisions in SAP?"

> [!tip] Strong answer includes
> - QM info record and control key blocking or relaxing inspection
> - Certificates and source inspection to move inspection upstream
> - Vendor evaluation with quality score; quotas or source list changes
> - Escalation: SCAR/8D and audit schedule

---
## 9. Quality Notifications and Corrective Actions
> 🟠 Tier 2 · _Key points:_ Q1/Q2/Q3, items, causes, tasks, activities, 8D, returns

### Definition
A **quality notification** (`QM01` create, `QM02` change, `QM03` display; table `QMEL`) records a problem and drives its resolution. Standard types: **Q1 customer complaint**, **Q2 complaint against vendor**, **Q3 internal problem report**. Structure:
- **Header:** description, material, batch, vendor/customer, priority, reference documents (inspection lot, delivery, PO).
- **Items:** the defects (type, location, quantity) and **causes** (QMUR) per item.
- **Tasks** (QMSM) planned remedial or corrective actions with responsible person and due date; **activities** (QMMA) done actions.
- **Status flow:** outstanding, in process, task released, completed; with system status changes and **notification long text**.
- **Links:** **return delivery** to vendor (122), credit memo, replacement PO, **quality order** to collect costs, and **8D report** fields in many implementations.
- **Statistics:** notification lists, Pareto of defect types and causes.

Corrective and preventive action (CAPA) logic: contain (block stock), correct (rework/return), find root cause (5-why, fishbone), prevent recurrence (change plan, add characteristic, update FMEA), verify (follow-up inspection), and close.

### Example
Q2 notification for 5,000 bearings: item 1 defect "noise" qty 6 in sample; cause "vendor lapping wheel wear"; tasks: (1) return lot to vendor by Friday, (2) vendor submits 8D in 10 days, (3) buyer places 3-lot tightened inspection. Return freight ₹12,000 and sorting cost ₹8,000 are booked to a QM internal order for cost of poor quality reporting. The notification closes when the 8D is accepted and 3 consecutive lots pass.

### In the news
See news box. The recall-narrowing example works only if notifications record batch/serial and supplier information accurately.

### Interview angle
> [!question] How it is asked
> "A customer complains about defective product. How is it handled in SAP QM?"

> [!tip] Strong answer includes
> - Q1 notification created, linked to delivery and batch
> - Containment (block stock, trace batches), cause analysis, tasks with owners and dates
> - Vendor feedback via Q2 and 8D
> - Closure with effectiveness check and cost capture

---
## 10. Quality Costs and Reporting
> 🟠 Tier 2 · _Key points:_ Prevention, appraisal, internal and external failure; ppm; trends

### Definition
**Cost of quality (COQ)** has four categories (Feigenbaum PAF model): **prevention** (training, planning, FMEA), **appraisal** (inspection, testing, calibration), **internal failure** (scrap, rework before delivery) and **external failure** (returns, warranty, recalls). Failure costs usually dwarf prevention and appraisal.

Where numbers come from in SAP: **QM internal orders** or cost centres for inspection labour and tests; **scrap postings** (551) valued at standard; **return-to-vendor** and **credit memos**; **warranty/claims** postings through notifications and SD; **notification costs** assigned to a QM order. Reporting: **QM information system** (inspection and notification lists, defect and cause Pareto), **vendor evaluation reports**, **quality score** history, and BI/Analytics dashboards ([[085 SAP Reporting & Analytics]]). KPIs: **ppm** (defective parts per million), **first-pass yield**, **lot rejection rate**, **notification ageing**, **COPQ as % of sales**.

### Example
Annual sales ₹200 crore. Prevention 1.2, appraisal 2.0, internal failure 3.0, external failure 2.2 (₹ crore): total COQ = **8.4 crore = 4.2% of sales**; failure costs are 5.2/8.4 = **61.9%** of COQ. If an extra ₹0.8 crore in prevention reduces failure costs by ₹1.9 crore, net saving ₹1.1 crore. A plant with 12 rejected parts out of 85,000 shipped has 12/85,000 × 10^6 ≈ **141 ppm**.

### In the news
See news box. The €1.4–1.8 billion annual recall reserves in the Catena-X article show the scale of external failure cost in automotive.

### Interview angle
> [!question] How it is asked
> "How would you quantify and reduce the cost of poor quality using SAP data?"

> [!tip] Strong answer includes
> - PAF model with data sources in SAP
> - Pareto of defects and causes by vendor, material, line
> - Business case for prevention investments
> - KPIs tracked monthly: ppm, rejection rate, COPQ%

---
## 11. SPC, Control Charts and Process Capability
> 🟠 Tier 2 · _Key points:_ Xbar-R, limits, rules, Cp and Cpk, results history

### Definition
SAP QM stores quantitative results (from `QE51N`/`QE01`) so that **control charts** and **capability** can be calculated for characteristics flagged for it. Chart types: **mean (X-bar) with range (R) or standard deviation (s)**, **individual values with moving range**, and attribute charts (**p, np, c, u**). Control limits come from the process, not specification limits:
$$UCL_{\bar{x}} = \bar{\bar{x}} + A_2 \bar{R}, \quad LCL_{\bar{x}} = \bar{\bar{x}} - A_2 \bar{R}, \quad UCL_R = D_4 \bar{R}$$
For subgroup size 5: $A_2 = 0.577$, $D_4 = 2.114$, $D_3 = 0$. Capability indices:
$$C_p = \frac{USL - LSL}{6\sigma}, \quad C_{pk} = \min\left(\frac{USL-\mu}{3\sigma}, \frac{\mu-LSL}{3\sigma}\right)$$
Signals: points beyond limits, runs on one side, trends. A signal in a control chart can trigger a **quality notification**. Background: [[091 Statistical Quality Control (SQC)]].

### Example
Brake-disc thickness: $\bar{\bar{x}}=20.004$ mm, $\bar{R}=0.030$, $n=5$: $UCL = 20.004 + 0.577 \times 0.030 = 20.0213$; $LCL = 19.9867$; $UCL_R = 2.114 \times 0.030 = 0.0634$. Capability for a shaft with spec 25.00 ± 0.05 (LSL 24.95, USL 25.05), $\mu=25.012$, $\sigma=0.012$: $C_p = 0.10/0.072 = 1.39$; $C_{pk} = \min(0.038/0.036, 0.062/0.036) = \min(1.056, 1.722) = 1.06$. The process is wide enough (Cp 1.39) but off-centre; re-centring the mean to 25.00 would lift Cpk to 1.39. At the present mean about 771 ppm exceed the upper limit (normal assumption).

### In the news
See news box. Streaming sensor and field data feed the same logic at larger scale; the discipline of separating process limits from spec limits still applies.

### Interview angle
> [!question] How it is asked
> "A characteristic is within spec but the process is unstable. How do you know and what do you do?"

> [!tip] Strong answer includes
> - Control limits vs spec limits, special vs common cause
> - Cp vs Cpk; centring vs spread
> - SAP route: results history, control chart, notification
> - Actions: find the special cause, re-centre, reduce variation, re-check capability

---
## 12. Integration with MM, PP, SD, WM, PM and S/4HANA
> 🟠 Tier 2 · _Key points:_ Where QM triggers, stock types, batch and certificate flows

### Definition
| Module | Integration point | Effect |
|---|---|---|
| MM | GR for PO; vendor QM control; vendor evaluation; returns | Lot, QI stock, UD posting, 122 return |
| PP | In-process inspection via routing/inspection points; GR from order (inspection type 04) | Stop/continue production by operation results; FG release |
| SD | Delivery inspection; customer complaints Q1; certificates of analysis for batches | Block delivery until UD; CoA printed with delivery |
| WM/EWM | QI stock posts as WM quant status; GR to quality area | TO from GR to inspection bin; release after UD |
| PM | Calibration inspection of test equipment; PM notifications | Instrument locked on rejection |
| CO/FI | QM orders, scrap, return costs | Cost of poor quality in controlling |
| Batch management | Batch status, characteristics, expiry; batch where-used | Block batch, trace to customers |

**S/4HANA:** QM master data and processes continue; Fiori apps cover lot processing, results and UD (check the Fiori apps reference library for the current list), and **SAP Quality Issue Management** and other cloud quality offerings sit alongside. In the public cloud edition, the scope of QM differs from on-premise, so check the scope item list. See [[083 SAP WM-EWM — Warehouse]] for stock handling and [[081 SAP PP — Production Planning]] for in-process links.

### Example
In a pharma plant a batch of API arrives: GR posts to QI stock (WM puts it into a quarantine bin); the lot has assay and moisture characteristics; UD releases it and sets batch status "released"; production order issues (261) only from released batches; SD delivery of the finished batch prints the CoA; a later customer complaint (Q1) uses batch where-used to find all sibling shipments.

### In the news
See news box. Traceability from field to supplier (1.4 million vehicles narrowed to 14) depends on batch and serial integration across these modules.

### Interview angle
> [!question] How it is asked
> "How does QM connect to MM, PP and SD?"

> [!tip] Strong answer includes
> - Each module's trigger and stock effect
> - Batch traceability and CoA
> - Master data prerequisites per integration
> - S/4HANA position: same functions, new UI, cloud scope differences

---
## 13. Worked Inbound Inspection Flow, End to End
> 🟠 Tier 2 · _Key points:_ PO to GR to lot to results to UD to invoice or return

### Definition
Sequence with T-codes and documents:
1. **PO** `ME21N` for 10,000 bearings at ₹45 = ₹4,50,000 (QM procurement active; QM info record released, `QI01`).
2. **GR** `MIGO` 101: material document, accounting document (Dr Inventory 4,50,000 / Cr GR/IR 4,50,000); stock sits in **QI stock**; **inspection lot** created (`QA32`).
3. **Plan and sample:** plan `QP03` assigned; sampling scheme gives $n=200$, accept $c=5$.
4. **Results** `QE51N`: diameter, surface, noise tests on 200 pieces.
5. **UD** `QA11`: accept (A) or reject (R) → stock posting.
6. **Accept path:** 321 to unrestricted; invoice `MIRO` pays later.
7. **Reject path:** UD R; notification `QM01` Q2; stock blocked; 122 return; credit memo or replacement.
8. **Follow-up:** quality score to vendor evaluation; dynamic modification adjusts the next lot.

### Example
Case A: 4 defectives in the 200-piece sample (acceptance number 5, reject at 6): accept; 10,000 pieces to unrestricted; vendor score 100; next lot moves toward reduced sampling. Case B: 7 defectives: reject; blocked stock 10,000; return freight ₹12,000; the Q2 notification triggers 8D; cost of poor quality recorded ₹12,000 + sorting ₹8,000. Accounting for the return: reversal Dr GR/IR 4,50,000 / Cr Inventory 4,50,000 (122), with a debit note or credit memo for the vendor. With plan $n=200,c=5$, a vendor with true 2% defects has an acceptance probability of about 78.7% (computed earlier), so roughly one in five lots from such a vendor is rejected.

### In the news
See news box. Flow digitisation (instrument interfaces, automated UD) shortens the time stock waits in inspection, a hidden inventory and cash cost; see [[116 Inventory Valuation, Cycle Counting & Inventory Governance]].

### Interview angle
> [!question] How it is asked
> "Walk me through what happens in SAP from PO to inspection to payment for a QM-relevant raw material, with the accounting entries."

> [!tip] Strong answer includes
> - Document chain with T-codes and stock types at each stage
> - Entries at GR, UD (no value change for 321), and returns
> - Reject path with notification and return
> - Metrics: inspection lead time, lot rejection rate, quality score

---
## 14. ⭐ Advanced: Digital Quality, Supplier Data Exchange and Predictive Quality
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Trends reshaping QM:
- **Cross-company quality data networks** (Catena-X in automotive): production and field data exchanged under data-sovereignty rules to narrow root causes and recalls.
- **Closed-loop quality:** field complaints and service data flow back to design (FMEA, control plan) and to the supplier through notifications.
- **Automated measurement capture:** instruments, vision systems and LIMS integrated to results recording; auto-UD for good lots; exceptions go to people.
- **Predictive and AI-based quality:** models score the risk of a lot or process step failing (for example from machine parameters) and drive **risk-based inspection** (inspect more where risk is higher, less where history is good) while dynamic modification rules provide the traditional equivalent.
- **Cloud and S/4HANA:** QM scope per edition; **SAP Quality Issue Management** style offerings add collaboration with suppliers.
- **Regulation and standards:** GMP data integrity (audit trail, electronic signatures) for pharma, IATF 16949 and VDA for automotive, ISO 9001 clause on knowledge and monitoring.

Design caution: automation does not remove the need for controlled master data, clear ownership of catalogs and a training plan.

### Example
A tyre manufacturer's curing press sensors feed a model that scores each lot for under-cure risk. High-risk lots are routed to **tightened** inspection and a hardness test; low-risk lots use skip-lot. Over six months inspection hours drop 18% with no increase in escaped defects (illustrative result, not a reported case), and the model's flags are stored as characteristics in the lot for audit.

### In the news
See news box. The Catena-X case demonstrates the largest published benefit of shared quality data in this domain (1.4 million narrowed to 14 vehicles), as described by SAP.

### Interview angle
> [!question] How it is asked
> "How would digital technologies change quality management in a supplier-heavy industry?"

> [!tip] Strong answer includes
> - Data exchange across the chain and the governance behind it
> - Risk-based vs fixed sampling, with controls
> - Role of ERP master data and traceability
> - Realistic implementation path: pilot a critical component, prove the benefit, scale

Related: [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]] (calibration and equipment), [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]] (flows and Q&A), [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]].
