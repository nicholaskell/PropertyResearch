# Portfolio Comparison Rules

Property records contain durable facts. Persona scores and cross-property rankings are **derived** and should be recalculated from the current repository.

## Persona Discovery

Read every `.md` file in `personas/active/`. Each file is an independent scoring lens and may represent a person, animal, business, lifestyle or other use case.

Ignore `personas/inactive/` unless explicitly requested. Moving a persona between these directories activates/deactivates it without deleting its history.

For every property, report a score for every active persona. Do not assume equal importance; preserve individual scores and use `default_weight` only when an aggregate scenario needs a default weighting.

## Comparison Dimensions

Use both raw property facts and persona-specific priorities. Common dimensions include:

- Fatal-flaw status and research confidence
- Effective property cost
- Total / usable / prime acreage
- Prime usable acres per $100k of effective cost
- Annual tax burden
- Broadband certainty/quality
- Buildability and zoning freedom
- OGM/mineral/surface-control risk
- Privacy
- Market reach
- Distance to Green Bay, WI
- House/homesite readiness
- Shop/garage readiness
- Cost/difficulty of missing features
- Resale/improvement potential
- Every active persona score

## Relative Analysis

Do not simply rank by one overall score.

Identify:

- Best overall opportunity under the selected weighting scenario
- Best property for each active persona
- Best value
- Best usable-land value
- Best ready-to-use property
- Best build-your-own/value-add opportunity
- Best market access
- Lowest carrying cost
- Highest-confidence candidate
- High-scoring properties with unresolved fatal-flaw risks
- Properties dominated by another candidate (more expensive and worse on most important dimensions)

Support alternate scenarios by changing persona weights without modifying the underlying property records.

## Status Changes

Recheck a property when price/listing status changes materially, broadband changes, new zoning/rights/access evidence appears, or a competing property materially changes its relative position.
