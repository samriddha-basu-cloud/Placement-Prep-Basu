---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP Sourcing & Procurement Deep Dive"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP Sourcing & Procurement Deep Dive

⬅ [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]] · [[_Index - SAP ERP|SAP ERP]] · [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Source Determination: How SAP Finds a Vendor]]
2. [[#2. Purchasing Info Record and Conditions]]
3. [[#3. Source List]]
4. [[#4. Quota Arrangement]]
5. [[#5. Outline Agreements: Contracts and Scheduling Agreements]]
6. [[#6. Release Strategies and Classification]]
7. [[#7. Vendor Evaluation (ME61)]]
8. [[#8. Subcontracting Process and Monitoring]]
9. [[#9. Services Procurement and Service Entry Sheets]]
10. [[#10. Automatic PO Creation and Purchasing Automation]]
11. [[#11. 3-Way Match, Tolerance Keys and Blocking]]
12. [[#12. S/4HANA Procurement Apps and Central Procurement]]
13. [[#13. Payment Terms, Vendor Blocks and the MSME Rule]]
14. [[#14. ⭐ Advanced: Procure-to-Pay Fraud and Control Design]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): procure-to-pay is re-platformed as ECC support runs out
> **S/4HANA 2025 on-premise release (8 Oct 2025).** IDES24 lists these items under "Sourcing & Procurement": **advanced ATP (aATP) with an automated stock-transport-order function**, an interactive supply-demand view, **event-driven planner notifications** for supply-demand imbalances and tighter integration with SAP IBP. (Vendor-described features; confirm in release notes before committing to a client.) ([IDES24](https://www.ides24.de/en/knowledge/what-s-new-in-s4hana-2025))
>
> **ECC deadline and the 2033 "transition option" (announced 4–5 Feb 2025).** Standard ECC maintenance ends **31 Dec 2027**; extended maintenance for on-premise SAP ERP ends at the **end of 2030**; for very large ECC estates SAP offers "SAP ERP, private edition, transition option", purchasable from **2028**, usable **2031–2033**, conditional on a RISE contract and SAP HANA. Procurement landscapes with hundreds of ECC systems are the case this was built for. ([CIO.com](https://www.cio.com/article/3816887/sap-throws-a-lifeline-to-large-organizations-with-new-ecc-offering.html); [TechTarget](https://www.techtarget.com/searchsap/news/366618912/Rise-With-SAP-will-extend-support-deadline-for-some))
>
> **GAIL goes live on S/4HANA Cloud (25 Jun 2025).** The Maharatna PSU described its one-year "Navodaya" programme as the first move of a Maharatna PSU from legacy ECC to S/4HANA on cloud. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
>
> **SAP Q2 2026 (23 Jul 2026).** Current cloud backlog **€22.9 billion (+27%)**; cloud revenue +24% at constant currency; 2026 cloud revenue outlook **€25.8–26.2 billion**. ([PR Newswire](https://www.prnewswire.com/news-releases/sap-quarterly-statement-q2-2026-302833633.html))
>
> Sub-topics that say **"See news box"** reuse these items. Foundations: [[080 SAP MM — Materials Management]]; strategy side: [[002 Procurement & Strategic Sourcing]].

---
## 1. Source Determination: How SAP Finds a Vendor
> 🟠 Tier 2 · _Key points:_ Quota, source list, outline agreement, info record; manual vs automatic

### Definition
**Source determination** assigns a supplier (and price) to a purchase requisition (PR) or PO item. SAP searches the source-of-supply data in this order of precedence (the exact path depends on the source list requirement and on whether the trigger is MRP, `ME57` or `ME21N`):
1. **Quota arrangement:** if one exists for the material, plant and date, the order is split across sources by quota.
2. **Source list:** if the plant requires a source list, only sources valid on the requirement date are eligible; a **fixed source** wins.
3. **Outline agreement:** contract or scheduling agreement (valid, with the right plant/material/purchasing org).
4. **Purchasing info record:** fallback; price from the info record and last/regular vendor.

If several sources remain, the user sees a **source list** dialog; if exactly one, it is assigned automatically; if none, buying is manual or goes through RFQ. In **MRP**, source determination happens when creating PRs; a PR for which a source exists can be turned into a PO by automatic PO creation (`ME59N`). T-code `ME57` (assign and process PRs) lets buyers assign sources to many PRs at once.

The **source list requirement** (set in the material master or plant parameters) and the **MRP-relevant** indicator in each source-list record control whether MRP uses it.

### Example
HDPE granules for plant 1100: a quota arrangement splits 60% to vendor A and 40% to vendor B. A has a contract at ₹94/kg; B has only an info record at ₹96/kg. A 5,000 kg PR is split by quota into 3,000 kg to A (via the contract price) and 2,000 kg to B (info record price). If the source list marked A as "fixed", the quota step would be bypassed. Weighted price = (3,000 × 94 + 2,000 × 96) / 5,000 = **₹94.80/kg**.

### In the news
See news box. Event-driven planner notifications and aATP listed by IDES24 sit on top of this classic source-determination logic.

### Interview angle
> [!question] How it is asked
> "How does SAP determine the source of supply for a PR?" or "Difference between a source list and a quota arrangement?"

> [!tip] Strong answer includes
> - Order of precedence with clear one-line explanation of each
> - Source list as allowed/blocked/fixed vendors; quota as split ratio
> - MRP relevance and source list requirement
> - Business reason: compliance (approved vendors) and risk (dual sourcing)

---

## 2. Purchasing Info Record and Conditions
> 🟠 Tier 2 · _Key points:_ ME11, general vs purchasing-org data, price conditions, scales

### Definition
An **info record** links one **vendor** with one **material** (or material group) and stores purchasing data: vendor material number, planned delivery time, standard order quantity, tolerances, and **conditions** (prices). Types: **standard, subcontracting, pipeline, consignment**.
- **General data** (vendor/material level): vendor material number, vendor subrange, base data.
- **Purchasing organisation data**: price, planned delivery time, minimum quantity, purchasing group, incoterms, GR/IR controls.
- **Conditions** with validity dates and **scales**: **PB00** gross price (net-price relevant), **PBXX** gross price without discounts, **RA01** percentage discount, **FRB1** absolute freight; tax comes from the tax procedure (India GST uses procedure TAXINN) and not from the info record.
- **Info update** indicator in the PO item saves the PO price back into the info record.

T-codes: `ME11` create, `ME12` change, `ME13` display, `ME1M` info records per material, `ME1P` PO price history, `ME1L` per vendor. Info records can be created manually, from an RFQ/quotation, or automatically from the PO. In S/4HANA they remain central; contracts can also hold the conditions.

### Example
Vendor quotes scale prices for HDPE: 1–999 kg ₹100, 1,000–4,999 kg ₹98, 5,000 kg and above ₹95. Discount RA01 is 2% and freight FRB1 is ₹1.50 per kg. An order for 6,000 kg gets ₹95; after 2% discount, net ₹93.10; with freight ₹94.60 per kg, so **₹5,67,600 before GST** (goods ₹5,58,600 + freight ₹9,000). For 3,000 kg the scale price ₹98 gives ₹98 × 0.98 × 3,000 = ₹2,88,120 goods. The buyer sees the scale step at 5,000 kg: ordering 2,000 kg more reduces unit cost by ₹3, which supports consolidating orders.

### In the news
See news box. For multi-system landscapes (the 2033 transition-option case), info records are among the master data that central procurement hubs distribute.

### Interview angle
> [!question] How it is asked
> "What is an info record, what data does it hold and how is the price determined in a PO?"

> [!tip] Strong answer includes
> - Vendor-material link with general and purchasing-org data
> - Conditions, scales and validity; PB00 and RA01 example
> - Info update from PO
> - Difference between info record, contract and source list

---

## 3. Source List
> 🟠 Tier 2 · _Key points:_ ME01, fixed/blocked source, MRP indicator, source list requirement

### Definition
A **source list** records, per material and plant, which vendors (or outline agreements, or supplying plants) are **allowed** to supply during which validity period. Fields: valid-from/to, vendor, purchasing org, **info record or outline agreement** reference, and indicators:
- **Fixed source:** the source that must be used (only one per validity period).
- **Blocked source:** vendor barred for a period (quality or compliance problem).
- **MRP indicator:** 0 not relevant to MRP; 1 MRP uses the entry to assign the source to PRs; 2 MRP may also create delivery schedule lines directly for a scheduling agreement.

The **source list requirement** is switched on in the material master (Purchasing view) or for the plant; once on, a PO can only be issued to a vendor on the source list (a strict control for approved-vendor policy). Maintenance: `ME01` manual, `ME03` display, `ME05` generate automatically from info records and outline agreements, `ME04` change log, `ME06` analyse source lists.

In regulated industries such as pharma, the source list is the system embodiment of the **approved vendor list (AVL)**: only audited suppliers may be used ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### Example
For HDPE at plant 1100: vendor A (valid 1 Jan 2026 to 31 Dec 2026, fixed, MRP indicator 1), vendor B (valid same period, not fixed), vendor C blocked after a failed audit. MRP assigns A to every PR; a buyer tries a PO to vendor C and gets the message that C is blocked for this period. When A's capacity is hit, the buyer removes "fixed" and splits to B.

### In the news
See news box. Approved-vendor controls matter most when systems are consolidated and risk data is merged.

### Interview angle
> [!question] How it is asked
> "What is a source list? How is it different from an info record?"

> [!tip] Strong answer includes
> - Allowed vendors by period; fixed and blocked flags
> - Source list requirement and MRP relevance
> - Auto-generation via `ME05`
> - Role in approved-vendor and compliance policy

---

## 4. Quota Arrangement
> 🟠 Tier 2 · _Key points:_ MEQ1, quota rating formula, split by percentage, max quantity

### Definition
A **quota arrangement** distributes procurement requirements across several sources according to **quotas** (shares). It is used for dual/multi-sourcing, domestic/import splits and for in-house vs external production. Items carry: source (vendor, supplying plant or production), **quota %**, **max quantity**, **max release quantity** per order, **minimum lot size**, procurement type (normal, subcontracting, stock transfer), and **quota base quantity**. Maintain with `MEQ1`, display `MEQ4`; activate in the material master via the **quota arrangement usage** key (e.g. in MRP and PRs).

Allocation rule: for each new requirement the system calculates the **quota rating** of every source and gives the requirement to the **lowest rating**:
$$\text{Quota rating}=\frac{\text{allocated quantity}+\text{quota base quantity}}{\text{quota}}$$
Allocated quantity grows after each assignment, so shares converge to the quota ratio over time. The base quantity is used to seed or correct a source (e.g. to start a new vendor with a deliberate lag).

### Example
Quotas A 50, B 30, C 20; each order is a 1,000 kg lot.

| Order | Rating A | Rating B | Rating C | Goes to |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | A |
| 2 | 20 | 0 | 0 | B |
| 3 | 20 | 33.3 | 0 | C |
| 4 | 20 | 33.3 | 50 | A |
| 5 | 40 | 33.3 | 50 | B |
| 6 | 40 | 66.7 | 50 | A |

After 10 orders: A 5,000 kg, B 3,000 kg, C 2,000 kg, exactly 50 : 30 : 20. A max quantity of 4,000 kg on A would stop it receiving more and shift the rest to B and C.

### In the news
See news box. Quota logic is also a risk-mitigation tool when supply disruptions force buyers to move volumes between vendors quickly ([[015 Supply Chain Risk & Resilience]]).

### Interview angle
> [!question] How it is asked
> "How does SAP split a requirement between two vendors 70:30?"

> [!tip] Strong answer includes
> - Quota arrangement with quota %, max qty and rating formula
> - Lowest-rating-first logic and a numeric run
> - Where it applies: MRP source determination, subcontracting, plant transfers
> - Business use: dual sourcing for risk and bargaining power

---

## 5. Outline Agreements: Contracts and Scheduling Agreements
> 🟠 Tier 2 · _Key points:_ Quantity vs value contract, release order, scheduling agreement, delivery schedules

### Definition
**Outline agreements** are long-term purchasing arrangements with a vendor over a validity period; they do not by themselves trigger delivery.
- **Contract:** two kinds. **Quantity contract (MK)** commits a target quantity; **value contract (WK)** a target value. Each call-off is a **release order**, an ordinary PO that references the contract (`ME21N` with contract reference, or `ME31K` to create the contract). Lists: `ME2K` (by account assignment), `ME2N`. Contract can include price scales and item categories.
- **Scheduling agreement (LP / LPA):** a long-term agreement with a vendor where the delivery dates and quantities are given as **schedule lines** (`ME31L`). Planned by MRP, which creates **delivery schedule lines** automatically (no PR); releases are sent as **forecast delivery schedules** and **JIT delivery schedules**, with **cumulative received quantities** reconciled between buyer and vendor. Maintain schedule `ME38`, output `ME9L`, lists `ME2L`.
- **Release documentation:** history of releases; shows how much of the target quantity or value is already used.
- S/4HANA: Fiori apps such as Manage Purchase Contracts and Monitor Purchase Contract Consumption.

Use contracts when you buy in unknown timing and want the price locked (indirect spend), and scheduling agreements for repetitive production material with fixed cadence (automotive tier-1 supply).

### Example
Value contract with vendor Shree Packaging, target value ₹50,00,000, validity 1 Apr 2026 to 31 Mar 2027, price ₹40 per carton. Three release orders: ₹12,00,000 (30,000 cartons), ₹15,00,000 (37,500), ₹9,00,000 (22,500). Released value = **₹36,00,000**, remaining **₹14,00,000** (28%). A scheduling agreement for a seat-frame supplier would instead show weekly schedule lines of, say, 400 units sent via EDI, with JIT releases for the next 3 days.

### In the news
See news box. Event-driven notifications for supply-demand imbalances (IDES24, 2025) matter most for scheduling-agreement items, where schedules change weekly.

### Interview angle
> [!question] How it is asked
> "Contract vs scheduling agreement: when to use which and how are release orders created?"

> [!tip] Strong answer includes
> - Quantity vs value contract; target and release documentation
> - Scheduling agreement with schedule lines, JIT/forecast releases, MRP integration
> - Flow with numbers (target vs released)
> - Strategic fit: price lock vs repetitive supply

---

## 6. Release Strategies and Classification
> 🟠 Tier 2 · _Key points:_ Release group/code/indicator/strategy, CEKKO characteristics, class type 032, approvals

### Definition
This sub-topic extends the high-level release strategy covered in [[080 SAP MM — Materials Management]]. A **release strategy** decides who must approve a PR or PO before it becomes an order, based on **classification**:
- **Characteristics** (`CT04`) on communication structure **CEKKO** for the PO header (e.g. `GNETW` total net order value, `BSART` document type, `EKGRP` purchasing group, `WERKS` plant) or **CEBAN** for PRs.
- **Class** (`CL02`) of **class type 032** collecting those characteristics.
- **Release group** (object type: PR/PO), **release codes** (approver roles), **release indicators** (status: blocked, released), and **release strategy** (the combination of codes and prerequisites, plus classification values that trigger it).
- **Release prerequisites** define sequence: code 02 can release only after 01.
- **Changeability:** after release, if the PO value changes beyond a tolerance percentage, the strategy can reset and re-trigger approval.

Approvals: `ME28` (collective), `ME29N` (individual); PR `ME54N`/`ME55`. Customising in SPRO: MM → Purchasing → Purchase Order → Release Procedure for PO. In S/4HANA, the Fiori apps (Manage Purchase Orders, My Inbox) show items awaiting release and **flexible workflow** can supplement or replace the classic procedure in some editions.

### Example
Thresholds on `GNETW`: ≤ ₹1,00,000: no release. ₹1,00,001 to ₹10,00,000: code 01 (purchasing manager). ₹10,00,001 to ₹50,00,000: 01 then 02 (plant head). Above ₹50,00,000: 01, 02, then 03 (CFO). A ₹12,00,000 PO therefore needs 01 and 02. If someone splits it into two POs of ₹6,00,000 to avoid the plant head, `ME2N` by vendor and date exposes the pattern, and the release strategy can be built to check the aggregate requirement value at PR level.

### In the news
See news box. Public-sector buyers moving to S/4HANA (GAIL, as an example of a PSU migration) need delegations of authority mapped into approval logic.

### Interview angle
> [!question] How it is asked
> "How is a release strategy configured and how would you stop PO splitting?"

> [!tip] Strong answer includes
> - Characteristics/class (CEKKO, class type 032), codes, indicators, prerequisites
> - Config example with ₹ thresholds
> - Changeability after release; split-order control
> - Link to delegation-of-authority policy and audit trail

---

## 7. Vendor Evaluation (ME61)
> 🟠 Tier 2 · _Key points:_ Main criteria, sub-criteria, weights, score 1-100, automatic vs manual

### Definition
**Vendor evaluation** (MM-PUR) produces a **score from 1 to 100** per vendor (optionally per material) from weighted criteria:
- **Main criteria:** Price, Quality, Delivery, General service/support, External service/ (user-defined).
- **Sub-criteria:** e.g. under Price: price level, price history; under Quality: goods receipt inspection results, quality audit, complaints/rejections; under Delivery: on-time delivery performance, quantity reliability, compliance with shipping instructions, confirmation date.
- **Weighting keys:** each main and sub-criterion has a weight; the sum of weights defines the final score.
- **Scoring:** automatic sub-criteria are computed from PO, GR and QM data; manual ones are entered by buyers.

T-codes: `ME61` maintain vendor evaluation, `ME62` display, `ME63` evaluation display; customising via the Purchasing → Vendor Evaluation path. Scores can be used for selection and vendor reviews; it is basic compared with supplier-performance tools in SAP Ariba ([[199 SAP Ariba, SRM & Business Network]]). Check the Simplification List for your S/4HANA release before promising it to a client.

### Example
Weights: price 40%, quality 30%, delivery 20%, service 10%. Vendor A scores 80/90/70/60, vendor B 95/70/85/80.
- A: 0.4 × 80 + 0.3 × 90 + 0.2 × 70 + 0.1 × 60 = **79.0**
- B: 0.4 × 95 + 0.3 × 70 + 0.2 × 85 + 0.1 × 80 = **84.0**
B wins overall on price and delivery, but its quality score (70) is below A's (90), so a pharma buyer with a quality threshold of 80 would exclude B and block it in the source list.

### In the news
See news box. As ERP consolidation brings several vendor bases together, evaluation scores often differ and need normalising.

### Interview angle
> [!question] How it is asked
> "How would you evaluate and compare vendors in SAP?"

> [!tip] Strong answer includes
> - Criteria, weights and 1-100 scoring
> - Automatic data sources (GR, QM, PO) vs manual input
> - Worked weighted score and how to use thresholds
> - Limits and where Ariba or custom analytics complement it

---

## 8. Subcontracting Process and Monitoring
> 🟠 Tier 2 · _Key points:_ Info category 1, PO item L, 541, 101 + 543, ME2ON, cost build-up

### Definition
Subcontracting (job work) is covered at movement level in [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]]; here is the procurement view.
1. **Master data:** finished material with **procurement type F** (external) and a **BOM** listing the components to provide; **subcontracting info record** (info category 1) with the service price and planned delivery time.
2. **PO** with item category **L**; the system explodes the BOM into component lines.
3. **Provision** of components: 541 to special stock **O**; reservations by the PO guide the picking.
4. **Receipt:** GR 101 of the finished item; components consumed (543); component quantities can be corrected (actual consumption) in the GR screen.
5. **Invoice** for the service fee (GR-based).
6. **Monitoring:** `ME2ON` cockpit (components required, provided, consumed), `MBLB` (stock at vendor), `ME2O` (older report).

Cost: $\text{Unit cost}=\frac{\text{Component value}+\text{Service fee}}{\text{Quantity received}}$. Companies Act and GST considerations (job-work challan, ITC-04) are in the MM note.

### Example
2,000 gear blanks at ₹150 (₹3,00,000) are sent to a heat-treatment vendor charging ₹28 per piece (₹56,000). Finished gears received 2,000: total cost ₹3,56,000, i.e. **₹178 per piece**. If 30 blanks are lost in processing and the contract allows 1% loss (20 pieces), the buyer recovers or debits the vendor for 10 extra blanks (10 × ₹150 = ₹1,500).

### In the news
See news box. Subcontracting scenarios are typical test cases in S/4HANA migration scripts for auto and engineering plants.

### Interview angle
> [!question] How it is asked
> "Walk me through subcontracting in SAP, from PO to invoice, and how you monitor stock at the vendor."

> [!tip] Strong answer includes
> - PO item L, BOM, 541, GR 101 with 543, fee-only invoice
> - Monitoring tools and reconciliations of component consumption
> - Cost build-up with numbers; handling of scrap and over-consumption
> - Compliance: job-work challan

---

## 9. Services Procurement and Service Entry Sheets
> 🟠 Tier 2 · _Key points:_ Item category D, service master, ML81N, acceptance, limit PO

### Definition
Services (AMC, housekeeping, transport, consulting) are bought with **PO item category D** (service) and no material number. Elements:
- **Service master** (`AC01`/`AC02`/`AC03`): catalogue of standardised services with units.
- **Service specifications** on the PO: planned services with quantity and price, or **limits** (expected value and overall limit for unplanned services) for open-ended work.
- **Service entry sheet (SES)** (`ML81N`): records the work done; has an approval (release) step by the requester or a cost-centre manager; accepting it posts the goods-receipt equivalent (**Dr Expense, Cr GR/IR**).
- **Invoice verification** is always against the accepted SES (GR-based): MIRO Dr GR/IR, Dr input GST, Cr vendor, plus TDS.
- **Outline (hierarchical) service specifications** for large projects (EPC) with hierarchical packages ([[168 Project Procurement, Contracts & EPC Delivery]]).
- Account assignment is mandatory (K cost centre, F order, P project) and funds are committed at PO stage.

### Example
Annual maintenance contract (AMC) for HVAC ₹12,00,000 a year, paid monthly. PO with service line ₹12,00,000 and planned monthly entries. Each month: SES of ₹1,00,000 accepted by the facilities manager (Dr Maintenance expense ₹1,00,000, Cr GR/IR ₹1,00,000); MIRO adds GST 18% = ₹18,000, giving vendor payable ₹1,18,000 less TDS at the applicable rate. If the work is not accepted, there is nothing to invoice against, which is the control.

### In the news
See news box. Services are a large share of indirect spend, and cloud procurement tools wrap SES into approval workflows.

### Interview angle
> [!question] How it is asked
> "Explain the services procurement process and how you control service spend."

> [!tip] Strong answer includes
> - Item category D, service master and specifications or limits
> - SES creation, acceptance and 3-way match through the SES
> - Accounting entries and commitment
> - Controls: limits, release, TDS and GST

---

## 10. Automatic PO Creation and Purchasing Automation
> 🟠 Tier 2 · _Key points:_ ME59N, preconditions, scheduling-agreement releases, touchless buying

### Definition
**Automatic PO generation** turns PRs into POs without buyer intervention. Preconditions:
- The PR has an **assigned source** (fixed vendor, source list or contract) so the vendor is known.
- The **vendor master** (purchasing data) has the **automatic purchase order** indicator.
- The **material master** (Purchasing view) allows automatic POs (indicator "Autom. PO").
- Item category and account assignment are standard; PRs requiring release have been released.

Run `ME59N` (online or as a background job) with selection by plant, purchasing group, material and creation date; log shows created POs and errors (`ME59N` also supports test run). Related: `ME58` (ordering: assigned PRs), `ME57` (assign and process PRs), **scheduling-agreement releases** created directly by MRP when source list indicator 2 is used, and output via EDI/email.

Typical "touchless" design: MRP creates PR with contract source, release strategy not needed under a value limit, `ME59N` job creates PO, output by EDI. In S/4HANA the intelligent assignment and PR Fiori worklists (such as Purchase Requisition Assignment) support the same flow.

### Example
A plant buys 200 types of caps, each with a contract and a fixed-vendor source list entry. MRP creates 120 PRs a week; `ME59N` converts 105 into POs overnight. The remaining 15 failed because the vendor lacked the automatic indicator (6), the PR needed release (5) or no source existed (4). A buyer clears only those 15; touchless rate = 105/120 = **87.5%**.

### In the news
See news box. Event-driven notifications for planners (IDES24, S/4HANA 2025) reduce the manual monitoring that used to follow batch jobs.

### Interview angle
> [!question] How it is asked
> "How would you automate PO creation and what are the prerequisites?"

> [!tip] Strong answer includes
> - `ME59N` and the three prerequisites (source, vendor flag, material flag)
> - Scheduling-agreement releases and EDI output
> - Touchless rate KPI and exception handling
> - Governance: value caps and release strategy still apply

---

## 11. 3-Way Match, Tolerance Keys and Blocking
> 🟠 Tier 2 · _Key points:_ OMR6 tolerance keys, block reasons, MRBR, ERS, 2-way match

### Definition
In **logistics invoice verification** the invoice is compared with the PO (price) and GR (quantity). Tolerances are set per company code in `OMR6` and use **tolerance keys**; a variance within tolerance posts normally, outside it the invoice is **blocked for payment** until released in `MRBR`.

| Key | Controls |
|---|---|
| **PP** | Price variance (absolute and %) |
| **PS** | Price variance against an estimated price |
| **DQ** | Quantity variance when a GR exists |
| **DW** | Quantity variance when no GR yet |
| **BD** | Small differences posted automatically to a small-difference account |
| **BR / BW** | Percentage order-price-quantity variance (invoice before / after GR) |
| **ST** | Date variance (value × days) |
| **VP** | Moving average price variance |
| **KW** | Variance from condition values |

**Block reasons:** R (quantity), P (price), D (date), M (manual), S (stochastic: random sample selection). **Evaluated receipt settlement (ERS, `MRRL`)** invoices automatically from GR (no vendor invoice), common in trusted-supplier and subcontracting flows; **2-way match** applies where no GR exists (non-GR-based items). A **tolerance** is a controlled decision of finance and procurement, not just a technical setting.

### Example
PO 1,000 units at ₹100; GR 1,000. Vendor invoices ₹104 (price +4%, ₹4,000). With the PP upper limit at 2% the invoice is blocked with reason P; with 5% it posts. A second invoice for 1,050 units at ₹100: invoice quantity exceeds GR by 50 (5%, ₹5,000). With DQ upper limit 5% it posts; with 2% it is blocked R until the extra 50 are received or credited. Blocking prevents overpayment risk of ₹4,000 and ₹5,000 here.

### In the news
See news box. Automated invoice capture (OCR/e-invoice) feeds MIRO faster, but the tolerance logic stays the control.

### Interview angle
> [!question] How it is asked
> "What are tolerance keys in invoice verification, and what do you do with a blocked invoice?"

> [!tip] Strong answer includes
> - Tolerance keys (PP, DQ, BD) and per-company-code configuration
> - Block reasons and release with `MRBR`
> - 2-way vs 3-way and ERS
> - Calibrating tolerances to risk: tight for high-value, looser for low-value items

---

## 12. S/4HANA Procurement Apps and Central Procurement
> 🟠 Tier 2 · _Key points:_ Fiori apps, Central Procurement hub, Ariba, classic ME21N still available

### Definition
S/4HANA keeps the MM-PUR data model but adds **Fiori apps** on top of the same tables:
- **Requisitions:** Manage Purchase Requisitions (Professional) for buyers; self-service requisitioning for employees.
- **Purchase orders:** Manage Purchase Orders and Create Purchase Order (Advanced); `ME21N` remains in the on-premise edition.
- **Contracts and monitoring:** Manage Purchase Contracts, Monitor Purchase Order Items, Monitor Purchase Contract Consumption.
- **Invoices:** supplier-invoice apps over the same MIRO logic.
- **Business Partner** replaces the classic vendor master.

**SAP S/4HANA Central Procurement** is a **hub** model: one S/4HANA system acts as a procurement hub for several connected systems (ECC or S/4HANA). It offers **central requisitioning** (PRs from connected systems are processed centrally), **central contracts** distributed to connected systems, and **central purchase orders** executed in the hub and replicated to the receiving system for goods receipt and invoice. Sourcing and spend visibility then sit in one place, with **SAP Ariba** supporting sourcing events and supplier collaboration ([[199 SAP Ariba, SRM & Business Network]]).

For large conglomerates with many ECC systems the hub is a step towards consolidation without moving everything at once.

### Example
A group has 3 ECC plants on separate systems. Each uses its own contract for steel at a different price (₹71, ₹73, ₹75 per kg) with the same vendor. A central contract at ₹70 for 1,500 tonnes a month, distributed to all three through the hub, saves on average (₹73 − ₹70) = ₹3/kg, i.e. **₹45 lakh a month** (1,500 t × 1,000 kg × ₹3 = ₹45,00,000), assuming equal volumes and the same vendor performance.

### In the news
See news box. SAP's transition-option for very large ECC estates (2031–2033) and the hub concept both address landscapes with many systems.

### Interview angle
> [!question] How it is asked
> "What is central procurement in S/4HANA and when would you recommend it?"

> [!tip] Strong answer includes
> - Hub-and-spoke concept; central requisitions, contracts, POs
> - Fiori apps vs classic transactions; Business Partner
> - Ariba complement for sourcing events
> - Fit: multi-system, multi-entity groups; caution about migration effort ([[200 SAP S-4HANA Migration, Data Migration & Testing]])

---

## 13. Payment Terms, Vendor Blocks and the MSME Rule
> 🟠 Tier 2 · _Key points:_ Terms of payment key, cash discount, posting/purchasing/payment blocks, 43B(h)

### Definition
**Payment terms** are keys (client-specific names, for example one for net 45 days and one for 2% in 10 days, net 30) held in the vendor master (company code data) and defaulted into PO and invoice. They define the **baseline date** (invoice, posting or GR date), discount percentages and days, and net due date. The **payment run** (`F110`) uses due date, discount and payment block.

**Vendor blocks:**
| Block | Effect | Level |
|---|---|---|
| Central posting block | No postings at all | All company codes |
| Company-code posting block | No postings | Company code |
| Central purchasing block | No POs | All purchasing orgs |
| Purchasing-org block | No POs | Purchasing org |
| Payment block (vendor or invoice) | Invoice posts but is excluded from payment | Company code / item |

In S/4HANA the same blocks are maintained on the **Business Partner**. **Cash discount value:** annualised return = $\frac{d}{1-d}\times\frac{365}{N-D}$ with discount d, discount days D, net days N.

**India: MSME rule.** Under the MSMED Act, buyers must pay micro and small enterprises within the agreed period (max **45 days** from acceptance; **15 days** if there is no written agreement); interest accrues for delay. Since Finance Act 2023, section 43B(h) of the Income-tax Act allows deduction of such purchases only in the year of actual payment, so **SAP payment terms and aging for MSME vendors should be capped at 45 days** and flagged for run priority. (Verify current rules with the finance team.)

### Example
"2/10 net 30" gives an annualised return of 0.02/0.98 × 365/20 = **37.2%**, so paying early is better than a 12% overdraft. "2/10 net 45" gives only **21.3%**. For an MSME vendor with invoice accepted on 1 Mar 2026 and a written agreement for 45 days, the due date is 15 Apr 2026; without agreement the legal limit is 16 Mar 2026. Missing it can disallow the expense in the current tax year, not just create interest.

### In the news
See news box. Moving the vendor master to Business Partner in S/4HANA is the moment to clean block logic, payment terms and MSME flags.

### Interview angle
> [!question] How it is asked
> "Which blocks exist on a vendor master and how would you handle MSME payment timelines?"

> [!tip] Strong answer includes
> - Posting vs purchasing vs payment blocks, with level
> - Payment terms, baseline date and cash discount annualised
> - MSME 45-day rule and 43B(h) consequence
> - Working-capital trade-off versus statutory compliance ([[136 Supply Chain Finance & Working Capital]])

---

## 14. ⭐ Advanced: Procure-to-Pay Fraud and Control Design
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Procure-to-pay (P2P) is a classic fraud area. A consultant should be able to design controls, using SAP features:
- **Segregation of duties (SoD):** the person who maintains vendors, creates POs, posts GR and approves invoices cannot be the same; test with SAP GRC ([[201 SAP Landscape, Transports, Security & GRC Basics]]).
- **Vendor master controls:** duplicate checks (name, tax number, bank account), dual approval for bank-detail changes, one-time-vendor limits, GSTIN and PAN validation.
- **PO controls:** release strategy, source list requirement, price tolerance versus info record, split-order monitoring.
- **Invoice controls:** duplicate-invoice check (vendor, reference, date, amount), tolerance blocks, stochastic block (sample), GR-based IV.
- **Payment controls:** payment run approval, payment blocks, bank file dual authorisation.
- **Detection analytics:** vendors with many invoices just under approval limits, round-sum invoices, vendor and employee address/bank matches, weekend postings; process-mining tools help ([[173 Process Mining & Operations Intelligence]]).

### Example
An analyst finds 14 POs to one vendor in a month, each between ₹9,50,000 and ₹9,99,000 when the next approval step is at ₹10,00,000. Total about ₹1.38 crore (illustrative case). Three signals combine: values just under the threshold, a vendor created two months ago and the same user creating PO and GR. The control response: a release rule on total value per vendor per month, mandatory vendor approval and reassigning the GR role.

### In the news
See news box. As landscapes move to S/4HANA/RISE, SoD rules and role design have to be rebuilt, which makes fraud-control design a core migration deliverable.

### Interview angle
> [!question] How it is asked
> "How would you reduce the risk of fraud in the procurement process using SAP?"

> [!tip] Strong answer includes
> - Layered controls across vendor, PO, GR, invoice and payment
> - SoD and role design
> - Data analytics on thresholds and duplicates
> - Cost/benefit judgement: controls proportionate to risk
