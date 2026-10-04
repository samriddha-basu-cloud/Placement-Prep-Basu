---
tags: [python-programming, tier3]
area: Python Programming
topic: "Python OOP, Modules & Project Structure"
tier: Tier 3
roles: Analytics / Operations
status: complete
subtopics: 14
---
# Python OOP, Modules & Project Structure

⬅ [[069 Python for Product Analytics]] · [[_Index - Python Programming|Python Programming]] · [[185 Python Interview Problem Bank]] ➡

> **Area:** Python Programming · **Priority:** 🟡 Tier 3 · **Target roles:** Analytics / Operations

## Sub-topics in this note
1. [[#1. Classes, Objects & __init__]]
2. [[#2. Dunder (Magic) Methods]]
3. [[#3. Inheritance, super() & MRO]]
4. [[#4. Composition vs Inheritance]]
5. [[#5. Properties, @classmethod & @staticmethod]]
6. [[#6. Dataclasses]]
7. [[#7. Modules, Packages & Imports]]
8. [[#8. Virtual Environments, Requirements & Dependencies]]
9. [[#9. Type Hints]]
10. [[#10. Logging]]
11. [[#11. Unit Testing with pytest]]
12. [[#12. Project Layout for an Ops Analytics Tool]]
13. [[#13. Worked Example: Inventory & Order Classes]]
14. [[#14. ⭐ Advanced: ABCs, Protocols, Decorators & Context Managers]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Python moves fast, so tooling and typing habits matter
> **Python 3.14 (released 7 October 2025).** The release made deferred evaluation of annotations the default (PEP 649/749), so forward references in type hints no longer need string quotes; made free-threaded CPython an officially supported build (PEP 779, single-thread penalty about 5-10%); and added template string literals (`t"..."`, PEP 750). ([What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html))
>
> **Python 3.15 release candidate (2 October 2026).** python.org lists 3.15.0rc3 as the third and final release candidate, with the final release scheduled for 9 October 2026 after a one-week delay for last-minute lazy-import blockers. Headline features include explicit lazy imports (PEP 810), UTF-8 as the default text encoding, new `frozendict` and `sentinel` built-ins, and a faster experimental JIT. Checked 4 October 2026; confirm the final date on python.org. ([python.org](https://www.python.org/downloads/latest/python3.15/))
>
> **uv and pytest.** The uv documentation describes it as a Rust-written package and project manager that replaces pip, pip-tools, pipx, poetry, pyenv and virtualenv, claims "10-100x" speed over pip, and provides `uv init`, `uv add`, `uv lock`, `uv sync` and `uv run` with a universal lockfile ([uv docs](https://docs.astral.sh/uv/)). pytest 9.1.1 was released on 19 June 2026 and supports Python 3.10 and newer ([PyPI](https://pypi.org/project/pytest/)).
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Classes, Objects & __init__
> 🟡 Tier 3 · _Key points:_ class vs instance attributes, self, constructor, mutable-default trap

### Definition
A **class** is a blueprint; an **object** (instance) is one concrete thing built from it. `__init__` runs right after the object is created and sets its **instance attributes**. A **class attribute** is defined in the class body and shared by all instances. Methods receive the instance as `self` (a convention, not a keyword). Basic syntax is in [[062 Python Fundamentals]]; this note is about structuring real tools.

```python
class Warehouse:
    count = 0                                   # class attribute, shared
    def __init__(self, code, capacity):
        self.code = code                        # instance attributes
        self.capacity = capacity
        self.stock = {}
        Warehouse.count += 1
    def utilisation(self):
        return sum(self.stock.values()) / self.capacity

w = Warehouse("NSK-01", 1000); w.stock["A"] = 250; w.stock["B"] = 150
print(w.utilisation(), Warehouse.count)

class Bad:
    def __init__(self, items=[]):               # one list, created once at def time
        self.items = items
a, b = Bad(), Bad()
a.items.append("x")
print(b.items)
class Good:
    def __init__(self, items=None):
        self.items = [] if items is None else list(items)
```
Output: `0.4 1` then `['x']`. The second line is the classic bug: default argument values are evaluated once, when `def` runs, so every `Bad()` shares the same list.

### Example
A Nashik warehouse with capacity 1,000 pallets holding 250 + 150 = 400 reports utilisation 0.4. Rule of thumb for interviews: data that differs per object goes in `__init__`; constants shared by all objects go on the class; never use a mutable default.

### In the news
See news box. Python 3.14's deferred annotations mean a method can annotate its return as its own class (`def clone(self) -> Warehouse`) without quotes.

### Interview angle
> [!question] How it is asked
> "What is the difference between a class attribute and an instance attribute? What happens if you use a list as a default argument?"

> [!tip] Strong answer includes
> - Class attribute is shared; instance attribute is per object; assignment through an instance creates a new instance attribute
> - Defaults are evaluated once at definition, hence `None` plus create inside
> - `self` is the instance passed automatically; `__init__` initialises, it does not allocate (`__new__` does)
> - A concrete ops example (Warehouse, Item, Order)

---
## 2. Dunder (Magic) Methods
> 🟡 Tier 3 · _Key points:_ `__repr__` vs `__str__`, `__eq__`/`__hash__`, ordering, container protocol

### Definition
**Dunder** methods (double underscore) let your class plug into Python syntax. `__repr__` is the unambiguous developer string (shown in the REPL, logs); `__str__` is the friendly one used by `print`. `__eq__`, `__lt__` give comparison (`functools.total_ordering` derives the rest); defining `__eq__` without `__hash__` makes instances unhashable. `__len__`, `__iter__`, `__getitem__`, `__contains__` make a class behave like a container; `__add__` overloads `+`.

```python
from functools import total_ordering

@total_ordering
class Rupees:
    def __init__(self, paise: int):
        self.paise = paise
    def __repr__(self):  return f"Rupees({self.paise})"
    def __str__(self):   return f"Rs {self.paise / 100:,.2f}"
    def __eq__(self, o): return self.paise == o.paise
    def __lt__(self, o): return self.paise < o.paise
    def __add__(self, o): return Rupees(self.paise + o.paise)
    def __hash__(self):  return hash(self.paise)

a, b = Rupees(10), Rupees(20)
print(a + b == Rupees(30), 0.1 + 0.2 == 0.3)
print(str(Rupees(123456789)), repr(a), a < b, max(a, b))

class Pallet:
    def __init__(self, cases): self.cases = list(cases)
    def __len__(self): return len(self.cases)
    def __iter__(self): return iter(self.cases)
    def __getitem__(self, i): return self.cases[i]
    def __contains__(self, x): return x in self.cases
p = Pallet(["A", "B", "C"])
print(len(p), "B" in p, p[-1], sorted(p, reverse=True))
```
Output: `True False`, then `Rs 1,234,567.89 Rupees(10) True Rs 0.20`, then `3 True C ['C', 'B', 'A']`.

### Example
Money stored as integer paise avoids float error: `0.1 + 0.2 == 0.3` is `False` in floating point, while 10 paise + 20 paise equals 30 paise exactly. `Rs 12,34,567.89` in Indian lakh grouping needs a custom formatter; the `,` format code groups in thousands (`1,234,567.89`).

### In the news
See news box. pytest 9.x compares objects through `__eq__`, and its assertion diff prints `__repr__`, so a good `__repr__` makes failing tests readable.

### Interview angle
> [!question] How it is asked
> "Difference between `__str__` and `__repr__`? What must you define so objects can be dict keys?"

> [!tip] Strong answer includes
> - `repr` for developers (ideally evaluable), `str` for users; `str` falls back to `repr`
> - `__eq__` plus `__hash__` together; equal objects must hash equal; mutable objects should not be hashable
> - Container protocol via `__len__`/`__iter__`/`__getitem__`
> - Why money and quantities should use integers or `Decimal`, not float

---
## 3. Inheritance, super() & MRO
> 🟡 Tier 3 · _Key points:_ is-a, override, super(), method resolution order, polymorphism

### Definition
**Inheritance** lets a subclass reuse and specialise a parent (**is-a** relationship). The subclass **overrides** methods to change behaviour and calls `super()` to extend the parent version instead of copying it. Calling the same method on different subclasses and getting different behaviour is **polymorphism**. With multiple inheritance Python resolves attribute lookups along the **MRO** (C3 linearisation), visible in `Class.__mro__`.

```python
class Supplier:
    def __init__(self, name, lead_days):
        self.name, self.lead_days = name, lead_days
    def expected_lead_time(self):
        return self.lead_days

class ImportSupplier(Supplier):
    def __init__(self, name, lead_days, customs_days):
        super().__init__(name, lead_days)
        self.customs_days = customs_days
    def expected_lead_time(self):                # override
        return super().expected_lead_time() + self.customs_days

for s in (Supplier("Pune Castings", 5), ImportSupplier("Shenzhen Sensors", 21, 6)):
    print(s.name, s.expected_lead_time())        # polymorphism
class A:  pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print([k.__name__ for k in D.__mro__])
print(isinstance(ImportSupplier("x", 1, 1), Supplier))
```
Output: `Pune Castings 5`, `Shenzhen Sensors 27` (21 + 6), `['D', 'B', 'C', 'A', 'object']`, `True`.

### Example
A domestic supplier quotes 5 days; an import supplier quotes 21 days plus 6 days customs clearance = 27 days. Code that plans reorder points only calls `expected_lead_time()` and works for both. In the diamond `D(B, C)`, Python visits D, B, C, A: each class once, children before parents.

### In the news
See news box. Free-threaded Python (PEP 779) makes shared mutable class state a concurrency risk, one more reason to keep class hierarchies shallow and state per-instance.

### Interview angle
> [!question] How it is asked
> "Explain `super()` and the MRO. When would you avoid inheritance?"

> [!tip] Strong answer includes
> - Override vs extend (`super()`); `isinstance` for is-a checks
> - MRO order from `__mro__`; each class appears once
> - Warning that deep hierarchies and multiple inheritance are fragile; prefer composition (next sub-topic)
> - A one-line example such as `ImportSupplier(Supplier)`

---
## 4. Composition vs Inheritance
> 🟡 Tier 3 · _Key points:_ has-a, dependency injection, strategy pattern, "favour composition"

### Definition
**Composition** builds a class from other objects it **has** (an `Inventory` has `Item`s, an `Order` has `OrderLine`s). **Inheritance** says it **is** one. Prefer composition when behaviour varies independently: pass the varying part in as an object (**dependency injection**, the **strategy** pattern) rather than creating subclasses for each combination (`EOQPlannerWithSafetyStock...`). Test: if you cannot say "X is a kind of Y" truthfully in every context, use composition.

```python
class FixedQty:
    def __init__(self, qty): self.qty = qty
    def order_qty(self, annual_demand): return self.qty

class EOQPolicy:
    def __init__(self, order_cost, holding_cost):
        self.s, self.h = order_cost, holding_cost
    def order_qty(self, annual_demand):
        return round((2 * annual_demand * self.s / self.h) ** 0.5)

class Planner:
    def __init__(self, policy):                   # has-a policy, injected
        self.policy = policy
    def plan(self, annual_demand):
        q = self.policy.order_qty(annual_demand)
        return q, round(annual_demand / q, 1)

print(Planner(FixedQty(1000)).plan(12000))
print(Planner(EOQPolicy(500, 50)).plan(12000))
```
Output: `(1000, 12.0)` and `(490, 24.5)`.

### Example
Demand 12,000 units/year, order cost ₹500, holding cost ₹50/unit/year. Fixed lots of 1,000 mean 12 orders a year; the EOQ policy gives $Q^*=\sqrt{2\cdot12000\cdot500/50}=\sqrt{240000}\approx490$, so 24.5 orders. Total cost at 1,000 is $12\cdot500+500\cdot50=₹31,000$; at 490 it is about ₹24,495, a saving of roughly 21%. Swapping policy required no subclass; see [[003 Inventory Management]] and [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]] for the policy theory.

### In the news
See news box. Because Python typing supports structural `Protocol`s, any object with `order_qty` can be injected without inheriting from a base class.

### Interview angle
> [!question] How it is asked
> "Inheritance or composition for a report generator that needs different export formats?"

> [!tip] Strong answer includes
> - Composition when variation is behavioural and combinable; inheritance for true is-a with shared invariants
> - Dependency injection makes tests easy (pass a fake)
> - Strategy pattern named, with the planner/policy example
> - Cost of inheritance: tight coupling, fragile base class

---
## 5. Properties, @classmethod & @staticmethod
> 🟡 Tier 3 · _Key points:_ computed attributes, validation, alternative constructors

### Definition
`@property` exposes a method as an attribute: use it for **derived values** (`holding_cost`) and **validated setters**, so callers keep writing `item.holding_rate = 0.2`. `@classmethod` receives the class (`cls`) and is the idiom for **alternative constructors** (`from_row`, `from_csv`). `@staticmethod` receives neither; it is a plain function namespaced in the class. Python has no true private members: a leading underscore (`_x`) signals "internal".

```python
class Item:
    def __init__(self, sku, unit_cost, holding_rate):
        self.sku = sku
        self.unit_cost = unit_cost
        self.holding_rate = holding_rate
    @property
    def holding_cost(self):                       # computed, read-only
        return self.unit_cost * self.holding_rate
    @property
    def holding_rate(self):
        return self._holding_rate
    @holding_rate.setter
    def holding_rate(self, v):                    # validated on every assignment
        if not 0 < v < 1:
            raise ValueError("holding_rate must be between 0 and 1")
        self._holding_rate = v
    @classmethod
    def from_row(cls, row):                       # alternative constructor
        return cls(row["sku"], float(row["unit_cost"]), float(row["holding_rate"]))
    @staticmethod
    def rupees(x):                                # no self or cls needed
        return f"Rs {x:,.0f}"

it = Item.from_row({"sku": "S1", "unit_cost": "250", "holding_rate": "0.2"})
print(it.holding_cost, Item.rupees(it.holding_cost))
try:
    it.holding_rate = 20
except ValueError as e:
    print(e)
```
Output: `50.0 Rs 50` and `holding_rate must be between 0 and 1`.

### Example
Row `{"unit_cost": "250", "holding_rate": "0.2"}` from a CSV arrives as strings; `from_row` converts once and the setter rejects `20` (someone typed 20 instead of 20%). Holding cost = 250 x 0.2 = ₹50 per unit per year, matching the inventory example later.

### In the news
See news box. Validation at the object boundary pairs with schema checks on whole tables, covered in [[186 Python Data Cleaning & EDA Playbook]].

### Interview angle
> [!question] How it is asked
> "What is the difference between `@staticmethod`, `@classmethod` and an instance method?"

> [!tip] Strong answer includes
> - First argument: instance, class, none
> - `classmethod` for factories that also work for subclasses
> - Property for computed or validated attributes without changing the calling syntax
> - Encapsulation by convention (`_name`), not enforcement

---
## 6. Dataclasses
> 🟡 Tier 3 · _Key points:_ `@dataclass`, frozen, slots, `field(default_factory)`, `__post_init__`

### Definition
`@dataclass` generates `__init__`, `__repr__` and `__eq__` from annotated fields. Options: `frozen=True` (immutable and hashable), `order=True` (comparison by field order), `slots=True` (less memory, no `__dict__`). Mutable defaults need `field(default_factory=list)`; Python refuses a bare `[]`. `__post_init__` runs after generated `__init__` for validation or derived fields; `asdict()` and `replace()` convert and copy. Compared with `namedtuple` (immutable tuple, no validation) and Pydantic (runtime validation and coercion, a third-party library), dataclasses are the standard-library default for plain records.

```python
from dataclasses import dataclass, field, asdict, replace

@dataclass(frozen=True, order=True, slots=True)
class Lane:
    origin: str
    dest: str
    km: int
    rate_per_km: float = 38.0

    def cost(self) -> float:
        return self.km * self.rate_per_km

@dataclass
class Shipment:
    ref: str
    lanes: list[Lane] = field(default_factory=list)
    def __post_init__(self):
        self.ref = self.ref.strip().upper()

l1 = Lane("Nashik", "Mumbai", 167)
print(l1, l1.cost())
print(replace(l1, rate_per_km=41.0).cost(), asdict(l1)["dest"])
print(sorted([Lane("Pune", "Goa", 450), l1])[0].origin)
try:
    l1.km = 1
except Exception as e:
    print(type(e).__name__)
s1, s2 = Shipment(" sh-1 "), Shipment("sh-2")
s1.lanes.append(l1)
print(s1.ref, s2.lanes)
try:
    @dataclass
    class Oops:
        xs: list = []
except ValueError as e:
    print("ValueError:", e)
```
Output: `Lane(origin='Nashik', dest='Mumbai', km=167, rate_per_km=38.0) 6346.0`, `6847.0 Mumbai`, `Nashik`, `FrozenInstanceError`, `SH-1 []`, then the ValueError about `default_factory`.

### Example
Nashik to Mumbai is 167 km at ₹38/km = ₹6,346; at ₹41/km the same lane costs 167 x 41 = ₹6,847. `replace()` produces the new lane without mutating the frozen original; `s2.lanes` stays empty because each Shipment got its own list from `default_factory`.

### In the news
See news box. Python 3.14's deferred annotations change how annotations are stored, but `dataclass` fields keep working; tools that read `__annotations__` directly should use `annotationlib.get_annotations()`.

### Interview angle
> [!question] How it is asked
> "Why use a dataclass instead of a dict or a plain class? What does `frozen=True` do?"

> [!tip] Strong answer includes
> - Less boilerplate, typed fields, readable repr, free equality
> - Frozen gives immutability and hashability (usable as dict key or set member)
> - `default_factory` for mutable defaults and why bare `[]` is rejected
> - Alternatives: namedtuple, TypedDict, Pydantic for external data validation

---
## 7. Modules, Packages & Imports
> 🟡 Tier 3 · _Key points:_ import system, `__init__.py`, absolute vs relative, `__main__`, circular imports

### Definition
A **module** is one `.py` file; a **package** is a folder of modules (with `__init__.py` for regular packages). `import x` binds the module; `from x import y` binds one name. Python searches `sys.modules` (cache), then `sys.path` (script folder, installed site-packages). Prefer **absolute imports** (`from invsim.models import Item`); use relative imports (`from .models import Item`) only inside a package. Code under `if __name__ == "__main__":` runs only when the file is executed, not when imported. Run package code with `python -m invsim.cli`, which keeps `sys.path` and relative imports right.

```python
import math
print(math.__name__, __name__)
if __name__ == "__main__":
    print("only when run as a script")
```
Output: `math __main__` then the guarded line (when run as a script).

**Circular imports** (`a` imports `b`, `b` imports `a`) fail with partially initialised modules. Fixes: move the shared class to a third module, import inside the function that needs it, or restructure so dependencies point one way (models <- services <- cli). Use `__all__` and the package `__init__.py` to define the public API; avoid `from x import *`.

### Example
In the `invsim` package below, `invsim/__init__.py` re-exports `Item`, `Order` and `Inventory`, so users write `from invsim import Inventory` while the code lives in `models.py` and `inventory.py`. `inventory.py` imports `models.py`, never the reverse: one-way dependency, no cycle.

### In the news
See news box. Python 3.15's explicit lazy imports (PEP 810, `lazy import json`) defer module loading until first use, which cuts start-up time of CLI tools with heavy imports such as pandas.

### Interview angle
> [!question] How it is asked
> "What does `if __name__ == '__main__'` do? How do you resolve a circular import?"

> [!tip] Strong answer includes
> - `__name__` equals `"__main__"` only for the entry script
> - Import caching in `sys.modules`; search order via `sys.path`
> - Absolute imports by default; relative only within a package
> - Breaking cycles by layering or moving shared code

---
## 8. Virtual Environments, Requirements & Dependencies
> 🟡 Tier 3 · _Key points:_ venv, pip freeze, pyproject.toml, lockfile, uv, reproducibility

### Definition
A **virtual environment** is an isolated folder with its own interpreter link and site-packages so each project has its own library versions. Never `pip install` into the system Python. **requirements.txt** lists dependencies for `pip install -r`; **pyproject.toml** is the modern standard for project metadata and dependency ranges; a **lockfile** pins the exact resolved versions (including transitive ones) for reproducible installs. Rule: ranges in `pyproject.toml` for libraries, exact pins in the lockfile for applications. Keep `.venv/` and data files out of git (`.gitignore`).

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install pandas pytest
pip freeze > requirements.txt        # exact versions of everything installed
pip install -r requirements.txt      # recreate elsewhere

# with uv (single tool: env + deps + lockfile)
uv init invsim && cd invsim
uv add pandas
uv add --dev pytest
uv sync                              # create/refresh .venv from the lockfile
uv run pytest                        # run inside the project environment
```
Example `requirements.txt` lines: `pandas==3.0.0`, `numpy>=2.0,<3`. The `==` pin is exact; `>=,<` is a compatible range; `~=2.3` means at least 2.3 and below 3.0.

### Example
A demand-planning notebook works on the analyst's laptop (pandas 2.2) but fails on the team server (pandas 3.0) because chained assignment such as `df["a"][mask] = 0` no longer works there. A committed lockfile or pinned `requirements.txt` makes both machines identical; the fix is also to rewrite the line with `.loc`. See [[064 Pandas — Data Manipulation]].

### In the news
See news box. uv's single-tool workflow (init, add, lock, sync, run) is why many new projects skip separate pip, pyenv and virtualenv steps.

### Interview angle
> [!question] How it is asked
> "A script runs on your machine but not your colleague's. What do you check and how do you prevent it?"

> [!tip] Strong answer includes
> - Python and library versions differ; use a venv per project
> - Pin versions (`requirements.txt` or lockfile) and commit it; record the Python version
> - Separate runtime and dev dependencies
> - Mention `pip freeze`, `pyproject.toml`, and a modern tool like uv or poetry

---
## 9. Type Hints
> 🟡 Tier 3 · _Key points:_ annotations are not enforced, `X | None`, TypedDict, Protocol, mypy

### Definition
**Type hints** annotate expected types (`def f(x: int) -> str`). Python **does not enforce them at run time**; tools such as `mypy`, `pyright` and IDEs check them statically and catch bugs before the code runs. Modern syntax: `list[int]`, `dict[str, float]`, `int | None` (rather than `Optional[int]`), `TypedDict` for dict-shaped rows, `Protocol` for structural ("duck") typing, `Callable`, `Literal`, `Final`. Start by hinting function signatures at module boundaries; do not chase 100% coverage.

```python
from typing import Protocol, TypedDict

def reorder_qty(demand: float, eoq: float, stock: float | None = None) -> int:
    on_hand = 0.0 if stock is None else stock
    return max(0, round(eoq - on_hand)) if demand > 0 else 0

print(reorder_qty(1200.0, 490.0, 100.0))

class Row(TypedDict):
    sku: str
    qty: int

def total(rows: list[Row]) -> int:
    return sum(r["qty"] for r in rows)

class HasLeadTime(Protocol):
    def expected_lead_time(self) -> int: ...

def slowest(suppliers: list[HasLeadTime]) -> int:
    return max(s.expected_lead_time() for s in suppliers)

def f(x: int) -> int:
    return x
print(f("not an int"))
print(total([{"sku": "A", "qty": 3}, {"sku": "B", "qty": 4}]), slowest([Supplier("a", 5), ImportSupplier("b", 21, 6)]))
```
Output: `390` (490 - 100), `not an int` (the hint was ignored at run time; `mypy` would flag the call), then `7 27`. `Supplier` and `ImportSupplier` come from sub-topic 3, and match `HasLeadTime` without inheriting from it.

### Example
Run `mypy src/` in CI: it reports `Argument 1 to "f" has incompatible type "str"; expected "int"` for the bad call above, and also flags a function that returns `None` on one path when the hint promises `int`.

### In the news
See news box. Python 3.14 evaluates annotations lazily (PEP 649/749), so a class can refer to a class defined later in the file without quotes; Python 3.15 adds typing features such as `TypedDict` with typed extra items and `TypeForm` (python.org summary of 3.15 rc3).

### Interview angle
> [!question] How it is asked
> "Are Python type hints enforced? Why use them?"

> [!tip] Strong answer includes
> - Not enforced at run time; checked by mypy/pyright, used by IDEs and libraries like Pydantic
> - Benefits: documentation, earlier bug detection, safer refactors
> - `X | None` for optional values and the need to handle `None`
> - `Protocol` and `TypedDict` for structural typing and dict rows

---
## 10. Logging
> 🟡 Tier 3 · _Key points:_ levels, getLogger(__name__), handlers, no print in libraries, `logger.exception`

### Definition
The `logging` module replaces `print` in anything that runs unattended. Levels: `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`; the default threshold is `WARNING`. Each module gets `logger = logging.getLogger(__name__)`, which forms a hierarchy (`invsim.inventory` is a child of `invsim`). **Libraries create loggers but never configure handlers**; the application's entry point calls `basicConfig` (or `dictConfig`) once. Use lazy formatting (`log.info("x %s", v)`) so strings are built only when the level is enabled, and `log.exception(...)` inside `except` to include the traceback.

```python
import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(name)s: %(message)s", force=True)
log = logging.getLogger("invsim.demo")
log.debug("not shown at INFO level")
log.info("loaded %d SKUs from %s", 3, "items.csv")
log.warning("SKU %s below reorder point (%.1f < %.1f)", "SKU-202", 40, 57.4)
try:
    1 / 0
except ZeroDivisionError:
    log.exception("zero demand")
```
Output: `INFO invsim.demo: loaded 3 SKUs from items.csv`, `WARNING invsim.demo: SKU SKU-202 below reorder point (40.0 < 57.4)`, then `ERROR invsim.demo: zero demand` followed by the traceback. The debug line is suppressed.

### Example
A nightly job that refreshes reorder alerts should log row counts in and out, number of SKUs flagged, and any rejected rows, writing to a rotating file (`logging.handlers.RotatingFileHandler`). When the planner asks "why was SKU-202 not flagged on Tuesday?", the log answers; a `print` to a closed terminal cannot.

### In the news
See news box. `pytest` captures log records with the built-in `caplog` fixture so tests can assert that a warning was emitted.

### Interview angle
> [!question] How it is asked
> "Why use logging instead of print? How do you configure it for a package?"

> [!tip] Strong answer includes
> - Levels, handlers, formatters, and per-module loggers
> - Libraries do not configure logging; the entry point does
> - Lazy `%s` arguments and `logger.exception` for tracebacks
> - Audit and debugging value for scheduled jobs; avoid logging sensitive data

---
## 11. Unit Testing with pytest
> 🟡 Tier 3 · _Key points:_ assert, fixtures, parametrize, raises, approx, tmp_path, capsys

### Definition
**pytest** discovers files named `test_*.py` and functions named `test_*`, and uses plain `assert` with rich failure output. Key features: **fixtures** (`@pytest.fixture`, shared setup, can live in `conftest.py`), **parametrize** (one test, many inputs), `pytest.raises` (expect an exception), `pytest.approx` (float comparison), built-in fixtures `tmp_path`, `monkeypatch`, `capsys`, `caplog`. Arrange-Act-Assert structure; one behaviour per test; test edge cases (zero, negative, empty, missing SKU). Run with `pytest -q`, a single test with `pytest -k eoq`, coverage with the `pytest-cov` plugin.

```python
import pytest

@pytest.mark.parametrize("sl, expected_ss", [(0.90, 20.34), (0.95, 26.11), (0.99, 36.93)])
def test_safety_stock(bearing, sl, expected_ss):
    assert bearing.safety_stock(sl) == pytest.approx(expected_ss, abs=0.01)

def test_issue_beyond_stock_raises(inv):
    with pytest.raises(InsufficientStock):
        inv.issue("SKU-202", 101)
```
The fixtures `bearing` and `inv` are defined in the full test files in sub-topic 13. Floating-point values must use `approx`: `assert 0.1 + 0.2 == 0.3` fails, `assert 0.1 + 0.2 == pytest.approx(0.3)` passes.

### Example
Safety stock for the bearing item (daily sigma 6, lead time 7 days) at service levels 90/95/99% is $z\cdot6\cdot\sqrt7$ = 20.34, 26.11, 36.93 units with $z$ = 1.2816, 1.6449, 2.3263. Parametrize checks all three in one test; if someone swaps `sqrt(lead_time)` for `lead_time` the test fails at once. See [[003 Inventory Management]] for the formula.

### In the news
See news box. pytest 9.1.1 (19 June 2026) supports Python 3.10 and newer, so the same test style works on any currently supported interpreter.

### Interview angle
> [!question] How it is asked
> "How do you test a function that reads a CSV and calculates reorder points?"

> [!tip] Strong answer includes
> - Separate pure calculation from I/O so the calculation is testable with literals
> - `tmp_path` for file tests, fixtures for shared setup, `parametrize` for edge-case tables
> - `approx` for floats, `raises` for expected errors
> - Testing the failure path (bad input, missing SKU) and running tests in CI

---
## 12. Project Layout for an Ops Analytics Tool
> 🟡 Tier 3 · _Key points:_ src layout, separation of I/O, domain and CLI, config, tests, README

### Definition
A maintainable analytics tool separates **data in/out** (CSV, SQL, Excel), **domain logic** (EOQ, reorder, ABC) and the **entry point** (CLI, scheduler, dashboard). The widely used **src layout** keeps the package under `src/` so tests run against the installed package, not the working folder. Typical layout:

```text
invsim/
├── pyproject.toml          # metadata, dependencies, pytest config
├── README.md               # what it does, how to run, sample output
├── .gitignore              # .venv/, __pycache__/, data/raw/
├── data/                   # sample inputs (small), never confidential extracts
│   ├── items.csv
│   └── stock.csv
├── src/invsim/
│   ├── __init__.py         # public API
│   ├── models.py           # dataclasses: Item, Order, OrderLine
│   ├── inventory.py        # Inventory class, business rules, logging
│   ├── cli.py              # argparse, loads CSVs, prints results
│   └── __main__.py         # enables: python -m invsim
└── tests/
    ├── conftest.py         # shared fixtures
    ├── test_models.py
    ├── test_inventory.py
    └── test_cli.py
```
Install in editable mode with `pip install -e .` (or `uv sync`), run with `python -m invsim data/items.csv data/stock.csv`, test with `pytest`. Rules: no hard-coded file paths or secrets in code (arguments or environment variables), no business logic in notebooks (import the package instead), one function does one thing, and log rather than print.

The CLI (`cli.py`, a short module) uses `argparse`, loads both CSVs with pandas, builds `Item` objects with `Item(**row)`, receives the stock and prints the reorder list. Output on the sample data:

```text
$ python -m invsim data/items.csv data/stock.csv
Reorder now: SKU-202
```

### Example
Sample stock: SKU-101 has 300 on hand against a reorder point of 256.2; SKU-202 has 40 against 57.4; SKU-303 has 95 against 78.3. Only SKU-202 is at or below its reorder point, so the tool prints `Reorder now: SKU-202`. A planner can schedule this command daily; a data engineer can swap the CSV loader for a SAP extract without touching `models.py`. For process-level data feeds see [[068 Operations-Specific Python (PuLP, SimPy)]] and [[046 Python for Operations]].

### In the news
See news box. uv gives a one-command setup (`uv sync`) for new colleagues, and Python 3.15's lazy imports can shorten the start-up of a CLI that imports pandas only for some sub-commands.

### Interview angle
> [!question] How it is asked
> "You built an analysis in a notebook. How would you turn it into something the planning team can run every week?"

> [!tip] Strong answer includes
> - Move logic into a package with functions/classes, keep the notebook as a thin caller
> - CLI or scheduled job, config via arguments, logging, tests, README
> - Version control, pinned dependencies, sample data, validation of inputs
> - Hand-over plan: owner, runbook, failure alerts

---
## 13. Worked Example: Inventory & Order Classes
> 🟡 Tier 3 · _Key points:_ dataclass Item with EOQ, ROP; Order composition; Inventory with exceptions; pytest suite

### Definition
Putting the pieces together: an immutable `Item` dataclass with derived properties, `Order`/`OrderLine` dataclasses (composition: an order has lines), and an `Inventory` class that owns the stock, raises a custom exception, logs, and ships orders atomically (check every line, then issue). The formulas are $EOQ=\sqrt{2DS/H}$ and $ROP=\bar d\,L+z\,\sigma_d\sqrt{L}$.

`src/invsim/models.py`
```python
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from math import sqrt
from statistics import NormalDist


@dataclass(frozen=True)
class Item:
    """One stocked SKU with the parameters needed for EOQ and reorder logic."""
    sku: str
    name: str
    unit_cost: float          # Rs per unit
    annual_demand: float      # units per year
    order_cost: float         # Rs per order placed
    holding_rate: float       # fraction of unit cost per year, e.g. 0.20
    lead_time_days: int
    daily_sigma: float = 0.0  # std dev of daily demand, units

    def __post_init__(self) -> None:
        if self.unit_cost <= 0 or self.annual_demand < 0:
            raise ValueError(f"{self.sku}: cost must be > 0 and demand >= 0")

    @property
    def holding_cost(self) -> float:
        return self.unit_cost * self.holding_rate

    @property
    def daily_demand(self) -> float:
        return self.annual_demand / 365

    @property
    def eoq(self) -> float:
        return sqrt(2 * self.annual_demand * self.order_cost / self.holding_cost)

    def safety_stock(self, service_level: float = 0.95) -> float:
        z = NormalDist().inv_cdf(service_level)
        return z * self.daily_sigma * sqrt(self.lead_time_days)

    def reorder_point(self, service_level: float = 0.95) -> float:
        return self.daily_demand * self.lead_time_days + self.safety_stock(service_level)


class OrderStatus(Enum):
    OPEN = "open"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class OrderLine:
    sku: str
    qty: int
    price: float

    @property
    def value(self) -> float:
        return self.qty * self.price


@dataclass
class Order:
    order_id: str
    customer: str
    lines: list[OrderLine] = field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    def add_line(self, sku: str, qty: int, price: float) -> None:
        if qty <= 0:
            raise ValueError("qty must be positive")
        self.lines.append(OrderLine(sku, qty, price))

    @property
    def total(self) -> float:
        return sum(line.value for line in self.lines)

    def __len__(self) -> int:
        return len(self.lines)

    def __iter__(self):
        return iter(self.lines)
```
`src/invsim/inventory.py`
```python
from __future__ import annotations

import logging
from collections import defaultdict

from invsim.models import Item, Order, OrderStatus

logger = logging.getLogger(__name__)


class InsufficientStock(Exception):
    """Raised when an issue would take stock below zero."""


class Inventory:
    def __init__(self, items: list[Item]) -> None:
        self._items = {it.sku: it for it in items}   # composition: Inventory HAS Items
        self._stock: dict[str, float] = defaultdict(float)

    def receive(self, sku: str, qty: float) -> None:
        self._require(sku)
        self._stock[sku] += qty
        logger.info("received %s x %s, on hand %s", sku, qty, self._stock[sku])

    def issue(self, sku: str, qty: float) -> None:
        self._require(sku)
        if qty > self._stock[sku]:
            logger.warning("short %s: want %s, have %s", sku, qty, self._stock[sku])
            raise InsufficientStock(f"{sku}: want {qty}, have {self._stock[sku]}")
        self._stock[sku] -= qty

    def on_hand(self, sku: str) -> float:
        return self._stock[sku]

    def ship(self, order: Order) -> None:
        # check every line first so a failed order leaves stock untouched
        for line in order:
            if line.qty > self._stock[line.sku]:
                raise InsufficientStock(f"{order.order_id}: {line.sku} short")
        for line in order:
            self.issue(line.sku, line.qty)
        order.status = OrderStatus.SHIPPED

    def to_reorder(self, service_level: float = 0.95) -> list[str]:
        return sorted(
            sku for sku, it in self._items.items()
            if self._stock[sku] <= it.reorder_point(service_level)
        )

    def _require(self, sku: str) -> None:
        if sku not in self._items:
            raise KeyError(f"unknown SKU {sku}")
```
`tests/test_inventory.py`
```python
import pytest

from invsim import Inventory, InsufficientStock, Item, Order, OrderStatus


@pytest.fixture
def inv() -> Inventory:
    items = [Item("SKU-101", "Bearing", 250, 12_000, 500, 0.20, 7, 6),
             Item("SKU-202", "Seal", 40, 3_650, 200, 0.25, 5, 2)]
    i = Inventory(items)
    i.receive("SKU-101", 300)
    i.receive("SKU-202", 100)
    return i


def test_issue_reduces_stock(inv):
    inv.issue("SKU-101", 120)
    assert inv.on_hand("SKU-101") == 180


def test_issue_beyond_stock_raises(inv):
    with pytest.raises(InsufficientStock):
        inv.issue("SKU-202", 101)


def test_failed_order_leaves_stock_untouched(inv):
    o = Order("SO-9", "Bajaj Auto")
    o.add_line("SKU-101", 50, 300)
    o.add_line("SKU-202", 500, 60)       # impossible line
    with pytest.raises(InsufficientStock):
        inv.ship(o)
    assert inv.on_hand("SKU-101") == 300 and o.status is OrderStatus.OPEN


def test_reorder_list(inv):
    # SKU-101 ROP = 12000/365*7 + 26.11 = 256.2; stock 300 -> fine
    assert inv.to_reorder() == []
    inv.issue("SKU-101", 100)
    assert inv.to_reorder() == ["SKU-101"]
```
The whole project (these files plus `cli.py`, `__main__.py`, `conftest.py`, `test_models.py` and `test_cli.py`) was run under `pytest`: 12 tests pass.

### Example
Item SKU-101: demand 12,000/year, order cost ₹500, unit cost ₹250, holding rate 20% so H = ₹50, lead time 7 days, daily sigma 6. EOQ = $\sqrt{2\cdot12000\cdot500/50}$ = 489.9 units (24.5 orders a year). Daily demand = 12,000/365 = 32.88; lead-time demand = 230.1; safety stock at 95% = 1.645 x 6 x $\sqrt7$ = 26.1; ROP = 256.2. Stock of 300 is fine; after issuing 100, stock is 200, below 256.2, so `to_reorder()` returns `["SKU-101"]`. A failed order (second line asks 500 seals but only 100 exist) raises `InsufficientStock` and leaves SKU-101 stock at 300 and the order status `OPEN`.

### In the news
See news box. Typed, tested, logged code like this is the kind of artefact that survives hand-over, unlike a one-off notebook.

### Interview angle
> [!question] How it is asked
> "Design classes for an order-to-ship process with stock checks. Walk me through them."

> [!tip] Strong answer includes
> - Entities (Item, Order, OrderLine), service (Inventory), exception for rule violations
> - Atomic operation: validate all lines before changing stock
> - Immutability for reference data, dataclasses for records, composition for has-a
> - Tests for the happy path, the failure path, and a parametrised numeric check

---
## 14. ⭐ Advanced: ABCs, Protocols, Decorators & Context Managers
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Abstract base class** (`abc.ABC` plus `@abstractmethod`): defines an interface that subclasses must implement; instantiating the base raises `TypeError`.
- **Protocol**: structural interface; any class with the right methods qualifies (see sub-topic 9).
- **Decorator**: a function that wraps another to add behaviour (timing, caching, retry, logging); use `functools.wraps` to keep the name and docstring.
- **Context manager** (`with`): guarantees set-up and clean-up (files, DB connections, timers); build one with `contextlib.contextmanager`.
- **Memoisation**: `functools.cache` stores results of pure functions.
- **`__slots__`**: fixed attribute set, no per-instance `__dict__`, saving memory for millions of small objects.

```python
from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import cache, wraps
import time

class Forecaster(ABC):
    @abstractmethod
    def predict(self, history: list[float]) -> float: ...

class MovingAverage(Forecaster):
    def __init__(self, n): self.n = n
    def predict(self, history): return sum(history[-self.n:]) / self.n

try:
    Forecaster()
except TypeError as e:
    print("TypeError:", e)
print(MovingAverage(3).predict([100, 120, 110, 130]))

def timed(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        t0 = time.perf_counter()
        out = fn(*a, **k)
        wrapper.last_seconds = time.perf_counter() - t0
        return out
    return wrapper

@timed
def slow_sum(n): return sum(range(n))
print(slow_sum(10**6), slow_sum.__name__, slow_sum.last_seconds < 5)

@contextmanager
def stage(name):
    print(f"start {name}")
    try:
        yield
    finally:
        print(f"end {name}")
with stage("load"):
    pass

@cache
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(80))

class Plain:
    def __init__(self): self.a = 1
class Slim:
    __slots__ = ("a",)
    def __init__(self): self.a = 1
print(hasattr(Plain(), "__dict__"), hasattr(Slim(), "__dict__"))
```
Output includes `TypeError: Can't instantiate abstract class Forecaster with abstract method predict` (exact wording varies slightly across versions), `120.0`, `499999500000 slow_sum True`, `start load` / `end load`, `23416728348467685`, and `True False`.

### Example
A moving-average forecaster over the last 3 periods of [100, 120, 110, 130] gives (120 + 110 + 130) / 3 = 120. A planning tool can accept any `Forecaster` (moving average, exponential smoothing, ARIMA wrapper from [[066 Demand Forecasting & Time Series]]) because they share `predict`. `fib(80)` returns instantly with `@cache`; the uncached recursive version would take astronomically long (exponential time). Decorators like `@timed` are how many ETL frameworks log step durations.

### In the news
See news box. Free-threaded Python (PEP 779) and multiple interpreters (PEP 734) make thread-safe design, immutable data and clean context-managed resources more important in 3.14+.

### Interview angle
> [!question] How it is asked
> "What is a decorator? Write one that times a function." or "ABC versus Protocol?"

> [!tip] Strong answer includes
> - Decorator is a function returning a wrapper; `functools.wraps` preserves metadata
> - Context manager guarantees clean-up even on exceptions
> - ABC enforces inheritance-based contracts; Protocol is structural and needs no inheritance
> - Memoisation only for pure functions with hashable arguments; mention memory growth (`lru_cache(maxsize=...)`)
> - Link to practice problems in [[185 Python Interview Problem Bank]] and testing style in [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]]
