---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "SCM Interview Question Bank"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SCM Interview Question Bank

⬅ [[142 Company Supply Chain Case Library]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[144 SCM Body of Knowledge Map - CSCP, CPIM, CLTD & SCPro]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Strategy, Frameworks and Fundamentals (Q1-Q6)]]
2. [[#2. Procurement and Sourcing (Q7-Q12)]]
3. [[#3. Inventory Management (Q13-Q18)]]
4. [[#4. Forecasting and S&OP (Q19-Q24)]]
5. [[#5. Production Planning, Lean and Constraints (Q25-Q30)]]
6. [[#6. Logistics and Transportation (Q31-Q36)]]
7. [[#7. Warehousing and Fulfilment (Q37-Q42)]]
8. [[#8. Quality Management (Q43-Q48)]]
9. [[#9. Risk and Resilience (Q49-Q54)]]
10. [[#10. Digital Supply Chain, Analytics and ERP (Q55-Q60)]]
11. [[#11. India Context: Policy, GST and Structure (Q61-Q66)]]
12. [[#12. Finance, KPIs and Working Capital (Q67-Q72)]]
13. [[#13. Mini-Case Playbook: Five Cases with Skeleton Answers]]
14. [[#14. ⭐ Advanced: Questions to Ask the Interviewer and a Last-Week Drill]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the three live SCM interview stories
> **Red Sea rerouting.** Maersk's July 2024 analysis: going around the Cape of Good Hope raised average cargo travel distance by **9%**, Suez crossings fell **66%** (the canal normally carries about **12% of global trade**) and available capacity was **15–20% lower in Q2 2024**. ([Maersk](https://www.maersk.com/insights/resilience/2024/07/09/effects-of-red-sea-shipping)) Suez Canal revenue fell from **$9.4 billion to $7.2 billion** between FY2022/23 and FY2023/24. ([Maritime Executive](https://maritime-executive.com/article/suez-canal-revenue-dropped-2b-last-year-due-to-red-sea-security-crisis))
>
> **Nexperia (October–November 2025).** The Dutch government took control of the chipmaker in early October 2025 and China blocked exports of its China-made output. Nexperia holds roughly **40%** of the market for automotive transistors and diodes; industry groups said stocks would last "a matter of weeks"; China confirmed exemptions on **6 November 2025**. ([Automotive Logistics](https://www.automotivelogistics.media/supply-chain/china-confirms-exemptions-to-export-controls-following-trumpxi-meeting-allowing-flow-of-nexperia-chips-to-resume/2098912))
>
> **US tariff volatility (2025).** The estimated average US tariff rate went from about **2.5% in January 2025 to about 27% in April 2025**, and tariffs on Chinese goods reached **145%** before a rollback to 30% in May 2025. ([Wikipedia: Tariffs in the second Trump administration](https://en.wikipedia.org/wiki/Tariffs_in_the_second_Trump_administration), checked October 2026)
>
> Sub-topics that say **"See news box"** reuse these items. Case detail is in [[141 Supply Chain Disruption Case Library (2011-2026)]] and [[142 Company Supply Chain Case Library]].

---
## 1. Strategy, Frameworks and Fundamentals (Q1-Q6)
> 🔴 Tier 1 · _Key points:_ Push-pull, fit, SCOR, trade-offs, drivers

### Definition
**Rapid-fire questions.** Answer in 30 seconds each; then stop.

**Q1. Supply chain vs logistics vs SCM?** Logistics is the movement and storage part; the supply chain is the whole network of suppliers, plants, DCs, retailers and customers; SCM is the management of flows (goods, information, cash) across it to meet demand at least cost. See [[001 SCM Introduction & Fundamentals]].

**Q2. Push vs pull; where is the decoupling point?** Push builds to forecast; pull builds to actual demand. The decoupling (CODP) is where the order meets the forecast: MTS at finished goods, ATO at modules, MTO at components. Dell sits near ATO. See [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]].

**Q3. Efficient or responsive chain for a product?** Fisher: functional products (staples, atta) with predictable demand need efficiency; innovative products (fashion, phones) need responsiveness. Pair with Chopra-Meindl's implied-uncertainty fit. See [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]].

**Q4. What are the processes of SCOR?** The SCOR Digital Standard (2022) has Plan, Order, Source, Transform, Fulfill, Return and Orchestrate (replacing Plan-Source-Make-Deliver-Return-Enable). See [[111 SCOR Model & Supply Chain Process Frameworks]].

**Q5. The six supply chain drivers?** Facilities, inventory, transportation, information, sourcing, pricing: each trades responsiveness against efficiency. See [[001 SCM Introduction & Fundamentals]].

**Q6. Why is cost-minimising rarely right?** Costs sit in different functions: cutting transport via full trucks raises inventory; cutting inventory raises stock-outs. The objective is **total landed cost at a service target**. See [[009 Logistics & Distribution]] and [[138 Order Management, Customer Service & Cost-to-Serve]].

### Example
**Numerical N1 (landed cost).** FOB ₹1,000, freight ₹80, insurance ₹10, customs duty 10% of CIF, port and clearing ₹15. CIF $= 1000 + 80 + 10 = ₹1{,}090$; duty $= 0.10 \times 1090 = ₹109$; landed cost $= 1090 + 109 + 15 = ₹1{,}214$ per unit. A domestic supplier at ₹1,200 with no duty is cheaper unless quality or lead time differ. Detail in [[126 International Trade Documentation, Customs & Trade Finance]].

### In the news
See news box. Tariffs and Red Sea show why "total landed cost" and "scenario cost" must replace unit price.

### Interview angle
> [!question] How it is asked
> "Mini-case: a consumer-durables company has 30 SKUs and complaints of stock-outs and high inventory at once. What is wrong?"

> [!tip] Strong answer includes
> - Hypothesis: one-size-fits-all strategy; segment SKUs (fast vs slow, stable vs volatile)
> - Different policies per segment (ABC-XYZ), postponement for variants
> - Quantify with fill rate, turns and forecast error before recommending
> - **Ask the interviewer:** "What is the service-level target and which SKUs drive the complaints?"

---
## 2. Procurement and Sourcing (Q7-Q12)
> 🔴 Tier 1 · _Key points:_ Kraljic, TCO, make-vs-buy, contracts, supplier risk

### Definition
**Q7. Explain the Kraljic matrix.** Items are classified by profit impact and supply risk: strategic (partner), leverage (competitive bidding), bottleneck (secure supply), non-critical (automate). See [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]].

**Q8. What is TCO and why not choose the lowest price?** TCO adds logistics, quality cost, inventory carrying, duties, risk and end-of-life cost to price; the cheapest quote is often the dearest. See [[002 Procurement & Strategic Sourcing]].

**Q9. Make or buy: how do you decide?** Compare relevant costs (variable cost plus avoidable fixed) at expected volume with strategic factors: core competence, capacity, IP, supply risk. Break-even volume $= F/(P_{buy} - V_{make})$. See [[002 Procurement & Strategic Sourcing]].

**Q10. Hard savings vs cost avoidance?** Hard savings reduce the P&L versus the baseline price; cost avoidance prevents an increase and is not booked. Finance wants hard savings. See [[122 Spend Analysis, Savings & Procurement Maturity]].

**Q11. How do you hedge a commodity price risk?** Map exposure, then use index-linked contracts with pass-through, forward buying, financial hedges (MCX, LME) up to a policy limit, and substitution. See [[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]].

**Q12. When is single sourcing acceptable?** When the item is non-critical or the supplier is a true partner with exit and continuity plans; otherwise dual or multi-source. See [[015 Supply Chain Risk & Resilience]].

### Example
**Numerical N2 (make vs buy).** Buy ₹120 per unit; make variable ₹80 with fixed cost ₹6,00,000 a year. Break-even $= 6{,}00{,}000 / (120 - 80) = 15{,}000$ units. At 20,000 units making saves $20{,}000 \times 40 - 6{,}00{,}000 = ₹2{,}00{,}000$; at 10,000 buying saves ₹2,00,000 (since $10{,}000 \times 40 = 4{,}00{,}000 < 6{,}00{,}000$).

**N3 (weighted scorecard).** Weights: quality 50%, delivery 20%, cost 20%, flexibility 10%. Supplier A scores 8, 7, 9, 6; B scores 7, 9, 7, 8. A $= 4.0 + 1.4 + 1.8 + 0.6 = 7.8$; B $= 3.5 + 1.8 + 1.4 + 0.8 = 7.5$. A wins; check sensitivity: if cost weight rises to 40% (quality 30%) B's lead in delivery and flexibility is outweighed by A's cost score, so A still wins.

### In the news
See news box. Nexperia is the textbook "non-critical by price, critical by impact" bottleneck item.

### Interview angle
> [!question] How it is asked
> "Mini-case: your sole supplier of a ₹40 component raises prices by 25%. What do you do?"

> [!tip] Strong answer includes
> - Classify the item (Kraljic), test whether the increase is cost-justified (should-cost)
> - Options: negotiate with data, qualify a second source (with timeline and cost), redesign or substitute
> - Quantify annual impact $= \text{volume} \times ₹10$ and compare with switching cost
> - **Ask the interviewer:** "How long does requalification take and what share of volume is at risk?"

---
## 3. Inventory Management (Q13-Q18)
> 🔴 Tier 1 · _Key points:_ EOQ, safety stock, ABC, turns, newsvendor, pooling

### Definition
**Q13. What does EOQ assume and what does it give?** Constant demand, known costs, instant replenishment; $EOQ = \sqrt{2DS/H}$ minimises ordering plus holding cost. At the optimum, ordering cost equals holding cost. See [[003 Inventory Management]], [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]].

**Q14. How is safety stock set?** $SS = z \cdot \sigma_{dL}$; with variable demand and lead time, $\sigma_{dL} = \sqrt{L\sigma_d^2 + d^2\sigma_L^2}$. $z$ comes from the target service level (95% gives 1.645, 99% gives 2.326). See [[003 Inventory Management]].

**Q15. ABC vs XYZ vs FSN vs VED?** ABC ranks by value, XYZ by demand variability, FSN by movement speed, VED by criticality; combine ABC-XYZ for policy. See [[003 Inventory Management]] and [[116 Inventory Valuation, Cycle Counting & Inventory Governance]].

**Q16. Why does pooling reduce inventory?** Independent demands partly cancel, so combined variability grows by $\sqrt{n}$ rather than $n$. Safety stock falls by $1 - 1/\sqrt{n}$ when $n$ locations merge. See [[003 Inventory Management]].

**Q17. Newsvendor in one line?** Order up to the quantile where $P(D \le Q) = C_u/(C_u + C_o)$, the critical ratio. See [[003 Inventory Management]] and [[137 Supply Chain Contracts & Game Theory]].

**Q18. Inventory is high and so is stock-out. Why?** Wrong inventory in the wrong place: poor segmentation, forecast bias, long lead times, no buffers where variability is high. Fix with ABC-XYZ policies, DDMRP-style buffers ([[117 Demand-Driven MRP (DDMRP) & Buffer Management]]) and bias tracking.

### Example
**N4 (EOQ).** $D = 12{,}000$ units, $S = ₹500$, $H = ₹20$ per unit-year:
$$EOQ = \sqrt{\frac{2 \times 12000 \times 500}{20}} = \sqrt{600000} \approx 775$$
Orders $= 12000/775 = 15.5$ a year (every 23.6 days); total cost $= \frac{12000}{775}(500) + \frac{775}{2}(20) \approx 7{,}746 + 7{,}746 = ₹15{,}492$.

**N5 (safety stock and ROP).** $d = 40$/day, $L = 9$ days, $\sigma_d = 8$/day, 95% service: $SS = 1.645 \times 8 \times \sqrt{9} = 39.5$ (1.65 gives 39.6); $ROP = 40 \times 9 + 39.6 = 399.6 \approx 400$.

**N6 (pooling).** Four DCs each with $\sigma = 50$: $SS = 4 \times 1.65 \times 50 = 330$; one central DC $\sigma = \sqrt{4} \times 50 = 100$, $SS = 1.65 \times 100 = 165$: a **50% reduction**.

**N7 (newsvendor).** Underage cost ₹30, overage ₹20: critical ratio $= 30/50 = 0.60$, $z = 0.253$. With demand mean 200, $\sigma = 40$: $Q = 200 + 0.253 \times 40 = 210$.

**N8 (turns).** COGS ₹240 crore, average inventory ₹40 crore: turns $= 6$, DIO $= 365/6 = 60.8$ days. A 10% cut on ₹50 crore of stock frees ₹5 crore; at 18% carrying cost saves ₹0.9 crore a year.

### In the news
See news box. Tariff front-loading and Nexperia buffers turned inventory policy into a boardroom topic.

### Interview angle
> [!question] How it is asked
> "Mini-case: an FMCG company's inventory days rose from 45 to 60. How do you diagnose?"

> [!tip] Strong answer includes
> - Decompose: raw material, WIP, FG; by SKU class and location
> - Candidate causes: forecast bias, MOQ, promotions, slow movers, lead times, safety-stock policy
> - Cash impact (each day of DIO = COGS/365 in ₹)
> - **Ask the interviewer:** "Did service level move, and was there a change in portfolio or channel?"

---
## 4. Forecasting and S&OP (Q19-Q24)
> 🔴 Tier 1 · _Key points:_ MAPE, bias, smoothing, FVA, S&OP, new products

### Definition
**Q19. MAD, MAPE, bias: when to use which?** MAD is in units, MAPE is relative but explodes near zero demand, bias (mean error) shows direction. Track bias first: it is systematic. See [[004 Demand Forecasting & Planning]].

**Q20. Exponential smoothing in one formula?** $F_{t+1} = \alpha A_t + (1 - \alpha)F_t$; higher $\alpha$ reacts faster but is noisier. Add trend (Holt) and seasonality (Holt-Winters). See [[004 Demand Forecasting & Planning]].

**Q21. How do you forecast a new product?** Analogous products, build-up by channel, Delphi and test markets, Bass diffusion, then update with early sales. See [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]].

**Q22. What is Forecast Value Added?** Compare each step of the forecast process with a naive forecast; steps that do not add accuracy should be dropped. See [[004 Demand Forecasting & Planning]].

**Q23. What is S&OP and what makes it work?** A monthly cross-functional cycle (demand review, supply review, pre-S&OP, executive meeting) producing one number and decisions on gaps. It works with executive ownership and financial reconciliation; see [[120 Integrated Business Planning (IBP) & S&OP Maturity]].

**Q24. Forecast error is 25% at SKU level; is that bad?** Not necessarily: aggregated across SKUs or longer horizons error falls; judge against forecastability (CoV), lead time and a naive benchmark. See [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]].

### Example
**N9 (smoothing).** Previous forecast 100, actual 120, $\alpha = 0.3$: $F = 0.3 \times 120 + 0.7 \times 100 = 106$.

**N10 (error metrics).** Actuals 100, 110, 90; forecasts 105, 100, 95. Errors $-5, +10, -5$. MAD $= 20/3 = 6.7$; MAPE $= (5/100 + 10/110 + 5/90)/3 = 6.5\%$; bias $= 0/3 = 0$: no bias, only noise, which suggests safety stock rather than model change.

### In the news
See news box. The shortage-era bullwhip started with distorted demand signals; see [[114 Bullwhip Effect, Beer Game & Information Sharing]].

### Interview angle
> [!question] How it is asked
> "Mini-case: sales and supply planning disagree every month and the forecast is always 15% over actual. What do you do?"

> [!tip] Strong answer includes
> - Identify the **bias** (consistent over-forecast) and its source (sales targets vs forecast, incentives)
> - Governance fix: separate targets from forecast, track FVA by contributor
> - Consequences: excess inventory in ₹, markdowns
> - **Ask the interviewer:** "Who owns the forecast and how are sales rewarded?"

---
## 5. Production Planning, Lean and Constraints (Q25-Q30)
> 🔴 Tier 1 · _Key points:_ MRP, takt, OEE, bottleneck, kanban, Little's law

### Definition
**Q25. MPS vs MRP vs RCCP?** MPS says what end items and when; MRP explodes the BOM to component orders using inventory and lead times; RCCP checks critical capacity against MPS. See [[005 Production & Operations Planning]], [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]].

**Q26. Define takt time and cycle time.** Takt = available time / customer demand; cycle time is the actual time per unit; the line must have cycle time at or below takt. See [[007 Lean Manufacturing]].

**Q27. What is OEE?** Availability × Performance × Quality; world-class often cited near 85%. See [[018 Capacity Management & OEE]].

**Q28. Theory of Constraints: five steps?** Identify, exploit, subordinate, elevate, repeat; throughput is set by the bottleneck. See [[005 Production & Operations Planning]].

**Q29. Little's Law?** $WIP = TH \times CT$; to cut lead time at constant throughput, cut WIP. See [[007 Lean Manufacturing]].

**Q30. Kanban vs MRP?** Kanban is pull for stable, repetitive flow; MRP plans from forecast and BOM; DDMRP blends them. See [[117 Demand-Driven MRP (DDMRP) & Buffer Management]].

### Example
**N11 (takt).** 450 minutes available, demand 90 units: takt $= 450/90 = 5$ min. If the process has four stations at 4, 5, 6, 3 minutes the bottleneck is 6 min, above takt, so the line makes $450/6 = 75$ units.

**N12 (OEE).** Availability 90%, performance 95%, quality 98%: $OEE = 0.90 \times 0.95 \times 0.98 = 83.8\%$.

**N13 (Little).** Throughput 20 units/hour, cycle time 3 hours: $WIP = 60$ units; cutting WIP to 40 gives CT $= 2$ hours.

**N14 (MRP netting).** Gross requirement 120, on hand 30, scheduled receipt 20: net $= 120 - 30 - 20 = 70$; lot-for-lot order of 70, offset by lead time.

### In the news
See news box. Toyota's 2011 and 2022 stoppages show where lean needs buffers ([[141 Supply Chain Disruption Case Library (2011-2026)]]).

### Interview angle
> [!question] How it is asked
> "Mini-case: a plant at 70% OEE wants to add a second shift. Would you?"

> [!tip] Strong answer includes
> - First, find the loss tree (availability, speed, quality) and the bottleneck
> - Value of 10 points of OEE vs capex and labour of a new shift
> - Demand check: is there demand to sell the extra output
> - **Ask the interviewer:** "What is the bottleneck, and what is the unmet demand?"

---
## 6. Logistics and Transportation (Q31-Q36)
> 🔴 Tier 1 · _Key points:_ Mode choice, Incoterms, 3PL, last mile, network, cost-to-serve

### Definition
**Q31. How do you choose a transport mode?** Trade-off of cost, speed, reliability, capacity and product value density; rail for bulk, road for flexibility, air for high-value urgent, sea for volume. See [[009 Logistics & Distribution]], [[125 Transportation Management Deep Dive]].

**Q32. Which Incoterms transfer risk where?** FOB: risk passes when goods are on board at origin port; CIF: seller pays freight and insurance but risk passes on board; DDP: seller bears all to the buyer's door. See [[126 International Trade Documentation, Customs & Trade Finance]].

**Q33. 3PL vs 4PL?** A 3PL runs physical logistics services; a 4PL orchestrates multiple providers and the design of the chain. See [[009 Logistics & Distribution]].

**Q34. Why is last-mile expensive?** Low drop density, failed deliveries, cash on delivery, address quality, returns; improve with density, batching and pickup points. See [[129 E-commerce & Quick-Commerce Fulfilment]].

**Q35. When does adding a warehouse help?** When service gain and transport savings exceed added fixed and inventory costs; test with network modelling. See [[113 Network Design & Facility Location Modelling]].

**Q36. What is a milk run?** A pre-planned route collecting from several suppliers in one truck to raise utilisation and frequency. See [[131 Automotive Supply Chain - JIT, Tiers & EVs]].

### Example
**N15 (pipeline inventory).** A lane carries ₹10 crore of goods a day and transit time rises from 25 to 35 days: extra pipeline inventory $= 10 \times 10 = ₹100$ crore; at 15% carrying cost the annual cost is ₹15 crore.

**N16 (truck load).** 24-tonne truck at ₹45,000 per trip carries 18 tonnes: ₹2,500/tonne; at 24 tonnes it is ₹1,875 (25% cheaper). Consolidation beats expediting.

**N17 (center of gravity).** Demand points A (0, 0) 300 units, B (10, 0) 100 units, C (5, 8) 100 units: $x = (0 + 1000 + 500)/500 = 3.0$; $y = (0 + 0 + 800)/500 = 1.6$; centre at (3.0, 1.6).

### In the news
See news box. Red Sea added about 9% to average cargo travel distance and moved freight rates sharply.

### Interview angle
> [!question] How it is asked
> "Mini-case: freight cost is 11% of sales for a client and they want it at 8%. How?"

> [!tip] Strong answer includes
> - Break freight cost into volume, rate, mode, utilisation, lane and service level
> - Levers: consolidation, mode shift (rail/coastal), contract renegotiation, network changes, return-load matching
> - Cost-to-serve by customer and order profile
> - **Ask the interviewer:** "How much is outbound vs inbound, and what is the average truck fill?"

---
## 7. Warehousing and Fulfilment (Q37-Q42)
> 🔴 Tier 1 · _Key points:_ Layout, slotting, picking, KPIs, cross-dock, automation

### Definition
**Q37. Pick methods?** Discrete, batch, zone, wave; choose by order profile (lines per order, SKUs). See [[010 Warehouse Management]].

**Q38. What is slotting?** Placing fast movers near the dock and at golden zone heights to cut travel. See [[010 Warehouse Management]], [[127 Warehouse Engineering - Racking, Sizing & Material Handling]].

**Q39. Key warehouse KPIs?** Dock-to-stock time, order accuracy, lines per labour hour, inventory accuracy, space utilisation, cost per order. See [[010 Warehouse Management]].

**Q40. Cross-dock: when does it work?** High volume, predictable inbound, reliable suppliers, and tight scheduling; no storage. See [[009 Logistics & Distribution]].

**Q41. When is automation justified?** High volume, labour intensive, stable SKU profile and payback within the lease or horizon; compare AMR, GTP and ASRS. See [[010 Warehouse Management]], [[128 Warehouse Labour, WES-WCS & Yard Management]].

**Q42. How do you cut e-commerce returns cost?** Quality and size guidance, better product data, return reasons analytics, grading and resale routing. See [[135 Reverse Logistics, Remanufacturing & EPR in India]].

### Example
**N18 (picker headcount).** 2,400 order lines a day, 80 lines per picker-hour, 8-hour shift: $2{,}400/(80 \times 8) = 3.75 \Rightarrow 4$ pickers (add 10-15% for absenteeism and peaks).

**N19 (fill rate and accuracy).** 960 units shipped of 1,000 ordered: line fill rate 96%; if 6 of 200 orders contain errors, accuracy is 97%.

**N20 (space).** 5,000 pallets, 4-high racking, 1.5 m² per pallet position, aisles and docks add 100% to floor area: $5000/4 \times 1.5 = 1{,}875$ m² storage, so about 3,750 m² total.

### In the news
See news box for the shipping context. For quick commerce see [[142 Company Supply Chain Case Library]].

### Interview angle
> [!question] How it is asked
> "Mini-case: a distribution centre misses shipping cut-offs in the peak season. What do you check?"

> [!tip] Strong answer includes
> - Flow analysis: inbound, putaway, pick, pack, dock
> - Labour planning against forecast; wave planning; slotting
> - Quick wins: temp labour, zone picking, cut-off rules
> - **Ask the interviewer:** "Where do orders wait longest, and what are the peak-to-average volumes?"

---
## 8. Quality Management (Q43-Q48)
> 🔴 Tier 1 · _Key points:_ Six Sigma, SPC, Cpk, COPQ, supplier quality

### Definition
**Q43. DMAIC in short?** Define, Measure, Analyse, Improve, Control; use for existing processes (DMADV for new designs). See [[008 Six Sigma & Quality Tools]].

**Q44. Cp vs Cpk?** $C_p = (USL - LSL)/6\sigma$ shows potential; $C_{pk} = \min\left(\frac{USL-\mu}{3\sigma}, \frac{\mu-LSL}{3\sigma}\right)$ accounts for centring. See [[008 Six Sigma & Quality Tools]], [[091 Statistical Quality Control (SQC)]].

**Q45. Special-cause vs common-cause variation?** Special causes are assignable and show on control charts as points beyond limits or patterns; common causes are inherent. See [[091 Statistical Quality Control (SQC)]].

**Q46. What is cost of poor quality?** Prevention, appraisal, internal failure, external failure; failures are usually the largest and prevention the cheapest lever. See [[011 Quality Management (TQM)]].

**Q47. PPAP, APQP, 8D?** APQP plans a launch, PPAP proves the supplier can make the part to spec at rate, 8D solves problems. See [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]].

**Q48. Rework vs scrap vs inspection?** Fix the process (poka-yoke, SPC) rather than inspect in quality. See [[007 Lean Manufacturing]].

### Example
**N21 (Cpk).** Spec 10.00 ± 0.30, mean 10.05, $\sigma = 0.08$: $C_p = 0.6/(6 \times 0.08) = 1.25$; $C_{pk} = \min(0.25, 0.35)/(0.24) = 1.04$. The process is capable in spread but off-centre; recentring to 10.00 would give $C_{pk} = 1.25$.

**N22 (RPN).** Severity 8, occurrence 4, detection 5: $RPN = 160$; after better detection (2): 64.

### In the news
See news box. Supply-side resilience and supplier quality now sit together in supplier-risk scorecards ([[015 Supply Chain Risk & Resilience]]).

### Interview angle
> [!question] How it is asked
> "Mini-case: customer returns have doubled for a component from one supplier. Walk me through your approach."

> [!tip] Strong answer includes
> - Contain (quarantine, sort, 100% inspection), then 8D root-cause
> - Pareto of defects; compare with Cpk and change history
> - Supplier audit and corrective action; cost of poor quality in ₹
> - **Ask the interviewer:** "What changed in the process, material or tooling before returns rose?"

---
## 9. Risk and Resilience (Q49-Q54)
> 🔴 Tier 1 · _Key points:_ Mapping, TTR/TTS, dual sourcing, BCP, tariffs, chokepoints

### Definition
**Q49. How do you identify supply chain risk?** Map to tier-n, identify single points of failure, score with likelihood-impact or FMEA RPN, and assign owners. See [[015 Supply Chain Risk & Resilience]].

**Q50. Resilience vs efficiency: how to trade off?** Invest selectively where criticality and time-to-recover exceed time-to-survive; buffers and second sources only for gating items. See [[141 Supply Chain Disruption Case Library (2011-2026)]].

**Q51. What lessons does Toyota 2011 teach?** Hidden tier-2 risk, single-site chips; Toyota mapped suppliers and asked for 2-6 months of extra stock on key parts. See [[141 Supply Chain Disruption Case Library (2011-2026)]].

**Q52. What does a control tower do?** Provides end-to-end visibility, alerts and workflows across plan, source, make, deliver. See [[016 Digital Supply Chain & Industry 4.0]].

**Q53. Should a company reshore?** Compare total landed cost including risk, tariffs, lead time and inventory; often a China+1 or regional network beats full reshoring. See [[014 Global SCM & Sustainability]].

**Q54. How do you respond to a sudden tariff?** Quantify landed-cost change, scenario-weight duration, re-source, pass through, bonded storage, contract clauses. See [[126 International Trade Documentation, Customs & Trade Finance]].

### Example
**N23 (dual-source failure).** Each of two independent suppliers fails with 5% probability: both fail $0.05 \times 0.05 = 0.25\%$ (assuming independence; correlated risks such as the same region make it far worse).

**N24 (break-even probability).** Gap = TTR − TTS = 3 weeks, 10,000 units a week, ₹2,000 contribution: loss ₹6 crore. A buffer costs ₹18 lakh a year: break-even event probability $= 0.18/6 = 3\%$ per year.

**N25 (tariff scenario).** 50% chance duty stays 30%, 20% chance 145%, 30% chance 10%: expected duty $= 15 + 29 + 3 = 47\%$.

### In the news
See news box: Red Sea (route risk), Nexperia (supplier and geopolitical risk), tariffs (policy risk).

### Interview angle
> [!question] How it is asked
> "Mini-case: a key tier-2 supplier in a flood zone supplies 60% of a part. What should we do in the next 90 days?"

> [!tip] Strong answer includes
> - Immediate: visibility, buffer, early warning, supplier BCP check
> - 30-60 days: qualify an alternate; shift volume gradually
> - Quantify the cost of buffer vs expected loss; use TTR/TTS
> - **Ask the interviewer:** "What does the tier-2 supplier's recovery time look like and how much stock do we hold?"

---
## 10. Digital Supply Chain, Analytics and ERP (Q55-Q60)
> 🔴 Tier 1 · _Key points:_ Control tower, AI, SAP, KPI trees, data quality

### Definition
**Q55. Where does AI add value in SCM?** Demand forecasting, inventory optimisation, ETA prediction, supplier risk sensing, routing; value depends on data quality and decision integration. See [[016 Digital Supply Chain & Industry 4.0]], [[099 ML for Operations & SCM]].

**Q56. What is a digital twin?** A model of the physical chain used to simulate scenarios; mature use is network and inventory simulation. See [[016 Digital Supply Chain & Industry 4.0]].

**Q57. SAP MM, PP, SD in one sentence each?** MM manages procurement and inventory, PP production planning and execution, SD order-to-cash. See [[013 ERP & Enterprise Systems (SAP-Oracle)]], [[080 SAP MM — Materials Management]].

**Q58. Why does master data matter?** Wrong lead times, units or lot sizes distort MRP and safety stock; garbage in, garbage out. See [[175 Data Quality, Master Data & Data Governance]].

**Q59. Build a KPI tree for OTIF.** OTIF = on-time × in-full; decompose by cause: order entry, inventory availability, picking, transport delay; assign owners. See [[012 Supply Chain Analytics & KPIs]].

**Q60. What would you automate first with RPA?** High-volume, rule-based, stable processes such as invoice matching or order entry. See [[016 Digital Supply Chain & Industry 4.0]], [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]].

### Example
**N26 (OTIF).** 1,000 orders: 920 on time, 950 in full, and 880 both on time and in full: OTIF $= 880/1000 = 88\%$. Multiplying 92% × 95% = 87.4% would assume the two failures are independent; always count orders that are both on time and in full.

**N27 (perfect order).** Perfect order rate $= $ OTIF $\times$ damage-free $\times$ correct documents: $0.88 \times 0.99 \times 0.98 = 85.4\%$.

### In the news
See news box. Visibility to tier-2/3 is the data problem behind both Nexperia and Red Sea responses.

### Interview angle
> [!question] How it is asked
> "Mini-case: a CEO wants an AI forecasting project. How do you decide whether it is worth it?"

> [!tip] Strong answer includes
> - Start from the decision and value: error to inventory and service in ₹
> - Data readiness, baseline (naive and current), pilot with FVA measurement
> - Process change and ownership (planners), not just a model
> - **Ask the interviewer:** "What does forecast error cost us today and which decisions use it?"

---
## 11. India Context: Policy, GST and Structure (Q61-Q66)
> 🔴 Tier 1 · _Key points:_ Logistics cost, NLP, Gati Shakti, GST, PLI, route-to-market

### Definition
**Q61. Why is India's logistics cost high?** Heavy dependence on road, fragmented trucking, low rail share, poor utilisation, dwell times, documentation and last-mile fragmentation. Verified current estimates and the LEADS index are in [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]; see also [[009 Logistics & Distribution]].

**Q62. How did GST change supply chain networks?** Removing interstate entry barriers and cascading taxes let firms consolidate many state warehouses into fewer hubs; see [[227 GST & Indirect Tax for Supply Chains]].

**Q63. What are PLI schemes for?** To raise domestic manufacturing and exports in selected sectors with incentives tied to incremental sales; see [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

**Q64. India's FMCG route-to-market?** Distributors and kirana outlets in general trade, modern trade, e-commerce and quick commerce; see [[130 FMCG & Retail Distribution - India Route-to-Market]].

**Q65. What is special about Indian perishables chains?** High losses from weak cold chain, many intermediaries, and mandi structure; see [[133 Food, Agri & Perishables Supply Chain - India]].

**Q66. Why do MSME payment terms matter?** MSMEs have limited working capital; the 45-day rule and TReDS shape buyers' payables strategy; see [[136 Supply Chain Finance & Working Capital]].

### Example
**N28 (logistics cost saving).** Illustrative: a company has ₹2,000 crore of sales and logistics cost of 12% (₹240 crore). A 1.5 percentage point reduction through consolidation and rail mix saves $0.015 \times 2000 = ₹30$ crore: an increase in EBITDA margin of 1.5 points with no volume growth.

### In the news
Not tied to the shared news box; use the verified numbers in [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]] before quoting any percentage of GDP.

### Interview angle
> [!question] How it is asked
> "What should India do to cut logistics cost?"

> [!tip] Strong answer includes
> - Structure: infrastructure, mode mix, process and documentation, technology, institutions
> - Examples: dedicated freight corridors, multimodal parks, ULIP, e-way bills
> - Company-level levers too (consolidation, rail, backhaul)
> - **Ask the interviewer:** "Are we asking at national policy level or for a specific company?"

---
## 12. Finance, KPIs and Working Capital (Q67-Q72)
> 🔴 Tier 1 · _Key points:_ Cash-to-cash, ROIC, carrying cost, cost-to-serve, supply chain finance

### Definition
**Q67. Cash-to-cash cycle?** DIO + DSO − DPO; the days cash is tied up. See [[012 Supply Chain Analytics & KPIs]], [[136 Supply Chain Finance & Working Capital]].

**Q68. Inventory carrying cost components?** Capital, storage, service, risk (obsolescence, shrink); typically 18-30% of value a year. See [[003 Inventory Management]], [[110 Cost Accounting for Operations]].

**Q69. How does supply chain affect ROIC?** Margin up via cost and price; invested capital down via inventory and fixed assets; see [[108 Financial Statements & Ratios]].

**Q70. What is reverse factoring?** The buyer's credit is used to finance suppliers' receivables early at lower cost; see [[136 Supply Chain Finance & Working Capital]].

**Q71. Cost-to-serve?** Fully loaded cost of serving a customer or channel, which reveals unprofitable accounts; see [[138 Order Management, Customer Service & Cost-to-Serve]].

**Q72. Capex vs opex logic for a new warehouse?** Compare NPV of owning vs leasing or 3PL, with flexibility value; see [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]].

### Example
**N29 (C2C).** DIO 60, DSO 45, DPO 50: cash cycle $= 60 + 45 - 50 = 55$ days. With COGS ₹3,650 crore a year (₹10 crore a day) each day is worth ₹10 crore of cash for inventory and payables; cutting DIO by 5 days releases ₹50 crore.

**N30 (2/10 net 30).** Skipping a 2% discount for 20 extra days costs an annualised $\frac{2}{98} \times \frac{365}{20} \approx 37\%$: take the discount if the cost of capital is below this.

### In the news
See news box: tariff front-loading and buffer stocks raise working capital, so cash-cycle questions are timely.

### Interview angle
> [!question] How it is asked
> "Mini-case: the CFO wants ₹100 crore of cash released from working capital. Where do you start?"

> [!tip] Strong answer includes
> - Decompose DIO, DSO, DPO and compare with peers
> - Inventory levers by segment (slow movers, safety stock, MOQs), payables terms, SCF
> - Service-level guardrails; quantify each lever in ₹
> - **Ask the interviewer:** "What is the target service level, and are there seasonality or covenants to respect?"

---
## 13. Mini-Case Playbook: Five Cases with Skeleton Answers
> 🔴 Tier 1 · _Key points:_ Structure, hypothesis, numbers, recommendation, risks

### Definition
Use the same skeleton on every case: **clarify** (objective, scope, constraints), **structure** (cost, service, risk, capability), **hypothesise**, **quantify**, **recommend with risks and next steps**. Linked frameworks: [[026 Case Interview — Operations Cases]], [[024 Consulting Frameworks]], [[162 Structured Communication - SCQA, Storylines & Case Delivery]].

1. **Reduce inventory 20% without hurting service** → segment SKUs; targeted safety stock; supplier lead times; slow-mover action (sub-topic 3).
2. **Design a distribution network for a new FMCG brand in west India** → demand clusters, service promise, number of DCs by cost curve ([[113 Network Design & Facility Location Modelling]]).
3. **A supplier is late 30% of the time** → quantify impact, root cause by supplier (capacity, planning, transport), scorecard, second source ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).
4. **Quick-commerce dark store is losing money** → unit economics: AOV, margin, delivery cost, fixed cost per day (see [[142 Company Supply Chain Case Library]] sub-topic 10).
5. **Should a company dual-source a critical component?** → TTR/TTS gap, break-even probability, cost of qualification ([[141 Supply Chain Disruption Case Library (2011-2026)]] sub-topic 14).

### Example
**Case 4 numbers.** AOV ₹450, gross margin 18% (₹81), delivery ₹40, so contribution ₹41. Fixed cost ₹9 lakh a month gives break-even $9{,}00{,}000/41 \approx 21{,}950$ orders a month ($\approx$ 730 a day). If actual volume is 500 a day the store loses $(730 - 500) \times 30 \times 41 \approx ₹2.8$ lakh a month. Levers: AOV (+₹50 at 18% adds ₹9 per order), delivery cost (batching), ads or private label margin.

### In the news
See news box. Mini-cases on rerouting, tariffs and chips are now routinely used in consulting interviews.

### Interview angle
> [!question] How it is asked
> "Our client's lead time from China doubled. How do we respond?"

> [!tip] Strong answer includes
> - Clarify cause: route, port congestion, supplier delay
> - Quantify pipeline inventory and stock-out risk, then options (mode, route, supplier, buffer)
> - Costs vs service targets; quick wins vs structural
> - **Ask the interviewer:** "Which SKUs are critical and how much stock cover do we have?"

---
## 14. ⭐ Advanced: Questions to Ask the Interviewer and a Last-Week Drill
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Good questions show structured thinking. Use these (pick two):
1. "What does the supply chain look like end to end: where are the biggest cost and service gaps today?"
2. "How do you measure success: OTIF, inventory days, cost-to-serve, or resilience?"
3. "How much of the network is single-sourced or single-site, and how visible are tier-2 suppliers?"
4. "How are planning decisions made: who owns the forecast, and how does S&OP resolve conflicts?"
5. "Which technology investments are in flight (planning, control tower, WMS/TMS), and what is the adoption challenge?"
6. "What did the last major disruption teach the team?" (links to [[141 Supply Chain Disruption Case Library (2011-2026)]])
7. "How does the team balance service, cost and working capital?"

**Last-week drill.** Day 1: Q1-Q18. Day 2: Q19-Q36. Day 3: Q37-Q54. Day 4: Q55-Q72. Day 5: one mini-case aloud (sub-topic 13). Day 6: two company cases from [[142 Company Supply Chain Case Library]]. Day 7: guesstimates in [[105 Operations & SCM Guesstimates]] and a mock with a friend.

### Example
**Deriving the right number.** To compare two policies in an interview, say: "I will compare total cost = ordering + holding + stock-out." For N4 (EOQ 775), a policy of ordering 1,200 units costs $\frac{12000}{1200}(500) + \frac{1200}{2}(20) = 5{,}000 + 12{,}000 = ₹17{,}000$ versus ₹15,492: **9.7% more** ($17{,}000/15{,}492 = 1.097$). Showing the cost of deviating from the optimum (flat near the optimum) is a strong way to demonstrate judgment.

### In the news
See news box. Closing with one live example (Red Sea, Nexperia or tariffs) usually lands well.

### Interview angle
> [!question] How it is asked
> "Do you have any questions for us?"

> [!tip] Strong answer includes
> - Two specific, researched questions tied to the company's chain
> - One question about the role and its measures of success
> - No questions answerable from the website
> - A short thank-you that restates fit
