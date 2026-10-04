---
tags: [python-programming, tier2]
area: Python Programming
topic: "Python for Product Analytics"
tier: Tier 2
roles: PM / Operations
status: complete
subtopics: 10
---
# Python for Product Analytics

⬅ [[068 Operations-Specific Python (PuLP, SimPy)]] · [[_Index - Python Programming|Python Programming]] · [[184 Python OOP, Modules & Project Structure]] ➡
> **Area:** Python Programming · **Priority:** 🟠 Tier 2 · **Target roles:** PM / Operations

## Sub-topics in this note
1. [[#1. Cohort Analysis]]
2. [[#2. Funnel Analysis]]
3. [[#3. A/B Test Analysis]]
4. [[#4. User Segmentation (Clustering)]]
5. [[#5. RFM Analysis]]
6. [[#6. DAU/MAU Calculation]]
7. [[#7. Churn Prediction]]
8. [[#8. Event Tracking Analysis]]
9. [[#9. ⭐ Advanced: Customer Lifetime Value and Retention Curves]]
10. [[#10. ⭐ Advanced: Variance Reduction (CUPED) and Sequential Testing]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the Python stack behind product analytics changed under analysts' feet
> **pandas 3.0.0 (21 January 2026).** Copy-on-Write is now the default: chained assignment such as `df[df['plan'] == 'free']['churn'] = 1` no longer modifies the original (use `df.loc[mask, 'churn'] = 1`), `SettingWithCopyWarning` is gone, strings default to a new `str` dtype, `pd.col()` expressions arrive, and Python 3.11+ is required. Cohort, funnel and RFM scripts written for older pandas should be re-tested. ([pandas 3.0.0 what's new](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html))
>
> **SciPy 1.16.0 (22 June 2025).** `scipy.stats.f_oneway` and `tukey_hsd` gain an `equal_var` option (Welch ANOVA, Games-Howell), useful for A/B/C tests with unequal variances. ([SciPy 1.16.0 release notes](https://docs.scipy.org/doc/scipy-1.16.0/release/1.16.0-notes.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Cohort Analysis
> 🟠 Tier 2 · _Tracker hint:_ df.groupby(['cohort_month','period']) — retention matrix; pivot to heatmap

### Definition
A **cohort** is a group of users who share a starting event in the same period (first purchase month, signup week). **Cohort analysis** tracks each cohort's behaviour over time since that start (period 0, 1, 2, ...), separating *lifecycle effects* from *calendar effects* that blended averages hide. The classic output is a **retention matrix**: rows = cohorts, columns = periods since start, cells = share of the cohort still active.
$$\text{Retention}_{c,k}=\frac{\text{active users of cohort }c\text{ in period }k}{\text{size of cohort }c}$$

```python
import pandas as pd, seaborn as sns
df["order_month"]  = df["order_date"].dt.to_period("M")
df["cohort_month"] = df.groupby("user_id")["order_month"].transform("min")
df["period"] = (df["order_month"] - df["cohort_month"]).apply(lambda x: x.n)
cohort = (df.groupby(["cohort_month", "period"])["user_id"].nunique()
            .reset_index().pivot(index="cohort_month", columns="period", values="user_id"))
retention = cohort.divide(cohort[0], axis=0)
sns.heatmap(retention, annot=True, fmt=".0%", cmap="Blues")
```

Read it diagonally for calendar events (a campaign or outage) and horizontally for lifecycle shape (steep drop then flat = a loyal core). Compare cohorts to see if newer ones retain better after a product change.

### Example
January cohort has 100 users. Active in month 0: 100; month 1: 40; month 2: 30. Retention = 100%, 40%, 30%. If the February cohort (after an onboarding redesign) shows month 1 retention of 52% against 40%, onboarding likely helped (confirm with an experiment).

### In the news
See news box. Cohort code uses `transform` and groupby on period dtypes; re-test it on pandas 3.0 and assign derived columns with `.loc` or `assign` rather than chained indexing.

### Interview angle
> [!question] How it is asked
> "Overall retention looks flat. How would you find out whether new users stay longer than before?"

> [!tip] Strong answer includes
> - Define cohort (acquisition period), period index and retention metric clearly
> - Heatmap reading: horizontal = lifecycle, vertical = cohort quality, diagonal = calendar effects
> - Avoid survivorship blur from averaging all users
> - Link to action: onboarding, reactivation, channel-level cohorts

---

## 2. Funnel Analysis
> 🟠 Tier 2 · _Tracker hint:_ Count users at each stage; conversion rate = users_next / users_current

### Definition
A **funnel** is an ordered sequence of steps toward a goal (visit, product view, add to cart, checkout, payment). Funnel analysis counts the distinct users (or sessions) reaching each step and computes **step conversion** $=\frac{n_{k+1}}{n_k}$ and **overall conversion** $=\frac{n_{last}}{n_1}$. The biggest relative drop-off is the first place to investigate, then segment by device, channel, city or new vs returning users.

```python
import pandas as pd
steps = ["visit", "view_product", "add_to_cart", "checkout", "payment"]
counts = pd.Series({s: df.loc[df["event"] == s, "user_id"].nunique() for s in steps})
funnel = pd.DataFrame({"users": counts,
                       "step_conv": counts / counts.shift(1),
                       "overall": counts / counts.iloc[0]})
```

Strict funnels also require the correct *order* (user did step 2 after step 1 within a window); a simple distinct-count can overstate conversion if users skipped steps via deep links. Decide the attribution window (same session vs 7 days) up front.

### Example
10,000 visits, 6,000 product views, 1,800 add-to-cart, 900 checkouts, 720 payments. Step conversions: 60%, 30%, 50%, 80%. Overall: $720/10{,}000=7.2\%$. The weakest step is view to cart (30%), so test pricing display, reviews, or delivery estimate there; fixing checkout (50% to 60%) would add $1800\times0.6\times0.8-720=144$ orders.

### In the news
See news box. For comparing funnel conversion across more than two variants, SciPy 1.16's Welch-style options and chi-square tests on counts apply.

### Interview angle
> [!question] How it is asked
> "Orders dropped 15% last week. How would you diagnose it?"

> [!tip] Strong answer includes
> - Break the metric into funnel steps and find where the rate changed
> - Segment (platform, source, geography, app version) and check for a release or outage
> - Differentiate traffic (top of funnel) vs conversion problems
> - Propose a hypothesis and experiment, not only a diagnosis

---

## 3. A/B Test Analysis
> 🟠 Tier 2 · _Tracker hint:_ Chi-square or z-test; calculate sample size beforehand; avoid peeking

### Definition
Product A/B testing randomises users into control and treatment and compares a primary metric. For conversion (binary) use a two-proportion **z-test** or a **chi-square** test on the 2x2 table (equivalent: $\chi^2=z^2$ without continuity correction). For continuous metrics (revenue per user) use Welch's t-test or a bootstrap.

Plan before launching:

- **Primary metric**, guardrail metrics (latency, cancellations), and a minimum detectable effect (MDE).
- **Sample size** per arm for proportions: $n\approx\frac{(z_{1-\alpha/2}+z_{1-\beta})^2\,[p_1(1-p_1)+p_2(1-p_2)]}{(p_2-p_1)^2}$.
- Fixed duration covering full weekly cycles.
- **No peeking**: repeatedly checking p-values and stopping at the first $p<0.05$ inflates false positives well above 5%; use a fixed horizon or a proper sequential method.

```python
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import chi2_contingency
z, p = proportions_ztest([250, 200], [2000, 2000])
chi2, p2, dof, exp = chi2_contingency([[250, 1750], [200, 1800]], correction=False)
```

Also check sample ratio mismatch (e.g., 50/50 split should be near 50/50, test with chi-square), novelty effects and interference between users.

### Example
Baseline 10%, expected 12%, 80% power, 5% two-sided ($z_{1-\alpha/2}=1.96$, $z_{1-\beta}=0.84$): $p_1(1-p_1)=0.09$, $p_2(1-p_2)=0.1056$, sum $=0.1956$. $n\approx\frac{(1.96+0.84)^2\times0.1956}{0.02^2}=\frac{7.84\times0.1956}{0.0004}\approx3{,}834$ **per arm**, about 7,700 users in total. The effect is only 2 points, so the test needs thousands of users; a 1,000-user-per-arm test could not reliably detect it. `NormalIndPower` in statsmodels gives about the same answer.

### In the news
See news box. Welch ANOVA (SciPy 1.16 `f_oneway(..., equal_var=False)`) helps for multi-variant tests; pandas 3.0 changes do not alter the statistics.

### Interview angle
> [!question] How it is asked
> "Design an experiment to test a new checkout page. How long do you run it?"

> [!tip] Strong answer includes
> - Hypothesis, primary and guardrail metrics, randomisation unit
> - Sample size from baseline, MDE, power and alpha; duration from traffic
> - No peeking, SRM check, multiple-variant correction
> - Decision rule including practical significance and rollout plan

---

## 4. User Segmentation (Clustering)
> 🟠 Tier 2 · _Tracker hint:_ KMeans on RFM (Recency, Frequency, Monetary); StandardScaler first

### Definition
**Segmentation** groups users with similar behaviour so each group can get a tailored product, message or service level. **K-means** partitions users into $k$ clusters by minimising within-cluster sum of squared distances to centroids. Because it uses Euclidean distance, **features must be scaled** (`StandardScaler`) and heavily skewed variables (monetary value) are often log-transformed first. Choose $k$ using the elbow plot of inertia, the **silhouette score** (higher is better, range -1 to 1) and, above all, business interpretability.

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X = rfm.loc[:, ["recency", "frequency", "monetary"]].copy()
X["monetary"] = np.log1p(X["monetary"])
Xs = StandardScaler().fit_transform(X)
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(Xs)
    print(k, silhouette_score(Xs, labels))
rfm["segment"] = KMeans(n_clusters=4, n_init=10, random_state=42).fit_predict(Xs)
print(rfm.groupby("segment").mean())      # profile the clusters
```

Limits: assumes roughly spherical equal-size clusters, sensitive to outliers and initialisation; alternatives are hierarchical clustering, Gaussian mixtures and DBSCAN. Profile each cluster and name it (e.g., "loyal high spenders", "lapsing").

### Example
Customer A: recency 10 days, frequency 5, monetary Rs 20,000. Customer B: recency 200, frequency 5, monetary Rs 20,500. Raw distance $=\sqrt{190^2+0^2+500^2}=\sqrt{286{,}100}\approx535$; the 500 rupee gap dominates the 190-day recency gap, so unscaled K-means would essentially cluster on spend. After standardising, recency and spend contribute comparably.

### In the news
See news box. Not specific to a news item; the scikit-learn pipeline works unchanged under pandas 3.0, but confirm column dtypes (`str` vs `object`) before `fit`.

### Interview angle
> [!question] How it is asked
> "How would you segment our customers, and what would we do with the segments?"

> [!tip] Strong answer includes
> - Features (RFM plus behaviour), scaling, log transform for skew
> - Choosing k with elbow/silhouette and business sense
> - Profiling clusters and mapping each to an action (retention offer, upsell)
> - Stability check (re-run on new data) and alternatives to K-means

---

## 5. RFM Analysis
> 🟠 Tier 2 · _Tracker hint:_ df.groupby('customer') agg last_purchase, count, sum; score each dimension

### Definition
**RFM** scores customers on **Recency** (days since last purchase; lower is better), **Frequency** (number of orders) and **Monetary** (total spend). Compute them per customer relative to a snapshot date, score each into quintiles (1-5), and combine into segments such as Champions (R5 F5 M5), Loyal, At Risk (low R, high F/M), and Lost.

```python
import pandas as pd
snap = df["order_date"].max() + pd.Timedelta(days=1)
rfm = df.groupby("customer_id").agg(
    last_purchase=("order_date", "max"),
    frequency=("order_id", "nunique"),
    monetary=("amount", "sum"))
rfm["recency"] = (snap - rfm["last_purchase"]).dt.days
rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])             # recent = high score
rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["M"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
rfm["score"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)
```

`rank(method="first")` avoids duplicate bin edges when many customers have the same frequency. Quintile scoring is relative (a top-quintile customer in a low-spend business is not necessarily valuable in absolute terms).

### Example
Snapshot date 1 Oct 2026. Customer C last bought on 19 Sep (recency 12 days), placed 8 orders, spent Rs 24,000 in total: scores R=5, F=5, M=5, so "555" Champion: reward with early access, not discounts. Customer D: recency 240 days, 6 orders, Rs 18,000: R=1, F=4, M=4, "At Risk": send a win-back message before the customer is lost.

### In the news
See news box. In pandas 3.0, `groupby().agg()` with named aggregation (as above) is unchanged; the `str` dtype affects only string key columns.

### Interview angle
> [!question] How it is asked
> "How would you identify our best customers and those about to churn?"

> [!tip] Strong answer includes
> - Define R, F, M with a snapshot date; quintile scoring
> - Segments mapped to actions (reward, upsell, win-back)
> - Limitations: ignores margin, product mix, and is backward-looking
> - Extension to CLV or clustering on RFM

---

## 6. DAU/MAU Calculation
> 🟠 Tier 2 · _Tracker hint:_ df[df['date']==today]['user'].nunique() / df[df['date'].dt.month==month]['user'].nunique()

### Definition
**DAU** = distinct users active on a day; **MAU** = distinct users active in a month (or rolling 30 days). **Stickiness** $=\frac{DAU}{MAU}$ (often using average DAU over the month): the share of monthly users who show up on a typical day; 100% would mean everyone comes daily. "Active" must be defined by a meaningful action (not just opening the app). Unique users are not additive across days, so you cannot sum DAU to get MAU.

```python
df["date"] = pd.to_datetime(df["event_time"]).dt.normalize()
dau = df.groupby("date")["user_id"].nunique()
mau = df.groupby(df["date"].dt.to_period("M"))["user_id"].nunique()
avg_dau = dau.groupby(dau.index.to_period("M")).mean()
stickiness = avg_dau / mau
# rolling 30-day MAU:
events = df.drop_duplicates(["date", "user_id"])
```

Related: WAU, new vs returning vs resurrected users, L7/L28 (days active out of last 7/28). Remember the metric depends on the product's natural frequency (a daily habit app vs a monthly bill-pay app); compare to the product's own trend and category.

### Example
In a month, average DAU = 30,000 and MAU = 100,000: stickiness $=30{,}000/100{,}000=30\%$ (about 9 days of use per user per 30-day month on average). If MAU grows to 120,000 but DAU stays 30,000, stickiness falls to 25%: growth came from casual users.

### In the news
See news box. No specific news; the code uses `dt.to_period`, which behaves the same on pandas 3.0 (check datetime resolution changes if you compare with exact timestamps).

### Interview angle
> [!question] How it is asked
> "DAU is flat but MAU is rising. What does that mean and what would you do?"

> [!tip] Strong answer includes
> - Definition of an active user and why DAU/MAU is not additive
> - Interpret stickiness vs product's natural frequency
> - Decompose growth: new, retained, resurrected, churned
> - Next steps: engagement features, notifications, cohort view

---

## 7. Churn Prediction
> 🟠 Tier 2 · _Tracker hint:_ Label churned users; Logistic Regression or XGBoost; feature engineering on usage

### Definition
Churn prediction is supervised classification: predict which users will leave in a future window. Steps:

1. **Define churn** (e.g., no activity or subscription cancelled in the next 30 days).
2. **Observation vs prediction window**: build features only from data *before* the cutoff date, label from the period *after*. Using later data in features is **leakage** and gives fake accuracy.
3. **Features**: recency, frequency trends, support tickets, plan, tenure, feature usage, payment failures.
4. **Model**: logistic regression (interpretable baseline), gradient boosting (XGBoost/LightGBM) for accuracy.
5. **Evaluate** with ROC-AUC, precision/recall, lift, not accuracy (imbalanced classes). Split by time.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
X = feat.loc[:, ["recency", "freq_30d", "freq_trend", "tickets", "tenure_days"]]
y = feat["churned_next_30d"]
split = feat["cutoff"] < "2026-06-01"
clf = LogisticRegression(max_iter=1000, class_weight="balanced").fit(X[split], y[split])
p = clf.predict_proba(X[~split])[:, 1]
print(roc_auc_score(y[~split], p))
```

Turn scores into action: contact the top-risk decile with an offer, whose cost must be less than the expected saved value; evaluate with a holdout test.

### Example
1,000 users, 100 churners (10%). A model predicting "nobody churns" has 90% accuracy and zero value. A useful model: top-decile (100 highest-risk users) contains 40 churners: precision 40%, recall $40/100=40\%$, **lift** $=40\%/10\%=4\times$. If a retention offer costs Rs 100 and saves Rs 1,500 of value with 25% success on churners: expected value per contacted user $=0.40\times0.25\times1500-100=50$ rupees (positive, so target this decile). (Illustrative numbers.)

### In the news
See news box. pandas 3.0 string dtype and Copy-on-Write affect feature engineering code; always rebuild features with `.loc`/`assign` and pin library versions for reproducible models.

### Interview angle
> [!question] How it is asked
> "How would you build a churn model for a subscription or e-commerce product?"

> [!tip] Strong answer includes
> - Precise churn definition, windows and leakage avoidance
> - Imbalance handling and the right metrics (PR-AUC, lift, recall at top-k)
> - Interpretability and action plan (who to contact, what offer, uplift test)
> - Monitor drift; distinguish voluntary vs involuntary churn (payment failure)

---

## 8. Event Tracking Analysis
> 🟠 Tier 2 · _Tracker hint:_ Parse event logs; sessionize by user+time gap; click-path analysis

### Definition
Product telemetry is an **event log**: rows of (user_id, timestamp, event_name, properties). Analysis steps: parse and clean (timestamps to UTC, dedupe, drop bots), **sessionize** (a new session starts when the gap between consecutive events of a user exceeds a threshold, commonly 30 minutes), then compute session metrics (length, events per session, bounce) and **click paths** (sequences, top next-steps, drop-off points).

```python
import pandas as pd
ev = ev.sort_values(["user_id", "ts"])
gap = ev.groupby("user_id")["ts"].diff()
new_sess = gap.isna() | (gap > pd.Timedelta(minutes=30))
ev["session_id"] = new_sess.groupby(ev["user_id"]).cumsum()
sess = ev.groupby(["user_id", "session_id"]).agg(
    start=("ts", "min"), end=("ts", "max"), n_events=("event", "size"))
sess["duration_min"] = (sess["end"] - sess["start"]).dt.total_seconds() / 60

ev["next_event"] = ev.groupby(["user_id", "session_id"])["event"].shift(-1)
paths = ev.groupby(["event", "next_event"], dropna=False).size().sort_values(ascending=False)
```

Pitfalls: client clocks, duplicate events from retries, schema changes between app versions, timezone and last-event duration (a single-event session has zero duration).

### Example
User U has events at 10:00, 10:10 and 10:50. The gap from 10:10 to 10:50 is 40 minutes (> 30), so the log has 2 sessions: session 1 (10:00-10:10, 2 events, 10 min) and session 2 (10:50, 1 event, 0 min). The paths table might show "search to product_view" as the most common transition and "cart to exit" as the main drop-off.

### In the news
See news box. For large logs (millions of rows) pandas 3.0 string dtype saves memory on event-name columns; for billions of rows use SQL or Spark.

### Interview angle
> [!question] How it is asked
> "Given raw clickstream logs, how would you define sessions and find where users get stuck?"

> [!tip] Strong answer includes
> - Sessionisation rule (inactivity gap) with justification and sensitivity
> - Path analysis, funnel and drop-off identification
> - Data quality: duplicates, bots, timezone, schema versions
> - Scaling: SQL window functions (`LAG`) or Spark for very large data

---

## 9. ⭐ Advanced: Customer Lifetime Value and Retention Curves
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Customer lifetime value (CLV)** estimates the profit a customer generates over the relationship. A simple model with constant monthly churn $c$:
$$CLV=\frac{ARPU\times\text{gross margin}}{c}$$
because expected lifetime is $1/c$ months for geometric survival. With discounting rate $d$ per month: $CLV=\frac{m}{c+d}$ approximately where $m$ is monthly margin per user. Compare with **CAC** (customer acquisition cost): the usual health check is $CLV/CAC>3$ and payback period (months to recover CAC) under about 12 months, though thresholds vary by business.

Retention is rarely a constant hazard: curves flatten as loyal users remain. Estimate **survival curves** with Kaplan-Meier (`lifelines` library) and use probabilistic models (BG/NBD plus Gamma-Gamma) for non-contractual settings.

```python
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter().fit(durations=users["tenure_months"], event_observed=users["churned"])
kmf.plot_survival_function()
```

### Example
ARPU = Rs 200/month, gross margin 50%, monthly churn 5%: $CLV=\frac{200\times0.5}{0.05}=$ Rs 2,000. If CAC is Rs 600, CLV/CAC $=3.3$ and payback $=600/100=6$ months. If churn worsens to 8%, CLV falls to Rs 1,250 and the ratio to about 2.1.

### In the news
See news box. Analysis libraries such as `lifelines` depend on the pandas version; check compatibility with pandas 3.0 before upgrading.

### Interview angle
> [!question] How it is asked
> "How would you decide how much we can spend to acquire a customer?"

> [!tip] Strong answer includes
> - CLV formula with margin (not revenue) and churn; cohort-based retention for accuracy
> - CLV/CAC and payback period; segment by channel
> - Limits: constant churn assumption, discounting, uncertainty
> - Use it to set budgets and bids, and to prioritise retention vs acquisition

---

## 10. ⭐ Advanced: Variance Reduction (CUPED) and Sequential Testing
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Experiments often lack traffic. **CUPED** (Controlled-experiment Using Pre-Experiment Data) reduces metric variance with a pre-experiment covariate $X$ (e.g., each user's spend in the 4 weeks before the test):
$$Y_{adj}=Y-\theta\,(X-\bar{X}),\qquad \theta=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}$$
The adjusted metric has variance $(1-\rho^2)\operatorname{Var}(Y)$, where $\rho$ is the correlation between $X$ and $Y$; the treatment effect estimate stays unbiased because $X$ is measured before randomisation. Smaller variance means a smaller required sample or a shorter test.

**Sequential testing** (e.g., SPRT, alpha-spending, always-valid p-values) lets you look at results during the test without inflating false positives, which fixed-horizon tests do not allow.

```python
import numpy as np
theta = np.cov(x_pre, y, ddof=1)[0, 1] / np.var(x_pre, ddof=1)
y_cuped = y - theta * (x_pre - x_pre.mean())
```

Other tools: stratification, ratio-metric delta method, multiple-testing correction across variants and metrics.

### Example
If pre-test and in-test spend correlate at $\rho=0.7$, variance falls by $\rho^2=49\%$ (to 51% of the original), so the needed sample size falls by about the same 49%. A test needing 100,000 users per arm would need roughly 51,000.

### In the news
See news box. SciPy 1.16's `tukey_hsd`/`f_oneway` `equal_var` options handle multi-variant comparisons after CUPED-style adjustment.

### Interview angle
> [!question] How it is asked
> "Our experiments take 6 weeks because traffic is low. How could we make them faster without losing rigour?"

> [!tip] Strong answer includes
> - Variance reduction with pre-experiment covariates (CUPED), stratification
> - Larger effect metrics, better proxy metrics, or higher-traffic surfaces
> - Sequential testing for early stopping with valid error control
> - Trade-offs: complexity, bias risk if the covariate is post-treatment

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
