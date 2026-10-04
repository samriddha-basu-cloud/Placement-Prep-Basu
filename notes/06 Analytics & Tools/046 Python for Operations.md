---
tags: [analytics-tools, tier2]
area: Analytics & Tools
topic: "Python for Operations"
tier: Tier 2
roles: Operations / PM
status: complete
subtopics: 12
---
# Python for Operations

⬅ [[045 SQL for Operations Analytics]] · [[_Index - Analytics & Tools|Analytics & Tools]] · [[047 MIS & Dashboard Design]] ➡

> **Area:** Analytics & Tools · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / PM

## Sub-topics in this note
1. [[#1. Pandas for Data Analysis]]
2. [[#2. NumPy Basics]]
3. [[#3. Data Cleaning]]
4. [[#4. Demand Forecasting in Python]]
5. [[#5. Data Visualization]]
6. [[#6. Supply Chain Optimization (PuLP)]]
7. [[#7. Simulation (SimPy)]]
8. [[#8. Inventory Analysis Scripts]]
9. [[#9. API Integration]]
10. [[#10. Jupyter Notebooks]]
11. [[#11. ⭐ Advanced: Python Automation of Recurring Ops Reports]]
12. [[#12. ⭐ Advanced: Forecast Accuracy Metrics and Bias]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Python keeps getting faster and more parallel
> **Python 3.14 released (7 Oct 2025).** The release makes free-threaded Python (no GIL) officially supported (PEP 779), adds template strings (PEP 750), multiple interpreters in the standard library (PEP 734), a `compression.zstd` module and an experimental JIT in the official macOS and Windows binaries. For analysts this means heavier simulations and data jobs can use multiple cores without leaving Python. ([Source](https://www.python.org/downloads/release/python-3140/))
> 
> **Power BI keeps tightening its Python/R hooks (Nov 2025 feature summary).** Microsoft announced that from 1 May 2026 R and Python visuals will no longer render in "Embed for your customers" scenarios, while it pushed Copilot and a Model Context Protocol server for agents querying semantic models. Lesson: ship analytics as code or governed models, not as fragile in-dashboard scripts. ([Source](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-November-2025-Feature-Summary/ba-p/5173992))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Pandas for Data Analysis
> 🟠 Tier 2 · _Tracker hint:_ DataFrame, Series; read_csv, groupby, merge, pivot_table

### Definition
**pandas** is the workhorse library for tabular data. A **Series** is a labelled 1-D array; a **DataFrame** is a 2-D table of Series sharing an index. Core operations an operations analyst uses daily:

```python
import pandas as pd

orders = pd.read_csv("orders.csv", parse_dates=["order_date"])
items  = pd.read_excel("sku_master.xlsx")

df = orders.merge(items, on="sku", how="left")          # VLOOKUP / join
df["revenue"] = df["qty"] * df["unit_price"]

by_wh = (df.groupby("warehouse")
           .agg(orders=("order_id", "nunique"), revenue=("revenue", "sum"))
           .sort_values("revenue", ascending=False))

pv = df.pivot_table(index="warehouse", columns=df["order_date"].dt.to_period("M"),
                    values="revenue", aggfunc="sum", fill_value=0)
```

Mapping to Excel: `merge` is VLOOKUP/INDEX-MATCH at scale, `groupby` is a pivot table, `pivot_table` is a pivot table with a column dimension. Key join types: `inner`, `left`, `right`, `outer`. Always check the row count after a merge: a many-to-many key silently multiplies rows.

### Example
A 5 lakh-row order file is too big to be comfortable in Excel. In pandas, `df.groupby("pincode")["delivery_days"].mean()` gives average delivery days per pincode in one line, and `merge` attaches the carrier name from a master list. If orders = 500,000 and the left merge returns 612,000 rows, the master list has duplicate SKUs: a data bug caught by a simple `len()` check.

### In the news
See news box. Python 3.14's free-threading and speed work matter most for large data jobs, but the daily skill remains clean pandas.

### Interview angle
> [!question] How it is asked
> "How would you analyse a large order dataset?" or "Difference between merge, join and concat?"

> [!tip] Strong answer includes
> - Names read, merge, groupby, pivot_table with the Excel equivalent of each
> - Mentions validating row counts after joins
> - Says why Python over Excel: size, repeatability, version control
> - A concrete business question answered (e.g. late deliveries by carrier)

---

## 2. NumPy Basics
> 🟠 Tier 2 · _Tracker hint:_ Arrays; mathematical operations; broadcasting; random module

### Definition
**NumPy** provides the `ndarray`: a fixed-type, contiguous n-dimensional array on which operations are **vectorised** (done in compiled code, no Python loop). pandas is built on it.

```python
import numpy as np
demand = np.array([120, 135, 150, 128])
demand.mean(), demand.std(ddof=1)          # sample std dev
cost = np.array([[4, 6, 8], [5, 3, 7]])    # 2x3
cost * 1.05                                # scalar broadcast
cost + np.array([1, 0, 2])                 # row vector broadcast across rows
rng = np.random.default_rng(42)
sim = rng.normal(loc=100, scale=15, size=10_000)   # demand simulation
np.percentile(sim, 95)
```

**Broadcasting** stretches the smaller array across the larger when trailing dimensions match or equal 1, so you avoid loops. The `random` module (`default_rng`) generates reproducible simulated demand, lead times and Monte Carlo scenarios. Remember `ddof=1` for sample standard deviation, because NumPy defaults to population ($ddof=0$).

### Example
Monte Carlo safety stock: simulate 10,000 lead-time demands from $N(200, 40^2)$ and take the 95th percentile. The analytic answer is $200 + 1.645 \times 40 = 265.8$; the simulation should land close (about 265 to 267).

### In the news
See news box. Free-threaded Python makes CPU-bound simulations like this easier to parallelise.

### Interview angle
> [!question] How it is asked
> "What is vectorisation / broadcasting?" or "How would you simulate demand uncertainty?"

> [!tip] Strong answer includes
> - Vectorised vs loop and why it is faster
> - Broadcasting rule in one sentence with an example
> - Seeded random generator for reproducibility
> - Link to a business use: Monte Carlo for safety stock or capacity

---

## 3. Data Cleaning
> 🟠 Tier 2 · _Tracker hint:_ Handle nulls: fillna, dropna; duplicates; dtype conversion; outliers

### Definition
Analysts spend most of their time cleaning. Standard moves:

```python
df.isna().sum()                              # audit nulls per column
df["lead_time"] = df["lead_time"].fillna(df["lead_time"].median())
df = df.dropna(subset=["sku", "qty"])        # drop rows missing key fields
df = df.drop_duplicates(subset=["order_id", "sku"])
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
# IQR outlier rule
q1, q3 = df["qty"].quantile([0.25, 0.75]); iqr = q3 - q1
mask = df["qty"].between(q1 - 1.5*iqr, q3 + 1.5*iqr)
clean = df[mask]
```

Rules: never silently delete; log how many rows each step removes. Choose imputation to match the data (median for skewed, forward-fill for time series, domain default such as zero demand only if truly zero). Outliers may be errors (typo of 10,000 for 100) or real events (a bulk order), so investigate before removing.

### Example
Daily sales for a SKU: [20, 22, 19, 25, 21, 2100]. $Q1 \approx 20.25$, $Q3 = 24.25$ (linear interpolation), IQR $= 4.0$, upper fence $= 24.25 + 1.5 \times 4 = 30.25$, so 2100 is flagged. A call to the store reveals a missing decimal: the real value is 21.0.

### In the news
See news box. The Power BI note is relevant: clean data upstream in code or the model, so dashboards stay trustworthy.

### Interview angle
> [!question] How it is asked
> "How do you handle missing values and outliers?"

> [!tip] Strong answer includes
> - Audit first (`isna().sum()`), then decide per column
> - Imputation choice justified (mean vs median vs forward-fill)
> - Outlier flagged, investigated, then removed or kept with reason
> - Documenting each transformation for audit

---

## 4. Demand Forecasting in Python
> 🟠 Tier 2 · _Tracker hint:_ statsmodels ARIMA; Prophet by Meta; sklearn forecasting

### Definition
Three common routes:

- **statsmodels ARIMA / SARIMAX**: classical time-series, ARIMA$(p,d,q)$ with $p$ autoregressive lags, $d$ differences for stationarity, $q$ moving-average lags; seasonal order for monthly seasonality.
- **Prophet** (Meta): additive model $y(t)=g(t)+s(t)+h(t)+\epsilon$ (trend, seasonality, holidays); robust to missing data, easy to add Indian festival effects.
- **scikit-learn**: turn forecasting into regression with lag features, rolling means, calendar variables (gradient boosting, random forest). Validate with time-based splits, never random shuffling.

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX
m = SARIMAX(y, order=(1,1,1), seasonal_order=(1,1,1,12)).fit(disp=False)
fc = m.forecast(12)

from prophet import Prophet
p = Prophet(yearly_seasonality=True); p.fit(df.rename(columns={"date":"ds","qty":"y"}))
future = p.make_future_dataframe(periods=12, freq="MS"); out = p.predict(future)
```

Measure with MAPE $=\frac{100}{n}\sum \left|\frac{A_t-F_t}{A_t}\right|$, WAPE or RMSE, and always compare with a naive or seasonal-naive benchmark.

### Example
Actual [100, 120, 110], forecast [90, 130, 100]. Absolute errors 10, 10, 10; percentage errors 10%, 8.33%, 9.09%; MAPE $= (10+8.33+9.09)/3 = 9.14\%$. If a seasonal-naive forecast gives 15%, the model adds value.

### In the news
See news box. Python 3.14 and the broader ecosystem keep lowering the cost of running many SKU-level models in parallel.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand for 5,000 SKUs?" or "ARIMA vs Prophet vs ML?"

> [!tip] Strong answer includes
> - Segment SKUs (ABC/XYZ): simple methods for C items, richer models for A
> - Benchmarks, time-based cross-validation, MAPE/WAPE and bias
> - Handles seasonality, promotions and holidays
> - Forecast feeds inventory/planning decisions, not just accuracy for its own sake

---

## 5. Data Visualization
> 🟠 Tier 2 · _Tracker hint:_ Matplotlib, Seaborn; line, bar, scatter, heatmap, boxplot

### Definition
**Matplotlib** is the base plotting library; **Seaborn** adds statistical plots with nicer defaults on top of pandas.

| Question | Chart | Call |
|---|---|---|
| Trend over time | Line | `plt.plot` / `sns.lineplot` |
| Compare categories | Bar | `sns.barplot` |
| Relationship of two numbers | Scatter | `sns.scatterplot` |
| Pattern across two dimensions | Heatmap | `sns.heatmap(pivot, annot=True)` |
| Spread and outliers | Boxplot | `sns.boxplot` |

```python
import matplotlib.pyplot as plt, seaborn as sns
fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(data=df, x="carrier", y="delivery_days", ax=ax)
ax.set(title="Delivery days by carrier", ylabel="Days")
plt.tight_layout(); fig.savefig("carrier.png", dpi=150)
```

Good practice: title that states the insight, labelled axes with units, one message per chart, sorted bars, no 3-D effects.

### Example
A boxplot of delivery days by carrier shows Carrier B has the same median (3 days) as Carrier A but a long upper whisker (up to 9 days). The mean hides this; the chart tells you to manage the tail through SLA penalties.

### In the news
See news box. The shift away from in-dashboard Python visuals suggests exporting static charts or building them in governed BI tools for broad distribution.

### Interview angle
> [!question] How it is asked
> "Which chart would you use to show X?" or "How do you present analysis to senior managers?"

> [!tip] Strong answer includes
> - Chart matched to the question
> - Heatmap/boxplot for operations patterns (day-hour load, delivery spread)
> - Clean design and a one-line takeaway
> - Knows when to hand off to Power BI or Tableau

---

## 6. Supply Chain Optimization (PuLP)
> 🟠 Tier 2 · _Tracker hint:_ Linear programming; minimize cost; transportation model

### Definition
**PuLP** is a Python modeller for linear and integer programs. A **transportation problem** minimises shipping cost $\sum_{i,j} c_{ij}x_{ij}$ subject to supply $\sum_j x_{ij}\le s_i$, demand $\sum_i x_{ij}= d_j$ and $x_{ij}\ge 0$.

```python
import pulp
plants = {"P1": 100, "P2": 150}
mkts   = {"M1": 80, "M2": 90, "M3": 80}
cost = {("P1","M1"):4, ("P1","M2"):6, ("P1","M3"):8,
        ("P2","M1"):5, ("P2","M2"):3, ("P2","M3"):7}
prob = pulp.LpProblem("transport", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", cost.keys(), lowBound=0)
prob += pulp.lpSum(cost[k]*x[k] for k in cost)
for i,s in plants.items(): prob += pulp.lpSum(x[i,j] for j in mkts) <= s
for j,d in mkts.items():   prob += pulp.lpSum(x[i,j] for i in plants) == d
prob.solve(pulp.PULP_CBC_CMD(msg=False))
print(pulp.LpStatus[prob.status], pulp.value(prob.objective))
```

Add binary variables for facility open/close decisions (mixed-integer). Read **shadow prices** to see the value of one more unit of capacity.

### Example
For the data above, total supply (250) equals total demand (250). The optimum is P1 to M1 = 80, P1 to M3 = 20, P2 to M2 = 90, P2 to M3 = 60: cost $= 80(4)+20(8)+90(3)+60(7) = 320+160+270+420 = 1170$ cost units. Check: sending more M1 volume from P2 instead would cost 1 more per unit.

### In the news
See news box. Shipping optimisation models like this are increasingly run as scheduled Python jobs rather than manual Solver sessions.

### Interview angle
> [!question] How it is asked
> "How would you decide which warehouse serves which region?"

> [!tip] Strong answer includes
> - Decision variables, objective, constraints stated in words first
> - Balanced vs unbalanced problem (dummy node)
> - Sensitivity: shadow prices and what-if scenarios
> - Practical caveats: data quality, service-level constraints, integer decisions

---

## 7. Simulation (SimPy)
> 🟠 Tier 2 · _Tracker hint:_ Discrete event simulation; queue modeling; capacity analysis

### Definition
**Discrete-event simulation (DES)** advances time from event to event (arrival, service start, service end). **SimPy** models processes as Python generators with shared `Resource` objects.

```python
import simpy, random
def customer(env, name, dock, svc_mean, waits):
    arrive = env.now
    with dock.request() as req:
        yield req
        waits.append(env.now - arrive)
        yield env.timeout(random.expovariate(1/svc_mean))

def source(env, dock, inter_mean, svc_mean, waits):
    i = 0
    while True:
        yield env.timeout(random.expovariate(1/inter_mean))
        i += 1; env.process(customer(env, i, dock, svc_mean, waits))

random.seed(1); env = simpy.Environment(); waits = []
dock = simpy.Resource(env, capacity=2)
env.process(source(env, dock, 10, 15, waits)); env.run(until=8*60)
```

Use it when closed-form queueing is too restrictive (breakdowns, shifts, priorities). Run many replications and report means with confidence intervals. For a single-queue M/M/c baseline, utilisation is $\rho = \lambda/(c\mu)$ and must be below 1.

### Example
Trucks arrive every 10 minutes on average and unloading takes 15 minutes. One dock: $\rho = 15/10 = 1.5 > 1$, queue grows without bound. Two docks: $\rho = 15/(2\times10) = 0.75$, a stable system. Simulation then tells you the average wait and the 95th percentile wait to decide if a third dock is justified.

### In the news
See news box. Free-threaded Python helps run hundreds of replications in parallel.

### Interview angle
> [!question] How it is asked
> "How would you decide how many docks or counters we need?"

> [!tip] Strong answer includes
> - Utilisation and queue stability check first
> - When simulation beats formulas
> - Replications, warm-up period, confidence intervals
> - Link to cost trade-off: waiting/demurrage vs extra resource

---

## 8. Inventory Analysis Scripts
> 🟠 Tier 2 · _Tracker hint:_ EOQ, ROP, safety stock calculators; ABC classification code

### Definition
Key formulas: $EOQ=\sqrt{\dfrac{2DS}{H}}$; safety stock $SS = z\,\sigma_d\sqrt{L}$ (daily demand variability, constant lead time); reorder point $ROP = \bar d L + SS$.

```python
import math, pandas as pd
def eoq(D, S, H): return math.sqrt(2*D*S/H)
def safety_stock(z, sd_daily, L): return z*sd_daily*math.sqrt(L)
def rop(d, L, ss): return d*L + ss

df = pd.DataFrame({"sku": ["A","B","C","D"], "annual_value": [900, 60, 30, 10]})
df = df.sort_values("annual_value", ascending=False)
df["cum_pct"] = df["annual_value"].cumsum() / df["annual_value"].sum() * 100
df["class"] = pd.cut(df["cum_pct"], [0,80,95,100], labels=list("ABC"))
```

ABC cut-offs of 80/95/100% of cumulative value are conventional, not fixed laws. Layer XYZ (demand variability) on top for policy selection.

### Example
$D=12{,}000$ units/year, $S=₹500$ per order, $H=₹20$ per unit-year: $EOQ=\sqrt{2\times12000\times500/20}=\sqrt{600{,}000}\approx 774.6$ units. With $d=40$/day, $L=5$ days, $\sigma_d=8$, $z=1.65$ (95%): $SS=1.65\times8\times\sqrt5=29.5$; $ROP=40\times5+29.5=229.5\approx 230$ units.

### In the news
See news box. Packaging these calculators as importable, tested functions is what keeps them auditable.

### Interview angle
> [!question] How it is asked
> "How would you set reorder points for 10,000 SKUs?"

> [!tip] Strong answer includes
> - Segment with ABC/XYZ first
> - Formula for EOQ, safety stock, ROP with assumptions (constant demand, normal error)
> - Automate and parameterise service level per class
> - Review exceptions, not every SKU

---

## 9. API Integration
> 🟠 Tier 2 · _Tracker hint:_ requests library; REST API calls; JSON parsing for SCM data

### Definition
An **API** lets programs exchange data. **REST** APIs use HTTP verbs (GET, POST, PUT, DELETE) on URLs and typically return **JSON**.

```python
import requests, pandas as pd
url = "https://api.example.com/v1/shipments"
headers = {"Authorization": "Bearer <TOKEN>"}
r = requests.get(url, headers=headers, params={"status": "in_transit"}, timeout=30)
r.raise_for_status()                 # fail loudly on 4xx/5xx
data = r.json()
df = pd.json_normalize(data["results"])      # flatten nested JSON
```

Good practice: keep secrets in environment variables, set timeouts, handle pagination and rate limits (retry with back-off), validate the schema, and log failures. Common SCM sources: carrier tracking, weather and port data, ERP/WMS REST endpoints, GST e-invoice and e-way bill portals.

### Example
Pull in-transit shipments every hour, normalise the JSON, compare `eta` with `promised_date`, and email a list of shipments predicted to be late by more than 24 hours. This replaces a manual tracking-site check.

### In the news
See news box. Microsoft's remote Model Context Protocol server for Power BI shows APIs are also becoming the way AI agents consume governed data.

### Interview angle
> [!question] How it is asked
> "How would you get live carrier data into your dashboard?"

> [!tip] Strong answer includes
> - GET request, JSON, normalise into a table
> - Authentication, pagination, rate limits, retries
> - Scheduling and storage (not a one-off script)
> - Security of tokens

---

## 10. Jupyter Notebooks
> 🟠 Tier 2 · _Tracker hint:_ Interactive analysis; markdown cells; sharing insights

### Definition
A **Jupyter notebook** mixes code cells, output (tables, charts) and Markdown narrative in one document. It is ideal for exploration, prototypes and explaining analysis; less ideal for production pipelines.

Practices: restart kernel and run all before sharing (hidden state is the commonest bug), put imports and parameters at top, use Markdown headings for the story (question, data, method, finding, recommendation), keep cells short and move reusable code into `.py` modules. Share via exported HTML/PDF (`jupyter nbconvert --to html notebook.ipynb`), GitHub, or hosted notebooks such as Colab. Do not commit secrets or confidential data.

### Example
A notebook titled "Why OTIF fell in Q3": load shipments, clean, chart OTIF by lane, test one hypothesis per section, end with a three-bullet recommendation. Exported to HTML, a manager reads it without Python installed.

### In the news
See news box. As embedded Python visuals are restricted in BI embedding, notebooks plus exported outputs remain a safe sharing route.

### Interview angle
> [!question] How it is asked
> "How do you document and share your analysis?"

> [!tip] Strong answer includes
> - Narrative structure with a clear recommendation
> - Reproducibility (run-all, seeds, requirements)
> - Awareness of notebook limits vs scripts
> - Data confidentiality

---

## 11. ⭐ Advanced: Python Automation of Recurring Ops Reports
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Turn a weekly manual report into a scheduled script: extract (SQL/API/Excel), transform (pandas), load (to Excel/Sheets/DB), notify (email/Teams). Use `argparse` for parameters, `logging` for audit, unit tests for key calculations, and a scheduler: cron, Windows Task Scheduler, Airflow or a cloud function.

```python
import pandas as pd, smtplib
from email.message import EmailMessage
df = pd.read_sql("select * from otif_weekly", conn)
df.to_excel("otif_weekly.xlsx", index=False)
msg = EmailMessage(); msg["Subject"] = "Weekly OTIF"; msg["To"] = "ops@example.com"
msg.add_attachment(open("otif_weekly.xlsx","rb").read(), maintype="application",
                   subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                   filename="otif_weekly.xlsx")
```

Measure benefit as hours saved per month times loaded cost, and error rate reduction.

### Example
A 3-hour weekly report automated to a 5-minute run saves $3 \times 52 = 156$ hours a year for one analyst, before counting fewer manual errors.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "Tell me about a process you automated."

> [!tip] Strong answer includes
> - Baseline time and error rate, then after
> - Monitoring and failure alerts
> - Handover/documentation so it outlives you
> - Honest scope: do not claim tools you have not used

---

## 12. ⭐ Advanced: Forecast Accuracy Metrics and Bias
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- $MAD=\frac1n\sum|A_t-F_t|$; $RMSE=\sqrt{\frac1n\sum(A_t-F_t)^2}$ (penalises large misses).
- $WAPE=\dfrac{\sum|A_t-F_t|}{\sum A_t}$: robust when some actuals are near zero, where MAPE explodes.
- **Bias** $=\dfrac{\sum(F_t-A_t)}{\sum A_t}$; persistent positive bias means over-forecasting and excess stock.
- **Tracking signal** $=\dfrac{\sum(A_t-F_t)}{MAD}$; values beyond about $\pm4$ signal a biased model.

```python
import numpy as np
a, f = np.array([100,120,110]), np.array([90,130,100])
wape = np.abs(a-f).sum() / a.sum()
bias = (f-a).sum() / a.sum()
```

### Example
With the data above: $\sum|A-F|=30$, $\sum A=330$, so $WAPE=9.09\%$. $\sum(F-A)=-10+10-10=-10$, so bias $=-3.03\%$ (slight under-forecast).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "How do you judge whether a forecast is good?"

> [!tip] Strong answer includes
> - Accuracy and bias reported together
> - WAPE for intermittent demand
> - Benchmark vs naive; segment-level reporting
> - Link to inventory cost of error

---
## 🔗 Go deeper: expansion notes
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
