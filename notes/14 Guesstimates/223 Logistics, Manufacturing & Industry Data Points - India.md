---
tags: [guesstimates, tier1]
area: Guesstimates
topic: "Logistics, Manufacturing & Industry Data Points - India"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 13
---
# Logistics, Manufacturing & Industry Data Points - India

⬅ [[222 Infrastructure, Energy, Healthcare & Public-Sector Guesstimates]] · [[_Index - Guesstimates|Guesstimates]]

> **Area:** Guesstimates · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. How to Use This Data Sheet]]
2. [[#2. Macro, Population and Income Anchors]]
3. [[#3. Logistics Cost and Modal Split]]
4. [[#4. Roads, Vehicles and Trucks]]
5. [[#5. Railways and Freight Corridors]]
6. [[#6. Ports, Containers and Shipping]]
7. [[#7. Warehousing, Cold Chain and E-commerce]]
8. [[#8. GST, Tax and Trade]]
9. [[#9. Manufacturing and Core Industries]]
10. [[#10. Power and Energy]]
11. [[#11. Consumer, Telecom and Digital Reference Points]]
12. [[#12. ⭐ Advanced: Conversion Ratios and Derived Constants]]
13. [[#13. ⭐ Advanced: Reconciling Conflicting Sources and Maintaining the Sheet]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the latest official and industry numbers, with the date checked
> **GST: FY26 closed at ₹22.27 lakh crore gross (Business Standard topic page, checked Oct 2026).** Gross GST collection for April 2025 to March 2026 was **₹22.27 lakh crore (+8.3%)** and net **₹19.34 lakh crore (+7.1%)**; the first half of FY2026-27 (April to September 2026) was **₹12.46 lakh crore gross (+11.6%)**, with September 2026 at **₹2.04 trillion (+14.7%)**. GST 2.0 moved the structure to **5%, 18% and 40%** slabs from 22 September 2025. ([Business Standard](https://www.business-standard.com/topic/gst-collection); [Wikipedia: GST in India](https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)))
>
> **Power demand hit a record (2026).** Installed capacity of **532.7 GW** (March 2026), a record peak of **270.82 GW on 21 May 2026**, FY26 generation of **1,840 TWh**. ([Wikipedia: Electricity sector in India](https://en.wikipedia.org/wiki/Electricity_sector_in_India))
>
> **Core industries expand.** Cement output was about **453 MT in FY25** against **668 MT** of capacity ([IBEF cement](https://www.ibef.org/industry/cement-india)); crude steel was **54.19 MT in April-July 2025**, with a 300 MT capacity goal for 2030 ([IBEF steel](https://www.ibef.org/industry/steel)); SIAM reported **3,10,34,174 vehicles produced** and **1,96,07,332 two-wheelers sold** in FY2024-25 ([SIAM](https://www.siam.in/pressrelease-details.aspx?mpgid=48&pgidtrail=50&pid=579)).
>
> **Trade infrastructure.** Major ports handled about **855 MT in FY25** ([IBEF](https://www.ibef.org/industry/ports-india-shipping)) and India's container traffic was **23.9 million TEU in 2024** ([World Bank API](https://api.worldbank.org/v2/country/IND/indicator/IS.SHP.GOOD.TU?format=json&per_page=10&mrv=6)).
>
> **Consumer and digital reference points.** Wireless subscribers were **1,312.25 million** in August 2026 ([TelecomTalk](https://telecomtalk.info/india-wireless-telecom-subscriber-base-130billion-august2026/1012285/)); NIQ reported FMCG value growth of **7.8%** in Oct-Dec 2025 ([NIQ](https://nielseniq.com/global/en/news-center/2026/niq-gst-2-0-transition-reshapes-indias-fmcg-growth-landscape/)); UPI recorded **24,161.69 crore transactions worth ₹314 lakh crore** in FY2025-26 ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=2)).
>
> Sub-topics that say **"See news box"** reuse these items. **Reading the tables**: each row gives value, year, source and a confidence tag: **H** = official or regulator figure read from the cited page; **M** = reputable secondary source read from the cited page; **L** = single market estimate, undated, or recalled and not re-fetched. **Last updated: 4 October 2026.** Re-check before quoting.

---
## 1. How to Use This Data Sheet
> 🔴 Tier 1 · _Key points:_ value, year, source, confidence; round to a spoken number; keep the exact number beside it

### Definition
A guesstimate is only as good as its anchors. This note collects the anchors for logistics, manufacturing and industry, each with **year**, **source link** and **confidence**. Rules for use:
1. **Say the round number, keep the exact one**: "about 1.46 billion" (exact 1,463,865,525).
2. **State the year and the definition** when quoting: "FY25 gross GST, not net".
3. **Never mix years silently**: a 2021 tonne-km figure divided by a 2023 loading figure gives a wrong lead distance.
4. **Prefer a ratio over a level** when sources disagree: shares and per-capita figures travel better.
5. **Refresh calendar**: GST (1st of each month), SIAM and TRAI (monthly), CEA power (monthly), NIQ and WGC (quarterly), GDP (quarterly, MoSPI), Economic Survey (January-February).

Links to the rest of the guesstimate area: method in [[102 Guesstimate Framework]], population and consumption anchors in [[103 Key India Data Points to Memorize]], templates in [[104 Classic Guesstimate Types & Templates]] and [[105 Operations & SCM Guesstimates]], practice sets in [[221 Retail, FMCG & Consumer Guesstimates - Practice Set]] and [[222 Infrastructure, Energy, Healthcare & Public-Sector Guesstimates]].

### Example
**Sanity-checking a quoted figure.** A candidate says "India's logistics bill is about ₹26 lakh crore." Check: logistics cost about 8% of GDP (Wikipedia, FY2023-24; M) × FY25 nominal GDP of ₹331.03 lakh crore (IBEF; M) = **₹26.5 lakh crore**. The two figures use adjacent years, so state it: "about ₹26 lakh crore, using 8% of GDP; the exact share depends on the study (published estimates range from about 8% to near 9%; recalled, L)".

### In the news
See news box. GST, power and SIAM figures are published on fixed monthly cycles, so a quick refresh before an interview is realistic.

### Interview angle
> [!question] How it is asked
> "Do you know the current numbers?" or "Where did that figure come from?"

> [!tip] Strong answer includes
> - A round number with the year and definition
> - The source type (regulator, industry body, market research) and your confidence
> - A cross-check with a ratio or a second data point
> - Honesty about stale or contested numbers

---
## 2. Macro, Population and Income Anchors
> 🔴 Tier 1 · _Key points:_ population, GDP, per capita, urban share, income ladder

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Population | **1,463,865,525** (1.46 billion); UNFPA: 146.39 crore | 2025 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/SP.POP.TOTL?format=json&per_page=10&mrv=4) | H |
| Urban share | **35.69%** | 2025 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/SP.URB.TOTL.IN.ZS?format=json&per_page=10&mrv=4) | H |
| Nominal GDP | **₹3,31,03,000 crore (₹331 lakh crore)**; US$3.78 trillion | FY25 | [IBEF](https://www.ibef.org/economy/indian-economy-overview) | M |
| Nominal GDP (World Bank) | **US$3.956 trillion** | 2025 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/NY.GDP.MKTP.CD?format=json&per_page=10&mrv=4) | H |
| GDP per capita | **US$2,702** (World Bank); US$2,813 (Wikipedia, FY26) | 2025 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/NY.GDP.PCAP.CD?format=json&per_page=10&mrv=4) | H/M |
| GVA shares | Agriculture 14.3%, industry 27.6%, manufacturing 17.0%, services 54.7% | FY24 | [Wikipedia: Economy of India](https://en.wikipedia.org/wiki/Economy_of_India) | M |
| Households | about 300 million (1.46B ÷ 4.5) | derived | [[103 Key India Data Points to Memorize]] | M |
| Income ladder | 5% affluent (above ₹10 lakh), 25% middle, 35% lower middle, 35% low | heuristic | [[103 Key India Data Points to Memorize]] | L |

Implied exchange rates: ₹331.03 lakh crore ÷ US$3.78 trillion = **₹87.6 per dollar**; exports ₹70.36 lakh crore ÷ US$825 billion = **₹85.3** (IBEF, FY25). Always state the rate you assume.

### Example
**Does the income ladder fit GDP?** GDP per household = ₹331.03 lakh crore ÷ 300M = **₹11.0 lakh**; GDP per capita = ₹331.03 × 10¹² ÷ 1.4639 × 10⁹ = **₹2.26 lakh**. Using midpoints ₹25 lakh, ₹6.5 lakh, ₹2 lakh and ₹0.6 lakh for the four tiers, mean household income = 0.05 × 25 + 0.25 × 6.5 + 0.35 × 2 + 0.35 × 0.6 = **₹3.79 lakh**, about 34% of GDP per household. Household income is typically a smaller share of GDP than 100% (corporate profits, government and others), but 34% is low, so the ladder likely understates the top end. Use it as a heuristic only.

### In the news
See news box. The three GDP figures (US$3.78 trillion IBEF FY25, US$3.956 trillion World Bank 2025, US$4.15 trillion Wikipedia FY26) differ by year and definition, a live example for [[180 Current Affairs & Economy Briefing for MBA Interviews (2025-26)]].

### Interview angle
> [!question] How it is asked
> "What is India's GDP and per-capita income?" as the base of a market-size question.

> [!tip] Strong answer includes
> - Rupee and dollar versions with the exchange rate stated
> - Per-household and per-capita views
> - The financial year or calendar year used
> - A caveat on heuristics such as the income ladder

---
## 3. Logistics Cost and Modal Split
> 🔴 Tier 1 · _Key points:_ about 8% of GDP; road about two-thirds of freight; cost per tonne-km by mode

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Transport logistics cost | **about 8% of GDP** | FY2023-24 | [Wikipedia: Transport in India](https://en.wikipedia.org/wiki/Transport_in_India) | L/M |
| Road share | **about 66% of freight, 82% of passenger traffic** | latest in article | same | M |
| Cost per km by mode (as cited) | rail ₹1.96, waterways ₹2.30, road ₹3.78, air ₹72 | FY2023-24 | same (unit "per km"; read as per tonne-km, check) | L |
| Logistics Performance Index | **3.40 (score out of 5)** | 2022 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/LP.LPI.OVRL.XQ?format=json&per_page=10&mrv=6) | H |
| LPI history | 3.12 (2010), 3.08 (2012), 3.08 (2014), 3.42 (2016), 3.18 (2018) | various | same | H |

Concept: logistics cost = transport + warehousing + inventory carrying + admin; headline percentages depend on the study and on what is included. The policy goal is to reduce the share through the National Logistics Policy, Gati Shakti and freight corridors ([[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]); operating levers are in [[009 Logistics & Distribution]] and [[125 Transportation Management Deep Dive]].

### Example
**Value of a one-point cut.** One percentage point of FY25 GDP = 0.01 × ₹331.03 lakh crore = **₹3.31 lakh crore** a year. Cutting from 8% to 7% saves ₹3.3 lakh crore, about the size of 15% of annual gross GST collections (₹3.31 ÷ 22.27). **Mode cost gap** (cited per-km costs): road ₹3.78 vs rail ₹1.96 means road costs **1.93×** rail; shifting 10% of the road tonne-km to rail cuts the cost of that freight by about (3.78 − 1.96) × 0.10 ÷ 3.78 ≈ **4.8%** of the road freight bill, before first-mile, last-mile and transfer costs.

### In the news
See news box. GST and policy changes (GST 2.0 slabs, e-way bill and logistics reforms) interact with route choice; see [[227 GST & Indirect Tax for Supply Chains]].

### Interview angle
> [!question] How it is asked
> "What is India's logistics cost as a share of GDP and why is it high?"

> [!tip] Strong answer includes
> - The approximate share and the fact that estimates differ by study
> - Reasons: road-heavy modal mix, fragmented trucking, dwell times, inventory
> - A quantified value of a one-point reduction
> - Levers: modal shift, corridors, digital documentation, warehousing

---
## 4. Roads, Vehicles and Trucks
> 🔴 Tier 1 · _Key points:_ road network; SIAM sales and production; stock vs sales

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Road network | about **6.7 million km** | 2024 est. | [Wikipedia: Transport in India](https://en.wikipedia.org/wiki/Transport_in_India) | M |
| National highways | **146,204 km** (IBEF); 161,350 km (Wikipedia) | FY25 / 2024 | [IBEF roads](https://www.ibef.org/industry/roads-india) | M (conflict) |
| Vehicle production | **3,10,34,174** (all categories) | FY2024-25 | [SIAM](https://www.siam.in/pressrelease-details.aspx?mpgid=48&pgidtrail=50&pid=579) | H |
| Domestic sales | passenger vehicles **43,01,848**; two-wheelers **1,96,07,332**; three-wheelers **7,41,420**; commercial **9,56,671** | FY2024-25 | same | H |
| Total domestic sales | **2,56,07,271** (sum of the four) | FY2024-25 | derived | H |
| Registered vehicle stock | about 250M two-wheelers, 35M cars, 8M commercial, 3M tractors | tracker | [[103 Key India Data Points to Memorize]] | L |

Notes: SIAM figures are dispatches from manufacturers, not registrations; goods-vehicle fleet counts come from MoRTH and Vahan (not fetched here). The two-wheeler share of domestic sales is 19,607,332 ÷ 25,607,271 = **76.6%**.

### Example
**Replacement cycle check.** Stock ÷ annual sales: 250M two-wheelers ÷ 19.6M sold = **12.7 years**, consistent with a 12-15 year vehicle life plus growth. For cars: 35M ÷ 4.3M = **8.1 years**, shorter because the car stock is younger and growing faster. Commercial vehicles: 8M ÷ 0.96M = 8.3 years. If an interviewer asks for annual two-wheeler demand without giving sales, "stock ÷ life" gives 250 ÷ 13 ≈ **19 million**, within 2% of SIAM's 19.6 million.

### In the news
See news box. The conflicting national-highway lengths (146,204 km vs 161,350 km) show why a source column matters; see sub-topic 13.

### Interview angle
> [!question] How it is asked
> "How many two-wheelers are sold in India each year?" or "How many trucks are there?"

> [!tip] Strong answer includes
> - Stock ÷ life as a method, then a SIAM check
> - Dispatch vs registration distinction
> - Segment mix and the FY it refers to
> - Admission that goods-vehicle counts need MoRTH data

---
## 5. Railways and Freight Corridors
> 🔴 Tier 1 · _Key points:_ loading in tonnes; tonne-km; average lead; DFC length

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Freight loading | **1,418.1 MT** (FY23); **1,512 MT** (latest listed, labelled 2023) | FY23 / 2023 | [Wikipedia: Rail transport in India](https://en.wikipedia.org/wiki/Rail_transport_in_India) | M |
| Freight tonne-km | **719,762 million** | 2021 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/IS.RRS.GOOD.MT.K6?format=json&per_page=10&mrv=6) | H |
| Loading (older) | **1,233 MT** | 2021 | Wikipedia (same) | M |
| Route length | **68,584 km** | 2023 | same | M |
| Freight wagons | **318,196** | listed | same | M |
| Dedicated freight corridors operational | **2,741 km** | March 2025 | same | M |

Concept: **lead distance** = tonne-km ÷ tonnes. Rail's strength is long-haul bulk (coal, ore, cement, containers); trucks win on short and time-critical movements.

### Example
**Average rail lead.** 719,762 million tonne-km ÷ 1,233 million tonnes (both 2021) = **584 km** per tonne. **Growth**: 1,512 ÷ 1,418.1 = **+6.6%** (the article labels the 1,512 figure "2023", most likely FY2023-24; confirm before quoting). If a candidate divides the 2021 tonne-km by the 1,512 MT figure the lead becomes 476 km, which is wrong because the years differ: that is the "never mix years" rule from sub-topic 1.

### In the news
See news box. Cement (453 MT in FY25) and steel (54.19 MT in four months) are large rail-eligible bulk flows; coal remains the biggest.

### Interview angle
> [!question] How it is asked
> "What share of freight moves by rail and how can it be raised?"

> [!tip] Strong answer includes
> - Tonnes and tonne-km, with average lead
> - DFC length and why it matters
> - First-mile and last-mile gaps limiting modal shift
> - Year discipline in ratios

---
## 6. Ports, Containers and Shipping
> 🔴 Tier 1 · _Key points:_ cargo tonnes, TEU, tonnes per TEU, concentration at Mundra and JNPA

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Major ports cargo | **about 855 MT** (819 MT FY24, +4.3%) | FY25 | [IBEF ports](https://www.ibef.org/industry/ports-india-shipping) | M |
| Container traffic, all India | **23.9 million TEU** (22.2M in 2023; 19.7M in 2022) | 2024 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/IS.SHP.GOOD.TU?format=json&per_page=10&mrv=6) | H |
| JNPA container volume | **5,835,650 TEU**; container cargo 78.05 MT | FY2023-24 | [Wikipedia: JNPT](https://en.wikipedia.org/wiki/Jawaharlal_Nehru_Port) | M |
| Mundra cargo | about **155 MT** (2022-23); 24 berths; about 33% of India's container traffic | 2022-23 | [Wikipedia: Mundra Port](https://en.wikipedia.org/wiki/Mundra_Port) | M/L |
| Port counts | 14 major ports (2024); 217 non-major, 68 cargo-handling | 2024 | [Wikipedia: Ports in India](https://en.wikipedia.org/wiki/Ports_in_India) | M |
| Share of trade | about 95% by volume, 70% by value | n/a | same | L |

**Conversion**: JNPA FY24: 78.05 MT ÷ 5,835,650 TEU = **13.4 tonnes per TEU**. A 40 ft box is 2 TEU, so about 27 tonnes of cargo per 40 ft container at that ratio. Network context: [[014 Global SCM & Sustainability]], [[126 International Trade Documentation, Customs & Trade Finance]].

### Example
**Container cargo and growth.** 23.9M TEU × 13.4 t = **320 MT** of containerised cargo. Growth 2023 to 2024 = 23.898 ÷ 22.208 − 1 = **+7.6%**; 2019 to 2024 CAGR = (23.898 ÷ 17.488)^(1/5) − 1 = **6.4%** a year. At 6.4% a year India would pass 30 million TEU in 2028 (23.9 × 1.064⁴ = 30.6). **Concentration**: Mundra's share of 33% of 23.9M TEU is about 7.9M TEU (the older Mundra figure was 5.65M in 2020-21, so the 33% share implies strong growth or a different year; treat as L).

### In the news
See news box. Major ports at about 855 MT (FY25) and the 23.9M TEU container figure are the two checked anchors.

### Interview angle
> [!question] How it is asked
> "How many containers does India handle?" or "How would you size port capacity?"

> [!tip] Strong answer includes
> - TEU and tonnes with the conversion factor
> - Major vs non-major ports and concentration
> - Growth rate and projection method
> - Hinterland connectivity (rail, DFC) as the bottleneck

---
## 7. Warehousing, Cold Chain and E-commerce
> 🔴 Tier 1 · _Key points:_ lowest-confidence block; use derived ranges; say what you could not verify

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| E-commerce GMV | **US$147.3 billion** | 2024 | [Wikipedia: E-commerce in India](https://en.wikipedia.org/wiki/E-commerce_in_India) | L |
| Online shoppers | **312.5 million** | 2022 | same | L |
| E-commerce share of urban FMCG | **6%** urban, 14% all metros, 18% top 8 metros; quick commerce over 75% of e-commerce FMCG | Oct-Dec 2025 | [NIQ](https://nielseniq.com/global/en/news-center/2026/niq-gst-2-0-transition-reshapes-indias-fmcg-growth-landscape/) | M |
| Kirana stores | **13 million**; 450,000 FMCG distributors | Oct 2025 | [Storyboard18](https://www.storyboard18.com/how-it-works/agentic-shopping-could-hit-13-million-kirana-stores-warns-retail-body-aicpdf-82164.htm) | M |
| Food processing market | **₹30.5 lakh crore** (US$354.5 billion) | 2024 | [IBEF](https://www.ibef.org/industry/food-processing) | M |
| Cold storage capacity | roughly 37-40 MT in about 8,000-9,000 units (potato dominant) | recalled | NHB/NCCD (not fetched) | L |
| Warehousing stock | no verified figure fetched; broker reports vary widely | n/a | n/a | n/a |

Operating detail: [[010 Warehouse Management]], [[127 Warehouse Engineering - Racking, Sizing & Material Handling]], [[129 E-commerce & Quick-Commerce Fulfilment]], [[133 Food, Agri & Perishables Supply Chain - India]].

### Example
**Orders per day, derived.** GMV US$147.3B × ₹84 = **₹12.4 lakh crore**. Orders at AOV ₹1,500 = ₹12.4 lakh crore ÷ ₹1,500 = **8.25 billion a year = 22.6 million a day**; at ₹1,000 AOV 33.9M; at ₹2,000 16.9M. Say "roughly 17-34 million orders a day, centred near 23 million, derived from a market estimate". Note the GMV estimate includes categories (travel, services) in some definitions, so goods orders are lower. Compare: UPI handled about 66 crore transactions a day in 2025 (see [[103 Key India Data Points to Memorize]]), so even 23 million orders a day is about 3.5% of UPI's count.

### In the news
See news box. NIQ's channel shares and the AICPDF's kirana count (13 million) are the only items in this block that were read directly from fresh sources; everything else here is labelled L.

### Interview angle
> [!question] How it is asked
> "How many e-commerce orders are placed in India per day?"

> [!tip] Strong answer includes
> - A derived range from GMV and AOV, not a memorised number
> - GMV vs revenue and category scope
> - Cross-check with a payments or logistics count
> - Honesty about low-confidence anchors

---
## 8. GST, Tax and Trade
> 🔴 Tier 1 · _Key points:_ gross vs net GST; FY26 totals; GST 2.0 slabs; export and import values

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Gross GST collection | **₹22.27 lakh crore (+8.3%)** | FY2025-26 | [Business Standard](https://www.business-standard.com/topic/gst-collection) | M |
| Net GST collection | **₹19.34 lakh crore (+7.1%)** | FY2025-26 | same | M |
| H1 FY27 | gross **₹12.46 lakh crore (+11.6%)**; net ₹10.66 lakh crore (+10.4%) | Apr-Sep 2026 | same | M |
| Monthly | Sept 2026 gross **₹2.04 trillion (+14.7%)**; July 2026 ₹2.11 trillion | 2026 | same | M |
| Rate slabs | **5%, 18%, 40%** (12% and 28% removed) from 22 September 2025 | 2025 | [Wikipedia: GST](https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)) | M |
| Total exports (goods and services) | **₹70,36,425 crore (US$825 billion)** | FY25 | [IBEF](https://www.ibef.org/economy/indian-economy-overview) | M |
| Merchandise exports | **US$445.3 billion** | 2025 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/TX.VAL.MRCH.CD.WT?format=json&per_page=10&mrv=4) | H |

Notes: gross vs net differ by refunds; whether cess is included changes comparisons (see the example). Supply-chain relevance of GST (input credit, e-way bills, place of supply) is in [[227 GST & Indirect Tax for Supply Chains]].

### Example
**GST as a share of GDP.** FY26 gross GST ₹22.27 lakh crore ÷ FY25 GDP ₹331.03 lakh crore = **6.7%** (using adjacent years; FY26 GDP would lower it slightly). Net: 19.34 ÷ 331.03 = 5.8%. **Base check**: ₹22.27 ÷ 1.083 = ₹20.56 lakh crore implied for FY25, which is lower than the ₹22.08 lakh crore commonly quoted for FY25 gross including cess (recalled, L), so the FY26 series probably excludes cess or follows a different definition; confirm on the GST Council or PIB release before quoting growth. **Run rate**: H1 FY27 of ₹12.46 lakh crore annualises to ₹24.9 lakh crore.

### In the news
See news box. The GST 2.0 reform (announced 3 September 2025, effective 22 September 2025) was expected to cost about ₹930 billion in revenue offset by about ₹450 billion from the 40% slab (Wikipedia); FY26 gross growth of 8.3% and H1 FY27 growth of 11.6% show collections holding up.

### Interview angle
> [!question] How it is asked
> "How much GST does India collect, and how is it split?"

> [!tip] Strong answer includes
> - Gross vs net and the year
> - Recent growth and the effect of rate changes
> - GST as a share of GDP for a plausibility check
> - Awareness that definitions (cess, IGST on imports) change comparisons

---
## 9. Manufacturing and Core Industries
> 🔴 Tier 1 · _Key points:_ manufacturing share of GDP (definition matters); auto, steel, cement; PLI

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Manufacturing value added | **13.47% of GDP** (World Bank); 17.0% of GVA (Wikipedia/MoSPI basis) | 2025 / FY24 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/NV.IND.MANF.ZS?format=json&per_page=10&mrv=6) | H/M |
| MVA history (World Bank) | 14.12% (2020), 14.38% (2021), 13.33% (2022), 13.31% (2023), 13.14% (2024) | | same | H |
| Crude steel | **54.19 MT** in April-July 2025; goal 300 MT capacity by 2030 | FY26 (4 months) | [IBEF steel](https://www.ibef.org/industry/steel) | M |
| Cement | **453 MT** production, **668 MT** capacity | FY25 | [IBEF cement](https://www.ibef.org/industry/cement-india) | M |
| Vehicle production | **3,10,34,174** | FY25 | [SIAM](https://www.siam.in/pressrelease-details.aspx?mpgid=48&pgidtrail=50&pid=579) | H |
| PLI | **₹21,534 crore** disbursed across 12 sectors; ₹1.76 lakh crore PLI-linked investment | 2025 | [IBEF manufacturing](https://www.ibef.org/industry/manufacturing-sector-india) | M |
| Manufacturing FDI | **₹14,45,781 crore** (US$165.1 billion) | 2025 | same | M |

Context for operations roles: [[006 Manufacturing Systems]], [[131 Automotive Supply Chain - JIT, Tiers & EVs]], [[134 Electronics & Semiconductor Supply Chain]].

### Example
**Cement utilisation and per-capita use.** 453 ÷ 668 = **67.8% utilisation**; per capita = 453 × 10⁹ kg ÷ 1.4639 × 10⁹ = **310 kg a person**. **Steel annualised**: 54.19 MT × 3 = 162.6 MT (a simple run-rate; seasonal and not an official forecast), about **111 kg a person** if all crude output were consumed, an upper bound. **Manufacturing GDP**: 13.47% × US$3.956 trillion = **US$533 billion**, vs 17.0% × a GVA of about US$3.6 trillion (assumed 91% of GDP) = US$612 billion: the gap is about 15% and comes from the definition and price basis, a point to state in an interview.

### In the news
See news box. Cement capacity of 668 MT against 453 MT output and a planned 150-160 MT of additions mean spare capacity in the near term; steel's 300 MT goal needs a very large capex programme ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]).

### Interview angle
> [!question] How it is asked
> "What is the share of manufacturing in India's GDP, and what is the 'Make in India' target?"

> [!tip] Strong answer includes
> - Two definitions (World Bank vs national accounts) and the numbers
> - Utilisation and per-capita ratios for cement and steel
> - PLI and FDI as policy levers
> - Auto, electronics and capital goods as growth segments

---
## 10. Power and Energy
> 🔴 Tier 1 · _Key points:_ capacity, peak, generation, per capita; fleet utilisation

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| Installed capacity | **532.7 GW** | March 2026 | [Wikipedia: Electricity sector in India](https://en.wikipedia.org/wiki/Electricity_sector_in_India) | M |
| Peak demand met | **270.82 GW** (21 May 2026) | May 2026 | same | M |
| Generation | **1,840 TWh** (29% non-fossil; coal 1,280.7 TWh, about 70%) | FY26 | same | M |
| Consumption | **1,694 billion units** (1 BU = 1 TWh) | FY25 | [IBEF power](https://www.ibef.org/industry/power-sector-india) | M |
| Solar | **157.05 GW** (AC) | May 2026 | [Wikipedia: Solar power in India](https://en.wikipedia.org/wiki/Solar_power_in_India) | M |
| Per-capita consumption | **1,181.6 kWh** | 2023 | [World Bank API](https://api.worldbank.org/v2/country/IND/indicator/EG.USE.ELEC.KH.PC?format=json&per_page=10&mrv=6) | H |
| World Bank per-capita series | 970.8 (2018), 988.3 (2019), 901.4 (2020), 963.4 (2021), 1,085.3 (2022) | | same | H |

Application: [[018 Capacity Management & OEE]] for plant utilisation logic; [[222 Infrastructure, Energy, Healthcare & Public-Sector Guesstimates]] for demand estimates.

### Example
**Fleet utilisation.** 1,840 TWh ÷ (532.7 GW × 8.76 TWh per GW) = **39.4%**. **Average load** = 1,840 ÷ 8.76 = **210 GW**; peak-to-average = 270.82 ÷ 210 = **1.29**. **Per capita**: FY25 consumption 1,694 × 10⁹ kWh ÷ 1.4639 × 10⁹ = **1,157 kWh**, within 2% of the World Bank's 1,182 kWh for 2023 (different years and definitions, but consistent). **Solar energy**: 1 GW at 17% CUF = 8.76 × 0.17 = **1.49 TWh a year**; 157 GW of solar would give about 234 TWh if all were at that CUF, about 13% of FY26 generation (an upper-end reading, because new capacity was added during the year).

### In the news
See news box. A record 270.82 GW peak at 532.7 GW installed shows how much capacity sits idle outside peak hours.

### Interview angle
> [!question] How it is asked
> "What is India's installed power capacity and per-capita consumption?"

> [!tip] Strong answer includes
> - Capacity vs peak vs energy and the conversion (GW to TWh)
> - Utilisation and the role of renewables' low CUF
> - Per-capita comparison and year
> - Implications for industry cost and captive power

---
## 11. Consumer, Telecom and Digital Reference Points
> 🔴 Tier 1 · _Key points:_ FMCG growth, telecom base, UPI, internet users

### Definition
| Metric | Value | Year | Source | Conf. |
|---|---|---|---|---|
| FMCG value growth | **7.8%**; volume rural 2.9%, urban 2.3% | Oct-Dec 2025 | [NIQ](https://nielseniq.com/global/en/news-center/2026/niq-gst-2-0-transition-reshapes-indias-fmcg-growth-landscape/) | M |
| Wireless subscribers | **1,312.25 million**; mobile 1,293.43M; active 1,207.59M (93.36%); tele-density 91.69% | Aug 2026 | [TelecomTalk](https://telecomtalk.info/india-wireless-telecom-subscriber-base-130billion-august2026/1012285/) | M |
| Jio | 508.43M wireless subscribers (39.31% share); Airtel 491.60M (38.01%); Vodafone Idea 199.57M | Aug 2026 | same | M |
| Jio ARPU | **₹215.6 a month** | Q1 FY27 | [TelecomTalk](https://telecomtalk.info/jio-adds-million-subscribers-q1fy27-arpu-rs215/1009790/) | M |
| UPI | **24,161.69 crore transactions; ₹314 lakh crore**; peak month March 2026 | FY2025-26 | [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=2) | H |
| Internet users | **886 million** (488M rural) | 2024 | [Indian Startup News](https://indianstartupnews.com/news/indias-internet-users-to-surpass-90-crores-in-2025-says-iamai-kantar-report-8627977) | M |
| Kirana | **13 million** stores | Oct 2025 | [Storyboard18](https://www.storyboard18.com/how-it-works/agentic-shopping-could-hit-13-million-kirana-stores-warns-retail-body-aicpdf-82164.htm) | M |

### Example
**Ratios from these points.** UPI average ticket = ₹314 lakh crore ÷ 24,161.69 crore = **₹1,300**. Active share = 1,207.59 ÷ 1,312.25 = **92%** of the wireless base reported as active (the page states 93.36% with its own base). Jio's share of wireless subscribers: 508.43 ÷ 1,312.25 = 38.7% (page: 39.31% on a slightly different base). Telecom revenue pool = 1,207.59M × ₹215.6 × 12 = **₹3.1 lakh crore** (Jio ARPU applied to all active users; a rough upper bound because other operators' ARPUs differ). Kirana per distributor = 13,000,000 ÷ 450,000 = **29 stores**.

### In the news
See news box. NIQ's GST-driven findings (60% of FMCG products with rate revisions) show the importance of dated price assumptions in consumer estimates.

### Interview angle
> [!question] How it is asked
> "How many mobile subscribers and UPI transactions are there in India?"

> [!tip] Strong answer includes
> - Latest figure with month and year
> - Active vs total subscriber definitions
> - Average ticket and ARPU as cross-checks
> - Which numbers are rounded for speaking and which are exact

---
## 12. ⭐ Advanced: Conversion Ratios and Derived Constants
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Ratios that save time and reveal errors (all derived from the sourced rows above; check the year before using):

| Ratio | Value | How derived |
|---|---|---|
| 1 lakh crore | $10^{12}$ rupees | 1 crore = $10^7$, 1 lakh = $10^5$ |
| 1 billion units (BU) | 1 TWh = $10^9$ kWh | definition |
| 1 GW for a year at 100% | 8.76 TWh | 1 GW × 8,760 h |
| Solar GW to TWh at 17% CUF | 1.49 TWh per GW | 8.76 × 0.17 |
| Fleet utilisation (FY26) | 39.4% | 1,840 ÷ (532.7 × 8.76) |
| Peak-to-average load | 1.29 | 270.82 ÷ 210 |
| Tonnes per TEU | 13.4 | 78.05 MT ÷ 5,835,650 TEU (JNPA FY24) |
| Average rail lead | 584 km | 719,762M tonne-km ÷ 1,233 MT (2021) |
| Cement per capita | 310 kg | 453 MT ÷ 1.46B |
| Cement utilisation | 67.8% | 453 ÷ 668 |
| UPI average ticket | ₹1,300 | ₹314 lakh crore ÷ 24,161.69 crore |
| Kirana per FMCG distributor | 29 | 13M ÷ 450,000 |
| Implied exchange rate (FY25) | ₹87.6 per US$ | ₹331.03 lakh crore ÷ US$3.78T |
| Households | about 300M | 1.46B ÷ 4.5 |
| Two-wheeler share of vehicle sales | 76.6% | 19.6M ÷ 25.6M |

Also useful: a 40 ft container = 2 TEU; a typical truck payload is 10-25 tonnes depending on class (assumption for goods vehicles); one pallet is about 1.2 m × 1.0 m; 1 GW × 1 year = 8.76 TWh.

### Example
**Chain several constants.** How much cargo is in a year of container traffic? 23.9M TEU × 13.4 t = **320 MT**. How many 25-tonne truckloads is that? 320M ÷ 25 = **12.8 million loads a year, 35,000 a day**. How much rail would it take at an average lead of 584 km? 320M t × 584 km = **187 billion tonne-km**, which is about **26%** of the 719,762 million tonne-km railways carried in 2021 (mixed years; indicative only). Each step uses a sourced ratio and each can be verified.

### In the news
See news box. GST, power and SIAM releases are monthly, so ratios built from them can be refreshed quickly; rebuild the table once a quarter.

### Interview angle
> [!question] How it is asked
> Implicit: speed and accuracy of conversions inside an estimate.

> [!tip] Strong answer includes
> - Conversions done aloud with units
> - Ratios that double as sanity checks
> - Year matching for numerators and denominators
> - A habit of showing the check, not only the answer

---
## 13. ⭐ Advanced: Reconciling Conflicting Sources and Maintaining the Sheet
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Sources disagree for four reasons: **definition** (scope, cess included or not), **period** (fiscal vs calendar year), **price basis** (current vs constant prices) and **vintage** (revised later). Method: list the conflicting figures, name the reason, choose one for the interview and state the other as a range.

| Item | Source A | Source B | Reason | What to say |
|---|---|---|---|---|
| Nominal GDP in dollars | US$3.78T FY25 (IBEF) | US$3.956T 2025 (World Bank); US$4.15T FY26 (Wikipedia) | Different year, exchange rate and vintage | "About US$3.8-4.2 trillion" |
| Manufacturing share | 13.47% of GDP (World Bank, 2025) | 17.0% of GVA (FY24) | Definition and price basis | "13-17% depending on the measure" |
| National highways | 146,204 km (IBEF FY25) | 161,350 km (Wikipedia 2024) | Dates and inclusion of state-transferred roads | "About 1.5 lakh km" |
| FY25 gross GST | ₹22.08 lakh crore incl. cess (recalled) | ₹20.56 lakh crore implied by FY26 growth | Cess treatment | "Gross GST is about ₹22 lakh crore" |
| GDP per capita | US$2,702 (World Bank 2025) | US$2,813 (Wikipedia FY26) | Year and vintage | "About US$2,700-2,800" |

### Example
**Resolve the manufacturing share question.** World Bank: manufacturing value added 13.47% of GDP (2025). National accounts view: 17.0% of GVA (FY24). Reconcile: GVA at basic prices is below GDP at market prices (taxes less subsidies are added to reach GDP), so the same manufacturing output is a smaller share of GDP; price basis (constant vs current) also differs. Interview line: "Manufacturing is roughly 13-17% of the economy depending on measure; the policy target of 25% of GDP is not yet near." (The 25% target is a widely cited National Manufacturing Policy goal, recalled; check.)

**Maintenance plan** (10 minutes a month): update GST (1st), SIAM (mid-month), TRAI (late month), power peak (as it happens); quarterly: NIQ, WGC, GDP. Keep columns: *metric, spoken value, exact value, year, source link, confidence*.

### In the news
See news box. Five different dated figures for India's GDP in the sources above are themselves a "news" item: new vintages arrive every quarter.

### Interview angle
> [!question] How it is asked
> "Two sources give different numbers; which do you use?"

> [!tip] Strong answer includes
> - Named reasons for the difference (definition, period, basis, vintage)
> - A single working number and a stated range
> - Preference for the official primary source when available
> - A refresh routine and a confidence tag
