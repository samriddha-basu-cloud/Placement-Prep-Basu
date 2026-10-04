---
tags: [reference]
---
# Formula Cheat Sheet

[[00 Home]]

| Area | Concept | Formula | Variables | When to use |
|---|---|---|---|---|
| Inventory | EOQ | `√(2DS/H)` | D=annual demand, S=order cost, H=holding cost/unit/yr | Optimal order qty |
| Inventory | Reorder Point (ROP) | `d̄ × LT + Safety Stock` | d̄=avg daily demand, LT=lead time in days | When to place order |
| Inventory | Safety Stock | `Z × σ_d × √LT` | Z=service level factor, σ_d=demand std dev | Buffer against variability |
| Inventory | Inventory Turnover | `COGS / Avg Inventory` | Higher = leaner operations | Efficiency benchmarking |
| Inventory | Days Inventory Outstanding | `Avg Inventory / (COGS/365)` | Lower DIO = faster cash cycle | Cash flow analysis |
| Inventory | Total Carrying Cost | `Q/2 × H` | Q=order qty, H=holding cost per unit per year | Cost optimization |
| Inventory | Total Ordering Cost | `(D/Q) × S` | Number of orders × cost per order | Cost optimization |
| Forecasting | Simple Moving Average | `ΣDemand(n periods) / n` | n = number of periods | Stable demand patterns |
| Forecasting | Exponential Smoothing | `Ft = α·At-1 + (1-α)·Ft-1` | α=smoothing constant (0-1), At-1=actual last period | Responsive forecasting |
| Forecasting | MAD | `Σ\|Actual - Forecast\| / n` | Mean Absolute Deviation; lower = better | Forecast accuracy |
| Forecasting | MAPE | `Σ\|(A-F)/A\| / n × 100%` | Mean Abs % Error; <10% = excellent | % accuracy measure |
| Forecasting | RMSE | `√(Σ(A-F)² / n)` | Penalizes large errors more heavily | When large errors are critical |
| Production | Takt Time | `Available time / Customer demand` | Sets production rhythm to match demand rate | Line balancing |
| Production | Cycle Time | `Total process time / Units produced` | Avg time per unit; compare to takt time | Bottleneck analysis |
| Production | Line Efficiency | `(Sum of task times) / (Workstations × Cycle time)` | Higher = better balanced line | Assembly line design |
| Production | Utilization | `Actual output / Design capacity` | As a %; high util = efficient but risky | Capacity planning |
| Production | Efficiency | `Actual output / Effective capacity` | Effective = design × availability | Performance measure |
| Quality | OEE | `Availability × Performance × Quality` | World class ≥ 85% | Overall equipment health |
| Quality | Availability | `(Planned - Downtime) / Planned time` | Uptime ratio; impacted by breakdowns | OEE component |
| Quality | Cp (Process Capability) | `(USL - LSL) / 6σ` | Cp ≥ 1.33 = capable process | Process spread vs spec |
| Quality | Cpk | `min[(USL-μ),(μ-LSL)] / 3σ` | Centering + spread; Cpk ≥ 1.33 ideal | Centered capability |
| Quality | DPMO | `(Defects / Opp × Units) × 1,000,000` | 3.4 DPMO at Six Sigma level | Sigma level calculation |
| Project Mgmt | PERT Estimate | `(O + 4M + P) / 6` | O=Optimistic, M=Most likely, P=Pessimistic | Activity duration estimation |
| Project Mgmt | PERT Variance | `((P - O) / 6)²` | Standard deviation = (P-O)/6 | Schedule uncertainty |
| Project Mgmt | Total Float | `LS - ES  or  LF - EF` | Zero float = critical activity | Critical path analysis |
| Project Mgmt | CPI (Cost Performance Index) | `EV / AC` | CPI > 1 = under budget; < 1 = over budget | Project cost health |
| Project Mgmt | SPI (Schedule Performance Index) | `EV / PV` | SPI > 1 = ahead; < 1 = behind schedule | Project schedule health |
| Project Mgmt | EAC (Estimate at Completion) | `BAC / CPI` | Typical scenario; assumes trend continues | Revised project budget |
| Project Mgmt | CV (Cost Variance) | `EV - AC` | Positive = under budget; negative = over | Budget variance |
| Project Mgmt | SV (Schedule Variance) | `EV - PV` | Positive = ahead; negative = behind | Schedule variance |
| Supply Chain | Cash-to-Cash Cycle | `DIO + DSO - DPO` | Days: Inventory + Sales Outstanding - Payable | Working capital efficiency |
| Supply Chain | Fill Rate | `(Orders delivered complete / Total orders) × 100` | Target typically >95% | Service level KPI |
| Supply Chain | Perfect Order Rate | `OTIF × Quality × Documentation × Invoicing` | All-or-nothing metric; <1 = issue exists | End-to-end SC health |
| Product Mgmt | DAU/MAU (Stickiness) | `DAU / MAU × 100%` | >20% = good; >50% = excellent (WhatsApp level) | Engagement quality |
| Product Mgmt | LTV:CAC Ratio | `LTV / CAC` | >3x = healthy unit economics | Business sustainability |
| Product Mgmt | Monthly Churn Rate | `Lost customers / Start-of-month customers` | Lower = better retention | Retention health |

