---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP Production Execution, Confirmation & Product Costing"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP Production Execution, Confirmation & Product Costing

⬅ [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]] · [[_Index - SAP ERP|SAP ERP]] · [[195 SAP SD Advanced - Pricing, Output & Document Flow]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Production Order: Structure and Order Types]]
2. [[#2. Order Lifecycle and Status Management]]
3. [[#3. Release, Availability Check and Goods Issue: Manual vs Backflush]]
4. [[#4. Confirmation: CO11N and CO15]]
5. [[#5. Goods Receipt, By-products and Co-products]]
6. [[#6. Product Costing: BOM + Routing = Cost Estimate (CK11N)]]
7. [[#7. Standard Cost Estimate: Marking, Release and Revaluation]]
8. [[#8. Planned vs Actual Costs and WIP Calculation]]
9. [[#9. Variance Categories at Production-Order Level]]
10. [[#10. Settlement and Journal Entries]]
11. [[#11. TECO, Business Completion and the Order Closing Sequence]]
12. [[#12. Rework and Scrap]]
13. [[#13. Plain-English Glossary of Production and Costing Terms]]
14. [[#14. ⭐ Advanced: S/4HANA Costing, Material Ledger and Production Changes]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): production execution and costing move onto S/4HANA's real-time model
> **S/4HANA 2025 on-premise release (8 Oct 2025).** IDES24's release overview lists a manufacturing enhancement for **comprehensive rework, even after the order has been completed and for purchased parts**, plus more efficient production engineering and flexible production processes; under Finance it lists faster period-end closing and automated reconciliations on the Universal Journal. (Vendor-described features; confirm in release notes.) ([IDES24](https://www.ides24.de/en/knowledge/what-s-new-in-s4hana-2025))
>
> **ECC deadline and the 2033 "transition option" (announced 4–5 Feb 2025).** Standard ECC maintenance ends **31 Dec 2027**; extended maintenance for on-premise SAP ERP ends at the **end of 2030**; for very large ECC estates SAP offers a transition option purchasable from **2028**, usable **2031–2033**, tied to a RISE contract and SAP HANA. Plants must retest order costing, settlement and the material-ledger run on S/4HANA before then. ([CIO.com](https://www.cio.com/article/3816887/sap-throws-a-lifeline-to-large-organizations-with-new-ecc-offering.html); [TechTarget](https://www.techtarget.com/searchsap/news/366618912/Rise-With-SAP-will-extend-support-deadline-for-some))
>
> **GAIL goes live on S/4HANA Cloud (25 Jun 2025).** GAIL, a gas-processing and petrochemicals major, called its one-year "Navodaya" programme the first move of a Maharatna PSU from legacy ECC to S/4HANA on cloud; its finance director stressed building a smarter, more agile enterprise rather than a technology change. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
>
> **SAP Q2 2026 (23 Jul 2026).** Current cloud backlog **€22.9 billion (+27%)**; cloud revenue +24% at constant currency; 2026 cloud revenue outlook **€25.8–26.2 billion**; Investing.com reports Cloud ERP Suite revenue of €5.5 billion (+27%), about 88% of cloud revenue. ([PR Newswire](https://www.prnewswire.com/news-releases/sap-quarterly-statement-q2-2026-302833633.html); [Investing.com](https://www.investing.com/news/company-news/sap-q2-2026-slides-cloud-backlog-surges-27-amid-margin-pressure-93CH-4810220))
>
> Sub-topics that say **"See news box"** reuse these items. Foundations: [[081 SAP PP — Production Planning]], [[110 Cost Accounting for Operations]], [[190 SAP FI-CO Essentials for Operations Professionals]].

---
## 1. Production Order: Structure and Order Types
> 🟠 Tier 2 · _Key points:_ Header, components, operations, order type, production version

### Definition
A **production order** (discrete manufacturing) is the instruction to make a quantity of a material by a date, with the full recipe. Plain English: it is the "job card" of the factory, and the account that collects what the job costs.

Structure:
- **Header:** material, quantity, basic start/finish dates, plant, **order type** (e.g. PP01), **production version** (which BOM + routing), MRP controller, profit centre and status.
- **Components:** copied from the **BOM** with quantities scaled to the order quantity; each creates a **reservation**. Items can have scrap % and a backflush flag.
- **Operations:** copied from the **routing**: work centre, setup/machine/labour standard values, control key, reporting points.
- **Costing:** **planned costs** (from BOM and routing at the cost estimate) and **actual costs** (as postings happen).
- **Order type controls:** number range, settlement profile, order-type-dependent parameters (confirmation parameters, status profile, costing variants), and whether it is cost-collecting or has revenue.

Order creation: manual `CO01`, planned order conversion from MRP (`MD04`, `CO40`), or automatically from sales orders (MTO). Change `CO02`, display `CO03`, mass `COHV`, list `COOIS` (order information system). Process industries use **process orders** (`COR1`) with recipes; repetitive manufacturing uses period-based backflush ([[081 SAP PP — Production Planning]]).

### Example
Order 1000812: 1,000 pieces of gear housing FG-500, production version 0001, start 5 Oct, finish 12 Oct. Components: aluminium alloy 2,000 kg (2 kg per piece) and bolts 4,000 (4 per piece); operations: 0010 machining (250 machine hours, 800 labour hours in total at 1,000 pieces) and 0020 assembly. Planned cost of the order (see sub-topic 6): ₹8,36,000.

### In the news
See news box. S/4HANA keeps the production order but surfaces it through new Fiori apps and a faster, single data model.

### Interview angle
> [!question] How it is asked
> "What is a production order and what does it contain?"

> [!tip] Strong answer includes
> - Header, components (from BOM), operations (from routing), costing
> - Order type and production version as control fields
> - Creation routes (MRP conversion, `CO01`, MTO)
> - Distinction from process and repetitive manufacturing

---

## 2. Order Lifecycle and Status Management
> 🟠 Tier 2 · _Key points:_ CRTD, REL, PCNF/CNF, DLV, TECO, CLSD; system vs user status

### Definition
The order moves through **system statuses** which control what business transactions are allowed:

| Status | Meaning | Allows |
|---|---|---|
| **CRTD** | Created | Change, availability check; no goods movements or confirmation |
| **REL** | Released | Goods issue, confirmations, printing of shop papers |
| **GMPS** | Goods movement posted | (information) |
| **PCNF / CNF** | Partially / fully confirmed | More confirmations (PCNF) |
| **PDLV / DLV** | Partially / fully delivered | GR for finished product |
| **TECO** | Technically completed | No more movements; planned open reservations and capacity requirements dropped; WIP stops |
| **CLSD** | Business-completed (closed) | Settlement done; no more changes |
| **DLFL** | Deletion flag | Prepares archiving |

**User status** (via status profile) adds company-specific stops, e.g. "QC approval required" before release. Business transactions are allowed or forbidden depending on the combined statuses. Release: `CO05N` or in `CO02`; **TECO** and its reversal in `CO02` (technical completion can be reset); **closing** in `CO02`/`COHV` after settlement.

Lifecycle: create to release to issue to confirm to deliver to TECO to settle to close.

### Example
A pharma plant adds user status "QAREL" to the status profile: orders cannot be released until Quality has approved the master batch record. Status flow for order 1000812: CRTD (5 Oct) → REL (5 Oct) → PCNF (7 Oct) → CNF + DLV (12 Oct) → TECO (13 Oct) → settled and CLSD at month-end. Attempting a goods issue after TECO fails with "status TECO is set".

### In the news
See news box. Status-driven control stays unchanged in S/4HANA, while newer apps display the same statuses.

### Interview angle
> [!question] How it is asked
> "Explain order status management and what TECO does."

> [!tip] Strong answer includes
> - Ordered statuses and what each permits
> - System vs user status with a business example
> - TECO effects (stops WIP, drops open reservations) and reversibility vs CLSD
> - Link to month-end sequence

---

## 3. Release, Availability Check and Goods Issue: Manual vs Backflush
> 🟠 Tier 2 · _Key points:_ Component availability, 261, backflush indicators, pull list

### Definition
**Release** requires the **availability check** of components (and optionally capacity, PRT) at the configured check scope; releasing creates the order's shop papers and enables postings.

**Goods issue (GI)** of components to the order uses movement type **261** (reversal 262) in `MIGO` (or `MB1A`/`CO27` pick list). Two ways:
- **Manual (planned) issue:** stores issue components against the reservation before production starts. Gives visibility of component use and variances at issue; more transactions.
- **Backflush:** components are issued **automatically at confirmation** of the operation (or at GR for repetitive manufacturing) in proportion to the confirmed yield (+scrap). The backflush flag can be set: **material master** (MRP 2 view: always, never, work centre decides), **BOM item**, and **work centre**. Component must be assigned to an operation.

| Aspect | Manual issue | Backflush |
|---|---|---|
| Timing | Before/during production | At confirmation |
| Effort | High | Low |
| Accuracy of stock | Real consumption posted | Theoretical BOM consumption unless corrected |
| Variance visibility | At issue | Hidden unless actual consumption entered on confirmation |
| Best for | Expensive, batch/serial items, critical parts | Low-value, high-volume items (screws, washers) |

Batch-managed components need batch determination at backflush, and negative stock can occur when the physical stock was not received yet.

### Example
Order of 1,000 pieces uses 4,000 bolts at ₹12 (₹48,000, low-value) and 2,000 kg aluminium at ₹95 (₹1,90,000, valuable). Policy: bolts **backflushed** at operation 0020; aluminium issued **manually** via 261 for the batch with batch determination. At confirmation of 600 good pieces, backflush issues 2,400 bolts (₹28,800) automatically; the Dr production order / Cr stock posting follows the 261 accounting ([[190 SAP FI-CO Essentials for Operations Professionals]]).

### In the news
See news box. IDES24's note on rework after order completion matters because a rework often needs further component issues.

### Interview angle
> [!question] How it is asked
> "Backflush or manual goods issue: which one do you recommend and why?"

> [!tip] Strong answer includes
> - Movement type 261/262 and where the backflush flag is set
> - Pros and cons table (speed vs accuracy)
> - Criteria: value, batch/serial control, stock accuracy
> - Variance consequence and how to catch it (consumption reports, cycle counts)

---

## 4. Confirmation: CO11N and CO15
> 🟠 Tier 2 · _Key points:_ Yield, scrap, rework, activities, partial/final, auto GR, cancel

### Definition
A **confirmation** reports what was produced and which activities were consumed at an **operation**. `CO11N` confirms one operation (or order) and records:
- **Yield** (good quantity), **scrap** (with reason code), **rework quantity**;
- **Actual activities**: setup, machine and labour hours (these drive costing); **work start/end** dates;
- **Confirmation type:** partial (more to come), final (clears remaining requirements; sets CNF), and **no remaining work** flag.
- **Goods movements at confirmation:** backflush (261), optionally **automatic goods receipt**, batch entry.
`CO15` confirms at order header (yield and goods movements), `CO13` cancels a confirmation, `CORS` reverses, `COOIS` lists confirmations. **Reporting points** allow milestone-based backflush.

**Accounting effect:** activity consumption debits the order and credits the cost centre: **Dr Production order, Cr Cost centre (activity type)**: secondary cost postings, with no FI document unless profit centre or segment differs.

$$\text{Activity cost}=\text{hours confirmed}\times\text{activity price}$$

### Example
Operation 0010 machining: confirm 600 pieces yield, 8 scrap, 150 machine hours and 480 labour hours. Machine rate ₹600/h, labour ₹400/h: machine cost 150 × 600 = ₹90,000; labour 480 × 400 = **₹1,92,000**; production overhead 40% on labour = ₹76,800. The order is debited ₹90,000 + ₹1,92,000 + ₹76,800 = ₹3,58,800 and the machine and labour cost centres are credited by the activity amounts. Scrap of 8 pieces stays in the order cost, so the cost per good piece rises.

### In the news
See news box. Confirmation is the data source for shop-floor analytics, OEE and plant dashboards ([[018 Capacity Management & OEE]]).

### Interview angle
> [!question] How it is asked
> "What happens in SAP when you confirm a production order operation?"

> [!tip] Strong answer includes
> - Yield, scrap, rework and activity hours as inputs
> - Backflush and auto-GR effects; partial vs final confirmation
> - Accounting: order debited, cost centre credited at activity price
> - Reversal path and master-data dependencies (control key, work centre)

---

## 5. Goods Receipt, By-products and Co-products
> 🟠 Tier 2 · _Key points:_ 101 to stock, 531 by-product, co-product apportionment, standard price credit

### Definition
**Goods receipt (GR) from the production order** posts the finished product into stock with movement **101** (`MIGO`, reference order); partial deliveries are allowed with the delivery tolerance. Accounting: **Dr Finished goods stock (at standard price), Cr Production order** (valued at standard price S). Under MAP, the actual order cost is used.

**By-product** (low-value output that arises alongside the main product): modelled as a **negative component** in the BOM; GR with movement **531**. Its stock value credits the order, thus **reducing the main product cost**; value at its standard price or a net-realisable value.
**Co-products** (joint products of comparable value): modelled in a **co-product BOM**; the order costs are shared through an **apportionment structure** (percentages by quantity, value or other key), and each co-product is delivered with 101.

### Example
Sugar milling run with cost ₹10,00,000: 1,000 units of molasses by-product valued ₹200 each ₹2,00,000 credit (531: Dr By-product stock ₹2,00,000, Cr Order ₹2,00,000). Main product (sugar) bears **₹8,00,000** instead of ₹10,00,000, a 20% drop in its unit cost. For co-products A and B whose net realisable values are ₹14,00,000 and ₹6,00,000 (70 : 30), the joint cost ₹10,00,000 splits ₹7,00,000 / ₹3,00,000 via the apportionment structure.

### In the news
See news box. For process industries (chemicals, food, steel) joint-product costing drives pricing and is part of S/4HANA fit-to-standard workshops.

### Interview angle
> [!question] How it is asked
> "How do you cost by-products and co-products in SAP?"

> [!tip] Strong answer includes
> - Movement types 101 and 531 and the Dr/Cr
> - By-product as negative BOM item vs co-product apportionment
> - Effect on main-product cost with numbers
> - Valuation basis (standard price vs NRV)

---

## 6. Product Costing: BOM + Routing = Cost Estimate (CK11N)
> 🟠 Tier 2 · _Key points:_ Quantity structure, costing variant, costing sheet, cost components

### Definition
**Product cost planning** computes the planned cost of a material from its **quantity structure** (BOM quantities × price, routing operations × activity price) plus **overheads** from a **costing sheet**.

Inputs:
- **Material prices** (valuation of components: standard or MAP) and **activity prices** from the cost centres (`KP26`, `KSPI`).
- **BOM and routing** chosen by the **production version** (alternative BOM, alternative routing).
- **Costing lot size** (Costing 1 view) used to spread lot-fixed costs.
- **Costing variant** (e.g. PC01 for standard cost estimate; PPC1 for order planned costs) with the valuation variant that decides price sources, dates and the costing sheet.
- **Costing sheet** (overheads): surcharges such as material overhead % on material cost, production overhead % on labour; credit keys.
- **Cost components**: the output columns (raw material, labour, machine, overhead).

Transactions: `CK11N` (create cost estimate with quantity structure), `CK13N` (display), `CK40N` (costing run), `KKBC_ORD`/`CO03` for planned vs actual of an order.

### Example
Gear housing FG-500 (per piece): aluminium 2 kg × ₹95 = ₹190; bolts 4 × ₹12 = ₹48, so **material ₹238**. Machining 0.25 h × ₹600 = **₹150**; labour 0.8 h × ₹400 = **₹320**; production overhead 40% on labour = **₹128**. Total **₹836 per piece**. For a lot of 100 pieces the planned cost is ₹83,600; for the 1,000-piece order ₹8,36,000.

| Cost component | ₹ per piece | Share |
|---|---|---|
| Raw material | 238 | 28.5% |
| Machine | 150 | 17.9% |
| Labour | 320 | 38.3% |
| Overhead | 128 | 15.3% |
| **Total** | **836** | 100% |

### In the news
See news box. Because the Material Ledger is always active in S/4HANA, standard costs can be paired with actual costing for price pass-through.

### Interview angle
> [!question] How it is asked
> "How does SAP calculate the standard cost of a manufactured item?"

> [!tip] Strong answer includes
> - BOM + routing via production version, with price sources
> - Costing variant, costing sheet and cost components
> - Numeric roll-up with material, activity and overhead
> - Link to [[110 Cost Accounting for Operations]] and [[225 Budgeting, Variance Analysis & Balanced Scorecard]]

---

## 7. Standard Cost Estimate: Marking, Release and Revaluation
> 🟠 Tier 2 · _Key points:_ CK24, CK40N, future/current/previous price, inventory revaluation

### Definition
A cost estimate is only a calculation until it is **marked** and **released**:
1. **Cost** (CK11N for one item, `CK40N` run for many: select, BOM explosion, costing, **mark**, **release**).
2. **Mark:** stores the result as the **future planned price** in the material master Accounting 2 view (and the price valid from a start date).
3. **Release** (`CK24` for single, in the run for mass): copies the future price to the **standard price**; the old becomes **previous price**.
4. **Revaluation:** stock held at the old price is revalued: **Dr/Cr Inventory, Cr/Dr a price-change/revaluation account** (OBYC key PRD or UMB depending on process and configuration). With the Material Ledger the price change is also logged for multiple currencies.

Timing: standard costs are usually set once a year (before the budget), or when significant changes arise (new BOM, rates, commodity cost). Components must be released **before** their parents, hence costing in **low-level code** order.

### Example
1,000 finished pieces are in stock at the old standard ₹800. The new released standard is ₹836: revaluation = 1,000 × (836 − 800) = **₹36,000**, posted Dr Finished goods stock ₹36,000, Cr Price-change/revaluation ₹36,000 (P&L). Any WIP and later production variances will now be measured against ₹836.

### In the news
See news box. Commodity and wage inflation make annual standard-cost resets a regular finance and operations exercise.

### Interview angle
> [!question] How it is asked
> "What do marking and releasing a cost estimate mean?"

> [!tip] Strong answer includes
> - Cost, mark (future price), release (standard price) sequence
> - Costing run steps and low-level code order
> - Revaluation posting with a number
> - Frequency and governance

---

## 8. Planned vs Actual Costs and WIP Calculation
> 🟠 Tier 2 · _Key points:_ Plan/target/actual, WIP definition, KKAO, change in stock

### Definition
An order accumulates: **plan costs** (from the cost estimate at order creation), **target costs** (plan scaled to the quantity delivered), **actual costs** (issues, activities, overheads) and **commitments**.

**WIP (work in process)** at period end: for orders that are **released but not yet delivered/TECO**, WIP = **cumulative actual debits − cumulative credits (deliveries)**. It is capitalised on the balance sheet. `KKAO` (collective processing of production orders) calculates and posts WIP; the result is **Dr WIP (balance sheet), Cr Change in stock (P&L)**, reversed and recalculated next period. When an order is **delivered in full** (GR) or **TECO**, WIP is cancelled because the cost is now in stock or variance.

$$\text{WIP}=\sum\text{Actual debits}-\sum\text{Credits (GR at standard)}$$

### Example
Order 1000812 at month-end (day 20): full material issue ₹2,10,700 (aluminium at MAP) + ₹48,000 = ₹2,58,700. 60% of machining, labour and overhead is confirmed: ₹93,600 + ₹1,96,800 + ₹78,720 = ₹3,69,120. No GR yet. **WIP = ₹2,58,700 + ₹3,69,120 = ₹6,27,820**; posting Dr WIP ₹6,27,820, Cr Change in stock ₹6,27,820. This avoids an artificially low profit in the month where costs were incurred but no stock appeared. Next month the entry is reversed and, after GR, replaced by finished-goods stock.

### In the news
See news box. With the Universal Journal, WIP postings carry profit centre and segment, so segment balance sheets include WIP automatically.

### Interview angle
> [!question] How it is asked
> "What is WIP in SAP and how is it calculated at month-end?"

> [!tip] Strong answer includes
> - Plan, target, actual cost vs commitments
> - WIP = debits − credits for open orders; posting entry
> - Cancellation when delivered or TECO
> - Why it matters: matching revenue and cost, balance-sheet accuracy

---

## 9. Variance Categories at Production-Order Level
> 🟠 Tier 2 · _Key points:_ Input price, input quantity, resource usage, lot size, mixed price, output price, remaining, scrap

### Definition
At period end (`KKS1` collective, `KKS2` single) SAP compares **target cost** (what the delivered quantity should have cost at standard) with **actual cost** and splits the difference into categories:

| Category | Plain English | When it arises |
|---|---|---|
| **Input price variance** | Paid a different price for the same thing | Component valued at MAP/actual differs from standard; activity at different price |
| **Input quantity variance** | Used more or fewer units than the recipe | Extra material, longer machine or labour time |
| **Resource-usage variance** | Used a different material or activity than planned | Substitute component, different work centre |
| **Input lot-size variance** | Fixed costs spread differently | Order lot differs from the costing lot size (setup) |
| **Output price variance / mixed price variance** | Output valued differently from standard or mixed prices | GR valued with a different price, multiple inputs/outputs |
| **Scrap variance** | Loss beyond the planned scrap | Scrap higher or lower than planned in the costing |
| **Remaining variance** | Unexplained difference | Items the system cannot allocate |

Formulas (all per component or activity):
$$\text{Price var}=(P_{act}-P_{std})\times Q_{act}\qquad \text{Qty var}=(Q_{act}-Q_{target})\times P_{std}$$
Positive = unfavourable (actual above target). The theory is in [[225 Budgeting, Variance Analysis & Balanced Scorecard]].

### Example
Order of 1,000 pieces at standard ₹836 (target ₹8,36,000).

| Item | Target | Actual | Variance |
|---|---|---|---|
| Aluminium | 2,000 kg × ₹95 = 1,90,000 | 2,150 kg × ₹98 = 2,10,700 | 20,700 |
| Bolts | 4,000 × ₹12 = 48,000 | 4,000 × ₹12 = 48,000 | 0 |
| Machine | 250 h × ₹600 = 1,50,000 | 260 h × ₹600 = 1,56,000 | 6,000 |
| Labour | 800 h × ₹400 = 3,20,000 | 820 h × ₹400 = 3,28,000 | 8,000 |
| Overhead (40% of labour) | 1,28,000 | 1,31,200 | 3,200 |
| **Total** | **8,36,000** | **8,73,900** | **37,900** |

Split: **input price** = (98 − 95) × 2,150 = **₹6,450**; **input quantity** = aluminium (2,150 − 2,000) × 95 = ₹14,250 + machine ₹6,000 + labour ₹8,000 + overhead ₹3,200 = **₹31,450**. Total ₹6,450 + ₹31,450 = ₹37,900 ✓. Actual cost per piece ₹873.90 is 4.5% above standard. **Lot-size variance** illustration: a ₹5,000 fixed set-up costed on a 100-piece lot is ₹50 a piece; an order of 1,000 pieces pays one set-up but absorbs 1,000 × 50 = ₹50,000, a **favourable ₹45,000** lot-size variance.

### In the news
See news box. IDES24 reports faster closing for the Universal Journal; variance calculation is among the steps expected to run more quickly.

### Interview angle
> [!question] How it is asked
> "Name the variance categories on a production order and calculate price and quantity variance for this data."

> [!tip] Strong answer includes
> - Input price, input quantity, resource usage, lot size, output/mixed price, scrap, remaining
> - Correct formulas and sign convention with a worked table
> - Link between cause (MAP price, over-consumption) and category
> - Operations remedy per category (sourcing, scrap reduction, set-up)

---

## 10. Settlement and Journal Entries
> 🟠 Tier 2 · _Key points:_ KO88, settlement rule, variance to P&L or stock, price control S vs V

### Definition
**Settlement** clears the production order balance after delivery/TECO. The **settlement rule** (created from the production version or the material master) names the receiver: the **material** (for MAP-controlled finished goods), a **cost centre**, a G/L account or profit-and-loss account. With **standard price control (S)** the difference is a variance and goes to **production-variance accounts** in P&L (by variance category when so configured); with **MAP (V)** the order is settled to stock. Execute with `KO88` (individual order) or `CO88` (collective processing of production orders).

Sequence: **GR at standard (credit)** → **variance calculation** (`KKS1`) → **settlement** (`KO88`) → order balance zero. With the **Material Ledger**, variances may be further pushed into inventory and COGS at actual-costing close.

### Example
Journal entries for order 1000812:
1. Issues and activities: **Debits** ₹8,73,900 (components ₹2,58,700; machine ₹1,56,000; labour ₹3,28,000; overhead ₹1,31,200).
2. GR 1,000 pieces at standard ₹836: Dr Finished goods ₹8,36,000, Cr Order ₹8,36,000.
3. Order balance = ₹37,900 debit. Settlement: **Dr Production variance (P&L) ₹37,900, Cr Production order ₹37,900**: split ₹6,450 input price and ₹31,450 input quantity.
If the finished piece were MAP-valued, the ₹37,900 would be added to stock instead (new MAP higher by about ₹37.90 per piece for the 1,000 pieces).

### In the news
See news box. The real-time FI-CO integration of the Universal Journal means that the settlement postings are visible instantly in profit-centre and segment reports.

### Interview angle
> [!question] How it is asked
> "What happens at production order settlement? Where do the variances go for a standard-price material?"

> [!tip] Strong answer includes
> - Settlement rule, receiver, `KO88`
> - Standard (variance to P&L) vs MAP (to stock)
> - Full entry chain: issues, GR at standard, settlement
> - Role of the material ledger for actual costs

---

## 11. TECO, Business Completion and the Order Closing Sequence
> 🟠 Tier 2 · _Key points:_ TECO vs CLSD, WIP cancellation, open reservations, sequence

### Definition
- **Technical completion (TECO):** the order is finished from a production standpoint. Open component reservations are deleted, capacity requirements dropped, WIP is cancelled, and no further confirmations or goods issues are possible unless TECO is reset (`CO02`). Open GR for the delivered quantity must be completed first.
- **Business completion (CLSD):** the order is financially closed after settlement; used before archiving.
- **Recommended sequence:** (1) final confirmation and GR; (2) check/adjust consumptions (`COOIS`, `MB51`); (3) **TECO** (`CO02` or `COHV`); (4) **variance calculation** `KKS1`; (5) **settlement** `KO88`; (6) **close** CLSD; (7) set deletion flag and archive.
- **Common issues:** premature TECO then late postings fail; forgetting to TECO leaves WIP on the books; unsettled orders break the material-ledger close.
- **Mass tools:** `COHV` processes release, TECO, close for many orders using selection and variants.

### Example
A plant has 300 orders delivered in September. Controller runs `COHV` with variant "Delivered, not TECO", sets TECO and the "Close" step after settlement. Result: WIP of ₹1.4 crore on those orders drops to zero in October, and the variances (₹6.2 lakh) land in P&L. Four orders cannot be TECO'd because an open reservation for a batch-managed component is blocking: the planner removes it and retries. (Illustrative numbers.)

### In the news
See news box. IDES24 notes rework even after completion in the 2025 release, hinting at changed TECO handling; confirm exact behaviour in your release.

### Interview angle
> [!question] How it is asked
> "What is the difference between TECO and CLSD, and why does closing orders matter for finance?"

> [!tip] Strong answer includes
> - TECO effects and reversibility vs CLSD
> - Closing sequence: confirm, GR, TECO, variance, settle, close
> - Impact on WIP and variance accuracy
> - Mass processing and exceptions

---

## 12. Rework and Scrap
> 🟠 Tier 2 · _Key points:_ Rework quantity, rework order, scrap in costing, cost visibility

### Definition
- **Scrap** is output that cannot be used. In **confirmation** (`CO11N`) enter scrap quantity and reason; costs already incurred stay on the order and are spread over good output (higher cost per good piece). **Component scrap %** in the BOM and **assembly scrap %** in MRP plan for expected losses so MRP issues extra material; actual excess is quantity variance.
- **Rework** repairs defective units to usable quality. Options: (a) **rework quantity** confirmed in the original order (additional operations or repeat of an operation), (b) a separate **rework order** with its own cost collection, (c) **rework operation** in the routing for planned rework. Rework consumes extra labour/machine time and sometimes components.
- **Cost visibility:** rework in the original order increases input quantity variance. A separate rework order collects its cost and settles it to the original order or to a quality-cost account so quality cost can be tracked ([[011 Quality Management (TQM)]]).
- **Scrap in S/4HANA:** the PEO engine described by IDES24 supports comprehensive rework, including after completion and for purchased parts.

### Example
Order 1000812: 40 housings fail inspection and are reworked (0.4 h labour, 0.2 h machine each). Rework labour: 40 × 0.4 × ₹400 = **₹6,400**; machine: 40 × 0.2 × ₹600 = **₹4,800**; total **₹11,200**, or ₹280 per reworked piece (≈ 33% of the standard cost of ₹836). Over 1,000 pieces, a 4% rework rate adds about ₹11.2 per good piece (1.3%); a plant with 20% rework would add nearly ₹56 per piece, so rework rate belongs on the quality scorecard.

### In the news
See news box. IDES24's report of a rework enhancement in the 2025 release suggests rework handling is still a pain point for manufacturers.

### Interview angle
> [!question] How it is asked
> "How do you handle scrap and rework in SAP production and how do they affect cost?"

> [!tip] Strong answer includes
> - Scrap confirmation and its cost spreading; scrap % in BOM/MRP
> - Rework options: same order, rework order, rework operation
> - Variance impact with numbers
> - Quality-cost reporting and root-cause links (six sigma)

---

## 13. Plain-English Glossary of Production and Costing Terms
> 🟠 Tier 2 · _Key points:_ Decode the jargon in one table

### Definition
| SAP term | Plain English |
|---|---|
| **Order type** | The template that tells the system how a type of order behaves (numbering, costing, settlement) |
| **Production version** | The "recipe choice": which BOM and routing to use for a given lot size and date |
| **Routing** | The ordered list of operations (steps), work centres and standard times |
| **Operation** | One step in the routing, e.g. machining |
| **Work centre** | A machine or labour group where an operation is performed; links to a cost centre |
| **Activity type** | A measurable service of a cost centre (machine hour, labour hour) with a price |
| **Reservation** | A promise of components for the order, not yet issued |
| **Backflush** | Issue of components automatically when you report production |
| **Confirmation** | Reporting what has been made and how long it took |
| **Planned/target/actual cost** | What it should cost, what it should have cost for what was made, what it did cost |
| **Costing lot size** | The batch size on which standard cost is calculated |
| **Costing sheet** | The formula that adds overhead to direct costs |
| **WIP** | Costs spent on orders not yet delivered, shown as an asset |
| **TECO** | "Technically complete": nothing more will be made on this order |
| **Settlement** | Moving the final order balance (variances) to the right accounts |
| **Variance** | Difference between standard and actual cost |
| **Standard price (S)** | A fixed valuation price; differences go to variance accounts |
| **Moving average price (V)** | A price that moves with each receipt |
| **Material Ledger** | A sub-ledger that tracks stock value by period and calculates actual cost |
| **By-product** | A secondary output; its value reduces the main cost |

### Example
Reading a shop-floor message "Order 1000812 REL PCNF GMPS: operation 0020 confirm" in plain English: the order is released, partly reported complete, goods have been issued, and now the assembly step is being reported. Explaining it this way is a strong interview habit with HR/finance panels who are not SAP experts.

### In the news
See news box. As SAP projects move to cloud, explaining terms in plain English to business users is a core consulting skill ([[162 Structured Communication - SCQA, Storylines & Case Delivery]]).

### Interview angle
> [!question] How it is asked
> "Explain a production order and its costing to a CFO who has never used SAP."

> [!tip] Strong answer includes
> - Analogies: job card and cost account
> - Short flow: plan, issue, confirm, deliver, settle
> - One numeric example of variance
> - No jargon without translation

---

## 14. ⭐ Advanced: S/4HANA Costing, Material Ledger and Production Changes
> ⭐ Advanced · _Added beyond the tracker_

### Definition
What changes for production execution and costing on S/4HANA:
- **Universal Journal (ACDOCA):** order postings, activity allocations and variances carry cost centre, profit centre and segment on each line, and **no reconciliation ledger** is needed between FI and CO ([[190 SAP FI-CO Essentials for Operations Professionals]]).
- **Material Ledger always on:** standard-price materials accumulate price and exchange-rate differences, the **actual costing run (`CKMLCP`)** can compute **periodic unit prices** and revalue consumption and closing stock up the BOM (multilevel). Variances from production orders flow through the ML when actual costing is active.
- **Multiple valuations (parallel currencies/legal vs group/profit-centre views)** allow different cost bases for transfer pricing and group reporting.
- **Order execution:** `CO01`/`CO11N` remain in on-premise; newer Fiori apps (such as Confirm Production Operation and manufacturing-order apps) and the **PEO** engine in cloud editions provide a leaner model, including the rework options cited by IDES24.
- **Predictive and event-driven planning/execution:** IDES24 lists event-driven planner notifications and tighter IBP integration in 2025.
- **Conversion tasks:** reconcile ML history, review settlement profiles, test `KKS1`/`KO88`, and retest custom variance reports.

### Example
Aluminium price rises mid-month: purchases at ₹98 versus standard ₹95. Under standard costing without actual costing, the ₹3/kg gap appears as input price variance on each order and as price difference at GR. With **actual costing**, the ML calculates a periodic unit price (say ₹96.5) for the month, revalues consumption (e.g. 40,000 kg × (96.5 − 95) = ₹60,000) and passes the revaluation to finished-goods COGS and stock in proportion, so the cost of sales shows the true cost of aluminium, not an unexplained P&L variance.

### In the news
See news box. The ECC deadline (2027/2030) is what turns these changes from options into migration scope.

### Interview angle
> [!question] How it is asked
> "What are the main costing and production changes when moving from ECC to S/4HANA?"

> [!tip] Strong answer includes
> - Universal Journal and no reconciliation ledger
> - Material Ledger mandatory, actual costing optional with multilevel pass-through
> - Execution apps and rework/PEO developments, framed as vendor-described
> - Test scope for conversion: settlement, variance, ML close ([[200 SAP S-4HANA Migration, Data Migration & Testing]])
