---
tags: [guesstimates, tier2]
area: Guesstimates
topic: "Infrastructure, Energy, Healthcare & Public-Sector Guesstimates"
tier: Tier 2
roles: Consulting
status: complete
subtopics: 11
---
# Infrastructure, Energy, Healthcare & Public-Sector Guesstimates

⬅ [[221 Retail, FMCG & Consumer Guesstimates - Practice Set]] · [[_Index - Guesstimates|Guesstimates]] · [[223 Logistics, Manufacturing & Industry Data Points - India]] ➡

> **Area:** Guesstimates · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting

## Sub-topics in this note
1. [[#1. The Capacity-Planning Toolkit and a Power-Demand Warm-Up]]
2. [[#2. Rooftop Solar Potential]]
3. [[#3. LPG and Fuel Retail]]
4. [[#4. EV Charging Stations Needed]]
5. [[#5. Hospital Beds, Primary Health Centres and Ambulances]]
6. [[#6. Cold Storage Capacity]]
7. [[#7. Metro Ridership and City Water]]
8. [[#8. Ports Throughput and Truck Fleets]]
9. [[#9. Warehouse Area for E-commerce]]
10. [[#10. ⭐ Advanced: Checking Estimates Against Public Data]]
11. [[#11. ⭐ Advanced: From Capacity Estimate to Investment Case]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): public numbers to check infrastructure estimates against
> **Power: record peak and a bigger fleet (FY2025-26).** India's utilities had about **532.7 GW** of installed generation capacity in March 2026, met a record peak demand of **270.82 GW on 21 May 2026** during a heatwave, and generated **1,840 TWh in FY2025-26**, of which 29% came from non-fossil sources and about 70% from coal (1,280.7 TWh). ([Wikipedia: Electricity sector in India](https://en.wikipedia.org/wiki/Electricity_sector_in_India))
>
> **Solar keeps climbing.** Installed solar capacity was **157.05 GW (AC) in May 2026**, against 107.9 GW at 31 March 2025; the 100 GW mark was crossed on 31 January 2025. Grid-connected rooftop solar was **11,870 MW at 31 March 2024**, with a realisable rooftop potential of **57-76 GW**. ([Wikipedia: Solar power in India](https://en.wikipedia.org/wiki/Solar_power_in_India))
>
> **LPG reaches almost every household.** Total LPG connections stood at **328.9 million in 2025**, including **103.3 million** under the Ujjwala scheme (PMUY); PMUY households refilled **3.8 times** in 2023-24, up from 3.01 in 2019-20. ([Wikipedia: PMUY](https://en.wikipedia.org/wiki/Pradhan_Mantri_Ujjwala_Yojana))
>
> **Delhi Metro scale.** Average daily ridership **64.6 lakh (2025)**, a record **78.6 lakh on 18 November 2024**, a network of **374.47 km with 271 stations** and 2,055 coaches. ([Wikipedia: Delhi Metro](https://en.wikipedia.org/wiki/Delhi_Metro))
>
> **Ports and health capacity.** Major ports handled about **855 million tonnes in FY25** (819 MT in FY24, +4.3%) ([IBEF](https://www.ibef.org/industry/ports-india-shipping)); India's container port traffic was **23.9 million TEU in 2024** ([World Bank API](https://api.worldbank.org/v2/country/IND/indicator/IS.SHP.GOOD.TU?format=json&per_page=10&mrv=6)); hospital beds were **1.59 per 1,000 people in 2021**, down from 1.72 in 2014 ([World Bank API](https://api.worldbank.org/v2/country/IND/indicator/SH.MED.BEDS.ZS?format=json&per_page=10&mrv=8)), and physicians **0.72 per 1,000 in 2020** ([World Bank API](https://api.worldbank.org/v2/country/IND/indicator/SH.MED.PHYS.ZS?format=json&per_page=10&mrv=6)).
>
> Sub-topics that say **"See news box"** reuse these items. Numbers marked "assumption" are interview estimates; numbers marked "recalled" were not re-fetched and must be checked before you quote them. Checked October 2026.

---
## 1. The Capacity-Planning Toolkit and a Power-Demand Warm-Up
> 🟠 Tier 2 · _Key points:_ units ÷ capacity per unit ÷ utilisation; peak vs average; norms; always check against a public number

### Definition
Infrastructure questions ask "how many X do we need?" The core model is

$$N=\frac{D_{peak}}{c\times u}$$

where $D_{peak}$ is the demand in the busiest period, $c$ the capacity of one unit, and $u$ the achievable utilisation. Four habits make it work:
1. **Size for peak, not average**: $D_{peak}=D_{avg}\times PF$, where the **peak factor** $PF=1/\text{load factor}$ (about 1.3-1.4 for electricity).
2. **Use norms** where they exist (beds per 1,000, litres per capita per day, ambulances per lakh): they give a second route to the same number.
3. **Separate stock from flow** (cold storage tonnes vs tonnes processed a year).
4. **Check against public data and say so**: name the figure you would compare with and its source. Method background: [[102 Guesstimate Framework]], [[104 Classic Guesstimate Types & Templates]], [[105 Operations & SCM Guesstimates]]; India anchors: [[103 Key India Data Points to Memorize]] and [[223 Logistics, Manufacturing & Industry Data Points - India]].

### Example
**G1. India's peak electricity demand.**
- **Structure**: annual energy ÷ 8,760 hours = average load; ÷ load factor = peak.
- **Assumptions**: FY2025 consumption 1,694 billion units (IBEF; 1 billion units = 1 TWh); load factor 0.75.
- **Calculation**: average load = 1,694 × 10⁹ kWh ÷ 8,760 h = **193.4 GW**; peak = 193.4 ÷ 0.75 = **258 GW**.
- **Check against public data**: the record peak was **270.82 GW** on 21 May 2026 (news box), 5% above the estimate, which is reasonable because demand grew in the intervening year. FY26 generation of 1,840 TWh implies an average of 210 GW, so the actual peak-to-average ratio is 270.82 ÷ 210 = **1.29** (load factor 0.78).
- **Follow-up**: firm capacity needed with a 15% reserve margin = 270.82 × 1.15 = **311 GW**, against 532.7 GW installed; the fleet's average utilisation is 1,840 ÷ (532.7 × 8.76) = **39%**, because solar and wind run at about 17-30% and thermal plants are not dispatched all year. That gap is why storage and flexible demand are planning topics.

### In the news
See news box. The 270.82 GW peak in May 2026 and 532.7 GW of installed capacity are the two public numbers used above.

### Interview angle
> [!question] How it is asked
> "Estimate India's peak power demand" or "How much generation capacity does India need?"

> [!tip] Strong answer includes
> - Energy to average to peak via load factor
> - Reserve margin and the difference between installed and firm capacity
> - A public benchmark (record peak) for the sanity check
> - The reason utilisation is far below 100%

---
## 2. Rooftop Solar Potential
> 🟠 Tier 2 · _Key points:_ suitable roofs × kW per roof; yield per kW; compare with policy potential

### Definition
Rooftop potential is built from **segments**: residential, commercial and industrial (C&I). For each: (buildings with suitable, shade-free, owned roof) × (kW per roof). Energy follows $E=P\times 8{,}760\times CUF$; a typical Indian rooftop CUF is about 16-17% (about 1,450 kWh per kW per year). A usable rule is about 10 m² of roof per kW. Payback = system cost ÷ annual bill savings.

### Example
**G2. Rooftop solar potential in India.**
- **Structure**: (households × suitable share × kW) + C&I capacity.
- **Assumptions**: 300M households; 12% have an owned, suitable roof (independent houses, not flats or shared roofs); 2 kW average; C&I 30 GW (assumption).
- **Calculation**: residential = 300M × 0.12 × 2 kW = **72 GW**; total = 72 + 30 = **102 GW**. Energy = 102 GW × 1,450 kWh/kW = **148 TWh a year**, **8.0%** of FY26 generation (1,840 TWh). Roof area = 102 GW × 10⁶ kW/GW × 10 m² = **1,020 km²**.
- **Check against public data**: the Wikipedia article cites a realisable rooftop potential of **57-76 GW**, so the estimate is 1.3-1.8× the published range; installed rooftop was **11.87 GW** (March 2024), only **12%** of the estimate. Lower the suitable share to 7% and the total becomes 42 + 30 = 72 GW, inside the published band.
- **Follow-up (household economics)**: a 3 kW system at ₹60,000 per kW (assumption) costs ₹1.8 lakh; it generates 3 × 1,450 = 4,350 kWh, saving 4,350 × ₹7 = **₹30,450 a year** (tariff ₹7 per unit, assumption), a payback of **5.9 years**. With a central subsidy of ₹78,000 (the PM Surya Ghar structure for 3 kW, recalled; check the current scheme), net cost is ₹1.02 lakh and payback **3.3 years**.

### In the news
See news box. India's solar fleet of 157.05 GW is mostly utility-scale; the 11.87 GW of rooftop (March 2024) shows how much of the 57-76 GW potential was still untapped.

### Interview angle
> [!question] How it is asked
> "How much rooftop solar can India install?" or "Would a household find a rooftop system worthwhile?"

> [!tip] Strong answer includes
> - Segmented build (residential, C&I) with suitability filters
> - Energy yield per kW and the share of national generation
> - A comparison with published potential and installed capacity
> - Payback with and without subsidy; see [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]] for the NPV view

---
## 3. LPG and Fuel Retail
> 🟠 Tier 2 · _Key points:_ connections × refills × 14.2 kg; pump throughput × margin per litre

### Definition
Household energy is **connections × refills a year × cylinder size**. Fuel retail is **throughput per outlet × price** for turnover and **throughput × dealer commission** for the dealer's income. Cross-check national totals: number of outlets × average throughput should land near national consumption of petrol and diesel.

### Example
**G3. LPG cylinders delivered per day.**
- **Structure**: PMUY and non-PMUY connections × refills per connection ÷ 365.
- **Assumptions**: 103.3M PMUY connections at 3.8 refills (2023-24, from the news box); the other 225.6M (328.9 − 103.3) at 7 refills (assumption); cylinder 14.2 kg; retail price ₹900 (assumption, check the current price).
- **Calculation**: weighted refills = (103.3 × 3.8 + 225.6 × 7) ÷ 328.9 = **6.0 a year**; cylinders = 328.9M × 6.0 = **1.97 billion a year = 5.4 million a day**; weight = 1.97B × 14.2 kg = **28 million tonnes**; value = 1.97B × ₹900 = **₹1.77 lakh crore**.
- **Check against public data**: total LPG consumption is reported at around 30 million tonnes or more a year including commercial and industrial use (recalled; check PPAC), so 28 MT for domestic cylinders is plausible. Sensitivity: non-PMUY refills of 6 give 24.8 MT; 8 give 31.2 MT.
- **Follow-up**: a delivery person completes about 40 cylinders a day, so the system needs 5.4M ÷ 40 ≈ **135,000 delivery staff**.

**G4. Revenue and income of one petrol pump.**
- **Structure**: litres a day × price; dealer income = litres × commission.
- **Assumptions**: 150 kilolitres a month (petrol plus diesel, an average pump); average price ₹95 a litre; dealer commission ₹3.5 a litre (assumption; commissions differ by fuel and are revised periodically).
- **Calculation**: 150,000 L ÷ 30 = **5,000 L a day**, about 417 vehicles at 12 L each; turnover = 150,000 × ₹95 = **₹1.425 crore a month**; commission = 150,000 × 3.5 = **₹5.25 lakh a month, ₹63 lakh a year**, before staff, power and rent.
- **Check against public data**: 90,000 pumps (recalled; Wikipedia gives 60,799 petrol stations as of November 2017) × 150 kL × 12 months = 162 million kL, about **121 million tonnes** at 0.75 t/kL, against national petrol and diesel consumption of about 130 MT (recalled; verify with PPAC). A close match; true pumps vary from 50 kL in villages to 500+ kL on highways.
- **Follow-up**: if EVs and efficiency cut a pump's volume by 10%, commission falls by ₹6.3 lakh a year; non-fuel income (convenience store, air, EV charging) is the hedge, a theme in [[130 FMCG & Retail Distribution - India Route-to-Market]].

### In the news
See news box. LPG connections of 328.9 million against about 300 million households put coverage above one connection per household on paper (multiple connections and non-household users), so growth now comes mainly from refills, not new connections (analytical reading).

### Interview angle
> [!question] How it is asked
> "How many LPG cylinders are used per day?" or "How much does a petrol pump earn?"

> [!tip] Strong answer includes
> - Segmenting by refill behaviour (subsidised vs other households)
> - Converting units to tonnes and ₹ for a national cross-check
> - Pump economics: throughput × commission, then fixed costs
> - A transition risk (EVs) and a mitigation (non-fuel retail)

---
## 4. EV Charging Stations Needed
> 🟠 Tier 2 · _Key points:_ EV stock × public-charging share ÷ vehicles per charger; AC vs DC mix; highway spacing

### Definition
Charger counts use a **vehicles-per-public-charger** ratio, which depends on how much charging happens at home. Energy check: public kWh per day ÷ charger throughput. Highway networks use **spacing**: stations per km × two directions. Two-wheelers and three-wheelers mostly charge at home or via swapping, so public-charger counts are dominated by cars, buses and fleets.

### Example
**G5. Public chargers for electric cars by FY2030.**
- **Structure**: EV car stock ÷ EVs per public charger.
- **Assumptions**: passenger vehicle sales of 4.4, 4.6, 4.8, 5.0, 5.2 million in FY26-FY30 (starting near the 4.3 million FY25 domestic sales reported by SIAM); EV share 3%, 5%, 8%, 11.5%, 15%; existing stock 0.2M; 15 EVs per public charger (assumption; many cars charge at home).
- **Calculation**: EV sales = 0.132 + 0.230 + 0.384 + 0.575 + 0.780 = **2.10 million**; stock = **2.3 million**; chargers = 2.3M ÷ 15 = **153,000** (range 92,000 at 25 EVs per charger to 230,000 at 10).
- **Energy check**: if 30% of charging is public at 12 kWh per car a day, public energy = 2.3M × 0.3 × 12 = **8.3 million kWh a day**; spread over 153,000 chargers that is 54 kWh per charger per day, typical of slower AC points. Fast chargers (60 kW) delivering 250 kWh a day would number **33,000**.

**G6. Chargers along national highways.**
- **Structure**: highway length ÷ spacing × two sides × chargers per station.
- **Assumptions**: national highways 146,204 km (IBEF, FY25); one station every 25 km on each side; four DC chargers a station.
- **Calculation**: stations = 146,204 ÷ 25 × 2 = **11,700**; chargers = 11,700 × 4 = **46,800**.
- **Check**: highway chargers (47,000) are about 30% of the 153,000 total, reasonable for a car stock where intercity use is a minority. Compare with the public charger count (about 25,000-30,000 in early 2025, recalled from Ministry of Power/BEE statements; verify), which means a five- to six-fold build-out in five years.
- **Follow-up**: see sub-topic 11 for the economics of one DC charger.

### In the news
See news box. SIAM's FY25 domestic passenger vehicle sales of 43,01,848 units (a record) are the base on which the EV share assumption is applied ([SIAM](https://www.siam.in/pressrelease-details.aspx?mpgid=48&pgidtrail=50&pid=579)); a Delhi EV policy running from July 2026 offers two-wheeler incentives of up to ₹30,000 in its first year, according to a [Business Standard](https://www.business-standard.com/topic/electric-vehicles) page checked in October 2026.

### Interview angle
> [!question] How it is asked
> "How many EV charging stations does India need by 2030?"

> [!tip] Strong answer includes
> - EV stock projection from sales and share, not a single number
> - Home vs public charging and AC vs DC mix
> - Highway spacing as a second route
> - A utilisation and economics follow-up

---
## 5. Hospital Beds, Primary Health Centres and Ambulances
> 🟠 Tier 2 · _Key points:_ admissions × stay ÷ occupancy; population norms for PHC and CHC; call-volume route for ambulances

### Definition
**Beds**: $\text{Beds}=\dfrac{\text{admissions per year}\times \text{average length of stay}}{365\times\text{occupancy}}$. **Facilities by norm**: population ÷ catchment per facility (the Indian Public Health Standards recommend about one sub-centre per 5,000 people, one primary health centre (PHC) per 30,000 and one community health centre (CHC) per 1,20,000 in plain areas; recalled, check the current IPHS). **Ambulances**: either the norm (about one per lakh population, recalled) or a demand route: calls ÷ (trips per ambulance × utilisation).

### Example
**G7. Hospital beds in India and in a district.**
- **National (norm route)**: beds = 1.46B × 1.59 per 1,000 = **2.32 million** (WHO figure for 2021 via World Bank, news box). A commonly cited benchmark of 3 per 1,000 would need 4.4 million, a gap of **2.06 million beds**.
- **District of 20 lakh (flow route)**: admissions 6% a year = 1.2 lakh; stay 5 days; occupancy 75%: beds = 1,20,000 × 5 ÷ (365 × 0.75) = **2,192**, or 1.1 per 1,000.
- **Check**: 1.1 is 69% of the national 1.59 per 1,000; districts depend on referral flows to nearby cities, and the national figure includes private tertiary beds, so the district ratio is lower; use 8.7% admissions to match 1.59.
- **Follow-up**: physicians at 0.72 per 1,000 (2020) means 1.05 million doctors for 1.46B people; at one doctor per 10 beds in a hospital, the 2.32M beds need only 0.23M hospital doctors, so doctor supply is not the only constraint.

**G8. Primary health facilities needed.**
- **Calculation by norm**: PHCs = 1.46B ÷ 30,000 = **48,700**; CHCs = 1.46B ÷ 1,20,000 = **12,200**; sub-centres = 1.46B ÷ 5,000 = **292,000** (hill and tribal areas use smaller norms, so these are lower bounds).
- **Check**: compare with the latest Rural Health Statistics (not fetched here); say you would look up the shortfall by state.

**G9. Ambulances needed.**
- **Norm route**: 1.46B ÷ 1 lakh = **14,600**.
- **Demand route**: 1% of people need an ambulance a year = 14.6M calls = 40,000 a day; each ambulance does 6 trips a day at 50% utilisation = 3 effective trips → 40,000 ÷ 3 = **13,300**.
- **Check**: the two routes agree within 10%. Wikipedia mentions about 18,000 ambulances under the National Rural Health Mission (undated), so the estimate is the same order; urban density, response time targets and advanced life-support units would raise the count.

### In the news
See news box. Beds per 1,000 fell from 1.72 (2014) to 1.59 (2021) while population grew, so the bed gap widened; PM-JAY targets cover 100 million families (about 500 million people) with ₹5 lakh a year, which raises demand for beds in empanelled hospitals.

### Interview angle
> [!question] How it is asked
> "How many hospital beds or ambulances does India need?" or "Size the market for a hospital chain in a Tier 2 city."

> [!tip] Strong answer includes
> - Flow route (admissions × stay ÷ occupancy) and norm route
> - Public vs private and urban vs rural splits
> - Per-1,000 benchmark and the gap
> - Operational constraints (staff, response time) beyond counts

---
## 6. Cold Storage Capacity
> 🟠 Tier 2 · _Key points:_ crop output × share stored × storage cycle ÷ fill factor; potato dominates

### Definition
Cold storage is a **stock** capacity (tonnes held at one time). Demand = (output of each perishable crop) × (share that is stored) ÷ (fill factor). Seasonal crops that are stored for months (potato, apples) fill a store once a year, while multi-commodity stores can turn more than once. Value chain context: [[133 Food, Agri & Perishables Supply Chain - India]].

### Example
**G10. Cold storage capacity India needs.**
- **Structure**: potatoes stored + other perishables stored, ÷ fill factor.
- **Assumptions**: potato output 60 million tonnes (recalled; check NHB); 60% stored; other horticulture produce 290 million tonnes (recalled total of about 350 minus potatoes), of which 3% is cold-stored; fill factor 90%.
- **Calculation**: potato = 36 MT; others = 0.03 × 290 = 8.7 MT; total = 44.7 MT; capacity = 44.7 ÷ 0.9 = **49.7 MT**.
- **Check against public data**: published capacity is in the range of **37-40 MT** held in about **8,000-9,000 cold storages** (recalled from NHB and NCCD sources; Low confidence, not verified here); at 37.5 MT that is an average of 37.5M ÷ 8,333 = 4,500 tonnes a store. The estimate is 1.3× the recalled capacity, which hints that the stored share is lower than assumed (many farmers sell at harvest) or that stores run more than one cycle.
- **Follow-up**: a 5,000-tonne store serves 5,000 ÷ (25 tonnes per hectare, assumption) ≈ **200 hectares** of potato, a catchment of a few villages: location near production clusters, not consumption centres, is the key design choice.

### In the news
See news box. IBEF's food-processing page values the processing industry at about ₹30.5 lakh crore (2024) and notes PLI support of ₹10,900 crore ([IBEF](https://www.ibef.org/industry/food-processing)), but it carries no cold-storage statistic; no verified cold storage count was found for this note, so use the figures above as recalled anchors.

### Interview angle
> [!question] How it is asked
> "How much cold storage does India need?" or "Where should a cold-chain company build?"

> [!tip] Strong answer includes
> - Stock vs flow and fill factor
> - Crop-wise stored share, with potato as the anchor
> - Public benchmark and a reason for any gap
> - Siting by production cluster and power reliability

---
## 7. Metro Ridership and City Water
> 🟠 Tier 2 · _Key points:_ catchment × trip rate × mode share; per-capita norm for water; non-revenue losses

### Definition
**Metro**: riders a day = people within walking distance of stations × trips per person × share using the metro. Benchmarks are riders per km of line per day. **Water**: demand = population × litres per capita per day (lpcd); supply must also cover **non-revenue water** (leakage and theft), so $\text{Supply}=\dfrac{\text{Demand}}{1-\text{losses}}$. The urban norm of 135 lpcd is a commonly used planning figure (recalled, check the latest CPHEEO guideline).

### Example
**G11. Ridership of a new 30 km metro line.**
- **Structure**: catchment population × trips × metro share.
- **Assumptions**: 800 m each side of the line (1.6 km wide) = 48 km²; density 12,000 people per km²; 2 trips a day per person; metro share 15%.
- **Calculation**: catchment = 48 × 12,000 = 576,000; riders = 576,000 × 2 × 0.15 = **172,800 a day**, or **5,760 per km**.
- **Check against public data**: Delhi Metro's 64.6 lakh average ÷ 374.47 km = **17,250 riders per km a day**, so the new line is one-third of Delhi's network density, typical of a first line in a smaller city. Delhi's record day (78.6 lakh) is 1.22× its average, a peak-day factor for capacity design. Peak-hour load (10% of daily, half each way) = 8,640 per direction, within the 36,000 an hour per direction that 24 trains of 1,500 passengers can carry.
- **Follow-up**: at an average fare of ₹30, revenue = 172,800 × ₹30 × 365 = **₹189 crore a year**, which will not cover the capital cost of a 30 km line alone: fares, real-estate monetisation and subsidy matter.

**G12. Water demand of a city of 1 crore.**
- **Calculation**: demand = 1 crore × 135 lpcd = **1,350 million litres a day (MLD)**; with 30% non-revenue water, supply needed = 1,350 ÷ 0.7 = **1,929 MLD**.
- **Check**: if 10% of demand is met by tankers of 12,000 litres, tanker trips = 1.0 crore × 135 × 0.1 ÷ 12,000 = **11,250 trips a day**.
- **Follow-up**: cutting losses from 30% to 20% reduces supply need to 1,688 MLD, freeing **241 MLD**, which is cheaper than a new source.

### In the news
See news box. Delhi Metro's 235 crore annual trips (2025) and record 78.6 lakh day show a mature network's scale; use its 17,250 riders per km a day as the upper benchmark for any new-city estimate.

### Interview angle
> [!question] How it is asked
> "Estimate daily ridership of a new metro line in Pune" or "How much water does Bengaluru need?"

> [!tip] Strong answer includes
> - Catchment, trip rate and mode share, with a benchmark per km
> - Peak-day and peak-hour factors for capacity
> - Per-capita norm and system losses for utilities
> - Funding gap: fare revenue vs capital cost

---
## 8. Ports Throughput and Truck Fleets
> 🟠 Tier 2 · _Key points:_ berth throughput; TEU to tonnes; cement tonnes to trucks

### Definition
Port capacity is **berths × throughput per berth** with an occupancy limit (about 65-70% to keep queues short). **Conversion**: JNPA's FY24 figures give 78.05 million tonnes of container cargo on 5,835,650 TEU, so **1 TEU ≈ 13.4 tonnes** of cargo. Trucking fleet size = trips a day × days per round trip ÷ availability. Data points are tabulated in [[223 Logistics, Manufacturing & Industry Data Points - India]]; operating context is in [[125 Transportation Management Deep Dive]] and [[009 Logistics & Distribution]].

### Example
**G13. Port throughput and container berths.**
- **Berth throughput**: Mundra handled about 155 million tonnes in 2022-23 across 24 berths (Wikipedia): 155 ÷ 24 = **6.5 million tonnes per berth a year, about 17,700 tonnes a day**.
- **Container berths**: India's 23.9M TEU (2024) × 13.4 t = **320 million tonnes** of container cargo. If a container berth handles 1.0M TEU a year at 70% occupancy, India needs 23.9 ÷ (1.0 × 0.7) = **34 container berths** (assumption on berth capacity).
- **Check**: JNPA's 5.84M TEU was about 24% of the national 23.9M (different years, FY24 vs 2024); the major ports' 855 MT (FY25) includes bulk cargo and excludes non-major ports such as Mundra, so it is not directly comparable with the 320 MT of container cargo; no verified all-ports total was fetched.
- **Follow-up**: a 10% growth in TEU needs 3.4 more berths, or higher productivity (moves per hour) on the existing 34, the trade-off in [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

**G14. Trucks needed to move India's cement.**
- **Structure**: tonnes by road ÷ payload × trip time ÷ availability.
- **Assumptions**: production 453 MT (FY25, IBEF); 60% moves by road; payload 25 tonnes; average lead 300 km, so a 600 km round trip at 250 km a day takes 2.4 days; fleet availability 80%.
- **Calculation**: road tonnes = 271.8 MT; trips = 271.8M ÷ 25 = **10.9 million a year (29,800 a day)**; trucks in motion = 29,800 × 2.4 = **71,500**; with 80% availability = **89,400 trucks**.
- **Check**: a few per cent of the country's goods-vehicle fleet (recalled order of magnitude: a few million trucks; verify with MoRTH or Vahan); cement's share of freight is one dependable bulk flow, so rail share matters for the cost per tonne-km.
- **Follow-up**: moving 10% of road tonnes to rail takes 8,940 trucks off the road in the model (10% of 89,400), the tangible gain behind rail-share policy.

### In the news
See news box. Major ports handled about 855 MT in FY25 (+4.3%) and India's container traffic reached 23.9M TEU in 2024; both numbers anchor throughput guesstimates. Cement production of about 453 MT in FY25 comes from [IBEF cement](https://www.ibef.org/industry/cement-india).

### Interview angle
> [!question] How it is asked
> "How many trucks does India's cement industry need?" or "How many container berths does India need?"

> [!tip] Strong answer includes
> - Throughput per berth with an occupancy ceiling
> - TEU-to-tonne conversion and a bulk vs container split
> - Truck fleet from trips, round-trip time and availability
> - A modal-shift follow-up (road to rail or coastal)

---
## 9. Warehouse Area for E-commerce
> 🟠 Tier 2 · _Key points:_ orders a day ÷ orders per fulfilment centre; inventory route as a second method

### Definition
Fulfilment space is sized by **throughput** (orders a day ÷ orders per centre × area per centre) or by **stock** (units held × days of inventory ÷ units per sq ft). Always say what the area includes: fulfilment centres only, or also sortation hubs, dark stores and seller warehouses. Detail on racking, density and productivity is in [[127 Warehouse Engineering - Racking, Sizing & Material Handling]], [[010 Warehouse Management]] and [[129 E-commerce & Quick-Commerce Fulfilment]].

### Example
**G15. Fulfilment floor space for Indian e-commerce.**
- **Structure**: GMV → orders → fulfilment centres → area; cross-check by inventory.
- **Assumptions**: online retail GMV about US$147.3 billion in 2024 (Wikipedia citing market estimates; Low confidence); ₹84 per dollar (assumption); average order value ₹1,500; a 3 lakh sq ft centre handles 40,000 orders a day.
- **Calculation**: GMV = 147.3B × 84 = **₹12.4 lakh crore**; orders = ₹12.4 lakh crore ÷ ₹1,500 = **8.25 billion a year = 22.6 million a day**; centres = 22.6M ÷ 40,000 = **565**; area = 565 × 3 lakh = **170 million sq ft**.
- **Inventory route**: 1.5 units per order = 33.9M units a day; 30 days of stock = 1.02 billion units; at 10 units per sq ft of floor (multi-level shelving, aisles included) = **102 million sq ft**.
- **Check**: the two routes give 100-170 million sq ft; neither includes sortation, returns and dark stores, so total e-commerce-related warehousing is higher. Say that no verified leasing statistic was used here; compare with broker reports (not checked).
- **Follow-up**: sensitivity: if AOV is ₹1,000 orders rise 50% (to 33.9M a day) and area rises with them to 254M sq ft on route one; AOV is the largest swing input.

### In the news
See news box. NIQ reports that quick commerce is more than 75% of e-commerce FMCG sales and e-commerce is 18% of FMCG in the top eight metros ([NIQ](https://nielseniq.com/global/en/news-center/2026/niq-gst-2-0-transition-reshapes-indias-fmcg-growth-landscape/)), which shifts floor space from large fulfilment centres to small dark stores (see [[221 Retail, FMCG & Consumer Guesstimates - Practice Set]]).

### Interview angle
> [!question] How it is asked
> "How much warehouse space does Indian e-commerce need?"

> [!tip] Strong answer includes
> - Orders per day from GMV and AOV, then centres and area
> - A second route (inventory days and storage density)
> - Scope definition: fulfilment, sortation, dark stores
> - Sensitivity to AOV and orders per centre

---
## 10. ⭐ Advanced: Checking Estimates Against Public Data
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Interviewers reward candidates who say what they would verify. For each estimate write down the **public benchmark, its source, the year and the ratio** $r=\text{estimate}/\text{benchmark}$. Treat $0.7\le r\le 1.4$ as a pass, 0.5-2 as "explain", outside as "rebuild". Tag your confidence: **H** (official or regulator figure fetched), **M** (reputable secondary source), **L** (recalled or single estimate). See [[107 Common Mistakes & How to Avoid]].

### Example
Summary of this note's checks (everything marked "fetched" was read from the cited page in October 2026):

| Guesstimate | Estimate | Benchmark and source | Ratio | Confidence |
|---|---|---|---|---|
| Peak power (G1) | 258 GW | 270.82 GW record, May 2026 (Wikipedia, fetched) | 0.95 | M |
| Rooftop solar (G2) | 102 GW | 57-76 GW potential; 11.87 GW installed (Wikipedia, fetched) | 1.3-1.8 | M |
| LPG domestic (G3) | 28 MT | about 30 MT total LPG (recalled) | 0.93 | L |
| Petrol-diesel via pumps (G4) | 121 MT | about 130 MT (recalled) | 0.93 | L |
| Hospital beds (G7) | 2.32M | 1.59 per 1,000 (World Bank API, fetched) | by construction | H |
| Ambulances (G9) | 13,300-14,600 | about 18,000 under NRHM (Wikipedia, undated) | 0.7-0.8 | L |
| Metro per km (G11) | 5,760 | Delhi 17,250 per km (Wikipedia, fetched) | 0.33 | M |
| Container berths (G13) | 34 | none found | n/a | n/a |
| Cold storage (G10) | 49.7 MT | 37-40 MT (recalled) | 1.3 | L |
| E-commerce area (G15) | 100-170M sq ft | none verified | n/a | n/a |

Where the confidence is L, the answer in an interview is "I recall roughly X; I would verify with the source (PPAC, NHB, MoRTH)", which is honest and still shows structure.

### In the news
See news box. The shift of ministries and agencies to publishing monthly and quarterly data (TRAI, GST Council, CEA, SIAM) makes quick refreshes possible; keep a source column in your anchor sheet as in [[103 Key India Data Points to Memorize]].

### Interview angle
> [!question] How it is asked
> "How would you validate this number?"

> [!tip] Strong answer includes
> - Named benchmark, source and year
> - A ratio and the reasons for any gap
> - Confidence labels; no pretended precision
> - Which input you would refine first

---
## 11. ⭐ Advanced: From Capacity Estimate to Investment Case
> ⭐ Advanced · _Added beyond the tracker_

### Definition
After the number comes the decision: **what does one unit cost, what does it earn, and how much utilisation is needed?** Convert counts into capex = units × cost per unit, then test unit economics: contribution per unit × utilisation − fixed cost, payback, and NPV (see [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]] and [[109 Valuation Basics (NPV, IRR, DCF)]]). In consulting cases this is the bridge from market sizing to profitability ([[025 Case Interview — Profitability]]).

### Example
**One 60 kW DC fast charger (all inputs are assumptions).** Capex ₹20 lakh including grid connection; sells electricity at ₹18 per kWh and buys at ₹9, so margin is ₹9 per kWh; operating cost ₹1.5 lakh a year.
- At **250 kWh a day** (about 4 hours at 60 kW): margin = 250 × 365 × 9 = ₹8.21 lakh; net = ₹6.71 lakh; **payback 3.0 years**; 8-year pre-tax NPV at 12% = **+₹13.3 lakh**.
- At **125 kWh a day**: margin ₹4.11 lakh; net ₹2.61 lakh; **payback 7.7 years**; 8-year NPV = **−₹7.1 lakh**.
- **Break-even utilisation** for a 5-year payback: (₹20 lakh ÷ 5 + ₹1.5 lakh) ÷ (₹9 × 365) = **167 kWh a day**, about 2.8 hours a day at full power.
- Network view: building 33,000 DC chargers (from G5) at ₹20 lakh needs about **₹6,600 crore** of capex; if utilisation lags, it is the 125 kWh case that applies, and the NPV is negative, so the rollout depends on subsidies, EV growth and charging-time pricing.

### In the news
See news box. The record 270.82 GW peak and 157.05 GW of solar also affect charger economics: daytime solar surplus supports cheap daytime charging, while evening peak charging is costly.

### Interview angle
> [!question] How it is asked
> "You estimated the number of chargers; is it a good business?"

> [!tip] Strong answer includes
> - Capex = count × cost per unit; revenue per unit from utilisation
> - Break-even utilisation and payback
> - Sensitivity (utilisation, tariff spread) and risks
> - Policy levers: subsidy, tariff design and land access
