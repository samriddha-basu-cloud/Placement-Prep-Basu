---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Demand-Driven MRP (DDMRP) & Buffer Management"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Demand-Driven MRP (DDMRP) & Buffer Management

⬅ [[116 Inventory Valuation, Cycle Counting & Inventory Governance]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Why Classic MRP Struggles: Nervousness, Bullwhip and Variability]]
2. [[#2. The DDMRP Method: Five (Six) Components]]
3. [[#3. Strategic Inventory Positioning and Decoupling Points]]
4. [[#4. Buffer Profiles and Level Factors]]
5. [[#5. Buffer Zones: Red, Yellow and Green Formulas]]
6. [[#6. The Net Flow Equation and Order Generation]]
7. [[#7. Dynamic Buffer Adjustments]]
8. [[#8. Qualified Demand Spikes]]
9. [[#9. Visible and Collaborative Execution]]
10. [[#10. DDMRP vs MRP vs Kanban vs TOC Buffer Management]]
11. [[#11. Implementation Roadmap, Results and Pitfalls]]
12. [[#12. Tool Support: SAP and Other Planning Systems]]
13. [[#13. ⭐ Advanced: Buffer Economics and Comparison with Statistical Safety Stock]]
14. [[#14. ⭐ Advanced: DDS&OP, Demand Driven Distribution and Positioning Trade-offs]]

## 📰 News box
> [!news] Why this matters now (checked 3 October 2026): DDMRP has moved from a niche method into mainstream planning software
> **Vendor-reported case results.** The Demand Driven Institute (DDI), which certifies DDMRP, publishes company results: Allergan reports **30%+ inventory reduction, over 50% lead-time reduction and 99%+ service levels**; Ceramfix reports **20% lower raw and WIP inventory, 99.5%+ service levels and inventory-to-revenue improving from 68.7% to 54.4%**; Mettler Toledo is cited as implementing across **20 plants and 180,000+ parts**; JELD-WEN is cited for "millions of dollars in free cash flow". These are DDI-hosted, self-reported figures, not independent audits. ([Demand Driven Institute: case studies](https://www.demanddriveninstitute.com/case-studies))
>
> **Software support.** DDI's compliance list (the vendor must pass the institute's DDMRP compliance test) names **SAP S/4HANA and SAP Integrated Business Planning** among compliant ERP systems, and add-on or planning applications including **Blue Yonder, Anaplan, ToolsGroup (Service Optimizer 99+), OMP, DELMIA, Asprova, QAD DynaSys, Dynamics 365 Planning** and many smaller tools. Kinaxis was not on the list as read; treat any Kinaxis DDMRP claim as unverified until checked with the vendor. DDI lists six components (the sixth is tactical adaptation through demand-driven S&OP), while the 2016 book framing is five. ([DDI: compliant software](https://www.demanddriveninstitute.com/ddmrp-compliant-software); [DDI: DDMRP overview](https://www.demanddriveninstitute.com/ddmrp))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Why Classic MRP Struggles: Nervousness, Bullwhip and Variability
> 🔴 Tier 1 · _Key points:_ Forecast-driven netting at every level amplifies noise

### Definition
**MRP** (see [[005 Production & Operations Planning]] and [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]]) explodes forecast and order demand through the bill of materials, nets against stock at every level, and offsets by lead time. Its weaknesses in volatile supply chains, which Carol Ptak and Chad Smith set out in *Orlicky's Material Requirements Planning* (3rd ed.) and *Demand Driven Material Requirements Planning* (2016):
- **System nervousness**: a small change at the top re-times and re-sizes orders at every level below.
- **Bullwhip**: lumpy lot-sized dependent demand amplifies variability upstream ([[114 Bullwhip Effect, Beer Game & Information Sharing]]).
- **Forecast dependence**: every level plans on a forecast, so errors compound across long lead times.
- **Flow-blind**: priority is by due date; planners cannot see which shortage will actually stop the line, so they expedite everything.
- **Unstable priority** and the "shortage plus excess" paradox: stock-outs on some parts, surplus on others.

DDMRP's response: stop netting everywhere; place a few **buffers at decoupling points**, size them from real usage and lead time, and replenish on **net flow** rather than on a forecast explosion. It combines MRP's planning logic, distribution requirements planning, Lean pull, and Theory of Constraints buffer management.

### Example
A pump maker has a 45-day cumulative lead time (30-day bought casting, 10-day machining, 5-day assembly) but customers expect delivery in 10 days. Under MRP every level carries safety stock based on a forecast, yet shortages recur because the forecast is wrong at SKU level. Under DDMRP the casting and machined subassembly get buffers sized on actual usage, shrinking the *unprotected* lead time seen by planning.

### In the news
See news box. Wider ERP vendors (SAP) adding DDMRP shows planners now expect pull-based buffers alongside classic MRP.

### Interview angle
> [!question] How it is asked
> "Why does MRP create expediting and excess stock at the same time, and what would you change?"

> [!tip] Strong answer includes
> - Forecast explosion plus lead-time offsets at every level; nervousness and bullwhip
> - Due-date priority is blind to actual stock status
> - Fix: decoupling buffers, net flow replenishment, execution by buffer status
> - Realistic: DDMRP supplements MRP where lead times are long and demand variable

---
## 2. The DDMRP Method: Five (Six) Components
> 🔴 Tier 1 · _Key points:_ Position, Protect, Pull, Adapt

### Definition
The method is summarised as **Position, Protect, Pull** (and Adapt). Five components, in order:
1. **Strategic inventory positioning**: decide where to place decoupling buffers in the BOM and distribution network.
2. **Buffer profiles and levels**: group items by type, lead time and variability and compute red, yellow and green zones.
3. **Dynamic adjustments**: recalculate buffers as usage, lead time or events change.
4. **Demand-driven planning**: daily **net flow equation** generates supply orders for buffered items.
5. **Visible and collaborative execution**: manage open orders through buffer-status and synchronisation alerts.

DDI now adds a sixth, **tactical adaptation**, implemented through Demand Driven S&OP (DDS&OP), which adjusts the model and strategy from past performance and planned future events. Components 1-3 *design* and maintain the model; 4-5 *run* it daily.

### Example
A distributor of 2,000 SKUs defines 120 decoupling points in the central warehouse and 60 at regional depots (component 1), classifies them into 9 buffer profiles (2), sets seasonal factors for monsoon and festive demand (3), runs the net flow check every night (4), and reviews a red/yellow alert list each morning (5).

### In the news
See news box. DDI describes the method as multi-echelon: planning and execution, not planning only.

### Interview angle
> [!question] How it is asked
> "Walk me through DDMRP in two minutes."

> [!tip] Strong answer includes
> - The five components in order, with a one-line purpose each
> - Net flow equation as the planning trigger, buffer status as the execution trigger
> - Contrast with MRP (dependent-demand netting) in one sentence
> - Honest scope: best where long lead times meet volatile demand

---
## 3. Strategic Inventory Positioning and Decoupling Points
> 🔴 Tier 1 · _Key points:_ Six criteria; decoupled lead time (DLT)

### Definition
A **decoupling point** is a stocked position that breaks the dependency between upstream supply variability and downstream demand: planning below it no longer needs to chase the end-customer forecast. DDMRP uses six criteria to place them (standard list in the Ptak and Smith literature): **customer tolerance time**, **market potential lead time** (can a longer lead time win more business?), **sales order visibility horizon**, **inventory leverage and flexibility** (stock at the point of greatest commonality or lowest cost), **critical operation protection** (for example a bottleneck, see [[005 Production & Operations Planning]]), and **external variability** (supply and demand volatility to be absorbed).

$$DLT = \text{longest cumulative unprotected lead time from the item back to a stocked (decoupled) position or purchase}$$

The buffer is sized on the DLT, not on the full cumulative lead time. Positioning is a strategic choice, not a software default: more buffers raise inventory but cut lead times and nervousness.

### Example
Pump: purchased casting 30 days, machining 10 days, final assembly 5 days; customer tolerance 10 days. Buffer only the casting: DLT of the finished pump = 10 + 5 = **15 days** (still above 10). Also buffer the machined subassembly: DLT of the pump = **5 days**, below customer tolerance, so no finished-goods stock is needed and the product can be assembled to order. The subassembly itself has DLT 10 days.

### In the news
See news box. Mettler Toledo's reported rollout across 180,000+ parts shows positioning has to be done by explicit rules at scale; poor placement gives either too much stock or unprotected lead time.

### Interview angle
> [!question] How it is asked
> "Where would you hold stock in this multi-level supply chain?"

> [!tip] Strong answer includes
> - Names the criteria (customer tolerance time versus lead time is the first test)
> - Computes DLT with and without a buffer
> - Uses commonality (shared parts) and bottlenecks to choose positions
> - Links to postponement ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]])

---
## 4. Buffer Profiles and Level Factors
> 🔴 Tier 1 · _Key points:_ Item type, lead-time category, variability category

### Definition
A **buffer profile** combines:
- **Item type**: **M**anufactured, **I**ntermediate, **P**urchased, **D**istributed.
- **Lead-time category** (relative to the supply chain): short, medium, long, each with a **lead-time factor (LTF)**. Guidance ranges: long lead time about 20-40%, medium 41-60%, short 61-100% (shorter lead times get *larger* factors because the stock is a bigger share of the cycle).
- **Variability category** (supply or demand variability exposure): low, medium, high, each with a **variability factor (VF)**: roughly 0-40% low, 41-60% medium, 61-100% high.

The factors are design parameters chosen by profile and then tuned from performance. Items with a **minimum order quantity (MOQ)** or a long order cycle get a larger green zone. Typical rule: pick the profile once, so a planner cannot hand-tune each SKU and so the model stays auditable. Use [[004 Demand Forecasting & Planning]] (forecast error, CoV) to rank variability.

### Example
Illustrative values within the guidance ranges: profile "Purchased, long lead time, high variability" LTF 0.25, VF 0.80; profile "Distributed, short lead time, low variability" LTF 0.75, VF 0.30. A 40-day imported component gets the first; a locally sourced packaging item with a 5-day lead time the second.

### In the news
See news box. Vendors listed as compliant must implement profile-driven zones; ToolsGroup and Blue Yonder both appear on the list.

### Interview angle
> [!question] How it is asked
> "How do lead time and variability influence the buffer?"

> [!tip] Strong answer includes
> - Item types and the two factor families
> - Why a long lead time shrinks the red base factor but raises DLT
> - Variability factor builds on the red base, so unstable items get more safety
> - Fixed profiles keep governance simple versus per-SKU tuning

---
## 5. Buffer Zones: Red, Yellow and Green Formulas
> 🔴 Tier 1 · _Key points:_ ADU × DLT; red = base + safety; green = max of three

### Definition
Let $ADU$ be **average daily usage** (historic, forward, or blended), $DLT$ the decoupled lead time, $LTF$ and $VF$ the profile factors, $MOQ$ the minimum order quantity and $OC$ the desired order cycle in days.

$$\text{Yellow} = ADU \times DLT$$
$$\text{Red base} = ADU \times DLT \times LTF, \quad \text{Red safety} = \text{Red base} \times VF, \quad \text{Red} = \text{Red base} + \text{Red safety}$$
$$\text{Green} = \max\big(ADU \times DLT \times LTF,\; MOQ,\; ADU \times OC\big)$$

Boundaries: **TOR** (top of red) = Red; **TOY** = TOR + Yellow; **TOG** = TOY + Green. Meaning: **red** is protection against variability, **yellow** covers demand during the lead time (the replenishment cycle), **green** sets order frequency and size and protects against too-early, too-large orders. Higher ADU or DLT scales every zone.

### Example
$ADU = 100$/day, $DLT = 10$ days, $LTF = 0.5$, $VF = 0.5$, $MOQ = 200$, $OC = 5$ days.
Red base = 100 × 10 × 0.5 = **500**; red safety = 500 × 0.5 = **250**; red = **750**. Yellow = 100 × 10 = **1,000**. Green = max(500, 200, 100 × 5) = **500**. So TOR 750, TOY 1,750, TOG **2,250**. Compare a classic safety stock for demand s.d. 40/day: $1.65 \times 40 \times \sqrt{10} \approx 209$ units, but the DDMRP red (750) is a different construct: it is a flow-protection zone sized by profile, not a statistical service-level formula.

### In the news
See news box. Allergan's and Ceramfix's reported results (vendor-reported) are attributed by DDI to flow-based buffers like these, rather than ad hoc safety stocks.

### Interview angle
> [!question] How it is asked
> "Calculate the buffer for an item with ADU 100, lead time 10 days, medium variability."

> [!tip] Strong answer includes
> - Red base, red safety, yellow, green formulas without hesitation
> - Why green takes the maximum of three drivers (lead time, MOQ, order cycle)
> - Relates zones to purpose: protection, demand coverage, order cycle
> - Notes that the factors are profile-based design choices

---
## 6. The Net Flow Equation and Order Generation
> 🔴 Tier 1 · _Key points:_ NFP = on-hand + on-order − qualified demand

### Definition
Every day, each buffered item is compared on **net flow position**:

$$NFP = \text{On-hand} + \text{On-order} - \text{Qualified demand}$$

**Qualified demand** = past-due sales orders + sales orders due today + **qualified spikes** (see sub-topic 8); non-spike future orders are *not* netted, which keeps the signal stable. **Rule:** if $NFP \le TOY$, generate a supply order for

$$\text{Order qty} = TOG - NFP$$

rounded up to MOQ or order multiples. Priority for execution is $\dfrac{NFP}{TOG}$ (planning priority) and on-hand position vs zones (execution priority). Contrast with MRP, which nets forecast and orders for every time bucket and level.

### Example
Using the buffer above (TOY 1,750, TOG 2,250): on-hand 900, on-order 600, qualified demand 300. $NFP = 900 + 600 - 300 = 1{,}200 \le 1{,}750$, so order $2{,}250 - 1{,}200 = 1{,}050$, rounded to the MOQ multiple of 200 gives **1,200** units. Planning priority = 1,200/2,250 = **53%**. On-hand 900 sits in the **yellow** zone (750-1,750), so the execution view is "ok but watch". If a bulky order of 600 units due in 8 days were also qualified, NFP = 900 + 600 − 900 = 600 and the order becomes 2,250 − 600 = 1,650, rounded to **1,800** units.

### In the news
See news box. SAP S/4HANA and SAP IBP are on DDI's compliant list, so net flow checks can run inside the ERP and planning stack.

### Interview angle
> [!question] How it is asked
> "On-hand 900, on-order 600, demand 300; TOY 1,750, TOG 2,250. What happens?"

> [!tip] Strong answer includes
> - NFP calculation, comparison with TOY, order quantity = TOG − NFP
> - Rounding to MOQ and why priority uses NFP/TOG
> - Why future non-spike demand is not netted (reduces nervousness)
> - Notes on timing: order due date set by DLT, not by forecast offset

---
## 7. Dynamic Buffer Adjustments
> 🔴 Tier 1 · _Key points:_ Recalculated ADU, zone adjustment factors, planned events

### Definition
Buffers are not static. Three kinds of adjustment:
1. **Recalculated adjustments**: ADU (and DLT, MOQ) updated on a schedule from history, forward demand, or a blend. All zones scale with ADU.
2. **Planned adjustments**: **demand adjustment factor (DAF)** or zone adjustment factors applied for seasons, promotions, launches, phase-outs. Example: raise ADU by a seasonal factor before Diwali.
3. **Manual adjustments**: planner overrides with reasons (supply disruption, supplier change).
Rule: adjust *buffers*, not the plan; avoid chasing noise by smoothing ADU and limiting how often zones change. Good governance logs every override and reviews it in tactical meetings.

### Example
ADU rises from 100 to 130 (+30%): zones scale by 1.3, so TOR 975, TOY 2,275 and TOG **2,925**. An NFP of 1,200 is now well below TOY, so a larger replenishment (2,925 − 1,200 = 1,725) is triggered, adding stock *as* demand rises rather than after a forecast review. When demand falls the buffer shrinks and orders pause, so stock bleeds off naturally instead of becoming excess.

### In the news
See news box. This self-adjusting property is the main claim behind DDMRP's reported ability to lower stock and hold service levels at once (vendor-reported).

### Interview angle
> [!question] How it is asked
> "Demand for an item has jumped 30%. What does DDMRP do and what could go wrong?"

> [!tip] Strong answer includes
> - ADU recalculation scales all zones; new orders are generated by the NFP rule
> - Planned factors for known events, reviewed in DDS&OP
> - Risks: noisy ADU, over-reaction, supplier capacity limits
> - Governance of manual overrides

---
## 8. Qualified Demand Spikes
> 🔴 Tier 1 · _Key points:_ Spike threshold and horizon; orders netted only if large and near

### Definition
A **demand spike** is a single order (or cluster) large enough to threaten the buffer's red or yellow zone. Because netting every future order creates the nervousness DDMRP aims to avoid, only **qualified** spikes are netted into qualified demand. Qualification needs two parameters:
- **Spike threshold**: the order size above which an order is considered a spike, commonly set around **half of the red zone** (or an item-specific value); users may use a multiple of ADU.
- **Spike horizon**: how far ahead orders are examined, commonly one **DLT** (orders due beyond the lead time can still be dealt with later).

An order that is above threshold *and* inside the horizon is added to qualified demand, so the buffer is protected before the order arrives; smaller orders consume stock and are handled by the buffer.

### Example
Red = 750, so the threshold is 375; DLT = 10 days. A 600-unit order due in 8 days **is** a qualified spike (600 > 375, 8 < 10). A 300-unit order due in 8 days is not (below threshold); a 600-unit order due in 25 days is not yet (beyond horizon). Result: only the first changes NFP now. If the 600-unit order were ignored, the buffer would show healthy flow right up to the day stock fell below the red line.

### In the news
See news box. DDI runs a compliance test for software vendors, so spike qualification is something buyers can ask a vendor to demonstrate.

### Interview angle
> [!question] How it is asked
> "A customer places a very large order for next week. How does DDMRP respond without distorting everything else?"

> [!tip] Strong answer includes
> - Qualified spike definition: threshold and horizon
> - Order is netted, buffer triggers supply; small orders are absorbed
> - Consequence for lead-time commitment (promise date)
> - Compare to MRP, which nets all orders at all times

---
## 9. Visible and Collaborative Execution
> 🔴 Tier 1 · _Key points:_ Buffer status alerts, synchronisation alerts, priority by % of buffer

### Definition
DDMRP separates **planning** (when to make or buy, via NFP) from **execution** (making sure open orders arrive in time). Two main alert types:
- **Buffer status alerts**: open orders and on-hand are ranked by **on-hand position as a percentage of the buffer** (or % of red zone remaining). Colour bands: **green** (healthy), **yellow** (watch), **red** (critical, expedite); within red, planners work the lowest percentage first. Priority is by *what actually threatens flow*, not by due date.
- **Synchronisation alerts**: for non-stocked positions (items between buffers), compare the order's due date to the stock status of the buffered parent so unnecessary expediting is avoided.
Additional signals: lead-time alerts (suppliers taking longer than DLT), planner **projected on-hand** alerts, and supplier collaboration screens, as with shared priority lists. The aim: one version of priorities across planning, production and purchasing.

### Example
Four open purchase orders: item A (stock at 20% of red, due date in 3 days), item B (stock at 90% of the buffer, due in 1 day), item C (yellow, due in 5 days), item D (red, due in 20 days). Under due-date priority B comes first; under buffer status A and D come first because they are in red, and B (healthy) needs no expediting. The planner's morning list has three red lines instead of 140 "late" orders.

### In the news
See news box. DDI's case studies emphasise service level and lead-time gains, which depend on planners working the buffer-status list rather than due-date lists (vendor-reported).

### Interview angle
> [!question] How it is asked
> "How would you prioritise expediting across 500 open orders?"

> [!tip] Strong answer includes
> - Rank by buffer penetration, not by due date
> - Distinguish buffer status vs synchronisation alerts
> - Supplier collaboration with shared priorities and capacity
> - Outcome metrics: number of expedites, red-zone days, service level

---
## 10. DDMRP vs MRP vs Kanban vs TOC Buffer Management
> 🔴 Tier 1 · _Key points:_ Where each method wins and fails

### Definition
| Dimension | MRP | Kanban | TOC buffer management (DBR) | DDMRP |
|---|---|---|---|---|
| Trigger | Forecast and orders, exploded with lead time offsets | Card or container consumed | Buffer penetration at the constraint | Net flow position vs zones |
| Where planned | Every level of BOM | Between adjacent stations | At the constraint (drum), shipping and assembly buffers | Only at decoupling points |
| Demand signal | Forecast plus actuals | Actual consumption | Orders and constraint schedule | Actual usage (ADU) and qualified orders |
| Buffer sizing | Safety stock, fixed lead times | Fixed card count | Time buffer (typically a fraction of lead time) | Dynamic zones |
| Strength | Complex dependent demand, planning visibility | Simple, visual, stable repetitive flow | Protects the bottleneck and gives simple priorities | Long lead time and volatile demand, multi-level BOM |
| Weakness | Nervousness, forecast error, expediting | Weak with variable demand and long lead times | Single-constraint focus; less suited to many SKUs | Needs master-data discipline, change management, limited to chosen positions |

TOC colour priorities: buffer consumed in thirds (green 0-33%, yellow 34-66%, red 67-100%). DDMRP borrows the colour logic but applies it to inventory and open orders. For Lean pull see [[007 Lean Manufacturing]] and [[006 Manufacturing Systems]]; for TOC see [[005 Production & Operations Planning]].

### Example
Automotive aftermarket spares (thousands of SKUs, erratic demand, 60-day import lead times): kanban cards do not scale and MRP's forecast is poor; DDMRP buffers on stocked parts suit. High-volume repetitive assembly of one product at stable rate: kanban remains simplest. A job shop with a clear bottleneck: drum-buffer-rope.

### In the news
See news box. DDI's case list spans pharma (Allergan), ceramics (Ceramfix), appliances (Haier Europe) and building products (JELD-WEN), showing use beyond one sector (vendor-reported).

### Interview angle
> [!question] How it is asked
> "Is DDMRP just kanban or safety stock with colours?"

> [!tip] Strong answer includes
> - Differences: dynamic sizing, net flow vs card count, decoupling rationale
> - Where MRP is still needed (planning visibility, BOM explosion for unbuffered parts)
> - Fit conditions: long lead times, volatile demand, multi-level BOM, spares
> - Hybrid use is normal: MRP for stable parts, DDMRP for the volatile or long-lead ones

---
## 11. Implementation Roadmap, Results and Pitfalls
> 🔴 Tier 1 · _Key points:_ Pilot, data, change management, KPIs

### Definition
Typical stages: (1) **segment and select** items and the network (high variability, long lead time, many shortages); (2) **design** decoupling points and profiles; (3) **clean master data**: lead times, MOQs, BOM, usage history, calendars ([[175 Data Quality, Master Data & Data Governance]]); (4) **pilot** on one plant or product family for 3-6 months with clear KPIs; (5) **scale** and train planners; (6) **adapt** through DDS&OP. KPIs: service level/OTIF, inventory days, number of expedites, red-zone days, order-count stability, lead time.

Pitfalls: treating it as a software switch, no change in planners' habits (still working the due-date list), buffers set by hand, bad lead-time data, no executive sponsor, measuring only inventory not service. Reported results: Allergan 30%+ inventory reduction with 99%+ service; Ceramfix inventory-to-revenue from 68.7% to 54.4% (vendor-reported, DDI site). Indian relevance: capital goods, auto aftermarket, pharma and FMCG plants with long import lead times or volatile channels; compare with [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]].

### Example
Pilot sizing: 400 SKUs with ₹80 crore stock and 94% service. Target: 20% stock reduction (₹16 crore) and service to 98%. At 22% carrying cost the stock saving is ₹3.5 crore a year; the ₹16 crore also shortens cash-to-cash directly. Success metric chosen before the pilot: service level in the pilot group versus a control group of similar SKUs.

### In the news
See news box. All reported figures are self-reported by adopters and DDI; a consulting answer should say which claims are independent and which are not.

### Interview angle
> [!question] How it is asked
> "A client is considering DDMRP. How would you decide and run a pilot?"

> [!tip] Strong answer includes
> - Fit test (lead time, variability, BOM depth, shortages)
> - Data readiness and pilot design with control group
> - KPIs: service, inventory days, expedites, red-zone days
> - Change management and honest handling of vendor-reported results

---
## 12. Tool Support: SAP and Other Planning Systems
> 🔴 Tier 1 · _Key points:_ ERP vs planning layer; compliance list

### Definition
DDMRP needs daily recalculation of ADU, zones and NFP, plus buffer-status dashboards. Options: native support in ERP/APS, an add-on, or a spreadsheet pilot. On DDI's compliant list (as read on 3 Oct 2026) are **SAP S/4HANA** and **SAP IBP** (ERP category), **Blue Yonder**, **Anaplan**, **ToolsGroup**, **OMP**, **DELMIA**, **Asprova**, **QAD DynaSys**, **Dynamics 365** tools and others. See [[198 SAP IBP, APO & Demand-Driven Planning]] for the SAP design and [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]] for how DDMRP differs from MRP types in S/4HANA; the wider landscape is in [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]. Integration needs: stock, open orders and sales history from ERP; item master and lead times; and write-back of replenishment proposals.

### Example
A pilot in Excel or Python: compute ADU from the last 90 days, DLT from item master, zones from profile factors, NFP from an ERP stock extract, and flag items where NFP ≤ TOY. Use [[046 Python for Operations]] or [[078 Excel for Operations & SCM]]. Once rules are validated, move to the compliant planning tool for daily runs.

### In the news
See news box. DDI's list shows compliance is a testable property of a tool, which gives buyers a checklist rather than marketing language.

### Interview angle
> [!question] How it is asked
> "How would you run DDMRP at a client with SAP?"

> [!tip] Strong answer includes
> - Choose between native S/4HANA/IBP capability and an add-on
> - Pilot in a spreadsheet to validate parameters
> - Data feeds and integration needs
> - Do not claim a vendor is compliant without checking DDI's current list

---
## 13. ⭐ Advanced: Buffer Economics and Comparison with Statistical Safety Stock
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A buffer carries average on-hand of roughly **red + green/2** under steady demand (the yellow zone is in motion). Compare with a classic (Q, R) policy: average inventory $Q/2 + SS$ ([[003 Inventory Management]]). The difference is not in the arithmetic but in the *reaction*: the buffer changes with ADU and DLT daily, whereas a statistical safety stock is reviewed rarely and assumes a stable normal distribution. Where demand is erratic or intermittent, statistical formulas misstate risk; DDMRP trades a statistical guarantee for adaptability and visibility. Cross-check with [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]] and [[114 Bullwhip Effect, Beer Game & Information Sharing]].

### Example
Item 1 (ADU 100): red 750, green 500, average on-hand ≈ 750 + 250 = **1,000** (10 days of cover). Item 2 (purchased, ADU 50, DLT 40 days, LTF 0.25, VF 0.8, MOQ 1,000, OC 30 days): red base 500, red safety 400, red **900**, yellow **2,000**, green max(500, 1,000, 1,500) = **1,500**; TOG **4,400**; average on-hand ≈ 900 + 750 = **1,650** (33 days of cover). The order-cycle driver (30 days × ADU) makes green large to cut order frequency from a distant supplier.

### In the news
See news box. Reported inventory-to-revenue improvements (Ceramfix 68.7% to 54.4%) are the type of outcome buffer economics aims at, though not proof of a general result.

### Interview angle
> [!question] How it is asked
> "How is a DDMRP buffer different from safety stock plus cycle stock?"

> [!tip] Strong answer includes
> - Average on-hand approx red + green/2 versus Q/2 + SS
> - Dynamic recalculation and flow-based triggers versus periodic statistical review
> - When statistical safety stock is still right (stable demand, service-level contract)
> - Evidence base: mostly case studies, so frame results with caution

---
## 14. ⭐ Advanced: DDS&OP, Demand Driven Distribution and Positioning Trade-offs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Demand Driven S&OP (DDS&OP)** is the tactical layer: it reviews buffer performance, scenario changes in positions or profiles, and the impact of planned events, instead of reviewing a single-number consensus forecast. It ties into [[120 Integrated Business Planning (IBP) & S&OP Maturity]]. **Demand Driven Distribution** applies the same logic in the network: buffers at each stocking location with the **supplier-pull** logic of net flow, reducing the bullwhip on the central warehouse and linking to [[119 Supply Planning, DRP & Available-to-Promise]] (DRP-style time-phased netting vs flow-based buffers). A positioning review compares: inventory cost of an extra decoupling point versus lead-time reduction versus shortage cost.

### Example
Adding a buffer on the machined subassembly costs, say, 10 days × ADU × unit cost: ADU 100/day at ₹1,500 gives ₹15 lakh of stock; carrying cost at 22% = ₹3.3 lakh a year. Benefit: DLT of the finished pump drops from 15 to 5 days, letting the firm quote a 10-day delivery and avoid an assumed ₹40 lakh a year of lost orders and expediting. Net benefit ≈ ₹36.7 lakh a year, justifying the buffer; if the benefit were only ₹2 lakh, the buffer would not be placed.

### In the news
See news box. A DDS&OP review fits the same cadence as a monthly IBP cycle; whichever tool is used, the central question is where to place stock, not how to forecast better.

### Interview angle
> [!question] How it is asked
> "Where would you add stock in this supply chain to meet a 10-day promise?"

> [!tip] Strong answer includes
> - Compare cost of the extra buffer with the DLT reduction and shortage cost
> - Use customer tolerance time as the target
> - Link positioning decisions to S&OP governance
> - Re-evaluate positions when demand, supply or product mix change
