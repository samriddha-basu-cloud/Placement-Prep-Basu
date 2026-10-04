---
tags: [statistics, tier2]
area: Statistics
topic: "Design of Experiments - Factorial, Fractional & Taguchi"
tier: Tier 2
roles: Operations / Quality / Analytics
status: complete
subtopics: 13
---
# Design of Experiments - Factorial, Fractional & Taguchi

⬅ [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]] · [[_Index - Statistics|Statistics]] · [[214 Causal Inference & Experimentation Beyond A-B Tests]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Quality / Analytics

## Sub-topics in this note
1. [[#1. One-Factor ANOVA: Worked Table]]
2. [[#2. Randomisation, Replication and Blocking]]
3. [[#3. The 2² Full Factorial: Effects and Interaction]]
4. [[#4. The 2³ Factorial: Worked Example with a Strong Interaction]]
5. [[#5. Main-Effect and Interaction Plots; Reading Effect Plots]]
6. [[#6. Fractional Factorials: Aliasing and Resolution]]
7. [[#7. Blocking in Factorials, Confounding and Centre Points]]
8. [[#8. Response Surface Methodology: Steepest Ascent and Optimisation]]
9. [[#9. Taguchi Methods: Orthogonal Arrays, S/N Ratios and Loss Function]]
10. [[#10. Split-Plot and Other Restricted-Randomisation Designs]]
11. [[#11. Executed Python Example: Factorial Analysis]]
12. [[#12. DOE in a Six Sigma Project: Steps, Sample Size and Pitfalls]]
13. [[#13. ⭐ Advanced: DOE vs A/B Testing, Optimal Designs and Adaptive Experimentation]]

## 📰 News box
> [!news] Why this matters now: designed experiments are going adaptive and Bayesian in industry tooling
> **Meta maintains Ax, an open-source "Adaptive Experimentation Platform" (documentation checked 2026).** Ax supports Bayesian optimisation, A/B tests and field experiments, with a peer-reviewed paper, "Ax: A Platform for Adaptive Experimentation", at the AutoML 2025 conference; the documentation lists version 1.3.1 as the latest stable release and it installs via `pip install ax-platform`. Classical factorial designs fix every run in advance; adaptive platforms choose the next run from what has been learned so far. The statistics you learn here (factors, effects, interactions, response surfaces) are what those tools automate. ([Ax documentation](https://ax.dev/))
>
> **The NIST/SEMATECH Engineering Statistics Handbook still anchors the standard definition.** It describes design of experiments as "an efficient procedure for planning experiments so that the data obtained can be analyzed to yield valid and objective conclusions", with the steps of fixing objectives, choosing process factors and laying out a detailed plan in advance. It treats experimentation as deliberate manipulation of inputs to build empirical input-output models. ([NIST handbook](https://www.itl.nist.gov/div898/handbook/pri/section1/pri11.htm))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. One-Factor ANOVA: Worked Table
> 🟠 Tier 2 · _Key points:_ SSB, SSW, MS, F = MSB/MSW; then multiple comparisons (Tukey); eta-squared

### Definition
A **one-factor (one-way) experiment** compares $a$ treatments (machines, suppliers, furnaces) on a response using $n$ replicates each, run in random order. The model: $y_{ij}=\mu+\tau_i+\varepsilon_{ij}$, $\varepsilon\sim N(0,\sigma^2)$. $H_0:\tau_1=\dots=\tau_a=0$. The total variation splits:

$$SS_T=SS_{Between}+SS_{Within},\quad MS_B=\frac{SS_B}{a-1},\quad MS_W=\frac{SS_W}{a(n-1)},\quad F=\frac{MS_B}{MS_W}\sim F_{a-1,\;a(n-1)}$$

Assumptions: independence, normal residuals, equal variances (check residual plots; Levene's test). A significant $F$ only says "some means differ"; use **Tukey HSD** (all pairs, controls family error), Dunnett (vs a control) or Fisher LSD (only after significant F). Effect size $\eta^2=SS_B/SS_T$. Basic ANOVA is also in [[089 Hypothesis Testing]]; the design view is in [[092 Sampling & Experimental Design]].

### Example
Tensile strength (MPa) of rods from 3 heat-treatment furnaces, 5 rods each: F1: 512, 518, 509, 521, 515; F2: 526, 531, 528, 524, 533; F3: 516, 520, 514, 519, 522. Means 515.0, 528.4, 518.2; grand mean 520.53.

| Source | SS | df | MS | F | p |
|---|---|---|---|---|---|
| Between furnaces | 489.73 | 2 | 244.87 | **15.97** | 0.0004 |
| Within (error) | 184.00 | 12 | 15.33 | | |
| Total | 673.73 | 14 | | | |

Critical $F_{0.05;2,12}=3.89$, so reject $H_0$. $\eta^2=0.727$. Tukey HSD at 5% is $q_{0.05;3,12}\sqrt{MS_W/n}=3.77\times\sqrt{15.33/5}=6.61$ MPa: F2 is higher than F1 (difference 13.4, p < 0.001) and F3 (10.2, p = 0.004), while F1 vs F3 (3.2) is not significant (p = 0.43). Business reading: F2 gives a stronger rod; confirm it is not a one-off by replication, then check cost.

### In the news
See news box. NIST's handbook treats single-factor comparison as the starting block on which factorial and response-surface designs are built.

### Interview angle
> [!question] How it is asked
> "Three suppliers' batches were tested. How do you decide whether quality differs and which is best?"

> [!tip] Strong answer includes
> - Randomised replicated design, ANOVA table with F test, then Tukey for pairs
> - Check assumptions (residuals, equal variances)
> - Distinguish statistical significance from practical size (effect size, spec margin)
> - Mention blocking if conditions vary (batch, day) and a confirmation run

---
## 2. Randomisation, Replication and Blocking
> 🟠 Tier 2 · _Key points:_ Fisher's three principles; replicate ≠ repeat measurement; block what you cannot randomise away

### Definition
- **Randomisation:** run order and unit assignment by chance, which averages out unknown lurking variables (warm-up drift, tool wear, operator fatigue) and justifies the statistical analysis. Not randomising makes a time trend look like a factor effect.
- **Replication:** repeating the entire experimental run (set-up from scratch) to estimate pure error and improve precision. **Repeated measurements** of the same run are not replicates; they understate the error. Standard error of an effect in a two-level factorial with $N$ total runs: $SE=2\sigma/\sqrt N$.
- **Blocking:** group runs into homogeneous blocks (shift, batch, machine, day) and compare treatments within blocks, removing block-to-block variation. Randomised complete block design: every treatment appears in every block. Related designs: Latin squares (two blocking variables), incomplete blocks and **confounding** (sub-topic 7). Nuisance variables are blocked, factors of interest are varied, and noise is randomised.
- **Hard-to-change factors** (furnace temperature) may force restricted randomisation: split-plot designs (sub-topic 10).
- Related ideas: sample size from the needed detectable effect; balanced designs; orthogonality (columns uncorrelated, so effects are estimated independently).

### Example
Testing a new cutting insert on 8 CNC machines running two shifts. Wrong: run all new inserts on the morning shift. Right: block by machine (each machine runs both insert types in random order) so the machine-to-machine variation drops out. If shift-to-shift differences are 4 units and insert differences are 1.5 units, a block design makes the 1.5 detectable; an unblocked design buries it. Required replicates with $\sigma=2$ and wanting to detect an effect of 2.8: $SE=2\sigma/\sqrt N=1\Rightarrow N=16$ runs (detectable effect $\approx2.8\,SE$ at 5% two-sided significance and 80% power).

### In the news
See news box. Whether experiments are run by hand or through a platform such as Ax, the principles of randomisation, replication and blocking are unchanged.

### Interview angle
> [!question] How it is asked
> "Why randomise, and how is a block different from a factor?"

> [!tip] Strong answer includes
> - Randomisation protects against hidden trends; replication gives error estimate; blocking removes known nuisance variation
> - A block is a nuisance grouping you do not study; a factor is something you deliberately vary
> - Replicates vs repeated measures
> - Example from a plant (shift, machine, batch)

---
## 3. The 2² Full Factorial: Effects and Interaction
> 🟠 Tier 2 · _Key points:_ Two factors at two levels, 4 runs; effect = mean(high)−mean(low); interaction = difference of simple effects

### Definition
A **2^k full factorial** runs every combination of $k$ factors at 2 levels (coded −1, +1). It estimates all main effects and interactions with the same runs (**hidden replication**), which is far more efficient than one-factor-at-a-time. For a 2² with $n$ replicates and treatment totals $(1),a,b,ab$:

$$A=\frac{a+ab-b-(1)}{2n},\quad B=\frac{b+ab-a-(1)}{2n},\quad AB=\frac{ab+(1)-a-b}{2n},\quad SS_{effect}=\frac{(\text{contrast})^2}{4n}$$

The **interaction** exists when the effect of A depends on the level of B. The regression coefficient is half the effect: $\hat y=\bar y+\frac{A}{2}x_1+\frac{B}{2}x_2+\frac{AB}{2}x_1x_2$. The standard error of an effect is $\sqrt{4\,MSE/(4n)}$ with error df $=4(n-1)$.

### Example
Chemical yield (%): A = temperature 160 vs 180 C, B = catalyst 1% vs 2%, three replicates each.

| Run | A | B | Yields | Total | Mean |
|---|---|---|---|---|---|
| (1) | − | − | 28, 25, 27 | 80 | 26.67 |
| a | + | − | 36, 32, 32 | 100 | 33.33 |
| b | − | + | 18, 19, 23 | 60 | 20.00 |
| ab | + | + | 31, 30, 29 | 90 | 30.00 |

- $A=(100+90-60-80)/6=\mathbf{+8.33}$; $B=(60+90-100-80)/6=\mathbf{-5.00}$; $AB=(90+80-100-60)/6=\mathbf{+1.67}$.
- $SS_A=50^2/12=208.33$, $SS_B=30^2/12=75.0$, $SS_{AB}=10^2/12=8.33$; $SS_T=323.0$, $SS_E=31.33$ (8 df), $MSE=3.92$.
- $F_A=53.2$ ($p<0.001$), $F_B=19.1$ ($p=0.002$), $F_{AB}=2.13$ ($p=0.18$): temperature helps, higher catalyst hurts, no significant interaction. Effect SE $=1.14$; 95% margin $2.31\times1.14=2.6$.
- Simple effects: A at low B $=+6.67$, A at high B $=+10.0$ (the difference, 3.3, is twice $AB$, hence the interaction estimate 1.67).
- Decision: choose 180 C and 1% catalyst, predicted mean about 33.3%.

### In the news
See news box. NIST's handbook builds from 2^2 and 2^3 designs for exactly this reason: they are the unit from which screening and optimisation designs grow.

### Interview angle
> [!question] How it is asked
> "Compute main effects and the interaction from a 2² table, and explain why factorials beat one-factor-at-a-time."

> [!tip] Strong answer includes
> - Effect = average at high minus average at low; interaction = half the difference in simple effects
> - Every run contributes to every effect (efficiency), and interactions are detectable
> - Error estimate from replicates; effect SE and F test
> - Coded units and the equivalent regression model

---
## 4. The 2³ Factorial: Worked Example with a Strong Interaction
> 🟠 Tier 2 · _Key points:_ 8 runs, 7 effects; sign table; a null main effect can hide a big interaction

### Definition
For three factors A, B, C at two levels there are 8 treatment combinations and 7 effects: A, B, C, AB, AC, BC, ABC. Effect of any term $=\frac{1}{N/2}\sum (\text{sign})\,y$ where the sign column of an interaction is the product of its factor columns; $SS=(\sum \text{sign}\cdot y)^2/N$. With $n$ replicates, error df $=8(n-1)$. Without replication use **normal/half-normal plot of effects** or Pareto chart to separate real effects (off the line) from noise (on the line), or pool negligible high-order terms (sparsity-of-effects principle; three-factor interactions are rarely real). Residual checks: normality, constant variance vs fitted values, and run order.

### Example
Injection moulding, response = warpage (units of 0.01 mm, **lower is better**): A = melt temperature 230/250 C, B = hold pressure 60/80 bar, C = cooling time 12/18 s, 2 replicates per run (16 runs). Treatment means in standard order (1), a, b, ab, c, ac, bc, abc: 23, 31, 27, 19, 20, 29, 23, 15.

| Term | Effect | SS | F | p | % of total SS |
|---|---|---|---|---|---|
| A | +0.25 | 0.25 | 0.13 | 0.73 | 0.1% |
| B | −4.75 | 90.25 | 45.1 | <0.001 | 21.3% |
| C | −3.25 | 42.25 | 21.1 | 0.002 | 10.0% |
| **AB** | **−8.25** | 272.25 | 136.1 | <0.001 | 64.2% |
| AC | +0.25 | 0.25 | 0.13 | 0.73 | 0.1% |
| BC | −0.75 | 2.25 | 1.13 | 0.32 | 0.5% |
| ABC | −0.25 | 0.25 | 0.13 | 0.73 | 0.1% |
| Error (8 df) | | 16.0 | | | MSE = 2.0 |

$SE_{effect}=\sqrt{4\times2/16}=0.707$; margin of error at 5% $=2.31\times0.707=1.63$. **Main effect of A is nearly zero but the AB interaction is the biggest effect.** Cell means of warpage at (A,B): (230,60)=21.5, (230,80)=25.0, (250,60)=30.0, (250,80)=17.0. Raising temperature worsens warpage at low pressure (+8.5) but improves it at high pressure (−8.0); averaged over B, these cancel to a zero A effect. Best setting: **A high, B high, C high** (predicted warpage 15.0), $R^2=0.96$. Moral: never interpret main effects alone when a significant interaction involves that factor. One-factor-at-a-time from the (230,60) corner would have found both A and B "bad" and missed the best corner.

### In the news
See news box. Interactions are why simple A/B thinking ("test one variable") needs the factorial extension, a theme repeated in multi-variant online experiments.

### Interview angle
> [!question] How it is asked
> "A factor shows no main effect in your factorial. Can you drop it from the process model?"

> [!tip] Strong answer includes
> - No: check interactions; opposite simple effects cancel in the average
> - Use interaction table/plot and ANOVA with interaction terms
> - Hierarchy principle: keep main effects of terms in a significant interaction
> - Confirm optimum with a verification run

---
## 5. Main-Effect and Interaction Plots; Reading Effect Plots
> 🟠 Tier 2 · _Key points:_ Parallel lines = no interaction; crossing or diverging lines = interaction; Pareto/normal plot of effects

### Definition
- **Main-effects plot:** mean response at each factor level, joined by a line; steeper slope = bigger effect. Horizontal = no effect (but see interactions).
- **Interaction plot:** mean response vs factor A with separate lines for levels of B. **Parallel lines: no interaction. Non-parallel lines: interaction; crossing lines: strong (disordinal) interaction**, where the best level of one factor flips with the level of the other.
- **Pareto chart of effects** (standardised effect against the critical $t$ line) and **normal probability plot of effects** (Daniel plot): effects falling off the straight line through the near-zero cluster are active.
- **Cube plot** displays 2³ cell means at the corners.
- **Residual plots:** residual vs fitted (funnel shape signals a transformation), normal plot, vs run order (time drift).
- **Optimisation:** with multiple responses use desirability functions, or overlay contour plots.
Software: Minitab, JMP, Design-Expert, Python (`statsmodels`, `matplotlib`, `pyDOE`). Plotting best practice is in [[065 Data Visualization (Matplotlib-Seaborn-Plotly)]].

### Example
From the moulding study, the interaction plot of mean warpage against A (230 vs 250) has two lines: for B = 60 bar the line rises from 21.5 to 30.0; for B = 80 bar it falls from 25.0 to 17.0. The lines cross, a pure picture of $AB=-8.25$. The main-effects plot of A is flat (mean 23.25 at 230 C vs 23.50 at 250 C) because up-slope and down-slope average out. The Pareto chart ranks AB (t = 11.7), B (6.7), C (4.6) above the critical $t=2.31$, while A, AC, BC, ABC fall below it. A plot reading is therefore: set B and A high together, lengthen cooling.

### In the news
See news box. Software draws these plots in one click; the interview skill is reading them correctly.

### Interview angle
> [!question] How it is asked
> "What does it mean if lines cross in an interaction plot?"

> [!tip] Strong answer includes
> - Effect of one factor depends on the other; crossing = best level flips
> - Do not interpret main effects in isolation
> - Use a Pareto or normal plot of effects to identify active terms
> - Check residuals before trusting conclusions

---
## 6. Fractional Factorials: Aliasing and Resolution
> 🟠 Tier 2 · _Key points:_ 2^(k−p) runs; generators define aliasing; Resolution III/IV/V; sparsity of effects

### Definition
A **fractional factorial** $2^{k-p}$ runs only $1/2^p$ of the full design, buying economy by **confounding (aliasing)** effects. Build it by assigning extra factors to interaction columns (**generators**), such as $D=ABC$ in a $2^{4-1}$ design. The **defining relation** (for example $I=ABCD$) shows every alias: multiply any effect by the defining word (squares vanish). **Resolution** is the length of the shortest word in the defining relation:
- **Resolution III:** main effects aliased with two-factor interactions (A = BC). Used for screening many factors.
- **Resolution IV:** main effects clear of two-factor interactions, but 2fi aliased with each other (AB = CD). Good for screening with some safety.
- **Resolution V:** main effects and 2fi clear of one another (2fi aliased with 3fi). Preferred for characterisation.

Common designs: $2^{3-1}_{III}$ (4 runs, $I=ABC$); $2^{4-1}_{IV}$ (8 runs, $I=ABCD$); $2^{5-1}_{V}$ (16 runs, $I=ABCDE$); $2^{7-4}_{III}$ (8 runs for 7 factors); $2^{6-2}_{IV}$ (16 runs). Also **Plackett-Burman** (12 runs for up to 11 factors, resolution III, with partial aliasing). Strategy: screen with a fraction, then **fold over** (rerun with signs reversed) to de-alias, or add runs for the important factors. Assumes sparsity of effects, hierarchy and heredity.

### Example
Take the moulding data and run only the half-fraction where $C=AB$ (defining relation $I=ABC$; 8 of 16 runs). The estimates become sums of aliased effects: $\hat A=A+BC=0.25-0.75=-0.50$; $\hat B=B+AC=-4.75+0.25=-4.50$; and **$\hat C=C+AB=-3.25-8.25=-11.50$**. The fraction would claim cooling time has a huge effect (−11.5) when the true driver is the AB interaction (−8.25) and cooling is only −3.25. A resolution III design cannot tell these apart; a fold-over (the complementary half with $C=-AB$) would give $C-AB$ and separate them. Run counts: full 2⁷ = 128 runs; a $2^{7-4}$ screen uses 8. Cost at ₹5,000 per run: ₹6.4 lakh vs ₹40,000; screening risk is aliasing, so follow up with confirmatory runs.

### In the news
See news box. Adaptive tools lean on the same sparsity logic: most factors do little, so spend runs on the few that matter.

### Interview angle
> [!question] How it is asked
> "What is aliasing and what does resolution IV mean?"

> [!tip] Strong answer includes
> - Fraction confounds effects; defining relation shows alias chains
> - Resolution III/IV/V meaning with examples
> - Assumption: higher-order interactions negligible; fold-over to resolve
> - Practical sequence: screen, then follow up and confirm

---
## 7. Blocking in Factorials, Confounding and Centre Points
> 🟠 Tier 2 · _Key points:_ Confound the highest interaction with blocks; centre points test curvature and give pure error

### Definition
**Blocking a factorial:** when 8 runs of a 2³ cannot all be done in one batch, split into 2 blocks of 4 by confounding the three-factor interaction with the block: block 1 has runs with $ABC=-1$, block 2 with $ABC=+1$. The block effect is then inseparable from ABC, which is usually negligible, while all main effects and two-factor interactions are clear. For larger designs, partial confounding spreads the loss across replicates.

**Centre points:** add runs at the midpoint of all quantitative factors (coded 0). They (1) estimate **pure error** without replicating every corner, (2) provide a test for **curvature**: $F=\dfrac{n_Fn_C(\bar y_F-\bar y_C)^2/(n_F+n_C)}{s_C^2}$ with 1 and $n_C-1$ df, and (3) detect drift if spread over time. If curvature is significant, augment to a response-surface design (sub-topic 8). Centre points cannot say which factor is curved.

### Example
Blocking: in the moulding experiment, blocks defined by the sign of ABC have means 23.50 (ABC = −1) and 23.25 (+1); the ABC/block effect is −0.25, negligible, so splitting the 8 runs into two shifts costs nothing for the other six effects. Curvature: the 2² yield study had factorial mean $\bar y_F=27.50$ (12 runs). Add 5 centre runs at 170 C and 1.5% catalyst giving 27.5, 28.2, 26.9, 28.6, 27.1 (mean 27.66, $s_C^2=0.523$). Curvature $F=\frac{12\cdot5\cdot(27.5-27.66)^2/17}{0.523}=\mathbf{0.17}$ (p = 0.70): no evidence of curvature, so the first-order (planar) model is adequate and steepest ascent is the sensible next step.

### In the news
See news box. Adaptive optimisers cope with curvature internally by fitting flexible surrogate models; in classical DOE we test for it explicitly with centre points.

### Interview angle
> [!question] How it is asked
> "What are centre points for in a factorial experiment, and what do you do if curvature is significant?"

> [!tip] Strong answer includes
> - Curvature test, pure error estimate, drift check
> - If significant, add axial points for a CCD to fit quadratic terms
> - Blocking with a high-order interaction confounded
> - Centre points apply to continuous factors only

---
## 8. Response Surface Methodology: Steepest Ascent and Optimisation
> 🟠 Tier 2 · _Key points:_ Sequential: screen → steepest ascent → CCD/BBD → quadratic model → stationary point → confirm

### Definition
**RSM** finds optimal factor settings sequentially. (1) Fit a **first-order model** $\hat y=b_0+\sum b_ix_i$ from a 2^k (or fraction) with centre points. (2) If curvature is negligible, move along the **path of steepest ascent** (maximisation) or descent: step $\Delta x_i\propto b_i$ in coded units, running trials along the path until the response stops improving. (3) Near the optimum, curvature appears: use a **central composite design (CCD)** (factorial + $2k$ axial points at $\pm\alpha$ + centre points; $\alpha=(2^k)^{1/4}$ for rotatability: 1.414 for k=2, 1.682 for k=3) or **Box-Behnken** (3 levels, no corner runs, 15 runs for k=3). (4) Fit a **second-order model** $\hat y=b_0+\sum b_ix_i+\sum b_{ii}x_i^2+\sum\sum b_{ij}x_ix_j$ and find the **stationary point** $x_s=-\tfrac12\mathbf B^{-1}\mathbf b$; its nature comes from the eigenvalues of $\mathbf B$ (all negative: maximum; all positive: minimum; mixed: saddle). Use contour plots and canonical analysis. Multiple responses: overlay contours or desirability functions. Quality context: [[008 Six Sigma & Quality Tools]], [[092 Sampling & Experimental Design]] for the survey view.

### Example
Steepest ascent from the yield study (coded effects of the 2² factorial give $b_1=A/2=+4.17$ for temperature, $b_2=B/2=-2.50$ for catalyst). Centre (170 C, 1.5%), half-ranges 10 C and 0.5%. Take step 1 coded unit in temperature, so catalyst steps $-2.5/4.17=-0.60$ coded.

| Step | Temp (C) | Catalyst (%) | Predicted yield |
|---|---|---|---|
| 0 | 170 | 1.50 | 27.5 |
| 1 | 180 | 1.20 | 33.2 |
| 2 | 190 | 0.90 | 38.8 |
| 3 | 200 | 0.60 | 44.5 |

Run real trials at each step; stop when yield drops (the linear model is only local). Suppose the best is near step 3: then run a CCD around it (k=2: 4 factorial + 4 axial at $\pm1.414$ + 5 centre = 13 runs) and fit the quadratic. Illustration of a fitted surface $\hat y=80+4x_1+2x_2-3x_1^2-2x_2^2+1.5x_1x_2$: $\mathbf B=\begin{pmatrix}-3&0.75\\0.75&-2\end{pmatrix}$, stationary point $x_s=(0.87,\,0.83)$ coded, predicted maximum $\hat y=82.6$; eigenvalues $-3.40$ and $-1.60$ are both negative, so it is a true maximum.

### In the news
See news box. Bayesian optimisation in Ax plays the role of RSM when the number of factors and runs is large, choosing each next run to balance learning and improvement.

### Interview angle
> [!question] How it is asked
> "Describe how you would optimise a process with 3 continuous factors from scratch."

> [!tip] Strong answer includes
> - Screen with a fraction, then factorial with centre points, steepest ascent, CCD or Box-Behnken, optimum, confirmation
> - Curvature test as the trigger for second-order design
> - Stationary point and its type (max/min/saddle)
> - Stay within operating limits; consider several responses

---
## 9. Taguchi Methods: Orthogonal Arrays, S/N Ratios and Loss Function
> 🟠 Tier 2 · _Key points:_ Robust design; OA (L4, L8, L9, L18); S/N ratios (larger/smaller/nominal); loss = k(y−m)²

### Definition
**Taguchi's robust design** seeks settings of controllable factors that make performance insensitive to **noise** (material variation, temperature, wear, customer usage), not just on target. Elements:
- **Quality loss function:** loss grows quadratically as the response departs from target $m$: $L(y)=k(y-m)^2$, $k=A_0/\Delta_0^2$ ($A_0$ = loss at tolerance limit $\Delta_0$). Meeting spec is not the same as zero loss.
- **Orthogonal arrays (OA):** compact fractional designs; **L4** (up to 3 two-level factors), **L8** (7 two-level), **L9** (4 three-level factors in 9 runs), **L12** (11 two-level, screening), **L16**, **L18** (one 2-level + seven 3-level), **L27**. Control factors in the **inner array**, noise factors in an **outer array**.
- **Signal-to-noise (S/N) ratio**, maximised in every case: larger-the-better $-10\log_{10}\!\big(\tfrac1n\sum y_i^{-2}\big)$; smaller-the-better $-10\log_{10}\!\big(\tfrac1n\sum y_i^{2}\big)$; nominal-the-best $10\log_{10}(\bar y^2/s^2)$.
- Analyse **level means of S/N** to select the best level of each factor (and means to adjust the mean on target), then predict and confirm.
Critics note that Taguchi's S/N ratios can confound mean and variance and OAs often ignore interactions; modern practice combines orthogonal designs with response-surface models on mean and variance. Taguchi-style arrays remain common in manufacturing quality and engineering teams.

### Example
Loss function: spec limit ±0.5 mm, scrap/rework cost ₹200 per part at the limit: $k=200/0.5^2=\text{₹}800$ per mm². A part 0.2 mm off target costs $800\times0.04=\text{₹}32$ even though it is "in spec".
OA example (L4, larger-the-better): adhesive pull-off force (N) for a rubber-to-metal bond, factors A (primer type), B (cure temperature), C (cure time), two readings per run:

| Run | A | B | C | Force | S/N (dB) |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 42, 45 | 32.75 |
| 2 | 1 | 2 | 2 | 55, 58 | 35.03 |
| 3 | 2 | 1 | 2 | 48, 44 | 33.23 |
| 4 | 2 | 2 | 1 | 61, 64 | 35.91 |

Level means of S/N: A1 33.89, A2 34.57; B1 32.99, **B2 35.47**; C1 34.33, C2 34.13. B is the dominant factor (range 2.48 dB), A is modest (0.68), and C is negligible (0.20 dB). Best combination A2 B2 C1 (the tested run 4, S/N 35.91, mean force 62.5 N). With only 4 runs and 3 factors the design is saturated: no error df and no interaction estimates; use confirmation runs and, if needed, an L8.

### In the news
See news box. Taguchi's robust-design thinking, designing for noise rather than only for the mean, still shapes how engineers specify tests in adaptive platforms.

### Interview angle
> [!question] How it is asked
> "What is a signal-to-noise ratio in Taguchi methods and how do you use an orthogonal array?"

> [!tip] Strong answer includes
> - Robustness: maximise S/N, choose by level means, confirm
> - Three S/N forms and when each applies
> - OA = fractional factorial with balanced columns; inner/outer arrays
> - Fair critique: interactions ignored, S/N confounding; compare with factorial/RSM

---
## 10. Split-Plot and Other Restricted-Randomisation Designs
> 🟠 Tier 2 · _Key points:_ Hard-to-change factor on whole plots; two error terms; the wrong analysis inflates significance

### Definition
When a factor is **hard or costly to change** (oven temperature, line speed, a mould swap), complete randomisation is impractical, so runs are grouped: the hard factor is applied to **whole plots** and the easy factors to **subplots** within each. The origin is agricultural (irrigation applied to whole fields, varieties to plots inside), but it is common in industry: semiconductor furnaces, tyre curing presses, heat treatment, paint lines. Key features:
- **Two error terms:** the whole-plot error (variation between whole-plot runs) tests the hard-to-change factor; the subplot error tests the easy factors and the interaction. The subplot factors are usually estimated more precisely.
- Analyse as a **mixed model** (random whole-plot effect) or the split-plot ANOVA; treating it as a fully randomised design (single error) makes the hard-to-change factor look falsely significant because the effective replication is the number of whole plots, not observations.
- Related: **strip-plot** (two hard-to-change factors crossed), **nested/hierarchical** designs (batches within suppliers), repeated-measures designs.

### Example
Heat-treatment experiment: furnace temperature (3 levels, hard to change) and coating type (3 levels, easy) with 4 furnace runs per temperature, each loaded with all 3 coatings: 12 whole plots × 3 = 36 parts.

| Source | df | Tested against |
|---|---|---|
| Temperature | 2 | Whole-plot error |
| Whole-plot error (runs within temperature) | $3\times3=9$ | |
| Coating | 2 | Subplot error |
| Temperature × Coating | 4 | Subplot error |
| Subplot error | $3\times2\times3=18$ | |
| Total | 35 | |

The ignorance cost: a naive one-way analysis would use error df of about 27 and treat all 36 parts as independent, but temperature has only 12 independent runs, so its test should rest on 9 error df. Furnace runs cost ₹40,000 each, coating changes are free, so the split-plot is also the cheaper design.

### In the news
See news box. Hard-to-change factors are a reminder that real experiments carry constraints; adaptive platforms must be configured around them, and classical designs encode them through the split-plot structure.

### Interview angle
> [!question] How it is asked
> "A factor is expensive to change and cannot be fully randomised. How do you design and analyse the experiment?"

> [!tip] Strong answer includes
> - Split-plot with whole plots and subplots; restricted randomisation
> - Two error terms or a mixed model; effective replication is the whole plots
> - Trade-off: precision on easy factors, less on the hard factor
> - Compare with fully randomised design and cost

---
## 11. Executed Python Example: Factorial Analysis
> 🟠 Tier 2 · _Key points:_ statsmodels ols with coded factors; effect = 2×coefficient; ANOVA table; check residuals

### Definition
In Python, code the factors as −1/+1, fit a linear model with all interactions using `statsmodels`, double the coefficients to obtain effects and use `anova_lm(typ=2)` for sums of squares. For design generation use `pyDOE2`/`pyDOE3` (`ff2n`, `fracfact`, `ccdesign`, `bbdesign`) or `itertools.product`. For adaptive optimisation use `ax-platform` (Bayesian). Add residual diagnostics (`qqplot`, residual vs fitted). Excel (Data Analysis ANOVA plus manual contrasts), Minitab and JMP give equivalent output. See also [[067 Statistical Analysis in Python]] and [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]].

### Example
Executed code for the 2³ moulding study of sub-topic 4 (16 runs):

```python
import pandas as pd, statsmodels.api as sm
from statsmodels.formula.api import ols

levels = [(-1,-1,-1),(1,-1,-1),(-1,1,-1),(1,1,-1),(-1,-1,1),(1,-1,1),(-1,1,1),(1,1,1)]
rep1 = [22,32,26,18,19,28,24,14]; rep2 = [24,30,28,20,21,30,22,16]
rows = [(a, b, c, y) for (a, b, c), y1, y2 in zip(levels, rep1, rep2) for y in (y1, y2)]
df = pd.DataFrame(rows, columns=["A", "B", "C", "warpage"])

m = ols("warpage ~ A * B * C", data=df).fit()
print((2 * m.params.drop("Intercept")).round(2))      # effects
print(sm.stats.anova_lm(m, typ=2).round(3))
print(round(m.rsquared, 3))
```

Output: effects A 0.25, B −4.75, C −3.25, AB −8.25, AC 0.25, BC −0.75, ABC −0.25; ANOVA F for AB = 136.1 (p < 0.001), B = 45.1, C = 21.1, others not significant; residual SS = 16.0 on 8 df; $R^2=0.962$. Reduced model `warpage ~ A + B + C + A:B` keeps $R^2=0.956$ with residual sd 1.31, so the three negligible terms can be dropped. Predicted warpage at A, B, C all high: 15.0 (observed cell mean 15.0). Always follow with a confirmation run at the chosen setting.

### In the news
See news box. The same `statsmodels` workflow validates the classical designs that tools such as Ax automate and extend.

### Interview angle
> [!question] How it is asked
> "How would you analyse a 2³ experiment in Python or Excel?"

> [!tip] Strong answer includes
> - Coded factors, full model with interactions, effects = 2×coefficients, ANOVA
> - Drop non-significant high-order terms, check residuals
> - Report optimum with confirmation run and prediction interval
> - Mention alternatives: Minitab/JMP, pyDOE for design generation

---
## 12. DOE in a Six Sigma Project: Steps, Sample Size and Pitfalls
> 🟠 Tier 2 · _Key points:_ DOE sits in Improve; check MSA first; screen → optimise → confirm → control

### Definition
In a DMAIC project (see [[008 Six Sigma & Quality Tools]] and [[017 Process Management & Optimization]]) DOE belongs in **Improve**: it converts "we think X matters" from Analyse into quantified settings. Steps:
1. **Define** problem, response(s) (CTQs) and objective: maximise, minimise, hit target, reduce variation.
2. **Validate measurement:** run Gauge R&R before experimenting (see [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]]); noisy gauges hide effects.
3. **Select factors and levels** from fishbone/FMEA/regression (see [[090 Regression Analysis]]); levels bold but safe.
4. **Choose design:** many factors, screening (fraction, Plackett-Burman); few factors, full factorial; optimisation, CCD/BBD; robustness, Taguchi/crossed arrays.
5. **Plan resources:** runs, replicates, blocks, randomisation, cost, who runs what; pilot run to check set-up.
6. **Run and record** randomised, with notes on anomalies; keep non-experimental variables fixed.
7. **Analyse:** effects, ANOVA, residual diagnostics, models.
8. **Interpret and optimise;** **confirm** with 3 to 5 runs at the predicted optimum; **control**: update the control plan, SOP, SPC and FMEA.
Sample size: for a 2^k with $N$ runs, $SE=2\sigma/\sqrt N$ and detectable effect $\approx2.8\,SE$ (80% power, 5% two-sided). Pitfalls: ignoring interactions, too narrow level ranges, un-randomised order, treating repeated measurements as replicates, optimising a model outside its range, no confirmation, many responses without trade-offs, and failing to involve process owners.

### Example
A tyre-curing line has curing-time variation. Plan: 4 suspected factors (temperature, pressure, time, mould age); $\sigma=2$ (from a Gauge R&R-approved test). A $2^{4-1}_{IV}$ with 8 runs and 2 replicates (16 runs): $SE=2\times2/\sqrt{16}=1.0$, so effects of about 2.8 or more are detectable. Cost: 16 runs × ₹6,000 = ₹96,000, against a full 2⁴ with 2 replicates (32 runs, ₹1.92 lakh) or trial and error that might consume 40 runs without isolating interactions. Verification: after choosing settings, 5 confirmation runs and a capability study (see [[091 Statistical Quality Control (SQC)]]).

### In the news
See news box. NIST's guidance to fix objectives, factors and a detailed plan in advance is the same "plan before you run" discipline expected in an Improve-phase DOE.

### Interview angle
> [!question] How it is asked
> "Walk me through a DOE you would run to reduce defects on a line."

> [!tip] Strong answer includes
> - Link to project CTQ; validate the measurement system
> - Screening then optimisation, randomisation, replication, blocking
> - Analysis (ANOVA, effects, residuals), confirmation run, control plan
> - State resource and cost trade-offs, with a tangible outcome

---
## 13. ⭐ Advanced: DOE vs A/B Testing, Optimal Designs and Adaptive Experimentation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Online A/B tests and industrial DOE share randomisation and inference but differ:
- **Many variants and factors:** multivariate (factorial) web tests let you estimate interactions (button colour × headline) with the same traffic, via full or fractional factorial assignment.
- **Run cost:** industrial runs cost hours and rupees, so the design must be efficient; online units are cheap, so power comes from volume.
- **Optimal designs** (D-, I-optimal) are computer-generated when constraints make standard designs impossible (irregular regions, mixtures, constraints between factors, unequal level counts). D-optimal minimises the volume of the parameter confidence region ($|X'X|$ maximal).
- **Mixture experiments:** components sum to 100% (blends, fuel, concrete, paint); special simplex-lattice designs.
- **Computer experiments/surrogates:** deterministic simulations (CFD, FEA) are explored with space-filling designs (Latin hypercube) and Gaussian-process surrogates.
- **Adaptive/Bayesian experimentation:** choose the next experiment from a posterior surrogate (Bayesian optimisation, bandits), as in Ax; efficient for many factors with expensive runs; weaker for clean effect estimates (see [[210 Bayesian Statistics for Decisions]] and [[214 Causal Inference & Experimentation Beyond A-B Tests]]).
Sequential strategy for most business problems: screening design to cut factors, factorial/RSM on the vital few, confirmation, then monitoring.

### Example
A growth team wants to test headline (2), image (2), CTA colour (2) and layout (2): 16 combinations. A full factorial would need all 16 cells with traffic split 16 ways; a $2^{4-1}_{IV}$ half-fraction needs 8 cells with each main effect estimated from all traffic and 2fi aliased in pairs (AB with CD, and so on). If baseline conversion is 4% and 10 lakh visitors are available, each of 8 cells receives 125,000 visitors (SE of an effect on conversion about $2\sqrt{0.04\times0.96/10^6}=0.039$ pp, so effects of about 0.11 pp are detectable at 80% power). A one-factor-at-a-time sequence of four A/B tests would need four separate periods and could not reveal interactions. Calculation: $2\times\sqrt{0.0384/1{,}000{,}000}=0.000392$; ×2.8 = 0.11 pp.

### In the news
See news box. Meta's Ax documentation describes support for Bayesian optimisation alongside A/B tests and field experiments, i.e. both the classical and adaptive styles of this sub-topic.

### Interview angle
> [!question] How it is asked
> "When would you use a factorial or a Bayesian optimisation approach instead of separate A/B tests?"

> [!tip] Strong answer includes
> - Several factors and interactions, limited traffic or expensive runs
> - Fractional designs and their aliasing risk
> - Adaptive methods for many continuous factors, with confirmation by a randomised test
> - Honest limits: contamination, novelty effects, interference between units
