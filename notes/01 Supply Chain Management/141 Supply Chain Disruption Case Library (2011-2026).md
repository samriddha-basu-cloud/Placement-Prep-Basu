---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Supply Chain Disruption Case Library (2011-2026)"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 14
---
# Supply Chain Disruption Case Library (2011-2026)

⬅ [[140 Packaging, Unitisation & Load Optimisation]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[142 Company Supply Chain Case Library]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. How to Read a Disruption Case: The CIRL Template]]
2. [[#2. Tohoku Earthquake & Toyota (March 2011)]]
3. [[#3. Thailand Floods & Western Digital (October 2011)]]
4. [[#4. Rana Plaza (April 2013): Social Compliance as Supply Risk]]
5. [[#5. NotPetya & Maersk (June 2017) and Cyber-Driven Stoppages]]
6. [[#6. Hurricane Maria & Pharma (2017-2018): Sole-Site Risk]]
7. [[#7. COVID-19 and the 2020-23 Chip Shortage]]
8. [[#8. Ever Given and the Suez Blockage (March 2021)]]
9. [[#9. Texas Winter Storm Uri (February 2021)]]
10. [[#10. Red Sea and Panama: Chokepoint Crises (2023-2025)]]
11. [[#11. CrowdStrike (July 2024) and the Baltimore Bridge (March 2024)]]
12. [[#12. Tariff Shocks (2025) and the Nexperia Crisis (October 2025)]]
13. [[#13. Cross-Case Lessons: A Disruption Pattern Table]]
14. [[#14. ⭐ Advanced: Pricing Resilience with TTR, TTS and Break-Even Probability]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): chokepoints, tariffs and a 40 cent chip
> **Red Sea / Suez rerouting (analysed July 2024).** Maersk reports that rerouting around the Cape of Good Hope raised average cargo travel distance by **9%**, Suez crossings fell **66%** (the canal normally carries about **12% of global trade**), and available shipping capacity was **15–20% lower in Q2 2024** because ships were tied up on longer voyages. ([Maersk](https://www.maersk.com/insights/resilience/2024/07/09/effects-of-red-sea-shipping)) Egypt's Suez Canal revenue fell from **$9.4 billion (FY2022/23) to $7.2 billion (FY2023/24)**, about 23%, with transits down roughly 22%. ([Maritime Executive](https://maritime-executive.com/article/suez-canal-revenue-dropped-2b-last-year-due-to-red-sea-security-crisis))
>
> **Nexperia export halt (October–November 2025).** After the Dutch government took control of Nexperia in early October 2025, China blocked exports of Nexperia chips made in China. Nexperia holds roughly **40% of the market for automotive transistors and diodes**, and about **70%** of its Netherlands-made chips go to China for packaging and testing. Industry groups warned stocks would last "a matter of weeks"; China confirmed exemptions on **6 November 2025** after the Trump-Xi meeting. ([Automotive Logistics](https://www.automotivelogistics.media/supply-chain/china-confirms-exemptions-to-export-controls-following-trumpxi-meeting-allowing-flow-of-nexperia-chips-to-resume/2098912))
>
> **US tariff shock (2025–2026).** The 2 April 2025 "Liberation Day" tariffs lifted the estimated average US tariff rate from about **2.5% (January 2025) to about 27% at the April peak**, the highest in over a century; tariffs on Chinese goods briefly reached **145%** before a May rollback to 30% for 90 days. A Wikipedia summary of later events reports the US Supreme Court ruled on 20 February 2026 (6-3) that IEEPA tariffs exceeded presidential authority, with refunds of about $166 billion at stake: verify current status before quoting. ([Wikipedia: Tariffs in the second Trump administration](https://en.wikipedia.org/wiki/Tariffs_in_the_second_Trump_administration), checked October 2026)
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. How to Read a Disruption Case: The CIRL Template
> 🔴 Tier 1 · _Key points:_ Cause, impact, response, lesson; exposure map; time-to-recover

### Definition
Interviewers rarely want a story; they want a **structured read** of a disruption. Use the **CIRL template** (Cause, Impact, Response, Lesson) and add an **exposure map**:

| Step | Question | What good looks like |
|---|---|---|
| **C**ause | Trigger and *why it propagated* | Separates the trigger (flood, hack) from the vulnerability (single site, no buffer, no visibility) |
| **I**mpact | Who lost what, for how long | Numbers: output lost, revenue, days, price moves; distinguishes **delay** from **loss** |
| **R**esponse | What the firm did in hours, weeks, months | Short-term (triage, expedite), medium (re-source, re-route), long-term (redesign) |
| **L**esson | Transferable rule | One sentence, stated as a policy: "map to tier-2", "pre-qualify a second site" |
| **E**xposure map | Which nodes and flows in *this* chain look the same | Names the equivalent single point of failure in the interviewer's company |

Three diagnostic lenses explain almost every case in this library:
- **Concentration:** one site, one supplier, one canal, one port (Naka fab, Bang Pa-In estate, Suez).
- **Opacity:** the firm could not see tier-2/3 (Nexperia, Renesas). Linked to [[015 Supply Chain Risk & Resilience]].
- **Thin buffers:** lean flow with no slack (Toyota 2011, chip shortage). See [[007 Lean Manufacturing]] and [[117 Demand-Driven MRP (DDMRP) & Buffer Management]].

Two measures turn a story into analysis: **time-to-recover (TTR)**, how long a node takes to return to normal, and **time-to-survive (TTS)**, how long the chain can keep serving customers without that node (Simchi-Levi's framing). The danger zone is $TTR > TTS$.

$$\text{Exposure gap} = TTR - TTS \quad (\text{weeks of unserved demand})$$

### Example
Apply CIRL to **Ever Given (March 2021)** in one breath: *Cause:* 400 m ship grounded in a single-lane canal in 40+ knot winds. *Impact:* about six days of blocked traffic, 369 ships queued, a delay not a destruction of goods. *Response:* tugs and dredging, then Cape diversions. *Lesson:* a delay of days is absorbed by buffer stock; chains with zero buffer fail first. *Exposure map:* "Which of our lanes has no alternative route within 14 days?"

### In the news
See news box. Red Sea, Nexperia and tariffs are three fresh cases of the same lenses: concentration, opacity, thin buffers.

### Interview angle
> [!question] How it is asked
> "Walk me through a recent supply chain disruption and what the company should have done differently."

> [!tip] Strong answer includes
> - CIRL structure, delivered in 90 seconds with two or three hard numbers
> - Distinction between trigger and vulnerability
> - A transferable lesson, then a link to the interviewer's own chain (exposure map)
> - Admission of what is uncertain (estimates are estimates)

---
## 2. Tohoku Earthquake & Toyota (March 2011)
> 🔴 Tier 1 · _Key points:_ Tier-2 chip fab, 78% output fall, RESCUE-type mapping, buffer policy

### Definition
**Cause.** The 11 March 2011 Tohoku earthquake and tsunami damaged the Renesas Electronics **Naka** factory, which made about **20% of Renesas's microcontrollers and system-on-chip products** and nearly 10% of its analog and power devices. Five Renesas wafer fabs and three assembly sites were forced to halt at first. ([Renesas](https://www.renesas.com/en/about/newsroom/impact-march-11-tohoku-district-pacific-offshore-earthquake-renesas-electronics-operations-and-its)) Automakers had no visibility into who made which custom MCU; the chips were custom-qualified, so substitution took months.

**Impact.** Toyota's production fell **78% year on year in April 2011** (research cited by Supply Chain Dive). Toyota's own plants were largely intact; the problem was thousands of parts from tier-2/3 suppliers in the affected region.

**Response.** Toyota built a system to find, early in a crisis, which suppliers and parts are at risk across multiple tiers, set up **business continuity plans**, and now asks suppliers for **2 to 6 months of extra inventory on high-priority parts**; Toyota itself reportedly holds **1 to 4 months of semiconductors**. ([Supply Chain Dive](https://www.supplychaindive.com/news/toyota-semiconductor-shortage-earthquake-inventory-ihs-gartner-forecast-2022/600193/))

**Lesson.** Pure JIT is efficient only while the whole network is stable. The fix was **selective buffers for the 5–10% of parts that are single-source and long-to-requalify**, not abandoning TPS (see [[007 Lean Manufacturing]] and [[131 Automotive Supply Chain - JIT, Tiers & EVs]]).

### Example
A critical custom MCU costs ₹120 and goes into a ₹9 lakh car. A 4-month requalification means every car needs the chip; holding 3 extra months of MCUs for 20,000 cars a month costs 20,000 × 3 × ₹120 = ₹72 lakh of inventory. At 20% carrying cost that is about ₹14.4 lakh a year to protect roughly 60,000 cars (about ₹5,400 crore of vehicle revenue). The policy pays for itself if it avoids a one-in-fifteen-year event costing even a few days of output.

### In the news
Toyota later cited the 2011 lessons when it said it expected limited impact from the 2021 chip shortage, a rare case of a documented lesson paying off (Supply Chain Dive, above).

### Interview angle
> [!question] How it is asked
> "Toyota is the JIT benchmark, yet it stopped in 2011. Is JIT too risky?"

> [!tip] Strong answer includes
> - Cause was tier-2 opacity, not JIT itself
> - Selective buffers on single-source, long-requalification parts
> - Supplier mapping to tier-n and a pre-agreed recovery playbook
> - Quantified trade-off: cost of buffer vs expected disruption loss

---
## 3. Thailand Floods & Western Digital (October 2011)
> 🔴 Tier 1 · _Key points:_ Cluster concentration, 46-day restart, price spike, margin windfall

### Definition
**Cause.** Monsoon flooding in October 2011 inundated industrial estates north of Bangkok. Thailand produced about **40% of global hard disk drives**, and Western Digital (WD) made roughly **60% of its units there**, with about 37,000 workers at two large sites. The Bang Pa-In plant was under about 6 feet of water from 16 October 2011.

**Impact.** Gartner projected HDD shipments to fall by at least **10 million units** from the previous Q4 target of **180 million**. Q4 2011 HDD output fell about **29%**, and the average drive price rose about **30% (from $51 to $66)** in the UCLA teaching case. WD's shipments were 28.5 million units against 52.2 million a year earlier in the case data. (Sources: [StorageNewsletter](https://www.storagenewsletter.com/2011/10/18/thailand-floods-to-significant-impact-wd/); [UCLA Anderson teaching case](https://www.anderson.ucla.edu/documents/areas/fac/dotm/bio/V4EDITResilientResponseRecoveryWD.pdf))

**Response (WD).** Reopened the flooded plant in **46 days** (30 November 2011); kept about 38,000 employees on 75% pay; used divers to dismantle submerged machines and recovered about 80% of equipment; ramped Malaysian sites; ran a command centre with daily communication. By September 2012 WD was back at pre-flood capacity and #1 again.

**Lesson.** *Response and recovery capability* can matter more than prevention when a once-in-a-century event exceeds design limits. Industry-wide, gross margins rose from roughly 20% to about 30% post-flood and prices never fully reverted ([IEEE Spectrum](https://spectrum.ieee.org/the-lessons-of-thailands-flood)): a shortage shared by all rivals can *raise* profit for the firms that recover first.

### Example
Compute WD's fall: 28.5 / 52.2 = 0.546, so shipments were about **45% lower** than a year earlier. Industry output fell 29%, so WD lost share (to Seagate) before it recovered: a firm that is *more* concentrated than peers falls further than the market. A buyer such as a laptop OEM with 60% of drives from Thai plants faces a 29% shortfall on that slice; dual sourcing from non-Thai fabs (Samsung's operations were unaffected) caps the loss. See [[134 Electronics & Semiconductor Supply Chain]].

### In the news
See news box. Clustered, concentrated nodes (Nexperia's China packaging step) repeat the Thai pattern 14 years later.

### Interview angle
> [!question] How it is asked
> "Your key supplier is in a flood-prone industrial park. What do you do?"

> [!tip] Strong answer includes
> - Ask where the supplier's own tier-2 and sites are (cluster risk, not just single-supplier risk)
> - Options: second source in another geography, buffer, supplier BCP audit, contractual recovery clauses
> - Cost of each option vs expected loss
> - Notes the post-disaster pricing power of firms that recover first

---
## 4. Rana Plaza (April 2013): Social Compliance as Supply Risk
> 🔴 Tier 1 · _Key points:_ 1,134 deaths, Accord vs Alliance, tier-n visibility, brand liability

### Definition
**Cause.** On 24 April 2013 the nine-storey Rana Plaza building in Savar, near Dhaka, collapsed, killing **1,134 people**. It housed garment workshops supplying global brands, some sub-contracted without the brand's knowledge. Structural violations and ignored cracks were the root causes; the vulnerability was **sub-contracting beyond the buyer's visibility** and cost-only sourcing.

**Impact.** Beyond lives, brands faced consumer boycotts, regulatory and legal pressure, and a collapse of trust in "social audits".

**Response.** The legally binding **Accord on Fire and Building Safety** was signed on **15 May 2013** by over 200 brands and importers, two global unions and Bangladeshi unions; its engineers identified more than **150,000 safety hazards** and inspected over 2,000 factories. Gap and Walmart declined, citing US litigation risk, and formed the non-binding **Alliance** (about 700 factories; 93% remediation rate on exit in 2018). ([Wikipedia: Accord](https://en.wikipedia.org/wiki/Accord_on_Fire_and_Building_Safety_in_Bangladesh); [Al Jazeera, April 2023](https://www.aljazeera.com/news/2023/4/24/ten-years-of-rana-plaza-how-safe-is-bangladesh-garment-industry))

**Lesson.** Compliance risk is supply risk: an unsafe tier-2 factory can stop a brand's supply and wreck its reputation. Binding, transparent, jointly funded programmes outperformed voluntary audits. Ten years on, Bangladesh's garment exports grew about 79% from $19 billion (2015) to $34 billion (2022) and over 80% of the country's 3,200 factories are reported as internationally safety-compliant. See [[014 Global SCM & Sustainability]] and [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]].

### Example
A fashion retailer sources 40% of volume at a ₹300 FOB price from three Bangladeshi vendors. A 3% price premium for a remediation fund costs 0.03 × ₹300 = ₹9 per unit; for 5 million units that is ₹4.5 crore, against one boycott that can cost far more in lost sales and brand value. The decision rule: accept a premium when it is below the **expected reputation loss** and is set through a *shared*, enforceable mechanism, not a one-off audit.

### In the news
Tenth-anniversary coverage (2023) shows the same debate now playing out in the EU supply chain due-diligence directive and Indian BRSR value-chain disclosures.

### Interview angle
> [!question] How it is asked
> "A buyer discovers its supplier subcontracted work to an unsafe unit. What now?"

> [!tip] Strong answer includes
> - Immediate containment and traceability (who else uses this vendor)
> - Structural fix: audit rights, subcontracting ban or disclosure, binding corrective plans
> - Distinguishes audit theatre from verified remediation
> - Weighs cost of compliance vs reputational loss

---
## 5. NotPetya & Maersk (June 2017) and Cyber-Driven Stoppages
> 🔴 Tier 1 · _Key points:_ IT outage as supply outage, 10-day rebuild, $250-300m, supplier ransomware at Toyota

### Definition
**Cause.** The NotPetya malware, spread through a Ukrainian accounting software update in June 2017, wiped systems globally. A-P Moller-Maersk lost its IT estate.

**Impact.** Maersk reinstalled **45,000 PCs, 4,000 servers and 2,500 applications in about 10 days** and estimated damage of **$250–300 million**; chairman Jim Hagemann Snabe said recovery "would take six months. It took ten days." Operations ran on manual processes at about **80% of normal volume**. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/maersk-reinstalled-45-000-pcs-and-4-000-servers-to-recover-from-notpetya-attack/))

**Response.** Rebuild from the surviving copy, manual booking and paper process, daily crisis calls, and afterwards segmented networks, backups and a zero-trust approach.

**Second example: Toyota and Kojima Industries (1 March 2022).** A suspected cyberattack on plastics supplier Kojima halted **28 production lines at 14 Japanese plants**, about **13,000 vehicles or 5% of Toyota's monthly Japan output**, for roughly a day. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/toyota-halts-production-after-reported-cyberattack-on-supplier/))

**Lesson.** IT is a supply chain node; cyber resilience belongs in the BCP, and in supplier onboarding. JIT amplifies a one-supplier outage into a plant stop within hours. See [[016 Digital Supply Chain & Industry 4.0]] and [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]].

### Example
Maersk's cost works out to $250–300m / 10 days = **$25–30 million per outage day**. Recovery rate: 45,000 / 10 = 4,500 PCs and 4,000 / 10 = 400 servers per day. Compared with a 6-month (about 180-day) plan, the speed-up is 180 / 10 = 18 times. Any firm can use this arithmetic to size a cyber-recovery budget: if a day of outage costs ₹X crore, a one-week reduction in TTR is worth 7X.

### In the news
See news box. CrowdStrike (sub-topic 10) repeats the lesson for software dependencies.

### Interview angle
> [!question] How it is asked
> "How should a manufacturer think about cyber risk as a supply chain risk?"

> [!tip] Strong answer includes
> - IT/OT systems and tier-1 suppliers' IT as nodes in the map
> - Quantified daily outage cost, TTR targets, offline backups, manual fall-back process
> - Supplier cyber-posture in onboarding and tiering
> - Rehearsed drills, not just documents

---
## 6. Hurricane Maria & Pharma (2017-2018): Sole-Site Risk
> 🔴 Tier 1 · _Key points:_ Single Baxter site, IV saline shortage, FDA import relief

### Definition
**Cause.** Hurricane Maria hit Puerto Rico in September 2017. Around **8% of US medicines** are made there, and Baxter's Puerto Rico facilities were a major source of IV fluids. Hospital IV fluid supply had been tight since 2014, so there was no slack.

**Impact.** By October 2017 many plants ran at 70% capacity or less, some below 20%. The American Hospital Association warned only **10–15% of hospital demand** might be met at the peak of the shortage. ([BiopharmaDive](https://www.biopharmadive.com/news/fda-works-to-ease-iv-shortages-after-hurricane-maria/514927/))

**Response.** The FDA allowed temporary imports from Baxter facilities in Ireland, Australia, Mexico and Canada and from B. Braun (Germany), and approved Fresenius Kabi and Laboratorios Grifols saline products. ([FDA](https://www.fda.gov/drugs/drug-safety-and-availability/fda-works-help-relieve-iv-fluid-shortages-wake-hurricane-maria))

**Lesson.** In regulated products the bottleneck is **qualification**: a second site must be validated before disaster, because approval takes months. This is the mirror image of chip custom-qualification. Cross-reference [[132 Pharma & Healthcare Supply Chain]].

### Example
A hospital group uses 12,000 IV bags a week. Supplier A (single site) delivers 100%. After a 6-week outage with 15% of demand met, the unmet need is $12{,}000 \times 6 \times 0.85 = 61{,}200$ bags. Pre-qualifying supplier B at 20% of volume (A at 80%) would have raised coverage to 20% + 15% × 80% = **32%** during the outage: the unmet share falls from 85% to 68%. A bigger second-source share or pre-built stock is needed to close the gap. This motivates a **minimum second-source share** for critical, qualification-heavy items.

### In the news
Not tied to the news box; the structural issue (concentrated generic sterile injectables and APIs) is current in India's PLI and bulk-drug park policy; see [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

### Interview angle
> [!question] How it is asked
> "How would you reduce supply risk for a life-saving drug made at one site?"

> [!tip] Strong answer includes
> - Pre-qualified second site or CMO (the long pole)
> - Safety stock sized to TTR, expiry-aware
> - Regulator and hospital communication plan
> - Demand allocation rules in a shortage (clinical priority)

---
## 7. COVID-19 and the 2020-23 Chip Shortage
> 🔴 Tier 1 · _Key points:_ Bullwhip, order cancellations, $210bn auto loss, GSCPI

### Definition
**Cause.** Lockdowns cut capacity while demand shifted to electronics and goods. Automakers cancelled chip orders in early 2020, then demand returned faster than expected; chipmakers had reallocated capacity to consumer electronics. Aggravators: **Renesas fire (March 2021)**, a **February 2021 winter storm** that closed three Austin plants (Samsung, Infineon, NXP), Taiwan's drought and port congestion. ([Wikipedia: chip shortage](https://en.wikipedia.org/wiki/2020%E2%80%932023_global_chip_shortage))

**Impact.** AlixPartners raised its 2021 estimate on 23 September 2021 to **$210 billion in lost auto industry revenue and 7.7 million vehicles of lost production**, doubling its May estimate of $110 billion. ([AlixPartners](https://www.alixpartners.com/newsroom/press-release-shortages-related-to-semiconductors-to-cost-the-auto-industry-210-billion-in-revenues-this-year-says-new-alixpartners-forecast/)) India lost an estimated half a million vehicles to chips in 2021. The NY Fed's **Global Supply Chain Pressure Index (GSCPI)** hit its record high in December 2021 ([NY Fed](https://www.newyorkfed.org/research/policy/gscpi)).

**Response.** Automakers shifted to direct chipmaker contracts, long-term capacity agreements, stock builds and redesign; governments launched fab subsidies (US CHIPS Act, India Semiconductor Mission). See [[134 Electronics & Semiconductor Supply Chain]].

**Lesson.** A demand-signal failure ([[114 Bullwhip Effect, Beer Game & Information Sharing]]) plus single-source commodity inputs. Lean systems cut inventory to a level that could not absorb a 12-month supply shock.

### Example
$210bn / 7.7m vehicles = about **$27,300 revenue per lost vehicle**. If a Tier-1 supplier with ₹3,000 of content per vehicle loses 500,000 Indian vehicles, revenue at stake is 500,000 × ₹3,000 = ₹150 crore. The chip itself might cost ₹150 against a vehicle price of several lakh: **a part worth a tiny fraction of vehicle value gating 100% of vehicle revenue**, the basis of "criticality over cost" in [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]].

### In the news
GSCPI value 0.19 in May 2025 signalled renewed (mild) pressure per the Wikipedia supply-chain-crisis article, and the Nexperia event in news box showed that the chip risk had not gone away.

### Interview angle
> [!question] How it is asked
> "Why did the chip shortage hit auto more than electronics, and how would you prevent a repeat?"

> [!tip] Strong answer includes
> - Order-cancellation bullwhip; autos were low-priority in foundry queues
> - Direct visibility to tier-2/3, long-term capacity agreements, buffer for gating parts
> - Design flexibility (alternative chips, validated in advance)
> - Cost-of-criticality logic, not blanket stock

---
## 8. Ever Given and the Suez Blockage (March 2021)
> 🔴 Tier 1 · _Key points:_ 6 days, 369 ships, $9.6bn/day of trade, delay vs loss

### Definition
**Cause.** The 400 m, 20,000 TEU container ship **Ever Given** grounded on 23 March 2021 in winds above 40 knots and blocked the canal for **6 days 7 hours** (23 to 29 March). By 28 March at least **369 ships** were queued carrying about 16.9 million tonnes of cargo.

**Impact.** Lloyd's List estimated about **$9.6 billion of trade per day** was held up (about $5.1bn westbound, $4.5bn eastbound), a rough figure for *delayed* trade, not lost trade. The Suez Canal Authority lost about $15 million a day in fees and first demanded over $916 million, settling at **$540 million**. ([gCaptain](https://gcaptain.com/the-9-6-billion-a-day-price-of-a-suez-stuck-ship/); [Wikipedia](https://en.wikipedia.org/wiki/2021_Suez_Canal_obstruction))

**Response.** Tugs and dredgers freed the ship; some lines diverted via the Cape, adding up to about two weeks.

**Lesson.** A short outage at a chokepoint produced weeks of **schedule unreliability and port congestion**, since ships arrived bunched. Buffer stock absorbs a few days; thin chains felt it most. See [[125 Transportation Management Deep Dive]].

### Example
$9.6\text{bn} \times 6.29 \text{ days} \approx \$60$ billion of trade delayed. For an Indian importer with ₹10 crore of goods a day moving through Suez, a 6-day block with 14-day diversion adds pipeline inventory of ₹10 cr × 14 days = **₹140 crore** for those 14 days. At 15% annual carrying cost, that costs 140 × 0.15 × 14/365 = **₹0.8 crore**: the holding cost is small; **stock-out and demurrage** risk is the real exposure.

### In the news
See news box. The Red Sea crisis made the Suez "event" semi-permanent: rerouting became a structural cost.

### Interview angle
> [!question] How it is asked
> "Ever Given blocked Suez for six days. What does this mean for an importer of auto parts?"

> [!tip] Strong answer includes
> - Pipeline inventory = daily flow × extra days; quantifies the carrying cost
> - Delay vs loss; criticality of parts decides buffer
> - Mode switch options (air for critical parts), alternative routings
> - Notes that bunching creates a secondary congestion wave

---
## 9. Texas Winter Storm Uri (February 2021)
> 🔴 Tier 1 · _Key points:_ Utilities and petrochemicals, force majeure cascades, resin shortage

### Definition
**Cause.** Winter Storm Uri (14-20 February 2021) knocked out natural gas, wind and coal generation in Texas; **69% of Texans lost power** for an average of 42 hours. ([Texas Comptroller](https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-impact.php))

**Impact.** Federal Reserve Bank of Dallas estimates put losses at **$80 to $130 billion**; at least 210 deaths. In petrochemicals, about **80% of US olefins/polyolefins capacity** was knocked out; by 19 March only 60% of olefins had resumed. LyondellBasell estimated a **10–14% hit to annual US polyethylene output** and up to $450 million lower Q1 profit; Celanese, Covestro, BASF and others declared force majeure. Dow's CFO called it a "6-plus-month event" versus about 3 months for typical hurricanes. ([C&EN](https://cen.acs.org/business/petrochemicals/Texas-petrochemical-production-still-thawing/99/i11))

**Response.** Allocation by producers, spot imports, price rises; later weatherisation rules for Texas power and gas.

**Lesson.** **Hidden common-mode failure**: power, gas and resin plants depend on each other, so "different suppliers" can share one weather risk. Downstream, packaging, auto and appliance makers found resin shortages in mid-2021.

### Example
A packaging converter buys PE from three producers, all on the Gulf Coast. Each is "independent" but they share the same freeze. If all three lose 80% for 3 weeks and resume at 60% for 3 more, expected supply in the 6 weeks = $3 \times 0.2 + 3 \times 0.6 = 2.4$ weeks of nominal supply, so a **shortfall of 3.6 weeks**. With 2 weeks of resin stock the uncovered gap is **1.6 weeks**: sourcing in a second region (or imports) is worth more than adding a fourth Gulf supplier.

### In the news
Climate-related cold and heat events keep recurring (Panama drought is the same family: weather as a supply chain event; see sub-topic 10).

### Interview angle
> [!question] How it is asked
> "You have three suppliers, so you are covered. Are you?"

> [!tip] Strong answer includes
> - Common-mode risk: same region, same utility, same feedstock
> - Map shared dependencies (energy, water, port, tier-2)
> - Geographic diversification; contractual allocation priority
> - Stock sized to the regional recovery time

---
## 10. Red Sea and Panama: Chokepoint Crises (2023-2025)
> 🔴 Tier 1 · _Key points:_ Cape diversion, capacity loss, rates, Panama drought, structural vs transient

### Definition
**Red Sea.** Houthi attacks from late 2023 led carriers to avoid Suez. Suez passages fell to about **63%** of prior-year levels and Cape transits rose about **70%** by January 2024; insurance on cargo rose from about **0.6% to 2%** of value; container spot rates on key lanes more than doubled within weeks (Shanghai to Los Angeles from $1,985 to $3,860 per 40 ft between mid-December and 18 January) ([CSIS](https://www.csis.org/analysis/global-economic-consequences-attacks-red-sea-shipping-lanes)). Drewry modelled that if diversions lasted through 2024, effective global container capacity would fall by about **9%**, and the Shanghai to Rotterdam index was up **246%** since mid-December ([gCaptain/Drewry](https://gcaptain.com/suez-canal-diversions-drewry-assesses-impact-on-container-shipping/)). Singapore to Rotterdam via the Cape adds about **3,600 nautical miles**. For India, CSIS notes that about 80% of goods exports to Europe travel via Red Sea routes, representing about 15% of total Indian exports. Per Wikipedia, a ceasefire on 10 October 2025 gave limited recovery and attacks reportedly resumed on 28 March 2026: status should be checked before an interview.

**Panama Canal.** Drought left Gatun Lake at its lowest since at least 1965. Transits fell from a normal of **36-38 a day** to **24** (from 7 November 2023) and a low of **18** in February 2024, then recovered fully by August 2024. Container vessel transits dropped below 250 a month versus 300-330 pre-drought. ([project44](https://www.project44.com/supply-chain-insights/recovery-of-the-panama-canal/); [EIA](https://www.eia.gov/todayinenergy/detail.php?id=62408))

**Lesson.** Two chokepoints failed simultaneously for *different* reasons (security, climate), removing the fallback route of each other. Planning needs **route portfolios**, not a primary and an untested backup.

### Example
Cape diversion on a 35-day Asia-Europe voyage that adds 10 days (≈ +29% time). Pipeline inventory for ₹10 crore per day of flow rises by ₹100 crore; at 15% carrying cost, that is ₹15 crore a year. Safety stock also rises because voyage-time variability typically grows with transit time: if lead-time standard deviation $\sigma_L$ rises from 3 to 4.5 days (illustrative), $SS = z \cdot d \cdot \sigma_L$ with demand rate $d$ grows by 50%. See [[003 Inventory Management]] and [[009 Logistics & Distribution]].

Panama arithmetic: from 36 to 18 transits is a **50% cut**; 24 is a **33% cut**.

### In the news
See news box for Maersk's measured effects and Egypt's loss of about $2 billion in canal revenue.

### Interview angle
> [!question] How it is asked
> "A client ships electronics from China to Europe via Suez. How should they respond to the Red Sea crisis?"

> [!tip] Strong answer includes
> - Quantify: extra days, pipeline inventory, freight, insurance, service level
> - Options: Cape, rail (China-Europe), air for critical SKUs, nearshoring, safety stock, contract rate structure ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]])
> - Segmentation: critical vs non-critical SKUs
> - Scenario triggers for returning to Suez

---
## 11. CrowdStrike (July 2024) and the Baltimore Bridge (March 2024)
> 🔴 Tier 1 · _Key points:_ Software single point of failure, Delta $500m, port closure 11 weeks

### Definition
**CrowdStrike.** A faulty security-software update on 19 July 2024 crashed an estimated **8.5 million Windows devices** (Microsoft's figure). Delta Air Lines said the outage cost about **$500 million in five days**, with more than **5,000 cancelled flights**, and its crew-scheduling systems needed manual recovery including resetting about **40,000 servers**. ([NPR](https://www.npr.org/2024/07/31/nx-s1-5058652/delta-crowdstrike-outage-500-million-dollars)) Other airlines recovered in about a day; Delta's heavy reliance on affected tools, plus tightly coupled crew scheduling, extended the stoppage.

**Baltimore.** On **26 March 2024** the container ship Dali hit the Francis Scott Key Bridge; six construction workers died. The Fort McHenry channel fully reopened on **12 June 2024**, about **11 weeks** later. Baltimore is the nation's busiest port for autos, light trucks and other ro-ro cargo; cargo diverted to Virginia, Georgia and others, and the port expected volumes to recover by 2025. ([Supply Chain Dive](https://www.supplychaindive.com/news/port-of-baltimore-fort-mchenry-channel-reopening-future/718633/))

**Lesson.** Both are "unlikely but systemic" events that exposed **single points of failure with no tested fallback**: a monoculture of software, a single bridge channel. Resilience here is **optionality** (manual modes, alternate ports and IT diversity) and **recovery speed**.

### Example
Delta: $500m / 5 days = **$100 million per day**; at a recovery of 7 days instead of 5, loss ≈ $700m. Suppose (hypothetically) a $50m crew-system redundancy cut recovery time by 2 days, saving $200m per event: the break-even probability is 50 / 200 = 25% that such an event occurs during the investment's life. Rare-event economics like this is why boards underinvest and why [[015 Supply Chain Risk & Resilience]] stresses scenario analysis.

### In the news
Not in the shared news box; both are 2024 events and are cited here with their own sources.

### Interview angle
> [!question] How it is asked
> "What do the CrowdStrike outage and the Baltimore bridge teach about resilience investment?"

> [!tip] Strong answer includes
> - Single points of failure in non-physical systems too
> - Tested manual fall-back and failover, vendor diversity
> - Expected-loss math with TTR reduction, not just probability
> - Port alternatives and pre-agreed rerouting contracts with carriers

---
## 12. Tariff Shocks (2025) and the Nexperia Crisis (October 2025)
> 🔴 Tier 1 · _Key points:_ Policy risk, front-loading, China+1, export-control chokepoints

### Definition
**Tariffs.** Policy, not physics, was the trigger. Importers **front-loaded** goods ahead of deadlines, then faced stranded stock and sudden landed-cost swings; US tariffs on China reached **145%** before the May 2025 reduction to 30%, and the average effective US tariff rate peaked near 27% in April 2025 (Wikipedia, see news box). Responses: re-route through third countries (China+1), absorb or pass through cost, renegotiate contracts, and use bonded or free-trade-zone storage. India saw both an opportunity (China+1) and pressure on exports to the US once higher duties were applied. See [[126 International Trade Documentation, Customs & Trade Finance]].

**Nexperia.** The Dutch state took control of Nexperia in early October 2025; China then barred exports of its China-made chips. Nexperia's high-volume, low-price discrete chips (transistors and diodes, about **40% market share** in automotive, about **70%** of Dutch chips needing China for packaging) are in every car, and rivals' qualified substitutes are not quick to approve. Affected: VW, BMW, Mercedes, Stellantis, Renault, Volvo Cars, GM, Toyota, Ford and Hyundai in the list reported. Exemptions followed on **6 November 2025**. ([Automotive Logistics](https://www.automotivelogistics.media/supply-chain/china-confirms-exemptions-to-export-controls-following-trumpxi-meeting-allowing-flow-of-nexperia-chips-to-resume/2098912))

**Lesson.** Geopolitics is now a *supplier attribute*: ownership and jurisdiction of every tier matter. Cheap commodity parts can have the highest criticality-to-cost ratio. See [[134 Electronics & Semiconductor Supply Chain]] and [[227 GST & Indirect Tax for Supply Chains]] for the GST side of re-routed inbound flows.

### Example
An electronics importer buys an item at US$100 customs value. At a 30% duty the landed cost is $130; at 145% it is **$245** (+88%). If the buyer can re-source in 8 weeks at a 12% higher FOB ($112) from a country facing a 20% duty, landed cost is 112 × 1.2 = $134.4: a **third-country option is far better than paying 145%** and roughly equal to 30%. The decision therefore depends on the *expected duration* of the tariff regime: use **scenario weights**, e.g. 50% chance of staying at 30%, 20% at 145%, 30% at 10%: expected duty = 0.5×30 + 0.2×145 + 0.3×10 = **47%**.

### In the news
See news box. Tariff regime volatility (including litigation in 2026) shows why contracts need **tariff-adjustment clauses** and why firms keep dual-country capacity.

### Interview angle
> [!question] How it is asked
> "US tariffs on your client's product just jumped. What is your recommendation?"

> [!tip] Strong answer includes
> - Quantify landed-cost change; separate temporary vs structural
> - Options ladder: pass-through, renegotiate, re-source, tariff engineering, bonded warehousing
> - Scenario weighting and trigger points
> - Pre-existing buffers and cash cost of inventory held under uncertainty

---
## 13. Cross-Case Lessons: A Disruption Pattern Table
> 🔴 Tier 1 · _Key points:_ Eight patterns, mitigation levers, which case proves it

### Definition
| Pattern | Cases | Lever | Typical metric |
|---|---|---|---|
| **Cluster / single-site concentration** | Naka (Tohoku), Thai estates, Baxter PR, Nexperia | Second qualified site, geographic split | % volume with one site |
| **Tier-2/3 opacity** | Toyota 2011, chips 2021, Nexperia | Multi-tier mapping, supplier data sharing | % spend mapped to tier-2 |
| **Thin buffers (lean without slack)** | Toyota 2011, 2021 shortage, Kojima | Selective safety stock on gating parts | Days of cover, criticality |
| **Shared hidden dependency (common mode)** | Texas Uri, Red Sea + Panama | Region and utility diversity | Number of independent routes |
| **IT/software as node** | NotPetya, Kojima, CrowdStrike | Offline backups, drills, vendor diversity | TTR in hours |
| **Social and compliance risk** | Rana Plaza | Binding standards, traceability | Audit-to-remediation rate |
| **Policy and geopolitics** | Tariffs, Nexperia, Red Sea | Scenario planning, contract clauses | Landed cost range |
| **Demand-signal distortion** | Chip cancellations, COVID | Information sharing, visibility ([[114 Bullwhip Effect, Beer Game & Information Sharing]]) | Order variance ratio |

Crisis-response sequence common to successful responders: **detect (hours) → assess exposure by part (days) → allocate scarce supply by margin and customer priority → re-source and qualify (weeks) → redesign (months)**. The winners (WD, Toyota, Maersk) had a rehearsed command centre and pre-agreed authority, not new ideas.

### Example
Score a client's top five inputs on **criticality (1-5)**, **substitutability (1-5, 5 = hard)**, and **TTR vs TTS gap (weeks)**. A part scoring 5/5 with a 6-week gap gets a buffer or second source; a 2/2 part with no gap gets nothing. This ties to the Kraljic matrix in [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]] and to [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]].

### In the news
See news box. Each 2024-25 event maps to a row above: Red Sea (common mode, geopolitics), Nexperia (concentration, opacity, geopolitics), tariffs (policy).

### Interview angle
> [!question] How it is asked
> "What are the common lessons across supply chain disruptions of the last 15 years?"

> [!tip] Strong answer includes
> - Patterns rather than a list of stories
> - Selective, criticality-based resilience (not "stock everything")
> - Visibility plus rehearsed response
> - Cost-benefit logic; acknowledges that resilience competes with efficiency

---
## 14. ⭐ Advanced: Pricing Resilience with TTR, TTS and Break-Even Probability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Simchi-Levi's **time-to-recover (TTR)** and **time-to-survive (TTS)** analysis gives a defensible, quantitative way to decide where to spend. For each node $i$:

$$\text{Gap}_i = \max(0,\; TTR_i - TTS_i)$$

$$\text{Loss}_i = \text{Gap}_i \times \text{daily (or weekly) contribution lost}$$

A mitigation (buffer, second source, redundancy) costs $C$ per year and avoids loss with probability $p$ per year of the disruption. It pays when $p \times \text{Loss avoided} > C$, i.e. the **break-even probability** is

$$p^{*} = \frac{C}{\text{Loss avoided}}$$

Use $p^*$ as a discipline: compare it to a plausible annual frequency (e.g. once-in-20-years = 5%) and to cheaper alternatives (shorten TTR by pre-qualified suppliers, tooling duplication, contract options).

### Example
A component supports 10,000 units a week at a contribution of ₹2,000. A sole supplier takes 8 weeks to restore (TTR), and stock plus pipeline cover 5 weeks (TTS). Gap = 3 weeks, so

- Unserved units = 10,000 × 3 = 30,000
- Loss = 30,000 × ₹2,000 = **₹6 crore**
- Buffer to close the gap: 30,000 components × ₹300 = ₹90 lakh of stock
- Carrying cost at 20% = **₹18 lakh a year**
- $p^* = 18 \text{ lakh} / 6 \text{ crore} = 3\%$ per year

If the node's annual disruption probability is higher than 3% (say a flood-prone cluster at 5%), the buffer pays; at 1%, shorten TTR or accept. Compare cheaper options too: pre-qualifying a second source for part of the volume, or cutting TTR through tooling duplication, may beat holding stock. Linked: [[136 Supply Chain Finance & Working Capital]] for the cash tied in the buffer, and [[110 Cost Accounting for Operations]] for contribution margin.

### In the news
See news box. The Nexperia and tariff cases show the recurring problem: TTS of "a matter of weeks" against TTR of months.

### Interview angle
> [!question] How it is asked
> "How much should we spend on resilience, and where?"

> [!tip] Strong answer includes
> - TTR, TTS and gap per node; rank by loss
> - Break-even probability and sensitivity to event frequency
> - Distinguishes buffers, second sources and faster recovery, with costs
> - Notes that estimates are rough and updates with new mapping data
