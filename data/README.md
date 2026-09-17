# Structured Data Layer

This directory contains **generated analytical data** derived from the authoritative Markdown property records and development scenarios.

## Source-of-truth rule

Markdown property records and their supporting evidence remain authoritative. Parquet/JSON files are generated analytical indexes and must not silently override source records.

## Planned datasets

- `properties.parquet` — one row per property.
- `scenarios.parquet` — one row per property + development strategy.
- `lots.parquet` — optional lot-level model when a scenario is detailed enough.
- `comps.parquet` — normalized land/lot/home comparable sales.
- `research_tasks.parquet` — unresolved/resolved research queue.
- `site-data.json` — browser-friendly generated dataset for the static dashboard.

Generated binary Parquet files may be produced by the build workflow rather than hand-edited in GitHub.

## Core analytical unit

The primary investment comparison is **Property + Development Scenario**, not property alone.

A single parcel may therefore have multiple rows in `scenarios.parquet`, such as:

- larger acreage lots,
- mid-size lots,
- smaller lots,
- mixed-size layout,
- raw-lot sales,
- improved-lot sales,
- phased vertical construction,
- presale/build-to-contract.

## Key scenario fields

Each scenario should capture when known:

- property_id
- scenario_id
- scenario_name
- lot_count
- lot_size_mix
- sale_product
- entitlement_status
- net_developable_acres
- acquisition_cost
- entitlement_cost
- infrastructure_cost
- vertical_build_cost
- soft_cost
- finance_carry_cost
- selling_cost
- contingency
- total_project_cost
- conservative_sellout_value
- expected_gross_profit
- profit_margin_on_cost
- minimum_upfront_capital
- peak_capital_at_risk
- return_on_cash
- capital_per_profit_dollar
- time_to_first_sale_months
- time_to_cash_recovery_months
- project_duration_months
- twenty_four_month_feasibility
- absorption_rating
- downside_sale_price_profit
- downside_cost_increase_profit
- maximum_land_basis
- preferred
- capital_efficient_preferred
- confidence
- last_updated

## Build philosophy

The generator should tolerate older property records with missing fields. Missing values remain null/unknown rather than being invented.
