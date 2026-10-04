---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP MRP Deep Dive - Planning Strategies & Parameters"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP MRP Deep Dive - Planning Strategies & Parameters

⬅ [[192 SAP Sourcing & Procurement Deep Dive]] · [[_Index - SAP ERP|SAP ERP]] · [[194 SAP Production Execution, Confirmation & Product Costing]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. MRP Types: PD, VB, VM, VV, ND]]
2. [[#2. MRP Logic: Netting, Planning Horizon and Processing Keys]]
3. [[#3. Static Lot-Sizing Procedures: EX, FX, HB]]
4. [[#4. Periodic and Optimum Lot-Sizing Procedures]]
5. [[#5. Safety Stock, Safety Time, Rounding and Lead-Time Buffers]]
6. [[#6. Planning Strategies: 10, 20, 30, 40, 50, 60, 70]]
7. [[#7. MTS, MTO and ATO Flows in SAP]]
8. [[#8. Procurement Type, Special Procurement, MRP Controller and MRP Group]]
9. [[#9. Planning Time Fence and Planning Horizon]]
10. [[#10. Lead-Time Scheduling and the Scheduling Margin Key]]
11. [[#11. Stock/Requirements List (MD04), MRP List (MD05) and Exception Messages]]
12. [[#12. From Planned Order to PR, PO and Production Order]]
13. [[#13. MRP Live, Planning File Entries and Planning Calendar]]
14. [[#14. ⭐ Advanced: MRP Troubleshooting Playbook]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): planning logic moves to HANA and to event-driven, IBP-linked planning
> **S/4HANA 2025 on-premise release (8 Oct 2025).** IDES24's overview lists, for sourcing and supply planning, **event-driven planner notifications for supply-demand imbalances**, an interactive view of production structures, **advanced ATP with automated stock transfer** and **tighter integration with SAP IBP**; it also lists a manufacturing rework enhancement. The classic MRP logic below (netting, lot sizes, strategies, time fences) is the base these features sit on. (Vendor-described; confirm in release notes.) ([IDES24](https://www.ides24.de/en/knowledge/what-s-new-in-s4hana-2025))
>
> **ECC deadline and the 2033 "transition option" (announced 4–5 Feb 2025).** Standard ECC maintenance ends **31 Dec 2027**; extended maintenance for on-premise SAP ERP ends at the **end of 2030**; for very large ECC estates SAP offers a transition option purchasable from **2028** and usable **2031–2033**, tied to a RISE contract and SAP HANA. Plants running classic `MD01` jobs must decide when to move to MRP Live and S/4HANA. ([CIO.com](https://www.cio.com/article/3816887/sap-throws-a-lifeline-to-large-organizations-with-new-ecc-offering.html); [TechTarget](https://www.techtarget.com/searchsap/news/366618912/Rise-With-SAP-will-extend-support-deadline-for-some))
>
> **GAIL goes live on S/4HANA Cloud (25 Jun 2025).** The Maharatna PSU's one-year "Navodaya" programme moved it from legacy ECC to S/4HANA on cloud, which GAIL called a first for a Maharatna PSU. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
>
> **SAP Q2 2026 (23 Jul 2026).** Current cloud backlog **€22.9 billion (+27%)**; cloud revenue +24% at constant currency; 2026 cloud revenue outlook **€25.8–26.2 billion**. ([PR Newswire](https://www.prnewswire.com/news-releases/sap-quarterly-statement-q2-2026-302833633.html))
>
> Sub-topics that say **"See news box"** reuse these items. Basics of MRP and PP: [[081 SAP PP — Production Planning]], [[005 Production & Operations Planning]].

---
## 1. MRP Types: PD, VB, VM, VV, ND
> 🔴 Tier 1 · _Key points:_ Deterministic vs consumption-based planning; reorder point; ND

### Definition
The **MRP type** (MRP 1 view) decides *how* a material is planned.
- **PD (MRP):** deterministic. Planning from known and forecast **requirements** (sales orders, PIRs, dependent requirements, reservations). Used for finished goods and for components with BOM dependence.
- **VB (manual reorder point):** consumption-based. When stock falls to the **reorder point**, a procurement proposal is raised; reorder point and safety stock are entered manually.
- **VM (automatic reorder point):** like VB but the system calculates the reorder point and safety stock from a **forecast** and the service level.
- **VV (forecast-based planning):** forecast values (with consumption history) become requirements and are netted like PD.
- **ND (no planning):** MRP ignores the item; used for items managed manually, service materials, trading items bought ad hoc.

Reorder point: $ROP=\bar d\times L+SS$, with safety stock $SS=z\,\sigma_d\sqrt{L}$ ($L$ is replenishment lead time in days, $z=1.65$ for 95% service).

Selection rule: **PD for anything with dependent demand or a real forecast; VB/VM for low-value C-class items with stable usage** (nuts, gloves, lubricants); ND for items outside planning. The theory is in [[003 Inventory Management]] and [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]].

### Example
A consumable with average usage 25 units a day, daily standard deviation 6, replenishment lead time 16 days (14 planned delivery + 2 GR processing). $SS=1.65\times6\times\sqrt{16}=39.6\approx40$. $ROP=25\times16+40=$ **440 units**. Under VB, you maintain ROP 440 and SS 40 in the material master; MRP raises a PR once stock plus open receipts is at or below 440. Under VM, the system recomputes these values from the forecast every time the forecast is run.

### In the news
See news box. Event-driven planner notifications (IDES24) matter most for PD items; reorder-point items rely on thresholds rather than demand signals.

### Interview angle
> [!question] How it is asked
> "Difference between MRP type PD and VB? Which items would you put on reorder-point planning?"

> [!tip] Strong answer includes
> - PD (requirements-driven) vs VB/VM (consumption-driven) and VV, ND
> - ROP and safety stock formula with a worked number
> - Item selection logic (A items PD, C items VB/VM; ABC/XYZ)
> - Risk: VB with stale ROP leading to stock-outs; periodic review of parameters

---

## 2. MRP Logic: Netting, Planning Horizon and Processing Keys
> 🔴 Tier 1 · _Key points:_ Gross to net, receipts, safety stock, low-level code, NETCH/NETPL/NEUPL

### Definition
**MRP** converts requirements into procurement proposals in these steps:
1. **Planning file entry** check: only materials flagged for planning (changed since the last run) are processed.
2. **Net requirements calculation** for each material by period: available quantity = stock + scheduled receipts (POs, PRs, planned orders, production orders) − requirements (sales orders, PIRs, dependent requirements, reservations). If available < **safety stock**, the shortage is the net requirement.
3. **Lot sizing:** shapes the quantity of the proposal (EX, FX, HB, WB and so on).
4. **Scheduling:** dates from lead times (backward from the requirement date).
5. **Proposal creation:** planned order (in-house) or PR / delivery schedule line (external), followed by **BOM explosion** which creates dependent requirements for the next **low-level code** (items are planned top-down so that a component is planned after all its parents).

$$\text{Net requirement}=\text{Safety stock}-\left(\text{Stock}+\text{Receipts}-\text{Requirements}\right)\ \text{if positive}$$

**Processing keys:** **NEUPL** regenerative planning (all materials, slow, used after master-data clean-up); **NETPL** net change planning (only materials with changes); **NETCH** net change in the **planning horizon** (only materials with changes inside the horizon, the usual daily run). The **planning horizon** is the period in which MRP creates proposals; beyond it, MRP will not create new proposals.

### Example
Stock 100, safety stock 20, PO receipt of 150 in week 2; weekly requirements 80, 0, 120, 60, 0, 150, 90, 40. Lot-for-lot (EX) planning:

| Week | Requirement | Receipt | Available before order | Planned order | Available after |
|---|---|---|---|---|---|
| 1 | 80 | – | 20 | – | 20 |
| 2 | 0 | 150 | 170 | – | 170 |
| 3 | 120 | – | 50 | – | 50 |
| 4 | 60 | – | −10 | **30** | 20 |
| 5 | 0 | – | 20 | – | 20 |
| 6 | 150 | – | −130 | **150** | 20 |
| 7 | 90 | – | −70 | **90** | 20 |
| 8 | 40 | – | −20 | **40** | 20 |

The shortage in week 4 is 10 units below zero **plus** the safety stock of 20, so MRP orders 30. Total proposals 310 units in four orders. Every proposal is a function of the MRP master data, which is why wrong data gives wrong plans.

### In the news
See news box. IDES24 describes planner notifications for supply-demand imbalances in the 2025 release, which present this same net-requirement logic to planners as alerts.

### Interview angle
> [!question] How it is asked
> "Walk me through how MRP calculates a planned order." or "What is the difference between net change and regenerative planning?"

> [!tip] Strong answer includes
> - Netting formula with safety stock and a numbered example
> - Low-level code and BOM explosion
> - NEUPL vs NETPL vs NETCH, and when each is used
> - Role of planning file entries and horizon

---

## 3. Static Lot-Sizing Procedures: EX, FX, HB
> 🔴 Tier 1 · _Key points:_ Lot-for-lot, fixed lot, replenish to maximum

### Definition
The **lot-size key** (MRP 1 view) tells MRP how to size each proposal. **Static** procedures use only the shortage quantity and fixed parameters:
- **EX (exact/lot-for-lot):** the proposal equals the shortage exactly. Minimum stock and cost; many small orders. Suited to expensive, make-to-order and high-variability items.
- **FX (fixed lot size):** proposals are in multiples of a fixed quantity until the shortage is covered (pallet, tank, batch size). May leave surplus stock.
- **HB (replenish to maximum stock level):** the proposal is the difference between **maximum stock level** and available stock: $Q = Max-\text{available}$. Common for bulk and reorder-point items.

Modifiers (apply to almost all procedures): **minimum lot size**, **maximum lot size** (splits larger quantities into several orders), **rounding value** (round up to multiple, e.g. pallet of 50) or **rounding profile** (dynamic by range) and **assembly scrap %** (inflates quantity to cover expected loss). Splitting and overlapping apply when capacity is limited.

### Example
(a) EX: shortage 230 gives an order of 230. (b) FX 100: 230/100 = 2.3, so 3 lots, **300** (surplus 70 into stock). (c) EX with rounding value 50: **250**. (d) HB, maximum stock 500: stock 100, requirement 150, no receipts; available after requirement −50, so $Q=500-(-50)=$ **550**, bringing stock back to 500. In the 8-week data of the previous sub-topic: **FX 250** creates two orders (week 4 and week 7, total 500, ending stock 210); **HB 400** creates one order of **410** in week 4 (ending stock 120).

### In the news
See news box. Many migrations clean lot-size keys before cut-over because years of unmanaged EX/FX settings inflate order counts.

### Interview angle
> [!question] How it is asked
> "A planner complains about too many tiny orders. Which parameters do you change?"

> [!tip] Strong answer includes
> - EX/FX/HB logic with numbers
> - Rounding, minimum and maximum lot sizes and assembly scrap
> - Trade-off: set-up/ordering cost vs holding cost ([[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]])
> - Match to item type (high value EX; bulk HB)

---

## 4. Periodic and Optimum Lot-Sizing Procedures
> 🔴 Tier 1 · _Key points:_ WB/MB/TB, planning-calendar lot size, part-period balancing, Groff, least unit cost

### Definition
**Periodic procedures** group requirements within a period into one lot: **TB** daily, **WB** weekly, **MB** monthly (also 2-weekly), or by a **planning calendar** (key PK in the standard delivery). The lot is created at the start of the period and covers all net requirements in it; grouping lowers order count and suits bought items with a vendor delivery rhythm.

**Optimum procedures** compare ordering cost with holding cost across periods:
- **Part-period balancing (key SP in the standard delivery):** adds future periods to the lot while accumulated *part periods* (quantity × periods held) stay below $EPP=\frac{S}{h}$ (set-up cost ÷ holding cost per unit per period).
- **Groff reorder procedure (GR):** adds periods while the marginal holding cost is lower than the marginal saving in set-up per unit.
- **Least unit cost (WI)** and **dynamic lot-size creation (DY)** minimise cost per unit over the periods covered.

They need **set-up cost** and **holding cost** in the material master or plant data. (Key names for the optimum procedures differ between sources and clients; confirm them in the lot-size customising `OMI4` of your system.)

### Example
Net weekly requirements 60, 0, 120, 60, 0, 150, 90, 40 (total 520); set-up ₹1,000 per order; holding ₹2 per unit per week; $EPP=1000/2=500$ unit-weeks.

| Procedure | Orders (week: qty) | Order cost | Holding cost | Total |
|---|---|---|---|---|
| Lot-for-lot | 6 orders | ₹6,000 | ₹0 | ₹6,000 |
| Fixed 250 | 1: 250, 6: 250, 8: 250 | ₹3,000 | ₹1,660 | ₹4,660 |
| 2-week periodic | 1: 60, 3: 180, 5: 150, 7: 130 | ₹4,000 | ₹500 | ₹4,500 |
| Part-period balancing | 1: 240, 6: 280 | ₹2,000 | ₹1,180 | **₹3,180** |

Part-period balancing covers weeks 1–5 in order 1 (accumulated part periods 240 + 180 = 420 ≤ 500) and weeks 6–8 in order 2 (90 + 80 = 170). Its ₹3,180 equals the Wagner-Whitin optimum for this data, 47% below lot-for-lot.

### In the news
See news box. S/4HANA 2025's planner notifications do not change the lot-size logic; optimisation is still the planner's parameter decision.

### Interview angle
> [!question] How it is asked
> "Compare lot-for-lot, fixed lot and part-period balancing for a given demand profile."

> [!tip] Strong answer includes
> - Static, periodic and optimum families with keys
> - EPP concept with set-up and holding cost
> - A cost table showing the trade-off
> - Practical remark: optimum procedures need reliable cost data; many plants stay with EX/FX and tune lot size by ABC class

---

## 5. Safety Stock, Safety Time, Rounding and Lead-Time Buffers
> 🔴 Tier 1 · _Key points:_ Static safety stock, safety time/range of coverage, service level, rounding profile

### Definition
Buffers protect against uncertainty. In the material master:
- **Safety stock (MRP 2):** quantity MRP tries not to dip below; a shortfall below it triggers a proposal (exception **96** when stock fell below safety stock). Setting it in units is **static**.
- **Safety time/actual range of coverage (MRP 2):** MRP advances requirement dates by a number of days (**safety time**), producing a time buffer instead of a quantity buffer. **Dynamic** safety stock uses **range of coverage profiles** to size stock by upcoming demand.
- **Service level (MRP 1):** for VM and forecast-based planning, determines automatically computed safety stock.
- **Rounding value / profile**, **minimum and maximum lot size**, **assembly scrap**.
- **Lead-time elements:** planned delivery time (external), GR processing time, in-house production time or routing lead time; these decide start dates.

Safety stock theory: $SS=z\sigma_d\sqrt{L}$ for demand variability; with supply-time variability use $SS=z\sqrt{L\sigma_d^2+\bar d^2\sigma_L^2}$ ([[003 Inventory Management]]).

### Example
Daily demand 40, σ_d 10, lead time 9 days, service level 95% (z = 1.65): $SS=1.65\times10\times3=49.5\approx50$. With lead-time variability σ_L = 2 days: $SS=1.65\sqrt{9\times100+1600\times4}=1.65\sqrt{7300}=1.65\times85.4=$ **141 units**, nearly three times higher. Using a safety **time** of 3 days instead would move requirements three days earlier, keeping stock at zero until needed but leaving the plan exposed if demand is higher than forecast.

### In the news
See news box. Stale safety stocks are a known finding in S/4HANA clean-up projects because they inflate working capital.

### Interview angle
> [!question] How it is asked
> "How would you reduce inventory without hurting service in SAP?"

> [!tip] Strong answer includes
> - Safety stock vs safety time and dynamic profiles
> - Formula with demand and lead-time variability, with a number
> - Periodic parameter review (lead-time actuals, forecast accuracy)
> - Link to S&OP/IBP for demand signals ([[198 SAP IBP, APO & Demand-Driven Planning]])

---

## 6. Planning Strategies: 10, 20, 30, 40, 50, 60, 70
> 🔴 Tier 1 · _Key points:_ Strategy group in MRP 3, PIR vs sales order, consumption

### Definition
A **planning strategy** (config `OPPS`, assigned through the **strategy group** in the MRP 3 view) decides the **requirement types** for planned independent requirements (PIR) and for sales orders, i.e. which requirements MRP plans for and how sales orders interact with forecasts.

| Strategy | Name | Idea |
|---|---|---|
| **10** | Net requirements planning (MTS) | Plan from PIR; **sales orders do not create requirements**; deliveries reduce the PIR |
| **20** | Make-to-order production | No PIR; each sales order item drives its own planned order and stock (special stock E) |
| **30** | Production by lot size | Make-to-stock variant where production follows the item's lot-size rules (confirm the exact description in your client) |
| **40** | Planning with final assembly | PIR for the finished good; **sales orders consume the PIR**; production of the FG is planned in advance |
| **50** | Planning without final assembly | PIR created for the FG, but MRP plans only **components**; FG assembly starts when the sales order arrives |
| **60** | Planning with planning material | PIR on a planning (grouping) material, then split to variants as orders arrive |
| **70** | Planning at assembly level | PIR for an assembly; consumed by orders for the final product that contain it |

Related MRP 3 fields: **consumption mode** (backward/forward), **consumption periods** (days backward and forward) and **availability check**. In the standard delivery, strategy 20 uses requirement type KE, and strategy 40 uses VSF for PIR and KSL for sales orders (check `OPPS` in your client).

### Example
**Strategy 40 consumption.** PIR 1,000 units for a month. A sales order of 300 arrives within the consumption window: it consumes the PIR, so the open PIR falls to 700 and total demand stays 1,000 (not 1,300). **Strategy 10:** the same 300 sales order does not reduce the PIR; the PIR falls to 700 only when the 300 are delivered. If the sales order is not consumed against the right PIR (wrong consumption period), demand is double-counted and stock builds up.

### In the news
See news box. Strategy choice defines how forecasts from tools like SAP IBP flow into S/4HANA as PIRs.

### Interview angle
> [!question] How it is asked
> "Which planning strategies exist in SAP and which would you choose for a customised machine vs a consumer product?"

> [!tip] Strong answer includes
> - Strategy groups and requirement types
> - 10/40 for stock, 20 for MTO, 50/70 for ATO, 60 for variants
> - Consumption logic with an example
> - Business trade-off: service level vs inventory vs lead time ([[112 Supply Chain Strategy - Fit, Segmentation & Maturity]])

---

## 7. MTS, MTO and ATO Flows in SAP
> 🔴 Tier 1 · _Key points:_ Where the customer order decoupling point sits

### Definition
Which strategy to use depends on the **customer order decoupling point** (CODP).

**MTS (strategy 10 or 40):**
1. Demand planner enters PIR (`MD61`) or loads from IBP.
2. MRP creates planned orders; production orders produce for stock.
3. Sales orders are delivered from stock; ATP checks stock; GI (601) reduces stock and (strategy 10) the PIR.

**MTO (strategy 20):**
1. Sales order (`VA01`) item with requirement type KE triggers MRP.
2. Planned order or PR **assigned to the sales order**; components planned for that order.
3. GR goes to **sales-order stock (E)**, valued per order when set; delivery from that stock; billing and per-order profit analysis.

**ATO (strategy 50 or 70):**
1. Components or sub-assemblies planned from the PIR (forecast); no FG stock.
2. When the sales order arrives, **final assembly** order is created; the sales order consumes the planned assembly.
3. Delivery lead time shortened to the final-assembly time.

Delivery times and risks: MTS best service/high stock; MTO low stock/long delivery; ATO balances them for products with many variants.

### Example
A tractor maker builds engines and transmissions to forecast (strategy 50 PIR: 400 engines a month, ₹3.2 lakh each) but assembles the tractor only on order. Component stock is held at about 1.2 months' forecast (₹15.4 crore for engines), while FG stock is zero. A customer order triggers final assembly with a 5-day lead time instead of the 25 days it would take to build everything from raw material. (Illustrative numbers.)

### In the news
See news box. Event-driven notifications are especially helpful in ATO and MTO flows where a single sales order change cascades to components.

### Interview angle
> [!question] How it is asked
> "Explain MTS, MTO and ATO in SAP with the planning strategy and special stock used for each."

> [!tip] Strong answer includes
> - CODP concept and strategies 10/40, 20, 50/70
> - MTO uses special stock E (see [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]])
> - Delivery-time vs inventory trade-off with numbers
> - Link to postponement ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]])

---

## 8. Procurement Type, Special Procurement, MRP Controller and MRP Group
> 🔴 Tier 1 · _Key points:_ E/F/X, special procurement keys, planner ownership, MRP group

### Definition
- **Procurement type (MRP 2):** **E** in-house production (planned order), **F** external procurement (PR or schedule line), **X** both (the special procurement key says which applies).
- **Special procurement key:** refines the procurement route: **10** consignment, **30** subcontracting, **40** stock transfer from another plant, **50** phantom assembly (an assembly not stocked: its components are passed straight through).
- **MRP controller (MRP 1):** the person or team responsible for the material; used to select materials in MRP runs, in `MD04`/`MD06` worklists and exception messages.
- **MRP group:** groups materials with common planning control parameters (strategy group, consumption mode, planning time fence, planning horizon, creation indicator for PRs and planned orders).
- **Creation indicators:** whether MRP creates PRs directly, planned orders only, or schedule lines in the opening or planning horizon.
- **Phantom assemblies:** BOM explosion goes through them, so planning is at the level of components.

### Example
Material X123 has procurement type X and special procurement key 40 (stock transfer from plant 1100 to plant 1200). MRP at plant 1200 creates a **stock transport requisition** instead of a PR to an outside vendor; the transfer arrives by STO and delivery ([[191 SAP MM Advanced - Inventory, Batches & Special Stocks]]). If the key were blank, procurement type X would fall back to the default, in-house production (a planned order). A phantom assembly "wiring kit" with key 50 is exploded in the BOM so MRP orders its wires and connectors directly, avoiding a work order for the kit.

### In the news
See news box. Aligning MRP controllers and MRP groups with the new organisation is a typical task in S/4HANA conversions for companies reorganising plants.

### Interview angle
> [!question] How it is asked
> "What is the difference between procurement type and special procurement type?"

> [!tip] Strong answer includes
> - E, F, X and the role of the special key (10, 30, 40, 50)
> - MRP controller as worklist owner and MRP group as parameter bundle
> - Example of stock transfer or subcontracting planning
> - Phantom assemblies and BOM explosion

---

## 9. Planning Time Fence and Planning Horizon
> 🔴 Tier 1 · _Key points:_ Freeze period, firming, rescheduling, horizon vs fence

### Definition
- **Planning time fence (MRP 3, in days):** a window from today in which MRP **does not automatically change existing proposals or create new ones**. Shortages inside the fence are shown for manual action; MRP creates new proposals at the end of the fence. The fence protects the shop floor from nervous changes.
- **Planning horizon (plant/MRP group):** the period for which MRP creates proposals under NETCH; materials with changes outside it are not re-planned in daily runs.
- **Firming:** planned orders can be firmed (manually, or automatically with **firming type** and **fixing type**) so MRP will not delete or reschedule them.
- **Rescheduling check:** compares existing receipts with requirements and issues exception messages (**10 reschedule in**, **20 reschedule out**, **30 cancel**) with a **tolerance** (days) to avoid noise.
- **Opening period / release period:** from the scheduling margin key (next sub-topic).

### Example
Planning time fence 10 days. Today is day 0 and a new urgent sales order creates a shortage on day 6. MRP does not create a planned order inside the fence; the planner sees the shortage and either expedites an existing PO, creates a manual order, or accepts the fence-end proposal (day 11), after which the customer is delivered five days late. Alternatively the planner can shorten the fence for this material, which increases system changes but improves responsiveness.

### In the news
See news box. IDES24's event-driven notifications aim to help planners handle exactly the imbalance cases that arise inside fences.

### Interview angle
> [!question] How it is asked
> "What is a planning time fence and what would be the downside of setting it too long or too short?"

> [!tip] Strong answer includes
> - Freeze window, what MRP will and will not change inside it
> - Firming and rescheduling tolerance
> - Trade-off stability vs responsiveness; fence ≈ cumulative lead time
> - Distinction from the planning horizon

---

## 10. Lead-Time Scheduling and the Scheduling Margin Key
> 🔴 Tier 1 · _Key points:_ Backward scheduling, floats, opening and release dates

### Definition
MRP schedules **backwards from the requirement date**. For external procurement:
- **GR processing time** (working days) is subtracted from the requirement date to give the **delivery date**;
- **planned delivery time** (calendar days) gives the **order date**;
- **purchasing department processing time** (working days, plant parameter) gives the **PR release/creation date**.

For in-house production the planned order dates come from either **in-house production time** (basic dates, no routing) or **lead-time scheduling** from the **routing** (operation durations, queue and move times) with the factory calendar.

The **scheduling margin key** (MRP 2) adds buffers (in working days): **opening period** (time between opening date and start), **float before production**, **float after production** (buffer between production finish and requirement date) and **release period** (between opening date and release). Floats and lead-time scheduling convert master data into dates; wrong lead times are the biggest cause of late orders.

### Example
Requirement date Fri 30 Oct 2026 for a bought item: GR processing time 2 working days, planned delivery time 14 calendar days, purchasing processing time 3 working days (Mon–Fri calendar). **Delivery date** Wed 28 Oct; **order date** Wed 14 Oct (28 Oct − 14 days); **PR date** Fri 9 Oct (3 working days before 14 Oct). Any approval or vendor delay beyond that cascades into the requirement date. For an in-house item with float after production of 1 day, the planned finish is the day before the requirement date.

### In the news
See news box. IBP and S/4HANA lead-time data both rely on the same master-data lead times; cleaning them is part of migration.

### Interview angle
> [!question] How it is asked
> "How does SAP calculate the dates of a purchase requisition?" or "What is a scheduling margin key?"

> [!tip] Strong answer includes
> - Backward scheduling with the three lead-time elements and working vs calendar days
> - Scheduling margin key components with purpose
> - Basic dates vs lead-time scheduling with routing
> - Root-cause practice for late supply (stale lead times)

---

## 11. Stock/Requirements List (MD04), MRP List (MD05) and Exception Messages
> 🔴 Tier 1 · _Key points:_ Real-time vs snapshot, elements, exception reaction

### Definition
- **`MD04` Stock/requirements list:** *real-time* view of all supply (stock, PO, PR, planned and production orders, schedule lines) and demand (sales orders, PIRs, dependent requirements, reservations) with running **available quantity** per date. Planners can convert planned orders, firm, change dates, and display exception messages. `MD07` is the collective display.
- **`MD05` MRP list:** *snapshot* created at the end of the last MRP run for that material; `MD06` collective display. It does not reflect later changes; use it for audit of what MRP saw.
- **Exception messages** flag what needs attention. Core ones: **10 reschedule in** (receipt can be earlier because requirement is earlier), **20 reschedule out** (receipt is too early, move later), **30 cancel process** (no longer needed), **96 stock fell below safety stock level**. Others cover missing BOM or routing, past-dated opening/start dates and exceeding maximum lots. Exception groups let planners filter in `MD06`.

**Reaction logic:** reschedule in/out → move PO/order dates; cancel → delete or reduce; shortage → expedite, split, change source; safety stock breach → either replenish or reconsider the parameter. In S/4HANA, the Fiori app **Monitor Material Coverage** provides a planner worklist over the same data.

### Example
Material A: stock 50, open PO 200 for week 5, but a sales order of 120 now due in week 3. `MD04` shows available −70 in week 3 and exception 10 on the PO (bring forward by 2 weeks). The planner calls the vendor; if impossible, creates an STO from another plant for 100 units. Material B: PO 300 arrives week 2 while the requirement is week 6: exception 20, reschedule out, avoids carrying 4 weeks of stock (300 units × ₹40 × 4/52 × 12% ≈ ₹111 of cost of capital; small per item, but about ₹1.1 lakh across 1,000 such items).

### In the news
See news box. IDES24 lists event-driven planner notifications for the 2025 release; they are a push version of the exception messages above.

### Interview angle
> [!question] How it is asked
> "What is the difference between MD04 and MD05, and how do you react to an exception message?"

> [!tip] Strong answer includes
> - Real-time (MD04) vs snapshot (MD05), collective views (MD06, MD07)
> - Meaning of reschedule in/out, cancel, safety stock breach
> - Concrete reaction per message
> - Fiori counterpart and exception groups for prioritisation

---

## 12. From Planned Order to PR, PO and Production Order
> 🔴 Tier 1 · _Key points:_ Conversion, production version, opening date, mass conversion

### Definition
MRP's output is **procurement proposals**; each is converted into an executable document:
- **Planned order → production order:** in `MD04` (convert) or mass via `CO40` (collective conversion) and `COHV`. The **production version** (MRP 4 view) selects the BOM alternative and routing; the **order type** comes from plant parameters. The planned order is replaced by the production order (marked as converted); components get reservations and capacity requirements are carried over.
- **Planned order → process order** in process industries and **repetitive** planning: repetitive manufacturing uses planned orders as direct production through production lines.
- **PR → RFQ/PO:** buyer converts via `ME21N` (with PR selection) or automatic `ME59N`; the vendor, price and delivery date come from source determination ([[192 SAP Sourcing & Procurement Deep Dive]]).
- **Delivery schedule line** in scheduling agreement is created directly and transmitted via EDI.
- **Conversion timing:** within the **opening period** the proposal becomes PR or can be converted; PRs have a release date derived from lead-time scheduling.
- **Partial conversion:** a planned order can be split, converting a part to a production order.

Conversion is the point at which a plan becomes a commitment: after it, components are reserved and goods issue is possible ([[194 SAP Production Execution, Confirmation & Product Costing]]).

### Example
MRP has planned order 400 pieces for FERT-220, start 5 Oct, finish 12 Oct. The planner converts it in `MD04` to production order 1000812; availability check shows component COMP-10 short by 50 kg, so the order is held (not released) until a PO receipt on 7 Oct arrives. If the planner converts a second planned order of 300 pieces partially (200 now, 100 later), the remainder stays a planned order of 100.

### In the news
See news box. Fewer manual conversion steps are one reason plants adopt notifications and mass processing on S/4HANA.

### Interview angle
> [!question] How it is asked
> "How does a planned order become a production order or PO?"

> [!tip] Strong answer includes
> - Planned order to production order (`MD04`, `CO40`), PR to PO (`ME21N`, `ME59N`)
> - Production version and BOM/routing selection
> - Availability check on conversion and reservations created
> - Process vs repetitive variants

---

## 13. MRP Live, Planning File Entries and Planning Calendar
> 🔴 Tier 1 · _Key points:_ MD01N, HANA-run logic, change entries, MD20/MD21, MD25

### Definition
- **MRP Live (`MD01N`)** executes the planning logic in the HANA database using database procedures instead of reading each material into the ABAP application server. Result: one set-oriented pass, much faster full-plant runs, so planners can run more often. Classic MRP (`MD01`, `MD02`) remains available, but SAP recommends MRP Live in S/4HANA. Always check the current limitations list for your release before promising behaviour. SAP has also described **predictive MRP (pMRP)**, which simulates MRP into the future (check availability in your release).
- **Planning file entries:** MRP plans only materials flagged because of change (new sales order, goods movement, BOM change, master data change). `MD20` creates an entry manually (after data correction), `MD21` displays entries. NETCH/NETPL use them; NEUPL ignores them. SAP re-implemented parts of this mechanism for HANA, but the principle is unchanged.
- **Planning calendar (`MD25` create, `MD26` change, `MD27` display):** defines planning days (e.g. dates when a vendor delivers or when MRP plans the item), used with **periodic lot sizing by planning calendar** and the **planning cycle** in MRP 2.
- **MRP area:** plan a material separately at plant, storage location or subcontractor level.

### Example
A food distributor orders from a vendor who delivers Monday and Thursday. Calendar "MON/THU" is assigned to the material; requirements arising between deliveries accumulate; MRP creates PRs only for those two days. Requirements in the week are 40 (Tue), 60 (Wed) and 80 (Fri). With periodic lot sizing by calendar, requirements falling between two calendar dates are grouped into one lot delivered at the start of that interval: Tue 40 + Wed 60 form one lot of **100** delivered Monday, and Fri 80 forms a lot of **80** delivered Thursday. Two PRs replace three, and vendor deliveries match the vendor's route days; the cost is holding 40 units for one day, 60 units for two days and the 80 units for one day.

### In the news
See news box. As S/4HANA plants shift to MRP Live, replacing overnight jobs with intra-day runs is a typical benefit goal.

### Interview angle
> [!question] How it is asked
> "What is MRP Live and how does it differ from classic MRP? How does SAP decide which materials to plan?"

> [!tip] Strong answer includes
> - HANA-run logic, same results, faster and more frequent runs
> - Planning file entries and processing keys
> - Planning calendars for periodic delivery
> - Honest caveat: verify supported features per release

---

## 14. ⭐ Advanced: MRP Troubleshooting Playbook
> ⭐ Advanced · _Added beyond the tracker_

### Definition
When MRP "did not create a proposal", check in this order:
1. **MRP type** is ND or blank for the plant/material.
2. **Planning file entry** missing (no change since last run) or the material is outside the selection (MRP controller, plant, planning scope).
3. **No net shortage:** available stock, firmed receipts or safety stock cover demand; check `MD04` and consumption of PIR.
4. **Planning strategy / requirement type** wrong, so the sales order is not an MRP requirement (strategy 10 does not plan from sales orders).
5. **Planning horizon or time fence:** shortage is beyond the horizon, or inside the fence (no automatic change).
6. **Procurement type/special key:** F with no source, E without a production version or BOM ("no BOM selected" exception).
7. **Lot-size** (HB without maximum stock, FX with huge lot) producing a surprising quantity.
8. **Dates:** lead times or calendar create opening dates in the past.
9. **Firmed orders** or fixed documents block rescheduling.
10. **MRP area / storage location MRP** segmenting the plan.

**Consultant questions:** what changed (master data, strategy, calendar), what the planner expected, and a sample material to trace in `MD04` and `MD05`.

### Example
Planner complaint: "MRP created no order for FERT-330 although a 200-unit sales order is due in two weeks." Trace: `MD04` shows no requirement; strategy group 10 makes the sales order not an MRP requirement; the PIR was consumed down to zero by deliveries and was not replenished. Fix: enter new PIR (`MD61`) or switch the material to strategy 40 so sales orders create requirements and consume the PIR. After the change the shortage appears and MRP creates a planned order of 200.

### In the news
See news box. Ahead of the 2027 maintenance deadline, many plants audit planning parameters in this same way as part of fit-to-standard workshops ([[079 SAP Fundamentals & Architecture]]).

### Interview angle
> [!question] How it is asked
> "A planner says MRP is not creating proposals for an item. How do you investigate?"

> [!tip] Strong answer includes
> - A systematic checklist from MRP type to dates
> - Use of `MD04`, `MD05`, `MD21` and the MRP run log
> - Distinguish data errors from design errors (strategy, fence)
> - Fix, test with one material, then mass-correct through a migration or LSMW-type load; document the cause ([[175 Data Quality, Master Data & Data Governance]])
