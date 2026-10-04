---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Supply Chain Strategy - Fit, Segmentation & Maturity"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 13
---
# Supply Chain Strategy - Fit, Segmentation & Maturity

⬅ [[111 SCOR Model & Supply Chain Process Frameworks]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[113 Network Design & Facility Location Modelling]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. From Competitive Strategy to Supply Chain Strategy]]
2. [[#2. Fisher: Functional vs Innovative Products]]
3. [[#3. Chopra-Meindl Strategic Fit: Implied Uncertainty vs Responsiveness]]
4. [[#4. The Efficient Frontier: Cost versus Responsiveness]]
5. [[#5. Lee's Triple-A Supply Chain]]
6. [[#6. Gattorna's Dynamic Alignment: Buyer Behaviour as the Starting Point]]
7. [[#7. Supply Chain Segmentation: Demand, Supply and Cost-to-Serve]]
8. [[#8. Lean, Agile and Leagile]]
9. [[#9. Decoupling Point: MTS, ATO, MTO, ETO]]
10. [[#10. Supply Chain Maturity Models]]
11. [[#11. Strategy-to-Capability Mapping]]
12. [[#12. Worked Case: Re-aligning a Consumer-Durables Supply Chain]]
13. [[#13. ⭐ Advanced: Resilience, Dual Networks and the Limits of Fisher]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): fast-fashion speed and "network-centric" chains show strategy-to-capability fit in action
> **Gartner Supply Chain Top 25 (17 June 2026).** Schneider Electric ranked first for the fourth year in a row (composite score 7.05), followed by NVIDIA (6.42), Walmart (5.78) and Cisco (5.77). Gartner's summary of what separates leaders: "building autonomous workforces, investing in network-centric strategies and orchestrating supply chains end-to-end". Peer and Gartner-expert opinion carry 25% each of the score, ESG 20%, inventory as % of revenue 10%. ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-06-17-gartner-announces-2026-rankings-of-the-global-supply-chain-top-25); scores also in [Supply Chain 24/7](https://www.supplychain247.com/article/gartner-2026-global-supply-chain-top-25-rankings))
>
> **Inditex (Zara), the textbook responsive chain.** Wikipedia's summary of published reporting: Inditex reported 2024 revenue of about **€38.63 bn** and net profit of about **€5.86 bn** across **5,563 stores**; the design-to-shelf process is reported to take "as little as 15 days in some cases"; about half of Zara merchandise is made in company-owned or nearby factories (Spain, Portugal, Turkey) while longer-life basics come from Asia; fashion items can leave shelves within four weeks. These are secondary-source figures: check Inditex's annual report before quoting a precise number. ([Inditex](https://en.wikipedia.org/wiki/Inditex), [Zara](https://en.wikipedia.org/wiki/Zara_(retailer)))
>
> **Shein's test-and-repeat model.** Reported to limit initial production runs to "about 100 items" and scale up only if the small batch sells, and to produce items "as quickly as three days after the identification of a trend". In April 2025 the US ended the duty-free de minimis exemption for sub-$800 parcels, which had supported such direct-to-consumer models, a reminder that a responsive design depends on policy as well as operations. ([Shein](https://en.wikipedia.org/wiki/Shein))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. From Competitive Strategy to Supply Chain Strategy
> 🔴 Tier 1 · _Key points:_ strategic fit, competitive priorities, supply chain as a source of advantage

### Definition
**Competitive strategy** defines the customer needs a company aims to serve (low price, variety, speed, quality, innovation). **Supply chain strategy** defines the *capabilities* that deliver those needs: how inventory, transport, facilities, sourcing, information and pricing are set (the drivers in [[001 SCM Introduction & Fundamentals]]). **Strategic fit** (Chopra and Meindl) means the supply chain's level of responsiveness matches the uncertainty and needs of the targeted customer segment.

Three steps to build fit: (1) understand the **customer** and the **implied demand uncertainty** of the segment; (2) understand the **supply chain's capabilities** (its position on the efficiency-responsiveness spectrum); (3) achieve fit by adjusting capabilities, or by changing the target segment. Misfit comes from three sources: strategy changes without chain changes, product portfolio widening beyond the chain's design, and **different functions pursuing different goals** (sales wants availability, finance wants inventory down). Link with [[020 Operations Strategy]] and [[023 Business Fundamentals & Strategy]].

### Example
A company selling air-conditioners positions on "lowest cost" but runs a chain built for quick delivery with high safety stock and air freight: a classic misfit (responsive chain, efficiency strategy). The fix is either to change the chain (consolidate DCs, ocean freight, lower service) or to change the positioning (premium pricing with delivery promise).

### In the news
See news box. Gartner's 2026 commentary on "network-centric strategies" is a statement that leaders choose a chain shape to fit strategy, not the reverse.

### Interview angle
> [!question] How it is asked
> "A client says its supply chain is expensive. How would you decide whether that is a problem?"

> [!tip] Strong answer includes
> - Cost is a problem only relative to the strategy: first ask which customer needs the chain must serve
> - Strategic fit and the three-step test
> - Evidence of misfit: high expediting, high stock plus stock-outs, margin erosion on responsive SKUs
> - Fix by aligning capabilities or by changing segments, not just cutting cost

---

## 2. Fisher: Functional vs Innovative Products
> 🔴 Tier 1 · _Key points:_ physically efficient vs market-responsive chain; demand predictability, margin, life cycle

### Definition
Marshall Fisher (HBR, 1997, "What Is the Right Supply Chain for Your Product?") argued that the chain must fit the **product's demand pattern**, not just industry norms.

| | **Functional** (staples) | **Innovative** (fashion, tech, new launches) |
|---|---|---|
| Demand | Stable, predictable (forecast error ~10%) | Volatile (forecast error often 40-100%) |
| Product life cycle | Long (2+ years) | Short (3 months to 1 year) |
| Contribution margin | Low (5-20%) | High (20-60%) |
| Variety | Low | High |
| Markdown at end | Low | High and uncertain |
| Chain required | **Physically efficient**: low cost, high utilisation, minimal inventory | **Market-responsive**: buffer capacity and stock, speed, flexibility, supplier collaboration |
| Main risk | Wasted cost | Stock-outs and markdowns (mismatch costs) |

(The ranges above are the indicative bands associated with Fisher's framework; treat them as teaching ranges, not hard thresholds.) The two failure modes are **efficient chain for innovative product** (stock-outs and mark-downs) and **responsive chain for functional product** (needless cost).

### Example
Jackets: price ₹2,500, salvage ₹300 after season, mean demand 1,000. Offshore chain: cost ₹1,000, order months ahead, forecast s.d. 600. Quick-response (near-shore) chain: cost ₹1,250, order after early sales, s.d. 150. Newsvendor critical ratios: offshore $(2500-1000)/(2500-300)=0.68$, order about 1,284, expected sales 876, **leftover 407**, profit about **₹10.3 lakh**; QR critical ratio 0.568, order 1,026, expected sales 952, **leftover 74**, profit about **₹11.2 lakh**. Break-even QR unit cost is about ₹1,340 (a 34% premium): the faster chain wins despite higher unit cost. For a staple (price ₹100, efficient cost ₹70, s.d. 60, salvage ₹60) the responsive option (cost ₹80, s.d. 20) earns only about ₹19.7k against ₹29.2k: responsiveness destroys value on a functional product. (See the newsvendor model in [[003 Inventory Management]].)

### In the news
See news box. Zara (reported design-to-shelf of days to weeks, near-shore production for fashion lines, Asian sourcing for basics) shows a firm running both chains in one portfolio.

### Interview angle
> [!question] How it is asked
> "What supply chain strategy fits a premium smartphone vs a staple like salt?"

> [!tip] Strong answer includes
> - Fisher's two columns with the key attributes (predictability, margin, life cycle)
> - The two mismatch failure modes
> - A numeric or cost-of-mismatch argument (markdown vs expediting)
> - Caveat: real products sit on a spectrum, and one firm has many segments

---

## 3. Chopra-Meindl Strategic Fit: Implied Uncertainty vs Responsiveness
> 🔴 Tier 1 · _Key points:_ implied uncertainty spectrum, responsiveness spectrum, zone of strategic fit

### Definition
Chopra and Meindl generalise Fisher with two spectra:
- **Implied demand uncertainty**: the uncertainty the supply chain must handle for the customer need being served. It combines **demand uncertainty** (forecast error) with the effect of customer needs: wide range of quantity per order, short lead time wanted, wide variety, high service level, narrow margins and rapid product change all *raise* implied uncertainty. It runs from "certain demand" (salt, staple grain) to "highly uncertain" (new product launch, custom-built).
- **Supply chain responsiveness**: ability to respond to wide ranges of quantity, short lead times, variety, service levels, innovation and uncertain supply. It runs from **efficient** to **highly responsive**. Responsiveness costs money.

The **zone of strategic fit** is the diagonal band where the right responsiveness matches the implied uncertainty. High-uncertainty demand needs a responsive chain; low-uncertainty demand an efficient one. Because customer segments have different needs, a company often needs **several chains** or one chain with segmented policies. Fit needs **scope**: all stages (and all functions) must share the same position, so a responsive retailer with efficient, slow suppliers is not fit.

### Example
A pharma distributor in Nashik serves (a) chronic-medicine refills for hospitals: low uncertainty, wide forecasts, low urgency; (b) emergency orders from clinics within 4 hours. Implied uncertainty for (b) is high though *demand* is the same drug: the response-time need raises it. One chain (daily milk-run from a regional DC) cannot serve both; the distributor sets a stocked "emergency kit" at a local node for (b) and a consolidated weekly replenishment for (a).

### In the news
See news box. Shein's 100-unit tests and Zara's weekly design rotation are high-responsiveness answers to high implied uncertainty (fashion trends), with trade-offs in cost and complexity.

### Interview angle
> [!question] How it is asked
> "How do you decide how responsive a supply chain should be?"

> [!tip] Strong answer includes
> - Implied uncertainty (not just demand variability): lead-time needs, variety, service level
> - Position on the responsiveness spectrum and cost of moving along it
> - Fit across all stages and functions, not just the factory
> - Segment-specific policies

---

## 4. The Efficient Frontier: Cost versus Responsiveness
> 🔴 Tier 1 · _Key points:_ trade-off curve, move to the frontier then along it, drivers as levers

### Definition
For any set of technologies and drivers there is an **efficient frontier**: the lowest cost achievable for each level of responsiveness. A firm *inside* the frontier can improve both (better execution: remove waste, improve forecasting, share information). A firm *on* the frontier can only trade cost for responsiveness by changing driver settings:

| Driver | Toward efficiency | Toward responsiveness |
|---|---|---|
| Inventory | Low, centralised, cycle-stock driven | High buffers, forward positioned |
| Transport | Ocean/rail, full loads, consolidation | Air/express, frequent small shipments |
| Facilities | Few, large, specialised | Many, flexible, near customers |
| Information | Standard, periodic | Real-time, shared, collaborative |
| Sourcing | Lowest price, single/offshore | Speed and flexibility, multiple/nearshore |
| Pricing | Stable, volume-based | Dynamic, lead-time based |

**Strategy sequence:** first move to the frontier (eliminate waste: this is free), then choose a position on it that matches the segment. Do not trade along the frontier as a substitute for fixing inefficiency.

### Example
Chain A delivers 94% service at 12% of revenue cost; chain B 98% at 14%. A competitor delivers 98% at 12.5%: both A and B are *inside* the frontier, so the first job is execution (see [[012 Supply Chain Analytics & KPIs]]). A firm that wants to go from 94% to 98% service on the frontier must buy it: with normal demand the safety factor $z$ rises from 1.55 (94% cycle service) to 2.05 (98%), a 32% bigger buffer.

### In the news
See news box. Gartner's methodology blends cost and asset metrics (inventory % revenue, ROPA) with opinion scores, i.e. it rewards firms near the frontier on cost and still credible on service.

### Interview angle
> [!question] How it is asked
> "Can a company be both low cost and highly responsive?"

> [!tip] Strong answer includes
> - Yes, by moving to the frontier through better execution and information; on the frontier, no without technology change
> - Driver table, one example per driver
> - Cost of each extra point of service rises steeply (safety stock logic)
> - Technology or design changes (postponement, nearshoring, automation) shift the frontier itself

---

## 5. Lee's Triple-A Supply Chain
> 🔴 Tier 1 · _Key points:_ agility, adaptability, alignment; beyond speed and cost

### Definition
Hau Lee (HBR, 2004, "The Triple-A Supply Chain") argued that top performers achieve lasting advantage with three qualities, not just speed and cost:
1. **Agility**: respond quickly to short-term changes in demand or supply with little disruption (share data with suppliers and customers, build contingency and postponement, keep a pool of dependable logistics partners, design products with common parts).
2. **Adaptability**: adjust the chain's design to structural shifts in markets, strategies, technologies (find new suppliers and markets as economies move, use intermediaries to track trends, develop products for the new reality, know your product life cycle).
3. **Alignment**: align the incentives of all partners so that each one improving its own results also improves the chain's results (share information, risk, cost and reward; define roles and responsibilities clearly).

Agility handles volatility, adaptability handles structural change, alignment keeps partners from sub-optimising (compare double marginalisation in [[137 Supply Chain Contracts & Game Theory]]). Lee's central point: efficiency and responsiveness alone do not give *lasting* advantage because they erode when markets move and partners optimise locally.

### Example
A Pune auto-component supplier to a carmaker (illustrative): **agility** = weekly schedule sharing plus a buffer of semi-finished parts; **adaptability** = qualifying EV-component lines as the carmaker's mix shifts; **alignment** = gain-share agreement on cost-down ideas so the supplier does not hide savings.

### In the news
See news box. Gartner's 2026 emphasis on "orchestrating supply chains end-to-end" is alignment across partners; autonomous planning supports agility.

### Interview angle
> [!question] How it is asked
> "Beyond cost and speed, what makes a supply chain a competitive advantage?"

> [!tip] Strong answer includes
> - Define A-A-A with a one-line example each
> - Link: agility (days), adaptability (years), alignment (always)
> - Incentive misalignment as the usual failure (contracts, shared KPIs)
> - Relate to resilience: see [[015 Supply Chain Risk & Resilience]]

---

## 6. Gattorna's Dynamic Alignment: Buyer Behaviour as the Starting Point
> 🔴 Tier 1 · _Key points:_ segment by buyer behaviour, multiple chains, culture and leadership alignment

### Definition
John Gattorna's **dynamic alignment** (Living Supply Chains, 2006) argues that supply chain design should start from **customer buying behaviour** (the "dominant behavioural logic" of each segment), then align strategy, **organisation, culture and leadership** with it, rather than starting from product type or channel. Four generic behaviours are commonly summarised:
- **Collaborative**: relationship-driven, wants joint planning (key accounts, long-term contracts).
- **Lean / efficient (transactional)**: price-and-reliability driven, predictable demand.
- **Agile / responsive**: wants speed and a dependable response to variable, urgent demand.
- **Fully flexible (innovative)**: needs problem-solving for unique or unpredictable needs (project and crisis demand).

The key claim: each behaviour needs a **different supply chain design and a different management culture**; one chain for all segments creates misalignment. "Dynamic" means the segments and the alignment must be re-checked as behaviour shifts. (Categories are paraphrased from the framework; exact labels differ between Gattorna's publications, so name the idea rather than reciting labels.)

### Example
A Mumbai industrial-chemicals distributor: anchor customers (collaborative, joint forecasts and VMI), small traders (lean: weekly milk-run, price list), plant-shutdown emergencies (agile: 24-hour tankers from a buffer), and R&D custom blends (fully flexible: a dedicated technical team). Four service models, four cost profiles, one customer relationship map.

### In the news
See news box. Segmenting by what customers value, as with Shein's data-driven tests versus Zara's store-led signals, is the practical form of "behaviour first".

### Interview angle
> [!question] How it is asked
> "Why not just segment customers by revenue (A, B, C)?"

> [!tip] Strong answer includes
> - Revenue tells you value, not what service model fits; behaviour does
> - Gattorna's four behaviours and why culture and leadership must follow
> - Need to verify with data (order patterns, lead-time needs, price sensitivity)
> - Governance: a segment owner and per-segment KPIs

---

## 7. Supply Chain Segmentation: Demand, Supply and Cost-to-Serve
> 🔴 Tier 1 · _Key points:_ ABC-XYZ, demand and supply characteristics, cost-to-serve, policy per segment

### Definition
**Segmentation** groups products and customers by what they need and what they cost, then designs a distinct policy for each. Common axes:
- **Demand side**: volume or value (ABC), variability (XYZ by coefficient of variation $CV=\sigma/\mu$), channel, order profile, service need, margin.
- **Supply side**: lead time, supplier reliability, supply risk, changeover cost, shelf life.
- **Cost-to-serve (CTS)**: the full cost to deliver an order line to a segment (handling, freight, expediting, returns, credit): contribution after CTS decides which segments to serve how. See [[138 Order Management, Customer Service & Cost-to-Serve]] and ABC/XYZ in [[012 Supply Chain Analytics & KPIs]].

A policy menu per segment: service level, inventory location, review frequency, replenishment mode, transport mode, planning cadence.

### Example
Appliance maker, revenue ₹2,000 cr (figures in ₹ crore):

| Segment | Revenue | Gross margin | Cost-to-serve | Contribution | Contribution % |
|---|---|---|---|---|---|
| Core fast movers (X) | 1,100 | 22% = 242 | 6% = 66 | 176 | 16.0% |
| Seasonal/promo (Y) | 400 | 28% = 112 | 11% = 44 | 68 | 17.0% |
| Long tail (Z) | 300 | 30% = 90 | 22% = 66 | 24 | **8.0%** |
| Projects (MTO) | 200 | 25% = 50 | 9% = 18 | 32 | 16.0% |
| **Total** | 2,000 | | | **300** | 15.0% |

The long tail has the best gross margin and the worst contribution: it eats 22 points of cost-to-serve. Actions: pull Z to make-to-order or a central slow-mover stock, raise minimum order values, rationalise SKUs. Moving long-tail contribution from 8% to 12% adds 300 × 0.04 = **₹12 cr**.

### In the news
See news box. Gartner highlights network-centric orchestration; cost-to-serve segmentation is the analytical basis for deciding which nodes serve which flows.

### Interview angle
> [!question] How it is asked
> "The client has one distribution model for 700 SKUs and thousands of outlets. What would you do?"

> [!tip] Strong answer includes
> - Segment on at least two axes (value x variability), then add cost-to-serve
> - A policy table per segment (service level, stock position, mode)
> - Quantification: contribution after cost-to-serve, not gross margin
> - Implementation: governance, systems that support segment-specific parameters, change management

---

## 8. Lean, Agile and Leagile
> 🔴 Tier 1 · _Key points:_ market winners and qualifiers, lean for volume, agile for volatility, leagile with decoupling point

### Definition
- **Lean** (see [[007 Lean Manufacturing]]): remove waste, level schedules, high utilisation; right for **high volume, low variety, predictable** demand where **cost** is the order winner.
- **Agile**: respond to volatile, unpredictable demand; spare capacity, flexibility, short lead times, information-rich; right where **availability and speed** win orders.
- **Leagile** (Naylor, Naim and Berry, 1999): lean upstream, agile downstream, split at the **decoupling point**; typical in postponement and mass-customisation (see [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]).

Christopher and Towill's **market qualifier / order winner** idea: qualifiers (what you must have to be considered) differ from order winners (what wins the order); lean suits cost as winner and service as qualifier, agile the opposite. Lean is not the same as efficient; agile is not the same as responsive in the strict Chopra sense, but they are used loosely as synonyms in exams.

### Example
A two-wheeler maker (illustrative, not a description of any named firm): engine and frame (stable volume, low variety) built lean in level schedules; colour, graphics, accessory fitment (variety, seasonality) done agile at regional hubs or at the dealer, after the order. The decoupling point is the semi-finished bike.

### In the news
See news box. Zara blends both: basics lean from Asia, fashion lines agile close to home.

### Interview angle
> [!question] How it is asked
> "Is lean or agile better? What about both?"

> [!tip] Strong answer includes
> - Conditions for each (volume, variety, variability, order winner)
> - Leagile and the decoupling point as the integrating device
> - Order qualifiers vs order winners
> - Where lean fails (no buffers, post-COVID) and where agile fails (cost, complexity)

---

## 9. Decoupling Point: MTS, ATO, MTO, ETO
> 🔴 Tier 1 · _Key points:_ customer order decoupling point, lead-time tolerance, postponement

### Definition
The **customer order decoupling point (CODP)** is where the chain switches from **forecast-driven** (push, upstream) to **order-driven** (pull, downstream). Positions:

| Strategy | Decoupling point | Customer lead time = | Typical |
|---|---|---|---|
| **Make-to-stock (MTS)** | Finished goods | Delivery only | Soaps, Parle-G, standard tyres |
| **Assemble-to-order (ATO)** | Components or modules | Assembly + delivery | PCs, modular kitchens, cars with options |
| **Make-to-order (MTO)** | Raw material or purchased parts | Make + assembly + delivery | Industrial machinery variants |
| **Engineer-to-order (ETO)** | Design | Design + all downstream | Turbines, ships, custom plant |

Move the CODP **upstream** (towards ETO) to cut stock and obsolescence and gain customisation; move it **downstream** (towards MTS) to cut customer lead time. Choose the position **just upstream of where cumulative lead time equals the customer's tolerance**, then reduce variety upstream of the point (commonality) and keep post-point steps short and flexible.

### Example
Product lead-time stack: procure 21 days, fabricate 7, assemble 3, ship 2. Customer tolerates **5 days**. MTS: lead time 2 days (OK, high stock of 120 end-item variants). ATO with modules stocked: 3 + 2 = **5 days** (just meets). MTO from raw material: 7 + 3 + 2 = 12 days (21 more if parts not stocked): fails. **ATO is the minimal-stock option that meets the promise.** Stock effect: 6 colours x 5 sizes x 4 options = 120 end items, each mean 10/week and s.d. 5/week, 3-week lead time, $z=1.65$. Holding at end-item level: safety stock $120 \times 1.65 \times 5 \times \sqrt{3}\approx$ **1,715 units**. Holding modules (6 + 5 + 4 = 15 items; each module serves 20, 24 or 30 variants so its s.d. is $5\sqrt{20}$, $5\sqrt{24}$ or $5\sqrt{30}$): about **1,047 units**, **39% lower**, before counting the benefit of lower obsolescence.

### In the news
See news box. Shein's small test batches move the effective decoupling point toward demand evidence; Zara decides late which designs to scale.

### Interview angle
> [!question] How it is asked
> "A client wants to offer 3-day delivery on a customised product without holding huge stock. What do you recommend?"

> [!tip] Strong answer includes
> - Define CODP, show lead-time stacking against customer tolerance
> - Place decoupling point at modules (ATO) plus postponement
> - Quantify pooling effect (square-root logic) and note extra cost of flexible final assembly
> - Product design changes (modularity) as an enabler

---

## 10. Supply Chain Maturity Models
> 🔴 Tier 1 · _Key points:_ stages 1-5, from functional silos to extended collaboration, assess then roadmap

### Definition
A **maturity model** describes stages of capability so that a firm can locate itself and plan the next step. Two commonly cited five-stage models:

| Stage | Lockamy and McCormack (2004) process maturity | Gartner supply chain maturity (commonly cited labels) |
|---|---|---|
| 1 | Ad hoc: unstructured, reactive | **React**: functional silos, firefighting |
| 2 | Defined: processes documented | **Anticipate**: plan and forecast within functions |
| 3 | Linked: cross-functional integration | **Integrate**: end-to-end internal integration (S&OP) |
| 4 | Integrated: shared metrics with partners | **Collaborate**: joint planning with trading partners |
| 5 | Extended: networked, collaborative improvement | **Orchestrate**: dynamic network, outcome-driven, digitally enabled |

(Check current Gartner labels in its latest publication; vendors paraphrase them.) Use: **assess** across dimensions (planning, sourcing, logistics, organisation, technology, metrics), **score** per dimension, **gap** against the target stage required by the strategy, **roadmap** the capabilities. A caution: the highest stage is not always the right one; a stable staples business may rationally stay at stage 3. Maturity of S&OP and IBP has its own ladder: see [[120 Integrated Business Planning (IBP) & S&OP Maturity]].

### Example
A mid-size Indian auto-parts maker self-scores: planning 2 (Excel forecasts, no consensus), sourcing 3 (supplier scorecards), logistics 2, technology 2 (ERP used for transactions only), metrics 2. Strategy: tier-1 supplier to a global OEM needing weekly schedule sharing = stage 4 in planning and information. Roadmap: first an S&OP forum and a data foundation (stage 3), then an EDI/portal-based schedule share (stage 4). Scoring everything 4 on day one would be unrealistic.

### In the news
See news box. Gartner's own list shows what stage 5 behaviour looks like in 2026: autonomous workforces and end-to-end orchestration.

### Interview angle
> [!question] How it is asked
> "How would you assess a company's supply chain maturity and build a roadmap?"

> [!tip] Strong answer includes
> - Stage model with dimensions, scored with evidence (interviews, data, process walks)
> - Target stage derived from strategy, not from ambition
> - Quick wins vs foundational moves (data, planning process)
> - KPIs to prove progress (forecast accuracy, OTIF, turns)

---

## 11. Strategy-to-Capability Mapping
> 🔴 Tier 1 · _Key points:_ competitive priority, supply chain requirement, driver settings, KPI

### Definition
Translate each competitive priority into a **supply chain requirement**, then into **driver settings** and **KPIs**. A mapping table makes the logic explicit and testable:

| Priority | Supply chain requirement | Typical lever settings | KPI (example) |
|---|---|---|---|
| Lowest cost | Efficiency, scale | Fewer DCs, full loads, long runs, offshore | Cost % revenue, turns |
| Fast availability | Responsiveness | Forward stock, regional DCs, express | Fill rate, order cycle time |
| Variety / customisation | Flexibility | Modular design, postponement, ATO | Variant lead time, mix flexibility |
| Innovation / newness | Speed to market | Concurrent engineering, small test runs, quick reaction capacity | Time to market, markdown % |
| Reliability / premium | Consistency | Quality at source, dual sourcing, buffers for critical parts | POF (see [[111 SCOR Model & Supply Chain Process Frameworks]]), OTIF |
| Sustainability | Footprint control | Modal shift, packaging, circular loops | tCO2e per tonne-km |

For each target segment, define **what we must be best at**, **what is good enough** and **what we deliberately sacrifice**. The sacrificed dimension is the check on strategy honesty.

### Example
An Indian D2C skincare brand targets "launch new variants every month". Mapping: priority = innovation; requirements = speed, small batches, flexible co-packers; levers = multiple contract manufacturers on rate cards, postponement of labelling and boxing, 8-week demand sensing; KPI = time from concept to first shipment (target 10 weeks), markdown rate (<8%). Sacrificed: unit cost per bottle, minimal inventory.

### In the news
See news box. The Inditex and Shein figures are mapping examples: high speed and small batches in exchange for higher unit cost and complexity.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would turn the company's strategy into supply chain design choices."

> [!tip] Strong answer includes
> - Priority to requirement to lever to KPI chain, per segment
> - Explicit sacrifices (what we will not optimise)
> - Evidence that levers produce the capability (pilot, data)
> - Governance and measurement: owners and target values

---

## 12. Worked Case: Re-aligning a Consumer-Durables Supply Chain
> 🔴 Tier 1 · _Key points:_ diagnose misfit, segment, assign chains, quantify, sequence

### Definition
A repeatable consulting flow for a "supply chain does not support the strategy" case:
1. **Strategy and customer**: who are the segments and what do they value?
2. **Diagnose misfit**: symptoms (stock-outs plus excess stock, expediting, long cycle times, margin leakage) and which segments they sit in.
3. **Segment** products and customers (demand, supply, cost-to-serve).
4. **Design** per segment: decoupling point, stocking location, replenishment, transport, planning cadence.
5. **Quantify** (inventory, service, cost) and **sequence** by value and effort; then a maturity target.

### Example
Appliance maker from sub-topic 7 (₹2,000 cr revenue). Symptoms: fill rate 91%, inventory 62 days, airfreight on 8% of lanes, long-tail contribution only 8%.
- **Core fast movers (55% of revenue):** efficient chain: MTS at 3 regional DCs, weekly production plan, sea/rail inbound, target fill 98%.
- **Seasonal/promotional:** forecast collaboration with key retailers, pre-season build with a decided cap and a late-season ATO for colour/features.
- **Long tail (600 SKUs, 15% of revenue):** consolidate to one central slow-mover DC; MTO with a 10-day promise for the slowest 300 SKUs; minimum order value; cut ~30% of SKUs.
- **Projects:** MTO/ETO with order-promising from ATP, a dedicated desk.
Impact (indicative): long-tail contribution 8% to 12% = +₹12 cr; inventory days 62 to 52 on COGS ₹1,500 cr releases $10 \times 1500/365\approx$ **₹41 cr** of cash; airfreight reduced by shifting planning to weekly with a cap. Maturity: planning from stage 2 to 3 (S&OP) in 6 months; supplier collaboration to stage 4 for the top five component families within 18 months.

### In the news
See news box. The speed-versus-efficiency choice here echoes what Zara and Shein show at the extreme.

### Interview angle
> [!question] How it is asked
> "Service is poor and inventory is high at the same time. What is going on and what would you do?" 

> [!tip] Strong answer includes
> - Simultaneous stock-outs and excess means misallocation across segments, not just "too little" or "too much"
> - Segmented diagnosis with numbers and a policy per segment
> - Quantified benefits with a stated range and key assumptions
> - Roadmap with quick wins, owners and risks

---

## 13. ⭐ Advanced: Resilience, Dual Networks and the Limits of Fisher
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Fisher and Chopra-Meindl assume demand uncertainty is the main uncertainty. Supply uncertainty (disruptions, geopolitical, single-source parts) is a second axis: **Lee (2002)** extended Fisher into a 2x2 of **demand uncertainty** (low/high) by **supply uncertainty** (low/high): *efficient* (stable/stable), *risk-hedging* (stable demand, uncertain supply: share and pool inventory, multiple suppliers), *responsive* (uncertain demand, stable supply), *agile* (both uncertain: combine hedging and responsiveness). Practical resilience designs: **dual or hybrid networks** (a cheap base network plus a fast flex network), **strategic buffers** for critical single-sourced parts, **China+1 / near-shoring** for exposure, and **flexible capacity contracts**. They cost money, so decide by **expected loss avoided**:

$$\text{Value of buffer} \approx P(\text{disruption}) \times \text{loss per day} \times \text{days covered} - \text{holding cost of buffer}$$

### Example
A carmaker's single-sourced ₹150 chip, if missing, stops a line that earns ₹0.2 cr contribution a day. Assume a 10% yearly chance of a 20-day outage: expected loss = 0.1 × 20 × ₹0.2 cr = **₹0.4 cr** a year. A 20-day buffer at 1,000 chips a day is 20,000 chips × ₹150 = ₹30 lakh of stock; carrying cost at 20% = **₹0.06 cr** a year. The buffer pays (0.4 > 0.06) under these assumptions; break-even outage probability = 0.06 / (20 × 0.2) = **1.5%** a year. The point: cheap, vital parts justify buffers even though lean theory says "cut inventory".

### In the news
See news box. Gartner 2026 pairs resilience and ESG with efficiency in its scoring, signalling that leaders no longer treat Fisher's efficient-versus-responsive axis alone as sufficient.

### Interview angle
> [!question] How it is asked
> "Is just-in-time dead? How should a company decide where to hold buffers?"

> [!tip] Strong answer includes
> - Two uncertainty axes: demand and supply
> - Buffer where criticality (VED), lead time and single-source risk are high
> - Expected-loss maths and break-even probability
> - Link to [[015 Supply Chain Risk & Resilience]] and [[141 Supply Chain Disruption Case Library (2011-2026)]]