## Expansion formulas (notes 111-227)

These extend the table above; each is derived and worked in the linked note area (inventory 115/117, bullwhip 114, network design 113, supply chain finance 136, queueing 149, learning curves 152, reliability 155/211, sampling 205, MSA 212, decisions 150, new products 118, finance 224-226).

| Area | Concept | Formula | Variables | When to use |
|---|---|---|---|---|
| Inventory | EPQ (finite production rate) | `√(2DS / (H(1−d/p)))` | d=demand rate, p=production rate | Lot size when stock builds gradually |
| Inventory | Newsvendor critical ratio | `CR = Cu / (Cu + Co)` | Cu=underage cost, Co=overage cost | One-period order quantity: order where P(D≤Q)=CR |
| Inventory | Fill-rate safety stock | `ESC = σL·L(z) = (1−β)·Q` | β=fill rate, L(z)=unit normal loss function, σL=s.d. of lead-time demand | Type-2 service (units filled), not cycle service |
| Inventory | Base-stock level | `S = μ(R+L) + z·σ√(R+L)` | R=review period, L=lead time | Periodic review order-up-to policy |
| Inventory | DDMRP red/yellow zones | `Red = ADU×DLT×LTF×(1+VF); Yellow = ADU×DLT` | ADU=average daily usage, DLT=decoupled lead time, LTF/VF=lead-time and variability factors | Sizing DDMRP buffers |
| Inventory | DDMRP net flow | `On-hand + On-order − Qualified demand` | Compare with top of yellow to order | Daily replenishment trigger in DDMRP |
| Supply Chain | Bullwhip (moving average forecast) | `Var(q)/Var(D) ≥ 1 + 2L/p + 2L²/p²` | L=lead time, p=averaging periods | Quantifies order-variance amplification |
| Supply Chain | Centre of gravity | `x = Σ(wᵢxᵢ)/Σwᵢ ;  y = Σ(wᵢyᵢ)/Σwᵢ` | w=volume or weight, (x,y)=location | First-cut facility location |
| Supply Chain | Trade-credit discount cost | `EAR ≈ d/(1−d) × 365/(N−t)` | d=discount rate, N=net days, t=discount days | 2/10 net 30 ≈ 37%: compare with cost of capital |
| Supply Chain | Dimensional (volumetric) weight | `L×W×H (cm) / 6000 (air) ; / 5000 (many couriers)` | Use the larger of actual and volumetric weight | Air and courier freight billing; check carrier divisor |
| Operations | Little's Law | `L = λ × W` | L=items in system, λ=arrival rate, W=time in system | Any stable process, WIP and lead time |
| Operations | M/M/1 queue | `ρ=λ/μ; Lq=ρ²/(1−ρ); Wq=λ/(μ(μ−λ)); W=1/(μ−λ)` | λ=arrival rate, μ=service rate | Single-server waiting lines |
| Operations | Learning curve (Wright) | `Yₓ = a·xᵇ ,  b = log(r)/log(2)` | a=first-unit time, r=learning rate (e.g. 0.8) | Ramp-up time and cost estimates |
| Operations | Standard time | `ST = Observed × Rating × (1 + Allowance)` | Rating=performance rating factor | Time study |
| Operations | Availability | `A = MTBF / (MTBF + MTTR)` | MTBF=mean time between failures | Maintenance planning |
| Operations | Reliability (exponential, Weibull) | `R(t)=e^{−λt} ;  R(t)=exp(−(t/η)^β)` | λ=failure rate, η=scale, β=shape | Failure analysis; β>1 means wear-out |
| Operations | System reliability | `Series: ΠRᵢ ;  Parallel: 1−Π(1−Rᵢ)` | Rᵢ=component reliability | Redundancy decisions |
| Statistics | Sample size for a mean / proportion | `n = (zσ/E)² ;  n = z²p(1−p)/E²` | E=margin of error | Survey and sampling plans |
| Statistics | Confidence interval for a mean | `x̄ ± t(α/2,n−1) × s/√n` | s=sample s.d. | Estimation with unknown σ |
| Statistics | Kaplan-Meier survival | `S(t) = Π (1 − dᵢ/nᵢ)` | dᵢ=events at time i, nᵢ=at risk | Time-to-failure with censoring |
| Statistics | Gauge R&R | `%GRR = σ_GRR/σ_total ; ndc = 1.41 × PV/GRR` | PV=part variation | Measurement system acceptance (<10% good, >30% unacceptable) |
| Statistics | Expected value of perfect information | `EVPI = EV(with perfect info) − EMV(best action)` |  | Upper bound on what information is worth |
| Statistics | Bass diffusion | `F(t) = (1 − e^{−(p+q)t}) / (1 + (q/p)e^{−(p+q)t})` | p=innovation, q=imitation coefficients | New-product adoption forecasts |
| Finance | WACC | `E/V·Re + D/V·Rd·(1−Tc)` | Re from CAPM: rf+β(Rm−rf) | Discount rate for projects |
| Finance | Degree of operating leverage | `DOL = Contribution margin / EBIT` |  | Profit sensitivity to volume |
