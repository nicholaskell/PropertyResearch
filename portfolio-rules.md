# Portfolio Comparison Rules

Property records contain durable facts. Persona scores, Financial Fit and cross-property rankings are **derived** and should be recalculated from the current repository.

## Persona Discovery

Read every `.md` file in `personas/active/`. Each file is an independent scoring lens and may represent a person, animal, business, lifestyle or other use case.

Ignore `personas/inactive/` unless explicitly requested. Moving a persona between these directories activates/deactivates it without deleting its history.

For every property, report a score for every active persona. Do not assume equal importance; preserve individual scores and use `default_weight` only when an aggregate scenario needs a default weighting.

## Benchmark Discovery

Read every `.md` file in `benchmarks/active/`. Benchmarks are **not contenders** and should not appear in the ranked purchase list unless explicitly requested.

A `current-home` benchmark defines the user's present geographic/economic baseline. Use it to compare:

- Distance/drive time from the current home
- Local Market Trajectory
- Resale Liquidity
- Population/household/employment direction
- Land scarcity and path-of-development pressure
- Taxes/carrying costs
- Infrastructure and economic catalysts
- Buyer depth and likely ease of future resale

Explicitly identify when a candidate means trading from a stronger market into a weaker/less-liquid one, and what benefit compensates for that trade (acreage, privacy, taxes, business utility, price, etc.). Also identify candidates whose market fundamentals are equal to or stronger than the benchmark.

Do not use a single home's Zestimate as proof of market trajectory. Benchmark comparisons should rely primarily on broader municipality/county/metro evidence, using property-level value history only as supplemental context.

## Finance Discovery

Read `finance/buyer-finance.md` and active files under `finance/scenarios/` when populated.

Finance is not a persona. It answers whether a purchase structure is realistic and how available capital should be allocated.

For serious contenders, compare where useful:

- Conservative sale-proceeds scenario
- Expected/balanced sale-proceeds scenario
- Optimistic sale-proceeds scenario
- Smaller down payment + retained improvement capital
- Larger down payment + lower monthly payment
- Buying a property with an expensive feature already present versus buying cheaper and adding it

Never assume all available cash should become down payment.

## Comparison Dimensions

Use raw property facts, persona-specific priorities, benchmarks and finance assumptions. Common dimensions include:

- Fatal-flaw status and research confidence
- Effective Property Cost
- Cash to Goal
- Estimated purchase cash required
- Estimated loan amount
- Estimated monthly housing cost
- Cash reserve remaining
- Financial Fit
- Total / usable / prime acreage
- Prime usable acres per $100k of effective cost
- Annual tax burden
- Broadband certainty/quality
- Buildability and zoning freedom
- OGM/mineral/surface-control risk
- Privacy
- Market reach
- Distance to Green Bay, WI
- Distance to active current-home benchmark
- Market Trajectory vs current-home benchmark
- Resale Liquidity vs current-home benchmark
- Development optionality / growth tailwind / value-trap risk
- House/homesite readiness
- Shop/garage readiness
- Cost/difficulty of missing features
- Resale/improvement potential
- Every active persona score

## Financial Fit

Financial Fit is a derived assessment, not a stakeholder preference. Consider:

- Monthly payment versus target/max
- Cash required at closing
- Cash/reserve remaining
- Immediate capital needs
- Effective Property Cost
- Taxes, insurance and recurring carrying costs
- Cost to reach desired functionality
- Financing flexibility
- Value/equity cushion

Use current financing assumptions for live calculations and clearly label estimated rates, insurance, closing costs or other uncertain inputs.

## Capital Allocation

For serious contenders, answer:

**Where does the next available dollar create the most value?**

Compare additional down payment against retained capital for improvements/reserves. Important examples include shops, barns, access, fencing, homesite infrastructure, renovations and other high-value additions.

Do not treat equity as cash. Track:

- Cash used at closing
- Equity created by down payment
- Cash retained after closing
- Future financing/equity-borrowing potential only as an optional strategy, never as guaranteed capital

## Relative Analysis

Do not simply rank by one overall score.

Identify:

- Best overall opportunity under the selected weighting/finance scenario
- Best property for each active persona
- Best Financial Fit
- Best value
- Best usable-land value
- Best ready-to-use property
- Best build-your-own/value-add opportunity
- Best market access
- Strongest market trajectory / resale outlook
- Best development optionality
- Lowest carrying cost
- Highest-confidence candidate
- Best use of available cash/equity
- High-scoring properties with unresolved fatal-flaw risks
- Properties dominated by another candidate (more expensive and worse on most important dimensions)
- Candidates that improve lifestyle but materially weaken exit/liquidity versus the current-home benchmark

Support alternate scenarios by changing persona weights, benchmarks or finance assumptions without modifying the underlying property facts.

## Status Changes

Recheck a property when price/listing status changes materially, broadband changes, new zoning/rights/access evidence appears, finance assumptions change materially, the current home sale becomes more certain, the current-home benchmark changes, or a competing property materially changes its relative position.
