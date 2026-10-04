---
tags: [python-programming, tier1]
area: Python Programming
topic: "Pandas — Data Manipulation"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 16
---
# Pandas — Data Manipulation

⬅ [[063 NumPy]] · [[_Index - Python Programming|Python Programming]] · [[065 Data Visualization (Matplotlib-Seaborn-Plotly)]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. DataFrame Creation]]
2. [[#2. Indexing & Selection]]
3. [[#3. Filtering]]
4. [[#4. Adding & Dropping Columns]]
5. [[#5. Data Cleaning]]
6. [[#6. Data Types]]
7. [[#7. GroupBy & Aggregation]]
8. [[#8. Merge & Join]]
9. [[#9. Pivot Table]]
10. [[#10. Apply & Map]]
11. [[#11. String Methods (str accessor)]]
12. [[#12. DateTime Operations]]
13. [[#13. Rolling & Expanding]]
14. [[#14. Melt & Stack/Unstack]]
15. [[#15. ⭐ Advanced: Performance, Chaining & Memory at Scale]]
16. [[#16. ⭐ Advanced: Analytics Recipes (ABC, Cohorts, Service Level)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): pandas 3.0 changes the ground rules
> **pandas 3.0.0 (21 Jan 2026).** Headline changes: (1) **Copy-on-Write** is now the only mode, so chained assignment such as `df["foo"][df["bar"] > 5] = 100` no longer works and `SettingWithCopyWarning` is gone (use `df.loc[df["bar"] > 5, "foo"] = 100`); (2) text columns are inferred as a dedicated **`str` dtype** instead of `object` (needs `pyarrow` recommended); (3) the default datetime resolution is no longer nanoseconds, avoiding out-of-bounds errors for dates before 1678 or after 2262; (4) initial `pd.col()` syntax for `DataFrame.assign`. ([Source](https://pandas.pydata.org/community/blog/pandas-3.0.html), [release notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html))
> 
> **Python's growth (2025).** Python is used by 57.9% of Stack Overflow survey respondents, up 7 percentage points from 2024, which keeps pandas the default tool for analysts. ([Source](https://survey.stackoverflow.co/2025/technology))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. DataFrame Creation
> 🔴 Tier 1 · _Tracker hint:_ pd.DataFrame(dict), pd.read_csv(), pd.read_excel(); df.head(), df.info(), df.describe()

### Definition
A **DataFrame** is a labelled 2-D table: columns (each a `Series`, with its own dtype) sharing a row index. A `Series` is a labelled 1-D array.

```python
import pandas as pd
df = pd.DataFrame({"sku": ["A", "B", "C"], "qty": [10, 25, 7],
                   "price": [50.0, 20.5, 99.0]})
df = pd.read_csv("sales.csv", parse_dates=["date"], dtype={"sku": "string"})
df = pd.read_excel("sales.xlsx", sheet_name="Q1")
df = pd.read_json("x.json"); pd.read_sql(query, conn)

df.head(); df.tail(3)     # peek
df.shape                  # (rows, cols)
df.info()                 # dtypes, non-null counts, memory
df.describe()             # count, mean, std, min, quartiles, max (numeric)
df.describe(include="all")
```
`read_csv` options worth knowing: `usecols`, `nrows`, `chunksize`, `na_values`, `sep`, `encoding`.

### Example
`df.info()` on a 1,000-row file shows `qty` with 950 non-null: 50 missing values. `df.describe()` shows min price of -5, a data-entry error caught before analysis. That two-line check is the first step of any case-study dataset.

### In the news
See news box. In pandas 3.0 `read_csv` text columns arrive as the new `str` dtype by default, which `df.info()` will show instead of `object`.

### Interview angle
> [!question] How it is asked
> "You get a new CSV. What are the first five things you do?"

> [!tip] Strong answer includes
> - `head`, `shape`, `info`, `describe`, `isnull().sum()`
> - Check dtypes and parse dates on load
> - Chunk or `usecols` for large files
> - Eyeball for duplicates, impossible values, units

---

## 2. Indexing & Selection
> 🔴 Tier 1 · _Tracker hint:_ df['col'], df[['a','b']], df.loc[label], df.iloc[position], df.at[], df.iat[]

### Definition
| Accessor | Selects by | Slice end |
|---|---|---|
| `df['col']` | column label, returns Series | n/a |
| `df[['a','b']]` | list of columns, returns DataFrame | n/a |
| `df.loc[rows, cols]` | **labels** | inclusive |
| `df.iloc[rows, cols]` | integer **positions** | exclusive |
| `df.at[r, c]` / `df.iat[i, j]` | single scalar (fast) | n/a |

```python
df.loc[0, "qty"]
df.loc[df["qty"] > 10, ["sku", "qty"]]   # boolean rows, named columns
df.iloc[0:2, 0:2]                         # first 2 rows, first 2 cols
df.set_index("sku").loc["B"]
df.loc[df["sku"] == "A", "price"] = 55    # safe assignment
```
Always assign through a single `.loc[...]` call. Chained indexing (`df[cond]["col"] = v`) is not supported under pandas 3.0 Copy-on-Write.

### Example
`df.loc[df["qty"] > 10, "price"] *= 1.1` raises the price by 10% for rows with qty above 10. Replacing it with `df[df["qty"] > 10]["price"] *= 1.1` modifies a temporary object and would not update `df`.

### In the news
See news box. pandas 3.0 removed chained assignment, so `.loc` for setting values is no longer a best practice but the only one.

### Interview angle
> [!question] How it is asked
> "Difference between `loc` and `iloc`?" or "What is `SettingWithCopyWarning`?"

> [!tip] Strong answer includes
> - Label vs position; inclusive vs exclusive end
> - Boolean masks inside `.loc`
> - Single-call assignment and why chaining fails (Copy-on-Write)
> - `at`/`iat` for fast scalars

---

## 3. Filtering
> 🔴 Tier 1 · _Tracker hint:_ df[df['sales']>1000], df.query('sales > 1000 and region == "North"')

### Definition
Filtering uses a **boolean mask**: a Series of True/False aligned to the rows.

```python
df[df["sales"] > 1000]
df[(df["sales"] > 1000) & (df["region"] == "North")]   # & | ~, with parentheses
df[df["region"].isin(["North", "East"])]
df[df["sales"].between(500, 1000)]
df[df["name"].str.contains("pvt", case=False, na=False)]
df[df["date"] >= "2026-01-01"]
df[df["x"].isna()]
df.query('sales > 1000 and region == "North"')
thr = 1000; df.query("sales > @thr")      # @ references a Python variable
df.nlargest(5, "sales")
```
Python's `and`/`or` do not work on Series; use `&`/`|` with each condition in parentheses. `query` is more readable for long conditions.

### Example
Orders 500, 1,200, 3,000 in North/South/North: `(sales>1000)&(region=="North")` is `[False, False, True]`, so only the 3,000 row survives. Filtering to the top-selling 20% uses `df[df["sales"] > df["sales"].quantile(0.8)]`.

### In the news
See news box. Filter results are new objects under Copy-on-Write, so modifying them never silently changes the source.

### Interview angle
> [!question] How it is asked
> "Select customers in Maharashtra with more than 5 orders and revenue above the median."

> [!tip] Strong answer includes
> - Boolean masks with `&`, `|`, `~` and parentheses
> - `isin`, `between`, `str.contains`, `query`
> - Quantile or aggregate thresholds computed first
> - NaN handling in comparisons

---

## 4. Adding & Dropping Columns
> 🔴 Tier 1 · _Tracker hint:_ df['new'] = df['a'] + df['b']; df.drop(columns=['x']); df.rename(columns={'old':'new'})

### Definition
```python
df["revenue"] = df["qty"] * df["price"]            # new column, vectorised
df["tier"] = np.where(df["revenue"] > 1000, "High", "Low")
df = df.assign(margin=lambda d: d["revenue"] * 0.2)   # chainable
df = df.drop(columns=["tmp", "x"])
df = df.rename(columns={"qty": "units"})
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
df.insert(1, "region", "North")                    # at a position
df = df.reindex(columns=["sku", "units", "revenue"])
```
`inplace=True` is discouraged (no speed benefit, breaks chaining); assign the result instead. `assign` supports **method chaining**, and pandas 3.0 adds early `pd.col()` support for assign expressions.

### Example
`df["revenue"] = df["qty"] * df["price"]`: rows (10, 50.0), (25, 20.5), (7, 99.0) give 500.0, 512.5, 693.0. Total 1,705.5.

### In the news
See news box. `pd.col()` in pandas 3.0 is the first step toward writing assign expressions without lambdas.

### Interview angle
> [!question] How it is asked
> "Add a column for gross margin % and drop unused columns, in one chain."

> [!tip] Strong answer includes
> - Vectorised column math, not loops
> - `assign` for chains; `drop(columns=)` explicit
> - Avoids `inplace=True`
> - Standardises column names early

---

## 5. Data Cleaning
> 🔴 Tier 1 · _Tracker hint:_ df.isnull().sum(), df.fillna(0), df.dropna(subset=['col']), df.duplicated(), df.drop_duplicates()

### Definition
```python
df.isnull().sum()                    # missing count per column
df.isnull().mean() * 100             # missing %
df["qty"] = df["qty"].fillna(0)
df["price"] = df["price"].fillna(df["price"].median())
df["x"] = df["x"].ffill()            # forward fill (time series)
df = df.dropna(subset=["sku"])       # drop rows missing sku
df.duplicated(subset=["order_id"]).sum()
df = df.drop_duplicates(subset=["order_id"], keep="first")
df["name"] = df["name"].str.strip().str.title()
df = df[df["qty"] >= 0]              # remove impossible values
```
Decide per column: drop, impute (mean/median/mode/ffill/model) or flag. Document every rule. Median is safer than mean with outliers; never impute the target leakage-style before splitting data for modelling.

### Example
A 1,000-row table has `price` missing in 40 rows (4%). Filling with the median 120 is reasonable; 400 missing (40%) suggests asking the data owner, since imputing would invent most of the column. Duplicate order IDs, 12 of 1,000, are removed with `drop_duplicates`, shrinking the table to 988 rows.

### In the news
See news box. In pandas 3.0 the `str` dtype uses a proper missing marker for text, making missing-value checks on text columns more consistent than with `object`.

### Interview angle
> [!question] How it is asked
> "Describe your data cleaning process" or "How do you handle missing values?"

> [!tip] Strong answer includes
> - Quantify missingness first and understand why it is missing
> - Imputation choice tied to distribution and use
> - Dedupe on a business key
> - Validation checks and a log of changes

---

## 6. Data Types
> 🔴 Tier 1 · _Tracker hint:_ df.dtypes, df['date'] = pd.to_datetime(df['date']), df['cat'].astype('category')

### Definition
```python
df.dtypes
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")
df["qty"] = pd.to_numeric(df["qty"], errors="coerce")   # bad -> NaN
df["region"] = df["region"].astype("category")
df["qty"] = df["qty"].astype("int32")
df["id"] = df["id"].astype("string")
df["flag"] = df["flag"].astype("boolean")   # nullable boolean
df.memory_usage(deep=True)
```
Common types: `int64`, `float64`, `bool`, `datetime64`, `category`, `string`/`str`. Use **nullable** types (`Int64`, `boolean`) when integers have missing values. `category` saves memory for low-cardinality text and enables ordering. pandas 3.0 infers text as `str` rather than `object`.

### Example
A 1 million row table with a `region` column of 5 distinct values: as `object` strings it can use tens of MB; `astype("category")` stores 5 labels plus small integer codes, typically cutting memory by 90% or more. Dates left as text cannot be sorted or resampled correctly ("10-01" sorts before "2-01").

### In the news
See news box. pandas 3.0 changed datetime defaults from nanoseconds to microsecond/input resolution, so dates before 1678 or after 2262 no longer overflow.

### Interview angle
> [!question] How it is asked
> "A numeric column loaded as object. Why, and how do you fix it?"

> [!tip] Strong answer includes
> - Mixed or dirty values cause `object`; `to_numeric(errors="coerce")` then inspect NaNs
> - `to_datetime` with explicit format, mindful of day-first
> - `category` for memory and speed
> - Nullable dtypes for missing integers

---

## 7. GroupBy & Aggregation
> 🔴 Tier 1 · _Tracker hint:_ df.groupby('dept')['salary'].agg(['mean','max','count']); named agg: .agg(avg=('sal','mean'))

### Definition
GroupBy follows **split-apply-combine**: split rows by key, apply a function per group, combine results.

```python
df.groupby("dept")["salary"].agg(["mean", "max", "count"])
df.groupby(["region", "month"], as_index=False).agg(
    total=("sales", "sum"),
    avg_price=("price", "mean"),
    orders=("order_id", "nunique"))           # named aggregation
df["share"] = df["sales"] / df.groupby("region")["sales"].transform("sum")
df.groupby("region")["sales"].rank(ascending=False)
df.groupby("region").apply(lambda g: g.nlargest(2, "sales"))
df.groupby("region").size()                   # rows per group
```
`transform` returns a result aligned to the original rows (for shares, z-scores); `agg` collapses each group. NaN keys are dropped by default (`dropna=False` keeps them).

### Example
Sales: North 100, North 300, South 200. `groupby("region")["sales"].sum()` gives North 400, South 200. Share of total via transform: North rows get 100/400 = 25% and 300/400 = 75%; South 200/200 = 100%.

### In the news
See news box. Under Copy-on-Write, groupby results are independent objects; assigning a transformed column back to the frame is the clean pattern.

### Interview angle
> [!question] How it is asked
> "Find the top 3 products by revenue in each region" or "Percent contribution of each SKU within its category."

> [!tip] Strong answer includes
> - Split-apply-combine explanation
> - Named aggregation for readable output
> - `transform` vs `agg` vs `apply`
> - Sanity-check totals after aggregation

---

## 8. Merge & Join
> 🔴 Tier 1 · _Tracker hint:_ pd.merge(df1,df2,on='key',how='left'); pd.concat([df1,df2]); df.join()

### Definition
```python
pd.merge(orders, products, on="sku", how="left")
pd.merge(a, b, left_on="cust_id", right_on="id", how="inner",
         validate="many_to_one", indicator=True)
pd.concat([jan, feb], ignore_index=True)      # stack rows
pd.concat([a, b], axis=1)                     # side by side by index
a.join(b, on="key", rsuffix="_b")             # index-based convenience
```
| `how` | Keeps |
|---|---|
| inner | keys in both |
| left | all left, matching right (else NaN) |
| right | all right |
| outer | all keys in either |

Equivalent to SQL joins. Use `validate=` to catch accidental many-to-many explosions and `indicator=True` to see unmatched rows. Check the row count after every merge.

### Example
Orders has 1,000 rows; products has duplicate SKU "A1" (2 rows) from a dirty master. A left merge on `sku` returns more than 1,000 rows because every "A1" order doubles. `validate="many_to_one"` raises an error immediately and exposes the duplicated key.

### In the news
See news box. As the Python stack matures (pandas 3.0), explicit validation of merges is a recommended habit, not an optional extra.

### Interview angle
> [!question] How it is asked
> "Explain inner vs left join and what can go wrong when merging in pandas." Often paired with a SQL equivalent.

> [!tip] Strong answer includes
> - Join types and SQL mapping
> - Row-count check before and after
> - Duplicate keys causing row explosion; `validate`
> - `merge` vs `concat` vs `join`

---

## 9. Pivot Table
> 🔴 Tier 1 · _Tracker hint:_ df.pivot_table(values='sales',index='region',columns='month',aggfunc='sum',fill_value=0)

### Definition
`pivot_table` is Excel's PivotTable in code: group by `index` (rows) and `columns`, aggregate `values` with `aggfunc`.

```python
pt = df.pivot_table(values="sales", index="region", columns="month",
                    aggfunc="sum", fill_value=0, margins=True)
df.pivot_table(index="region", values=["sales", "qty"],
               aggfunc={"sales": "sum", "qty": "mean"})
pd.crosstab(df["region"], df["category"], normalize="index")   # row %
pt.reset_index()
```
`pivot` (no aggregation) fails with duplicate index/column pairs; `pivot_table` aggregates them. `margins=True` adds row and column totals. `crosstab` is a frequency/proportion table.

### Example
Rows: (North, Jan, 100), (North, Jan, 50), (North, Feb, 80), (South, Jan, 60). `pivot_table(..., aggfunc="sum", fill_value=0)` gives North: Jan 150, Feb 80; South: Jan 60, Feb 0. Grand total 290.

### In the news
See news box. Recruiters often test pivot tables in both Excel and pandas to confirm the same answer arises in each tool.

### Interview angle
> [!question] How it is asked
> "Create a region by month sales matrix and show each region's share of its total."

> [!tip] Strong answer includes
> - Correct index/columns/values/aggfunc mapping
> - `fill_value` and `margins`
> - `pivot` vs `pivot_table` difference
> - Normalising to percentages and checking totals

---

## 10. Apply & Map
> 🔴 Tier 1 · _Tracker hint:_ df['col'].apply(lambda x: x*1.1); df.applymap(); df['cat'].map({'A':1,'B':2})

### Definition
```python
df["price_new"] = df["price"].apply(lambda x: x * 1.1)   # works, but slow
df["price_new"] = df["price"] * 1.1                       # vectorised: prefer
df["code"] = df["cat"].map({"A": 1, "B": 2})              # dict lookup; unmapped -> NaN
df["len"] = df["name"].map(len)
df["bucket"] = df.apply(lambda r: r["a"] + r["b"], axis=1)   # row-wise, slowest
df[["a", "b"]].map(lambda x: round(x, 1))   # element-wise on a DataFrame
```
`Series.map` for dict/function element lookups; `Series.apply` for functions; `DataFrame.apply(axis=1)` for row logic; `DataFrame.applymap` was deprecated and renamed **`DataFrame.map`** in pandas 2.1. Rule: vectorise first (`np.where`, `.str`, arithmetic); `apply` is a Python loop in disguise.

### Example
Mapping `{"A": 1, "B": 2}` onto `["A","B","C"]` gives `[1, 2, NaN]` because "C" is unmapped. For a margin flag, `np.where(df["margin"] > 0.2, "Good", "Poor")` is far faster than `df.apply(..., axis=1)` on a million rows.

### In the news
See news box. Faster string and datetime handling in recent pandas reduces the cases where you need `apply` at all.

### Interview angle
> [!question] How it is asked
> "Difference between `apply`, `map` and `applymap`?" or "How would you speed up `apply(axis=1)`?"

> [!tip] Strong answer includes
> - The three scopes (element/Series, DataFrame element, row/column)
> - Prefer vectorised alternatives; explain why
> - Notes `applymap` renamed to `DataFrame.map`
> - Unmapped values become NaN with `map`

---

## 11. String Methods (str accessor)
> 🔴 Tier 1 · _Tracker hint:_ df['name'].str.upper(), .str.contains('abc'), .str.split('-').str[0]

### Definition
The `.str` accessor applies vectorised string functions and skips missing values.

```python
s = df["name"]
s.str.upper(); s.str.lower(); s.str.strip(); s.str.title()
s.str.contains("abc", case=False, na=False)
s.str.startswith("SKU")
s.str.replace(r"\s+", " ", regex=True)
s.str.split("-").str[0]                       # first piece
df[["city", "state"]] = s.str.split(",", expand=True)
s.str.extract(r"(\d+)")                       # first capture group
s.str.len(); s.str.zfill(6); s.str.cat(sep=";")
```
Regex support is built in (`regex=True`). For large text columns, the pandas 3.0 `str` dtype is more memory-efficient and faster than `object`.

### Example
Product codes `"IN-MH-0042"`: `.str.split("-").str[1]` gives `"MH"` (state) and `.str.extract(r"(\d+)$")` gives `0042`. Cleaning `" Pune "` with `.str.strip().str.title()` gives `"Pune"`, fixing a groupby that previously showed `"Pune"` and `" Pune "` as two groups.

### In the news
See news box. pandas 3.0 makes `str` the default text dtype, the biggest change to string handling in the library's recent history.

### Interview angle
> [!question] How it is asked
> "Clean a messy city column so a groupby works."

> [!tip] Strong answer includes
> - `strip`, case normalisation, `replace`, `contains` with `na=False`
> - `split(expand=True)` and `extract` with regex
> - Why inconsistent text breaks aggregations
> - Mentions fuzzy matching for harder cases

---

## 12. DateTime Operations
> 🔴 Tier 1 · _Tracker hint:_ df['date'].dt.year, .dt.month, .dt.dayofweek, .dt.days_in_month; resample()

### Definition
```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["dow"] = df["date"].dt.dayofweek          # Monday=0 ... Sunday=6
df["dim"] = df["date"].dt.days_in_month
df["q"] = df["date"].dt.to_period("Q")
df["lead_days"] = (df["delivered"] - df["ordered"]).dt.days
df["date"] + pd.Timedelta(days=7)
df.set_index("date").resample("MS")["sales"].sum()    # month-start buckets
pd.date_range("2026-01-01", periods=12, freq="MS")
df["date"].dt.strftime("%b-%Y")
```
Frequency codes: `D` day, `W` week, `MS` month start, `ME` month end (older `M` is deprecated in favour of `ME`), `QS` quarter start, `YS` year start. `resample` needs a datetime index (or `on=`).

### Example
Orders on 2026-01-05 and delivered 2026-01-12: `(delivered - ordered).dt.days = 7`. Daily sales resampled with `resample("MS").sum()` rolls 31 daily rows into one row for January.

### In the news
See news box. pandas 3.0's new default datetime resolution (not always nanoseconds) removes the old 1678 to 2262 range limit in many cases.

### Interview angle
> [!question] How it is asked
> "Compute average delivery lead time by month" or "Which weekday has the highest order volume?"

> [!tip] Strong answer includes
> - `to_datetime` first, then `.dt` accessors
> - Timedelta subtraction for durations
> - `resample` vs `groupby` by period
> - Time zones and fiscal-year alignment (April start in India)

---

## 13. Rolling & Expanding
> 🔴 Tier 1 · _Tracker hint:_ df['sales'].rolling(window=3).mean(); .expanding().sum() — moving averages

### Definition
**Rolling** applies a function over a fixed-size sliding window; **expanding** over all observations from the start.

```python
df["ma3"] = df["sales"].rolling(window=3).mean()          # first 2 values NaN
df["ma3c"] = df["sales"].rolling(3, min_periods=1).mean()
df["roll_std"] = df["sales"].rolling(7).std()
df["cum_sum"] = df["sales"].expanding().sum()             # same as cumsum()
df["ewm"] = df["sales"].ewm(span=3, adjust=False).mean()  # exponential
df["sales"].rolling("7D").sum()                           # time-based window
df["pct_change"] = df["sales"].pct_change()
df["lag1"] = df["sales"].shift(1)
```
$MA_t=\frac{1}{w}\sum_{i=0}^{w-1}x_{t-i}$. Rolling uses only *past* values by default (trailing); `center=True` uses surrounding values and would leak the future in forecasting.

### Example
Sales `[10, 20, 30, 40]`, window 3: MA is `[NaN, NaN, 20, 30]` since (10+20+30)/3 = 20 and (20+30+40)/3 = 30. Expanding sum is `[10, 30, 60, 100]`.

### In the news
See news box. Copy-on-Write means derived columns like `ma3` are safely independent of the source column.

### Interview angle
> [!question] How it is asked
> "Smooth noisy daily demand and flag days above 2 standard deviations of the 30-day rolling mean."

> [!tip] Strong answer includes
> - Rolling vs expanding vs EWM
> - NaN at window start; `min_periods`
> - Trailing windows to avoid look-ahead bias
> - Use for trend, anomaly detection, control charts

---

## 14. Melt & Stack/Unstack
> 🔴 Tier 1 · _Tracker hint:_ pd.melt() — wide to long; df.pivot() — long to wide; stack/unstack for multi-index

### Definition
**Wide** format has one column per period/category; **long (tidy)** format has one row per observation. Plotting (seaborn/plotly) and groupby prefer long.

```python
long = pd.melt(wide, id_vars=["sku"], value_vars=["Jan", "Feb", "Mar"],
               var_name="month", value_name="sales")
wide2 = long.pivot(index="sku", columns="month", values="sales").reset_index()

s = df.set_index(["region", "month"])["sales"]     # MultiIndex Series
s.unstack()          # inner index level becomes columns
s.unstack().stack()  # back to long
df.set_index(["a", "b"]).unstack(level="b")
```
`melt` = wide to long; `pivot`/`unstack` = long to wide; `stack` = columns to inner index level. Hierarchical indexes are reachable with `.loc[("North", "Jan")]` and `xs()`.

### Example
Wide: SKU A with Jan 100, Feb 120. `melt` gives two rows: (A, Jan, 100) and (A, Feb, 120). Now `sns.lineplot(data=long, x="month", y="sales", hue="sku")` plots all SKUs in one call.

### In the news
See news box. As visualisation libraries expect tidy data, reshaping remains a daily task in analytics roles.

### Interview angle
> [!question] How it is asked
> "Your Excel report has one column per month. Reshape it for analysis and plotting."

> [!tip] Strong answer includes
> - Wide vs long (tidy data) and why
> - `melt` arguments (`id_vars`, `value_vars`, `var_name`, `value_name`)
> - `pivot` vs `pivot_table` and `unstack`
> - Checks row counts before and after reshaping

---

## 15. ⭐ Advanced: Performance, Chaining & Memory at Scale
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Method chaining** with `assign`, `pipe`, `query`, `loc`: readable, no intermediate variables, and well suited to pandas 3.0 Copy-on-Write.
- **Performance:** vectorise; use `category`; downcast numerics (`pd.to_numeric(..., downcast="integer")`); read only needed columns (`usecols`); process in `chunksize`; parquet instead of CSV (`df.to_parquet`) for typed, compressed storage.
- **Large data:** `pyarrow`-backed dtypes, `polars`, `duckdb` (SQL on DataFrames), `dask`.
- **Window functions:** `groupby().cumsum()`, `rank`, `shift`, `diff` for per-group sequences.
- **Quality checks:** `assert df["id"].is_unique`, `pd.testing.assert_frame_equal`.

```python
res = (pd.read_csv("o.csv", usecols=["date","sku","qty","price"], parse_dates=["date"])
         .query("qty > 0")
         .assign(rev=lambda d: d.qty * d.price)
         .groupby(["sku", pd.Grouper(key="date", freq="MS")], as_index=False)["rev"].sum())
```

### Example
A 2 GB CSV: loading all columns as `object` uses well over 2 GB RAM. Loading three columns with `dtype`/`category`, then writing to parquet, often shrinks both memory and disk several-fold, and later reads take a fraction of the time (exact ratio is data-dependent).

### In the news
See news box. Copy-on-Write plus the Arrow-backed `str` dtype in 3.0 are the two changes that most affect performance tuning.

### Interview angle
> [!question] How it is asked
> "Your pandas script is slow or runs out of memory. What do you do?"

> [!tip] Strong answer includes
> - Profile first; find the slow step
> - Dtypes, `usecols`, chunks, parquet
> - Replace `apply` with vectorised or groupby operations
> - Know when to switch tools (SQL, DuckDB, Polars, Spark)

---

## 16. ⭐ Advanced: Analytics Recipes (ABC, Cohorts, Service Level)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Common ops-analytics patterns built from the tracker's building blocks.

```python
# ABC classification
s = df.groupby("sku")["rev"].sum().sort_values(ascending=False)
c = s.cumsum() / s.sum()
abc = pd.cut(c, [0, .8, .95, 1.0], labels=["A", "B", "C"])

# On-time delivery %
df["on_time"] = df["delivered"] <= df["promised"]
otd = df.groupby("supplier")["on_time"].mean().mul(100).round(1)

# Cohort / retention
df["cohort"] = df.groupby("cust")["date"].transform("min").dt.to_period("M")

# Year-over-year growth
m = df.set_index("date")["sales"].resample("MS").sum()
yoy = m.pct_change(12)
```
Also: Pareto charts, inventory ageing buckets with `pd.cut`, safety stock by SKU with `groupby().agg(std=("d","std"))`, and fill rate as `shipped.sum() / ordered.sum()`.

### Example
SKU revenues 500, 300, 100, 50, 50 (total 1,000): cumulative shares 50%, 80%, 90%, 95%, 100%. With bins (0, .8], (.8, .95], (.95, 1], SKUs 1 and 2 are A, SKUs 3 and 4 are B, SKU 5 is C. (Note `pd.cut` bins are right-inclusive, so exactly 80% falls in A.)

### In the news
See news box. These recipes are what take-home case tests in consulting and ops interviews ask for.

### Interview angle
> [!question] How it is asked
> "Given an order table, identify which suppliers are least reliable and which SKUs drive 80% of revenue."

> [!tip] Strong answer includes
> - Clear metric definitions first (what counts as on-time)
> - Groupby plus sort plus cumulative share
> - Sanity check totals and edge cases
> - Ends with a recommendation, not just a table

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
