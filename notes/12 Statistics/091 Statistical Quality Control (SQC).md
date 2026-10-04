---
tags: [statistics, tier1]
area: Statistics
topic: "Statistical Quality Control (SQC)"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 12
---
# Statistical Quality Control (SQC)

⬅ [[090 Regression Analysis]] · [[_Index - Statistics|Statistics]] · [[092 Sampling & Experimental Design]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Control Charts — X-bar & R chart]]
2. [[#2. P-chart & NP-chart]]
3. [[#3. C-chart & U-chart]]
4. [[#4. Process Capability Indices]]
5. [[#5. Six Sigma Level & DPMO]]
6. [[#6. Acceptance Sampling]]
7. [[#7. CUSUM Chart]]
8. [[#8. EWMA Chart]]
9. [[#9. Measurement System Analysis (MSA)]]
10. [[#10. Statistical Tolerance]]
11. [[#11. ⭐ Advanced: Pp/Ppk vs Cp/Cpk, Non-Normal Data and ARL]]
12. [[#12. ⭐ Advanced: DMAIC with SPC, Cost of Quality and Pareto Prioritisation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Boeing's 737 MAX audit, a quality-system failure made visible
> **FAA audit of 737 MAX production (reported March 2024).** After the January 2024 Alaska Airlines door-plug blowout, a six-week FAA audit found Boeing failed **33 of 89** product audits at its Renton plant, and its supplier Spirit AeroSystems failed **7 of 13**. Findings included "vague and unclear" mechanic instructions, technicians lacking process knowledge, liquid dish soap used as a lubricant on door seals, and a hotel key card used to test a door seal. Boeing was given 90 days to submit an action plan. The lesson for SQC: weak work instructions and measurement methods (MSA) fail long before a control chart can help. ([Airport Technology](https://www.airport-technology.com/news/faa-737max-audit-fails-boeing-processes/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Control Charts — X-bar & R chart
> 🔴 Tier 1 · _Tracker hint:_ Monitor process mean and range; UCL/LCL = mean ± 3σ; Western Electric rules

### Definition
A **control chart** (Shewhart) plots a statistic over time against a centre line and control limits at $\pm3\sigma$ of the statistic. It separates **common-cause** (random, inherent) variation from **special-cause** (assignable) variation. Control limits come from the process data, **not** from customer specifications.

**X-bar and R charts** are used for variable data in rational subgroups of size $n$ (typically 4 to 6):
- $\bar{\bar X}$ = average of subgroup means; $\bar R$ = average subgroup range.
- X-bar chart: $UCL/LCL=\bar{\bar X}\pm A_2\bar R$
- R chart: $UCL=D_4\bar R$, $LCL=D_3\bar R$ (where $D_3=0$ for $n\le6$).
- Estimate of $\sigma\approx\bar R/d_2$.

| n | A2 | D3 | D4 | d2 |
|---|---|---|---|---|
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |

Read the R chart (variation) first; interpret the X-bar chart only if R is in control. For $n>10$ use X-bar and S charts. **Western Electric / Nelson rules** signal out-of-control: (1) one point beyond 3σ; (2) 2 of 3 consecutive points beyond 2σ, same side; (3) 4 of 5 beyond 1σ, same side; (4) 8 consecutive points on one side of the centre line. Also trends (6 rising or falling) and cycles.

### Example
Bottle-fill process, $n=5$, $\bar{\bar X}=50.0$ ml, $\bar R=4.0$ ml.
X-bar: $50\pm0.577\times4=50\pm2.308$, so UCL = 52.308, LCL = 47.692.
R chart: UCL = $2.114\times4=8.456$; LCL = 0.
A subgroup with mean 52.5 is beyond UCL: look for a special cause (new operator, nozzle wear).

### In the news
See news box. Boeing's audit failures were about process control and instructions; a control chart only works if the process is stable and measured consistently, which is why audit-style checks and SPC complement each other.

### Interview angle
> [!question] How it is asked
> "How would you know if a production process is out of control?" or "What is the difference between control limits and specification limits?"

> [!tip] Strong answer includes
> - Common vs special cause variation (Shewhart/Deming)
> - Limits at $\pm3\sigma$ from the process, not from the customer's spec
> - Check R chart before X-bar; at least two or three Western Electric rules
> - Action: investigate and fix the special cause, do not tamper with a stable process

---

## 2. P-chart & NP-chart
> 🔴 Tier 1 · _Tracker hint:_ Attribute charts for proportion defective; P=variable sample size; NP=fixed

### Definition
**Attribute charts** monitor pass/fail (conforming/nonconforming) data, modelled by the binomial distribution.

- **p-chart**: fraction nonconforming per subgroup; sample size may vary (limits then vary per subgroup).
$$\bar p=\frac{\sum d_i}{\sum n_i},\quad UCL/LCL=\bar p\pm3\sqrt{\frac{\bar p(1-\bar p)}{n}}$$
- **np-chart**: number nonconforming; sample size **constant**.
$$UCL/LCL=n\bar p\pm3\sqrt{n\bar p(1-\bar p)}$$

If the LCL is negative, set it to 0. Use p/np when each unit is simply good or bad; use c/u when counting multiple defects on a unit. Need a sample large enough that $n\bar p\ge5$ (roughly). Attribute charts are less sensitive than variable charts.

### Example
Daily sample $n=100$ packs, long-run $\bar p=0.04$.
$\sigma_p=\sqrt{0.04\times0.96/100}=\sqrt{0.000384}=0.0196$.
p-chart: UCL = $0.04+3(0.0196)=0.0988$ (9.88%); LCL = $0.04-0.0588<0$, so 0.
np-chart: centre = 4; UCL = $4+3\sqrt{100\times0.04\times0.96}=4+3(1.96)=9.88$. A day with 11 rejects signals out of control.

### In the news
See news box. An inspection regime that counts door-plug checks as "pass/fail" depends on how clearly pass is defined; the FAA found vague instructions and improvised tests, so a nominal p-chart would have understated the true defect rate.

### Interview angle
> [!question] How it is asked
> "Which control chart would you use to monitor the percentage of defective units in a call-centre or factory shift?"

> [!tip] Strong answer includes
> - Choice rule: pass/fail data, binomial, p (variable n) or np (constant n)
> - Formula with $\sqrt{p(1-p)/n}$ and setting a negative LCL to zero
> - Need for adequate sample size
> - Prefer variable charts when measurable data are available (more sensitive)

---

## 3. C-chart & U-chart
> 🔴 Tier 1 · _Tracker hint:_ Count of defects per unit; C=constant sample; U=variable; Poisson-based

### Definition
These chart the **number of defects (nonconformities)** where one unit can have several defects (scratches on a panel, errors per invoice). Defect counts follow a **Poisson** distribution, whose variance equals its mean.

- **c-chart** (constant inspection unit/area): $\bar c=\frac{\sum c_i}{k}$, $\;UCL/LCL=\bar c\pm3\sqrt{\bar c}$
- **u-chart** (variable sample size, defects per unit): $\bar u=\frac{\sum c_i}{\sum n_i}$, $\;UCL/LCL=\bar u\pm3\sqrt{\bar u/n_i}$

Distinguish a **defective** (a unit that fails) from a **defect** (a single flaw): one defective unit can contain many defects. Negative LCL is set to 0.

### Example
c-chart: average 9 defects per 100 m of cable, so UCL = $9+3\sqrt9=18$ and LCL = $9-9=0$. A roll with 20 defects is out of control.
u-chart: average $\bar u=0.5$ errors per invoice, batch of $n=20$ invoices: $\sigma=\sqrt{0.5/20}=0.158$, UCL = $0.5+0.474=0.974$, LCL = $0.5-0.474=0.026$.

### In the news
See news box. Counting each deficiency found per aircraft (instructions unclear, wrong lubricant, improper test) is a defects-per-unit view, the natural input to a u-chart across audits.

### Interview angle
> [!question] How it is asked
> "When would you use a c-chart instead of a p-chart?"

> [!tip] Strong answer includes
> - Defect vs defective, with an example
> - Poisson basis and the formula $\bar c\pm3\sqrt{\bar c}$
> - c for fixed area/unit size, u when the inspection unit varies
> - Application in services (errors per report, tickets per shift)

---

## 4. Process Capability Indices
> 🔴 Tier 1 · _Tracker hint:_ Cp=(USL-LSL)/6σ; Cpk=min[(USL-μ),(μ-LSL)]/3σ; target Cp/Cpk ≥ 1.33

### Definition
Capability compares process **spread** with **customer specification limits** (USL, LSL), and is meaningful only when the process is **in statistical control** and approximately normal.

$$C_p=\frac{USL-LSL}{6\sigma},\qquad C_{pk}=\min\left[\frac{USL-\mu}{3\sigma},\ \frac{\mu-LSL}{3\sigma}\right]$$

- $C_p$ = potential capability (ignores centring). $C_{pk}$ = actual capability (penalises off-centre process). $C_{pk}\le C_p$, equal only when centred.
- Common targets: $\ge1.33$ for existing processes, $\ge1.67$ for new/critical processes; $C_{pk}=1$ means 3σ to the nearest limit (about 2,700 ppm out of spec if centred); 2.0 corresponds to Six Sigma level (with the 1.5σ shift convention).
- $C_{pk}<1$: process produces defects. If $C_p$ is high but $C_{pk}$ is low, **centre the process** (cheap); if both are low, **reduce variation** (expensive).

### Example
Shaft diameter spec 10.0 mm ± 0.6 (LSL 9.4, USL 10.6). Process $\mu=10.1$, $\sigma=0.12$.
$C_p=1.2/(6\times0.12)=1.2/0.72=1.667$.
$C_{pk}=\min[(10.6-10.1)/0.36,\ (10.1-9.4)/0.36]=\min[1.389,\ 1.944]=1.389$.
Spread is excellent, but off-centre; shifting the mean to 10.0 would give $C_{pk}=C_p=1.667$.

### In the news
See news box. Capability analysis assumes the measurement is trustworthy; the audit's improvised tests (a hotel key card) show how an unreliable gauge makes any Cpk number meaningless: do MSA first (see sub-topic 9).

### Interview angle
> [!question] How it is asked
> "Cp is 2 but Cpk is 0.8. What does that tell you?" or "What Cpk do you need to supply an automaker?"

> [!tip] Strong answer includes
> - Formulas for Cp and Cpk, with the meaning of the difference
> - Prerequisites: stable process, normality, valid measurement
> - Targets (1.33, 1.67) and what to fix first (centre, then spread)
> - Short-term Cp/Cpk vs long-term Pp/Ppk (see the advanced section below)

---

## 5. Six Sigma Level & DPMO
> 🔴 Tier 1 · _Tracker hint:_ 6σ = 3.4 DPMO; sigma level from Z-score; DPMO = defects/opportunities × 1M

### Definition
$$DPMO=\frac{\text{Defects}}{\text{Units}\times\text{Opportunities per unit}}\times1{,}000{,}000$$

Sigma level is the Z-score of the yield, conventionally with a **1.5σ long-term shift** allowance: $\sigma_{level}=Z_{(1-\text{DPMO}/10^6)}+1.5$.

| Sigma level | DPMO | Yield |
|---|---|---|
| 2 | 308,538 | 69.1% |
| 3 | 66,807 | 93.3% |
| 4 | 6,210 | 99.38% |
| 5 | 233 | 99.977% |
| 6 | 3.4 | 99.99966% |

Related metrics: **DPU** (defects per unit), **FPY** (first-pass yield) and **rolled throughput yield** $RTY=\prod FPY_i$ (the product across process steps). **DMAIC** (Define, Measure, Analyse, Improve, Control) is the improvement roadmap; belts: Yellow, Green, Black, Master Black Belt. Six Sigma is a data-driven programme to cut variation and defects; critics note the 1.5σ shift is a convention and not a law.

### Example
500 invoices, 4 error opportunities each, 38 errors found.
$DPMO=\dfrac{38}{500\times4}\times10^6=\dfrac{38}{2000}\times10^6=19{,}000$.
Yield = $1-0.019=98.1\%$; $Z\approx2.07$, so sigma level $\approx2.07+1.5\approx3.6$.
RTY example: 5 steps each with FPY 98% gives $0.98^5=0.904$, about 90%.

### In the news
See news box. Safety-critical industries aim for very low defect rates; the audit's 33 of 89 failures (a 37% failure rate on sampled audits, my arithmetic) shows how far a weak system is from Six Sigma discipline.

### Interview angle
> [!question] How it is asked
> "What does Six Sigma mean, and how do you compute DPMO?" or "Process is at 3 sigma; is that good enough?"

> [!tip] Strong answer includes
> - DPMO formula, 3.4 DPMO at 6σ with the 1.5σ shift
> - Rolled throughput yield: many steps compound small defect rates
> - DMAIC sequence with one tool per phase
> - Contextual answer: 3σ may be fine for a canteen, not for surgery or aircraft

---

## 6. Acceptance Sampling
> 🔴 Tier 1 · _Tracker hint:_ AQL; Operating Characteristic (OC) curve; producer's risk (α) vs consumer's risk (β)

### Definition
**Acceptance sampling** decides whether to accept or reject a **lot** by inspecting a random sample. A **single sampling plan** is $(n, c)$: inspect $n$ items; accept if defectives $\le c$.

- **AQL** (Acceptable Quality Level): quality level the supplier is expected to meet; lots at AQL should be accepted with high probability ($1-\alpha$).
- **LTPD/RQL**: the poor quality level the buyer wants rejected.
- **Producer's risk $\alpha$**: probability a good lot (at AQL) is rejected. **Consumer's risk $\beta$**: probability a bad lot (at LTPD) is accepted.
- **OC curve**: plots probability of acceptance $P_a$ against lot fraction defective $p$. Steeper curve = better discrimination; larger $n$ steepens it; larger $c$ shifts it right.
- Binomial: $P_a=\sum_{x=0}^{c}\binom nx p^x(1-p)^{n-x}$ (Poisson approximation when $n$ is large and $p$ small).
- **AOQ**/AOQL: average outgoing quality, with rectifying inspection. Standards: ANSI/ASQ Z1.4 (MIL-STD-105E), ISO 2859; sampling by variables Z1.9.

Acceptance sampling is a screening of lots, not a way to build quality in; modern practice favours process control and supplier certification.

### Example
Plan $n=50$, $c=2$.
At $p=0.02$: $P(0)=0.98^{50}=0.364$; $P(1)=50(0.02)(0.98^{49})=0.372$; $P(2)=1225(0.02)^2(0.98^{48})=0.186$. $P_a=0.364+0.372+0.186=0.922$, so $\alpha\approx7.8\%$.
At $p=0.08$: $P_a=0.0155+0.0673+0.1433=0.226$, so $\beta\approx22.6\%$ (consumer's risk is high; increase $n$ or reduce $c$).

### In the news
See news box. When a supplier (Spirit AeroSystems failed 7 of 13 audits) is not reliably producing quality, buyers move from lot sampling to tighter inspection levels and on-site supplier surveillance.

### Interview angle
> [!question] How it is asked
> "Explain AQL and the OC curve" or "How would you decide how many units to inspect from an incoming lot?"

> [!tip] Strong answer includes
> - Plan notation $(n,c)$ and the accept/reject rule
> - Producer's vs consumer's risk and their link to AQL and LTPD
> - OC curve reading and how $n$ and $c$ change it
> - Limits: sampling does not improve quality; prefer supplier quality systems

---

## 7. CUSUM Chart
> 🔴 Tier 1 · _Tracker hint:_ Cumulative Sum chart; detects small shifts; better than Shewhart for subtle drift

### Definition
Shewhart charts react to large shifts (about 2σ or more) but are slow on small sustained shifts (about 0.5σ to 1.5σ). **CUSUM** accumulates deviations from the target, so small persistent drifts add up.

Tabular CUSUM with target $\mu_0$, reference value $k$ (usually half the shift to detect, e.g. $0.5\sigma$) and decision interval $h$ (typically $4\sigma$ to $5\sigma$):

$$C_i^+=\max[0,\ x_i-(\mu_0+k)+C_{i-1}^+],\qquad C_i^-=\max[0,\ (\mu_0-k)-x_i+C_{i-1}^-]$$

Signal when $C_i^+>h$ or $C_i^->h$. Starting values are 0. The cumulative sum resets to zero when the process is on target, so it is robust to noise. Use for tool wear, slow drifts in temperature, process mean creep; also in fraud and credit monitoring. Tune $k,h$ to the desired Average Run Length (ARL).

### Example
Target $\mu_0=50$, $\sigma=2$, $k=1$ (0.5σ), $h=10$ (5σ). Observations: 52, 53, 52, 53, 52, 53, 52, 53 (true mean 52.5, a 1.25σ shift).
$C^+_i=\max[0,\,x_i-51+C^+_{i-1}]$: 1, 3, 4, 6, 7, 9, 10, 12.
Signal at observation 8 ($12>10$). A Shewhart chart with 3σ limits (UCL = 56) never signals on these points.

### In the news
See news box. Slow drifts (tool wear, a lubricant substitution) are exactly what CUSUM detects before a hard failure; a manufacturer facing scrutiny would add run-based charts to catch creeping deviations.

### Interview angle
> [!question] How it is asked
> "A process drifts slowly and your X-bar chart does not flag it. What would you do?"

> [!tip] Strong answer includes
> - Shewhart is insensitive to small shifts; CUSUM accumulates evidence
> - Formula with $k$ and $h$ and how they are chosen
> - ARL trade-off: faster detection vs false alarms
> - Alternative: EWMA, or Western Electric run rules

---

## 8. EWMA Chart
> 🔴 Tier 1 · _Tracker hint:_ Exponentially Weighted Moving Average control chart; weighted recent observations

### Definition
The **EWMA** statistic blends the latest observation with the previous EWMA:

$$z_i=\lambda x_i+(1-\lambda)z_{i-1},\qquad z_0=\mu_0,\quad 0<\lambda\le1$$

Weights on past data decay geometrically, $\lambda(1-\lambda)^j$. Small $\lambda$ (0.05 to 0.25) gives long memory and sensitivity to small shifts; $\lambda=1$ is the Shewhart chart. Control limits:

$$\mu_0\pm L\sigma\sqrt{\frac{\lambda}{2-\lambda}\left[1-(1-\lambda)^{2i}\right]}$$

which converge to $\mu_0\pm L\sigma\sqrt{\lambda/(2-\lambda)}$ (with $L\approx2.7$ to $3$). EWMA is robust to non-normal data when used with individual observations, and is also used for **forecasting** (exponential smoothing in demand planning). Compared with CUSUM: similar small-shift sensitivity, simpler to explain; EWMA can serve as a one-step-ahead predictor.

### Example
$\mu_0=50$, $\sigma=2$, $\lambda=0.2$. $x_1=52$: $z_1=0.2(52)+0.8(50)=50.4$. $x_2=53$: $z_2=0.2(53)+0.8(50.4)=10.6+40.32=50.92$.
Steady-state half-width $=3\times2\times\sqrt{0.2/1.8}=6\times0.3333=2.0$, so UCL = 52.0 and LCL = 48.0. EWMA drifting beyond 52 signals a shift while individual points stay within ±6.

### In the news
See news box. Monitoring a stream of weekly audit or defect scores with an EWMA would flag a gradual decline without reacting to each noisy week.

### Interview angle
> [!question] How it is asked
> "What is an EWMA control chart and how does it differ from a Shewhart chart?"

> [!tip] Strong answer includes
> - Recursive formula and the meaning of $\lambda$
> - Small $\lambda$ = better for small shifts, larger = closer to Shewhart
> - Comparison with CUSUM
> - Use also as a forecasting smoother

---

## 9. Measurement System Analysis (MSA)
> 🔴 Tier 1 · _Tracker hint:_ Gauge R&R; repeatability + reproducibility ≤ 10% = excellent; 10-30% = marginal

### Definition
MSA checks that observed variation reflects the **process**, not the **gauge**: $\sigma^2_{total}=\sigma^2_{process}+\sigma^2_{measurement}$.

**Gauge R&R** has two parts: **Repeatability** (equipment variation, EV): same operator, same part, same gauge, repeated. **Reproducibility** (appraiser variation, AV): different operators.

$$GRR=\sqrt{EV^2+AV^2},\qquad \%GRR=\frac{GRR}{TV}\times100,\qquad TV=\sqrt{GRR^2+PV^2}$$

AIAG guidance: **below 10% acceptable (excellent)**; **10% to 30% marginal** (depends on cost and criticality); **above 30% unacceptable**. Also report **ndc** (number of distinct categories) $=1.41\,(PV/GRR)$, which should be at least 5. Other attributes of a measurement system: **bias, linearity, stability, resolution**. For attribute data use attribute agreement analysis (Kappa). Typical study: 10 parts, 3 operators, 2 to 3 trials, with ANOVA method.

### Example
$EV=0.20$, $AV=0.10$, $PV=1.00$ (part-to-part).
$GRR=\sqrt{0.04+0.01}=0.2236$; $TV=\sqrt{0.05+1.00}=1.0247$; $\%GRR=0.2236/1.0247=21.8\%$ (marginal). $ndc=1.41\times(1.00/0.2236)=6.3$, so 6 categories, enough for control but not for capability work.

### In the news
See news box. The FAA's observation of a hotel key card used to check a door seal is a vivid MSA failure: a non-calibrated, non-standard gauge guarantees poor repeatability and reproducibility.

### Interview angle
> [!question] How it is asked
> "Different inspectors measure the same part and get different values. What do you do?"

> [!tip] Strong answer includes
> - Repeatability vs reproducibility, with the %GRR thresholds (10% and 30%)
> - Run a Gauge R&R study before capability or SPC work
> - Bias, linearity, stability and resolution as other checks
> - Remedies: training, standard work instruction, better gauge, calibration

---

## 10. Statistical Tolerance
> 🔴 Tier 1 · _Tracker hint:_ Natural tolerance vs specification; process centering; sigma-based tolerance

### Definition
- **Specification (engineering) tolerance**: allowed range set by design/customer, $USL-LSL$.
- **Natural tolerance**: what the process actually delivers, $\mu\pm3\sigma$, i.e. a width of $6\sigma$, covering 99.73% of output if normal.
- Capability is the ratio: $C_p=\text{spec width}/\text{natural width}$.
- A **statistical tolerance interval** covers a stated proportion (e.g. 99%) of the population with stated confidence (e.g. 95%): $\bar x\pm k\,s$, with $k$ larger than the z-value since the mean and σ are estimated.

**Tolerance stack-up:** in assemblies with independent parts, worst-case adds tolerances linearly; the **statistical (RSS) method** adds in quadrature, $T_{assembly}=\sqrt{\sum T_i^2}$, allowing looser part tolerances if parts are centred and in control. **Centring** matters: an off-centre process uses up tolerance on one side. Taguchi's **loss function** $L=k(y-m)^2$ adds that any deviation from target costs money, even inside the spec.

### Example
Three stacked parts, each ±0.30 mm. Worst case $=0.30\times3=\pm0.90$ mm. RSS $=\sqrt{3\times0.30^2}=\sqrt{0.27}=\pm0.52$ mm. Natural tolerance check: spec ±0.6 and $\sigma=0.1$ gives natural tolerance ±0.3, so spec is twice as wide as the process ($C_p=2$).

### In the news
See news box. The audit noted insufficient quality checks on the door plug that failed; tolerance and fit verification at assembly are what ensure such parts are correctly seated and secured.

### Interview angle
> [!question] How it is asked
> "What is the difference between control limits, natural tolerance and specification limits?"

> [!tip] Strong answer includes
> - Three limits: voice of the process vs voice of the customer
> - Natural tolerance ±3σ and the link to $C_p$
> - Worst-case vs RSS stack-up with numbers
> - Process centring and Taguchi's loss idea

---

## 11. ⭐ Advanced: Pp/Ppk vs Cp/Cpk, Non-Normal Data and ARL
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Cp/Cpk** use **short-term (within-subgroup)** sigma, $\hat\sigma=\bar R/d_2$: what the process could do if only common-cause variation acted. **Pp/Ppk** use **overall (long-term)** sample standard deviation, including drift and shifts: what the customer actually receives. Normally $P_{pk}\le C_{pk}$; a large gap signals an unstable process or tool drift.
- **Non-normal data** (cycle time, defect rates, failure times): transform (Box-Cox, Johnson), fit another distribution (Weibull, lognormal) or use percentile-based capability; applying normal formulas to skewed data misleads.
- **Cpm** (Taguchi) penalises deviation from the target as well as spread.
- **Average Run Length (ARL):** the average number of points plotted before a signal. In control, $ARL_0=1/\alpha\approx370$ for 3σ Shewhart (false-alarm interval); out of control, $ARL_1=1/(1-\beta)$ (detection speed). Chart choice is an ARL trade-off.
- **Chart selection:** continuous data and subgroups: X-bar/R or X-bar/S; individuals: I-MR; defective units: p/np; defects: c/u; small shifts: CUSUM/EWMA.

### Example
Short-term $\sigma=0.10$, long-term $\sigma=0.15$, spec width 1.2, centred: $C_p=1.2/0.6=2.0$ but $P_p=1.2/0.9=1.33$. The process has the potential for 2.0 but delivers 1.33 because of drift between subgroups. For 3σ Shewhart, $ARL_0=1/0.0027\approx370$.

### In the news
See news box. A large gap between potential (Cpk) and performance (Ppk) is what tends to show up in audits: processes that look fine in a good sample but vary from shift to shift and supplier to supplier.

### Interview angle
> [!question] How it is asked
> "What is the difference between Cpk and Ppk?" or "How do you handle capability for non-normal data?"

> [!tip] Strong answer includes
> - Within vs overall sigma, and what a large gap means
> - Non-normal handling (transform or fitted distribution)
> - ARL concept for chart design and the 370 number
> - Chart selection map by data type

---

## 12. ⭐ Advanced: DMAIC with SPC, Cost of Quality and Pareto Prioritisation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
SQC tools plug into **DMAIC**: Define (project charter, SIPOC, CTQ), Measure (MSA, baseline capability), Analyse (Pareto, fishbone, regression, hypothesis tests), Improve (DOE, poka-yoke), Control (SPC charts, control plan, SOPs).

**Pareto analysis:** about 80% of defects come from about 20% of causes; rank by frequency (or cost) and target the vital few.

**Cost of Quality (COQ) = Prevention + Appraisal + Internal failure + External failure.** Investing in prevention (training, design, SPC) lowers failure costs; the "1-10-100 rule" (cost grows by roughly 10x at each later stage) is a heuristic. **Lean Six Sigma** adds waste removal; **Poka-yoke** (mistake-proofing) removes the chance of error; **Jidoka** stops the line on defect detection. Standards: ISO 9001, IATF 16949 (auto), AS9100 (aerospace).

### Example
Defect log for 200 rejects: label wrong 90, seal leak 56, short fill 30, others 24. Cumulative: 45%, 73%, 88%, 100%. The top two causes explain 73% of the defects, so start there. COQ: if prevention ₹5 lakh and appraisal ₹3 lakh reduce failure cost from ₹40 lakh to ₹20 lakh, net saving is ₹12 lakh.

### In the news
See news box. After quality crises, firms typically raise prevention and appraisal spending, which is COQ logic: pay earlier to avoid the far larger failure cost.

### Interview angle
> [!question] How it is asked
> "A plant has a rising rejection rate. Walk me through how you would fix it."

> [!tip] Strong answer includes
> - DMAIC structure with a tool in each phase
> - Pareto to focus, MSA to validate data, control chart to confirm stability
> - Root cause (5 Whys, fishbone) and sustainable control plan
> - COQ framing to justify investment to management

---
## 🔗 Go deeper: expansion notes
- [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)|Acceptance Sampling & Measurement System Analysis (Gauge R&R)]]
- [[213 Design of Experiments - Factorial, Fractional & Taguchi|Design of Experiments - Factorial, Fractional & Taguchi]]
