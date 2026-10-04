---
tags: [python-programming, tier2]
area: Python Programming
topic: "Python Data Cleaning & EDA Playbook"
tier: Tier 2
roles: Analytics / Operations
status: complete
subtopics: 13
---
# Python Data Cleaning & EDA Playbook

⬅ [[185 Python Interview Problem Bank]] · [[_Index - Python Programming|Python Programming]]

> **Area:** Python Programming · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / Operations

## Sub-topics in this note
1. [[#1. Systematic EDA Checklist]]
2. [[#2. Worked Case: A Messy ERP Purchase-Order Export]]
3. [[#3. Type Fixes: Numbers, IDs & Categories]]
4. [[#4. Date & Time Normalisation]]
5. [[#5. Text Normalisation & Standard Mappings]]
6. [[#6. Duplicates & Fuzzy Matching]]
7. [[#7. Missing Data: MCAR, MAR, MNAR]]
8. [[#8. Imputation Strategies]]
9. [[#9. Outliers: IQR, Z-Score & MAD]]
10. [[#10. Validation: Assertions & Pandera Schemas]]
11. [[#11. Profiling Tools]]
12. [[#12. Reproducible Cleaning Pipeline]]
13. [[#13. ⭐ Advanced: Control Totals, Reconciliation & Audit Trail]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the data-cleaning toolchain changed under analysts' feet
> **pandas 3.0 (21 January 2026).** The release notes list a default `str` dtype for text columns (replacing NumPy `object`; it holds only strings or missing values), Copy-on-Write semantics (chained assignment never works; `SettingWithCopyWarning` removed), datetime inference that is no longer nanosecond-only, and a minimum Python of 3.11. Cleaning code that relied on `object` columns holding mixed types, or on chained assignment, needs review. ([pandas 3.0.0 release notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html))
>
> **Validation and profiling tools (2026).** pandera 0.33.1 was released on 1 September 2026; for pandas frames the documented import path is `pandera.pandas` (importing `DataFrameSchema` from the top level raises a `FutureWarning`) ([PyPI](https://pypi.org/project/pandera/)). The profiling library formerly named ydata-profiling (and before that pandas-profiling) is now published as **fg-data-profiling** (4.20.0, 11 September 2026): imports change from `ydata_profiling` to `data_profiling`, the old package no longer receives fixes, and the new package lists Python 3.10 up to but excluding 3.15 ([PyPI](https://pypi.org/project/fg-data-profiling/)). Checked 4 October 2026; confirm versions before installing.
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Systematic EDA Checklist
> 🟠 Tier 2 · _Key points:_ ten-minute health check before any analysis, disguised missing values, cardinality, dtypes

### Definition
Exploratory data analysis (EDA) for cleaning has a fixed order so that nothing is missed. Work **outside-in**: the file, then columns, then values, then relationships.

1. **Provenance**: source system, extract date and filters, row count and control totals from the source (see [[175 Data Quality, Master Data & Data Governance]]).
2. **Shape and types**: rows, columns, inferred dtypes. Read everything as text first (`dtype=str, keep_default_na=False`) so the parser cannot silently convert.
3. **Missingness**: real nulls and **disguised nulls** (`-`, `N/A`, `0`, `9999`, `1900-01-01`, "TBD").
4. **Cardinality and keys**: distinct counts, candidate unique key, duplicates (exact and by business key).
5. **Validity**: ranges, formats, allowed values, units of measure, cross-column rules (delivery after order, qty x price = value).
6. **Distribution**: `describe()`, histograms, quantiles, outliers per group.
7. **Consistency across tables**: joins to master data; orphan keys.
8. **Time**: gaps, duplicates and spikes by date; time zones.
9. **Decisions log**: every fix, its rule and the rows affected.

```python
import numpy as np
import pandas as pd

def quick_eda(df: pd.DataFrame, tokens=("", "-", "N/A", "NA", "NULL", "?")) -> pd.DataFrame:
    """One-screen health check: types, blanks, disguised blanks, cardinality, example."""
    s = df.astype("string")
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "nulls": df.isna().sum(),
        "disguised_null": s.apply(lambda c: c.str.strip().isin(tokens).sum()),
        "distinct": df.nunique(),
        "example": s.iloc[0],
    })
```
The function is applied to a real messy extract in the next sub-topic.

### Example
A planner receives a "clean" PO export. `df.isna().sum()` shows zero nulls, yet `quick_eda` finds `N/A` in the quantity column and `-` in price: the nulls were disguised as text, and `pd.to_numeric` would have either failed or quietly produced NaN depending on options. Total time to find: under a minute. Skipping the check means the first symptom is a wrong spend figure in front of a stakeholder.

### In the news
See news box. In pandas 3.0 `df.dtypes` shows `str` for text columns where earlier versions showed `object`, so a "mixed-type object column" now has to be handled explicitly.

### Interview angle
> [!question] How it is asked
> "You are given a new dataset from the ERP. Walk me through what you do before building any analysis."

> [!tip] Strong answer includes
> - Outside-in order: source and control totals, shape/types, missing, keys/duplicates, validity, distributions, joins
> - Disguised missing values and units/format mismatches, not only `isna()`
> - Writing down each cleaning rule and its row impact
> - Reconciling the cleaned data back to a source control total; see [[064 Pandas — Data Manipulation]] for the mechanics

---
## 2. Worked Case: A Messy ERP Purchase-Order Export
> 🟠 Tier 2 · _Key points:_ SAP-style text export, leading-zero material numbers, trailing minus, mixed dates, vendor name variants

### Definition
The case used for the rest of this note: an 11-line purchase-order extract in the style of an SAP list download (see [[080 SAP MM — Materials Management]] and [[085 SAP Reporting & Analytics]]) with realistic defects:

| Defect | Where |
|---|---|
| Material numbers padded to 15 characters with leading zeros | `Material` |
| Thousands separators, Indian grouping (`1,20,000`), SAP trailing minus (`950-`), `N/A`, `-` | `Qty`, `Net_Price` |
| Five date formats and one blank | `Order_Date` |
| Same vendor spelled eight ways | `Vendor` |
| UoM variants (`EA`, `Each`, `PC`, `nos`, `kg `, `Kgs`) | `UoM` |
| Extra spaces, mixed case | `Description`, `Status` |
| One exact duplicate row | PO 4500003 |
| One implausible quantity (1,20,000 oil seals) | PO 4500004 item 20 |

```python
import io
import numpy as np
import pandas as pd

RAW = """PO_No,Item,Material,Description,Vendor,Order_Date,Qty,UoM,Net_Price,Status
4500001,10,000000000010234, Bearing 6205 ZZ ,Tata Steel Ltd,15.01.2026,"1,200",EA,250.00,OPEN
4500001,20,000000000010871,Oil seal 35x52,TATA STEEL LIMITED,15.01.2026,500,Each,40.50,open
4500002,10,000000000010234,Bearing 6205 ZZ,Bharat Forge Ltd,2026-01-16,"2,000",PC,248.00,OPEN
4500003,10,000000000020555,Hex bolt M12 (10.9),Sundaram Fasteners,17/01/2026,"12,000",nos,3.25,CLOSED
4500003,10,000000000020555,Hex bolt M12 (10.9),Sundaram Fasteners,17/01/2026,"12,000",nos,3.25,CLOSED
4500004,10,000000000030100,Hydraulic hose 1/2in,Tata Steel Ltd.,20260118,150,EA,"1,250.50",Open
4500004,20,000000000010871,Oil seal 35x52,Bharat Forge Limited,19-Jan-26,"1,20,000",EA,41.00,OPEN
4500005,10,000000000040020,Steel rod 16mm,TATA STEEL LTD,2026-01-20,"2,500",KG,68.20,OPEN
4500005,20,000000000040020,Steel rod 16mm,Tata Steel Ltd,2026-01-20,"950-",kg ,68.20,RETURN
4500006,10,000000000030100,Hydraulic hose 1/2in,Sundaram Fasteners,,N/A,EA,-,OPEN
4500007,10,000000000010234,Bearing 6205 ZZ,bharat forge ltd,22.01.2026,800,Kgs,246.50,OPEN
"""
raw = pd.read_csv(io.StringIO(RAW), dtype=str, keep_default_na=False)   # read EVERYTHING as text first

# EDA first pass: shape, types, blanks, cardinality, duplicates
print(raw.shape)
print((raw == "").sum()[lambda s: s > 0].to_dict())                    # blanks per column
print(raw.nunique().to_dict())
print(raw.duplicated().sum(), raw.duplicated(["PO_No", "Item"]).sum())
print(raw["UoM"].value_counts().to_dict())
print(raw["Vendor"].nunique(), raw["Vendor"].str.lower().str.replace(r"[^a-z ]", "", regex=True).str.strip().nunique())

print(quick_eda(raw).reindex(["Order_Date", "Qty", "Net_Price", "UoM"]).to_string())
```
Output: shape `(11, 10)`; the only real blank is in `Order_Date`; 1 exact duplicate and 1 duplicate PO/item key; 8 vendor spellings that collapse to only 5 after lower-casing and stripping punctuation (the `LIMITED` versus `LTD` difference needs a rule); `quick_eda` finds one disguised null each in `Order_Date`, `Qty` and `Net_Price`, and reports dtype `str` under pandas 3.0 (`object` in older versions).

### Example
The first pass already tells the story: three disguised nulls that `isna()` misses, three UoM spellings for what should be "each", and eight vendor strings for what is really three suppliers (Tata Steel, Bharat Forge, Sundaram Fasteners). Cleaning is therefore a set of rules to write, not one function call.

### In the news
See news box. The export is read as text because pandas 3.0's stricter `str` dtype and `dtype=str` together make the later parsing step explicit.

### Interview angle
> [!question] How it is asked
> "Here is a CSV downloaded from SAP. What problems do you expect and how do you check for them?"

> [!tip] Strong answer includes
> - Leading zeros on IDs, trailing minus signs, locale decimal and thousand separators, mixed date formats
> - Reading as text first, then converting with explicit rules
> - Looking for duplicates by business key as well as exact rows
> - Checking vendor/material names against the master data

---
## 3. Type Fixes: Numbers, IDs & Categories
> 🟠 Tier 2 · _Key points:_ parse rules not `astype`, IDs are text, trailing minus, categories

### Definition
Convert types **with explicit parsing rules**; `astype(float)` on messy text either raises or hides problems. Rules of thumb: identifiers (material, PO, GSTIN, PIN code, phone) are **text** even when they look numeric; money and quantities are floats or, for exact accounting, `Decimal`/integer paise; low-cardinality repeated labels (status, UoM, plant) are `category`; flags are `bool`. Use `pd.to_numeric(..., errors="coerce")` only after you have counted what coercion will turn into NaN.

```python
import re

MISSING_TOKENS = {"", "-", "N/A", "NA", "n/a", "NULL", "null", "None", "#N/A", "?"}

def parse_sap_number(x: str) -> float:
    """'1,20,000' -> 120000.0 ; '950-' (SAP trailing minus) -> -950.0 ; '-' / 'N/A' -> NaN."""
    s = str(x).strip()
    if s in MISSING_TOKENS:
        return np.nan
    neg = s.endswith("-") or (s.startswith("(") and s.endswith(")"))   # 950-  or  (950)
    s = re.sub(r"[^\d.]", "", s)                                        # drop commas, spaces, currency signs
    return -float(s) if neg else float(s)

assert parse_sap_number("1,20,000") == 120000 and parse_sap_number("950-") == -950
assert parse_sap_number("1,250.50") == 1250.5 and np.isnan(parse_sap_number("N/A")) and np.isnan(parse_sap_number("-"))

df = raw.copy()
df["Qty"] = df["Qty"].map(parse_sap_number)
df["Net_Price"] = df["Net_Price"].map(parse_sap_number)
df["Material"] = df["Material"].str.strip()                    # IDs stay text: keeps leading zeros
df["Material_Short"] = df["Material"].str.lstrip("0")          # for display or joins to a master without zeros
df["PO_No"] = df["PO_No"].astype("string")
df["Item"] = pd.to_numeric(df["Item"]).astype("int16")
df["Status"] = df["Status"].str.strip().str.upper().astype("category")
print(df.filter(["Qty", "Net_Price"]).dtypes.to_dict(), df["Qty"].isna().sum(), df["Net_Price"].isna().sum())
assert df["Qty"].tolist()[:3] == [1200.0, 500.0, 2000.0] and df.loc[8, "Qty"] == -950
assert df["Material_Short"].iloc[0] == "10234"

# Integers read as float lose nothing here, but IDs read as numbers lose leading zeros:
bad = pd.read_csv(io.StringIO(RAW))["Material"].iloc[0]
print(bad, type(bad).__name__)
```
Output: both columns `float64` with one NaN each, and the last line shows `10234 int64`: letting `read_csv` infer types turned `000000000010234` into the integer 10,234, so it would no longer join to the SAP master.

### Example
`1,20,000` is 1.2 lakh written in Indian grouping, and removing every comma gives 120,000 correctly; a parser that assumes thousands groups of three might mis-read it. `950-` becomes -950: a goods return. If you had used `to_numeric(errors="coerce")` directly, every trailing-minus quantity would become NaN and returns would vanish from the analysis without a warning.

### In the news
See news box. pandas 3.0's `str` dtype stores only strings or missing values, which makes accidental mixed-type ID columns fail early instead of staying hidden in `object`.

### Interview angle
> [!question] How it is asked
> "A merge on material number returns no rows even though the materials exist. Why?"

> [!tip] Strong answer includes
> - IDs read as integers lose leading zeros, or one table has padded and the other unpadded numbers
> - Strip, pad (`zfill(15)`) or un-pad consistently on both sides before joining
> - Trailing minus, thousands separators and locale decimals
> - Counting NaNs before and after conversion

---
## 4. Date & Time Normalisation
> 🟠 Tier 2 · _Key points:_ known formats in order, day-first ambiguity, Excel serials, never guess silently

### Definition
Dates arrive as `15.01.2026`, `2026-01-16`, `17/01/2026`, `20260118`, `19-Jan-26`, Excel serial numbers and plain text like "TBD". Prefer an **explicit list of formats tried in order**, returning `NaT` (not a guess) when none fits. Ambiguity is real: `03/04/2026` is 3 April in India and 4 March in the US, so decide per source system and test with unambiguous rows (a day above 12). Excel stores dates as serial numbers (days since 30 December 1899 for modern files). Store timestamps in one zone (UTC or IST) and keep the source's zone in a column if needed.

```python
from datetime import datetime

def parse_date(s: str):
    """Try the known formats in a fixed order; return NaT if none fits (never guess silently)."""
    s = str(s).strip()
    if s in MISSING_TOKENS:
        return pd.NaT
    for fmt in ("%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y", "%Y%m%d", "%d-%b-%y"):
        try:
            return pd.Timestamp(datetime.strptime(s, fmt))
        except ValueError:
            continue
    return pd.NaT

df["Order_Date"] = pd.to_datetime(raw["Order_Date"].map(parse_date))
print(df["Order_Date"].dt.strftime("%Y-%m-%d").tolist())
assert df["Order_Date"].notna().sum() == 10 and df["Order_Date"].iloc[6] == pd.Timestamp("2026-01-19")
assert df["Order_Date"].iloc[3] == pd.Timestamp("2026-01-17")           # 17/01/2026 is day-first, as 17 cannot be a month

# Ambiguity demo: 03/04/2026 is 3 April or 4 March?
print(pd.to_datetime("03/04/2026", dayfirst=True), pd.to_datetime("03/04/2026", dayfirst=False))
# Excel serial dates (numbers) convert with an origin
print(pd.to_datetime(46037, unit="D", origin="1899-12-30"))
```
Output: ten valid dates from 15 to 22 January 2026 and one `NaT` (printed `nan` by `strftime`), then `2026-04-03` versus `2026-03-04`, then `2026-01-15` for Excel serial 46037.

### Example
`19-Jan-26` parses as 19 January 2026 with `%d-%b-%y`; the blank in PO 4500006 stays `NaT` and is later flagged by validation instead of being filled with today's date. Delivery-date logic then works: `(delivery - order).dt.days` gives lead time. Related Excel date logic is in [[073 Text & Date Functions]].

### In the news
See news box. pandas 3.0 no longer defaults datetimes to nanoseconds, so very old placeholder dates (for example `1900-01-01`) or far-future "never expires" dates (`9999-12-31`) no longer overflow, but they should still be treated as disguised nulls.

### Interview angle
> [!question] How it is asked
> "The date column has several formats and some are ambiguous. How do you convert it safely?"

> [!tip] Strong answer includes
> - Explicit formats and `errors` policy; no silent inference with `dayfirst` guesses on mixed data
> - Check ambiguity with rows that cannot be misread (day above 12)
> - Sentinel dates (`1900-01-01`, `9999-12-31`) as missing
> - Time zones, fiscal-year (April to March) and week-start rules documented

---
## 5. Text Normalisation & Standard Mappings
> 🟠 Tier 2 · _Key points:_ whitespace, case, Unicode, legal suffixes, UoM maps, cross-checks with master data

### Definition
Text cleaning is a sequence of small, testable steps: Unicode normalisation (`NFKC`), collapse whitespace, trim, consistent case, remove punctuation noise, strip legal suffixes (`Ltd`, `Limited`, `Pvt`), and map variants to a **controlled vocabulary** through a dictionary (`UOM_MAP`). Unmapped values should become NaN or a visible "UNMAPPED" bucket, never pass silently. Then check **business consistency**: one base UoM per material, one currency per vendor.

```python
UOM_MAP = {"EA": "EA", "EACH": "EA", "PC": "EA", "PCS": "EA", "NOS": "EA",
           "KG": "KG", "KGS": "KG"}

def clean_text(s: pd.Series) -> pd.Series:
    return (s.str.normalize("NFKC")                      # unify odd Unicode forms (non-breaking spaces, full-width)
             .str.replace(r"\s+", " ", regex=True)       # collapse runs of whitespace
             .str.strip())

def canon_vendor(s: pd.Series) -> pd.Series:
    t = clean_text(s).str.lower().str.replace(r"[.,]", "", regex=True)
    t = t.str.replace(r"\b(limited|ltd)\b$", "", regex=True).str.strip()       # legal suffixes
    return t.str.title()

df["Description"] = clean_text(df["Description"])
df["UoM"] = clean_text(df["UoM"]).str.upper().map(UOM_MAP)                      # unmapped codes become NaN, visible
df["Vendor_Clean"] = canon_vendor(df["Vendor"])
print(sorted(df["Vendor_Clean"].unique()), df["UoM"].isna().sum())
assert df["Vendor_Clean"].nunique() == 3 and df["UoM"].isna().sum() == 0
assert df["Description"].nunique() == 5          # was 6 before trimming

# Material master truth: one base UoM per material. Which rows break it?
mode_uom = df.groupby("Material")["UoM"].agg(lambda s: s.mode().iat[0])
df["uom_mismatch"] = df["UoM"] != df["Material"].map(mode_uom)
print(df.loc[df["uom_mismatch"], ["PO_No", "Material_Short", "UoM"]].to_string(index=False))
```
Output: `['Bharat Forge', 'Sundaram Fasteners', 'Tata Steel'] 0`, then the one row whose UoM disagrees with its material: PO 4500007, material 10234 (a bearing) recorded as `KG`.

### Example
Eight vendor strings collapse to three suppliers, and six distinct descriptions collapse to five once the stray spaces are trimmed. The bearing ordered "800 Kgs" is almost certainly a UoM error, since bearings are counted in each; rules based on master data catch it where purely statistical checks cannot. Vendor consolidation matters commercially: the same supplier under several names understates spend concentration (see [[122 Spend Analysis, Savings & Procurement Maturity]]).

### In the news
See news box. pandas 3.0's `str` dtype makes the `.str` accessor available only on genuine text columns, so a numeric column accidentally passed to a text cleaner fails loudly.

### Interview angle
> [!question] How it is asked
> "The same supplier appears under many spellings in the spend data. How do you fix it?"

> [!tip] Strong answer includes
> - Rule-based normalisation first (case, punctuation, suffixes), then a mapping table owned by the business
> - Fuzzy matching only for the residue, with a human-review band
> - Cross-field rules against master data (UoM, currency, plant)
> - Keeping the original column alongside the cleaned one for audit

---
## 6. Duplicates & Fuzzy Matching
> 🟠 Tier 2 · _Key points:_ exact vs key duplicates, keep rule, rapidfuzz scores, blocking, accept/review thresholds

### Definition
Three kinds of duplicates: **exact** (all columns equal; `duplicated()`), **business-key** (same PO and item but different values: needs a keep rule such as latest timestamp), and **entity** (same real-world supplier or customer written differently: needs fuzzy matching). Fuzzy matching scores string similarity (Levenshtein-based ratio, token-sort, `WRatio`). Use **thresholds with a review band**: accept above ~90, send 75-90 to a human, reject below. For large lists, use **blocking** (compare only names sharing a first letter or PIN code) to avoid $n^2$ comparisons. Always keep a crosswalk table (raw name to master name) for audit.

```python
# Exact duplicates, then business-key duplicates
exact = df.duplicated(keep="first")
key_dup = df.duplicated(["PO_No", "Item"], keep=False)
print(int(exact.sum()), int(key_dup.sum()))
assert exact.sum() == 1 and df.loc[key_dup, "PO_No"].tolist() == ["4500003", "4500003"]
dedup = df.drop_duplicates(keep="first")
assert len(dedup) == len(df) - 1

# Fuzzy matching for names that rules cannot normalise (needs: pip install rapidfuzz)
from rapidfuzz import fuzz, process
master = ["Tata Steel", "Bharat Forge", "Sundaram Fasteners", "Mahindra Forgings"]
messy = ["Tata Stel", "Bharath Forge", "Sundaram Fastners", "Sundram Fasteners Pvt", "Tata Motors"]
for name in messy:
    best, score, _ = process.extractOne(name, master, scorer=fuzz.WRatio)
    print(f"{name!r:28} -> {best!r:22} {score:5.1f}", "ACCEPT" if score >= 90 else "REVIEW")
res = {n: process.extractOne(n, master, scorer=fuzz.WRatio)[1] for n in messy}
assert res["Tata Stel"] >= 90 and res["Tata Motors"] < 90
```
Output: `1 2` (one exact duplicate row to drop, two rows sharing a PO/item key), then scores: Tata Stel 94.7, Bharath Forge 96.0, Sundaram Fastners 97.1 (accepted), `Sundram Fasteners Pvt` 87.2 (review) and `Tata Motors` 57.1 (a different company; do not merge).

### Example
Tata Steel and Tata Motors share a token and a brand but are different legal entities; a threshold of 90 correctly refuses to merge them (57.1), while the typo variants are accepted. The 87.2 case shows why a review band exists: a missing "a" plus "Pvt" is probably the same supplier but money is at stake, so a person confirms. Master-data duplicate control is part of [[175 Data Quality, Master Data & Data Governance]].

### In the news
See news box. `drop_duplicates` and `duplicated` behave the same in pandas 3.0; what changes is that results are always new objects under Copy-on-Write.

### Interview angle
> [!question] How it is asked
> "How would you de-duplicate a vendor master of 50,000 records with spelling variations?"

> [!tip] Strong answer includes
> - Normalise first, then block, then score, then threshold with a manual-review band
> - Precision versus recall of the matcher and the cost of a wrong merge
> - Survivorship rule (which record's address and bank details win)
> - Crosswalk table and audit trail; prevent new duplicates at entry

---
## 7. Missing Data: MCAR, MAR, MNAR
> 🟠 Tier 2 · _Key points:_ why data is missing decides what is safe, bias demonstration

### Definition
- **MCAR** (missing completely at random): the chance of being missing is the same for every row, unrelated to any data. Dropping rows is unbiased (but loses power).
- **MAR** (missing at random): missingness depends on **observed** variables (long-distance lanes have more missing lead times). Unbiased analysis is possible by conditioning on those variables.
- **MNAR** (missing not at random): missingness depends on the **missing value itself** (suppliers with long lead times avoid reporting them). No fix from the data alone; needs domain knowledge, sensitivity analysis or new data collection.

Diagnostics: compare other variables between missing and non-missing groups (t-test, chi-square), plot missing-pattern matrices; formal MCAR tests exist (Little's test in R or specialised packages) but a domain argument is usually stronger.

```python
# Missingness mechanisms on a simulated lead-time column (true mean is known)
rng = np.random.default_rng(7)
n = 20_000
dist_km = rng.uniform(50, 1500, n)                                   # distance of the lane
lead = 2 + 0.006 * dist_km + rng.normal(0, 1, n)                     # true lead time in days
full = pd.DataFrame({"dist_km": dist_km, "lead": lead})

def drop(mask_prob):                                                  # delete values with given probabilities
    out = full.copy()
    out.loc[rng.random(n) < mask_prob, "lead"] = np.nan
    return out

mcar = drop(np.full(n, 0.20))                                         # same 20% chance everywhere
mar  = drop(np.where(full["dist_km"] > 800, 0.40, 0.05))              # depends on an OBSERVED column
mnar = drop(np.where(full["lead"] > full["lead"].median(), 0.35, 0.05))  # depends on the missing value itself

true_mean = full["lead"].mean()
for name, d in [("MCAR", mcar), ("MAR", mar), ("MNAR", mnar)]:
    print(name, "missing %.1f%%" % (100 * d["lead"].isna().mean()), "observed mean %.2f" % d["lead"].mean(), "true %.2f" % true_mean)

# MAR can be fixed with the observed driver: impute within distance bands
mar["band"] = pd.cut(mar["dist_km"], [0, 400, 800, 1200, 1600])
mar["lead_band"] = mar["lead"].fillna(mar.groupby("band", observed=True)["lead"].transform("median"))
print("MAR global-mean fill %.2f | band-median fill %.2f | true %.2f" %
      (mar["lead"].fillna(mar["lead"].mean()).mean(), mar["lead_band"].mean(), true_mean))
assert abs(mcar["lead"].mean() - true_mean) < 0.05                    # MCAR: observed mean is unbiased
assert mnar["lead"].mean() < true_mean - 0.2                          # MNAR: biased low
assert abs(mar["lead_band"].mean() - true_mean) < abs(mar["lead"].mean() - true_mean)
```
Output (seed 7): MCAR 20.1% missing, observed mean 6.65 vs true 6.66; MAR 21.6% missing, observed mean 6.18; MNAR 19.9% missing, observed mean 6.23; and for MAR a global-mean fill still gives 6.18 while the distance-band median fill recovers 6.66.

### Example
Deleting missing rows is harmless under MCAR (6.65 vs 6.66) but biases lead time down by about 0.4-0.5 days under MAR and MNAR, because the long lanes and slow suppliers went missing. A planner who sets safety stock from 6.2 days instead of 6.7 would under-protect the very lanes that are most uncertain. Conditioning on distance repairs the MAR case; no observed variable can repair MNAR, so the honest answer is a sensitivity range.

### In the news
See news box. Missing text in pandas 3.0's `str` dtype is `NaN`, and nullable dtypes treat `NaN` and `NA` consistently, so `isna()` counts are the same across dtypes.

### Interview angle
> [!question] How it is asked
> "20% of lead-time values are missing. What do you do?"

> [!tip] Strong answer includes
> - First ask why they are missing (MCAR, MAR, MNAR) and test what predicts missingness
> - MCAR: deletion or simple imputation is acceptable; MAR: impute using the predictors; MNAR: model the mechanism or bound the answer
> - Never impute the target or leak test data; keep a missing-indicator flag
> - Report how much was imputed and the sensitivity of the result

---
## 8. Imputation Strategies
> 🟠 Tier 2 · _Key points:_ delete vs mean/median/mode, group-wise, ffill/interpolate, KNN/MICE, indicators

### Definition
| Method | Use when | Risk |
|---|---|---|
| Drop rows or columns | MCAR, few missing, or column >50-60% empty and unimportant | Loses data; biased if not MCAR |
| Mean / median / mode | Quick baseline; median for skewed values | Shrinks variance, weakens correlations |
| **Group-wise** median/mode | A grouping explains the value (supplier, material, region) | Needs enough rows per group |
| Forward fill / interpolation | Time series: stock levels, prices, sensor readings | Never across long gaps or for event data |
| Constant or "Unknown" | Categorical, when missing is itself informative | Can hide a data issue |
| KNN / iterative (MICE) / model-based | Many related variables, enough data | Complexity; fit inside cross-validation to avoid leakage |
| Multiple imputation | Inference with uncertainty (statistics) | Heavier workflow |
| Domain rule | Known default (zero demand on closed days) | Needs sign-off |

Always add a **missing indicator** when missingness may carry information, and fit imputers on training data only (see [[094 ML Fundamentals & Workflow]]).

```python
# Imputation recipes on a small series and table
s = pd.Series([100, np.nan, np.nan, 130, np.nan, 150],
              index=pd.date_range("2026-01-01", periods=6, freq="D"), name="stock")
print(s.ffill().tolist())                      # carry last observation forward (stock levels, prices)
print(s.interpolate().round(1).tolist())       # straight line between known points (smooth quantities)
assert s.ffill().tolist() == [100, 100, 100, 130, 130, 150]
assert s.interpolate().round(1).tolist() == [100.0, 110.0, 120.0, 130.0, 140.0, 150.0]

lt = pd.DataFrame({"supplier": ["S1", "S1", "S1", "S2", "S2", "S2"],
                   "lead_days": [5, np.nan, 7, 10, np.nan, 14]})
lt["lead_missing"] = lt["lead_days"].isna()                                  # keep an indicator: missingness can carry information
lt["lead_filled"] = lt["lead_days"].fillna(lt.groupby("supplier")["lead_days"].transform("median"))
print(lt["lead_filled"].tolist(), "global mean would give", round(lt["lead_days"].mean(), 1))
assert lt["lead_filled"].tolist() == [5.0, 6.0, 7.0, 10.0, 12.0, 14.0]
assert round(lt["lead_days"].mean(), 1) == 9.0
```
Output: forward fill `[100, 100, 100, 130, 130, 150]`; interpolation `[100, 110, 120, 130, 140, 150]`; group-median fill `[5, 6, 7, 10, 12, 14]` while a global mean (9.0) would give both suppliers' gaps the same value.

### Example
S1 is a Pune supplier (5 to 7 days), S2 is imported (10 to 14 days). Filling S2's gap with the global mean of 9 days would be below its own minimum; the supplier median of 12 is plausible. Forward-filling a stock level across a 2-day gap is acceptable; forward-filling demand (an event series) would invent sales. Imputation choices feed straight into inventory parameters, see [[003 Inventory Management]].

### In the news
See news box. With Copy-on-Write in pandas 3.0, `lt["lead_days"].fillna(...)` always returns a new Series; assign the result (as above) instead of relying on `inplace=True`.

### Interview angle
> [!question] How it is asked
> "Which imputation method would you use for missing prices and why?"

> [!tip] Strong answer includes
> - Choice by mechanism and variable type (numeric skew, categorical, time series)
> - Group-wise imputation and missing indicators
> - Fitting imputers on training data only; assessing impact by comparing results with and without imputation
> - Stating how much was imputed in any deliverable

---
## 9. Outliers: IQR, Z-Score & MAD
> 🟠 Tier 2 · _Key points:_ Tukey fences, 3-sigma and its small-n limit, modified z with MAD, domain rules, treat vs delete

### Definition
- **IQR (Tukey) rule**: flag values below $Q_1-1.5\,IQR$ or above $Q_3+1.5\,IQR$ (use 3 for "far out"). Robust, no normality assumption.
- **Z-score**: $z=(x-\bar x)/s$, flag $|z|>3$. Sensitive because outliers inflate $\bar x$ and $s$ (masking). For a sample of size $n$ the largest possible $|z|$ is $(n-1)/\sqrt n$, so with $n=8$ no value can ever exceed 2.47.
- **Modified z-score (MAD)**: $M=0.6745\,(x-\tilde x)/\text{MAD}$ with $\text{MAD}=\text{median}|x-\tilde x|$; flag $|M|>3.5$ (Iglewicz and Hoaglin). Robust to the outliers themselves.
- **Domain rules**: physical or commercial limits (qty above 20 times the typical order, negative price) that beat any statistic. Compute statistical rules **within a group** (per material), because 12,000 bolts is normal and 12,000 bearings is not.
- **Treatment**: investigate, then correct (typo), cap (winsorise), transform (log), model separately, or exclude with a documented reason. Do not delete silently; outliers may be the signal (a demand spike, a fraud case).

```python
qty = pd.Series([1200, 500, 2000, 12000, 150, 120000, 2500, 800], name="qty", dtype=float)

q1, q3 = qty.quantile([0.25, 0.75])
iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
z = (qty - qty.mean()) / qty.std(ddof=1)
med = qty.median()
mad = (qty - med).abs().median()
mod_z = 0.6745 * (qty - med) / mad                      # modified z-score (Iglewicz-Hoaglin), flag |M| > 3.5
print(f"Q1={q1:.0f} Q3={q3:.0f} IQR={iqr:.0f} fences=({lo:.0f}, {hi:.0f})  median={med:.0f} MAD={mad:.0f}")
res = pd.DataFrame({"qty": qty, "iqr_flag": (qty < lo) | (qty > hi), "z": z.round(2), "z_flag": z.abs() > 3,
                    "mod_z": mod_z.round(1), "mad_flag": mod_z.abs() > 3.5})
print(res.to_string())
assert res["iqr_flag"].sum() == 2 and res["mad_flag"].sum() == 2 and res["z_flag"].sum() == 0
# With n = 8 the largest possible |z| is (n-1)/sqrt(n) = 2.47, so the 3-sigma rule can never fire
assert round((len(qty) - 1) / len(qty) ** 0.5, 2) == 2.47 and z.abs().max() < 2.47

# Treatments: cap (winsorise) at the fences, or flag and send to review; do not silently delete
capped = qty.clip(lower=max(lo, 0), upper=hi)
print(capped.tolist())
# Domain rule beats statistics: an oil seal is never ordered in lakhs
rule_flag = qty > 20 * med
assert rule_flag.sum() == 1 and qty[rule_flag].iloc[0] == 120000
```
Output: Q1 = 725, Q3 = 4,875, IQR = 4,150, fences (-5,500, 11,100); median 1,600, MAD 1,000. IQR and MAD both flag 12,000 and 120,000 (modified z 7.0 and 79.9); the 3-sigma rule flags nothing, because the 120,000 value pulls the mean and standard deviation up and its z is only 2.46. Capping at the upper fence turns both into 11,100.

### Example
The 120,000 is the oil-seal typo (1,20,000 for 1,200), costing ₹48.7 lakh of phantom spend (4,920,000 versus 49,200); the 12,000 is a legitimate bolt order that the statistics also flag. This is why flags go to **review** rather than deletion, and why a within-material comparison or a domain rule is better than one global threshold. Statistical background is in [[086 Descriptive Statistics]].

### In the news
See news box. The pandas 3.0 `quantile` and `clip` behave as before; the change that matters here is that filtering and capping return new objects, so assign the result.

### Interview angle
> [!question] How it is asked
> "How do you detect and handle outliers in order quantities?"

> [!tip] Strong answer includes
> - IQR and MAD for robustness; why plain z-scores mask outliers and cannot flag at small n
> - Group-wise thresholds and domain rules
> - Decide per case: correct, cap, transform, separate model, or exclude with documentation
> - Check whether the outlier is an error or a real event before touching it

---
## 10. Validation: Assertions & Pandera Schemas
> 🟠 Tier 2 · _Key points:_ fail fast, schema as contract, lazy validation, reject file

### Definition
Validation turns assumptions into executable checks. Levels: (1) **assertions** inside the script for invariants that must never break; (2) a **schema** (pandera or Great Expectations) declaring types, nullability, ranges, allowed sets, uniqueness; (3) **reconciliation** to control totals from the source. Validate at the boundaries: right after load, and right before publishing. `lazy=True` in pandera reports all failures at once, so one run produces a full defect list. Decide per rule whether a failure **stops the pipeline**, **quarantines rows** to a rejects file or **warns**.

```python
import pandera.pandas as pa

clean = df.drop_duplicates(keep="first").reset_index(drop=True)

# 1. Plain assertions: cheap, explicit, fail fast
assert clean["PO_No"].str.len().eq(7).all(), "PO number must be 7 digits"
assert clean["Material"].str.len().eq(15).all(), "material number must keep its 15-character SAP form"
assert clean.filter(["PO_No", "Item"]).duplicated().sum() == 0, "PO/item must be unique"

# 2. A schema with business rules; lazy=True reports every failure, not only the first
schema = pa.DataFrameSchema(
    {
        "Material": pa.Column(str, pa.Check.str_matches(r"^\d{15}$")),
        "Qty": pa.Column(float, pa.Check.gt(0), nullable=False),
        "Net_Price": pa.Column(float, pa.Check.gt(0), nullable=False),
        "UoM": pa.Column(str, pa.Check.isin(["EA", "KG"])),
        "Order_Date": pa.Column("datetime64[us]", nullable=False,
                                checks=pa.Check.ge(pd.Timestamp("2026-01-01"))),
    },
    unique=["PO_No", "Item"],
    coerce=False,
)
try:
    schema.validate(clean, lazy=True)
except pa.errors.SchemaErrors as err:
    fc = err.failure_cases.filter(["column", "check", "failure_case"])
    print(fc.to_string(index=False))
    assert set(fc["column"]) == {"Qty", "Net_Price", "Order_Date"}
```
Output (pandera 0.33.1, pandas 3.0.6): four failure cases: `Qty` not nullable (NaN) and `Qty` not greater than 0 (-950.0); `Net_Price` not nullable (NaN); `Order_Date` not nullable (NaT). The material format, UoM set and key-uniqueness rules pass. Note the schema checks the outlier-free structure but not the 1,20,000 quantity: that is a plausibility rule to add (for example `Check.le(50_000)` per material).

### Example
The schema catches the return line (-950 kg), the line with missing quantity, price and date, and nothing else; the `uom_mismatch` rule from sub-topic 5 catches the bearing in kilograms. Together these three defects form the **rejects** file sent back to the buyer, while the other rows proceed. The principle is the same as an ERP input check: stop bad data at the door. Master-data governance context is in [[175 Data Quality, Master Data & Data Governance]].

### In the news
See news box. In pandera 0.33.1 the pandas API lives under `pandera.pandas`; code written against the old top-level import will warn. Pin versions in `requirements.txt` as discussed in [[184 Python OOP, Modules & Project Structure]].

### Interview angle
> [!question] How it is asked
> "How would you make sure bad data never reaches the dashboard?"

> [!tip] Strong answer includes
> - Layered checks: schema on load, business rules, reconciliation to control totals
> - Fail, quarantine or warn decided per rule, with an owner for each reject
> - Automated tests in the pipeline and alerts on failure
> - Tools by name (pandera, Great Expectations, dbt tests, SQL constraints) with a concrete rule

---
## 11. Profiling Tools
> 🟠 Tier 2 · _Key points:_ one-line profile reports, what they show, when not to trust them

### Definition
Profiling libraries generate a full EDA report in one call: per-column type, missing, distinct, distribution, correlations, duplicates and alerts (high cardinality, constant column, skew, high correlation). Options: **fg-data-profiling** (formerly ydata-profiling and pandas-profiling; HTML or JSON output, `minimal=True` for large frames), Sweetviz, `df.describe(include="all")`, SQL profiling queries, and the built-in profilers of Power BI Power Query (column quality, distribution, profile). Use a profile report to **start** the investigation and to give stakeholders a shareable snapshot; do not treat its alerts as the cleaning plan. It cannot know your business rules.

```python
# pip install fg-data-profiling   (the project formerly published as ydata-profiling / pandas-profiling)
from data_profiling import ProfileReport

report = ProfileReport(clean, title="PO lines - after type and text fixes", minimal=True)     # minimal=True skips heavy correlations
report.to_file("po_profile.html")                                          # shareable HTML
```
The call ran with fg-data-profiling 4.20.0 on pandas 3.0.6 and wrote a self-contained HTML report (about 1.3 MB, because the assets are embedded). With the old package the import is `from ydata_profiling import ProfileReport`.

### Example
On the PO extract a profile would show `Qty` with a minimum of -950 and a maximum of 120,000 (an extreme range), `Net_Price` with one missing value, `Material` with 5 distinct values over 10 rows, and a duplicate-row count of 0 after de-duplication. It would not know that a bearing priced per kilogram is wrong or that 120,000 oil seals is a typo; the domain rules do that. Use the report in the hand-over to the data owner.

### In the news
See news box. The rename means code and notebooks that `pip install ydata-profiling` will keep working only until the old package ages out; new work should use the new name, and on Python 3.15 the package's stated upper bound (below 3.15) means a Python 3.14 environment for now.

### Interview angle
> [!question] How it is asked
> "Is there a quick way to get a first look at a new dataset?"

> [!tip] Strong answer includes
> - Names a profiling tool and what it reports (missing, distinct, distributions, correlations, alerts)
> - Limits: large data (use `minimal=True`, sampling), no business rules, privacy of sensitive columns in a shared HTML
> - Combines it with `describe`, `value_counts` and domain checks
> - Reads dtype and cardinality alerts as prompts for questions to the data owner

---
## 12. Reproducible Cleaning Pipeline
> 🟠 Tier 2 · _Key points:_ one pure function, counts in/out, rejects file, tests, logging

### Definition
A cleaning script is a **product**: raw data in, clean data plus rejects plus a report out, and the same input always gives the same output. Principles: never edit the raw file; one function per step (or `df.pipe(step)`); no hidden state; parameters (formats, maps, thresholds) in one place; **row accounting** (rows in = duplicates + clean + rejected); log counts at each step; write rejects with a reason column; keep unit tests on small fixtures and a validation step at the end; run from a scheduler with alerting. Packaging and tests follow [[184 Python OOP, Modules & Project Structure]].

```python
import logging, re
from datetime import datetime
import numpy as np
import pandas as pd

log = logging.getLogger("erp_clean")
MISSING = {"", "-", "N/A", "NA", "n/a", "NULL", "None", "#N/A", "?"}
UOM_MAP = {"EA": "EA", "EACH": "EA", "PC": "EA", "PCS": "EA", "NOS": "EA", "KG": "KG", "KGS": "KG"}
DATE_FORMATS = ("%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y", "%Y%m%d", "%d-%b-%y")

def num(x):
    s = str(x).strip()
    if s in MISSING:
        return np.nan
    neg = s.endswith("-") or (s.startswith("(") and s.endswith(")"))
    v = float(re.sub(r"[^\d.]", "", s))
    return -v if neg else v

def date(x):
    s = str(x).strip()
    for fmt in DATE_FORMATS:
        try:
            return pd.Timestamp(datetime.strptime(s, fmt))
        except ValueError:
            pass
    return pd.NaT

def vendor(s):
    t = s.str.normalize("NFKC").str.replace(r"\s+", " ", regex=True).str.strip().str.lower()
    t = t.str.replace(r"[.,]", "", regex=True).str.replace(r"\b(limited|ltd)$", "", regex=True)
    return t.str.strip().str.title()

def clean_erp(raw: pd.DataFrame):
    """Return (clean, rejects, counts). Pure function: same input gives same output."""
    counts = {"rows_in": len(raw)}
    df = raw.copy()
    df["Qty"], df["Net_Price"] = df["Qty"].map(num), df["Net_Price"].map(num)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"].map(date))
    df["Vendor"] = vendor(df["Vendor"])
    df["Description"] = df["Description"].str.replace(r"\s+", " ", regex=True).str.strip()
    df["UoM"] = df["UoM"].str.strip().str.upper().map(UOM_MAP)
    df["Status"] = df["Status"].str.strip().str.upper()
    df["Material"] = df["Material"].str.strip()
    before = len(df)
    df = df.drop_duplicates()
    counts["exact_duplicates_removed"] = before - len(df)

    bad_uom = df["UoM"] != df["Material"].map(df.groupby("Material")["UoM"].agg(lambda s: s.mode().iat[0]))
    rules = {
        "qty_missing_or_nonpositive": ~(df["Qty"] > 0),
        "price_missing": df["Net_Price"].isna(),
        "date_missing": df["Order_Date"].isna(),
        "uom_conflicts_with_material": bad_uom,
    }
    reasons = pd.DataFrame(rules).apply(lambda r: ";".join(k for k, v in r.items() if v), axis=1)
    rejects = df.loc[reasons != ""].assign(reject_reason=reasons[reasons != ""])
    good = df.loc[reasons == ""].reset_index(drop=True)
    good["qty_review"] = good["Qty"] > 10 * good["Qty"].median()      # flag for a human, do not delete
    counts.update(rows_clean=len(good), rows_rejected=len(rejects))
    assert counts["rows_in"] == counts["exact_duplicates_removed"] + counts["rows_clean"] + counts["rows_rejected"]
    log.info("cleaning counts: %s", counts)
    return good, rejects, counts

good, rejects, counts = clean_erp(raw)
print(counts)
print(rejects.filter(["PO_No", "Item", "reject_reason"]).to_string(index=False))
assert counts == {"rows_in": 11, "exact_duplicates_removed": 1, "rows_clean": 7, "rows_rejected": 3}
good["Net_Value"] = good["Qty"] * good["Net_Price"]
print(good.filter(["PO_No", "Vendor", "Qty", "Net_Price", "Net_Value", "qty_review"]).to_string(index=False))
print("clean spend (Rs):", good["Net_Value"].sum())
# Reproducibility: the same input always gives the same output
again = clean_erp(raw)[0]
assert again.equals(good.drop(columns="Net_Value"))
# Effect of the one typo: 1,20,000 instead of 1,200 oil seals
fixed_spend = good["Net_Value"].sum() - 4_920_000 + 1_200 * 41.0
print("spend if the quantity were 1,200:", fixed_spend)
assert fixed_spend == 1_262_525.0
```
Output: counts `{'rows_in': 11, 'exact_duplicates_removed': 1, 'rows_clean': 7, 'rows_rejected': 3}`; rejects: PO 4500005 item 20 (return, non-positive quantity), PO 4500006 item 10 (quantity, price and date all missing) and PO 4500007 item 10 (UoM conflict). The seven clean lines have net values ₹3,00,000, ₹20,250, ₹4,96,000, ₹39,000, ₹1,87,575, ₹49,20,000 (flagged `qty_review`) and ₹1,70,500, totalling ₹61,33,325. If the 120,000 were the intended 1,200, spend would be ₹12,62,525.

### Example
The single typo drives 80% of the spend (49.2 lakh of 61.3 lakh). A pipeline that silently loaded the file would have produced a spend report with one supplier, Bharat Forge, looking dominant. The row accounting line (11 = 1 + 7 + 3) and the review flag are what make the output trustworthy. Returns (PO 4500005 item 20) were rejected here only because the rule requires positive quantities; in production route returns to their own table instead of rejecting them.

### In the news
See news box. pandas 3.0's Copy-on-Write makes the "copy at the start, return a new frame" style used above the standard pattern, and the `str` dtype plus pandera schemas make type drift between monthly extracts visible.

### Interview angle
> [!question] How it is asked
> "You clean the same export every month. How do you make the process repeatable and trustworthy?"

> [!tip] Strong answer includes
> - Scripted, versioned, parameterised pipeline; raw data never edited
> - Row and value accounting, rejects with reasons, logging, unit tests
> - Validation gate and alerting; documented assumptions and owner sign-off
> - Handover and schedule (Power Query for simple cases, Python for rule-heavy ones); compare with [[075 Pivot Tables & Power Query]]

---
## 13. ⭐ Advanced: Control Totals, Reconciliation & Audit Trail
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A cleaned dataset is only trusted if it **reconciles** to the source. Reconciliation compares row counts and money or quantity totals between stages: source system report, raw extract, cleaned table, rejects, published dashboard. Keep an **audit trail**: the raw file hash and extract timestamp, the code version, parameters, row counts per step, the rejects file, and who approved overrides. In regulated settings (pharma, finance, customs) this is a compliance need; elsewhere it is what lets you answer "why does your number differ from SAP?" in one minute.

```python
# Control totals: every rupee and every row in the raw export must be accounted for
parsed = raw.assign(Qty=raw["Qty"].map(num),
                    Net_Price=raw["Net_Price"].map(num))
raw_value = (parsed["Qty"] * parsed["Net_Price"]).sum()                       # NaN rows add nothing
dup_value = (parsed[parsed.duplicated()]["Qty"] * parsed[parsed.duplicated()]["Net_Price"]).sum()
rej_value = (rejects["Qty"] * rejects["Net_Price"]).sum()
good_value = good["Net_Value"].sum()
print(raw_value, dup_value, rej_value, good_value)
assert raw_value == dup_value + rej_value + good_value                        # raw = duplicates + rejects + clean
assert counts["rows_in"] == counts["exact_duplicates_removed"] + counts["rows_clean"] + counts["rows_rejected"]
```
Output: raw value ₹63,04,735 = duplicates ₹39,000 + rejects ₹1,32,410 (the return at -₹64,790 and the UoM-conflict bearing line at ₹1,97,200) + clean ₹61,33,325.

### Example
If a reviewer asks why spend is ₹61.3 lakh when the raw file implies ₹63.0 lakh, the reconciliation answers it line by line: ₹0.39 lakh of duplicate bolts, ₹1.32 lakh of rejected lines (to be corrected by the buyer and reloaded), the rest accepted. Save that table with the report. Add a hash of the raw file and the git commit of the script, and the number becomes reproducible. Related spend analytics are in [[122 Spend Analysis, Savings & Procurement Maturity]]; other tools for the same job are in [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]].

### In the news
See news box. Because pandera and profiling packages release frequently (September 2026 versions above), record library versions in the audit trail so a re-run in a year gives the same result.

### Interview angle
> [!question] How it is asked
> "The dashboard total does not match the ERP report. How do you find the gap?"

> [!tip] Strong answer includes
> - Reconcile stage by stage (source, extract, cleaned, rejected, published) using counts and value totals
> - Typical causes: duplicates, filters (date, plant, status), currency/UoM, cancelled or reversed documents, timing cut-off
> - Stored rejects and audit trail that make the gap explainable
> - Agreeing the definition of the number with the business before investigating
