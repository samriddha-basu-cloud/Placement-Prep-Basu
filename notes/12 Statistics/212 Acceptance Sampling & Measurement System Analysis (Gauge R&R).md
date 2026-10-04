---
tags: [statistics, tier2]
area: Statistics
topic: "Acceptance Sampling & Measurement System Analysis (Gauge R&R)"
tier: Tier 2
roles: Operations / Quality
status: complete
subtopics: 13
---
# Acceptance Sampling & Measurement System Analysis (Gauge R&R)

⬅ [[211 Reliability & Survival Analysis]] · [[_Index - Statistics|Statistics]] · [[213 Design of Experiments - Factorial, Fractional & Taguchi]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Quality

## Sub-topics in this note
1. [[#1. Acceptance Sampling Basics and Single Sampling Plans]]
2. [[#2. The OC Curve: Worked Construction]]
3. [[#3. AQL, LTPD, Producer's and Consumer's Risk, and Designing a Plan]]
4. [[#4. AOQ, AOQL and ATI (Rectifying Inspection)]]
5. [[#5. Double, Multiple and Sequential Sampling Plans]]
6. [[#6. ANSI/ASQ Z1.4 and ISO 2859-1: How to Read the Tables]]
7. [[#7. Skip-Lot, Continuous Sampling and Variables Plans]]
8. [[#8. MSA Components: Bias, Linearity, Stability, Repeatability, Reproducibility]]
9. [[#9. Gauge R&R: Average and Range Method (Worked)]]
10. [[#10. Gauge R&R: ANOVA Method, %Study Variation and %Contribution]]
11. [[#11. Attribute Agreement Analysis (Kappa)]]
12. [[#12. Calibration, MSA in Practice and Common Pitfalls]]
13. [[#13. ⭐ Advanced: The Economics of Inspection and the Deming kp Rule]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the lot-sampling standard has been reissued, and the MSA manual is still the 4th edition
> **ISO 2859-1 is replaced by a 2026 edition (status checked on the ISO catalogue page).** The ISO catalogue entry for ISO 2859-1:1999, "Sampling procedures for inspection by attributes, Part 1: sampling schemes indexed by acceptance quality limit (AQL) for lot-by-lot inspection", shows the second edition as **withdrawn as of 22 January 2026** and **superseded by ISO 2859-1:2026**. This is the international twin of ANSI/ASQ Z1.4 used by buyers in textiles, electronics and auto parts. If a customer contract still cites "ISO 2859-1:1999", confirm which edition applies before arguing over sample sizes. (This note's Z1.4 / ISO 2859-1 table readings are the long-standing scheme; check them against the edition your contract names.) ([ISO catalogue entry](https://www.iso.org/standard/1141.html))
>
> **AIAG MSA manual: the 4th edition remains the current offering.** AIAG's product page lists the MSA reference manual as the 4th edition, aimed at helping manufacturers assess measurement system quality, with no newer edition announced on the page (checked 2026). The 4th edition's Gauge R&R guidelines (below 10% acceptable, 10 to 30% conditional, above 30% unacceptable; at least 5 distinct categories) are widely used in automotive supplier audits. ([AIAG MSA page](https://www.aiag.org/training-and-resources/manuals/details/MSA-4))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Acceptance Sampling Basics and Single Sampling Plans
> 🟠 Tier 2 · _Key points:_ Lot-by-lot accept/reject on a sample; single plan (n, c); attributes vs variables; no quality is "built in"

### Definition
**Acceptance sampling** decides the fate of a **lot** (accept, reject or screen) by inspecting a random sample, instead of 100% inspection. It suits destructive tests, high volumes, incoming material and final release, and is the sibling of the control-chart tools in [[091 Statistical Quality Control (SQC)]] (the SQC note gives a short overview; this note builds the full theory). Key terms:
- **Single sampling plan $(N,n,c)$:** from a lot of size $N$ inspect $n$ units; **accept if defectives $d\le c$** (the acceptance number), otherwise reject. $r=c+1$ is the rejection number.
- **Attributes plans** count defectives or defects (pass/fail); **variables plans** measure a characteristic (using the sample mean and sd, ISO 3951 / ANSI Z1.9) and need smaller samples for the same protection but assume normality.
- **Disposition of rejected lots:** return to supplier, sort 100% (rectifying inspection), or rework.
- Randomness is essential: draw units from across the lot (all pallets/cartons), not the top layer.
- Binomial model for $d$ when lot is large relative to $n$ ($n/N<0.1$); **hypergeometric** for small lots; **Poisson** for defects per unit or rare defects. The probability tools are in [[088 Probability Distributions]].

Limitation (Deming): sampling only sorts lots; it does not improve the process, and a supplier with a stable, capable process is better governed by SPC and audit than by lot inspection (sub-topic 13).

### Example
An auto-component plant receives lots of $N=1{,}000$ rubber bushes and uses the plan $n=50,\ c=2$. Inspect 50 bushes; if 0, 1 or 2 are out of tolerance, accept the lot; if 3 or more, reject. Under the binomial model, a lot with 4% defective has $P(d\le2)=\mathbf{67.7\%}$ chance of acceptance. The hypergeometric check for a lot with exactly 10 defectives (1%) gives $P_a=0.989$ vs binomial 0.986 (Poisson 0.986), so the approximations agree.

### In the news
See news box. Because ISO 2859-1 and Z1.4 define the standard plans, a revision changes what a supplier and buyer treat as the default sample size and switching behaviour.

### Interview angle
> [!question] How it is asked
> "A supplier ships 5,000 units per lot. How would you decide how many to inspect and when to accept?"

> [!tip] Strong answer includes
> - Define the plan $(n,c)$ and the random sampling method
> - Choose the plan from AQL, risk levels, lot size, or the Z1.4 tables rather than "inspect 10%"
> - Mention the OC curve to show what the plan protects against
> - Say it complements supplier process control; link [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]

---
## 2. The OC Curve: Worked Construction
> 🟠 Tier 2 · _Key points:_ Pa vs p; Pa = P(d ≤ c); steeper with larger n; c shifts the curve; ideal curve is a step

### Definition
The **operating characteristic (OC) curve** plots **probability of acceptance** $P_a$ against lot fraction defective $p$. For a single plan with a binomial model:

$$P_a(p)=\sum_{d=0}^{c}\binom{n}{d}p^{d}(1-p)^{n-d}$$

Build it by evaluating $P_a$ at a grid of $p$ values. Reading it:
- High $P_a$ at good quality, low $P_a$ at bad quality: the **discrimination** of the plan.
- Increasing $n$ with $c$ fixed shifts the curve left and makes it steeper; increasing $c$ with $n$ fixed shifts it right; to keep the AQL point and sharpen discrimination raise both $n$ and $c$.
- Fixed percentage sampling (inspect 10% of every lot) is a bad idea: protection varies with lot size. Fixed $n$ gives the same protection for large lots.
- **Type A OC curve** (isolated lot, hypergeometric) vs **Type B** (continuing stream, binomial). Variables plans have their own OC curve in terms of the process mean/sd.

### Example
Plan $n=50,\ c=2$ (binomial):

| Lot fraction defective $p$ | 0.5% | 1% | 2% | 3% | 4% | 5% | 6% | 8% | 10% | 12% | 15% |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $P_a$ | 0.998 | 0.986 | 0.922 | 0.811 | 0.677 | 0.541 | 0.416 | 0.226 | 0.112 | 0.051 | 0.014 |

A lot at 1% defective is accepted 98.6% of the time (producer's risk $\alpha=1.4\%$); a lot at 8% defective is still accepted 22.6% of the time (consumer's risk $\beta=22.6\%$), so the plan is generous to the producer. The "indifference" quality (where $P_a\approx0.5$) is about 5%. Plotting these points gives the S-shaped curve; the same table in Python is `scipy.stats.binom.cdf(2, 50, p)`.

### In the news
See news box. Any plan drawn from the Z1.4/ISO 2859-1 tables has a published OC curve; buyers should read it, not just the AQL label.

### Interview angle
> [!question] How it is asked
> "Draw and explain the OC curve of a plan with n = 50 and c = 2. What happens if n doubles?"

> [!tip] Strong answer includes
> - $P_a$ vs $p$, formula via binomial; compute a few points
> - Doubling $n$ with the same $c$ makes the curve steeper and moves it left (stricter); to keep a similar AQL, raise $c$ as well
> - Producer's and consumer's risk read from the curve
> - Ideal curve and why percentage sampling is flawed

---
## 3. AQL, LTPD, Producer's and Consumer's Risk, and Designing a Plan
> 🟠 Tier 2 · _Key points:_ AQL with α (producer's risk, ~5%); LTPD/RQL with β (consumer's risk, ~10%); solve for the smallest (n, c)

### Definition
- **AQL (acceptable quality limit):** quality level the buyer accepts as a satisfactory process average; plans accept AQL-quality lots with high probability $1-\alpha$. The standard calls it a quality limit, not a target or licence to ship defects.
- **Producer's risk $\alpha$:** probability of rejecting a lot at AQL quality (often about 5%).
- **LTPD (lot tolerance percent defective), also RQL or LQ:** poor quality the buyer wants rejected; plans accept at LTPD with only $\beta$ (consumer's risk, often 10%).
- **Designing a plan** from two points: find the smallest $(n,c)$ such that $P_a(p_{AQL})\ge1-\alpha$ and $P_a(p_{LTPD})\le\beta$ (use tables, the Poisson nomograph, or a search). The ratio $p_{LTPD}/p_{AQL}$ determines how small $c$ can be: a ratio above about 44.9 permits $c=0$, and a ratio near 8 needs $c=2$ to 3.

### Example
Buyer wants AQL = 1%, $\alpha=5\%$ and LTPD = 8%, $\beta=10\%$. Searching over $c$ with the binomial:

| $c$ | Smallest $n$ | $\alpha$ at 1% | $\beta$ at 8% |
|---|---|---|---|
| 2 | **65** | 2.8% | 9.9% |
| 3 | 82 | 0.9% | 9.8% |
| 4 | 98 | 0.3% | 9.9% |

The cheapest plan is $n=65,\ c=2$ (c = 0 or 1 cannot satisfy both points). Compare with the earlier $n=50,\ c=2$ plan whose $\beta$ at 8% is 22.6%: tightening consumer protection to 10% costs 15 extra inspections per lot. In rupees: at ₹40 per unit inspected, 15 extra units × ₹40 = ₹600 per lot, to cut the chance of accepting a 8%-defective lot from 22.6% to 9.9%. Weigh against the cost of a defective lot reaching the assembly line.

### In the news
See news box. Contracts refer to "AQL 1.0" or "AQL 2.5"; the new ISO edition is a prompt to confirm these numbers, the risk levels they imply and the inspection level.

### Interview angle
> [!question] How it is asked
> "Explain AQL, LTPD, producer's risk and consumer's risk. Is AQL 2.5 the allowed defect rate?"

> [!tip] Strong answer includes
> - Definitions with probabilities at the two points of the OC curve
> - AQL is a rejection-risk reference point (acceptance about 90 to 99%), not a permission to ship 2.5% defects
> - Two-point plan design; cost trade-off of larger $n$
> - Mention that moving AQL or inspection level changes both risks

---
## 4. AOQ, AOQL and ATI (Rectifying Inspection)
> 🟠 Tier 2 · _Key points:_ Reject → 100% screen and replace; AOQ=Pa·p·(N−n)/N; AOQL = max AOQ; ATI = n+(1−Pa)(N−n)

### Definition
Under **rectifying inspection** a rejected lot is 100% inspected and defectives are replaced by good units; accepted lots keep their uninspected defectives.
- **AOQ (average outgoing quality):** average fraction defective in the outgoing stream, $\text{AOQ}\approx P_a\,p\,\frac{N-n}{N}$ (often simplified to $P_a\,p$ for large $N$).
- **AOQL (limit):** the maximum of AOQ over all $p$, the worst average quality the customer ever receives, however bad the incoming quality. The curve rises, peaks and then falls (at high $p$ most lots are rejected and screened).
- **ATI (average total inspection):** $\text{ATI}=n+(1-P_a)(N-n)$, the inspection load per lot. It rises steeply as $p$ worsens, a hidden cost of poor supplier quality.
- Choosing plans by AOQL is the **Dodge-Romig** approach; tables give $(n,c)$ for a target AOQL and lot size.

### Example
Plan $N=1{,}000,\ n=50,\ c=2$:

| $p$ | $P_a$ | AOQ | ATI (units/lot) |
|---|---|---|---|
| 1% | 0.986 | 0.94% | 63 |
| 2% | 0.922 | 1.75% | 125 |
| 3% | 0.811 | 2.31% | 230 |
| 4% | 0.677 | 2.57% | 357 |
| 5% | 0.541 | 2.57% | 487 |
| 8% | 0.226 | 1.72% | 785 |
| 10% | 0.112 | 1.06% | 894 |

The maximum is **AOQL = 2.60%**, reached at $p\approx4.5\%$. Hence "even if incoming quality is terrible, the customer sees on average no worse than 2.6% defective". At $p=4\%$ the plant inspects 357 units per lot on average, more than seven times the sample. At ₹12 per inspected unit that is about ₹4,284 per lot against ₹600 for sampling alone, which is the cost of bad supplier quality in inspection hours.

### In the news
See news box. Standards-based plans tie AOQL to AQL and lot size; revisions keep this logic, so lot-level protection numbers are reproducible.

### Interview angle
> [!question] How it is asked
> "What is AOQL and why does the AOQ curve have a maximum?"

> [!tip] Strong answer includes
> - Definition, requirement that rejected lots are 100% screened
> - Why AOQ falls at high $p$ (more lots rejected and cleaned)
> - ATI formula and the extra cost of poor quality
> - Distinguish AOQL (guaranteed ceiling on average) from LTPD (single-lot protection)

---
## 5. Double, Multiple and Sequential Sampling Plans
> 🟠 Tier 2 · _Key points:_ Take a second sample only if the first is inconclusive; lower average sample number (ASN)

### Definition
A **double sampling plan** $(n_1,c_1,r_1;\,n_2,c_2)$: inspect $n_1$; if $d_1\le c_1$ accept; if $d_1\ge r_1$ reject; otherwise inspect $n_2$ more and accept if $d_1+d_2\le c_2$. **Multiple sampling** extends this to several stages (up to 7 in the standards). **Sequential sampling** (Wald's SPRT) inspects unit by unit and stops when the cumulative defects cross an accept or reject line. Advantages: same protection as a single plan with a lower **average sample number (ASN)** when quality is very good or very bad, and psychological second chance for the supplier. Drawbacks: more complex to administer, variable inspection workload, and larger maximum sample. ASN for double sampling: $\text{ASN}=n_1+n_2\,P(\text{second sample needed})$. $P_a$ is the sum of acceptance paths.

### Example
Plan: $n_1=50$, accept if 0, reject if $\ge3$ defectives; if 1 or 2 are found, take $n_2=50$ and accept if total $\le3$.

| $p$ | $P_a$ | ASN | Single plan $n=80,c=2$ $P_a$ |
|---|---|---|---|
| 1% | 0.975 | 69 | 0.953 |
| 2% | 0.843 | 78 | 0.784 |
| 4% | 0.424 | 77 | 0.375 |
| 8% | 0.043 | 61 | 0.040 |

The double plan gives comparable protection while averaging fewer than 80 units at good and bad quality (69 at 1%, 61 at 8%), but its worst-case sample is 100. Whether the saving is worth the added bureaucracy depends on inspection cost and whether tests are destructive.

### In the news
See news box. The ISO 2859-1 family contains single, double and multiple plans for each code letter, so the same switching framework covers all three.

### Interview angle
> [!question] How it is asked
> "Why would a company choose double sampling over single sampling?"

> [!tip] Strong answer includes
> - Lower ASN at good/bad quality; second chance
> - Compare OC curves and ASN, not just sample size
> - Practical costs: complexity, uneven workload
> - Sequential plans minimise ASN but need unit-by-unit data flow

---
## 6. ANSI/ASQ Z1.4 and ISO 2859-1: How to Read the Tables
> 🟠 Tier 2 · _Key points:_ Lot size + inspection level → code letter → sample size; code letter + AQL → Ac/Re; switching normal/tightened/reduced

### Definition
**ANSI/ASQ Z1.4** (descended from MIL-STD-105E) and its international counterpart **ISO 2859-1** are indexed by AQL for lot-by-lot attribute inspection of a continuing series of lots. Steps:
1. Fix the **AQL** (separately for critical, major, minor defects; common values: critical 0 or 0.065, major 1.0 or 1.5 or 2.5, minor 2.5 or 4.0) and the **inspection level** (General II by default; I for less discrimination, III for more; special S-1 to S-4 for destructive or costly tests).
2. From **Table I**, pick the **sample size code letter** from the lot size and level. General level II: lot 2-8 A, 9-15 B, 16-25 C, 26-50 D, 51-90 E, 91-150 F, 151-280 G, 281-500 H, **501-1,200 J**, 1,201-3,200 K, 3,201-10,000 L, 10,001-35,000 M, 35,001-150,000 N, 150,001-500,000 P, above Q.
3. Code letter → sample size: G 32, H 50, J 80, K 125, L 200, M 315, N 500, P 800, Q 1,250.
4. In **Table II-A** (normal, single) read the acceptance number $Ac$ and rejection number $Re$ at the AQL column; an arrow means use the nearest plan in the arrow direction (with that plan's sample size).
5. Apply **switching rules** (the scheme works as a feedback system):
   - Normal → **tightened** when 2 of 5 consecutive lots are rejected on original inspection.
   - Tightened → normal after 5 consecutive lots accepted; inspection is discontinued if 10 consecutive lots stay on tightened until quality improves.
   - Normal → **reduced** after 10 consecutive lots accepted, with total defectives in those samples within the limit number, steady production and approval of the responsible authority. Reduced → normal if a lot is rejected, or ends between Ac and Re, or production becomes irregular.
The tables are designed for a **continuing series of 10 or more lots**; isolated lots should be assessed using the OC curve or LQ-indexed plans (ISO 2859-2).

### Example
Lot of 1,000 tyre valve assemblies, AQL 1.0 (major), General II, normal inspection. Table I: 501-1,200 → code letter **J** → sample size **80**. Table II-A for J at AQL 1.0: **Ac = 2, Re = 3** (values as commonly reproduced; confirm in your edition). Check the plan's quality: for $n=80,c=2$, $P_a$ at 1% defective is **95.3%**, at 2% **78.4%**, at 5% **23.1%**, at 8% **4.0%**. For a 3,000-unit lot (K, $n=125$) the plan is $Ac=3$ at AQL 1.0 ($P_a=96.3\%$ at 1%); for a 10,000-unit lot (L, $n=200$), $Ac=5$ ($P_a=98.4\%$). Bigger lots get larger samples, but sample size does not scale linearly with lot size.

### In the news
See news box. With the 1999 ISO edition withdrawn in January 2026, QA teams using Z1.4/ISO 2859-1 for incoming inspection should check customer specifications for which edition, and update procedures and ERP inspection plans accordingly (compare [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]], where sampling schemes are configured).

### Interview angle
> [!question] How it is asked
> "Lot size 1,000, AQL 1.0, normal inspection: how many do you inspect and what is the accept number?"

> [!tip] Strong answer includes
> - Lot size and level → code letter J → 80 units; AQL 1.0 → Ac 2 / Re 3
> - Mention switching rules (tightened after 2 of 5 rejects) and defect classes
> - Mention the OC curve of the resulting plan
> - Admit you would verify against the current edition, and say the scheme is meant for continuing lots

---
## 7. Skip-Lot, Continuous Sampling and Variables Plans
> 🟠 Tier 2 · _Key points:_ Reward proven suppliers with fewer inspections; CSP-1 for flow lines; variables plans use fewer units

### Definition
- **Skip-lot sampling (SkSP-1, Dodge; ISO 2859-3):** once a supplier has a long run of accepted lots (a qualifying series, commonly about 10 lots) with good quality history and a stable process, inspect only a fraction $f$ (such as 1/2, 1/3, 1/5) of lots, chosen at random. Return to inspecting every lot when a sampled lot is rejected. It rewards quality with lower inspection cost, on the condition that the supplier's process is stable.
- **Continuous sampling (CSP-1, Dodge):** for a conveyor stream with no natural lots. Inspect 100% until $i$ consecutive units are good (the clearing number), then inspect a random fraction $f$; if a defective is found during sampling, return to 100% inspection. AOQL is controlled by $(i,f)$.
- **Chain sampling (ChSP-1):** for expensive or destructive tests with $c=0$; accept with one defective if the previous $i$ lots had none.
- **Variables plans (ANSI/ASQ Z1.9, ISO 3951):** use the sample mean $\bar x$ and sd $s$ against the spec limit with an acceptability constant $k$: accept if $(U-\bar x)/s\ge k$. For the same protection they typically need smaller samples than attribute plans, provided the characteristic is close to normal. The statistic has to be measured by a reliable gauge, which links to the MSA sub-topics below.

### Example
A supplier of wheel nuts has had 10 consecutive lots accepted under Z1.4 normal inspection with a stable process. The buyer qualifies it for skip-lot with $f=1/3$. If 150 lots are received per year with $n=80$ each, inspected samples fall from $150\times80=12{,}000$ units to $50\times80=4{,}000$ units, saving 8,000 inspected units a year; at ₹15 per unit that is ₹1.2 lakh a year. A single rejection ends the privilege. On the variables side, a Z1.9/ISO 3951 plan would use a markedly smaller sample than the $n=80$ attribute plan for the same AQL when the dimension is normally distributed (read the exact $n$ and $k$ from the standard), saving measurement time but requiring a validated gauge (Gauge R&R below).

### In the news
See news box. Skip-lot rules are in the ISO 2859 family (Part 3); another reason to check which parts of the series your contract invokes after the revision.

### Interview angle
> [!question] How it is asked
> "How can you reduce incoming inspection cost for suppliers who perform well?"

> [!tip] Strong answer includes
> - Reduced inspection under Z1.4 switching, skip-lot, then supplier certification/dock-to-stock
> - Conditions: history, stable SPC, audits, rapid reversion to full inspection
> - Variables plans when data are normal and measurable
> - Link to cost of poor quality and supplier development

---
## 8. MSA Components: Bias, Linearity, Stability, Repeatability, Reproducibility
> 🟠 Tier 2 · _Key points:_ Location (bias, linearity, stability) vs spread (repeatability, reproducibility); observed variance = process variance + measurement variance

### Definition
**Measurement systems analysis (MSA)** asks whether the measurement process is good enough to make decisions. Observed variation decomposes as

$$\sigma^2_{observed}=\sigma^2_{process}+\sigma^2_{measurement},\qquad \sigma^2_{measurement}=\sigma^2_{repeatability}+\sigma^2_{reproducibility}$$

**Location (accuracy) properties:**
- **Bias:** difference between the average of repeated measurements and the reference (master) value. Test with a $t$-test on 10 to 30 readings of one master.
- **Linearity:** how bias changes across the operating range (regress bias on reference value; slope should be near 0).
- **Stability (drift):** change in bias over time; monitored with an X-bar/R chart of a master part measured periodically.
**Spread (precision) properties:**
- **Repeatability (equipment variation, EV):** one appraiser, same part, same gauge, repeated: within-system variation.
- **Reproducibility (appraiser variation, AV):** differences between appraisers (also between gauges, labs or days).
Also **resolution (discrimination)**: the gauge increments should be at most about one-tenth of the tolerance or process variation (the "10-bucket" rule), and the gauge's **range of use**. Without a good measurement system, capability indices (see [[091 Statistical Quality Control (SQC)]]) and control charts are unreliable.

### Example
A tread-depth gauge is checked against a 25.000 mm master with 12 readings: mean 25.035, sd 0.0145. Bias $=+0.035$ mm; $t=0.035/(0.0145/\sqrt{12})=8.38$, $p<0.0001$, 95% CI for bias $[0.026,\,0.044]$ mm: the bias is statistically significant and should be corrected through calibration (adjust the gauge or apply a correction). As a share of an assumed process variation of 0.60 mm (6σ), bias is 5.8%. Linearity: biases at references 2, 4, 6, 8, 10 mm are 0.04, 0.06, 0.07, 0.11, 0.13; regression gives bias $=0.013+0.0115\times\text{reference}$, $R^2=0.965$; linearity $=|0.0115|\times0.60=0.0069$ mm (1.15% of process variation) but the gauge reads 0.128 mm high at 10 mm and only 0.036 mm high at 2 mm: the correction depends on size.

### In the news
See news box. The AIAG 4th edition is the reference auditors use for these definitions; the question "is the instrument good enough?" comes before any capability claim.

### Interview angle
> [!question] How it is asked
> "What is the difference between repeatability and reproducibility, and between precision and accuracy in MSA?"

> [!tip] Strong answer includes
> - Spread vs location; list all five properties and what each tests
> - Variance decomposition
> - Resolution rule and why it matters for SPC
> - Fix: calibrate for bias/linearity; train and standardise procedures for reproducibility; improve fixture or gauge for repeatability

---
## 9. Gauge R&R: Average and Range Method (Worked)
> 🟠 Tier 2 · _Key points:_ 10 parts × 3 appraisers × 3 trials; EV=R̄·K1, AV from X̄diff·K2, PV=Rp·K3; %GRR = GRR/TV

### Definition
Standard crossed study: about 10 parts spanning the process range, 2 to 3 appraisers, 2 to 3 trials, randomised order, appraisers blind to part identity. AIAG average-and-range formulas (sigma-scale constants):

$$EV=\bar{\bar R}\,K_1,\quad AV=\sqrt{(\bar X_{diff}K_2)^2-\frac{EV^2}{nr}},\quad GRR=\sqrt{EV^2+AV^2}$$

$$PV=R_p\,K_3,\qquad TV=\sqrt{GRR^2+PV^2},\qquad \%GRR=\frac{GRR}{TV}\times100,\quad ndc=1.41\frac{PV}{GRR}$$

where $\bar{\bar R}$ is the average of the appraisers' average ranges, $\bar X_{diff}$ the spread between appraiser means, $R_p$ the range of part averages, $n$ parts, $r$ trials. Constants: $K_1=0.8862$ (2 trials), **0.5908** (3 trials); $K_2=0.7071$ (2 appraisers), **0.5231** (3); $K_3=0.3146$ for 10 parts. Decision guide (AIAG): %GRR below 10% acceptable; 10 to 30% may be acceptable depending on application and cost; above 30% unacceptable; **ndc (number of distinct categories) at least 5**. Also compute $\%\text{tolerance}=6\,GRR/\text{tolerance}$ when the job is to sort parts against specification limits.

### Example
A simulated tread-depth study: 10 tyres (true depths 6.8 to 9.4 mm), 3 appraisers, 3 trials each (90 readings). Results:
- Average ranges by appraiser: 0.183, 0.162, 0.165, so $\bar{\bar R}=0.170$; $EV=0.170\times0.5908=\mathbf{0.1004}$ mm.
- Appraiser means 8.047, 8.103, 8.012, $\bar X_{diff}=0.091$; $AV=\sqrt{(0.091\times0.5231)^2-0.1004^2/9}=\mathbf{0.0439}$ mm.
- $GRR=\sqrt{0.1004^2+0.0439^2}=\mathbf{0.1096}$ mm.
- $R_p=2.589$, $PV=2.589\times0.3146=0.8145$; $TV=0.8218$.
- $\%EV=12.2\%$, $\%AV=5.3\%$, **%GRR $=13.3\%$** (marginal band), $ndc=1.41\times0.8145/0.1096=\mathbf{10.5}$ (at least 5, good).
- Against an illustrative tolerance of 2.0 mm: $\%\text{tol}=6\times0.1096/2.0=32.9\%$ (5.15σ: 28.2%): unacceptable for sorting parts near limits even though the study variation looks fine. The same gauge may be acceptable for process control but not for conformance decisions.
Dominant source: repeatability (EV), so improve the gauge or fixture rather than retrain operators.

### In the news
See news box. These constants and bands come from the AIAG 4th edition, still the current manual in 2026.

### Interview angle
> [!question] How it is asked
> "Gauge R&R shows 28%. What does it tell you and what do you do?"

> [!tip] Strong answer includes
> - Compare with 10%/30% bands and with %tolerance, not only %study variation
> - Identify repeatability vs reproducibility as the larger part and fix accordingly
> - Check part selection (must span the process range) and ndc
> - Do not run capability or SPC until acceptable

---
## 10. Gauge R&R: ANOVA Method, %Study Variation and %Contribution
> 🟠 Tier 2 · _Key points:_ Two-way ANOVA with part × operator interaction; variance components; preferred over average-range

### Definition
The **ANOVA method** fits $y_{ijk}=\mu+P_i+O_j+(PO)_{ij}+\varepsilon_{ijk}$ and estimates variance components from mean squares. It separates the **part × operator interaction** (appraisers measuring some parts differently) and uses all data, so it is preferred in software (Minitab, JMP) and by AIAG when available. For $p$ parts, $o$ operators, $r$ trials:

$$\hat\sigma^2_{e}=MS_E,\quad \hat\sigma^2_{PO}=\frac{MS_{PO}-MS_E}{r},\quad \hat\sigma^2_{O}=\frac{MS_O-MS_{PO}}{p\,r},\quad \hat\sigma^2_{P}=\frac{MS_P-MS_{PO}}{o\,r}$$

Repeatability $=\hat\sigma^2_e$; reproducibility $=\hat\sigma^2_O+\hat\sigma^2_{PO}$; $GRR=\hat\sigma^2_e+\hat\sigma^2_O+\hat\sigma^2_{PO}$. Report **%contribution** (variance ratio) and **%study variation** (square-root ratio: $\sqrt{\sigma^2_{GRR}/\sigma^2_{Total}}$), where $\%SV>\%\text{contribution}$ always. If the interaction $p$-value is above 0.25 (AIAG/Minitab default) drop it and pool its sum of squares into the error term. ANOVA connects to [[089 Hypothesis Testing]] (two-way ANOVA) and [[213 Design of Experiments - Factorial, Fractional & Taguchi]] (random-effects model).

### Example
Same 90 readings:

| Source | SS | df | MS | F | p |
|---|---|---|---|---|---|
| Part | 60.413 | 9 | 6.7126 | 771 | <0.001 |
| Operator | 0.1266 | 2 | 0.0633 | 7.27 | 0.0015 |
| Part × Operator | 0.0945 | 18 | 0.00525 | 0.60 | **0.883** |
| Repeatability (error) | 0.5222 | 60 | 0.00870 | | |

Interaction is not significant ($p=0.88>0.25$), so pool: error MS $=(0.0945+0.5222)/78=0.00791$.
- Repeatability sd $=0.0889$ mm; operator sd $=0.0430$ mm; $GRR$ sd $=0.0988$ mm.
- Part sd $\approx0.863$; total sd $\approx0.869$.
- **%contribution $\approx1.3\%$, %study variation $=\mathbf{11.4\%}$**, $ndc=\mathbf{12}$.
Compare the average-range answer (13.3%): the methods agree on "marginal-to-good, repeatability-dominated"; ANOVA is a bit lower because it estimates variance components more efficiently. Operators differ significantly ($p=0.0015$): a mean difference of 0.09 mm that standard work or a fixture should remove, even though it is small relative to part spread.

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols
m = ols("y ~ C(part) * C(op)", data=df).fit()   # df: part, op, trial, y
print(sm.stats.anova_lm(m, typ=2))
```

### In the news
See news box. PPAP submissions typically include MSA studies for key characteristics (see [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]); measurement systems should be acceptable before capability studies are relied on.

### Interview angle
> [!question] How it is asked
> "What is the advantage of the ANOVA Gauge R&R over the average-and-range method?"

> [!tip] Strong answer includes
> - Estimates the interaction, uses all data, gives variance components and tests of significance
> - Difference between %contribution and %study variation
> - Pool the interaction if $p>0.25$
> - Mention number of distinct categories and when to use %tolerance

---
## 11. Attribute Agreement Analysis (Kappa)
> 🟠 Tier 2 · _Key points:_ Pass/fail judgments; agreement within appraisers, between appraisers, vs standard; Cohen's κ corrects for chance

### Definition
For visual or go/no-go inspection the measurement is a category, so Gauge R&R is replaced by **attribute agreement analysis**: 30 to 50 samples (some clearly good, clearly bad and borderline), each judged by 2 to 3 appraisers over 2 or more rounds, ideally also compared with an expert **reference standard**. Metrics:
- **Within appraiser** (repeatability), **between appraisers** (reproducibility), **each vs standard** (accuracy), all appraisers vs standard.
- **Percent agreement** $p_o$ and **Cohen's kappa** $\kappa=\dfrac{p_o-p_e}{1-p_e}$ where $p_e$ is agreement expected by chance from the marginals. Rules of thumb (AIAG): $\kappa>0.75$ good, $\kappa<0.40$ poor; above 0.9 excellent. For ordinal ratings use weighted kappa or Kendall's coefficient; for several raters use Fleiss' kappa.
- **Effectiveness** (correct decisions), **miss rate** (bad parts passed) and **false alarm rate** (good parts failed) when a standard exists. Misses are costly to the customer; false alarms are costly to the plant.
- Fixes: visual standards and limit samples, lighting, training, boundary samples ("master defect library"), automated vision.

### Example
Two inspectors judge 50 painted wheels, pass or fail: both pass 28, A pass/B fail 3, A fail/B pass 2, both fail 17.
- Observed agreement $p_o=(28+17)/50=0.90$.
- Chance agreement $p_e=\frac{31}{50}\cdot\frac{30}{50}+\frac{19}{50}\cdot\frac{20}{50}=0.372+0.152=0.524$.
- $\kappa=(0.90-0.524)/(1-0.524)=\mathbf{0.79}$ (approximate 95% CI 0.62 to 0.96): acceptable, not excellent. 90% raw agreement sounds better than the 0.79 chance-corrected value. If the 5 disagreements cluster on one defect type (say, orange-peel texture), that type needs a boundary sample and a clearer standard.

### In the news
See news box. For attribute inspection the sampling plan only works if the pass/fail call itself is reliable, so attribute agreement belongs before applying Z1.4.

### Interview angle
> [!question] How it is asked
> "Two inspectors agree on 90% of judgments. Is that good?"

> [!tip] Strong answer includes
> - Compute kappa; raw agreement is inflated by chance, especially with many "pass" calls
> - Compare each appraiser against a standard: miss rate and false-alarm rate
> - State thresholds (about 0.75 good) and corrective actions
> - Mention automated vision/limit samples to remove subjectivity

---
## 12. Calibration, MSA in Practice and Common Pitfalls
> 🟠 Tier 2 · _Key points:_ Calibration fixes bias/linearity, GRR measures spread; traceability; resolution and TAR; MSA before capability

### Definition
**Calibration** compares an instrument with a traceable reference standard, documents the error and uncertainty, and adjusts or sets correction rules. In India, calibration traceability runs to the national metrology institute CSIR-NPL (National Physical Laboratory) and NABL-accredited calibration labs working to ISO/IEC 17025. **Calibration and Gauge R&R are complementary:** a gauge can be perfectly calibrated (no bias) and still unusable because it is too noisy (high GRR); or repeatable but biased. Rules and practice:
- **Test accuracy ratio:** reference standard should be several times more accurate than the instrument (commonly 4:1 to 10:1).
- **Calibration interval:** set from drift history (stability chart), usage and criticality; shorten if out-of-tolerance findings occur; assess impact on previously measured product after an out-of-tolerance finding.
- **MSA before SPC/capability:** a poor gauge understates $C_{pk}$ and creates false alarms.
- **Pitfalls:** parts that do not span the process range (understates PV and overstates %GRR); not randomising; operators who know the part IDs; using only 2 trials; ignoring the interaction; destructive tests (need nested studies, same-batch assumption); drift during the study; reporting %GRR with tolerance but not study variation.
- **Auto/tyre contexts:** tread-depth gauges, torque wrenches on wheel-nut lines, CMM for bead rings, tyre uniformity machines, air-leak testers; torque tools are classic reproducibility problems when operator technique matters.

### Example
A tyre plant's air-pressure gauge is certified accurate (calibration passes: bias 0.5 kPa, inside limits) but a Gauge R&R on 10 tyres shows %GRR = 35% dominated by repeatability because the connector seals poorly. Result: calibration alone gave false comfort. Replace the coupler, rerun Gauge R&R (target below 10%, certainly below 30%), and only then rely on process-capability studies for that characteristic. Afterwards, keep a stability chart (X-bar/R of a master tyre measured each shift) so that drift in the gauge triggers recalibration before bad readings reach production decisions.

### In the news
See news box. The AIAG 4th edition continues to be the standard auditors cite; calibration labs accredited to ISO/IEC 17025 are the usual evidence of traceability in supplier audits.

### Interview angle
> [!question] How it is asked
> "Our gauge was calibrated last month but the process capability still looks poor. What do you check?"

> [!tip] Strong answer includes
> - Calibration addresses bias, MSA addresses precision, linearity and stability
> - Run Gauge R&R, stability check and resolution rule; check part selection and fixtures
> - Re-measure capability only after the system is acceptable
> - Consider impact on previously accepted product

---
## 13. ⭐ Advanced: The Economics of Inspection and the Deming kp Rule
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Whether to sample at all is an economic question. **Deming's kp rule:** let $k_1$ = cost to inspect one unit, $k_2$ = cost when a defective unit passes to the next stage (or customer), and $p$ = process fraction defective (from a stable process). Then:
- If $p<k_1/k_2$: **no inspection** (cheaper to let the occasional defect through).
- If $p>k_1/k_2$: **100% inspection** (screen everything).
- Sampling plans (with intermediate $n$) are rarely the cheapest answer for a stable process; they matter when $p$ is near $k_1/k_2$ or when process stability is unknown.
The rule assumes the process is **stable and in control**, with $p$ known from SPC, which is why Deming argued for "improve the process, not inspect it" and why SPC (see [[091 Statistical Quality Control (SQC)]]) comes first. Combine with ATI/AOQ to estimate the total cost per lot of any plan: inspection cost + cost of accepted defectives + cost of screening rejected lots. For automotive suppliers, the cost of a defective reaching the assembly line includes line stoppage, containment and warranty (see [[011 Quality Management (TQM)]]).

### Example
A precision-turned part: $k_1=\text{₹}12$ to inspect a part, $k_2=\text{₹}900$ if a defective reaches the OEM line. Break-even $k_1/k_2=12/900=\mathbf{1.33\%}$.
- If SPC shows a stable $p=0.4\%$: do not inspect; expected cost of leaving defects $=0.004\times900=\text{₹}3.6$ per part vs ₹12 inspection.
- If $p=3\%$ and stable: inspect 100%; expected cost of not inspecting $=0.03\times900=\text{₹}27$ per part vs ₹12.
- For $p=1.33\%$ both cost ₹12 per part: indifferent. Now compare three policies for a 1,000-part lot at a stable $p=4\%$ (above break-even), with the $n=50,\ c=2$ plan from sub-topic 4 ($P_a=0.677$): no inspection costs $1{,}000\times0.04\times900=\text{₹}36{,}000$; 100% inspection costs $1{,}000\times12=\text{₹}12{,}000$ (assuming perfect screening); the sampling plan costs on average $50\times12+0.323\times950\times12+0.677\times(0.04\times950)\times900\approx600+3{,}685+23{,}144=\text{₹}27{,}429$. Sampling beats no inspection but loses clearly to 100% inspection here, because it lets about 38 defectives through in every accepted lot. The lasting fix is process improvement that brings $p$ below 1.33%, not better inspection.

### In the news
See news box. Standards (ISO 2859-1, Z1.4) assume a continuing stream of lots from a supplier whose quality can improve under switching rules, which is the practical bridge between Deming's economics and day-to-day inspection.

### Interview angle
> [!question] How it is asked
> "Is 100% inspection better than sampling? When would you inspect nothing?"

> [!tip] Strong answer includes
> - Cost of inspection vs cost of escaping defect: $p$ vs $k_1/k_2$
> - Stability prerequisite; process improvement as the real fix
> - Human 100% screening is never perfectly effective (measure it with attribute agreement analysis), so the cost of 100% inspection is understated
> - Use sampling for destructive tests or when the process is unknown
