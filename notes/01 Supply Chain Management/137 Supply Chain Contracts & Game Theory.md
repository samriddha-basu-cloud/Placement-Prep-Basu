---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Supply Chain Contracts & Game Theory"
tier: Tier 2
roles: Consulting / Operations
status: complete
subtopics: 13
---
# Supply Chain Contracts & Game Theory

⬅ [[136 Supply Chain Finance & Working Capital]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[138 Order Management, Customer Service & Cost-to-Serve]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. The Supply Chain as a Game: Decentralised vs Centralised]]
2. [[#2. Double Marginalisation (Worked Numbers)]]
3. [[#3. The Wholesale Price Contract and Why It Fails]]
4. [[#4. Newsvendor Channel Coordination: The Design Rule]]
5. [[#5. Buy-Back (Returns) Contracts]]
6. [[#6. Revenue-Sharing Contracts and Blockbuster]]
7. [[#7. Quantity-Flexibility and Sales-Rebate Contracts]]
8. [[#8. Stackelberg Leader-Follower Games]]
9. [[#9. Prisoner's Dilemma and Repeated Games in Supply Chains]]
10. [[#10. Bargaining and Nash Bargaining]]
11. [[#11. Information Asymmetry: Screening, Signalling and Forecast Gaming]]
12. [[#12. Collaboration Incentives and Contract Negotiation Implications]]
13. [[#13. ⭐ Advanced: Option Contracts, Take-or-Pay and Capacity Reservation]]

## 📰 News box
> [!news] Why this matters now (2024–2026): volatile lead times and rising dead stock make "who carries the risk" a contract question
> **Dead stock keeps rising (Oct 2026).** A Netstock survey of 150+ small and mid-size business customers, reported by Supply Chain Dive on 1 October 2026, found dead stock as a share of excess inventory rising from **12% (2024) to 17% (2025) to 24% (2026)**. Supplier lead-time swings were the top challenge for 29% of firms (77% listed it among their main problems), and average lead times ranged from **21 days for the fastest-moving firms to 79 days for the slowest**. Only 7% of firms met all four resilience measures Netstock tracked. Whoever holds unsold stock or idle capacity when forecasts miss is decided by the contract: buy-back, revenue sharing, flexibility bands and take-or-pay clauses are the tools. ([Supply Chain Dive](https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880/))
>
> **Take-or-pay is old law and still contested.** A take-or-pay clause makes the buyer either purchase an agreed volume or pay a (reduced) penalty price; it is common in energy and especially gas sales, and the English courts have called it a familiar commercial provision, while outside oil and gas courts often test such clauses as possible penalties. ([Wikipedia: Take-or-pay contract](https://en.wikipedia.org/wiki/Take-or-pay_contract))
>
> **Evidence that revenue sharing is real.** Julie Mortimer's study in the *Review of Economic Studies* (2008) uses store-level data to compare revenue-sharing contracts with linear pricing in video rental, showing the theory is testable and was used in practice. ([Oxford Academic](https://academic.oup.com/restud/article/75/1/165/1573036))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The Supply Chain as a Game: Decentralised vs Centralised
> 🟠 Tier 2 · _Key points:_ Players with own objectives, local vs system optimum, contracts align incentives

### Definition
A supply chain with separately owned firms is a **game**: each firm maximises **its own profit**, anticipates the others' responses, and the outcome (a **Nash equilibrium**) is usually worse for the whole chain than what a single owner would achieve. Two benchmarks:

- **Centralised (integrated) solution**: one decision maker maximises total chain profit. This is the **first-best**.
- **Decentralised solution**: each firm optimises locally given the others' actions. This is the **equilibrium**.

The gap between them is the **efficiency loss** (16% in the newsvendor example and 25% in the linear double-marginalisation example below). A contract **coordinates** the chain when the first-best actions form a Nash equilibrium of the decentralised game; it is **Pareto-improving** if no firm is worse off than before. Contracts also **split** the profit: coordination fixes the size of the pie, the parameters (prices, rebates, shares) fix who eats what, and that is the negotiation ([[002 Procurement & Strategic Sourcing]], [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]]).

Misaligned incentives are not exotic: they explain the **bullwhip effect** ([[114 Bullwhip Effect, Beer Game & Information Sharing]]), under-stocking by retailers, over-capacity at suppliers, and low effort by outsourced partners.

### Example
A Mumbai retailer and an Ahmedabad apparel maker each aim at their own margin. The retailer orders less than the chain-optimal quantity because it carries all the unsold-stock risk while the maker keeps its margin on every unit shipped. Total profit is below what one owner would make, even though both parties act rationally.

### In the news
See news box. Lead-time and demand volatility mean unsold stock is the main arena where decentralised incentives diverge from the system optimum.

### Interview angle
> [!question] How it is asked
> "Why can two rational firms in a supply chain end up with lower combined profit than one integrated firm?"

> [!tip] Strong answer includes
> - Define first-best (integrated) vs equilibrium (decentralised)
> - Name the cause: each party ignores the effect of its decision on the other's profit (externality)
> - Say a contract aligns incentives and splits surplus; coordination is not the same as fairness
> - Give a one-line example (double marginalisation or newsvendor under-ordering)

---
## 2. Double Marginalisation (Worked Numbers)
> 🟠 Tier 2 · _Key points:_ Two mark-ups, higher price, lower quantity, 25% profit loss in the linear case; fixes

### Definition
**Double marginalisation** (Spengler, 1950) occurs when an upstream firm and a downstream firm both add a mark-up over cost. The downstream firm treats the wholesale price $w$ as its marginal cost and prices above it; the combined mark-up exceeds the single mark-up an integrated firm would apply. Result: **retail price too high, quantity too low, chain profit lower**, and consumers also lose.

Linear model: demand $p = a - q$, unit production cost $c$.

$$\text{Integrated: } q^* = \frac{a-c}{2}, \quad p^* = \frac{a+c}{2}, \quad \pi^* = \frac{(a-c)^2}{4}$$

$$\text{Decentralised: } w^* = \frac{a+c}{2}, \quad q = \frac{a-c}{4}, \quad \pi_{chain} = \frac{3(a-c)^2}{16}$$

So the decentralised chain earns exactly **75%** of the first-best. Fixes: vertical integration; **two-part tariff** (price at marginal cost plus a fixed fee); nonlinear pricing; resale price maintenance and price caps (with legal limits); **buy-back and revenue-sharing** contracts for stochastic demand; competition at the retail tier.

### Example
$p = 100 - q$ (price in ₹, $q$ in thousand units), $c$ = ₹20.

- **Integrated:** $q^* = 40$, $p^* = ₹60$, profit = (60 − 20) × 40 = **₹1,600 thousand (₹16 lakh)**.
- **Decentralised:** the retailer's best response to $w$ is $q = (100-w)/2$. The manufacturer maximises $(w-20)(100-w)/2$, giving $w = ₹60$, $q = 20$, retail price ₹80. Manufacturer profit = 40 × 20 = **₹800**; retailer = (80 − 60) × 20 = **₹400**; chain = **₹1,200** (75%).
- **Two-part tariff:** wholesale price = ₹20 (marginal cost), fixed fee $F$ = ₹1,000. The retailer orders 40, earns 1,600 − 1,000 = **₹600**; the manufacturer earns **₹1,000**. Both beat the decentralised outcome (400 and 800). Any $F$ between 800 and 1,200 makes both better off.

### In the news
See news box. Where buyers and suppliers each add margin through long chains (distributor, wholesaler, retailer) the same effect compounds, which is one reason direct-to-consumer and platform models gain share.

### Interview angle
> [!question] How it is asked
> "A manufacturer sells through one retailer. Prices look high and volume low. What is going on and what would you do?"

> [!tip] Strong answer includes
> - Name double marginalisation and show the direction: price up, quantity down, profit below first-best
> - Quote the 75% figure for the linear case or compute a quick numeric example
> - Fixes: two-part tariff / franchise fee, revenue sharing, volume-based rebates, integration
> - Mention a limit: fees need the retailer to accept a fixed payment and the competition-law view on price control

---
## 3. The Wholesale Price Contract and Why It Fails
> 🟠 Tier 2 · _Key points:_ Simple, widely used, does not coordinate under demand uncertainty

### Definition
The **wholesale price contract** is the default: the supplier charges $w$ per unit; the retailer chooses the order quantity $Q$ and carries all demand risk. It is easy to administer, but with stochastic demand the retailer's critical ratio uses *its* margin $p - w$ rather than the chain's margin $p - c$:

$$\text{Retailer: } F(Q_w) = \frac{p-w}{p}, \qquad \text{Chain: } F(Q^*) = \frac{p-c}{p}$$

Because $w > c$ the retailer orders less than the chain optimum ($Q_w < Q^*$) for any $w > c$. The only price that coordinates is $w = c$, which leaves the supplier with zero profit. So a pure wholesale-price contract can never coordinate **and** give the supplier a positive profit: the reason richer contracts exist. It also pushes all inventory risk to the retailer, who then holds back, and later regrets under-stocking in peak demand.

This is the newsvendor critical ratio already developed in [[003 Inventory Management]] (sub-topic 15) and the decision-analysis view in [[150 Decision Analysis & Simulation]].

### Example
Retail price $p$ = ₹1,000, production cost $c$ = ₹300, salvage zero, demand uniform between 0 and 1,000 units.

- **Chain optimum:** critical ratio = 700/1,000 = 0.70, so $Q^* = 700$. Expected sales = 700 − 700²/2,000 = 455; expected profit = 1,000 × 455 − 300 × 700 = **₹2,45,000**.
- **Wholesale price ₹580:** retailer ratio = 420/1,000 = 0.42, so $Q_w = 420$; expected sales = 331.8. Retailer profit = 1,000 × 331.8 − 580 × 420 = **₹88,200**; supplier = (580 − 300) × 420 = **₹1,17,600**; chain = **₹2,05,800**, which is **84%** of first-best, a loss of ₹39,200.

### In the news
See news box. With dead stock rising, retailers rationally order cautiously under plain wholesale contracts, which then depresses supplier volume.

### Interview angle
> [!question] How it is asked
> "Why is a simple price-per-unit contract not enough when demand is uncertain?"

> [!tip] Strong answer includes
> - Retailer's critical ratio uses its own margin, so it under-orders
> - Only $w = c$ coordinates, and then supplier profit is zero
> - The fix: share demand risk (returns, revenue share, flexibility) so the retailer's effective cost of overstock falls
> - A quick numeric illustration (84% of first-best)

---
## 4. Newsvendor Channel Coordination: The Design Rule
> 🟠 Tier 2 · _Key points:_ Coordinate by making the retailer's critical ratio equal the chain's; contracts move the split

### Definition
Cachon's survey of coordinating contracts (Handbook chapter, "Supply chain coordination with contracts") treats a supplier selling to a newsvendor retailer. The design rule is: **choose contract parameters so the retailer's critical ratio equals the chain's, $(p-c)/p$**. Then the retailer, acting selfishly, orders $Q^*$. The remaining degrees of freedom set the **profit split**, so the same coordinated chain can give the retailer a small or large share.

| Contract | Retailer pays / gets | Coordination condition (zero salvage) | Who bears overstock |
|---|---|---|---|
| **Buy-back** | wholesale $w$; supplier repurchases leftovers at $b$ | $b = p - \frac{p(p-w)}{p-c}$ | Shared |
| **Revenue sharing** | wholesale $w$; retailer keeps fraction $\phi$ of revenue | $w = \phi c$ | Shared via lower $w$ |
| **Quantity flexibility** | commit to order $Q$; may adjust within a band | Band and price jointly set | Supplier takes part of the demand error |
| **Sales rebate** | rebate $r$ per unit sold above target $t$ | $w$, $r$, $t$ set jointly | Supplier pays for sales above $t$ |
| **Two-part tariff (certain demand)** | $w=c$ plus fee | Fee splits profit | Retailer |

Cachon reports an **equivalence** among several of these: a buy-back and a revenue-sharing contract can generate identical outcomes for suitable parameters.

### Example
With the same numbers ($p$ = ₹1,000, $c$ = ₹300, $w$ = ₹580), the buy-back price that coordinates is $b = 1000 - 1000 \times 420/700 =$ **₹400**. The retailer's ratio becomes (1,000 − 580)/(1,000 − 400) = 0.70, so $Q = 700$; leftovers = 245 units.

- Retailer: 1,000 × 455 + 400 × 245 − 580 × 700 = **₹1,47,000**
- Supplier: (580 − 300) × 700 − 400 × 245 = **₹98,000**
- Chain: **₹2,45,000** (first-best)

The retailer gains versus ₹88,200, but the supplier earns less than its ₹1,17,600 from plain wholesale, so this particular buy-back is not Pareto-improving; the supplier would need a higher $w$ to share the gain (next two sub-topics).

### In the news
See news box. Faced with unsold stock, buyers push for return rights, and suppliers push back; the coordinating rule tells both sides where the "fair" parameter combinations lie.

### Interview angle
> [!question] How it is asked
> "How would you design a contract that makes a retailer stock the chain-optimal quantity?"

> [!tip] Strong answer includes
> - The rule: equalise the retailer's critical ratio with the chain's
> - One concrete contract with the formula and a number
> - Parameters set the split, so negotiate the split separately from the coordination condition
> - Practical limits: monitoring returns, salvage value, and retailer's other products

---
## 5. Buy-Back (Returns) Contracts
> 🟠 Tier 2 · _Key points:_ Supplier repurchases unsold units; used in books, magazines, pharma, fashion; moral hazard

### Definition
In a **buy-back contract** the supplier charges $w$ and takes back unsold units at $b < w$. The retailer's underage cost is $p - w$ and overage cost is $w - b$, so its critical ratio is $(p-w)/(p-b)$. Raising $b$ cuts the retailer's downside, so it orders more. Used where demand is uncertain and products have short lives or salvage value to the supplier: books, newspapers and magazines, pharmaceuticals, greeting cards, seasonal clothing, perishable FMCG.

Costs and risks: **reverse logistics** (handling returned units, see [[135 Reverse Logistics, Remanufacturing & EPR in India]]), the retailer's **moral hazard** (less effort to sell, or ordering carelessly because returns are cheap), fraud (returning damaged stock), and the supplier's salvage value must exceed handling cost for returns to be efficient. In India, sale-or-return is standard in publishing and in many distributor chains in medicines (expiry returns).

Variants: a **credit-only return** (not cash), a **cap on returns** (for example up to 10-20% of units), and returns **limited to the end of season**.

### Example
Data as before; $w$ = ₹580, $b$ = ₹400 coordinates the chain at $Q$ = 700 (retailer ₹1,47,000, supplier ₹98,000), but the supplier ends below its ₹1,17,600 from plain wholesale. A coordinated buy-back gives the retailer a share $\phi = (p-w)/(p-c)$ of chain profit, so the split is set through $w$. The chain gain over plain wholesale is 2,45,000 − 2,05,800 = **₹39,200**; a symmetric (Nash) split gives the retailer ₹88,200 + 19,600 = **₹1,07,800**, which is $\phi$ = 0.44, so $w$ = 1,000 − 0.44 × 700 = **₹692** and $b = 1000 - 1000 \times 308/700 =$ **₹560**.

- Retailer: 1,000 × 455 + 560 × 245 − 692 × 700 = **₹1,07,800**
- Supplier: (692 − 300) × 700 − 560 × 245 = **₹1,37,200**; both beat plain wholesale.

A leftover return costs the supplier salvage loss: if goods return at ₹400 with salvage ₹150, loss per returned unit = ₹250 on 245 units = ₹61,250.

### In the news
See news box. As dead stock grows, return clauses become more valuable to buyers, so suppliers increasingly meter returns with caps, restocking fees and shorter windows.

### Interview angle
> [!question] How it is asked
> "Why would a supplier ever agree to buy back unsold goods? Who benefits?"

> [!tip] Strong answer includes
> - The retailer orders more, sales rise, and the chain (not just the retailer) earns more, so the supplier can recover by raising $w$
> - Show the formula for the retailer's critical ratio
> - Risks: moral hazard, reverse-logistics cost, salvage value
> - Practical controls: caps, credit notes, time windows, joint demand-forecasting

---
## 6. Revenue-Sharing Contracts and Blockbuster
> 🟠 Tier 2 · _Key points:_ Low wholesale price plus a share of revenue; Blockbuster and studios; multiplex split in India

### Definition
In a **revenue-sharing contract** the supplier lowers the wholesale price below cost and in return receives a fraction of the retailer's revenue. With the retailer keeping $\phi$ of revenue and paying $w = \phi c$, its critical ratio becomes $(\phi p - \phi c)/(\phi p) = (p-c)/p$, the chain's. The supplier earns a margin on sales rather than on shipments, so both want sales to be high. The retailer's profit equals $\phi$ times the chain's, so $\phi$ is a direct bargaining dial.

Downsides: needs **revenue visibility** (audits, system access), can cause **retailer to reduce selling effort** if its share is small, and does not handle **competitive retailers** perfectly. Cachon and Lariviere (2005) analyse the contract; it is used in video rental, theatrical release, publishing, and platform commissions.

**Blockbuster case (widely cited, from Cachon and Lariviere):** in the late 1990s studios sold VHS tapes to Blockbuster at about **$65 each**, so Blockbuster could not afford to stock enough copies for peak demand and customers often found a new release unavailable. In 1998 Blockbuster began revenue-sharing deals: a low upfront price (about **$8 a tape**) and a **30-45% share** of rental revenue to the studio. The standard textbook account is that Blockbuster stocked more copies of new releases, availability rose and both sides gained. Mortimer's *Review of Economic Studies* paper tests this using store-level data. Treat the exact dollar figures as textbook-cited rather than from company filings.

India: multiplex chains and film distributors reportedly split net box-office revenue on a share that declines week by week, a revenue-sharing structure whose terms are negotiated and occasionally disputed (check current terms before quoting).

### Example
Same numbers; the retailer keeps $\phi$ = 0.6, pays $w = 0.6 \times 300 =$ **₹180**.

- Retailer ratio = (600 − 180)/600 = 0.70, so $Q$ = 700.
- Retailer: 0.6 × 1,000 × 455 − 180 × 700 = **₹1,47,000**
- Supplier: (180 − 300) × 700 + 0.4 × 1,000 × 455 = −84,000 + 1,82,000 = **₹98,000**
- Identical to the buy-back with $w$ = ₹580 and $b$ = ₹400, confirming the equivalence.

To give the retailer ₹1,07,800 (symmetric Nash split of the gain), set $\phi = 107{,}800 / 245{,}000 =$ **0.44** and $w$ = 0.44 × 300 = **₹132**; the supplier then earns ₹1,37,200. Both beat plain wholesale (₹88,200 and ₹1,17,600).

### In the news
See news box (Mortimer's study). Revenue sharing now appears in platform commissions and SaaS marketplace fees, where "who carries the unsold risk" becomes "who carries the demand risk".

### Interview angle
> [!question] How it is asked
> "Explain how Blockbuster and the film studios used revenue sharing to make both better off."

> [!tip] Strong answer includes
> - The problem: expensive tapes meant Blockbuster under-stocked relative to chain-optimal quantity
> - The contract: low upfront price plus a share of rental income, aligning both on rentals
> - Condition: $w = \phi c$, retailer profit = $\phi$ × chain profit
> - Risks: audit cost, reporting disputes, retailer effort

---
## 7. Quantity-Flexibility and Sales-Rebate Contracts
> 🟠 Tier 2 · _Key points:_ Bands around the order, supplier shares forecast risk; rebates above a target

### Definition
**Quantity-flexibility (QF) contracts** (Tsay, 1999; stylised here): the retailer places an initial order $Q$; the supplier commits to deliver up to $(1+\delta)Q$ if the retailer wants more, and the retailer commits to pay for at least $(1-\delta)Q$ if demand disappoints. The band $\delta$ transfers part of the **demand-forecast risk** to the supplier, who must hold capacity, while the retailer's commitment gives the supplier planning certainty. Common in automotive and electronics supply (see [[131 Automotive Supply Chain - JIT, Tiers & EVs]], [[134 Electronics & Semiconductor Supply Chain]]), with rolling forecasts frozen at stage gates.

**Sales-rebate contracts** (Taylor, 2002): the supplier pays the retailer a rebate $r$ for each unit sold **above a threshold $t$**. The threshold matters: a rebate from unit one lets the supplier pay for sales the retailer would have made anyway and makes coordination costly; a well-chosen $t$ pays only for the extra effort or volume that the contract is designed to induce. A volume rebate also acts as an **incentive to push sales effort** (a moral-hazard fix), unlike buy-back, which protects against overstock but not effort.

Related: **sales-rebate vs price-protection** (a retailer is compensated for a list-price cut), **markdown allowances** and **price-discount contracts**.

### Example
Initial order $Q$ = 700, $\delta$ = 0.2, wholesale ₹580.

- Retailer must pay for at least 0.8 × 700 = **560** units; supplier guarantees up to 1.2 × 700 = **840**.
- Demand 500 units: retailer pays for 560 and is stuck with 60 unsold: cost 60 × 580 = **₹34,800** (versus 200 unsold units if it had no flexibility).
- Demand 900 units: retailer receives 840, loses 60 sales; shortfall margin = 60 × (1,000 − 580) = **₹25,200**.
- Supplier must hold capacity for 840, 20% above the committed 700, and will price this in.

### In the news
See news box. With lead times ranging from 21 to 79 days, flexibility bands are how buyers and suppliers agree who pays for forecast error.

### Interview angle
> [!question] How it is asked
> "How would you share forecast risk between an OEM and a component supplier?"

> [!tip] Strong answer includes
> - A flexibility band with frozen horizon and a rolling forecast
> - Risk transfer and its price: supplier holds capacity, retailer commits minimum volume
> - Compare with buy-back (returns), revenue sharing (sales-linked) and rebates (effort)
> - Governance: forecast accuracy tracking, penalties for repeated over-forecasting

---
## 8. Stackelberg Leader-Follower Games
> 🟠 Tier 2 · _Key points:_ Sequential moves; leader anticipates follower's best response; first-mover and power

### Definition
In a **Stackelberg game** one player (the **leader**) commits first and the **follower** responds optimally. The leader solves the follower's best-response problem backward ("backward induction"), then picks the action that maximises its own profit given that reaction. Supply chain uses:

- Manufacturer sets the wholesale price ($w$); retailer chooses quantity or price (the standard double-marginalisation set-up).
- A dominant retailer (a large Indian modern-trade chain or an e-commerce platform) sets margin or "back margin" terms and the supplier responds.
- An OEM sets a target cost or a mandated price-down; the supplier chooses effort and investment.

The leader earns more than in a simultaneous game only if it can **credibly commit**. The leader's gain is a **first-mover advantage**, but with a linear contract the leader still leaves chain profit on the table (efficiency loss). Contrast with **Cournot** (simultaneous quantities) and **Bertrand** (simultaneous prices).

### Example
Using $p = 100 - q$ and $c = 20$ from sub-topic 2, with the manufacturer as leader:

- Follower's reaction: $q(w) = (100-w)/2$.
- Leader's profit $(w-20)(100-w)/2$ is maximised at $w$ = **₹60**, giving $q = 20$, retail price ₹80.
- Leader profit = **₹800**, follower = **₹400**: the first mover captures two-thirds of the (reduced) chain profit of 1,200.

If the retailer were the leader (for example by dictating the wholesale price), the split would swing towards the retailer; in a linear contract the chain still earns less than first-best unless a coordinating term such as a franchise fee or buy-back is added.

### In the news
See news box. Large buyers dictating terms to smaller suppliers in times of volatility is the leader-follower game; the MSME payment rules in [[136 Supply Chain Finance & Working Capital]] limit how long the leader can delay payment.

### Interview angle
> [!question] How it is asked
> "Model a manufacturer choosing the wholesale price and a retailer choosing quantity. Who has the advantage?"

> [!tip] Strong answer includes
> - Backward induction: follower's best response first, then leader's optimisation
> - Result: first mover captures more of the (reduced) surplus
> - Chain profit still below first-best unless a coordinating contract is used
> - Note when the leader's commitment is credible (long-term contracts, exclusivity, brand power)

---
## 9. Prisoner's Dilemma and Repeated Games in Supply Chains
> 🟠 Tier 2 · _Key points:_ Dominant strategy to defect; repeated interaction and trust sustain cooperation

### Definition
In a **prisoner's dilemma**, each player has a dominant strategy to **defect**, yet mutual cooperation would leave both better off. Examples: both sides hide demand and capacity information; a buyer squeezes price while a supplier cuts quality; two competing retailers over-order in shortage ("shortage gaming", bullwhip, see [[114 Bullwhip Effect, Beer Game & Information Sharing]]); suppliers refuse to invest in a buyer-specific asset for fear of hold-up.

In a **one-shot** game the Nash equilibrium is (defect, defect). In a **repeated** game cooperation can be sustained by a **trigger strategy**: cooperate until the other defects, then punish forever. With payoffs $T > R > P > S$ (temptation, reward, punishment, sucker) and discount factor $\delta$, cooperation is sustainable when:

$$\delta \geq \frac{T - R}{T - P}$$

Practical routes: long-term contracts and partnership horizons, reputation and supplier scorecards, joint investment, transparent data sharing, multiple suppliers (credible threat), third-party audits ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]]).

### Example
Annual payoffs (₹ crore) (supplier, buyer):

| | Buyer shares forecast | Buyer hides forecast |
|---|---|---|
| **Supplier invests in capacity** | (8, 8) | (2, 10) |
| **Supplier holds back** | (10, 2) | (4, 4) |

Defecting is dominant for both, so the one-shot outcome is **(4, 4)** instead of (8, 8). In a repeated relationship, $T$ = 10, $R$ = 8, $P$ = 4: $\delta \geq (10-8)/(10-4) =$ **1/3**. If both value the future at a discount factor of at least 0.33 (for instance, the relationship continues next year with probability above one in three), cooperation is an equilibrium. This is why a one-year purchase order breeds opportunism and a 5-year framework agreement breeds data sharing.

### In the news
See news box. Where lead times swing from 21 to 79 days, hiding information is tempting; repeated-game incentives (long frameworks, vendor ratings) pull the other way.

### Interview angle
> [!question] How it is asked
> "Why do retailers inflate orders in shortages and what would you change in the contract?"

> [!tip] Strong answer includes
> - Prisoner's dilemma structure: each is better off defecting regardless of the other
> - Fix: allocation rules based on past sales rather than orders, order-cancellation penalties, shared point-of-sale data
> - Repeated game condition (δ high enough), reputation, and long contracts
> - A numeric payoff table if asked

---
## 10. Bargaining and Nash Bargaining
> 🟠 Tier 2 · _Key points:_ Surplus division, disagreement point, bargaining power, BATNA

### Definition
A coordinating contract creates **surplus** over the decentralised outcome; **bargaining** decides who gets it. The **Nash bargaining solution** picks the split that maximises $(u_1 - d_1)^{\alpha}(u_2 - d_2)^{1-\alpha}$ subject to the feasible profits $u_1 + u_2 = \pi^*$, where $d_i$ is the **disagreement point** (what each gets if talks fail, the BATNA) and $\alpha$ the bargaining power:

$$u_1 = d_1 + \alpha(\pi^* - d_1 - d_2), \qquad u_2 = d_2 + (1-\alpha)(\pi^* - d_1 - d_2)$$

Each side gets its fallback plus a share of the surplus equal to its power. Implications: **improve your BATNA** (second source, alternative customers, insourcing) before negotiating; the stronger your outside option, the more of the surplus you receive; a firm with no alternatives is a price-taker. Rubinstein-type alternating-offer models show that **patience** (lower discount rate) also raises a party's share. Link to procurement tactics in [[002 Procurement & Strategic Sourcing]] and [[122 Spend Analysis, Savings & Procurement Maturity]].

### Example
Double marginalisation numbers (₹ thousand): first-best 1,600; disagreement (decentralised, Stackelberg) payoffs 800 (manufacturer) and 400 (retailer); surplus = 1,600 − 1,200 = 400.

- Equal power ($\alpha$ = 0.5): manufacturer **1,000**, retailer **600**. A fixed fee of ₹1,000 with $w = c$ achieves exactly this.
- Manufacturer power 0.6: manufacturer 800 + 0.6 × 400 = **1,040**; retailer 400 + 0.4 × 400 = **560**.

Newsvendor numbers: surplus ₹39,200; with symmetric power, supplier ₹1,37,200 and retailer ₹1,07,800 (revenue-share $\phi$ = 0.44, $w$ = ₹132).

### In the news
See news box. Volatile conditions change BATNAs; a buyer with idle inventory has little urgency, a supplier with idle capacity has little leverage.

### Interview angle
> [!question] How it is asked
> "You are negotiating a long-term contract with a dominant customer. How do you improve your outcome?"

> [!tip] Strong answer includes
> - Compute the joint surplus first and negotiate size and split separately
> - Strengthen BATNA, show alternatives, diversify customers or products
> - Trade cheap-to-you, valuable-to-them terms (forecast visibility, volume commitments)
> - Walk-away point and concession plan prepared in advance

---
## 11. Information Asymmetry: Screening, Signalling and Forecast Gaming
> 🟠 Tier 2 · _Key points:_ Private demand info, adverse selection, moral hazard, forecast inflation, menus of contracts

### Definition
Supply chain partners hold **private information**: the retailer knows the market, the supplier knows its cost and capacity, each can hide effort. Two problems:

- **Adverse selection** (hidden type): the retailer's demand forecast is private; if the supplier cannot tell strong from weak forecasts, it must **screen** by offering a **menu of contracts** (for example a high-commitment low-price contract and a low-commitment high-price contract) so that each type self-selects.
- **Moral hazard** (hidden action): the retailer's selling effort or the supplier's quality effort is unobservable; contracts must pay for outcomes (rebates, revenue share, warranty cost-sharing).

**Cheap-talk forecasts** are not credible: a retailer who benefits when the supplier builds capacity will inflate its forecast. Credible communication needs **costly signals**: take-or-pay commitments, deposits, or payment on a non-refundable portion. **Forecast-sharing mechanisms**: Cachon and Lariviere (2001, "Contracting to assure supply") compare binding (commitment) and non-binding regimes when the retailer can misreport; the practical lesson is that commitment attached to the forecast makes inflation costly. Sport Obermeyer (HBS case, Hammond and Raman, 1994) shows a practical response: collect several forecasts from a committee, treat disagreement as a signal of uncertainty, make low-uncertainty styles first and keep capacity for the rest.

### Example
A retailer tells its supplier that demand will be 1,000 units; the supplier builds capacity of 1,000 at ₹300 per unit. True demand is 600. The 400 idle units cost the supplier ₹1,20,000 (400 × 300). Over several seasons the supplier discounts the retailer's forecasts. Fix: a **commit-and-flex** contract that requires the buyer to buy 80% of the forecast (800 units) regardless; the same inflation now costs the retailer 200 units × ₹580 = ₹1,16,000 in unwanted purchases, so it forecasts honestly.

### In the news
See news box. As forecast error widens (dead stock rising to 24% of excess inventory), unsupported forecasts lose credibility and committed volumes gain value.

### Interview angle
> [!question] How it is asked
> "How do you stop a customer from over-forecasting to secure capacity?"

> [!tip] Strong answer includes
> - Cheap talk is not credible: attach a cost to the forecast (take-or-pay share, deposits, frozen horizon)
> - Menu of contracts that makes each type self-select
> - Historical forecast-accuracy scoring and allocation tied to actual purchases
> - Joint planning to reduce the information gap ([[120 Integrated Business Planning (IBP) & S&OP Maturity]], [[114 Bullwhip Effect, Beer Game & Information Sharing]])

---
## 12. Collaboration Incentives and Contract Negotiation Implications
> 🟠 Tier 2 · _Key points:_ Gain-share, VMI, CPFR; pick contract by risk type; negotiation checklist

### Definition
Collaboration works when incentives are aligned and benefits visible and shared. Common structures:

- **VMI and consignment**: the supplier manages and owns stock until use; needs a replenishment rule and a fair holding-cost allocation.
- **CPFR**: joint forecasts and plans with exception handling.
- **Gain-share / pain-share**: savings from joint cost-reduction (design, logistics) split by formula; pain from shortfalls split likewise.
- **Long-term agreements with price indexation** to commodities ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]).
- **Performance-based contracts** with service levels, bonus and penalties.

Choosing a contract by the risk to be managed:

| Problem | Best-fit contract |
|---|---|
| Retailer under-orders (overstock risk) | Buy-back, revenue share, quantity flexibility |
| Retailer under-promotes (effort) | Sales rebate, revenue share with adequate $\phi$ |
| Supplier under-builds capacity | Take-or-pay, capacity reservation, option contracts |
| Forecast inflation | Commitment share, penalties, option pricing |
| Commodity price swings | Index-linked pricing, collars |
| Long projects with uncertain scope | Target-cost and gain-share contracts ([[168 Project Procurement, Contracts & EPC Delivery]]) |

**Negotiation implications:** quantify joint surplus first, negotiate the split second; trade items with asymmetric value; make commitments credible (deposits, exclusivity, minimum volumes); check legal limits (resale price maintenance, India's Competition Act, MSMED payment limits); and plan the **renegotiation clause** for large shocks.

### Example
A manufacturer and a distributor of kitchen appliances in Pune: the distributor returns 12% of units unsold each season. Plan: a buy-back for up to 10% of units at 70% of cost, a 2% volume rebate above last year's sales (to protect selling effort), a shared monthly forecast and a quarterly gain-share review. Illustrative target: distributor orders rise, returns are capped and monitored, and the supplier smooths factory slots.

### In the news
See news box. As volatility rises, rigid price-only contracts yield to risk-sharing clauses with explicit triggers and caps.

### Interview angle
> [!question] How it is asked
> "A key supplier and your firm blame each other for stock-outs and excess stock. How do you fix the commercial relationship?"

> [!tip] Strong answer includes
> - Diagnose the incentive problem (who bears which risk, who has what information)
> - Match the contract tool to the problem, with an explicit split of surplus
> - Add data sharing and governance (scorecards, review cadence, escalation path)
> - Keep it enforceable and legally compliant; pilot with one category before scaling

---
## 13. ⭐ Advanced: Option Contracts, Take-or-Pay and Capacity Reservation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Option (reservation) contracts**: the buyer pays a **reservation fee** $o$ per unit for the right, not the obligation, to buy up to $Q$ units later at an **exercise price** $e$. The supplier builds capacity for the reserved units; the buyer defers its quantity decision until demand is clearer. Option contracts are equivalent in effect to buy-back contracts (a buy-back is a call option on the supplier's inventory) and are used for capacity, commodity and energy supply.

**Take-or-pay**: the buyer must either take an annual minimum quantity or pay a penalty price for the shortfall (typically a fraction of the full price). It protects the supplier's fixed investment (pipelines, plants, tolling capacity) and is common in gas, power purchase agreements and long-term raw-material deals. Legal enforceability varies; courts may test whether a shortfall payment is a genuine pre-estimate of loss or a penalty.

**Capacity reservation** in semiconductors and contract manufacturing: buyers pay deposits or commit minimum volumes for scarce capacity ([[134 Electronics & Semiconductor Supply Chain]]).

Design trade-off: higher commitment lowers the supplier's risk and price but exposes the buyer to over-commitment; options and rolling forecasts reduce that exposure.

### Example
A tyre maker reserves 1,00,000 units of annual synthetic-rubber capacity with a supplier at a reservation fee of ₹20 per unit and an exercise price of ₹180 (spot expected to average ₹190, with ±₹40 swings).

- Upfront reservation cost = 1,00,000 × 20 = **₹20 lakh**.
- If spot in a shortage is ₹250 and the firm exercises all units: effective cost = 180 + 20 = ₹200 per unit versus ₹250, a saving of ₹50 per unit, i.e. **₹50 lakh** on 1,00,000 units (already net of the fee).
- Break-even: exercising pays whenever spot exceeds the exercise price of ₹180.
- If spot is ₹150 and the firm buys on the spot market instead: loses the **₹20 lakh** fee, an insurance premium for the shortage.

Take-or-pay comparison: minimum 80,000 units, shortfall price 40% of ₹180 = ₹72. If the firm uses only 60,000 units it pays 20,000 × 72 = **₹14.4 lakh** for goods it never receives.

### In the news
See news box. The take-or-pay item shows this is a long-standing clause with ongoing legal tests, and volatile lead times (21 to 79 days) increase the value of reserved capacity.

### Interview angle
> [!question] How it is asked
> "When would you use an option contract instead of a firm order?"

> [!tip] Strong answer includes
> - High uncertainty and a cost of being short larger than the reservation fee
> - Premium vs insurance logic and the exercise price comparison with spot
> - Supplier view: fee covers capacity and risk, so price accordingly
> - Compare with take-or-pay (commitment to supplier) and buy-back (returns to supplier)
