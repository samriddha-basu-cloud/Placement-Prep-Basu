---
tags: [statistics, tier2]
area: Statistics
topic: "Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis"
tier: Tier 2
roles: Analytics / Consulting / PM
status: complete
subtopics: 13
---
# Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis

⬅ [[206 Non-Parametric Tests]] · [[_Index - Statistics|Statistics]] · [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / Consulting / PM

## Sub-topics in this note
1. [[#1. Multivariate Data, Covariance and Mahalanobis Distance]]
2. [[#2. Principal Component Analysis: Eigen Decomposition and a Worked 2D Example]]
3. [[#3. PCA in Practice: How Many Components and How to Read Them]]
4. [[#4. Factor Analysis: Model, Loadings, Communalities and Rotation]]
5. [[#5. Is the Data Suitable? KMO, Bartlett's Test and Cronbach's Alpha]]
6. [[#6. Hierarchical Cluster Analysis]]
7. [[#7. K-Means Clustering and Segmentation in Marketing Research]]
8. [[#8. Discriminant Analysis]]
9. [[#9. MANOVA (Multivariate Analysis of Variance)]]
10. [[#10. Conjoint Analysis for Pricing and Feature Trade-offs]]
11. [[#11. Multidimensional Scaling and Perceptual Maps]]
12. [[#12. Correspondence Analysis]]
13. [[#13. ⭐ Advanced: Interpretation Rules, Pitfalls and Choosing a Method]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Multivariate methods behind composite indices, wealth quintiles and pricing studies
> **Financial inclusion index built with two-stage PCA (2025).** A 2025 SAGE paper (Annemalla and Kasturi) constructs a composite Financial Inclusion Index for all Indian states over 2000-2020 using two-stage principal component analysis on RBI and EPW Research Foundation data, across the dimensions of availability, penetration and usage. It finds Goa, Kerala and Tamil Nadu high, and Mizoram, Nagaland, Manipur and Meghalaya low. This is the standard consulting use of PCA: collapse many correlated indicators into one defensible score. ([SAGE abstract](https://journals.sagepub.com/doi/abs/10.1177/09721509251356954))
>
> **The DHS wealth index is a PCA score.** The Demographic and Health Surveys programme (the family of surveys that includes India's NFHS) builds household wealth from asset indicators with principal components analysis in three steps (common indicators, separate urban and rural scores, then a combined national index), producing a score with mean zero and standard deviation one that is cut into five quintiles. Wealth quintiles in much India health and market research come from this recipe. ([DHS Program guide](https://dhsprogram.com/data/Guide-to-DHS-Statistics/Wealth_Quintiles.htm))
>
> **Choice experiments for Indian EV pricing (published 2021, still the reference).** A study of over 1,000 Indian consumers using a discrete choice experiment reported willingness to pay of roughly US$7-40 for one extra km of range (at 200 km) and US$10-34 to cut fast-charging time by one minute, and that modelling reference dependence gave more realistic estimates. The paper predates this note's 2024-26 window; it is cited because it is the cleanest public example of conjoint-style trade-off research on Indian buyers. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0140988321002462))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Multivariate Data, Covariance and Mahalanobis Distance
> 🟠 Tier 2 · _Key points:_ Mean vector, covariance matrix $\mathbf S$, correlation matrix $\mathbf R$; standardise first; Mahalanobis distance

### Definition
Multivariate data record $p$ variables on each of $n$ units. Summaries: the mean vector $\bar{\mathbf x}$, the covariance matrix $\mathbf S$ (variances on the diagonal, covariances off it) and the correlation matrix $\mathbf R=D^{-1/2}\mathbf S D^{-1/2}$. Because covariances depend on units, standardise (use $\mathbf R$) before PCA, factor analysis or clustering unless variables share units. The **Mahalanobis distance** accounts for scale and correlation:

$$D^2=(\mathbf x-\bar{\mathbf x})^\top\mathbf S^{-1}(\mathbf x-\bar{\mathbf x})$$

Under multivariate normality $D^2\sim\chi^2_p$ approximately, so it flags multivariate outliers that look ordinary variable by variable. Hotelling's $T^2$ is the multivariate analogue of the t-test. Basics of means, SDs and correlation are in [[086 Descriptive Statistics]]; regression with many correlated predictors (multicollinearity) is in [[090 Regression Analysis]].

### Example
Six stores: footfall $x_1$ (thousand/day) = 2, 4, 6, 8, 10, 12; sales $x_2$ (₹ lakh/day) = 3, 5, 5, 9, 8, 12. Means 7 and 7. $\mathbf S=\begin{pmatrix}14&11.6\\11.6&10.8\end{pmatrix}$, correlation $r=11.6/\sqrt{14\times10.8}=0.943$. A new store with footfall 10 and sales 3: Euclidean distance from the mean is 5, unremarkable, but $D^2=36.0$, far beyond the $\chi^2_2$ 99.9% cut-off of 13.8: high footfall with very low sales breaks the correlation pattern. The six original stores have $D^2$ between 0.8 and 2.5.

### In the news
See news box. Index construction (financial inclusion, wealth) starts by standardising indicators and examining their correlation matrix.

### Interview angle
> [!question] How it is asked
> "Why does a point inside the range of every variable still count as an outlier?"

> [!tip] Strong answer includes
> - Correlation structure: unusual combination, not unusual values; Mahalanobis distance captures it
> - Standardise before distance-based methods
> - Mention use for fraud/anomaly flags and for robust covariance in small samples

---
## 2. Principal Component Analysis: Eigen Decomposition and a Worked 2D Example
> 🟠 Tier 2 · _Key points:_ Eigenvectors of $\mathbf S$ (or $\mathbf R$) are PCs; eigenvalue = variance of PC; scores = centred data x eigenvectors

### Definition
PCA finds orthogonal directions (principal components) of maximum variance. With $\mathbf S=\mathbf V\Lambda\mathbf V^\top$, the columns of $\mathbf V$ are the loadings (directions) and $\lambda_j$ the variance captured by component $j$; scores are $\mathbf z=\mathbf V^\top(\mathbf x-\bar{\mathbf x})$. Total variance is preserved: $\sum\lambda_j=\text{trace}(\mathbf S)$ (or $p$ for $\mathbf R$). Equivalent to the singular value decomposition of the centred data matrix. Use it to reduce dimension, remove multicollinearity before regression, compress features, and build indices. PCA is descriptive: no distributional model, no noise term (contrast factor analysis).

### Example
Using the six stores of sub-topic 1. Eigenvalues of $\mathbf S$: $\lambda_1=24.11$, $\lambda_2=0.69$ (sum 24.80 = 14 + 10.8). PC1 explains $24.11/24.80=97.2\%$ of variance. PC1 direction $(0.754,\,0.657)$ (signs are arbitrary), so PC1 $=0.754(x_1-7)+0.657(x_2-7)$, an overall "store size" axis. PC1 scores: -6.40, -3.58, -2.07, 2.07, 2.92, 7.05; PC2 scores are all within $\pm1.3$. Standardised (correlation) PCA: eigenvalues $1+r=1.943$ and $1-r=0.057$ with equal loadings $(0.707,0.707)$: for two variables the PCs always split into "sum" and "difference" axes. Keep one component and the six stores can be ranked on one number with only 2.8% variance lost.

```python
from sklearn.decomposition import PCA
import numpy as np
X = np.array([[2,3],[4,5],[6,5],[8,9],[10,8],[12,12]], float)
p = PCA().fit(X); print(p.explained_variance_, p.explained_variance_ratio_)
# [24.11  0.69]   [0.972 0.028]
```

### In the news
See news box. The financial inclusion index and the DHS wealth index are PC1-type scores; the first component is the weighted composite and its loadings are the weights.

### Interview angle
> [!question] How it is asked
> "Explain PCA to a non-technical manager and tell me when you would not use it."

> [!tip] Strong answer includes
> - Plain language: new axes that capture most variation with fewer numbers
> - Mechanics: standardise, covariance matrix, eigenvectors/eigenvalues, keep top components
> - Limits: linear only, components hard to interpret, scale-sensitive, PCs maximise variance not predictive power
> - Links to [[097 Unsupervised Learning]] and feature engineering in [[094 ML Fundamentals & Workflow]]

---
## 3. PCA in Practice: How Many Components and How to Read Them
> 🟠 Tier 2 · _Key points:_ Scree/elbow, Kaiser eigenvalue > 1 (on $\mathbf R$), cumulative variance 70-80%+, interpretability; loadings above about 0.4

### Definition
Choosing $k$: (1) **Kaiser rule**, keep components with eigenvalue above 1 (correlation matrix; crude, tends to over/under-select); (2) **scree plot**, keep components before the elbow; (3) **cumulative variance**, e.g. at least 70-80%; (4) **parallel analysis** (compare with eigenvalues from random data, the most defensible); (5) interpretability and the purpose. Interpret a component by its **loadings** (correlations between variables and components when using $\mathbf R$): variables with large absolute loadings define the component; signs show direction. Standardise variables; a variable in rupees would otherwise dominate. Do not interpret tiny components; do not use PCA scores as if they were observed measurements without noting they are weighted blends.

### Example
Six survey items (Price, Value, Offers, Quality, Brand, Service), 300 respondents (simulated, NumPy seed 3). Correlation-matrix eigenvalues: 2.685, 1.606, 0.495, 0.454, 0.404, 0.354. Variance explained: 44.8%, 26.8%, then 8.3% and below; cumulative 44.8%, 71.5%, 79.8%, 87.4%, 94.1%, 100%. Kaiser keeps two components (71.5% cumulative), and the scree plot has an elbow after component 2. Items 1-3 load on one component, items 4-6 on the other, which suggests the two-factor structure studied in sub-topic 4.

### In the news
See news box. Index builders typically keep only PC1 (or a few) and report variance explained; a PC1 that explains little signals that a single index is not a faithful summary.

### Interview angle
> [!question] How it is asked
> "You ran PCA on 30 KPIs. How do you decide how many components to keep?"

> [!tip] Strong answer includes
> - Scree plot, cumulative variance threshold, parallel analysis, business interpretability
> - Check loadings are sensible; name components
> - Standardise inputs; mention PCA on skewed variables (log-transform first)
> - Say what PCA does not do: no causal meaning, not feature selection

---
## 4. Factor Analysis: Model, Loadings, Communalities and Rotation
> 🟠 Tier 2 · _Key points:_ $\mathbf x=\Lambda\mathbf f+\boldsymbol\varepsilon$; communality $h_j^2=\sum_k\lambda_{jk}^2$; varimax rotation; EFA vs CFA

### Definition
**Exploratory factor analysis (EFA)** models observed variables as driven by a few latent factors plus unique noise:

$$\mathbf x=\boldsymbol\mu+\Lambda\mathbf f+\boldsymbol\varepsilon,\qquad \text{Cov}(\mathbf x)=\Lambda\Lambda^\top+\Psi$$

$\Lambda$ holds the **loadings**; the **communality** $h_j^2=\sum_k\lambda_{jk}^2$ is the share of variable $j$'s variance explained by common factors (the remainder is **uniqueness**). Unlike PCA, which explains total variance, FA explains the shared variance and separates noise. Extraction by principal-axis or maximum likelihood ([[205 Sampling Distributions & Estimation]] covers MLE). **Rotation** gives a simpler structure: **varimax** (orthogonal, factors uncorrelated) is the default; **promax/oblimin** (oblique) allow correlated factors, often more realistic for attitudes. Confirmatory factor analysis (CFA) tests a pre-specified structure. Convention: loadings above 0.4-0.5 are meaningful; communalities above about 0.5 are comfortable; each factor needs at least 3 items.

### Example
Same six items, two factors, varimax rotation (scikit-learn `FactorAnalysis(2, rotation='varimax')` on standardised data). Loadings (the sign of a factor is arbitrary):

| Item | Factor 1 | Factor 2 | Communality |
|---|---|---|---|
| Price | 0.77 | 0.10 | 0.61 |
| Value | 0.75 | 0.19 | 0.60 |
| Offers | 0.71 | 0.06 | 0.51 |
| Quality | 0.08 | 0.75 | 0.58 |
| Brand | 0.19 | 0.74 | 0.58 |
| Service | 0.10 | 0.73 | 0.54 |

Factor 1 is "price and value sensitivity" (Price, Value, Offers); Factor 2 is "quality and brand experience". Each item loads high on one factor and low on the other: clean simple structure. Factor scores can then be used in segmentation or regression.

### In the news
See news box. Composite indices in the news box use PCA; survey instruments (satisfaction, NPS drivers) use factor analysis to check that items measure what the label claims.

### Interview angle
> [!question] How it is asked
> "What is the difference between PCA and factor analysis?"

> [!tip] Strong answer includes
> - PCA: variance maximisation, components are exact combinations of variables; FA: latent variable model with unique error, explains correlations
> - Rotation to make factors interpretable; orthogonal vs oblique
> - Use PCA for compression and indices, FA for measurement and constructs
> - Name the factors and check reliability (Cronbach alpha)

---
## 5. Is the Data Suitable? KMO, Bartlett's Test and Cronbach's Alpha
> 🟠 Tier 2 · _Key points:_ Bartlett: R is not identity; KMO > 0.6 acceptable; $\alpha$ > 0.7 reliable

### Definition
**Bartlett's test of sphericity** tests H0: the correlation matrix is the identity (no correlations, nothing to factor): $\chi^2=-\left(n-1-\frac{2p+5}{6}\right)\ln|\mathbf R|$ with $p(p-1)/2$ d.f. A significant result is needed but easy to obtain with large $n$. **Kaiser-Meyer-Olkin (KMO)** compares correlations with partial correlations: values near 1 mean factors can explain the correlations; common labels: below 0.5 unacceptable, 0.5-0.7 mediocre, 0.7-0.8 good, 0.8-0.9 great, above 0.9 superb. Also check per-item MSA, sample size (rule of thumb at least 5-10 cases per variable, ideally 200+), and **Cronbach's alpha** $\alpha=\frac{k}{k-1}\left(1-\frac{\sum\sigma_i^2}{\sigma_{total}^2}\right)$ for scale reliability (0.7 or more acceptable).

### Example
Six-item survey, $n=300$: $|\mathbf R|$ gives Bartlett $\chi^2=584.4$ on 15 d.f., $p<10^{-100}$: reject identity. KMO $=0.73$: good enough to proceed. Cronbach's alpha: items 1-3 give 0.797; items 4-6 give 0.796, both acceptable. If an item had MSA below 0.5 or no loading above 0.4 you would drop it and re-run.

### In the news
See news box. Index and wealth-score methodologies document item selection and reliability checks for exactly this reason: a PCA score is only as defensible as its inputs.

### Interview angle
> [!question] How it is asked
> "Before running factor analysis, what checks do you do?"

> [!tip] Strong answer includes
> - Correlation matrix inspection, Bartlett (significant), KMO (above about 0.6)
> - Sample size, missing data, outliers, Likert scale treated as roughly continuous (or polychoric correlations)
> - Reliability with Cronbach alpha after naming factors

---
## 6. Hierarchical Cluster Analysis
> 🟠 Tier 2 · _Key points:_ Agglomerative: merge nearest clusters; linkage (single/complete/average/Ward) decides shape; dendrogram; no need to pre-set $k$

### Definition
Cluster analysis groups similar units without labels. **Agglomerative hierarchical clustering** starts with every unit alone and repeatedly merges the two closest clusters, producing a **dendrogram**; cutting at a height gives $k$ clusters. Linkage defines inter-cluster distance: **single** (nearest pair, chains), **complete** (farthest pair, compact clusters), **average**, **Ward** (minimises within-cluster variance increase; popular, favours equal-size spherical clusters). Choose a distance (Euclidean for standardised continuous data, Gower for mixed data, Jaccard for binary). Standardise variables; large jumps in merge height suggest the natural number of clusters. Cost is $O(n^2)$ memory, so it suits up to a few thousand units.

### Example
Five customers, (annual spend in ₹ thousand, visits per month): A (2,1), B (3,1), C (8,5), D (9,6), E (20,12). Euclidean distances: AB = 1.00, CD = 1.41, BC = 6.40, AC = 7.21, CE = 13.89, DE = 12.53. Merge order: A+B at height 1.00; C+D at 1.41; then {A,B} with {C,D} at 6.40 (single-link: nearest pair B-C) or 8.60 (complete-link: farthest pair A-D); finally E joins at 12.53 (single) or 21.10 (complete). The big final jump isolates E, a high-value customer. Cutting after the first two merges gives three segments: {A,B} light users, {C,D} regulars, {E} heavy user. Python: `scipy.cluster.hierarchy.linkage(X, 'ward')` then `fcluster`.

### In the news
See news box. Segmenting states (inclusion index scores) or households (wealth) is typically done after computing a PCA score, followed by clustering.

### Interview angle
> [!question] How it is asked
> "How would you segment customers using purchase data? Which clustering method and why?"

> [!tip] Strong answer includes
> - Choose features (RFM, category mix), standardise, transform skew
> - Hierarchical (Ward) to explore, k-means to scale; choose $k$ via dendrogram, silhouette, business usability
> - Profile clusters, check stability, and tie each segment to an action
> - Cross-reference [[097 Unsupervised Learning]]

---
## 7. K-Means Clustering and Segmentation in Marketing Research
> 🟠 Tier 2 · _Key points:_ Minimise within-cluster sum of squares; choose $k$ by elbow and silhouette; scale features; sensitive to initialisation and outliers

### Definition
**k-means** partitions $n$ points into $k$ clusters by alternating: assign each point to the nearest centroid, then recompute centroids as cluster means, until stable. It minimises $\sum_k\sum_{i\in C_k}\lVert\mathbf x_i-\boldsymbol\mu_k\rVert^2$ (inertia). Run with many random starts (k-means++ initialisation). Choose $k$ with the **elbow** in inertia, the **silhouette** score $s=(b-a)/\max(a,b)$ (between $-1$ and 1; above about 0.5 reasonable), the gap statistic, and above all business usefulness. Weaknesses: assumes roughly spherical, similar-size clusters; sensitive to scale and outliers; needs numeric features (k-modes/k-prototypes for categorical). In marketing research, clusters are profiled on demographics and behaviour to form named segments with distinct offers (see [[036 Go-To-Market Strategy]]).

### Example
150 simulated customers (annual spend in ₹ thousand, orders per month) drawn from three groups; features standardised, KMeans with 10 starts:

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
rng = np.random.default_rng(42)
X = np.vstack([rng.normal([20,3],[4,1],(60,2)), rng.normal([55,8],[6,1.5],(50,2)), rng.normal([90,15],[8,2],(40,2))])
Xs = (X - X.mean(0)) / X.std(0)
for k in range(2, 7):
    km = KMeans(k, n_init=10, random_state=0).fit(Xs)
    print(k, round(km.inertia_, 1), round(silhouette_score(Xs, km.labels_), 3))
```

| $k$ | Inertia | Silhouette |
|---|---|---|
| 2 | 85.1 | 0.641 |
| 3 | 18.5 | 0.748 |
| 4 | 14.7 | 0.645 |
| 5 | 11.9 | 0.579 |
| 6 | 9.5 | 0.572 |

Inertia drops sharply to $k=3$ then flattens (elbow); silhouette peaks at $k=3$. Cluster centres (spend, orders): about (20, 2.9) with 60 customers "occasional", (55, 7.9) with 49 "regular", (90, 14.7) with 41 "heavy". Real data rarely show an elbow this clean, which is why usefulness and stability are judged too.

### In the news
See news box. Quick-commerce and e-commerce firms segment on frequency, basket and category mix in exactly this way, then run differentiated promotions; segment definitions should be refreshed as behaviour shifts.

### Interview angle
> [!question] How it is asked
> "You have 2 million customers. How would you create segments and make them actionable?"

> [!tip] Strong answer includes
> - Feature design (recency, frequency, monetary value, category mix), log-transform and scale
> - k-means with k-means++ and silhouette/elbow; test stability across samples
> - Profile segments, name them, size them, attach an action and a KPI
> - Caveat: clusters are not natural categories; refresh and validate with an A/B test, see [[214 Causal Inference & Experimentation Beyond A-B Tests]]

---
## 8. Discriminant Analysis
> 🟠 Tier 2 · _Key points:_ Supervised: find linear combination that best separates known groups; equal covariance (LDA) vs unequal (QDA)

### Definition
**Linear discriminant analysis (LDA)** classifies units into known groups using a linear combination $D=\mathbf w^\top\mathbf x$ chosen to maximise between-group relative to within-group variance (Fisher's criterion). Assumes multivariate normal predictors with a common covariance matrix; **QDA** allows group-specific covariances. For two groups with equal priors the rule assigns to the nearer centroid in Mahalanobis distance. Evaluate with a hold-out or cross-validated confusion matrix, not training accuracy. For many practical binary tasks logistic regression ([[209 Generalised Linear Models & Categorical Data Analysis]], [[096 Classification Algorithms]]) is more flexible and needs fewer assumptions; LDA also doubles as supervised dimension reduction and is the classical tool for Altman's Z-score type credit models.

### Example
Simulated data: 60 retained customers (mean tenure 40 months, 5 service calls a year) and 60 churners (30 months, 8 calls) with a common covariance. Fitted LDA coefficients are about $-0.72$ on tenure and $+2.04$ on service calls (intercept $+11.7$), meaning calls separate churners more than tenure. Training accuracy 97.5%; 5-fold cross-validated accuracy 97.5%. (Simulated groups are well separated by construction; real churn data seldom classify so cleanly.) The discriminant score gives each customer a churn-risk rank.

### In the news
See news box. Discriminant-type scoring (credit, risk, churn) is where multivariate classification meets decisions; regulators and model-risk teams now expect validation and explainability, see [[220 Responsible AI, Explainability & Model Governance]].

### Interview angle
> [!question] How it is asked
> "How is discriminant analysis different from cluster analysis?"

> [!tip] Strong answer includes
> - Discriminant is supervised (known groups, builds a classifier); clustering is unsupervised (finds groups)
> - Assumptions of LDA (normality, equal covariance) and when logistic is preferred
> - Validate out of sample; report hit rate versus the naive proportional-chance benchmark

---
## 9. MANOVA (Multivariate Analysis of Variance)
> 🟠 Tier 2 · _Key points:_ Compare group mean vectors on several correlated outcomes; Wilks' lambda, Pillai's trace; then follow-up ANOVAs

### Definition
MANOVA tests whether $g$ groups differ on a **vector** of $p$ outcomes: H0: $\boldsymbol\mu_1=\dots=\boldsymbol\mu_g$. Compared with $p$ separate ANOVAs ([[089 Hypothesis Testing]]), it controls the family-wise error and can detect differences that appear only in the combination of outcomes. Statistics: Wilks' $\Lambda=|\mathbf E|/|\mathbf E+\mathbf H|$ (smaller is stronger evidence), Pillai's trace (most robust to violations), Hotelling-Lawley, Roy's largest root. Assumptions: multivariate normality, equal covariance matrices (Box's M), independence, adequate $n$ per cell. After a significant result, run follow-up univariate ANOVAs or discriminant analysis to find where the difference lies.

### Example
Three customer segments (30 each) scored on satisfaction and loyalty (simulated; statsmodels `MANOVA.from_formula('sat + loyalty ~ seg', df)`). Result for the segment effect: Wilks' $\Lambda=0.690$, $F(4,172)=8.78$, $p<0.001$; Pillai's trace 0.318 ($F(4,174)=8.21$). Segments differ on the pair of outcomes. The data were generated with satisfaction means of 50, 55 and 62 and loyalty means of 70, 70 and 78, so the third segment drives most of the effect; with real data you would confirm this with follow-up univariate ANOVAs or a discriminant analysis.

### In the news
See news box. Multi-outcome comparisons (several KPIs across regions or pilots) are common in operations and marketing tests, and testing each KPI alone inflates false positives.

### Interview angle
> [!question] How it is asked
> "You compared three regions on five KPIs with five ANOVAs. What is the problem?"

> [!tip] Strong answer includes
> - Multiple testing inflates Type I error; MANOVA tests the vector jointly, or use Bonferroni/Holm
> - Use Pillai's trace when assumptions are shaky
> - Follow up with univariate tests or discriminant analysis; check covariance equality

---
## 10. Conjoint Analysis for Pricing and Feature Trade-offs
> 🟠 Tier 2 · _Key points:_ Respondents rate/choose product profiles; regression gives part-worth utilities; importance = range of part-worths; WTP = utility per rupee

### Definition
**Conjoint analysis** infers how customers value attributes by asking them to rate, rank or choose among **profiles** that combine attribute levels (price, battery, brand). Estimating a regression (or a multinomial logit for choice-based conjoint, CBC) gives **part-worth utilities** for each level. **Attribute importance** $=\dfrac{\text{range of its part-worths}}{\sum\text{ranges}}$. **Willingness to pay** for a feature equals its part-worth divided by the utility per rupee (the price slope). Choice-based conjoint is closer to real purchase behaviour; **MaxDiff** ranks many features; full-factorial designs grow fast, so fractional or orthogonal designs are used. Simulator outputs: predicted share for a new profile, optimal price, cannibalisation. Limits: stated, not revealed, preference; hypothetical bias; too many attributes overload respondents.

### Example
A 3 x 2 x 2 full factorial of Bluetooth-speaker profiles (12 cards), rated 0-10 by a panel (illustrative simulated ratings): price ₹499/599/699, battery 4000/5000 mAh, brand X/Y. OLS with dummies on the 12 profiles ($R^2=0.99$) gives part-worths relative to base: price ₹599: $-1.55$, ₹699: $-3.23$; 5000 mAh: $+1.78$; Brand Y: $+0.82$. Ranges: price 3.23, battery 1.78, brand 0.82; total 5.83, so importance = **55.4%, 30.6%, 14.0%**. Utility per rupee about $3.23/200=0.0162$. WTP for the bigger battery $\approx1.78/0.0162=$ **₹110**; the Brand Y premium $\approx0.82/0.0162=$ **₹51**. Pricing implication: an upgrade to 5000 mAh costing the firm ₹70 can be priced up to about ₹110 higher and still be preferred; ₹150 more would lose to the baseline.

### In the news
See news box. The Indian EV choice-experiment study is a published example of this method, estimating rupee-equivalent value of range and charging speed for buyers; the same logic prices features in phones, appliances and SaaS plans.

### Interview angle
> [!question] How it is asked
> "How would you decide whether to add a premium feature and what to charge for it?"

> [!tip] Strong answer includes
> - Conjoint/choice experiment to get part-worths and WTP, plus a market simulator for share and revenue
> - Combine with cost-to-serve and competitor prices; segment-level utilities (latent class)
> - Caveats: stated vs revealed preference, attribute selection, check against sales data or a price A/B test
> - Tie to pricing and value propositions in [[160 Case Interview - Cost Reduction, Turnaround & Pricing]] and [[030 Product Fundamentals & Strategy]]

---
## 11. Multidimensional Scaling and Perceptual Maps
> 🟠 Tier 2 · _Key points:_ Turn pairwise (dis)similarities into a low-dimensional map; stress measures fit; axes need naming

### Definition
**Multidimensional scaling (MDS)** places objects (brands, products) in 2D so inter-point distances approximate input dissimilarities. **Classical (metric) MDS** double-centres the squared distance matrix, $\mathbf B=-\tfrac12\mathbf J\mathbf D^{(2)}\mathbf J$, and uses its top eigenvectors scaled by $\sqrt\lambda$; **non-metric MDS** preserves only the rank order and is fitted by minimising **stress** (Kruskal's guide: below 0.05 excellent, below 0.10 good, above 0.20 poor). The map is **perceptual** when distances are customers' similarity judgements: brands close together compete head to head; empty regions suggest positioning gaps. Axes are rotationally arbitrary and must be interpreted (for example with attribute ratings drawn as vectors, a property-fitting step). Number of dimensions chosen from a stress plot.

### Example
Four brands with consumer dissimilarity ratings (A-B = 2, A-C = 6, A-D = 7, B-C = 5, B-D = 6, C-D = 2). Classical MDS eigenvalues: 35.6, 1.5, 1.4, so the first dimension holds 35.6/(35.6+1.5+1.4)=92% of the structure. Dimension 1 coordinates: A -3.47, B -2.40, C 2.40, D 3.47; dimension 2 is negligible (about $\pm0.6$). The map shows two competitive pairs, {A, B} and {C, D}, far apart: for example "budget" brands vs "premium" brands, to be named from attribute data. A brand repositioning would aim to occupy the gap between pairs only if a segment lives there.

### In the news
See news box. Perceptual maps are standard output of consumer-perception research and are used in brand-health and positioning reviews.

### Interview angle
> [!question] How it is asked
> "How would you find out how customers see us relative to competitors?"

> [!tip] Strong answer includes
> - Collect similarity or attribute ratings, build a perceptual map by MDS or correspondence analysis
> - Interpret axes and gaps, identify closest competitors, check stress and stability
> - Complement with preference data (ideal points) before repositioning

---
## 12. Correspondence Analysis
> 🟠 Tier 2 · _Key points:_ Maps a contingency table; chi-square distances; SVD; inertia = $\chi^2/n$; for brand x attribute tables

### Definition
**Correspondence analysis (CA)** is PCA-like for a cross-tabulation (brands x attributes, regions x product categories). It decomposes the table's departure from independence: total **inertia** $=\chi^2/n$. Singular value decomposition of the standardised residual matrix gives dimensions; each dimension's share of inertia says how much it explains. Row and column categories are plotted together; rows near each other have similar profiles, and a row near a column is positively associated with it (interpret distances between rows with rows, and rows to columns only directionally unless symmetrical scaling is used). Multiple correspondence analysis handles several categorical variables (survey data).

### Example
250 respondents attribute brands to image words:

| | Cheap | Reliable | Premium |
|---|---|---|---|
| B1 | 40 | 10 | 5 |
| B2 | 30 | 30 | 10 |
| B3 | 10 | 15 | 40 |
| B4 | 5 | 20 | 35 |

Pearson $\chi^2=92.13$ (6 d.f., $p<10^{-16}$) so total inertia $=92.13/250=0.3685$. Dimension 1 takes 88.1% and dimension 2 takes 11.9% (singular values 0.570 and 0.209). Dimension 1 coordinates: B1 -0.79, B2 -0.36, B3 0.52, B4 0.58; columns Cheap -0.71, Reliable 0.02, Premium 0.65. Reading: dimension 1 is a price-to-premium axis; B1 is the "cheap" brand, B3 and B4 are "premium", B2 sits between, and dimension 2 mostly separates "Reliable" (-0.32) from the extremes.

### In the news
See news box. CA complements conjoint: use CA to see current perceptions, conjoint to price changes.

### Interview angle
> [!question] How it is asked
> "What is a perceptual map and how do you build one from survey data?"

> [!tip] Strong answer includes
> - Brand x attribute table, correspondence analysis (or MDS), plot first two dimensions with variance explained
> - Interpret proximity and axes; caution that it is descriptive and depends on the attributes asked
> - Use for positioning and white-space discovery, then validate with preference data

---
## 13. ⭐ Advanced: Interpretation Rules, Pitfalls and Choosing a Method
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Decision guide: **reduce variables** (many correlated numeric items): PCA for indices/compression; EFA for latent constructs. **Group units without labels**: hierarchical for small data and dendrogram insight, k-means or Gaussian mixtures for large data. **Predict known groups**: discriminant/logistic. **Compare group means on several outcomes**: MANOVA. **Map perceptions**: MDS (similarity ratings) or CA (frequency tables). **Trade-offs and pricing**: conjoint/choice models. Rules of thumb: standardise; inspect correlations first; keep components/factors that are interpretable, stable and meet a threshold (eigenvalue above 1, scree elbow, 70%+ variance); loadings above 0.4; $k$ chosen by elbow, silhouette and business use; validate on a hold-out or by re-sampling; never name clusters without profiling them.

Common pitfalls: running PCA on unscaled data; treating factor scores as measured data; overfitting clusters to noise (always cluster data that really has structure; k-means will return $k$ clusters on uniform noise); using PCA components in a supervised model without checking predictive value; cluster instability across samples; reading perceptual-map axes as causal; conjoint with too many attributes.

### Example
A consultant's engagement on a retail loyalty programme: (1) PCA on 20 behaviour metrics to get 3 components (spend intensity, category breadth, promo sensitivity); (2) k-means on the 3 scores, $k=4$ by silhouette; (3) discriminant model to assign new customers to segments; (4) MANOVA to confirm segments differ on satisfaction and loyalty; (5) conjoint within each segment to price rewards. Each step answers a different question and the output of one feeds the next.

### In the news
See news box. Indices and segmentation rely on the same toolbox; the 2025 inclusion-index paper uses a two-stage PCA for exactly the construction-then-ranking workflow above.

### Interview angle
> [!question] How it is asked
> "You are given a dataset with 50 customer variables and asked to find segments. Walk me through the approach."

> [!tip] Strong answer includes
> - Clean and scale, reduce dimensionality (PCA), cluster, validate, profile, act
> - Evaluate with silhouette, stability, business interpretability; run an experiment to prove value
> - Mention [[097 Unsupervised Learning]] for algorithms beyond k-means (DBSCAN, GMM), and [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]] for tool recipes (SPSS/R/Python)
