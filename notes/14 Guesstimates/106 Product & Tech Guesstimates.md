---
tags: [guesstimates, tier2]
area: Guesstimates
topic: "Product & Tech Guesstimates"
tier: Tier 2
roles: Consulting / PM
status: complete
subtopics: 8
---
# Product & Tech Guesstimates

⬅ [[105 Operations & SCM Guesstimates]] · [[_Index - Guesstimates|Guesstimates]] · [[107 Common Mistakes & How to Avoid]] ➡

> **Area:** Guesstimates · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / PM

## Sub-topics in this note
1. [[#1. Server capacity for a food delivery app]]
2. [[#2. Storage for Netflix India]]
3. [[#3. Bandwidth for YouTube India]]
4. [[#4. How many engineers does Flipkart need?]]
5. [[#5. App downloads for a new fintech in Year 1]]
6. [[#6. DAU for a B2B SaaS operations tool]]
7. [[#7. ⭐ Advanced: Back-of-envelope system design (QPS, storage, read/write ratio)]]
8. [[#8. ⭐ Advanced: Unit economics (CAC, LTV) for sizing an app business]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's streaming and app peaks are now measured in tens of millions of simultaneous users
> **IPL 2025 on JioStar (reported 19 Jun 2025).** JioStar reported **840 billion minutes** of total watch time for IPL 2025 across TV and digital and a reach of about **1 billion** viewers. The RCB vs PBKS final alone drew **31.7 billion minutes**, **892 million digital video views** and a **peak concurrency of 55 million** simultaneous viewers, even though the tournament was suspended for a week. Peak concurrency, not daily average, is what sizes bandwidth and servers. ([Business Standard](https://www.business-standard.com/industry/news/ipl-2025-breaks-viewership-records-rcb-final-draws-840-billion-minutes-125061900901_1.html))
> 
> **Eternal (Zomato + Blinkit), Q2 FY26 (Oct 2025).** Revenue of **₹13,590 crore (+183% YoY)** with Blinkit at ₹9,891 crore: an app business whose order growth directly drives API calls, payments and tracking load. ([INDmoney](https://www.indmoney.com/blog/stocks/eternal-zomato-q2-results))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Server capacity for a food delivery app
> 🟠 Tier 2 · _Tracker hint:_ Peak orders/sec × processing time × API calls per order → compute units; scale with cloud auto-scaling

### Definition
Capacity planning for a web service starts from **peak requests per second (QPS)** and the work per request.

$$\text{QPS}_{peak} = \frac{\text{Orders/day} \times \text{Peak-hour share}}{3600} \times \text{API calls per order}$$
$$\text{Servers} = \frac{\text{QPS}_{peak}}{\text{QPS per server} \times \text{Target utilisation}} \times (1 + \text{redundancy})$$

Count **all** traffic: browsing and search (the vast majority), cart, payment, and live-tracking polls. Peak-hour share for food is about 10–15% of daily orders in a 1-hour window (dinner). Add headroom (N+1 or N+2), and note auto-scaling handles variation but databases and payment gateways scale less elastically.

### Example
Assume 3M orders/day; peak hour holds 12% = 360,000 orders → 100 orders/s. If each order generates about 300 API calls over its session (browse, search, cart, pay, tracking polls), QPS = 100 × 300 = **30,000 requests/s**. One 8-vCPU server handles ~1,000 req/s at 50% utilisation → 30 servers; with 2x headroom for failover and spikes ≈ **60 servers** (stateless tier). The database tier is sized separately by write rate (about 100 orders/s plus status updates).

### In the news
See news box. Eternal's order growth and JioStar's 55M concurrent viewers show that Indian traffic is spiky around meals and events, so auto-scaling rules matter more than average load.

### Interview angle
> [!question] How it is asked
> "How many servers would Zomato need on New Year's Eve?" or (PM interview) "How would you prepare for a 5x traffic spike?"

> [!tip] Strong answer includes
> - Peak, not average, and a peak-hour share assumption
> - API calls per order including browse and polling
> - Stateless vs stateful tiers and where the bottleneck is
> - Auto-scaling, caching, queueing and graceful degradation

---

## 2. Storage for Netflix India
> 🟠 Tier 2 · _Tracker hint:_ ~50M subscribers; avg 2 hrs/day; ~1GB/hr (HD) → 100PB+ (but compression + encoding reduces)

### Definition
Separate **data streamed** (traffic) from **data stored** (capacity). The tracker's product, 50M × 2 h × 1 GB/h = 100M GB = **100 PB per day**, is daily *delivery traffic*, not storage; the subscriber count is also an assumption (I have not verified Netflix India's subscriber base). Storage depends on the **catalogue**, not on viewers.

$$\text{Storage} = \text{Catalogue hours} \times (\text{Master size/h} + \text{Encoded ladder size/h}) \times \text{Replication}$$

Streaming services encode each title into many bitrate/resolution/codec versions (an "encoding ladder") and cache popular titles at ISP edge servers (CDN). So total stored data includes origin copies and distributed edge copies of the popular subset.

### Example
Assume 15,000 titles × 1.5 h = 22,500 hours. Masters at 0.5 TB/h = 11,250 TB ≈ 11 PB. Encoded ladder at ~12 GB/h (sum over all versions) = 270,000 GB = 270 TB. Origin storage ≈ **11–12 PB**, even with 2–3 replicas only ~35 PB. Edge caches hold the top few percent of titles per ISP. Delivery traffic is the 100 PB/day, handled mostly by edge caches.

### In the news
See news box. Event streaming (IPL on JioStar: 892M views for one match) is the extreme case where traffic dominates; storage needs for one live match are small.

### Interview angle
> [!question] How it is asked
> "Estimate how much storage Netflix needs for India." The trap is mixing traffic with storage.

> [!tip] Strong answer includes
> - Explicit split: storage (catalogue) vs bandwidth (viewers)
> - Encoding ladder and replication
> - CDN edge caching reduces origin traffic
> - A sanity check against known catalogue size

---

## 3. Bandwidth for YouTube India
> 🟠 Tier 2 · _Tracker hint:_ ~500M views/day; avg 5 min; 5Mbps stream → 5×500M×5×60×5 Mbps → ~750 Tbps peak

### Definition
Bandwidth is a **rate** (bits per second); total data over a day is a **volume**. Method: total viewing seconds × bitrate gives daily bits; divide by 86,400 s for the average rate; multiply by a **peak-to-average factor** (2–3x for evening peaks).

$$\text{Avg bandwidth} = \frac{\text{Views/day} \times \text{Seconds per view} \times \text{Bitrate}}{86{,}400}$$

Use consistent units: 1 Tbps = $10^{12}$ bit/s = $10^6$ Mbps. Bitrate also depends on device (mobile 1–3 Mbps typical, TV higher) so a blended bitrate is realistic.

### Example
500M views × 300 s = $1.5\times10^{11}$ s of viewing/day. × 5 Mbps = $7.5\times10^{11}$ Mb = 750,000 Tb = **750 Pb (petabits) per day** (about 94 PB). Divide by 86,400: **≈ 8.7 Tbps average**; with a 3x peak factor ≈ **26 Tbps peak**.
Note the tracker's "750 Tbps" arises from reading the *total* ($7.5\times10^{11}$ Mb) as a rate; it is a units slip, exactly the error [[107 Common Mistakes & How to Avoid]] warns about. Cross-check with the news box: 55M concurrent viewers at an assumed 2.5 Mbps = 137.5 Tbps for a single record live event.

### In the news
See news box. At 55M peak concurrent viewers, bandwidth is set by concurrency × bitrate, not by daily views.

### Interview angle
> [!question] How it is asked
> "Estimate YouTube's bandwidth in India" or "How much bandwidth is needed to stream the IPL final?"

> [!tip] Strong answer includes
> - Units discipline (bits vs bytes, rate vs volume)
> - Average then peak, with a peak factor
> - Concurrency method as a cross-check
> - CDN/ISP edge caching and adaptive bitrate as levers

---

## 4. How many engineers does Flipkart need?
> 🟠 Tier 2 · _Tracker hint:_ ~1M orders/day; engineering ratio 1:5K orders/day → 200 core engineers; 10x for product/infra = 2,000

### Definition
Engineering headcount can be estimated by **volume-based ratio** (orders per engineer) or by **scope-based build-up** (teams × team size). A ratio heuristic is fragile because engineering effort scales with product surface area and complexity, not linearly with orders. Use the ratio as a rough cross-check and the team build-up as the primary method.

$$\text{Engineers} = \text{Teams} \times \text{Engineers per team}$$

Typical layers: consumer app (search, catalogue, cart, checkout, payments), supply chain tech (WMS, TMS, routing), seller tools, data/ML, platform/infra, and security.

### Example
Tracker: 1M orders/day ÷ 5,000 = **200 core engineers**; ×10 for product, data, infra, QA, support = **~2,000**.
Build-up check: 40 product teams × 8 engineers = 320; add platform/infra/data (about 3x) ≈ 1,000+; add QA and mobile ≈ 1,500–2,000. The two routes land in the same order of magnitude; I have not verified Flipkart's actual headcount.

### In the news
See news box. A higher order volume (Blinkit at ₹9,891 crore revenue) justifies dedicated supply-chain tech and ML teams (demand forecasting, routing), which is where headcount actually grows.

### Interview angle
> [!question] How it is asked
> "How many engineers does an e-commerce company with 1M orders a day need?" (PM and consulting)

> [!tip] Strong answer includes
> - Teams-times-size build-up and a ratio cross-check
> - Awareness that complexity, not volume, drives headcount
> - Layers: product, platform, data, supply-chain tech
> - Build vs buy and productivity levers

---

## 5. App downloads for a new fintech in Year 1
> 🟠 Tier 2 · _Tracker hint:_ Target urban India 100M; awareness 10%; interest 30%; install 20%; active 50% → 3M actives

### Definition
A **funnel guesstimate** multiplies conversion steps from addressable market to active users:

$$\text{Actives} = \text{TAM} \times \text{Awareness} \times \text{Interest} \times \text{Install} \times \text{Active}$$

Define each stage carefully: awareness (reached by marketing), interest (considers), install (downloads), active (monthly or weekly active). Replace guessed conversion rates by benchmarks (CAC, store conversion) when possible, and tie the funnel to the marketing budget: installs = budget ÷ cost per install.

### Example
100M × 10% = 10M aware; × 30% = 3M interested; × 20% = 600,000 installs; × 50% = **300,000 active users**.
The tracker's "3M actives" is the *interested* stage (3M); applying the last two stages gives 0.3M. Check: $100 \times 0.1 \times 0.3 \times 0.2 \times 0.5 = 0.3$ million. Cost view: at ₹150 per install, 600,000 installs cost ₹9 crore.

### In the news
See news box. Eternal and the IPL show how a single distribution moment (a match, a promotion) can move awareness quickly; fintech launches often piggyback on such events.

### Interview angle
> [!question] How it is asked
> "How many users can a new UPI/credit app get in Year 1?"

> [!tip] Strong answer includes
> - Defined funnel stages and honest conversion assumptions
> - Cross-check with budget and CAC
> - Segment by cohort (students, salaried, merchants)
> - Distinction between downloads, activations and retained users

---

## 6. DAU for a B2B SaaS operations tool
> 🟠 Tier 2 · _Tracker hint:_ Target: 50K companies × 5 users × 60% daily activity → 150K DAU

### Definition
$$DAU = \text{Customers} \times \text{Seats per customer} \times \text{Daily activity rate}$$

B2B DAU is driven by **seats** (licensed users) and usage habit, not downloads. Separate the **addressable** companies from **paying** customers: Year-1 penetration is a small share of the target. Healthy products show a DAU/MAU ratio (stickiness) of 40–60% for workflow tools; lower for periodic tools such as reporting.

### Example
Tracker: 50,000 × 5 × 60% = **150,000 DAU**; check: 50,000 × 5 = 250,000 seats × 0.6 = 150,000 ✓. This presumes all 50K companies are customers. With 5% Year-1 penetration: 2,500 companies × 5 × 0.6 = **7,500 DAU**. State which version you are answering.

### In the news
See news box. Enterprise tools for warehouse and delivery operations ride on the same growth in quick commerce and e-commerce volumes.

### Interview angle
> [!question] How it is asked
> "Estimate DAU for an operations SaaS tool" (PM roles).

> [!tip] Strong answer includes
> - Customers × seats × activity, with penetration over time
> - Distinction between target market and actual customers
> - DAU/MAU stickiness benchmarks
> - Metric choice: workflow tools may care about weekly active

---

## 7. ⭐ Advanced: Back-of-envelope system design (QPS, storage, read/write ratio)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
PM and tech interviews often ask for **system-design numbers**: writes per second, reads per second, storage growth. Recipe: (1) monthly volume; (2) divide by seconds (a month ≈ 2.6M s, a day = 86,400 s); (3) apply read:write ratio; (4) bytes per record × records × retention. Useful reference: 1 KB = $10^3$ B, 1 TB = $10^{12}$ B.

### Example
URL shortener: 100M new URLs/month. Write QPS = 100M / 2.592M ≈ **39/s**. At a 100:1 read:write ratio, read QPS ≈ **3,900/s**. Record 500 B: monthly storage 100M × 500 B = 50 GB; 5 years = 60 months × 50 GB = **3 TB**, small enough for a single sharded database.

### In the news
See news box. At the 55M-concurrent-viewer peak, read-heavy workloads depend on CDN and caching, not the origin database.

### Interview angle
> [!question] How it is asked
> "Design TinyURL and estimate the scale", or "How many requests per second will this feature generate?"

> [!tip] Strong answer includes
> - Clear read/write split
> - Peak factor (2–3x average)
> - Storage from bytes × records × retention
> - Identifying the true bottleneck (network, DB, cache)

---

## 8. ⭐ Advanced: Unit economics (CAC, LTV) for sizing an app business
> ⭐ Advanced · _Added beyond the tracker_

### Definition
After the funnel gives users, test the **economics**:

$$LTV = \frac{ARPU \times \text{Gross margin}}{\text{Churn rate}}, \quad \text{Rule of thumb: } LTV/CAC \ge 3$$

CAC is cost to acquire a paying user; payback = CAC ÷ (ARPU × gross margin) in months. For marketplaces and delivery apps add contribution margin per order after delivery and discount costs.

### Example
CAC ₹300; ARPU ₹40/month; gross margin 60%; monthly churn 5%. LTV = 40 × 0.6 / 0.05 = **₹480**; LTV/CAC = 1.6 (below 3). Payback = 300 / (40 × 0.6) = **12.5 months**. Either cut CAC to ₹160 or raise ARPU or reduce churn to 3% (LTV = ₹800; ratio 2.7).

### In the news
See news box. Eternal's profit of only ₹65 crore on ₹13,590 crore revenue in Q2 FY26 shows how thin contribution margins can be at scale.

### Interview angle
> [!question] How it is asked
> "Is this fintech app a good business? What do you need to believe?"

> [!tip] Strong answer includes
> - LTV, CAC and payback with a formula
> - Sensitivity to churn
> - Contribution margin, not revenue
> - Levers to improve and the assumption most at risk

---
## 🔗 Go deeper: expansion notes
- [[222 Infrastructure, Energy, Healthcare & Public-Sector Guesstimates|Infrastructure, Energy, Healthcare & Public-Sector Guesstimates]]
