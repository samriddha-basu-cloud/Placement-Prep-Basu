---
tags: [consulting-preparation, tier1]
area: Consulting Preparation
topic: "Business Fundamentals & Strategy"
tier: Tier 1
roles: Consulting
status: complete
subtopics: 16
---
# Business Fundamentals & Strategy

[[_Index - Consulting Preparation|Consulting Preparation]] · [[024 Consulting Frameworks]] ➡

> **Area:** Consulting Preparation · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting

## Sub-topics in this note
1. [[#1. Profitability Analysis]]
2. [[#2. Revenue Growth Levers]]
3. [[#3. Cost Structure Analysis]]
4. [[#4. Porter's Five Forces]]
5. [[#5. SWOT Analysis]]
6. [[#6. BCG Matrix]]
7. [[#7. Ansoff Matrix]]
8. [[#8. McKinsey 7S Framework]]
9. [[#9. Value Chain Analysis]]
10. [[#10. Blue Ocean Strategy]]
11. [[#11. Business Model Canvas]]
12. [[#12. Market Sizing Methods]]
13. [[#13. Unit Economics]]
14. [[#14. Break-Even Analysis]]
15. [[#15. ⭐ Advanced: Contribution Margin Analysis and Pricing Decisions]]
16. [[#16. ⭐ Advanced: Corporate Strategy — Demergers, Portfolio Moves and the Resource-Based View]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Tata Motors splits in two; Blinkit turns EBITDA-positive
> **Tata Motors demerger (Oct 2025).** The passenger vehicle business began trading as *Tata Motors Passenger Vehicles Ltd* (ticker **TMPV**) on **24 Oct 2025**; the commercial vehicle business (TMLCV) was demerged into a separate entity, with the record date **14 Oct 2025**, allotment on **15 Oct 2025**, and **one TMLCV share for each Tata Motors share held** (about 3.68 billion shares of ₹2 each). Its separate NSE/BSE listing was expected in late Nov or early Dec 2025. The stated purpose: simplify the structure and give each business its own strategy and capital allocation. ([HDFC Sky](https://hdfcsky.com/news/tata-motors-demerger-company-to-trade-as-tata-motors-passenger-vehicles-ltd))
>
> **Blinkit / Eternal Q3 FY26 (Oct–Dec 2025 quarter).** Blinkit reported **adjusted EBITDA of ₹4 crore profit** versus a **₹156 crore loss in Q2 FY26**, operating revenue **₹12,256 crore** (+24% QoQ), **2,027 dark stores** (211 net adds), and a shift to an **inventory-led model with about 90% of net order value on company inventory**. Hyperpure also turned adjusted-EBITDA positive (₹1 crore). ([Inc42](https://inc42.com/buzz/eternal-q3-blinkit-hyperpure-achieve-adjusted-ebitda-profitability/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Profitability Analysis
> 🔴 Tier 1 · _Tracker hint:_ Revenue = Price × Volume; Cost = Fixed + Variable; Profit = R - C

### Definition
$$Profit = Revenue - Cost = (P\times Q) - (FC + VC\times Q)$$
Revenue depends on price $P$ and volume $Q$ (and mix across products). Costs split into fixed (rent, salaries, depreciation) and variable (materials, freight, commissions). Contribution per unit = $P - VC$; total contribution = $(P-VC)\times Q$; profit = contribution − fixed cost.

Ratios: gross margin = (Revenue − COGS)/Revenue; EBITDA margin = EBITDA/Revenue; net margin = PAT/Revenue; ROCE = EBIT/capital employed. Profit falls only because revenue fell, cost rose, or both: that is the root of every profitability case. Diagnose with a *time* view (when did it change?), a *segment* view (which product/region/customer?) and a *benchmark* view (versus peers).

### Example
Price ₹200, volume 10,000 units, variable cost ₹120, fixed cost ₹5,00,000.
Revenue = ₹20,00,000; variable cost = ₹12,00,000; contribution = ₹8,00,000; profit = 8,00,000 − 5,00,000 = **₹3,00,000** (15% margin). If volume drops 10% to 9,000: revenue ₹18,00,000, contribution ₹7,20,000, profit **₹2,20,000**, a fall of 26.7% from a 10% volume drop (operating leverage, see sub-topic 3).

### In the news
See news box. Blinkit's move from a ₹156 crore loss to a ₹4 crore profit is a profitability story: higher volume against largely fixed dark-store costs, plus an inventory-led model that changes the revenue and margin line items.

### Interview angle
> [!question] How it is asked
> "Profits of a client fell 20%. How do you find out why?"

> [!tip] Strong answer includes
> - Profit = revenue − cost, then split into price × volume and fixed vs variable
> - Ask: since when, which segment, vs competitors
> - Prioritise the biggest driver with data
> - Close with recommendation and risks (see [[025 Case Interview — Profitability]])

---

## 2. Revenue Growth Levers
> 🔴 Tier 1 · _Tracker hint:_ Price, volume, mix, new products, new markets, M&A

### Definition
Revenue = price × volume, so growth levers fall into:
- **Price:** list price increases, reduced discounting, premiumisation, dynamic pricing, price-pack architecture.
- **Volume:** more customers (acquisition), more purchases per customer (frequency, basket size), reduced churn, distribution reach.
- **Mix:** shift sales toward higher-margin products or customers.
- **New products / services:** line extensions, adjacencies, new revenue streams (subscriptions, ads).
- **New markets:** new geographies, segments, channels (online, B2B).
- **M&A / partnerships:** buy growth or capability.
Organic = first four; inorganic = M&A. A lever must be judged by impact, feasibility, time-to-impact and risk. Price changes interact with volume through elasticity $\varepsilon = \%\Delta Q/\%\Delta P$.

### Example
Combined effect compounds: price +5% and volume +3% gives $1.05\times1.03=1.0815$, i.e. **+8.15%** revenue, not 8%. With elasticity −2, a 5% price rise cuts volume ~10%: revenue = 1.05 × 0.90 = 0.945, a 5.5% decline, so price is a poor lever for elastic goods but excellent where demand is inelastic.

### In the news
See news box. Tata Motors' split lets the passenger-vehicle business pursue growth (EVs, new models, premium mix) separately from the cyclical commercial vehicle business; Blinkit's growth came from new dark stores (volume reach) and categories.

### Interview angle
> [!question] How it is asked
> "How can a regional dairy grow revenue by 30% in 3 years?"

> [!tip] Strong answer includes
> - Structured levers (price, volume, mix, new product, new market, M&A)
> - Size each roughly with simple numbers
> - Prioritise by impact and ease; flag risks (margin dilution, cannibalisation)
> - Link to capacity/supply chain feasibility (operations angle)

---

## 3. Cost Structure Analysis
> 🔴 Tier 1 · _Tracker hint:_ Fixed vs variable; direct vs indirect; economies of scale

### Definition
- **Fixed vs variable:** fixed cost does not change with volume within a relevant range; variable scales with volume; *semi-variable/step* costs sit in between.
- **Direct vs indirect:** direct costs trace to a product (materials, direct labour); indirect (overheads) are allocated (use **activity-based costing** to avoid distortion).
- **Economies of scale:** average cost falls as volume rises because fixed cost is spread (plus purchasing power, learning, specialisation); **diseconomies** appear when complexity or coordination grows.
- **Operating leverage:** $DOL = \dfrac{\text{Contribution}}{\text{EBIT}}$ shows how profit swings with volume; high fixed costs mean high leverage, high risk.
- **Experience curve:** unit cost falls ~15–25% for each doubling of cumulative output in many industries (typical figure, varies).

### Example
Using sub-topic 1 numbers: contribution ₹8,00,000, profit ₹3,00,000: DOL = 8/3 = 2.67, so a 10% volume fall cuts profit by 26.7% (matches ₹3,00,000 to ₹2,20,000).
Scale: average cost at 10,000 units = 120 + 500,000/10,000 = ₹170; at 20,000 units = 120 + 25 = **₹145** (15% lower). A cost reduction case first asks which cost lines are largest (Pareto) and which are fixed.

### In the news
See news box. Blinkit's dark stores are fixed cost; the Q3 FY26 break-even shows operating leverage working as order volume per store rose.

### Interview angle
> [!question] How it is asked
> "A client's cost per unit is rising. Where do you look?"

> [!tip] Strong answer includes
> - Fixed vs variable, direct vs indirect, then Pareto of cost lines
> - Volume effect (fixed cost per unit) vs rate effect (input prices) vs efficiency
> - Benchmark cost per unit versus peers
> - Mention scale benefits and where scale stops

---

## 4. Porter's Five Forces
> 🔴 Tier 1 · _Tracker hint:_ Buyer power, supplier power, rivalry, new entrants, substitutes

### Definition
Michael Porter's (1979) tool to judge **industry attractiveness** (long-run profit potential) from five forces:
1. **Threat of new entrants:** barriers (scale, capital, brand, regulation, access to distribution).
2. **Bargaining power of suppliers:** few suppliers, unique inputs, high switching costs.
3. **Bargaining power of buyers:** concentrated buyers, price sensitivity, low switching cost.
4. **Threat of substitutes:** alternatives meeting the same need.
5. **Rivalry among existing competitors:** number, growth, fixed costs, exit barriers, differentiation.
Strong forces mean low industry profitability. Use: decide whether to enter, find where profit is captured, and craft a strategy to defend (differentiate, lock-in, integrate). Critique: static, industry-level; ignores complements (a sixth "force" proposed by Grove/Brandenburger).

### Example
Indian domestic aviation: high rivalry (IndiGo ~64% share in Aug 2025 yet price-led), high supplier power (two aircraft makers, engine makers, fuel taxes), moderate buyer power (price sensitive passengers), moderate substitutes (rail on short routes, Vande Bharat), moderate entrants threat (capital heavy, slot constraints). Typically a low-profit industry, hence the history of failures (Jet, Kingfisher, Go First).

### In the news
See news box. After the Tata Motors split, commercial vehicles (cyclical, price-sensitive fleet buyers with strong buyer power) and passenger cars (brand and product led, EV entrants) face different force profiles, an argument for separate strategies.

### Interview angle
> [!question] How it is asked
> "Should we enter the Indian EV charging market?" or "How attractive is the industry?"

> [!tip] Strong answer includes
> - All five forces, but only 2–3 that decide the answer
> - Evidence for each (concentration, switching costs, margins)
> - So-what: enter or not, and how to defend position
> - Mention limits (dynamic changes, regulation)

---

## 5. SWOT Analysis
> 🔴 Tier 1 · _Tracker hint:_ Strengths, weaknesses, opportunities, threats; TOWS strategies

### Definition
**SWOT** sorts a firm's position: **Strengths** and **Weaknesses** are *internal* (resources, capabilities, cost, brand); **Opportunities** and **Threats** are *external* (market, regulation, technology, competitors). Quality rules: be specific, evidence-based, relative to competitors, and prioritised; avoid generic lists.

**TOWS matrix** (Weihrich) turns SWOT into action:
| | Opportunities | Threats |
|---|---|---|
| **Strengths** | SO: use strengths to exploit opportunities (growth) | ST: use strengths to counter threats (defend) |
| **Weaknesses** | WO: fix weaknesses to capture opportunities (turnaround) | WT: minimise weaknesses and avoid threats (retrench/exit) |

SWOT is a summary, not an analysis: pair it with Five Forces (external) and value chain (internal).

### Example
Illustrative for a regional FMCG firm: S = strong distribution in Maharashtra, W = weak digital presence, O = rising quick-commerce demand, T = national brands' discounting. SO: use distributor network to supply dark stores; WO: partner with a quick-commerce aggregator for digital capability; ST: loyalty schemes in own stronghold; WT: exit unprofitable low-volume SKUs.

### In the news
See news box. For Blinkit, quick-commerce growth is the opportunity and cash burn the threat; the move to profitability turns a weakness (thin margins) into a strength.

### Interview angle
> [!question] How it is asked
> "Do a SWOT for this company and tell me what it should do." 

> [!tip] Strong answer includes
> - Internal vs external split clearly
> - Few, specific, evidence-backed points
> - TOWS pairs to convert to strategic options
> - Prioritise and choose; end with recommendation

---

## 6. BCG Matrix
> 🔴 Tier 1 · _Tracker hint:_ Stars, Cash Cows, Question Marks, Dogs; portfolio strategy

### Definition
The **BCG growth-share matrix** (Boston Consulting Group, 1970s) plots each business unit by **market growth rate** (y-axis) and **relative market share** (x-axis) = own share ÷ share of the largest competitor.

| | High share (relative > 1) | Low share |
|---|---|---|
| **High growth** | **Star:** invest to hold leadership | **Question mark:** invest selectively or divest |
| **Low growth** | **Cash cow:** harvest, fund others | **Dog:** divest, harvest or niche |

Logic: cash cows generate cash to fund stars and winning question marks. Circle size = revenue. Limits: market definition is arbitrary; ignores synergies; share is not the only source of advantage; growth rate is not the only attractiveness measure. Use with GE-McKinsey 9-box.

### Example
Business A has 30% market share; its largest rival has 15%: relative share = 30/15 = **2.0**. Business B has 6% against leader's 24%: relative share 0.25. If the market grows 12%/yr, A is a Star, B a Question Mark. At 2% growth, A is a Cash Cow and B a Dog.

### In the news
See news box. Splitting Tata Motors separates two units with different portfolio roles: a commercial vehicle business that can be a cash generator and a passenger/EV business needing heavy investment, so each can be funded on its own merits (an analytical reading, not a company statement).

### Interview angle
> [!question] How it is asked
> "A conglomerate has five divisions. How should it allocate capital?"

> [!tip] Strong answer includes
> - Axes defined correctly (relative share, not absolute)
> - Strategic stance per quadrant
> - Cash flow logic between quadrants
> - Caveats and use of complementary tools (9-box, synergies)

---

## 7. Ansoff Matrix
> 🔴 Tier 1 · _Tracker hint:_ Market penetration, development, product development, diversification

### Definition
Igor Ansoff's growth matrix crosses **products** (existing/new) with **markets** (existing/new):
| | Existing products | New products |
|---|---|---|
| **Existing markets** | **Market penetration** (lowest risk) | **Product development** |
| **New markets** | **Market development** | **Diversification** (highest risk; related or unrelated) |

Penetration: increase share through price, promotion, distribution, loyalty. Market development: new geography, segment or channel. Product development: new variants or features for current customers. Diversification: both new; vertical integration is sometimes counted separately. Risk and return both rise toward the diagonal corner. Choose using capabilities, market attractiveness and resource fit.

### Example
A packaged-snacks company: penetration = more kiosks and quick-commerce listings in current cities; market development = launch in Tier-2 cities or export; product development = baked, high-protein variants; diversification = entering beverages. Expected success falls and capital need rises as you move right and down.

### In the news
See news box. Blinkit adding dark stores and categories mixes penetration (more stores in existing cities) with product development (new assortment); an inventory-led model is a new way to serve existing customers.

### Interview angle
> [!question] How it is asked
> "Where should a successful kirana-chain brand grow next?"

> [!tip] Strong answer includes
> - Four cells, with risk ordering
> - Recommend one primary and one secondary path
> - Capabilities and capital needed
> - Metrics to test (pilot results, unit economics)

---

## 8. McKinsey 7S Framework
> 🔴 Tier 1 · _Tracker hint:_ Strategy, Structure, Systems, Shared Values, Skills, Staff, Style

### Definition
McKinsey's 7S (Peters, Waterman, Phillips, Pascale and Athos, 1980s) says organisational effectiveness needs **alignment** of seven elements:
- **Hard:** **Strategy** (plan to win), **Structure** (reporting, org design), **Systems** (processes, IT, KPIs, controls).
- **Soft:** **Shared values** (core of the model; culture), **Skills** (capabilities), **Staff** (people, talent mix), **Style** (leadership behaviour).
All are interdependent; changing one without the others causes failure. Use it for **change management, post-merger integration and diagnosing why a good strategy is not executed**: map current state, desired state, gaps, and sequence of changes.

### Example
A bank launching a digital-first strategy: Strategy (digital), Structure (product squads instead of branch hierarchy), Systems (new core banking and analytics), Skills (data and design), Staff (hire engineers, retrain branch staff), Style (leaders tolerate experimentation), Shared values (customer obsession). If it changes strategy and systems but not style or skills, adoption stalls.

### In the news
See news box. Splitting Tata Motors forces a 7S re-design for each entity: separate structures, systems, leadership and values.

### Interview angle
> [!question] How it is asked
> "A merger has stalled. How do you diagnose it?"

> [!tip] Strong answer includes
> - Hard vs soft elements and why alignment matters
> - Where the misalignment is, with evidence
> - Sequenced change plan with owners
> - Link to change management

---

## 9. Value Chain Analysis
> 🔴 Tier 1 · _Tracker hint:_ Primary vs support activities; competitive advantage source

### Definition
Porter's **value chain** (1985) decomposes the firm into activities that add value:
- **Primary:** inbound logistics, operations, outbound logistics, marketing and sales, service.
- **Support:** firm infrastructure, human resource management, technology development, procurement.
**Margin** = total value − total cost of activities. Steps: map activities, assign costs and assets, find the activities that drive cost or differentiation, benchmark, then decide to improve, re-configure, outsource or integrate. Linkages between activities (e.g. design for manufacturability lowering operations cost) are often the source of advantage. It differs from the **supply chain** (inter-firm) and **value stream map** (lean, process level).

### Example
Cost leadership in an airline: operations (single aircraft type, quick turnarounds), procurement (bulk orders), inbound (fuel hedging) and marketing (direct online sales) all aligned. Differentiation in luxury cars: R&D and technology, brand and service dominate. A margin squeeze is found by costing each activity, e.g. if outbound logistics is 12% of sales versus peers at 8%, that is the target.

### In the news
See news box. Blinkit's inventory-led model moves control of procurement and inbound logistics inside the firm to capture margin; Tata Motors' split separates two distinct value chains.

### Interview angle
> [!question] How it is asked
> "Where does this company make money and where is it leaking?"

> [!tip] Strong answer includes
> - Correct primary and support activities
> - Pick the 1–2 activities that create advantage
> - Cost or value benchmarks
> - Decision: improve, outsource, integrate

---

## 10. Blue Ocean Strategy
> 🔴 Tier 1 · _Tracker hint:_ Value innovation; eliminate-reduce-raise-create grid

### Definition
Kim and Mauborgne (2005): compete not in crowded **red oceans** but create **blue oceans** of uncontested market space through **value innovation**, pursuing differentiation *and* low cost simultaneously.

**Four Actions Framework (ERRC grid):**
- **Eliminate** factors the industry takes for granted that no longer add value.
- **Reduce** factors well below the industry standard.
- **Raise** factors well above the industry standard.
- **Create** factors the industry has never offered.
Tool: **Strategy canvas**, plotting the industry's competing factors on the x-axis and the offering level on the y-axis, to see how a new curve differs. Also the "Six Paths" to reshape boundaries and the **Buyer Utility Map**. Critique: examples are post-hoc; blue oceans are eventually imitated.

### Example
Cirque du Soleil: eliminated animal acts and star performers; reduced fun-and-humour and thrill (circus-style); raised the venue and artistic music; created a theatre-like storyline. Result: a new audience (adults, corporates) at premium prices.

### In the news
See news box. Quick-commerce is often described as creating a new space: 10-minute delivery as the raised factor, with eliminated factors such as browsing in store. Whether it stays a blue ocean is doubtful as several players now compete.

### Interview angle
> [!question] How it is asked
> "How can a small tea brand differentiate in a crowded market?"

> [!tip] Strong answer includes
> - Strategy canvas and ERRC grid with specifics
> - Non-customer segments targeted
> - Economic viability: cost structure, not only novelty
> - Honest note on imitation and sustainability

---

## 11. Business Model Canvas
> 🔴 Tier 1 · _Tracker hint:_ 9 building blocks; value proposition central

### Definition
Osterwalder and Pigneur's **Business Model Canvas** describes how an organisation creates, delivers and captures value in **nine blocks**:
1. Customer Segments
2. Value Propositions (centre)
3. Channels
4. Customer Relationships
5. Revenue Streams
6. Key Resources
7. Key Activities
8. Key Partnerships
9. Cost Structure
Right side = desirability (customer), left side = feasibility (operations), bottom = viability (cost vs revenue). Use to compare models, design startups, and test hypotheses with the **Lean Canvas** (problem/solution/key metrics instead of partners/resources). Fit between blocks matters more than filling them.

### Example
Blinkit: segments (urban households), value proposition (groceries in about 10 minutes), channels (app), relationships (repeat orders, ratings), revenue (product margin, delivery fees, ads), resources (dark stores, tech, riders), activities (inventory, picking, last-mile), partners (brands, delivery fleet), costs (stores, rent, riders, discounts). The reported shift to company inventory changes revenue streams and cost structure, not the customer segment.

### In the news
See news box. The Q3 FY26 switch to ~90% inventory-led is a business-model change visible in the revenue-streams and cost-structure blocks.

### Interview angle
> [!question] How it is asked
> "Describe the business model of Zomato or Ola. Where does it make money?"

> [!tip] Strong answer includes
> - Value proposition first, then the other blocks briefly
> - Revenue streams and cost drivers with logic
> - Where the model is fragile
> - Identify the key lever to profitability

---

## 12. Market Sizing Methods
> 🔴 Tier 1 · _Tracker hint:_ Top-down vs bottom-up; TAM-SAM-SOM

### Definition
- **Top-down:** start from a large known population or market and apply filters (e.g. population → households → income segment → adoption → spend).
- **Bottom-up:** build from unit economics (number of outlets × transactions × ticket size; or number of customers × price).
- **TAM** (Total Addressable Market): total demand for the product; **SAM** (Serviceable Available): portion you can reach with your model/geography; **SOM** (Serviceable Obtainable): realistic share you can capture near-term.
Good practice: state assumptions, use round numbers, cross-check top-down against bottom-up, and sanity-check against a known figure. Sources for real work: industry reports, government data (NSO, RBI), company filings.

### Example
Illustrative, assumption-based: India's urban working population who might buy a ₹300 monthly meal subscription. Assume 100 million urban working adults, 20% eat out/order regularly = 20 million, 10% of them in the target price band = 2 million (SAM), × ₹300 × 12 = ₹7,200 per year → 2 million × ₹7,200 = ₹14,400 million = **₹1,440 crore**. Bottom-up check: 2,000 cloud kitchens × 400 meals/day × ₹150 × 365 = ₹4,380 crore, three times larger; the gap means assumptions (price band, adoption, subscription vs per-meal spend) need rechecking. SOM at 5% of SAM ≈ ₹72 crore.

### In the news
See news box. Market sizing underpins quick-commerce investment: store count (2,027 for Blinkit) × orders per store × order value is a bottom-up view, but the source gives only store and revenue figures, so any order-level estimate is an assumption.

### Interview angle
> [!question] How it is asked
> "Estimate the size of the market for electric two-wheelers in India."

> [!tip] Strong answer includes
> - Clear structure and segmentation (urban/rural, price tiers)
> - Stated assumptions, simple arithmetic
> - Cross-check by a second method
> - End with so-what (attractive or not), not just a number

---

## 13. Unit Economics
> 🔴 Tier 1 · _Tracker hint:_ CAC, LTV, payback period, contribution margin per unit

### Definition
Profitability of one unit (order, customer, store).
- **Contribution margin per unit** = price − variable costs per unit.
- **CAC** = total acquisition spend ÷ new customers.
- **LTV** = (ARPU × gross margin) ÷ churn rate (subscription), or margin per order × orders per lifetime.
- **LTV/CAC** target ≈ 3x or better (rule of thumb); **CAC payback** = CAC ÷ monthly contribution; target under 12 months for many consumer businesses.
- For delivery/q-commerce: **AOV**, gross margin %, delivery cost per order, store-level EBITDA.
Beware: using revenue instead of margin, ignoring churn, including only marginal not fully-loaded costs, and averages that hide cohorts.

### Example
Subscription: CAC ₹400, ARPU ₹100/month, gross margin 60%, monthly churn 5%.
Monthly contribution = 100 × 0.6 = ₹60. Payback = 400/60 = **6.7 months**. Lifetime = 1/0.05 = 20 months; LTV = 60 × 20 = **₹1,200**; LTV/CAC = 3.0.
If churn doubles to 10%: lifetime 10 months, LTV ₹600, LTV/CAC 1.5, so retention is the biggest lever.

### In the news
See news box. Blinkit's quarter of adjusted EBITDA profit follows years of negative unit economics being fixed through higher orders per store and company inventory; margin is thin (0.03% adjusted EBITDA margin), showing how fragile quick-commerce unit economics are.

### Interview angle
> [!question] How it is asked
> "A food-delivery startup spends ₹250 to acquire a customer who orders 3 times a month at ₹40 contribution each. Is it viable?"

> [!tip] Strong answer includes
> - Compute monthly contribution (3 × 40 = ₹120), payback ₹250/120 ≈ 2.1 months
> - Ask about retention and cohort behaviour
> - LTV vs CAC, and fully loaded costs
> - Levers: AOV, frequency, delivery cost, take rate

---

## 14. Break-Even Analysis
> 🔴 Tier 1 · _Tracker hint:_ Fixed cost / (Price - Variable cost); margin of safety

### Definition
$$BEP_{units}=\frac{FC}{P-VC},\qquad BEP_{revenue}=\frac{FC}{CM\%}\ \text{where}\ CM\%=\frac{P-VC}{P}$$
Target profit: $Q=\dfrac{FC+\text{Target profit}}{P-VC}$.
**Margin of safety** = (actual sales − break-even sales) ÷ actual sales. **Operating leverage** and break-even shift with price, cost and mix. For investments, **payback** and **break-even time** (when cumulative cash turns positive) are the analogous ideas. Multi-product break-even uses weighted average contribution margin per unit/mix. Assumes linear costs and constant mix, so it is a screening tool.

### Example
FC ₹5,00,000, P ₹200, VC ₹120, unit contribution ₹80.
- BEP = 5,00,000 / 80 = **6,250 units**; BEP revenue = 6,250 × 200 = ₹12,50,000 (or 5,00,000 / 0.40).
- At 10,000 units, margin of safety = (10,000 − 6,250)/10,000 = **37.5%**.
- To earn ₹3,00,000: Q = (5,00,000 + 3,00,000)/80 = 10,000 units (consistent with sub-topic 1).
If price falls ₹20 to ₹180: contribution ₹60; BEP = 8,333 units (+33%).

### In the news
See news box. For dark stores, break-even depends on orders per store per day covering rent and staff; Blinkit's move from loss to small profit shows crossing that line.

### Interview angle
> [!question] How it is asked
> "A new plant costs ₹50 crore fixed per year. When does it break even?"

> [!tip] Strong answer includes
> - Formula and clear numeric work
> - Margin of safety and sensitivity to price/volume
> - Fixed vs variable assumptions explicit
> - Operational levers: lower fixed cost, higher contribution, utilisation

---

## 15. ⭐ Advanced: Contribution Margin Analysis and Pricing Decisions
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Decision rule: **accept an extra order or keep a product if it covers its avoidable (incremental) costs**, i.e. price > variable cost plus any extra fixed cost; sunk and allocated overheads are irrelevant. Pricing methods: **cost-plus** (VC + FC share + markup), **competitor-based**, **value-based** (willingness to pay), and **price discrimination**. Use **price elasticity**: markup-optimal rule for a profit-maximiser: $\dfrac{P-MC}{P}=\dfrac{1}{|\varepsilon|}$ (Lerner). With elasticity −2.5, optimal margin = 40%. Mix analysis: prune low-contribution SKUs only if the shared fixed costs are truly avoidable and no halo/demand effects exist.

### Example
Capacity spare; a distributor offers ₹150 per unit for 2,000 units (usual price ₹200, VC ₹120). Incremental contribution = (150 − 120) × 2,000 = ₹60,000 > 0, so accept if it does not cannibalise regular sales or set a price precedent (use a different channel/brand). Lerner: elasticity −2.5, MC ₹120: $P=\dfrac{MC}{1-1/|\varepsilon|}=\dfrac{120}{0.6}=₹200$.

### In the news
See news box. Quick-commerce players weigh unit-level contribution when choosing which categories and discounts to continue.

### Interview angle
> [!question] How it is asked
> "Should we accept a bulk order at a discount?" or "Should we drop this loss-making product?"

> [!tip] Strong answer includes
> - Relevant (incremental) vs sunk costs
> - Capacity availability and opportunity cost
> - Channel conflict and long-run price effects
> - Quantified decision plus qualitative factors

---

## 16. ⭐ Advanced: Corporate Strategy — Demergers, Portfolio Moves and the Resource-Based View
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Corporate strategy decides *which businesses to be in*; business strategy decides *how to compete* in each. **Portfolio moves:** acquire, divest, demerge (spin-off giving shareholders shares of the new entity), joint venture. **Rationales for demerger:** remove the **conglomerate discount**, give each business tailored capital allocation and management, make each business easier to value and fund. **Resource-Based View (VRIO):** advantage comes from resources that are **V**aluable, **R**are, hard to **I**mitate and exploited by the **O**rganisation. **Parenting advantage:** a business belongs in a portfolio only if the parent adds more value than it destroys. Core competence (Prahalad and Hamel) guides adjacency choices.

### Example
Tata Motors' demerger (Oct 2025): each existing shareholder got one share of the commercial vehicle company for each share held, so the economic claim is unchanged at split, while capital allocation, management focus and investor base can diverge. A test an interviewer may ask: after the split, would you value the combined entity higher or lower than the sum of parts, and why?

### In the news
See news box for the Tata Motors demerger.

### Interview angle
> [!question] How it is asked
> "Why would a company demerge a business? Would you recommend it for this client?"

> [!tip] Strong answer includes
> - Strategic logic: focus, valuation, capital allocation
> - Costs: dis-synergies, duplicated overheads, tax and legal complexity
> - Parenting-advantage test
> - Execution risks and a recommendation with conditions

---
## 🔗 Go deeper: expansion notes
- [[159 Case Interview - M&A & Due Diligence|Case Interview - M&A & Due Diligence]]
- [[160 Case Interview - Cost Reduction, Turnaround & Pricing|Case Interview - Cost Reduction, Turnaround & Pricing]]
- [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital|Corporate Finance Essentials - Capital Structure & Cost of Capital]]
