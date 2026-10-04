---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "New-Product Forecasting, Demand Sensing & Demand Shaping"
tier: Tier 1
roles: Operations / PM / Consulting
status: complete
subtopics: 14
---
# New-Product Forecasting, Demand Sensing & Demand Shaping

⬅ [[117 Demand-Driven MRP (DDMRP) & Buffer Management]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[119 Supply Planning, DRP & Available-to-Promise]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / PM / Consulting

## Sub-topics in this note
1. [[#1. Forecast Horizons and Planning Hierarchies]]
2. [[#2. Forecastability: CoV, Intermittency and When Not to Forecast]]
3. [[#3. New-Product Forecasting: The Problem and the Toolbox]]
4. [[#4. Analogous (Like-Product) and ATAR Build-Up Forecasts]]
5. [[#5. Delphi, Expert Panels and Test Markets]]
6. [[#6. The Bass Diffusion Model]]
7. [[#7. Post-Launch Tracking and Early-Sales Updating]]
8. [[#8. Causal and Regression Forecasting with Prices, Promotions and Events]]
9. [[#9. Price Elasticity of Demand]]
10. [[#10. Promotion Lift, Pull-Forward and Cannibalisation]]
11. [[#11. Demand Shaping: Price, Promotion, Assortment and Availability]]
12. [[#12. Demand Sensing: Short-Term Forecasts from Fresh Signals]]
13. [[#13. Consensus Forecasting, Governance and Forecast Value Added]]
14. [[#14. ⭐ Advanced: AI/ML Demand Forecasting, Cold Start and Vendor Landscape]]

## 📰 News box
> [!news] Shared news hook for this topic (2025–2026): AI-driven planning is everywhere, but trust and data quality lag
> **IDC study on AI in supply chains (Kinaxis-sponsored, published August 2026).** IDC surveyed over 2,000 supply chain leaders across nine markets: **98%** report some AI capability but only **12%** consider themselves AI leaders; **52%** cite trust in AI-driven decisions as a top barrier; **62%** want better data quality and integration; **51%** want clear ROI and time to value; **41%** expect autonomous-at-scale operations within 1-2 years against **6%** today. Sponsor-funded, so read as industry sentiment rather than neutral evidence. ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/kinaxis-sponsored-study-identifies-supply-chain-ai-accountability-gap))
>
> **Gartner 2026 planning quadrants (23 March 2026).** Kinaxis announced it was named a Leader in two 2026 Gartner Magic Quadrant reports (Supply Chain Planning Solutions for Discrete Industries and for Process Industries), its 11th consecutive year as a Leader; the vendor describes the scope as S&OP, demand planning, supply planning, inventory, production planning and scheduling. Vendor-reported. ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/kinaxis-recognized-leader-2026-gartnerr-magic-quadranttm-reports-supply))
>
> **What the tools claim to do.** SAP's Integrated Business Planning page lists demand sensing ("refine short-term forecasts to drive better fulfillment and inventory reduction"), demand planning that combines multiple demand signals with statistical forecasts, and what-if scenario planning as separate modules. ([SAP IBP features](https://www.sap.com/products/scm/integrated-business-planning/features.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Forecast Horizons and Planning Hierarchies
> 🔴 Tier 1 · _Key points:_ Strategic, tactical, operational; product, location and time hierarchies

### Definition
Different decisions need different forecasts:

| Horizon | Typical span | Decision | Level of detail |
|---|---|---|---|
| Strategic | 2-10 years | Plants, network, capacity ([[113 Network Design & Facility Location Modelling]]) | Product group, region, annual |
| Tactical (S&OP/IBP) | 3-24 months | Capacity, hiring, inventory build, budgets ([[120 Integrated Business Planning (IBP) & S&OP Maturity]]) | Family, region, monthly |
| Operational | 1-13 weeks | Production and replenishment ([[119 Supply Planning, DRP & Available-to-Promise]]) | SKU-location, weekly |
| Execution | Days | Allocation, expediting, last-minute deployment | SKU-location, daily |

Forecasts are built on **hierarchies** (product family to SKU, country to warehouse to store, year to month to week). **Top-down** forecasts a family and splits by historical share (stable, but loses SKU signals); **bottom-up** forecasts each SKU and sums (captures detail, noisy); **middle-out** forecasts at an intermediate level; **reconciliation** methods make levels coherent (see advanced section of [[004 Demand Forecasting & Planning]]). Rule of thumb: error falls as aggregation rises (pooling), so plan capacity at family level and inventory at SKU-location level.

### Example
Family forecast for next month: 10,000 units with historic mix S 50%, M 30%, L 20% gives 5,000, 3,000 and 2,000. If a promotion on M is planned, the share changes: using 50/40/10 the M forecast moves to 4,000 but the total may not (cannibalisation of S and L); reconcile so the sum equals the family total unless the promotion is expected to grow the family.

### In the news
See news box. Planning platforms (Kinaxis, SAP IBP) are sold on running these horizons in one data model so demand, supply and finance work from consistent numbers.

### Interview angle
> [!question] How it is asked
> "At what level would you forecast for a retailer with 20,000 SKUs and 500 stores?"

> [!tip] Strong answer includes
> - Match level to decision: capacity at family, replenishment at SKU-store
> - Top-down vs bottom-up trade-off and reconciliation
> - Horizon vs lead time: forecast must cover lead time plus review period
> - Error is lower at higher aggregation; hence pooling and postponement

---
## 2. Forecastability: CoV, Intermittency and When Not to Forecast
> 🔴 Tier 1 · _Key points:_ Coefficient of variation, ADI and CV², segment before modelling

### Definition
**Forecastability** is how well an item can be predicted *at best*. A first-pass indicator is the **coefficient of variation** of demand:

$$CoV = \frac{\sigma}{\mu}$$

Low CoV (below about 0.5) suggests stable demand; high CoV (above 1) suggests erratic items whose forecasts will always carry large error. For intermittent items, the Syntetos-Boylan classification uses the **average demand interval (ADI)** and the squared CoV of non-zero demand: with cut-offs ADI = 1.32 and CV² = 0.49, items are smooth, intermittent, erratic or lumpy (see Croston in [[004 Demand Forecasting & Planning]]). Practical segmentation: forecast **smooth/low-CoV** items statistically, give **high-value erratic** items a collaborative review, and manage **lumpy low-value** items with min-max or make-to-order instead of precision forecasting. Judge forecasters by **forecast value added** (does a step beat a naive forecast?), not raw accuracy.

### Example
Weekly demand: mean 200, s.d. 50 gives $CoV = 0.25$ (forecastable); mean 20, s.d. 40 gives $CoV = 2.0$ (erratic). A planner spending equal effort on both wastes time: the first gets a statistical model, the second gets a safety-stock policy or pooled stock ([[003 Inventory Management]]).

### In the news
See news box. IDC's finding that 62% of leaders want better data quality and integration is a forecastability issue too: dirty history makes even good algorithms look poor.

### Interview angle
> [!question] How it is asked
> "Forecast accuracy is stuck at 65%. What do you do?"

> [!tip] Strong answer includes
> - Segment by volume, CoV and intermittency before blaming the method
> - Benchmark against a naive forecast and compute FVA
> - Fix drivers: data cleaning, promotions, new-item handling, bias
> - Accept limits: for erratic items improve flexibility (lead time, postponement) rather than the forecast

---
## 3. New-Product Forecasting: The Problem and the Toolbox
> 🔴 Tier 1 · _Key points:_ No history, so use judgement, analogies, market data and diffusion models

### Definition
A new product has **no sales history**, so time-series methods cannot be used. The toolbox, ordered roughly from judgement to model:
1. **Judgemental**: sales-force composite, executive opinion, **Delphi**.
2. **Analogy (like-product)**: use the launch curve of a comparable item, scaled.
3. **Market research**: concept tests, conjoint, purchase intent, pre-orders, **test markets**.
4. **Build-up (ATAR)**: awareness, availability, trial and repeat.
5. **Diffusion models**: the **Bass model** (sub-topic 6) for products that spread by innovation and imitation.
6. **Post-launch tracking**: update quickly with early actuals (sub-topic 7).
Good practice combines two or three methods and expresses the forecast as a **range** with scenarios; supply plans use the low case for committed capacity and the high case for flexible options. See also qualitative methods in [[004 Demand Forecasting & Planning]] and product launch planning in [[036 Go-To-Market Strategy]].

### Example
A beverage firm launching a new drink in 2 states combines three views for year-1 volume: analogy (1.08 million bottles), ATAR build-up (0.95 million) and a sales-force composite (1.40 million, usually optimistic). It plans production for 1.0 million and keeps a rapid-reorder contract for another 0.3 million.

### In the news
See news box. AI forecasting vendors market "cold start" capabilities, but 52% of surveyed leaders cite trust as a barrier, so launch forecasts still need human review.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand for a product that has never been sold before?"

> [!tip] Strong answer includes
> - States that history is absent and lists 3-4 methods
> - Combines methods; gives a range, not a point
> - Pre-launch and post-launch (reorder) steps
> - Names biases: sales optimism, purchase-intent overstatement

---
## 4. Analogous (Like-Product) and ATAR Build-Up Forecasts
> 🔴 Tier 1 · _Key points:_ Pick analogues, scale, adjust; awareness x availability x trial x repeat

### Definition
**Analogy method**: choose one or more earlier launches that match on category, price tier, channel and target buyer; take their launch curve (for example units per week from launch); scale to the new product's market size and adjust for differences (price, promotion budget, distribution). Document why each analogue was chosen and weight them.

**ATAR (awareness-trial-availability-repeat) build-up**: 

$$\text{Year-1 units} = N \times a \times d \times t \times (1 + r \times k)$$

with $N$ target households, $a$ awareness, $d$ distribution (availability), $t$ trial rate among those aware and able to buy, $r$ repeat rate and $k$ repeat purchases per repeater. Each input comes from the media plan, trade distribution targets and concept-test benchmarks.

### Example
**Analogy**: a comparable launch sold 80,000 units in its first year in a market of 2 crore addressable households. The new market is 3 crore and the new product is priced 10% higher, so apply 0.9: $80{,}000 \times \frac{3}{2} \times 0.9 =$ **108,000 units**.
**ATAR**: 2,000,000 target households × awareness 40% × distribution 60% × trial 10% = **48,000 trial buyers**. If 30% repeat with 4 further packs each, volume = 48,000 × (1 + 0.3 × 4) = **105,600 packs**. The two methods agree to within 2%, which raises confidence; if they differed by 40%, investigate the assumption (usually trial or distribution).

### In the news
See news box. As planning suites add AI, the analogues are increasingly chosen by similarity algorithms, but the choice of comparable products still needs a business check.

### Interview angle
> [!question] How it is asked
> "A new FMCG snack launches in 6 months. Size year-1 volume for the plant planner."

> [!tip] Strong answer includes
> - Analogy plus ATAR with explicit assumptions
> - Cross-check ranges; sensitivity to distribution and trial
> - Seasonality of launch and pipeline fill
> - Review gates after 4, 8 and 12 weeks

---
## 5. Delphi, Expert Panels and Test Markets
> 🔴 Tier 1 · _Key points:_ Anonymous rounds, controlled feedback, regional test, purchase-intent haircuts

### Definition
**Delphi method**: a panel of experts (often 8-15) gives anonymous forecasts independently; a facilitator summarises the median and reasons; experts revise over 2-3 rounds. Anonymity limits dominance by senior voices and groupthink; the output is a median and range. Strength: works with no data; weakness: slow, depends on expert quality, can converge on shared bias.

**Test market**: launch in a few representative cities or channels, measure trial and repeat, extrapolate to national scale. Strong realism, but costs time, alerts competitors, and may not scale (distribution, advertising weight). **Concept testing and conjoint** estimate preference and price response; stated purchase intent usually overstates actual purchase, so firms apply **calibration (haircut) factors** learned from past launches. In e-commerce, **pre-orders, waitlists and landing-page tests** give cheaper signals; in quick commerce, a few dark stores serve as test markets ([[129 E-commerce & Quick-Commerce Fulfilment]]).

### Example
Eight experts forecast a new device's year-1 sales (thousand units): 40, 55, 60, 60, 65, 70, 90, 120. Round 1 median = 62.5. After feedback, the high outliers explain (a distribution deal) and low outliers explain (supply limit), and round 2 gives 50, 58, 60, 62, 64, 66, 75, 85: median **63**, range narrower. Plan base case 63,000 with a 50,000-85,000 range. A two-city test shows 4.2% trial in 8 weeks against a plan of 3.0%; extrapolation still needs a haircut for lower national distribution.

### In the news
See news box. IDC's trust gap shows why structured human methods like Delphi stay relevant: managers still ask "why" before acting on an algorithm.

### Interview angle
> [!question] How it is asked
> "What are the pros and cons of a test market versus a Delphi panel?"

> [!tip] Strong answer includes
> - Delphi steps: anonymity, feedback, iteration
> - Test-market realism versus cost, speed and leak risk
> - Calibrate stated intent using past launches
> - Combine with analogy to cross-check

---
## 6. The Bass Diffusion Model
> 🔴 Tier 1 · _Key points:_ Innovation p, imitation q, market potential m, peak time

### Definition
The **Bass model** (Frank Bass, 1969) describes adoption of a new durable or technology product as driven by **innovators** (adopt independently, coefficient $p$) and **imitators** (influenced by prior adopters, coefficient $q$). With market potential $m$, cumulative adopters $N(t)$ and cumulative share $F(t)=N(t)/m$:

$$\frac{dN}{dt} = \big(p + q\,F(t)\big)\,\big(m - N(t)\big)$$

Closed form:

$$F(t) = \frac{1 - e^{-(p+q)t}}{1 + \frac{q}{p}\,e^{-(p+q)t}}$$

Peak adoption occurs at $t^* = \dfrac{\ln(q/p)}{p+q}$ (when $q > p$); peak rate = $m\,\dfrac{(p+q)^2}{4q}$; cumulative adopters at peak = $m\,\dfrac{q-p}{2q}$. Published meta-analyses of consumer durables give typical values near $p \approx 0.03$ and $q \approx 0.38$ (Sultan, Farley and Lehmann; treat as indicative). Parameters can be fitted by non-linear regression once early data exist, or borrowed from analogues before launch. Limits: single market potential $m$ is assumed fixed, ignores price and marketing, and is for first purchase unless extended for repeat/replacement.

### Example
$m = 5{,}00{,}000$ households (5 lakh), $p = 0.03$, $q = 0.38$ (annual). $t^* = \ln(12.67)/0.41 =$ **6.2 years**; peak rate ≈ 500,000 × 0.41² / (4 × 0.38) ≈ **55,300 a year**; cumulative at peak ≈ 230,000 (46%).

| Year | Cumulative adopters | New adopters in year |
|---|---|---|
| 1 | 17,879 | 17,879 |
| 2 | 42,528 | 24,649 |
| 3 | 75,250 | 32,722 |
| 5 | 165,599 | 49,024 |
| 7 | 274,505 | 54,887 |
| 10 | 406,402 | 36,038 |

Year-1 supply need is 18k units, peak 55k: capacity and working capital should grow along the S-curve rather than be sized at launch for the whole market. Fast-adopting categories (a UPI-linked gadget, an app) have much larger $p, q$ and shorter peaks.

### In the news
See news box. AI forecasting tools often fit diffusion curves automatically for launches; the analyst still chooses the analogue and market potential, which dominate the answer.

### Interview angle
> [!question] How it is asked
> "Explain the Bass model. How would you use it to plan capacity for a new EV scooter?"

> [!tip] Strong answer includes
> - Roles of p (innovation), q (imitation), m (potential); S-curve shape
> - Peak time and peak sales formulas
> - Sources of parameters: analogues now, fit later
> - Limits: price, supply constraints, competition, regulation (subsidies shift m and p)

---
## 7. Post-Launch Tracking and Early-Sales Updating
> 🔴 Tier 1 · _Key points:_ Update fast on actuals; commit late, reorder fast

### Definition
After launch, early sales are the best information. Methods: **run-rate scaling** (extrapolate using the analogue's cumulative curve share), **Bayesian or weighted updating** (blend prior forecast with scaled actuals, weight shifting to actuals as weeks pass), and **refitting** diffusion parameters. Link to operations: **quick response / accurate response** designs (the Sport Obermeyer case, Fisher and Raman) commit a portion of production early and the rest after initial sales are seen, shortening replenishment so the second order can follow actuals. This turns the single-period **newsvendor** problem ([[003 Inventory Management]]) into a two-stage decision with less overage and fewer lost sales. Early-warning rules: stop-ship and ramp-up thresholds (for example, if two-week sales are 40% below plan, cut the next order).

### Example
A season order of 10,000 units; the plan has 12% of season sales in weeks 1-2 (1,200 units). Actual weeks 1-2: 1,800. Scaled run-rate: 1,800/0.12 = **15,000**. Blend 50/50 with the prior: **12,500**. The firm reorders 2,500 more units from a quick-turn supplier rather than adopting the full 15,000 (risk: early rush from fans, then fade). If the actual had been 600, scaled = 5,000 and blend = 7,500: cut the next order and start markdown planning ([[160 Case Interview - Cost Reduction, Turnaround & Pricing]]).

### In the news
See news box. Planning vendors market "real-time" re-forecasting; the benefit appears only if the supply side can also react quickly.

### Interview angle
> [!question] How it is asked
> "The new phone has sold twice the plan in week 1. What do you do about supply?"

> [!tip] Strong answer includes
> - Separate launch spike from run-rate; use analogue curve share
> - Update with weighting, not a full flip
> - Supply options: expedite, allocate, reorder from flexible suppliers, prioritise channels
> - Customer communication and allocation rules

---
## 8. Causal and Regression Forecasting with Prices, Promotions and Events
> 🔴 Tier 1 · _Key points:_ Sales = f(price, promo, festival, weather); dummy variables

### Definition
Causal forecasting models demand as a function of **drivers** rather than just its own history:

$$Q_t = \beta_0 + \beta_1 \,Price_t + \beta_2 \,Promo_t + \beta_3 \,Festival_t + \dots + \varepsilon_t$$

Event effects use **dummy variables** (1 in the promotion or festival week, else 0), lagged terms capture pull-forward and post-promo dips, and log-log forms give elasticities directly. In practice: regression with seasonality (see [[090 Regression Analysis]]), ARIMAX or exponential smoothing with regressors ([[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]), or gradient-boosted trees using price and calendar features ([[218 Forecasting with ML & Foundation Models]], [[099 ML for Operations & SCM]]). Pitfalls: **multicollinearity** (promo and price cut occur together), **endogeneity** (promotions run when demand is already high), small samples. For true causal answers use experiments ([[214 Causal Inference & Experimentation Beyond A-B Tests]]).

### Example
Illustrative 12 weeks of data for a snack brand (price ₹/pack, promo flag, festival flag) fitted by least squares: **Sales = 1,874 − 13.8 × Price + 90.2 × Promo + 206.5 × Festival** units, R² = 0.99. Reading: each ₹1 price increase lowers weekly sales by about 14 units; a promotion adds about 90 units over the price effect; festival weeks add about 207. Forecast for a ₹95 week with promo and no festival: 1,874 − 13.8 × 95 + 90.2 = **≈ 656** units (about 653 with the rounded coefficients shown). Because price and promo overlap in the sample, the separate coefficients are fragile, so test them on a hold-out.

### In the news
See news box. SAP IBP's description of combining "multiple demand signals with statistical forecasts" is this idea productised.

### Interview angle
> [!question] How it is asked
> "How would you build a forecast that accounts for Diwali, discounts and weather?"

> [!tip] Strong answer includes
> - Drivers and dummies, lags and interaction terms
> - Validation: hold-out by time, not random split
> - Caveat: correlated drivers and endogenous promotions
> - Maintain an events calendar owned by marketing and sales

---
## 9. Price Elasticity of Demand
> 🔴 Tier 1 · _Key points:_ ε = %ΔQ / %ΔP; margin matters, not just revenue

### Definition
**Price elasticity** $\varepsilon = \dfrac{\%\Delta Q}{\%\Delta P}$ (negative for normal goods). $|\varepsilon| > 1$ is **elastic** (revenue rises when price falls), $|\varepsilon| < 1$ **inelastic**. Under constant elasticity, $Q = A\,P^{\varepsilon}$, so a price change from $P_0$ to $P_1$ changes volume by $(P_1/P_0)^{\varepsilon}-1$. Elasticity varies by category, channel, brand strength, and time (promo vs everyday price). Own-price elasticity is only half the picture: **cross-elasticity** captures substitutes and complements. For profit, the break-even test uses contribution margin: a price cut pays only if the volume gain outweighs the margin lost per unit.

### Example
Price ₹100, unit cost ₹70 (contribution ₹30), $\varepsilon = -2$. A 10% cut to ₹90: volume rises by $0.9^{-2} - 1 =$ **+23.5%** (the linear shortcut would say 20%). Revenue per base unit = 90 × 1.2346 = ₹111.1 (+11.1%), but contribution = (90 − 70) × 1.2346 = ₹24.7 against ₹30: **−17.7%**. Break-even elasticity for this cut is about −3.85. A revenue-based view says "cut price"; a margin view says "do not".

### In the news
See news box. AI pricing and promotion engines ride on estimated elasticities; trust (52% cite it as a barrier in IDC's survey) is the adoption bottleneck.

### Interview angle
> [!question] How it is asked
> "Should the firm cut price by 10% if elasticity is -2?"

> [!tip] Strong answer includes
> - Compute volume change using elasticity, then compare contribution, not revenue
> - Break-even elasticity as a function of margin
> - Cross-elasticity and cannibalisation; competitor reaction
> - Supply side: can capacity and inventory deliver the extra volume?

---
## 10. Promotion Lift, Pull-Forward and Cannibalisation
> 🔴 Tier 1 · _Key points:_ Baseline, uplift, post-promo dip, halo/cannibalisation, net incremental

### Definition
**Baseline** = expected sales without promotion. **Lift** = (promo sales − baseline) / baseline. Gross lift overstates value because of three offsets: **pull-forward** (consumers stock up, so later weeks dip, the "post-promotion trough"), **cannibalisation** (substitute SKUs or packs lose sales), and **channel shift/forward buying** by trade. Some promotions have a **halo** on complementary items. Net incremental volume and profit are measured against baseline across the whole window and the category:

$$\text{Net incremental units} = \text{Lift units} - \text{Pull-forward dip} - \text{Cannibalised units}$$

Operationally, promotions drive the largest forecast errors and cause the bullwhip through trade forward-buying ([[114 Bullwhip Effect, Beer Game & Information Sharing]]); EDLP (everyday low price) and trade-promotion optimisation address it ([[130 FMCG & Retail Distribution - India Route-to-Market]]).

### Example
Baseline 1,000 units a week at price ₹100, contribution ₹30. Promotion at 15% off (contribution ₹15): promo week 2,200 units (**lift +120%**), the next 2 weeks fall to 800 units each (dip 400), and a sister SKU loses 300 units (contribution ₹25).
- Net incremental units = 1,200 − 400 − 300 = **+500**.
- Profit: promo week 2,200 × 15 = 33,000 vs baseline 30,000: +3,000; dip weeks: (800 − 1,000) × 30 × 2 = −12,000; cannibalisation: −300 × 25 = −7,500; **net −₹16,500**.
Strong volume lift, yet the promotion destroys profit unless the objective is trial, distribution or share.

### In the news
See news box. Promotion calendars are one of the first inputs to AI planning tools; their "multiple demand signals" claim covers this.

### Interview angle
> [!question] How it is asked
> "A promotion lifted sales 120%. Was it a success?"

> [!tip] Strong answer includes
> - Net out dip, cannibalisation and discount cost, then compare profit
> - Objectives: trial, share, clearance, traffic
> - Supply impact: promo spikes need stock, pack-size and logistics planning
> - Post-promotion evaluation and learning loop

---
## 11. Demand Shaping: Price, Promotion, Assortment and Availability
> 🔴 Tier 1 · _Key points:_ Steer demand to match supply, margin and inventory

### Definition
**Demand shaping** uses commercial levers to move demand towards what the supply chain can deliver profitably, instead of only forecasting it. Levers:
- **Price and revenue management**: markdown cadence, dynamic pricing, surge pricing, discounts on short-dated or excess stock ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]]).
- **Promotion design**: timing, depth, pack, channel; avoid peaks that exceed capacity.
- **Assortment and substitution**: promote items with available stock, de-list low-margin variants ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]).
- **Availability and lead-time signalling**: show lead times, push later delivery slots, nudge to cheaper fulfilment (consolidated slots, pickup).
- **Allocation and order rules**: minimum order quantity, cut-off times, quotas ([[138 Order Management, Customer Service & Cost-to-Serve]]).
The loop is run in S&OP: the demand review proposes shaping actions where supply is constrained or inventory is high ([[120 Integrated Business Planning (IBP) & S&OP Maturity]]).

### Example
A fashion retailer has 40,000 units of a colour that is selling at 60% of plan with 10 weeks of season left. Options: 20% markdown now (elasticity −2.5 raises volume by about 0.8^{-2.5} − 1 = 75%) or a bundle with a fast seller. Compute sell-through under each, choose the one that clears stock by week 10 at the best margin. In quick commerce, a platform shows a 'fastest slot' premium or delivery fee when dark-store capacity is saturated, shaping demand across time.

### In the news
See news box. Kinaxis, SAP and others position scenario planning (what-if on demand and supply) as the tool for testing shaping actions before executing them.

### Interview angle
> [!question] How it is asked
> "Supply is constrained for the festive season. How do you manage demand?"

> [!tip] Strong answer includes
> - Levers: price, promotion, assortment, allocation, lead-time signalling
> - Prioritise customers/channels by margin and strategic value
> - Quantify effect via elasticity; check cannibalisation
> - Coordination with sales and finance in S&OP

---
## 12. Demand Sensing: Short-Term Forecasts from Fresh Signals
> 🔴 Tier 1 · _Key points:_ Days-to-weeks horizon, POS/orders/weather signals, adjusts statistical baseline

### Definition
**Demand sensing** improves the **near-term** forecast (typically days to a few weeks) by using recent, high-frequency signals: point-of-sale and sell-through data, open orders and shipment patterns, inventory at customers, weather, local events, web and social signals, and competitor price. A statistical model learns how deviations from the baseline in the last days predict the next days, then adjusts the operational forecast. It differs from **demand planning** (monthly, consensus, causal, tactical) and from **demand shaping** (influencing demand). Value comes from better allocation, replenishment and expediting in the **execution horizon**, not from the S&OP plan, and depends on signal latency and data quality ([[175 Data Quality, Master Data & Data Governance]]). Tools: SAP IBP demand sensing, Kinaxis, o9, Blue Yonder, RELEX, ToolsGroup; see [[198 SAP IBP, APO & Demand-Driven Planning]] and [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]. Measure with weighted MAPE and **bias** at the lead time that matters, and compare with the baseline using forecast value added.

### Example
Six days of demand: actual 120, 135, 110, 150, 160, 140 (total 815). Static forecast 100/day gives absolute errors 20, 35, 10, 50, 60, 40: **WMAPE = 215/815 = 26.4%**. A sensing model that updates daily (108, 125, 120, 138, 150, 152) has errors 12, 10, 10, 12, 10, 12: **WMAPE = 66/815 = 8.1%**. The reduction of about 18 points on the next-week forecast lets the DC cut a day's safety stock: with Z = 1.65, shrinking the daily forecast-error s.d. from 40 to 15 over a 4-day lead time cuts safety stock from 1.65 × 40 × 2 = 132 to 1.65 × 15 × 2 = about 50 units, a **62% reduction**.

### In the news
See news box. SAP lists demand sensing as an IBP module to "refine short-term forecasts to drive better fulfillment and inventory reduction", and IDC's data show 98% of leaders have some AI capability but only 12% see themselves as leaders.

### Interview angle
> [!question] How it is asked
> "What is demand sensing and how is it different from demand planning?"

> [!tip] Strong answer includes
> - Short horizon, fresh signals, adjusts the baseline; plan is tactical and consensus-based
> - Signals and data latency; benefits in allocation, replenishment, safety stock
> - Measure with WMAPE and bias at execution lead time; compare with baseline
> - Limits: no help for long lead times; risk of over-reacting to noise

---
## 13. Consensus Forecasting, Governance and Forecast Value Added
> 🔴 Tier 1 · _Key points:_ One number, accountable owners, bias control

### Definition
**Consensus forecasting** combines the statistical baseline with sales, marketing, finance and operations input into one agreed demand plan in the **demand review** of the S&OP cycle ([[120 Integrated Business Planning (IBP) & S&OP Maturity]]). Rules that keep it honest: ownership by commercial teams (demand is a sales number, not a supply number), **override discipline** (every change logged with a reason and owner), **FVA analysis** (does each touch beat the previous step?), and separation of the **forecast** (unbiased expectation) from the **target** (aspiration) and the **budget**. Common problems: sandbagging (sales lowball to beat plan), optimism (marketing), and "gaming" supply with high forecasts. Track **bias** (mean forecast error) and tracking signal along with MAPE; collaborate with key customers where data sharing exists (CPFR; see [[004 Demand Forecasting & Planning]]).

### Example
Statistical forecast MAPE 22%; after sales overrides MAPE 25%; after consensus 20%. FVA of sales override = 22 − 25 = **−3 points** (it hurt); consensus FVA = +5 points vs override stage. Action: restrict sales overrides to promotions and new items with documented reasons, and keep the model for the rest. Bias of +8% (over-forecast) for a product line is an inventory-write-down risk ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]]).

### In the news
See news box. IDC's finding that 67% say accountability for AI outcomes will require significant governance changes reaches here: who owns an algorithmic override matters.

### Interview angle
> [!question] How it is asked
> "Sales and supply chain disagree on the forecast every month. How do you resolve it?"

> [!tip] Strong answer includes
> - Single-number process with agreed calendar and data
> - Separate forecast from target; FVA and bias metrics
> - Escalation rule: unresolved gaps go to the executive S&OP with scenarios
> - Incentives: measure forecast accuracy and bias, not just revenue vs target

---
## 14. ⭐ Advanced: AI/ML Demand Forecasting, Cold Start and Vendor Landscape
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Modern demand platforms use **global (cross-learning) models** trained across all SKUs (gradient boosting, deep learning, foundation models) with features for price, promotions, calendar, weather and product attributes, which also helps **cold-start** products: a new item's forecast borrows from similar items through attributes (category, price band, brand, colour) rather than from its own history. Probabilistic forecasts (quantiles) feed safety stock and newsvendor decisions. Vendors and platforms: **SAP IBP**, **Kinaxis Maestro**, **o9**, **Blue Yonder**, **RELEX**, **ToolsGroup**, **Anaplan** and cloud ML services; see [[218 Forecasting with ML & Foundation Models]] and [[099 ML for Operations & SCM]]. Evaluate on a hold-out with a **naive benchmark**, FVA, bias, and **business metrics** (service level, inventory days), and require explainability and override tracking ([[220 Responsible AI, Explainability & Model Governance]]).

### Example
A retailer's 12-month pilot on 5,000 new SKUs: statistical baseline WMAPE 48% on first-8-week sales; attribute-based global model 38%; blended with merchandiser judgement 35%. The 10-point gain on SKUs with ₹300 crore of sales and 25% gross margin matters if it reduces unsold and lost-sale units; compute the benefit from both overage and underage before approving a roll-out. Note that these pilot numbers are illustrative, not a vendor benchmark.

### In the news
See news box. Kinaxis is also named Leader in Gartner's 2026 Magic Quadrants (vendor-reported); Indian manufacturers such as STL have selected Kinaxis Planning One (August 2026), which shows mid-market adoption of cloud planning in India ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/sterlite-technologies-limited-selects-kinaxis-strengthen-supply-chain)).

### Interview angle
> [!question] How it is asked
> "Would you use AI to forecast new products? What are the risks?"

> [!tip] Strong answer includes
> - Global models and attribute-based cold start; probabilistic outputs
> - Benchmarking against naive and FVA; hold-out by time
> - Risks: data quality, bias, overfitting to promotions, black-box overrides
> - Operating model: human-in-the-loop, governance, clear ownership
