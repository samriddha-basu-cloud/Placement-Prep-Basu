---
tags: [python-programming, tier1]
area: Python Programming
topic: "Data Visualization (Matplotlib/Seaborn/Plotly)"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 10
---
# Data Visualization (Matplotlib/Seaborn/Plotly)

⬅ [[064 Pandas — Data Manipulation]] · [[_Index - Python Programming|Python Programming]] · [[066 Demand Forecasting & Time Series]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Matplotlib Basics]]
2. [[#2. Subplots]]
3. [[#3. Seaborn Plots]]
4. [[#4. Plotly Express (Interactive)]]
5. [[#5. Chart Selection Guide]]
6. [[#6. Styling & Annotations]]
7. [[#7. Color Palettes]]
8. [[#8. Saving Figures]]
9. [[#9. ⭐ Advanced: Data Storytelling & Dashboard Design]]
10. [[#10. ⭐ Advanced: Statistical & Operations-Specific Charts]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Plotting libraries modernise around multi-dataframe support
> **Plotly.py 6.** Plotly Express now uses **Narwhals** to natively support pandas, Polars and PyArrow, with measurably better performance for Polars/PyArrow, and benefits from Plotly.js's improved typed-array handling; legacy items were removed (deprecated Mapbox traces replaced by MapLibre-based ones, `heatmapgl`, `pointcloud`, transforms, old title attributes) and Jupyter Notebook below version 7 is no longer supported. (The fetched migration page does not state the release date.) ([Source](https://plotly.com/python/v6-migration/))
> 
> **Seaborn 0.13.2 (Jan 2024).** The 0.13 series (0.13.0 Sep 2023) brought major enhancements to categorical plots, support for alternate dataframe libraries and improved configuration of the `seaborn.objects` interface introduced in v0.12 (Sep 2022). ([Source](https://seaborn.pydata.org/whatsnew/index.html))
> 
> **Why it matters.** pandas 3.0 (Jan 2026) and Python's 57.9% usage share (Stack Overflow 2025, up 7 points) keep the pandas-to-plot workflow the default for analysts. ([pandas](https://pandas.pydata.org/community/blog/pandas-3.0.html), [Stack Overflow](https://survey.stackoverflow.co/2025/technology))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Matplotlib Basics
> 🔴 Tier 1 · _Tracker hint:_ plt.figure(figsize=(10,6)); plt.plot(), plt.bar(), plt.scatter(), plt.show(), plt.savefig()

### Definition
**Matplotlib** is Python's foundational plotting library. Two APIs: the quick **pyplot** state machine (`plt.plot`) and the explicit **object-oriented** API (`fig, ax = plt.subplots()`), which is preferred for anything beyond a one-liner.

```python
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 135, 128, 150]

plt.figure(figsize=(10, 6))              # width, height in inches
plt.plot(months, sales, marker="o", label="Sales")   # line: trend
plt.bar(months, sales)                   # bars: comparison
plt.scatter(price, qty, alpha=0.6, s=40) # points: relationship
plt.show()
plt.savefig("sales.png")                 # call BEFORE show()
```
Anatomy: **Figure** (canvas) contains **Axes** (a single plot) with axis, ticks, labels, legend. Use `ax.set_xlabel`, `ax.set_title` in OO style.

### Example
Plotting monthly sales `[120, 135, 128, 150]`: the line rises from 120 to 150, an overall +25% (30/120). `plt.bar` makes month-by-month comparison obvious, while the line highlights direction. Choosing the wrong one (bar for a 5-year daily series) clutters the message.

### In the news
See news box. Matplotlib stays the engine under many libraries (seaborn, pandas `.plot()`), so it is worth knowing even if you mostly use higher-level tools.

### Interview angle
> [!question] How it is asked
> "Walk me through plotting monthly sales and a target line in Python." Often live in a notebook.

> [!tip] Strong answer includes
> - Figure vs Axes; OO API over pyplot for control
> - Right chart type for the question
> - Labels, title, units, legend, readable ticks
> - Saves with `savefig` before `show`

---

## 2. Subplots
> 🔴 Tier 1 · _Tracker hint:_ fig, axes = plt.subplots(2,2); axes[0,0].plot(x,y); plt.tight_layout()

### Definition
`plt.subplots(nrows, ncols)` returns a Figure and an array of Axes, letting you put several related charts on one canvas.

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)
axes[0, 0].plot(months, sales);       axes[0, 0].set_title("Sales")
axes[0, 1].bar(months, units);        axes[0, 1].set_title("Units")
axes[1, 0].hist(lead_times, bins=10); axes[1, 0].set_title("Lead time")
axes[1, 1].scatter(price, qty);       axes[1, 1].set_title("Price vs qty")
fig.suptitle("Q1 Dashboard")
plt.tight_layout()                    # avoid overlaps
```
For a 1-D grid (`1, 3`) `axes` is a 1-D array, so index with `axes[0]`. `sharex`/`sharey` align scales. `plt.subplot_mosaic` allows unequal layouts and `constrained_layout=True` is a modern alternative to `tight_layout`.

### Example
A 2x2 panel for a plant review: trend of OEE, Pareto of defects, histogram of cycle times, scatter of temperature vs scrap. Four views let a manager answer "what, where, how variable, why" on one slide.

### In the news
See news box. Static multi-panel Matplotlib figures remain the standard for reports and slides, while Plotly covers interactive versions.

### Interview angle
> [!question] How it is asked
> "Create a 2x2 dashboard of key supply chain metrics."

> [!tip] Strong answer includes
> - Correct `subplots` unpacking and indexing
> - `tight_layout` or `constrained_layout`
> - Shared axes where comparing; consistent colours
> - One message per panel, not four random charts

---

## 3. Seaborn Plots
> 🔴 Tier 1 · _Tracker hint:_ sns.histplot(), sns.boxplot(), sns.heatmap(corr, annot=True), sns.pairplot(df), sns.barplot()

### Definition
**Seaborn** is a statistical layer on Matplotlib that works directly with DataFrames, adds themes, and computes aggregates and confidence intervals.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
sns.histplot(data=df, x="lead_time", bins=20, kde=True)     # distribution
sns.boxplot(data=df, x="supplier", y="lead_time")           # spread, outliers
sns.barplot(data=df, x="region", y="sales", estimator="sum", errorbar=None)
sns.scatterplot(data=df, x="price", y="qty", hue="region")
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm",
            vmin=-1, vmax=1, fmt=".2f")                     # correlation matrix
sns.pairplot(df[["price", "qty", "cost"]], hue="region")
sns.lineplot(data=long, x="month", y="sales", hue="sku")
```
`barplot` defaults to the **mean** with a confidence interval; use `countplot` for counts. Data should be in **long (tidy) format**. Box plot: box = IQR (Q1 to Q3), line = median, whiskers = 1.5 x IQR, points beyond = outliers.

### Example
Boxplot of lead time by supplier: Supplier A median 6 days with tight box, Supplier B median 6 days but a long upper whisker and outliers at 15+ days. Same average, very different reliability, which a bar of means would hide.

### In the news
See news box. Seaborn 0.13 improved categorical plots and dataframe-library support, and its objects interface offers a grammar-of-graphics style.

### Interview angle
> [!question] How it is asked
> "How would you show the distribution of delivery times across suppliers?" or "How do you read a correlation heatmap?"

> [!tip] Strong answer includes
> - Picks box/violin/histogram for distributions, not bars of means
> - Reads a heatmap: diverging colours centred at 0, annotated values
> - Warns correlation is not causation and checks for outliers
> - Uses `hue` to add a third variable sparingly

---

## 4. Plotly Express (Interactive)
> 🔴 Tier 1 · _Tracker hint:_ px.line(), px.bar(), px.scatter(), px.choropleth(); hover info; export to HTML

### Definition
**Plotly Express** (`px`) creates interactive charts (zoom, pan, hover, legend toggling) with one function call from a DataFrame, and renders in notebooks, Dash apps and standalone HTML.

```python
import plotly.express as px
fig = px.line(df, x="month", y="sales", color="region", markers=True)
fig = px.bar(df, x="region", y="sales", color="category", barmode="group")
fig = px.scatter(df, x="price", y="qty", size="revenue", color="region",
                 hover_data=["sku"], trendline="ols")
fig = px.choropleth(df, geojson=india_geojson, locations="state",
                    featureidkey="properties.ST_NM", color="sales")
fig.update_layout(title="Sales by region", template="plotly_white")
fig.show()
fig.write_html("sales.html")        # shareable interactive file
fig.write_image("sales.png")        # needs the kaleido package
```
`px.choropleth` needs a geometry source (GeoJSON) for Indian states. Plotly is ideal for exploration and dashboards; Matplotlib for print-quality static figures.

### Example
`px.scatter` of price vs quantity with `size=revenue` and hover on SKU lets a category manager hover over a single outlier and identify the product immediately, which a static plot cannot do. Emailing `sales.html` shares the same interactivity without a server.

### In the news
See news box. Plotly.py 6 adds native Polars and PyArrow support through Narwhals and improved array performance, useful for large datasets.

### Interview angle
> [!question] How it is asked
> "When would you use Plotly over Matplotlib?" or "Build an interactive map of sales by state."

> [!tip] Strong answer includes
> - Interactivity for exploration and dashboards; static for print
> - Express vs graph_objects trade-off (speed vs control)
> - `write_html` for sharing; Dash/Streamlit for apps
> - Awareness of performance limits on huge point counts

---

## 5. Chart Selection Guide
> 🔴 Tier 1 · _Tracker hint:_ Line→trend; Bar→comparison; Scatter→correlation; Box→distribution; Heatmap→correlation matrix

### Definition
Pick the chart from the **question**, not from habit.

| Question | Chart |
|---|---|
| How does it change over time? | Line (area for cumulative) |
| Which category is bigger? | Bar (horizontal for long labels), sorted |
| Are two numbers related? | Scatter (+ trendline) |
| How is it distributed? | Histogram, box, violin |
| Part of a whole? | Stacked bar or 100% bar; pie only for 2-4 slices |
| Many variables at once? | Heatmap, small multiples, pairplot |
| Contribution to a total change? | Waterfall |
| Ranking with cumulative effect? | Pareto (bars + cumulative line) |
| Geography? | Choropleth or bubble map |

Principles: start bars at zero, avoid 3-D and dual axes without need, limit colours, sort categories, label directly, one message per chart.

### Example
"Why did OTIF fall?" A line chart of OTIF over 12 months shows when; a Pareto of late-delivery causes shows why; a box plot by carrier shows who. Three charts, one story. A pie of 12 carriers would be unreadable.

### In the news
See news box. As libraries make charting a single line of code, judgment about the right chart is the differentiating skill.

### Interview angle
> [!question] How it is asked
> "Which chart would you use to show X, and why?" Often with a small dataset on a case.

> [!tip] Strong answer includes
> - Starts from the question and audience
> - Names the chart and a reason (e.g. bar for comparison)
> - Mentions pitfalls: truncated axes, pie overload, dual axes
> - Highlights the "so what" with a title that states the insight

---

## 6. Styling & Annotations
> 🔴 Tier 1 · _Tracker hint:_ plt.title(), plt.xlabel(), plt.legend(), plt.axhline(), plt.annotate()

### Definition
Good styling turns a plot into a message.

```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months, sales, marker="o", color="#1f77b4", label="Actual")
ax.axhline(140, color="red", linestyle="--", label="Target 140")
ax.axvspan("Mar", "Apr", alpha=0.15, color="grey")      # highlight a period
ax.annotate("Festival peak", xy=("Apr", 150), xytext=("Feb", 155),
            arrowprops=dict(arrowstyle="->"))
ax.set_title("Sales beat target in April", fontsize=14, weight="bold")
ax.set_xlabel("Month"); ax.set_ylabel("Units (000)")
ax.legend(loc="upper left", frameon=False)
ax.grid(alpha=0.3)
ax.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
plt.xticks(rotation=45)
```
Always include units, a title stating the takeaway, readable fonts, and colourblind-safe colours. Global styling via `plt.style.use("seaborn-v0_8-whitegrid")` or `sns.set_theme()`.

### Example
A plain line of sales is replaced by one with a dashed red target at 140 and an annotation at the April peak (150). The viewer sees immediately that only April exceeded target by 10 units (7.1% = 10/140).

### In the news
See news box. Plotly.py 6 removed several old title attributes (`titlefont`, `titleposition`), so styling code copied from old tutorials may need updating.

### Interview angle
> [!question] How it is asked
> "Make this chart presentation-ready for the leadership team."

> [!tip] Strong answer includes
> - Insight-led title, labelled axes with units
> - Reference line (target/average) and a key annotation
> - Declutter: gridlines light, fewer colours, no chartjunk
> - Consistent colour meaning across charts

---

## 7. Color Palettes
> 🔴 Tier 1 · _Tracker hint:_ sns.color_palette('viridis'); categorical vs sequential vs diverging

### Definition
Three palette families, each for a data type.

| Type | Use for | Examples |
|---|---|---|
| **Categorical (qualitative)** | Unordered groups | `tab10`, `Set2`, `colorblind` |
| **Sequential** | Ordered low-to-high magnitude | `viridis`, `Blues`, `rocket` |
| **Diverging** | Values around a meaningful midpoint (0, target) | `coolwarm`, `RdBu`, `vlag` |

```python
sns.color_palette("viridis", 6)         # list of 6 RGB colours
sns.set_palette("colorblind")
sns.heatmap(corr, cmap="coolwarm", center=0)
sns.barplot(data=df, x="region", y="sales", palette="Set2", hue="region", legend=False)
plt.scatter(x, y, c=z, cmap="viridis")
```
Guidelines: about 8% of men have a colour-vision deficiency, so avoid red-green only encoding; prefer perceptually uniform maps (viridis) over rainbow/jet; use a single highlight colour with grey for the rest to direct attention; keep meaning consistent (e.g. red always = bad).

### Example
A correlation heatmap uses a diverging map centred at 0: strong positive = deep red, strong negative = deep blue, near zero = white. A sequential map would hide the sign. For a sales-by-state map, a sequential single-hue palette (Blues) fits since values only increase.

### In the news
See news box. Seaborn's objects interface and theme options continue to ship accessible defaults, but explicit palette choice is still the analyst's job.

### Interview angle
> [!question] How it is asked
> "What colour scheme would you use for this heatmap/map and why?"

> [!tip] Strong answer includes
> - Matches palette type to data type
> - Colourblind safety and print/greyscale legibility
> - Highlight-with-grey strategy
> - Consistent colour semantics across a deck

---

## 8. Saving Figures
> 🔴 Tier 1 · _Tracker hint:_ plt.savefig('chart.png', dpi=300, bbox_inches='tight')

### Definition
```python
plt.savefig("chart.png", dpi=300, bbox_inches="tight", transparent=False)
fig.savefig("chart.pdf")                 # vector: crisp in reports
fig.savefig("chart.svg")                 # vector: editable
fig.savefig("chart.png", dpi=150, facecolor="white")
```
- `dpi`: 100-150 for slides/web, 300 for print.
- `bbox_inches="tight"` stops labels from being clipped.
- Call `savefig` **before** `plt.show()`, otherwise the saved image can be blank because `show` clears the figure.
- Vector formats (PDF, SVG) scale without blur; PNG for raster.
- Plotly: `fig.write_html("c.html")`, `fig.write_image("c.png", scale=2)` (requires kaleido).
- Close figures in loops (`plt.close(fig)`) to release memory.
- Pixel size = `figsize x dpi`, so (10, 6) at 300 dpi is 3000 x 1800 pixels.

### Example
A weekly report job loops over 50 SKUs, saving `fig.savefig(f"out/{sku}.png", dpi=150, bbox_inches="tight")` then `plt.close(fig)`. Without the close, 50 open figures would trigger a Matplotlib memory warning (it warns beyond 20 open figures).

### In the news
See news box. Plotly's static-image export relies on a separate package, a common deployment snag in automated reporting jobs.

### Interview angle
> [!question] How it is asked
> "How would you automate a weekly chart pack?"

> [!tip] Strong answer includes
> - `savefig` parameters (dpi, tight bbox) and format choice
> - Save before show; close figures in loops
> - Parameterised loop or function; scheduled run
> - Embeds charts into PPT/PDF/email downstream

---

## 9. ⭐ Advanced: Data Storytelling & Dashboard Design
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Consultants and PMs are judged on the **message**, not the code.

- **Action title:** state the insight ("Late deliveries concentrate in 3 of 12 lanes"), not the topic.
- **Pyramid / SCQA** structure: Situation, Complication, Question, Answer.
- **Data-ink ratio** (Tufte): remove non-informative ink; **small multiples** for comparing many groups.
- **Pre-attentive attributes:** colour, size and position guide the eye; highlight one thing.
- **Dashboards:** KPI cards at the top, trend in the middle, drill-downs below; limit to 5-7 visuals; consistent filters. Tools: Power BI, Tableau, Streamlit, Dash, Plotly.
- **Pitfalls:** truncated bar axes, dual axes, 3-D pies, cherry-picked ranges, unlabelled units, correlation shown as causation.
- **Accessibility:** colour-blind-safe palettes, adequate font size, alt text.

```python
import streamlit as st
st.metric("OTIF", "92%", "-3 pp")
st.plotly_chart(fig, use_container_width=True)
```

### Example
Instead of a chart titled "OTIF by month", write "OTIF fell 6 points since June, driven by two carriers", plot the monthly line in grey, highlight the two carriers in red, and add one annotation on the June event. The audience gets the answer in five seconds.

### In the news
See news box. With charting libraries converging on multiple dataframe backends, effort shifts from producing charts to choosing and framing them.

### Interview angle
> [!question] How it is asked
> "Here is a dataset. Prepare one slide for the COO."

> [!tip] Strong answer includes
> - One message, an action title, one highlighted series
> - Structure the narrative (what, so what, now what)
> - Quantified recommendation with a next step
> - Anticipates the "how reliable is this data?" question

---

## 10. ⭐ Advanced: Statistical & Operations-Specific Charts
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Charts that recur in operations and quality case work.

- **Pareto chart:** bars sorted descending plus cumulative % line; the 80/20 rule for defects, SKUs or delay causes.
- **Control chart (X-bar / I-MR):** time series with centre line and $\pm 3\sigma$ limits; points beyond limits or runs signal special-cause variation.
- **Histogram with spec limits and Cpk:** $C_{pk} = \min\left(\frac{USL-\mu}{3\sigma}, \frac{\mu-LSL}{3\sigma}\right)$.
- **Waterfall:** bridge from last year's cost to this year's.
- **Gantt:** project schedules (`px.timeline`).
- **Forecast-vs-actual with prediction intervals:** `ax.fill_between(x, lo, hi, alpha=0.2)`.
- **Sankey:** flows across the network (`plotly.graph_objects.Sankey`).

```python
counts = df["cause"].value_counts()
cum = counts.cumsum() / counts.sum() * 100
ax = counts.plot.bar(); ax2 = ax.twinx(); ax2.plot(range(len(cum)), cum.values, "r-o")
```

### Example
Defect causes: 50, 30, 10, 5, 5 (total 100). Cumulative: 50%, 80%, 90%, 95%, 100%. The first two causes explain 80%, so fixing them first gives the best return. Control chart: mean 100, sigma 2, so limits are 94 and 106; a reading of 107 is out of control.

### In the news
See news box. Plotly.py 6 removed the old `transforms` feature, so group/filter logic is now done in pandas before plotting.

### Interview angle
> [!question] How it is asked
> "How would you visualise quality problems in a plant to prioritise fixes?"

> [!tip] Strong answer includes
> - Pareto for prioritisation; control chart for stability over time
> - Explains the 80/20 reading and the $3\sigma$ limits
> - Chooses the chart to match the decision
> - Links to action: which cause, owner, expected gain

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
