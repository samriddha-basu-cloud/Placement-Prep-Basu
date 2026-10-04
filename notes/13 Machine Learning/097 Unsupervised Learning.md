---
tags: [machine-learning, tier2]
area: Machine Learning
topic: "Unsupervised Learning"
tier: Tier 2
roles: PM / Operations
status: complete
subtopics: 12
---
# Unsupervised Learning

⬅ [[096 Classification Algorithms]] · [[_Index - Machine Learning|Machine Learning]] · [[098 Model Selection & Optimization]] ➡

> **Area:** Machine Learning · **Priority:** 🟠 Tier 2 · **Target roles:** PM / Operations

## Sub-topics in this note
1. [[#1. K-Means Clustering]]
2. [[#2. Hierarchical Clustering]]
3. [[#3. DBSCAN]]
4. [[#4. Principal Component Analysis (PCA)]]
5. [[#5. t-SNE]]
6. [[#6. Association Rules (Apriori/FP-Growth)]]
7. [[#7. Anomaly Detection]]
8. [[#8. RFM Clustering for Customer Segmentation]]
9. [[#9. Evaluation: Unsupervised]]
10. [[#10. Topic Modeling (LDA)]]
11. [[#11. ⭐ Advanced: Gaussian Mixture Models and Soft Clustering]]
12. [[#12. ⭐ Advanced: Making Clusters Actionable (Profiling, Stability and Deployment)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Finding the unusual without fixed rules, RBI's MuleHunter.AI
> **RBI's MuleHunter.AI (announced Dec 2024).** The Reserve Bank Innovation Hub announced an ML solution to detect "mule" accounts, motivated by the limits of traditional rule-based systems (many false positives, slow to adapt to new criminal tactics). It studies 19 distinct behaviours associated with mule accounts, was piloted with two public sector banks, and per an RTI reply reported in Dec 2025, 23 banks had implemented it. RBI declined to disclose how many mule accounts were identified. The sources do not say whether the model is supervised or unsupervised; treat it as an applied example of pattern and anomaly detection, not as a documented unsupervised method. ([Business Standard](https://www.business-standard.com/finance/personal-finance/explained-rbi-has-a-new-ai-tool-mulehunter-ai-to-reduce-digital-frauds-124120900250_1.html), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/))
>
> **Stanford AI Index 2025 (April 2025).** 78% of organisations reported using AI in 2024, up from 55%; inference cost for GPT-3.5-level performance dropped over 280-fold (Nov 2022 to Oct 2024). ([Business Wire summary of the Stanford HAI report](https://www.businesswire.com/news/home/20250407539812/en/Stanford-HAIs-2025-AI-Index-Reveals-Record-Growth-in-AI-Capabilities-Investment-and-Regulation))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. K-Means Clustering
> 🟠 Tier 2 · _Tracker hint:_ Choose k centroids; assign points; update centroids; repeat; elbow method for k selection

### Definition
K-Means partitions data into $k$ clusters by minimising the **within-cluster sum of squares (WCSS / inertia)**:

$$\min\sum_{j=1}^{k}\sum_{x\in C_j}\|x-\mu_j\|^2$$

**Algorithm (Lloyd):** (1) choose $k$ initial centroids (use **k-means++**); (2) assign each point to the nearest centroid; (3) recompute each centroid as the cluster mean; (4) repeat until assignments stop changing. Assumes roughly spherical, similar-sized clusters; sensitive to scale (standardise), outliers, and initialisation (run `n_init` times); converges to a local optimum. **Elbow method:** plot WCSS versus $k$ and pick the bend; confirm with silhouette.

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(X_scaled)
labels, inertia = km.labels_, km.inertia_
```

### Example
1-D points 1, 2, 9, 10. $k=1$: mean 5.5, WCSS = 4.5²+3.5²+3.5²+4.5² = 20.25+12.25+12.25+20.25 = **65**. $k=2$: centroids 1.5 and 9.5, WCSS = 0.25×4 = **1.0**. The huge drop from 65 to 1 marks the elbow at $k=2$.

### In the news
See news box. Grouping accounts by behaviour is the clustering instinct, though the RBI sources do not say K-Means is used.

### Interview angle
> [!question] How it is asked
> "Explain K-Means and how you choose k."

> [!tip] Strong answer includes
> - Assign-update loop and the objective
> - Elbow plus silhouette, plus business sense for k
> - Scaling, k-means++, multiple restarts
> - Limits: spherical clusters, outliers, need to specify k

---

## 2. Hierarchical Clustering
> 🟠 Tier 2 · _Tracker hint:_ Agglomerative (bottom-up) or Divisive (top-down); dendrogram; no need to specify k

### Definition
**Agglomerative** clustering starts with each point as its own cluster and repeatedly merges the two closest clusters; **divisive** starts with one cluster and splits. The result is a **dendrogram**; cutting it at a height gives the clusters, so $k$ need not be fixed in advance.

| Linkage | Distance between clusters | Behaviour |
|---|---|---|
| Single | Minimum pairwise | Chaining, finds elongated shapes, noise-sensitive |
| Complete | Maximum pairwise | Compact clusters |
| Average | Mean pairwise | Compromise |
| Ward | Increase in within-cluster variance | Compact, similar-size clusters (common default) |

Complexity is about $O(n^2)$ memory, so it suits thousands, not millions, of points.

```python
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
Z = linkage(X_scaled, method="ward")
labels = fcluster(Z, t=4, criterion="maxclust")
```

### Example
Points 1, 2, 9, 10 with single linkage: merge (1,2) at distance 1, merge (9,10) at distance 1, then merge the two groups at distance $9-2=$ **7**. A long vertical gap in the dendrogram before the final merge says "two natural clusters".

### In the news
See news box. Hierarchies of product or customer groups are widely used in analytics, though there is no specific news item here.

### Interview angle
> [!question] How it is asked
> "K-Means versus hierarchical clustering: when would you pick hierarchical?"

> [!tip] Strong answer includes
> - Bottom-up merging and dendrogram reading
> - Linkage choices and their effects
> - Pros: no preset k, shows structure at all levels; cons: cost, no reassignments
> - Typical use: small datasets, taxonomies

---

## 3. DBSCAN
> 🟠 Tier 2 · _Tracker hint:_ Density-based; finds arbitrary shapes; identifies outliers; params: eps, min_samples

### Definition
**DBSCAN** groups points that are densely packed. Parameters: **eps** (neighbourhood radius) and **min_samples**. A point is a **core point** if at least `min_samples` points (including itself) lie within `eps`; **border points** are within `eps` of a core point but not core; the rest are **noise** (label -1). Clusters are connected chains of core points. Strengths: arbitrary shapes, no need to give $k$, built-in outlier detection. Weaknesses: single `eps` fails when densities differ (HDBSCAN helps), struggles in high dimensions, needs scaling. Choose `eps` from the **k-distance plot** knee, with `min_samples` about $2\times$dimensions.

```python
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=5).fit(X_scaled)
noise = (db.labels_ == -1)
```

### Example
eps = 1.5, min_samples = 3. Points 1, 2, 3 are mutual neighbours (core): cluster A. Points 20, 21, 22 form cluster B. Point 50 has no neighbours within 1.5, so it is **noise** (an outlier), something K-Means would force into a cluster.

### In the news
See news box. Density-based detection of "points that do not fit any normal group" is the logic behind many fraud screens (general principle; RBI sources do not name DBSCAN).

### Interview angle
> [!question] How it is asked
> "When is DBSCAN better than K-Means? How do you set eps?"

> [!tip] Strong answer includes
> - Core, border, noise points
> - Arbitrary shape and outlier handling
> - k-distance plot for eps
> - Limits with varying density and high dimensions

---

## 4. Principal Component Analysis (PCA)
> 🟠 Tier 2 · _Tracker hint:_ Dimensionality reduction; orthogonal components; retain 95% variance; eigenvalues/vectors

### Definition
PCA finds new orthogonal axes (**principal components**) ordered by the variance they capture. Steps: standardise; compute the covariance matrix $\Sigma$; find eigenvectors (directions) and eigenvalues (variance per direction); keep the top components; project: $Z=XW$. 

$$\text{Explained variance ratio}_i=\frac{\lambda_i}{\sum_j\lambda_j}$$

Choose components to retain e.g. 95% cumulative variance (or a scree-plot elbow). Uses: compression, noise reduction, de-correlating features before regression (fixes multicollinearity), visualisation. Limits: linear only, components are hard to interpret, **scale-sensitive**, variance is not the same as predictive signal. Equivalent to SVD of centred data.

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95).fit(X_scaled)   # keep 95% variance
Z = pca.transform(X_scaled); print(pca.explained_variance_ratio_)
```

### Example
Eigenvalues 5, 3, 1.5, 0.5 (total 10): ratios 50%, 30%, 15%, 5%. Cumulative: 50%, 80%, 95%, 100%. So **3 components** retain 95% of variance, compressing 4 features to 3.

### In the news
See news box. Behaviour-based risk models with many correlated features often compress them with PCA or similar before modelling (general practice; not stated for MuleHunter.AI).

### Interview angle
> [!question] How it is asked
> "Explain PCA to a non-technical person and say when you would use it."

> [!tip] Strong answer includes
> - New axes capturing maximum variance, orthogonal
> - Eigenvalues/eigenvectors, scree plot, 95% rule
> - Must scale; loses interpretability
> - Use cases: multicollinearity, visualisation, noise removal

---

## 5. t-SNE
> 🟠 Tier 2 · _Tracker hint:_ Non-linear dimensionality reduction for visualization; 2D/3D projection of high-dim data

### Definition
**t-SNE** (t-distributed Stochastic Neighbor Embedding) maps high-dimensional points to 2D or 3D so that **neighbours stay neighbours**. It converts distances to probabilities of being neighbours (Gaussian in high-D, heavy-tailed Student-t in low-D) and minimises the **KL divergence** between them. **Perplexity** (typically 5 to 50) sets the effective neighbourhood size. Cautions: for **visualisation only**; cluster sizes and distances between clusters are **not meaningful**; results vary with perplexity and random seed; slow on large data; no `transform` for new points. Pre-reduce with PCA to 30 to 50 dimensions first. UMAP is a faster alternative that keeps more global structure.

```python
from sklearn.manifold import TSNE
emb = TSNE(n_components=2, perplexity=30, init="pca", random_state=0).fit_transform(X_scaled)
```

### Example
Embedding 784-pixel images of handwritten digits yields ten visibly separate blobs in 2-D. Plotting customer embeddings (50 behaviour features reduced to 2-D) lets a marketing analyst see whether the K-Means segments are visually separated.

### In the news
See news box. Explaining model behaviour visually to non-technical stakeholders is part of why such tools matter as AI use spreads (78% of organisations).

### Interview angle
> [!question] How it is asked
> "PCA versus t-SNE: what is the difference and what are the pitfalls?"

> [!tip] Strong answer includes
> - Linear/global (PCA) versus non-linear/local (t-SNE)
> - Perplexity and randomness
> - Never read distances between clusters as real
> - Visualisation only; use PCA for feature reduction

---

## 6. Association Rules (Apriori/FP-Growth)
> 🟠 Tier 2 · _Tracker hint:_ Market basket: {milk} → {bread}; Support, Confidence, Lift metrics

### Definition
Association rule mining finds items that co-occur in transactions. For a rule $A\Rightarrow B$:

$$\text{Support}=P(A\cup B),\quad \text{Confidence}=\frac{P(A\cup B)}{P(A)},\quad \text{Lift}=\frac{\text{Confidence}}{P(B)}=\frac{P(A\cup B)}{P(A)P(B)}$$

Lift $>1$ means positive association, $=1$ independence, $<1$ substitutes. **Apriori** prunes using the property that every subset of a frequent itemset is frequent, generating candidates level by level; **FP-Growth** compresses data into an FP-tree and avoids candidate generation (faster). Set minimum support/confidence; filter by lift. Beware: association is not causation, and many trivial rules appear.

```python
from mlxtend.frequent_patterns import apriori, association_rules
freq = apriori(basket_df, min_support=0.05, use_colnames=True)
rules = association_rules(freq, metric="lift", min_threshold=1.2)
```

### Example
1,000 baskets: milk 200, bread 250, both 100. Support = 100/1000 = **0.10**. Confidence(milk → bread) = 100/200 = **0.50**. P(bread) = 0.25, so lift = 0.5/0.25 = **2.0**: milk buyers are twice as likely to buy bread than average.

### In the news
See news box. Cross-sell recommendations in e-commerce and quick commerce rely on this co-purchase logic; there is no specific dated item here.

### Interview angle
> [!question] How it is asked
> "Define support, confidence and lift. How would a retailer use them?"

> [!tip] Strong answer includes
> - Formulas and a worked numeric example
> - Why lift beats confidence (popular items inflate confidence)
> - Use: shelf layout, bundles, recommendations
> - Limits: no causality, pruning thresholds

---

## 7. Anomaly Detection
> 🟠 Tier 2 · _Tracker hint:_ Isolation Forest, One-Class SVM, Autoencoder; fraud detection, quality control

### Definition
Anomaly detection finds rare observations that differ from the norm. Approaches:

- **Statistical:** z-score, IQR, Mahalanobis distance.
- **Isolation Forest:** random splits isolate anomalies in fewer steps. Score $s=2^{-E(h(x))/c(n)}$; near 1 is anomalous, near 0.5 normal.
- **One-Class SVM:** learns a boundary around normal data.
- **Autoencoder:** neural net that reconstructs inputs; high **reconstruction error** signals anomaly.
- **LOF and DBSCAN:** density-based.

Often unsupervised or semi-supervised since labels are scarce; tune the **contamination** rate; evaluate with precision at top-K, and expect many false positives, so human review is needed. Handle drift.

```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.01, random_state=0).fit(X_scaled)
score = iso.decision_function(X_scaled)   # lower = more anomalous
```

### Example
UPI-style transaction: a customer who usually sends Rs 500 to 3 contacts suddenly sends Rs 49,000 to 15 new accounts in an hour. The Isolation Forest isolates it in about 2 splits versus the typical 8 to 10, giving a score close to 1.

### In the news
See news box. This is the closest news link: RBI built MuleHunter.AI because fixed rules produce false positives and adapt slowly; flagging unusual account behaviour is the anomaly-detection use case. The sources do not disclose its algorithm.

### Interview angle
> [!question] How it is asked
> "How would you detect fraudulent transactions when you have very few labelled frauds?"

> [!tip] Strong answer includes
> - Anomaly methods (Isolation Forest, autoencoder) plus supervised once labels accrue
> - Feature ideas: velocity, new payees, amount versus history
> - Evaluation with precision@K and analyst feedback loop
> - Cost of false positives and monitoring for drift

---

## 8. RFM Clustering for Customer Segmentation
> 🟠 Tier 2 · _Tracker hint:_ Recency, Frequency, Monetary; K-Means on scaled RFM; actionable segments

### Definition
**RFM** summarises each customer with: **Recency** (days since last purchase), **Frequency** (number of orders), **Monetary** (total spend). Pipeline: aggregate transactions per customer; transform skewed values (log); **standardise**; run K-Means (choose $k$ by elbow and silhouette, typically 4 to 6); profile each cluster by average R, F, M; name segments and attach actions. Alternative: rank each metric into quintiles (1 to 5) and combine scores. Recency is "lower is better", so invert when scoring.

```python
rfm = df.groupby("cust").agg(R=("date", lambda d: (today - d.max()).days),
                             F=("order_id", "nunique"), M=("amount", "sum"))
X = StandardScaler().fit_transform(np.log1p(rfm))
rfm["seg"] = KMeans(5, n_init=10, random_state=0).fit_predict(X)
```

### Example
Customer: last purchase 5 days ago, 12 orders, Rs 18,000 spent: R=5, F=12, M=18,000 (a "Champion": retain with early access). Another: R=200, F=6, M=9,000 is "At risk": send win-back offer. A third: R=3, F=1, M=500 is "New": nurture with a second-purchase coupon.

### In the news
See news box. As AI use spreads (78% of organisations in 2024), segmentation like this is now routine in Indian D2C and quick-commerce marketing teams.

### Interview angle
> [!question] How it is asked
> "How would you segment customers for a retailer and what would you do with the segments?"

> [!tip] Strong answer includes
> - RFM definitions, log and scale, choose k
> - Profile and name clusters, attach one action each
> - Validate stability and test uplift by A/B test
> - Refresh periodically since customers move between segments

---

## 9. Evaluation: Unsupervised
> 🟠 Tier 2 · _Tracker hint:_ Silhouette score (-1 to 1, higher better); Elbow method; Davies-Bouldin index

### Definition
Without labels, evaluate **cohesion** (tight clusters) and **separation** (far apart).

- **Silhouette** for a point: $s=\dfrac{b-a}{\max(a,b)}$, where $a$ = mean distance to its own cluster, $b$ = mean distance to the nearest other cluster. Range -1 to 1; near 1 well clustered, near 0 on a border, negative probably misassigned. Average over points.
- **Elbow (WCSS):** bend in the inertia curve.
- **Davies-Bouldin index:** average similarity of each cluster to its worst match; **lower is better**.
- **Calinski-Harabasz:** between- to within-cluster variance; higher is better.
- **External checks** (if labels exist): adjusted Rand index.
- **Practical:** stability across resamples, interpretability and actionability.

```python
from sklearn.metrics import silhouette_score, davies_bouldin_score
print(silhouette_score(X, labels), davies_bouldin_score(X, labels))
```

### Example
A point with mean intra-cluster distance $a=2$ and nearest-other-cluster distance $b=6$: $s=(6-2)/6=$ **0.667**, a well-placed point. If $a=5,b=4$: $s=(4-5)/5=-0.2$, likely in the wrong cluster.

### In the news
See news box. RBI's mule tool was judged against rule-based systems through a pilot (it found more mule accounts), a reminder that business benchmarking complements internal metrics.

### Interview angle
> [!question] How it is asked
> "How do you know your clusters are good when there is no ground truth?"

> [!tip] Strong answer includes
> - Silhouette with formula and interpretation, plus elbow and Davies-Bouldin
> - Stability across samples and seeds
> - Business usefulness: distinct, actionable, adequately sized
> - A/B test of actions per segment

---

## 10. Topic Modeling (LDA)
> 🟠 Tier 2 · _Tracker hint:_ Latent Dirichlet Allocation; document → topics; topics → words; NLP application

### Definition
**LDA** is a generative probabilistic model for text. Each **document** is a mixture of topics; each **topic** is a distribution over words. Both have Dirichlet priors: $\alpha$ (document-topic; small means few topics per document) and $\beta/\eta$ (topic-word). Given a bag-of-words corpus and the number of topics $K$, inference (Gibbs sampling or variational Bayes) estimates $\theta_d$ (topic mix of document $d$) and $\phi_k$ (word distribution of topic $k$). Topics are **unnamed**: humans label them from top words. Choose $K$ by **coherence** score or perplexity plus judgement. Preprocess: tokenise, remove stop-words, lemmatise, drop very rare/common words. Modern alternatives: BERTopic, embeddings with clustering.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
X = CountVectorizer(stop_words="english", max_df=0.9, min_df=5).fit_transform(docs)
lda = LatentDirichletAllocation(n_components=6, random_state=0).fit(X)
```

### Example
Analysing 50,000 delivery-app reviews with K=6 might give topics whose top words are: {late, delay, wait, rider} (delivery delay), {refund, money, cancelled, payment} (payments), {fresh, quality, damaged, packaging} (product quality). A review "arrived late and the milk was spoiled" might be about 50% delay, 40% quality, 10% other.

### In the news
See news box. As cheap text-capable AI spreads (280-fold inference cost fall), topic discovery over reviews and complaints has become an easy first step for product teams.

### Interview angle
> [!question] How it is asked
> "How would you find out what customers complain about from 100,000 reviews?"

> [!tip] Strong answer includes
> - Preprocess text then LDA (or embeddings plus clustering)
> - Choosing the number of topics via coherence and manual review
> - Naming topics and linking to product or operations fixes
> - Limits: bag-of-words ignores order; use sentiment alongside

---

## 11. ⭐ Advanced: Gaussian Mixture Models and Soft Clustering
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **Gaussian Mixture Model (GMM)** assumes data come from $K$ Gaussian components:

$$p(x)=\sum_{k=1}^{K}\pi_k\,\mathcal N(x\mid\mu_k,\Sigma_k)$$

Fitted by **Expectation-Maximisation (EM)**: E-step computes each point's **responsibility** (probability of belonging to each component); M-step updates $\pi,\mu,\Sigma$ using those weights. Differences from K-Means: **soft** assignments (probabilities), elliptical clusters of different sizes (full covariance), and a proper likelihood so you can select $K$ with **BIC/AIC**. K-Means is the special case of equal spherical covariances with hard assignments. Low likelihood under the mixture can also flag anomalies.

```python
from sklearn.mixture import GaussianMixture
gm = GaussianMixture(n_components=3, covariance_type="full", random_state=0).fit(X_scaled)
probs = gm.predict_proba(X_scaled); print(gm.bic(X_scaled))
```

### Example
A customer with responsibilities (0.7 loyal, 0.25 occasional, 0.05 dormant) is mostly loyal but borderline occasional, useful information that hard K-Means labelling discards. Comparing BIC for K=2 to 6 and picking the minimum gives a principled K.

### In the news
See news box. Probabilistic membership and likelihood scores suit risk and fraud settings where a "how unusual" score is more useful than a hard label.

### Interview angle
> [!question] How it is asked
> "What are the limitations of K-Means and what could you use instead?"

> [!tip] Strong answer includes
> - K-Means limits: spherical, equal-size, hard assignment
> - GMM with EM, soft probabilities, BIC for K
> - Other alternatives: DBSCAN, hierarchical
> - Practical caution: more parameters, need more data

---

## 12. ⭐ Advanced: Making Clusters Actionable (Profiling, Stability and Deployment)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Consulting and PM interviews reward turning clusters into decisions.

1. **Profile:** table of mean features by cluster, size, revenue share; compare to overall using index = cluster mean / overall mean × 100.
2. **Name and act:** one-line description and one action per segment.
3. **Stability:** re-run with different seeds and bootstrap samples; check adjusted Rand index between runs. Unstable clusters should not drive strategy.
4. **Size and value:** segments too small to serve are merged.
5. **Assignment in production:** save the scaler and model; score new customers; monitor migration between segments.
6. **Prove value:** hold out a control group and compare uplift per segment.

### Example
Segment B has 12% of customers but 38% of revenue; its average order value is Rs 1,900 versus Rs 950 overall, giving an index of 200. Action: loyalty tier and free delivery. The test group gets the offer, the control does not; after 8 weeks, compare repeat-purchase rate.

### In the news
See news box. Rolling out an AI tool to 23 banks (by Dec 2025) shows that scaling and operationalising matters more than the first pilot, the same lesson for segmentation.

### Interview angle
> [!question] How it is asked
> "You built clusters. How do you convince the marketing head to act on them?"

> [!tip] Strong answer includes
> - Business-friendly profiles with index values and names
> - Stability evidence
> - One concrete, testable action per segment
> - Control group measurement and refresh plan

---
## 🔗 Go deeper: expansion notes
- [[207 Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis|Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis]]
