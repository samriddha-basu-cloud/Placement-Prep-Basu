---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Inventory Valuation, Cycle Counting & Inventory Governance"
tier: Tier 2
roles: Operations / Finance
status: complete
subtopics: 14
---
# Inventory Valuation, Cycle Counting & Inventory Governance

⬅ [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[117 Demand-Driven MRP (DDMRP) & Buffer Management]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Finance

## Sub-topics in this note
1. [[#1. Why Inventory Valuation and Control Matter]]
2. [[#2. Cost Flow Methods: FIFO, Weighted Average, LIFO]]
3. [[#3. Standard Costing, Variances and Costing in ERP]]
4. [[#4. Ind AS 2: Cost, NRV Write-Downs and Reversals]]
5. [[#5. Obsolescence and Excess Provisioning]]
6. [[#6. FEFO and Shelf-Life Management]]
7. [[#7. Physical Counts: Wall-to-Wall vs Cycle Counting]]
8. [[#8. ABC-Based Count Frequency and Count Planning]]
9. [[#9. Record Accuracy (IRA) and Shrinkage]]
10. [[#10. GMROI and Inventory Days by Segment]]
11. [[#11. Inventory Policy by Segment (ABC-XYZ)]]
12. [[#12. Audit Trails and Inventory Governance]]
13. [[#13. Inventory Reduction Playbook with Worked Numbers]]
14. [[#14. ⭐ Advanced: GST on Write-offs, Valuation of Consignment and Third-Party Stock]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): shelf-life rules, shrink and the end of LIFO-style thinking
> **FSSAI sets minimum shelf life at delivery for online food (November 2024).** FSSAI told e-commerce and quick-commerce food operators to ensure "a minimum shelf life of 30 per cent or at least 45 days before products expire at the time of delivery", in a meeting with more than 200 platforms and industry bodies including Blinkit and Zepto. Dark stores and DCs now need FEFO discipline and expiry-aware replenishment, or stock becomes undeliverable. ([Business Standard](https://www.business-standard.com/industry/news/fssai-to-online-fbos-ensure-minimum-shelf-life-of-45-days-before-expiry-124111201488_1.html); [All India Radio / newsonair](https://www.newsonair.gov.in/fssai-directs-e-commerce-fbos-to-ensure-minimum-30-shelf-life-for-delivered-products-to-enhance-food-safety-standards))
>
> **US retail shrink hit 1.6% of sales (FY2022 data, reported 2023-24).** The NRF survey put shrink at 1.6% of sales in 2022 (1.4% in 2021), or $112.1 billion; Retail Dive noted that more than a third of shrink was administrative, not theft. In October 2024 the NRF said it would stop publishing the broad annual shrink report and focus on theft and violence instead, so no newer like-for-like benchmark exists. ([Retail Dive](https://www.retaildive.com/news/retailers-crime-problem-numbers/699107); [TheStreet](https://www.thestreet.com/retail/nrf-pauses-theft-reporting))
>
> **Accounting rule check (KPMG, June 2026).** KPMG's IFRS vs US GAAP comparison restates that IAS 2 (on which India's Ind AS 2 is based) prohibits LIFO because it "does not faithfully represent" inventory flow, allows only FIFO or weighted average (standard cost and retail methods if they approximate cost), measures inventory at the lower of cost and NRV, and requires reversal of earlier write-downs (up to original cost) when value recovers. ([KPMG](https://kpmg.com/us/en/articles/2026/inventory-accounting-ifrs-accounting-standards-vs-us-gaap.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Why Inventory Valuation and Control Matter
> 🟠 Tier 2 · _Key points:_ Balance-sheet asset, COGS driver, control risk

### Definition
Inventory is typically the largest current asset of a manufacturer or retailer, and its **valuation** feeds two statements at once: closing stock sits on the balance sheet and the cost of units sold hits the P&L:

$$COGS = \text{Opening stock} + \text{Purchases (and conversion)} - \text{Closing stock}$$

Any error in closing stock flows one-for-one into profit. Two questions are therefore always separate: **how many units exist** (existence and record accuracy, a control problem) and **at what rupee value** each is carried (valuation, an accounting problem). Operations owns the first, Finance the second, and **inventory governance** is the set of rules, counts, approvals and audit trails that keeps both honest. Link this note to [[003 Inventory Management]] (policy), [[108 Financial Statements & Ratios]] (ratios) and [[110 Cost Accounting for Operations]] (costing).

### Example
Closing stock is overstated by ₹5 crore because a warehouse count missed a damaged lot. COGS is understated by ₹5 crore, so pre-tax profit is overstated by ₹5 crore; at a 25% tax rate this triggers about ₹1.25 crore of tax too early, and next year's profit is understated by the same amount (the error reverses). Banks lending against stock (drawing power under working capital limits) are also misled.

### In the news
See news box. The FSSAI shelf-life rule and the NRF shrink data show the two faces of the problem: stock that exists but cannot be sold, and stock that is on the books but no longer physically there.

### Interview angle
> [!question] How it is asked
> "Why should an operations manager care how inventory is valued?"

> [!tip] Strong answer includes
> - Inventory valuation moves profit, tax, covenants and bank drawing power
> - Separates quantity accuracy (operations) from value (finance)
> - Names the controls: counts, cut-off, approvals, audit trail
> - Links to cash: every day of inventory reduced releases COGS/365 of cash

---
## 2. Cost Flow Methods: FIFO, Weighted Average, LIFO
> 🟠 Tier 2 · _Key points:_ India has no LIFO; method changes profit not cash flow

### Definition
- **FIFO**: oldest purchases are assumed sold first, so closing stock is valued at the **latest** costs.
- **Weighted average (WAC)**: cost per unit = (cost of opening stock + purchases) / (units available). In a perpetual system the average is recomputed after each receipt (**moving average**).
- **LIFO**: newest costs are assumed sold first. **Not permitted** under Ind AS 2 / IAS 2 (and the older Indian AS 2); India's income-tax valuation standard ICDS II likewise limits cost formulas to FIFO and weighted average. LIFO survives mainly under US GAAP, where it can defer tax in a rising-price market.
- **Specific identification** is required for items that are not interchangeable (a jewellery piece, a project-specific part). Ind AS 2 expects the **same formula** for inventories of a similar nature and use.

Direction of effect when prices rise: FIFO gives the lowest COGS and highest profit and stock value; LIFO the opposite; weighted average sits between. Total cash is identical; only the allocation between P&L and balance sheet differs.

### Example
Opening stock 100 units at ₹50; purchases 200 at ₹56 then 300 at ₹60; 350 units sold at ₹90. Cost of goods available = 5,000 + 11,200 + 18,000 = ₹34,200 for 600 units; closing stock 250 units. Revenue = ₹31,500.

| Method | COGS | Closing stock | Gross profit | GM % |
|---|---|---|---|---|
| FIFO | ₹19,200 | ₹15,000 | ₹12,300 | 39.0% |
| Weighted average (₹57.00) | ₹19,950 | ₹14,250 | ₹11,550 | 36.7% |
| LIFO (shown for contrast only) | ₹20,800 | ₹13,400 | ₹10,700 | 34.0% |

FIFO's closing stock is 250 × ₹60 = ₹15,000, matching current replacement cost; that is why FIFO balance sheets look closest to reality when prices move.

### In the news
See news box. KPMG's June 2026 restatement of the IAS 2 rule is a reminder that Indian companies, using Ind AS 2, choose between FIFO and weighted average only, so "LIFO vs FIFO tax benefit" arguments from US textbooks do not apply.

### Interview angle
> [!question] How it is asked
> "Prices of steel are rising. Which inventory method gives higher profit and why? Does India allow LIFO?"

> [!tip] Strong answer includes
> - FIFO gives higher profit in inflation; WAC smooths; LIFO barred in India
> - Compute a quick table as above, and note that cash flow is unchanged
> - Physical flow need not equal cost flow, but FEFO/FIFO physical handling is still good practice
> - Mention consistency, disclosure of the formula, and the same formula for similar items

---
## 3. Standard Costing, Variances and Costing in ERP
> 🟠 Tier 2 · _Key points:_ Standard price, PPV, price control S vs V

### Definition
**Standard cost** is a pre-set cost per unit (material, labour, overhead) revised periodically, typically yearly. Ind AS 2 allows it if it approximates actual cost and is reviewed regularly. Inventory is carried at standard; differences are captured as variances:

$$PPV = (\text{Standard price} - \text{Actual price}) \times \text{Quantity purchased}$$

(positive = favourable). Further variances: usage (quantity), labour rate and efficiency, overhead absorption. At period-end variances are either expensed to COGS or, if material, apportioned between COGS and closing stock so that inventory is not carried far from actual cost.

In **SAP**, the material master has a **price control**: **S** (standard price; goods receipts post at standard, the gap goes to a price-difference account) or **V** (moving average; the price floats with each receipt). Standard price changes are revalued with a price change document (MR21); the Material Ledger (CKM3 for price analysis) supports actual costing. See [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]], [[194 SAP Production Execution, Confirmation & Product Costing]] and [[190 SAP FI-CO Essentials for Operations Professionals]].

### Example
Standard price ₹58/unit. Receipts: 200 units at ₹56 (favourable ₹2 × 200 = ₹400) and 300 units at ₹60 (unfavourable ₹2 × 300 = ₹600). Net PPV = **₹200 unfavourable**. A purchasing manager judged on PPV alone is tempted to buy cheap in bulk; that inflates stock, so PPV must be read with days of inventory and quality cost.

### In the news
See news box. IAS 2 explicitly permits standard cost and the retail method only when results approximate cost, so a large unexplained PPV balance is an audit flag in Ind AS reporting.

### Interview angle
> [!question] How it is asked
> "What is the difference between standard cost and moving average, and what does a growing purchase price variance tell you?"

> [!tip] Strong answer includes
> - Definitions and SAP price control S vs V
> - PPV formula and sign convention
> - Variance causes: market price, wrong standard, spot buys, freight, wrong UoM
> - Why standards must be re-based (inflation, FX) and variances apportioned when material

---
## 4. Ind AS 2: Cost, NRV Write-Downs and Reversals
> 🟠 Tier 2 · _Key points:_ Lower of cost and NRV, item by item, reversal allowed

### Definition
Ind AS 2 (converged with IAS 2) measures inventory at the **lower of cost and net realisable value**.

**Cost** = purchase price (net of trade discounts, plus import duties and **non-recoverable** taxes, freight, handling) + conversion cost (direct labour and a systematic allocation of production overhead; fixed overhead allocated on **normal capacity**) + other costs to bring the item to its present location and condition. Excluded from cost: abnormal waste, storage not needed for production, administrative overheads, selling costs. GST that is recoverable as ITC is **not** part of cost.

**NRV** = estimated selling price in the ordinary course of business − estimated costs of completion − estimated costs necessary to make the sale. Rules: write down **item by item** (or groups of similar items); raw materials are not written down if the finished goods they go into are expected to sell at or above cost; if circumstances improve, the write-down is **reversed up to the original cost** (unlike US GAAP). Write-downs and reversals are recognised in the period and disclosed.

$$\text{Carrying amount} = \min(\text{Cost},\; NRV), \qquad NRV = SP - C_{complete} - C_{sell}$$

### Example
A handset model costs ₹1,000 per unit; expected selling price ₹1,200, discounting needed to clear stock; costs to complete (re-packaging) ₹150, selling costs ₹100. NRV = 1,200 − 150 − 100 = **₹950**, so write down ₹50 per unit. For 40,000 units the P&L charge is ₹20 lakh. If a later festive season lifts the expected price so that NRV is ₹1,080, the write-down is reversed to cost (₹1,000), reversing the full ₹20 lakh. Contrast with the ₹2 crore stock of [[003 Inventory Management]] (sub-topic 11): cost ₹2.0 crore, NRV ₹60 lakh, write-down ₹1.4 crore.

### In the news
See news box. The reversal rule in the KPMG comparison is the practical difference from US GAAP, relevant when an Indian subsidiary reports to a US parent.

### Interview angle
> [!question] How it is asked
> "Inventory has not moved for 18 months. What does the accounting standard require and who decides the value?"

> [!tip] Strong answer includes
> - Lower of cost and NRV with the NRV formula
> - Evidence for NRV: subsequent sales, quotes, liquidation recoveries, not a guess
> - Role of operations (age, demand, spec changes) and finance (judgement, auditor review)
> - Reversal permitted; disclosure of write-downs

---
## 5. Obsolescence and Excess Provisioning
> 🟠 Tier 2 · _Key points:_ Aging matrix, forward-demand test, SKU-level evidence

### Definition
Provisioning converts the operational view (slow, excess, obsolete) into an accounting charge. Two common methods:
1. **Aging matrix**: apply percentages to stock by age since last movement or receipt. Simple and auditable, but percentages must be backed by history of actual liquidation recoveries.
2. **Forward-demand (coverage) test**: for each SKU, quantity above *N* months of forecast demand (and its shelf-life limit) is provided at the difference between cost and realisable value. More accurate; needs a reliable forecast and fewer SKUs than a matrix.

Add specifics for **expiry** (provide 100% when expired or when remaining shelf life cannot meet customer minimums), **engineering change** (revision superseded), **customer-specific** stock (check contract buy-back) and **vendor return rights**. Provisions are estimates reviewed every quarter; consistent under-provisioning followed by sudden large write-offs is a classic red flag in audit. Keep the operational definitions of dead and obsolete stock from [[003 Inventory Management]] aligned with the accounting policy.

### Example
Stock of ₹13.5 crore by age: 0-90 days ₹8.0 cr (0% provision), 91-180 days ₹3.0 cr (10%), 181-365 days ₹1.5 cr (30%), above 365 days ₹1.0 cr (60%). Provision = 0 + 0.30 + 0.45 + 0.60 = **₹1.35 crore**, i.e. 10% of the total. If last year's liquidations of over-365-day stock actually recovered only 20% of cost, the 60% provision is too light (needs 80%), adding ₹0.20 crore.

### In the news
See news box. For quick-commerce, the FSSAI delivery rule effectively shortens the saleable life of food SKUs, so provisioning has to be tied to remaining shelf life, not just age since receipt.

### Interview angle
> [!question] How it is asked
> "How would you decide the provision for slow-moving stock at year-end?"

> [!tip] Strong answer includes
> - Aging-matrix and demand-coverage approaches with their trade-offs
> - Historic recovery data to calibrate percentages
> - Cross-check with FSN, expiry and engineering-change lists
> - Governance: quarterly review, finance sign-off, link to the sales and procurement KPIs that caused the excess

---
## 6. FEFO and Shelf-Life Management
> 🟠 Tier 2 · _Key points:_ First-expired-first-out, remaining shelf life, expiry risk

### Definition
**FEFO** issues the batch with the nearest expiry date first, regardless of receipt date; **FIFO** issues by receipt date. They differ when batches arrive out of expiry order (a new lot with a shorter life). Needed for food, pharma, chemicals, cosmetics, batteries and paint.

Key terms: **total shelf life** (manufacture to expiry), **remaining shelf life (RSL)** at receipt and at delivery, **minimum RSL** agreed with the customer (often 60-75% of life in modern trade; e-commerce food in India needs at least 30% or 45 days per FSSAI's November 2024 direction), and **expiry risk**: stock for which days of cover exceed RSL.

$$\text{Days of cover} = \frac{\text{Stock}}{\text{Average daily demand}}, \qquad \text{At risk} = \text{Stock} - d \times RSL$$

Controls: batch-managed stock with expiry dates in the WMS/ERP (SAP batch management with shelf-life data, see [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]] and [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]]), receiving rules that reject lots below minimum RSL, picking logic that enforces FEFO, near-expiry markdown or channel transfer triggers, and a weekly expiry report. See [[133 Food, Agri & Perishables Supply Chain - India]] and [[132 Pharma & Healthcare Supply Chain]].

### Example
A packaged snack has a 180-day shelf life; a retailer demands at least 60% RSL at delivery (108 days). The lot reaches the DC on day 30 (RSL 150 days, 83%). It must ship by day 180 − 108 = **day 72**, a 42-day window; after that it can only serve channels with lower minimums (discounters, institutional). Separately, 12,000 units with demand of 100/day and only 90 days of RSL: days of cover 120, at-risk stock = 12,000 − 100 × 90 = **3,000 units**.

### In the news
See news box. The FSSAI direction turns shelf-life policy into a regulatory minimum for online sellers, making RSL-aware allocation a compliance matter.

### Interview angle
> [!question] How it is asked
> "A dark store keeps expiring dairy and packaged foods. How do you cut the wastage?"

> [!tip] Strong answer includes
> - FEFO picking and RSL-based receiving and allocation rules
> - Demand-based replenishment with shelf-life caps on order quantity
> - Markdown ladders and transfers before expiry, wastage KPI (% of sales)
> - Supplier terms: minimum RSL at dispatch, return/credit for short-dated lots

---
## 7. Physical Counts: Wall-to-Wall vs Cycle Counting
> 🟠 Tier 2 · _Key points:_ Annual shutdown count vs continuous counting

### Definition
- **Wall-to-wall (periodic) physical inventory**: all stock counted on one date, usually with operations stopped. Gives an auditor-friendly point-in-time figure, but disrupts operations, relies on a rushed team, and errors found cannot be traced back to causes.
- **Cycle counting**: a rolling programme in which a subset of items or locations is counted every day; each item is counted at a frequency set by its class. Counting is **continuous**, discrepancies are investigated while records are fresh, and root causes are fixed. If the programme is statistically strong and the ERP is reliable, auditors can accept it in place of a full count; in India, check the audit view under SA 501 and company policy.
- Count methods: **blind count** (counter does not see the book quantity), **by location** (locations, then SKU in location), **by SKU**, **opportunity counts** (when a bin reaches zero, at receipt or when an error is reported).

SAP: physical inventory documents are created (MI01), counts entered (MI04) and differences posted (MI07); cycle counting uses indicators set per material (OMCO) with MICN creating the documents.

### Example
A 5,000-SKU warehouse running a wall-to-wall count every March needs 2 days of shutdown: with sales ₹20 lakh a day and 15% margin, lost contribution is about 2 × ₹3 lakh = ₹6 lakh plus overtime, and inaccuracy builds for 12 months. A cycle-count programme needs about 60 counts a day with two counters (calculation in the next sub-topic) and no shutdown; the full-count gap becomes a quarterly sample check.

### In the news
See news box. NRF's note that over a third of shrink is administrative shows why counts that locate process errors (receiving, UoM, putaway) beat counts that only find the total.

### Interview angle
> [!question] How it is asked
> "Should this warehouse switch from an annual physical count to cycle counting? What would you check?"

> [!tip] Strong answer includes
> - Pros and cons of both approaches, with cost of shutdown
> - Prerequisites: WMS/ERP with location control, discipline in posting, trained counters
> - Auditor acceptance and a residual statistical or year-end check
> - Counting rules: blind, recount above tolerance, freeze movements for counted bins

---
## 8. ABC-Based Count Frequency and Count Planning
> 🟠 Tier 2 · _Key points:_ A counted often, tolerances by class, daily count load

### Definition
Count frequency is set by class: A items (high value, ~70-80% of value) counted most often, C least. Frequencies are policy choices, not laws; typical illustrations are A monthly (12 per year), B quarterly (4), C yearly (1). Daily load:

$$\text{Counts per day} = \frac{\sum_{k} N_k f_k}{\text{Working days}}$$

with $N_k$ items in class $k$ and $f_k$ counts per year. Add triggers: items with prior errors (count again), high theft risk (the HML idea in [[003 Inventory Management]]), vital spares (VED) and any item whose book quantity is zero or negative. **Tolerances** are tighter for A (e.g. 0-1% or value-based) and looser for C. Use **ABC** from [[003 Inventory Management]] for frequency and **ABC value** for approval thresholds.

### Example
5,000 SKUs: 500 A items counted 12 times, 1,500 B items 4 times, 3,000 C items once. Annual counts = 6,000 + 6,000 + 3,000 = 15,000; over 250 working days that is **60 counts a day**. If one counter does 30 bin counts a shift, two counters suffice. Compared with a single wall-to-wall count (5,000 counts), each A item is counted 12 times a year but the 500 A items hold ~75% of value, so value coverage is far better than a once-a-year view.

### In the news
See news box. After 2022's shrink peak, retailers pointed counting effort at high-risk, high-value lines rather than counting everything equally.

### Interview angle
> [!question] How it is asked
> "Design a cycle-count schedule for a spare-parts store with 8,000 SKUs."

> [!tip] Strong answer includes
> - Classify by ABC, VED and HML, then set frequency per class
> - Daily workload arithmetic and staffing
> - Tolerance bands, recount rule, approval levels by variance value
> - Trigger counts (zero-stock, error history) and root-cause closure

---
## 9. Record Accuracy (IRA) and Shrinkage
> 🟠 Tier 2 · _Key points:_ Gross vs net variance, accuracy by count, shrink drivers

### Definition
**Inventory record accuracy (IRA)** = share of counted SKUs or locations where the system quantity matches the physical quantity within tolerance:

$$IRA = \frac{\text{Locations (or SKUs) within tolerance}}{\text{Locations (or SKUs) counted}}$$

World-class operations aim for 98-99%+; below ~95% planning tools (MRP, replenishment, ATP) start to produce false signals: phantom stock hides stock-outs, and invisible stock triggers excess orders. Report **net variance** (overages offset shortages) *and* **gross (absolute) variance**, because a small net figure can hide large errors. **Shrinkage** = book stock minus physical stock, caused by theft (internal, external, vendor), administrative error (receiving, UoM, pricing, wrong picks, unposted scrap) and damage or spoilage.

Typical root causes: receiving without a PO check, unit-of-measure mismatch, picking from the wrong bin, unrecorded returns and scrap, transfers not confirmed, unsupervised access. Data quality is the foundation (see [[175 Data Quality, Master Data & Data Governance]]). RFID can lift accuracy: American Eagle reports accuracy moving from 95% to 99% (NRF blog), a vendor-reported case rather than a benchmark.

### Example
Book stock ₹50 crore; counts find overages ₹2.5 crore and shortages ₹3.5 crore. Net variance = −₹1.0 crore = **2.0%** of book; gross variance = ₹6.0 crore = **12.0%**. Management sees "2% shrink" while the planning data are wrong on 12% of value. In a count of 5,000 locations, 4,600 within tolerance gives IRA = **92%**, below the 98% target, so the cycle-count frequency for failing zones is raised.

### In the news
See news box. NRF's 1.6% shrink (FY2022) is a net-to-sales figure; operations leaders should also track gross variance and IRA, which the headline figure does not show.

### Interview angle
> [!question] How it is asked
> "Book stock and physical stock differ by 2%. Is that acceptable?"

> [!tip] Strong answer includes
> - Net vs gross variance; ask for the breakdown by SKU, value and reason
> - IRA as the operational KPI, shrink % as the financial KPI
> - Root-cause categories and owners, not just write-off
> - Ties to planning: low IRA breaks MRP, replenishment and promise dates

---
## 10. GMROI and Inventory Days by Segment
> 🟠 Tier 2 · _Key points:_ Margin earned per rupee of stock; DIO split RM/WIP/FG

### Definition
**GMROI** (gross margin return on inventory investment) measures margin earned per ₹1 of inventory carried at cost:

$$GMROI = \frac{\text{Gross margin}}{\text{Average inventory at cost}} = \frac{GM\%}{1-GM\%}\times \text{Inventory turns}$$

The second form shows the trade-off: a slow-turn category must have a fatter margin. GMROI above about 1 means the item covers its own inventory cost; the cut-off is higher once carrying cost of 20-25% is included. **Days by segment**: DIO splits into raw material days, WIP days and finished-goods days (each = segment inventory / COGS × 365). Different levers act on each: RM days (supplier lead time, MOQ), WIP days (batch size, flow, [[007 Lean Manufacturing]]), FG days (forecast accuracy, service policy). Retail reads GMROI by category; manufacturing reads days by segment; both appear in [[012 Supply Chain Analytics & KPIs]] and [[108 Financial Statements & Ratios]].

### Example
Sales ₹1,200 crore, COGS ₹900 crore, average inventory ₹150 crore: GM = ₹300 crore, GM% = 25%, turns = 6, **GMROI = 300/150 = 2.0** (check: 0.25/0.75 × 6 = 2.0). Compare categories: Category B with 40% margin but only 2.5 turns gives 0.40/0.60 × 2.5 = **1.67**, below A despite its fatter margin; a grocery line with 15% margin at 18 turns gives **3.18**. Manufacturer: COGS ₹1,200 crore, RM ₹150 crore, WIP ₹60 crore, FG ₹110 crore gives 45.6, 18.3 and 33.5 days, total **97.3 days** (₹320 crore).

### In the news
See news box. The FSSAI direction affects FG days for food e-commerce: high-turn shelf-life SKUs earn GMROI only if stock moves inside the permitted shelf-life window.

### Interview angle
> [!question] How it is asked
> "Which category deserves more shelf space, one with 40% margin and slow turns or one with 25% margin and fast turns?"

> [!tip] Strong answer includes
> - GMROI formula and its decomposition into margin and turns
> - Numbers for both categories, then qualify with space, labour and carrying cost
> - DIO by segment to find where the cash is locked
> - Recognise halo effects: a low-GMROI traffic driver may still be right

---
## 11. Inventory Policy by Segment (ABC-XYZ)
> 🟠 Tier 2 · _Key points:_ Value × variability sets service, review and count rules

### Definition
Segmentation turns one blanket rule into a few differentiated policies. **ABC** (value) crossed with **XYZ** (demand variability, measured by coefficient of variation $CoV=\sigma/\mu$; illustrative cut-offs X < 0.5, Y 0.5-1.0, Z > 1.0) gives a 3×3 grid; add **VED** or **FSN** where criticality or movement matter (see [[003 Inventory Management]]).

| Segment | Service level | Review | Replenishment logic | Count frequency |
|---|---|---|---|---|
| AX | 97-98% | Weekly or continuous | Forecast-driven, tight safety stock | Monthly |
| AZ | 90-95% | Weekly | Make/buy-to-order, pooled buffers | Monthly |
| BY | 95% | Fortnightly | Min-max with forecast | Quarterly |
| CX | 98% (cheap) | Monthly | Bulk, two-bin or VMI | Yearly |
| CZ | Case by case | Monthly | Stock only if vital, else order on demand | Yearly |

Rules of thumb: A items get the lowest days of cover and the highest management attention; C items get high availability at low effort because they are cheap; Z items should be pooled or made to order since safety stock on erratic items is costly. For setting safety stock see [[003 Inventory Management]]; for policies beyond EOQ see [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]; for fit with strategy see [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]].

### Example
A company moves from a flat 95% service target (Z = 1.65) to differentiated targets: AX items 97% (Z = 1.88), AZ items 90% (Z = 1.28), CX items 98% (Z = 2.05). For an AZ item with lead-time demand s.d. of 100 units, safety stock falls from 1.65 × 100 = 165 to 1.28 × 100 = 128 units, a **22% cut**; for a very cheap CX item the extra stock costs almost nothing, so its service is raised. Savings on erratic, expensive items fund higher availability on cheap, stable ones.

### In the news
See news box. For food and quick commerce, expiry-limited A and Z items are the tightest segment: the longer the shelf life is consumed, the less safety stock the product can afford to carry.

### Interview angle
> [!question] How it is asked
> "How would you set different inventory policies for 10,000 SKUs?"

> [!tip] Strong answer includes
> - ABC by value plus XYZ by variability, with VED for spares
> - Service-level, review-period and replenishment rules per segment
> - Counting and governance intensity matched to the segment
> - Re-segment quarterly; avoid more than 6-9 policies to keep it operable

---
## 12. Audit Trails and Inventory Governance
> 🟠 Tier 2 · _Key points:_ Segregation of duties, adjustment authority, CARO and SA 501

### Definition
Governance means every quantity or value change is **traceable, authorised and reviewable**.
- **Audit trail**: every movement is a document with user, time and reference (SAP material documents via MIGO, viewed with MB51; change documents for master data; physical inventory documents). Adjustments need a reason code and approver.
- **Segregation of duties**: the person who counts is not the custodian, and neither approves or posts the adjustment. Adjustment authority by value (e.g. storekeeper up to ₹10,000; plant head above ₹5 lakh; CFO above ₹50 lakh; illustrative).
- **Cut-off controls**: goods received not invoiced (GR/IR), goods in transit, customer-owned and consignment stock, and sales dispatched but not billed are tested at period-end.
- **India-specific**: Companies (Auditor's Report) Order 2020 (CARO 2020) requires the auditor to comment on whether physical verification coverage and procedure are appropriate, and to report discrepancies of about 10% or more in aggregate for each class of inventory (value basis); where sanctioned working capital limits exceed ₹5 crore, quarterly returns to banks must be compared with the books. Auditors follow SA 501 (attendance at physical inventory counting). Under Ind AS 2, disclose the policy, carrying amount, write-downs and reversals, and inventory pledged as security.

### Example
A store clerk posts a ₹3 lakh "scrap adjustment" in SAP for a transformer coil and takes the material. With segregation of duties and approval thresholds, the transaction needs a plant-head approver and a scrap-yard weighbridge slip; an exception report on adjustments above ₹1 lakh by user catches repeat patterns. A year-end difference of 11% in a class would require disclosure in the auditor's CARO report even if later explained.

### In the news
See news box. NRF's finding that around 65% of shrink is theft (internal and external) and over a third administrative is the case for governance that covers both people and process controls.

### Interview angle
> [!question] How it is asked
> "What controls would you put in place to stop inventory leakage in a distribution centre?"

> [!tip] Strong answer includes
> - Segregation of duties, authority matrix and reason codes
> - Cycle counts with blind counts and exception reporting
> - Access control, CCTV and gate controls for physical security
> - Monitoring dashboards: variance by user, location and SKU; link to SAP GRC where relevant ([[201 SAP Landscape, Transports, Security & GRC Basics]])

---
## 13. Inventory Reduction Playbook with Worked Numbers
> 🟠 Tier 2 · _Key points:_ Excess clearing, safety stock, lot sizes, lead time, SKU cuts

### Definition
A reduction programme attacks inventory in order of ease and speed:
1. **Clear dead and excess stock** (liquidate, return to vendor, transfer): fast, but crystallises losses already provided for.
2. **Rightsize safety stock** by segment and by real variability, not blanket days of cover; remove double buffers (planner plus warehouse plus sales).
3. **Cut lot sizes** via lower setup/order cost (SMED, e-procurement): cycle stock falls with $\sqrt{S}$ (see [[003 Inventory Management]]).
4. **Shorten lead times** (supplier development, local sourcing): safety stock scales with $\sqrt{L}$.
5. **Rationalise SKUs and variants** and use postponement and commonality ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]).
6. **Fix the cause**: forecast bias, MOQ, S&OP discipline ([[004 Demand Forecasting & Planning]]).
Measure cash released, DIO and the service level at the same time; reduction must not erode OTIF. Working-capital effects: [[136 Supply Chain Finance & Working Capital]].

### Example
COGS ₹1,200 crore, inventory ₹320 crore: turns 3.75, DIO **97.3 days**. Lever plan: excess/obsolete liquidation ₹18 crore, safety-stock rightsizing ₹22 crore, lot-size reduction ₹15 crore, lead-time cut ₹12 crore, SKU rationalisation ₹8 crore: total **₹75 crore** (23.4% of inventory). New inventory ₹245 crore: turns **4.90**, DIO **74.5 days**. At 22% carrying cost, annual saving = 0.22 × 75 = **₹16.5 crore**; one day of DIO is worth COGS/365 = ₹3.29 crore. Lead-time check: for demand s.d. 10 units/day and Z = 1.65, cutting lead time from 20 to 12 days reduces safety stock from 73.8 to 57.2 units (−22.5%, equal to $1-\sqrt{12/20}$). Realism: if the ₹18 crore of excess recovers only 50%, the one-off loss is ₹9 crore (unless already provided), so the *cash* number is ₹75 crore gross but profit takes a hit in the year.

### In the news
See news box. Shelf-life regulation and shrink pressure push food and retail firms to sequence the playbook: clear short-dated stock first, then fix replenishment.

### Interview angle
> [!question] How it is asked
> "A client wants to cut inventory by 20% in 12 months without hurting service. How do you approach it?"

> [!tip] Strong answer includes
> - Baseline: inventory by segment (RM/WIP/FG), age, turns, service
> - Lever list with quantified sizing, sequenced quick wins first
> - Trade-offs: loss on liquidation, supplier cost, service risk; guardrail KPIs
> - Governance: owners, monthly review, linkage to bonus metrics so the gain sticks

---
## 14. ⭐ Advanced: GST on Write-offs, Valuation of Consignment and Third-Party Stock
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**GST angle.** Section 17(5)(h) of the CGST Act blocks input tax credit on goods "lost, stolen, destroyed, written off or disposed of by way of gift or free samples". When stock is physically scrapped or destroyed, ITC attributable to it must be reversed; an accounting **write-down to NRV** alone is not the same as a write-off of goods, and the treatment of inputs consumed in finished goods that are later destroyed remains contested (CBIC view vs some AAR rulings), so many companies reverse conservatively. See [[227 GST & Indirect Tax for Supply Chains]].

**Consignment and third-party stock.** Under consignment the supplier owns the stock until consumption, so it is **not** the customer's inventory; stock held by the customer for others, and goods in transit under Incoterms, must be separated at count and cut-off. Stock sent to job workers or held at third-party warehouses is still the company's asset but needs confirmations and periodic counts. SAP uses special stock indicators (K consignment, O subcontractor stock, E sales-order stock; see [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]]).

### Example
Expired stock with cost ₹2 crore is destroyed. If input GST of 18% is attributable (₹36 lakh), the P&L takes ₹2 crore of write-off plus the lost ITC of **₹36 lakh**, a total of ₹2.36 crore cash-equivalent loss, unless the stock is instead returned to the supplier under a credit-note arrangement or sold at scrap value (output GST then applies on the scrap). Compare this with an NRV write-down of the same stock to ₹60 lakh: no ITC reversal until goods are actually written off or destroyed, which is why the timing of disposal affects tax cost.

### In the news
See news box. FSSAI shelf-life rules mean more expired or short-dated returns; time-expired goods and ITC reversal remain a live GST question for FMCG and pharma, and the position should be checked with a tax adviser at the time.

### Interview angle
> [!question] How it is asked
> "A company is about to scrap ₹2 crore of stock. What should it consider before doing so?"

> [!tip] Strong answer includes
> - Alternatives first: return to vendor, rework, liquidate, donate
> - GST ITC reversal and scrap output GST; timing of disposal
> - Documentation: committee approval, destruction certificate, audit trail
> - Learning loop: root cause and provisioning accuracy

---
