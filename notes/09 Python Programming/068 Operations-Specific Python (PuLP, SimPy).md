---
tags: [python-programming, tier1]
area: Python Programming
topic: "Operations-Specific Python (PuLP, SimPy)"
tier: Tier 1
roles: Operations
status: complete
subtopics: 12
---
# Operations-Specific Python (PuLP, SimPy)

⬅ [[067 Statistical Analysis in Python]] · [[_Index - Python Programming|Python Programming]] · [[069 Python for Product Analytics]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. EOQ & Inventory Calculator]]
2. [[#2. ABC Classification]]
3. [[#3. Linear Programming (PuLP)]]
4. [[#4. Simulation with SimPy]]
5. [[#5. Gantt Chart in Python]]
6. [[#6. Network Optimization (NetworkX)]]
7. [[#7. Process Capability (from scratch)]]
8. [[#8. OEE Calculator Script]]
9. [[#9. Regression for Forecasting]]
10. [[#10. Data Pipeline Automation]]
11. [[#11. ⭐ Advanced: Vehicle Routing and Scheduling with OR-Tools]]
12. [[#12. ⭐ Advanced: Simulation of Inventory Policies (s, Q) with Monte Carlo]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the operations-research toolchain in Python keeps getting faster
> **Google OR-Tools v9.12 (released 17 February 2025).** Last release to support Python 3.8 and adds Python 3.13 support; CP-SAT gets improved `no_overlap_2d` propagation and new search heuristics; HiGHS support is added to the Model Builder and Xpress to MathOpt. One user reported a routing problem converging in 56 s instead of 85 s. ([OR-Tools v9.12 release](https://github.com/google/or-tools/discussions/4544))
>
> **pandas 3.0.0 (21 January 2026).** Copy-on-Write by default and a dedicated `str` dtype; chained assignment no longer works, which matters for inventory/OEE scripts that update DataFrame slices. Minimum Python is 3.11. ([pandas 3.0.0 what's new](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html))
>
> **SciPy 1.16.0 (22 June 2025).** `scipy.optimize` gets a rewritten COBYLA (PRIMA-based); HiGHS-backed `linprog`/`milp` remain the LP/MILP workhorses. ([SciPy 1.16.0 release notes](https://docs.scipy.org/doc/scipy-1.16.0/release/1.16.0-notes.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. EOQ & Inventory Calculator
> 🔴 Tier 1 · _Tracker hint:_ def eoq(D,S,H): return (2*D*S/H)**0.5; safety stock, ROP calculations

### Definition
The **Economic Order Quantity** balances ordering cost against holding cost: $Q^*=\sqrt{\frac{2DS}{H}}$ with annual demand $D$, cost per order $S$ and annual holding cost per unit $H$. At $Q^*$ the annual ordering cost equals the annual holding cost, and the minimum total cost is $TC^*=\sqrt{2DSH}$. Assumptions: constant demand, fixed lead time, no stock-outs, instantaneous replenishment.

With uncertain demand add **safety stock** $SS=z\,\sigma_d\sqrt{L}$ (demand variability only; with lead-time variability use $z\sqrt{L\sigma_d^2+d^2\sigma_L^2}$) and the **reorder point** $ROP=\bar{d}L+SS$.

```python
from math import sqrt
from scipy.stats import norm

def eoq(D, S, H):            return sqrt(2 * D * S / H)
def total_cost(D, S, H):     return sqrt(2 * D * S * H)
def safety_stock(service, sigma_d, L):  return norm.ppf(service) * sigma_d * sqrt(L)
def reorder_point(d, L, ss): return d * L + ss

print(eoq(12000, 500, 24))                 # ~707.1
ss = safety_stock(0.95, 20, 9)             # z=1.645
print(ss, reorder_point(40, 9, ss))        # ~98.7, ~458.7
```

Wrap these as functions, then apply them row-wise over a DataFrame of SKUs (`df["EOQ"] = np.sqrt(2*df.D*df.S/df.H)`).

### Example
D = 12,000 units/yr, S = Rs 500 per order, H = Rs 24/unit/yr: $Q^*=\sqrt{2\times12000\times500/24}=\sqrt{500000}\approx707$ units; orders per year $=12000/707\approx17$; $TC^*=\sqrt{2\times12000\times500\times24}=\sqrt{288{,}000{,}000}\approx$ Rs 16,971. Daily demand 40 (std 20), lead time 9 days, 95% service: $SS=1.645\times20\times3\approx98.7$; $ROP=40\times9+98.7\approx459$ units.

### In the news
See news box. These formulas are stable; what changes is the tooling: with pandas 3.0 Copy-on-Write, write `df.loc[mask, "ROP"] = ...` rather than chained assignment when updating SKU subsets.

### Interview angle
> [!question] How it is asked
> "Walk me through EOQ and how you'd compute reorder points for 5,000 SKUs." or "Code an EOQ function."

> [!tip] Strong answer includes
> - Formula, assumptions and what breaks them (discounts, variable demand)
> - Safety stock from service level and lead-time demand variability
> - Vectorised implementation across SKUs, with unit checks (annual vs daily demand)
> - Link to cycle service level vs fill rate

---

## 2. ABC Classification
> 🔴 Tier 1 · _Tracker hint:_ Use pd.qcut() or NTILE logic; classify by cumulative revenue %

### Definition
ABC analysis applies the Pareto principle: rank SKUs by annual consumption value (units x unit cost, or revenue) and classify by **cumulative share**: A = top items making about 80% of value (typically 10-20% of SKUs), B = next about 15%, C = last about 5% (the thresholds are policy choices). A items get tight control and frequent review; C items get simple rules (bulk, two-bin).

Note: `pd.qcut` or SQL `NTILE` split by **item count** (equal-sized buckets), which is not the same as splitting by cumulative value. The correct logic sorts descending, computes cumulative percentage and applies thresholds.

```python
import pandas as pd, numpy as np
df = df.sort_values("revenue", ascending=False).reset_index(drop=True)
df["cum_pct"] = df["revenue"].cumsum() / df["revenue"].sum()
df["class"] = pd.cut(df["cum_pct"], bins=[0, 0.80, 0.95, 1.0],
                     labels=["A", "B", "C"], include_lowest=True)
print(df.groupby("class", observed=True).agg(items=("sku", "count"), rev=("revenue", "sum")))
```

A common refinement: ABC x XYZ, where XYZ classifies demand variability by coefficient of variation ($CV=\sigma/\mu$). AX items (high value, stable) suit JIT and tight control; CZ items (low value, erratic) suit buffer stock.

### Example
Five SKUs with revenue 500, 250, 120, 80, 50 (total 1,000): cumulative = 50%, 75%, 87%, 95%, 100%. Using 80/95/100: SKU1 and SKU2 are **A** (75% of value, 40% of items), SKU3 and SKU4 are **B**, SKU5 is **C**. Using `qcut` into 3 buckets by count would label items by position, not by value share, which is wrong for this purpose.

### In the news
See news box. pandas 3.0 requires `observed=` thinking in groupby on categoricals; the code above passes `observed=True` explicitly to keep output predictable.

### Interview angle
> [!question] How it is asked
> "How would you classify 10,000 SKUs for inventory control in Python or SQL?"

> [!tip] Strong answer includes
> - Sort, cumulative percentage, threshold bins (not equal-count quantiles)
> - Policies per class (review frequency, safety stock, forecasting effort)
> - ABC-XYZ extension and periodic re-classification
> - Caveat: value is not criticality (a cheap but critical spare may need A treatment, i.e. VED analysis)

---

## 3. Linear Programming (PuLP)
> 🔴 Tier 1 · _Tracker hint:_ from pulp import *; prob = LpProblem(); LpVariable(); prob.solve() — transportation model

### Definition
**PuLP** is a Python modeller for linear and mixed-integer programs that calls solvers such as the bundled CBC. You declare the problem, variables, objective and constraints, then solve.

```python
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value, PULP_CBC_CMD

plants  = ["P1", "P2"];            supply = {"P1": 100, "P2": 80}
markets = ["M1", "M2", "M3"];      demand = {"M1": 60, "M2": 70, "M3": 50}
cost = {"P1": {"M1": 4, "M2": 6, "M3": 8}, "P2": {"M1": 5, "M2": 3, "M3": 7}}

prob = LpProblem("Transport", LpMinimize)
x = LpVariable.dicts("ship", (plants, markets), lowBound=0)      # continuous >= 0
prob += lpSum(cost[p][m] * x[p][m] for p in plants for m in markets)   # objective
for p in plants:   prob += lpSum(x[p][m] for m in markets) <= supply[p]
for m in markets:  prob += lpSum(x[p][m] for p in plants) >= demand[m]
prob.solve(PULP_CBC_CMD(msg=0))
print(LpStatus[prob.status], value(prob.objective))
```

Formulation template: $\min\sum_{i,j}c_{ij}x_{ij}$ s.t. $\sum_j x_{ij}\le s_i$, $\sum_i x_{ij}\ge d_j$, $x_{ij}\ge0$. Use `cat="Binary"` or `"Integer"` for yes/no or whole-unit decisions (MILP). Check `LpStatus` (Optimal, Infeasible, Unbounded) before trusting results; inspect `prob.constraints[name].pi` for shadow prices on an LP.

### Example
Supply 100 and 80 against demand 60, 70, 50 (balanced at 180) with the costs above. The optimum is P1 to M1 = 60, P1 to M3 = 40, P2 to M2 = 70, P2 to M3 = 10. Cost $=60(4)+40(8)+70(3)+10(7)=240+320+210+70=$ **Rs 840**.

### In the news
See news box. OR-Tools 9.12 added HiGHS to its Model Builder and SciPy's `linprog` already uses HiGHS, so PuLP/OR-Tools/SciPy increasingly share the same underlying open-source solver technology.

### Interview angle
> [!question] How it is asked
> "How would you decide which plant serves which market at minimum cost? Formulate it." (A consulting or SCM analytics case.)

> [!tip] Strong answer includes
> - Decision variables, objective and constraints written before code
> - Balanced vs unbalanced supply/demand and what infeasible means
> - Binary variables for opening plants (MILP) and why it is harder
> - Sensitivity: shadow price of capacity tells where to invest

---

## 4. Simulation with SimPy
> 🔴 Tier 1 · _Tracker hint:_ Discrete event simulation; queue, server, process modeling for operations

### Definition
**Discrete-event simulation (DES)** models a system as events at points in time (arrival, service start, breakdown), jumping the clock from event to event. **SimPy** implements processes as Python generator functions that `yield` events such as `env.timeout()` or resource requests. Key objects: `Environment` (clock), `Resource` (servers, capacity), `Container` (continuous stock), `Store` (items), `Process`.

```python
import simpy, random, statistics
waits = []
def customer(env, server):
    t0 = env.now
    with server.request() as req:
        yield req                               # wait in queue
        waits.append(env.now - t0)
        yield env.timeout(random.expovariate(1/3))   # mean service 3 min
def arrivals(env, server):
    while True:
        yield env.timeout(random.expovariate(1/4))   # mean inter-arrival 4 min
        env.process(customer(env, server))

random.seed(1)
env = simpy.Environment(); server = simpy.Resource(env, capacity=1)
env.process(arrivals(env, server)); env.run(until=100_000)
print(statistics.mean(waits))
```

Use simulation when queues interact, service times are random, or breakdowns and shifts matter (hospital, warehouse dock, call centre, assembly line). Always run multiple replications, discard a warm-up period and report confidence intervals, not a single run.

### Example
Single server, arrivals every 4 min on average ($\lambda=0.25$/min), service 3 min ($\mu=1/3$/min), so utilisation $\rho=0.75$. M/M/1 theory: $W_q=\frac{\lambda}{\mu(\mu-\lambda)}=\frac{0.25}{0.3333\times0.0833}=9$ min, $L_q=\lambda W_q=2.25$ customers, total time in system 12 min. The simulation above should converge to about 9 min of waiting, validating the model before you add complexity (two servers, priority customers).

### In the news
See news box. Simulation output is typically post-processed in pandas; pandas 3.0 Copy-on-Write and the `str` dtype make logging frames safer but check legacy `object`-dtype assumptions.

### Interview angle
> [!question] How it is asked
> "How would you decide how many dock doors or checkout counters we need?"

> [!tip] Strong answer includes
> - Arrival and service distributions from data; utilisation and queue metrics
> - Why simulation over closed-form queueing: complexity, non-exponential times, interactions
> - Warm-up, replications, validation against a known M/M/1 result
> - Decision linkage: cost of waiting vs cost of extra capacity

---

## 5. Gantt Chart in Python
> 🔴 Tier 1 · _Tracker hint:_ import plotly.express as px; px.timeline(df, x_start, x_end, y='Task') — project scheduling

### Definition
A **Gantt chart** shows tasks as horizontal bars along a time axis, exposing schedule, overlap, dependencies and progress. In Plotly Express use `px.timeline`, which needs datetime start and end columns.

```python
import pandas as pd, plotly.express as px
df = pd.DataFrame({
    "Task":   ["Design", "Procure", "Build", "Test"],
    "Start":  pd.to_datetime(["2026-01-05", "2026-01-12", "2026-01-26", "2026-02-23"]),
    "Finish": pd.to_datetime(["2026-01-12", "2026-01-26", "2026-02-23", "2026-03-09"]),
    "Owner":  ["Ops", "SCM", "Plant", "QA"],
})
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Owner")
fig.update_yaxes(autorange="reversed")      # first task on top
fig.show()
```

Alternatives: matplotlib `barh` with `left=start` and `width=duration`. Combine with schedule logic: compute durations, earliest start/finish with a forward pass, critical path with the `networkx` longest path in a DAG. Colour by owner or status, add a today line (`fig.add_vline`) and milestones. Excel/MS Project are the manual alternatives; Python wins when schedules are generated from data.

### Example
In the table above Procure starts when Design ends (12 Jan), Build when Procure ends (26 Jan, 4 weeks of work), Test starts 23 Feb. The project spans 5 Jan to 9 Mar (63 days). A delay of 1 week in Procure shifts every successor, which the chart makes visible instantly.

### In the news
Not tied to a specific development; see news box for the current Python/pandas versions the snippet runs on (Python 3.11+ with pandas 3.0).

### Interview angle
> [!question] How it is asked
> "How would you present and track a project plan, and automate the status chart?"

> [!tip] Strong answer includes
> - Gantt vs network diagram: bars show time, networks show logic and critical path
> - Mention dependencies, critical path, baseline vs actual, milestones
> - Generate from the task table so the chart updates with data
> - Be ready to name tools (MS Project, Excel, Jira timelines) and when each fits

---

## 6. Network Optimization (NetworkX)
> 🔴 Tier 1 · _Tracker hint:_ nx.Graph(); shortest_path; minimum spanning tree; supply network design

### Definition
**NetworkX** models networks as graphs: nodes (plants, DCs, cities) and weighted edges (distance, cost, time). Core algorithms for supply networks:

- **Shortest path** (Dijkstra): `nx.shortest_path(G, s, t, weight="w")`, `nx.shortest_path_length`.
- **Minimum spanning tree** (connect all nodes at least total weight): `nx.minimum_spanning_tree(G)`.
- **Max flow / min-cost flow**: `nx.maximum_flow`, `nx.min_cost_flow` (needs integer capacities and costs and node `demand` attributes, negative for supply).
- **Centrality** (`nx.betweenness_centrality`) to find critical nodes and single points of failure.
- Critical path in a project DAG: `nx.dag_longest_path`.

```python
import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([("A","B",4), ("A","C",2), ("C","B",1), ("B","D",5), ("C","D",8)], weight="w")
print(nx.shortest_path(G, "A", "D", weight="w"), nx.shortest_path_length(G, "A", "D", weight="w"))
T = nx.minimum_spanning_tree(G, weight="w"); print(T.size(weight="w"))
```

NetworkX is not a vehicle-routing solver; for TSP/VRP with constraints use OR-Tools.

### Example
Edges: A-B 4, A-C 2, C-B 1, B-D 5, C-D 8. Shortest A to D: A-C-B-D $=2+1+5=8$ (alternatives: A-B-D = 9, A-C-D = 10). Minimum spanning tree: pick C-B (1), A-C (2), skip A-B (would form a cycle), B-D (5): total $1+2+5=8$.

### In the news
See news box. For heavy routing, OR-Tools 9.12's CP-SAT and routing improvements are the relevant tooling; NetworkX is for analysis and prototyping.

### Interview angle
> [!question] How it is asked
> "How would you find the cheapest way to connect 20 warehouses, or the fastest route between two hubs?"

> [!tip] Strong answer includes
> - Map the problem to the right graph problem (shortest path vs MST vs flow)
> - Name the algorithm (Dijkstra, Kruskal/Prim) and complexity intuition
> - Centrality for resilience: where is the single point of failure?
> - Limits: NetworkX is slow for very large graphs; use OR-Tools or a graph database

---

## 7. Process Capability (from scratch)
> 🔴 Tier 1 · _Tracker hint:_ Cp = (USL-LSL)/(6*std); Cpk = min((USL-mean),(mean-LSL))/(3*std)

### Definition
**Process capability** compares the natural spread of a stable process with the specification limits.
$C_p=\frac{USL-LSL}{6\sigma}$ (potential capability, ignores centring) and $C_{pk}=\frac{\min(USL-\mu,\ \mu-LSL)}{3\sigma}$ (actual, penalises off-centre). $C_{pk}\le C_p$ always; equal only when centred. Common benchmarks: 1.00 minimum (about 2,700 ppm out of spec if centred, normal), 1.33 acceptable, 1.67 good; Six Sigma short-term target is $C_p=2$ ($C_{pk}\ge1.5$ allowing a 1.5 sigma shift).

$\sigma$ must be the **within-subgroup** (short-term) sigma, e.g. $\bar{R}/d_2$ from a control chart, for $C_p/C_{pk}$; using the overall sample standard deviation gives $P_p/P_{pk}$ (performance indices). Capability is only meaningful when the process is in statistical control and approximately normal.

```python
import numpy as np
from scipy.stats import norm
def capability(x, lsl, usl):
    mu, s = np.mean(x), np.std(x, ddof=1)
    cp  = (usl - lsl) / (6 * s)
    cpk = min(usl - mu, mu - lsl) / (3 * s)
    ppm = (norm.cdf(lsl, mu, s) + norm.sf(usl, mu, s)) * 1e6
    return cp, cpk, ppm
```

### Example
Shaft diameter spec 9.5 to 10.5 mm (LSL 9.5, USL 10.5); process mean 10.1, sigma 0.1.
$C_p=\frac{1.0}{0.6}=1.67$. $C_{pk}=\frac{\min(0.4,\ 0.6)}{0.3}=\frac{0.4}{0.3}=1.33$. The process is capable in spread but drifts towards USL; re-centring to 10.0 would lift $C_{pk}$ to $0.5/0.3=1.67$.

### In the news
See news box. Capability scripts are small NumPy/SciPy functions; SciPy 1.16 (Python 3.11-3.13) is the current base.

### Interview angle
> [!question] How it is asked
> "What is the difference between Cp and Cpk, and what does Cpk of 1.0 mean?"

> [!tip] Strong answer includes
> - Formulas, centring intuition, Cpk <= Cp
> - Short-term vs long-term sigma (Cp/Cpk vs Pp/Ppk), need for control and normality
> - Convert to ppm or sigma level to speak business language
> - Action: reduce variation vs re-centre; tie to Six Sigma DMAIC projects

---

## 8. OEE Calculator Script
> 🔴 Tier 1 · _Tracker hint:_ oee = availability * performance * quality; trend over time with pandas

### Definition
**Overall Equipment Effectiveness** $=A\times P\times Q$.

- **Availability** = run time / planned production time (loses: breakdowns, changeovers).
- **Performance** = (ideal cycle time x total count) / run time (loses: slow cycles, minor stops).
- **Quality** = good count / total count (loses: scrap, rework).

World-class benchmark is often quoted as 85% (A about 90%, P about 95%, Q about 99.9%), though targets are plant-specific. A shortcut: $OEE=\frac{\text{good count}\times\text{ideal cycle time}}{\text{planned time}}$ ("fully productive time"). Excluded from planned time: scheduled breaks and no-demand periods (those fall under TEEP).

```python
import pandas as pd
df = pd.read_csv("shift_log.csv", parse_dates=["date"])
df["availability"] = df["run_min"] / df["planned_min"]
df["performance"]  = df["ideal_ct_min"] * df["total_count"] / df["run_min"]
df["quality"]      = df["good_count"] / df["total_count"]
df["oee"] = df["availability"] * df["performance"] * df["quality"]
weekly = df.set_index("date").resample("W")["oee"].mean()   # trend
weekly.plot(title="Weekly OEE")
```

Aggregate OEE properly by summing times and counts first, then computing the ratios, rather than averaging shift-level OEEs.

### Example
Planned 480 min, downtime 60 min so run time 420 min: $A=420/480=0.875$. Ideal cycle 1 min/unit, total 360 units: $P=360/420=0.857$. Good units 342: $Q=342/360=0.95$. $OEE=0.875\times0.857\times0.95\approx0.7125$ (**71.3%**). Check with the shortcut: $342\times1/480=0.7125$.

### In the news
See news box. pandas 3.0 (21 Jan 2026) made Copy-on-Write default, so derived-column code like the above is safe, but chained updates to slices must use `.loc`.

### Interview angle
> [!question] How it is asked
> "A line has 71% OEE. How do you find where the losses are and improve it?"

> [!tip] Strong answer includes
> - Decompose into A, P, Q and identify the biggest loss (Pareto the downtime reasons)
> - Six big losses mapping; SMED for changeovers, TPM for breakdowns
> - Correct aggregation across shifts; data capture via MES/IoT
> - OEE benchmark caveats (do not chase 100%; protect the bottleneck first)

---

## 9. Regression for Forecasting
> 🔴 Tier 1 · _Tracker hint:_ from sklearn.linear_model import LinearRegression with time/seasonality features

### Definition
Regression forecasting expresses demand as a function of **time** and other features: $y_t=\beta_0+\beta_1t+\sum_m\gamma_m\,\text{month}_m+\delta\,\text{promo}_t+\varepsilon_t$. Time index captures trend; month (or week) dummies capture seasonality; lags, holidays, price and promotions capture drivers. Because ordinary cross-validation leaks the future, validate with **time-based splits** (`TimeSeriesSplit` or a hold-out of the last N periods). Metrics: MAE, RMSE, MAPE/WAPE, bias.

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
df["t"] = range(len(df)); df["month"] = df["date"].dt.month
X = pd.get_dummies(df.loc[:, ["t", "month"]], columns=["month"], drop_first=True)
y = df["demand"]
train, test = X.iloc[:-6], X.iloc[-6:]
model = LinearRegression().fit(train, y.iloc[:-6])
pred = model.predict(test)
wape = abs(y.iloc[-6:] - pred).sum() / y.iloc[-6:].sum()
```

Limits: linear trend only, residual autocorrelation (check Durbin-Watson), no intermittent-demand handling; compare with moving average, exponential smoothing (Holt-Winters), ARIMA and gradient boosting, and always benchmark against a naive/seasonal-naive forecast.

### Example
Trend-only fit on four quarters t = 1..4 with demand 100, 110, 120, 130 gives slope 10 and intercept 90, so the t = 5 forecast is 140. With a multiplicative seasonal index of 0.9 for a weak quarter, the adjusted forecast is $140\times0.9=126$. (Illustrative numbers.)

### In the news
See news box. `pd.get_dummies` returns boolean columns (since pandas 2.0), which scikit-learn accepts; use `dtype=int` if you export to other tools. Pin pandas and scikit-learn versions for reproducible forecasts.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand for the next quarter for 500 SKUs?"

> [!tip] Strong answer includes
> - Features: trend, seasonality, promotions, price; time-based validation
> - Baselines (naive, moving average) and error metrics (WAPE, bias)
> - Segment by demand pattern (smooth, intermittent: Croston) and hierarchy
> - Forecast value added: does it beat naive? Tie to inventory impact

---

## 10. Data Pipeline Automation
> 🔴 Tier 1 · _Tracker hint:_ Schedule scripts with cron/Task Scheduler; pandas + openpyxl for auto-reports

### Definition
A small **data pipeline** runs unattended: extract (read CSV/SQL/API) to transform (clean, aggregate with pandas) to load/report (write Excel, send email). Reliability features: logging, error handling and alerts, idempotent runs (safe to re-run), config separate from code, secrets in environment variables.

```python
import pandas as pd, logging
from datetime import date
logging.basicConfig(filename="report.log", level=logging.INFO)
df = pd.read_sql("SELECT * FROM orders WHERE order_date >= CURRENT_DATE - 7", conn)
summary = df.groupby("region").agg(orders=("order_id", "count"), revenue=("amount", "sum"))
with pd.ExcelWriter(f"weekly_{date.today():%Y%m%d}.xlsx", engine="openpyxl") as xw:
    summary.to_excel(xw, sheet_name="Summary")
    df.to_excel(xw, sheet_name="Detail", index=False)
logging.info("Report written")
```

Scheduling: **cron** on Linux/Mac, e.g. `0 7 * * 1-5 /usr/bin/python3 /home/user/report.py` runs at 07:00 Monday to Friday; **Windows Task Scheduler**, or Airflow/Prefect for dependencies and retries at scale. `openpyxl` also formats cells, adds formulas and charts to existing workbooks. Beyond a few scripts, move to an orchestrator and a warehouse.

### Example
A plant manager gets a Monday 07:00 Excel with last week's OEE by line, scrap by cause and top 10 downtime events. Manual effort was about 2 hours per week (illustrative); automated, it is zero and consistent. The cron entry above implements the schedule.

### In the news
See news box. Upgrading to pandas 3.0 (Python 3.11+) can break scheduled scripts that use chained assignment or rely on `object` strings, so pin versions in `requirements.txt` and test before upgrading production jobs.

### Interview angle
> [!question] How it is asked
> "Tell me about a process you automated" or "How would you automate a weekly operations MIS?"

> [!tip] Strong answer includes
> - Structure: problem, before/after time saved, tools, result (use your own real project; do not invent figures)
> - Reliability: logging, error alerts, idempotency, version pinning
> - Maintainability: config, documentation, handover
> - When to graduate to Airflow, a BI tool or ERP-native reporting

---

## 11. ⭐ Advanced: Vehicle Routing and Scheduling with OR-Tools
> ⭐ Advanced · _Added beyond the tracker_

### Definition
PuLP handles LP/MILP; many operations problems are combinatorial: **vehicle routing (VRP)** with capacities and time windows, **job-shop/shift scheduling**, **bin packing**. Google **OR-Tools** offers a routing library (`pywrapcp`) and **CP-SAT** (constraint programming with SAT), which is state of the art for scheduling and assignment.

CP-SAT sketch (simple assignment with capacity):

```python
from ortools.sat.python import cp_model
m = cp_model.CpModel()
x = {(i, j): m.NewBoolVar(f"x{i}_{j}") for i in range(3) for j in range(2)}
for i in range(3): m.Add(sum(x[i, j] for j in range(2)) == 1)           # each job to one machine
for j in range(2): m.Add(sum(w[i] * x[i, j] for i in range(3)) <= cap[j])
m.Minimize(sum(c[i][j] * x[i, j] for i in range(3) for j in range(2)))
solver = cp_model.CpSolver(); status = solver.Solve(m)
```

(`w`, `cap`, `c` are your data.) VRP is NP-hard, so solvers use heuristics (savings, local search) plus metaheuristics, with a time limit and an optimality gap rather than a proof of optimality. Model features: time windows, pickup-delivery, multiple depots, fleet cost.

### Example
Tiny facility-location MILP (a CBC/PuLP-style problem): two candidate DCs with fixed cost Rs 100 and Rs 150, customer demands 10, 20, 30, per-unit costs DC1 = 2, 4, 6 and DC2 = 5, 3, 1. Open only DC1: $100+(20+80+180)=380$. Open only DC2: $150+(50+60+30)=290$. Open both (each customer served by cheaper DC): $250+(20+60+30)=360$. Best: **open only DC2, cost Rs 290**; the fixed cost outweighs the saving from opening both.

### In the news
See news box. OR-Tools v9.12 (17 Feb 2025) improved CP-SAT and added Python 3.13 support and HiGHS in Model Builder.

### Interview angle
> [!question] How it is asked
> "How would you route 40 delivery vehicles with time windows? What tool would you use?"

> [!tip] Strong answer includes
> - Recognise VRP as NP-hard; heuristic plus local search with a time limit
> - Name constraints: capacity, time windows, driver hours; objective: distance/cost/SLA
> - Real-world data: road distances matrix, service times, traffic
> - Evaluate with KPIs (cost per drop, vehicle utilisation, on-time rate)

---

## 12. ⭐ Advanced: Simulation of Inventory Policies (s, Q) with Monte Carlo
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Closed-form formulas assume stationary, simple demand. A simulation lets you test an **(s, Q) policy** (reorder Q when inventory position falls to s) against realistic demand and lead-time variability, measuring **fill rate** (units served from stock / units demanded), **cycle service level** (share of cycles without stock-out), average inventory and total cost.

```python
import numpy as np
rng = np.random.default_rng(0)
def simulate(s, Q, days=365, mu=40, sd=12, L=5, start=300):
    inv, pipeline, short, demand_tot, holding = start, [], 0, 0, 0
    for t in range(days):
        inv += sum(q for (arr, q) in pipeline if arr == t)
        pipeline = [(a, q) for (a, q) in pipeline if a != t]
        d = max(0, rng.normal(mu, sd)); demand_tot += d
        served = min(inv, d); short += d - served; inv -= served
        position = inv + sum(q for _, q in pipeline)
        if position <= s: pipeline.append((t + L, Q))
        holding += inv
    return 1 - short / demand_tot, holding / days     # fill rate, avg inventory
```

Run the function many times (replications) per (s, Q) pair and pick the cheapest policy that meets the service target. This also tests how fill rate differs from cycle service level (typically fill rate is higher at the same safety stock).

### Example
With $\mu=40$/day, $\sigma=12$, $L=5$: lead-time demand mean 200, sd $12\sqrt{5}\approx26.8$. A 95% cycle service level suggests $s=200+1.645\times26.8\approx244$. Simulate $s=244, Q=400$ across 200 replications; if fill rate is about 99% and average inventory is about 250 units, you may even lower $s$ and compare costs. (Results to be generated by the code, not asserted here.)

### In the news
See news box. NumPy's `default_rng` and pandas 3.0 DataFrames are enough; OR-Tools or SimPy are used when the system has many interacting resources.

### Interview angle
> [!question] How it is asked
> "How do you pick the reorder point and order quantity when demand and lead time are both uncertain?"

> [!tip] Strong answer includes
> - Analytical starting point (EOQ and $z\sigma\sqrt{L}$) then validation by simulation
> - Service metrics: CSL vs fill rate, and the cost trade-off curve
> - Replications and confidence intervals on the simulated metrics
> - Sensitivity to demand distribution and lead-time variability

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
