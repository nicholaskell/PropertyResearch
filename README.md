# PropertyResearch

A Git-backed **land-development due-diligence and investment system** for ChatGPT. The current active strategy is to acquire land, determine the economically optimal subdivision, develop/build selectively, recycle capital through staged sales, and target realized profit in roughly **24 months** with **low upfront capital exposure**.

GitHub is the durable source of truth. Chats are working sessions. Markdown and supporting evidence remain authoritative; generated Parquet/JSON data and the static dashboard are analytical views.

## Current Workflow

```text
Listing / parcel
      ↓
PROPERTY INVESTIGATOR
Initial due diligence + development screening
      ↓
Property Markdown + evidence + development scenarios
      ↓
PROPERTY RESEARCHER
Closes entitlement / buildability / market / cost unknowns
      ↓
STRUCTURED DATA BUILD
Properties + scenarios → Parquet + JSON
      ↓
STATIC DEVELOPMENT DASHBOARD
Filter / compare / inspect portfolio
      ↓
PROPERTY PORTFOLIO
Ranks property + strategy combinations
```

## Repository Structure

```text
PropertyResearch/
├── README.md
├── criteria.md
├── project-instructions.md
├── researcher-instructions.md
├── portfolio-rules.md
├── property-template.md
├── development-scenario-template.md
├── asset-manifest-template.md
├── requirements-build.txt
│
├── personas/
│   ├── active/
│   │   └── land-development.md      # sole active investment lens
│   └── inactive/                    # retained former lifestyle/business personas
├── benchmarks/
├── finance/
├── properties/
│   └── <STATE>/
│       └── <property-slug>/
│           ├── property.md
│           ├── assets.md
│           ├── scenarios/           # first-class development alternatives
│           │   ├── acreage-lots.md
│           │   ├── one-acre-lots.md
│           │   └── phased-build.md
│           └── assets/
├── data/
│   ├── README.md
│   └── generated/
│       ├── properties.parquet
│       ├── scenarios.parquet
│       └── site-data.json
├── scripts/
│   └── build_data.py
├── site/
│   ├── index.html
│   └── site-data.json
├── reports/
│   └── research-queue.md
└── .github/workflows/
    └── build-dashboard.yml
```

Legacy flat property records at `properties/<STATE>/<property>.md` remain supported and can migrate lazily.

# Investment Objective

The active `Land Development / Build-to-Sell` persona evaluates each property for **capital-efficient realized profit**, not lifestyle fit and not maximum lot count.

Core preferences:

- roughly **24 months acquisition-to-realized-profit**;
- **less upfront capital is better**;
- optimize lot size for the actual local market;
- compare multiple subdivision/product scenarios;
- favor existing road frontage and lower infrastructure burden;
- favor staged lot sales, presales and one-at-a-time builds that recycle capital;
- distinguish highest theoretical profit from the **best capital-efficient strategy**;
- preserve multiple exits if the original plan changes.

A 10-acre parcel might rationally become two 5-acre homesites, four 2-acre lots, several ~1-acre lots, a mixed layout, or remain whole. The system should determine which configuration produces the best combination of return on cash, profit, marketability, absorption and execution risk.

# Development Scenarios Are First-Class Records

The primary analytical unit is now:

**Property + Development Strategy**

Use `development-scenario-template.md` for serious alternatives. A property may have several scenarios under `scenarios/`.

Each scenario should model land yield, entitlement, product, revenue, infrastructure, construction, soft/carry/selling costs, minimum upfront capital, peak capital at risk, time to first sale, cash recovery, total duration, profit, return on cash, residual land value and downside sensitivity.

For serious candidates identify both:

- **Highest Expected Profit Strategy**
- **Best Capital-Efficient Strategy**

If they differ, explain the tradeoff. The capital-efficient strategy is normally preferred unless the additional return from the higher-capital strategy clearly compensates for the extra risk/cash exposure.

## Residual Land Value

A core acquisition metric is:

**Maximum Land Basis = Conservative Sellout Value − All Development / Construction / Selling / Finance / Carry Costs − Required Developer Profit**

A parcel can be excellent development land and still be a poor acquisition at the asking price.

# Structured Data / Parquet

`data/` is a generated analytical layer. Markdown remains authoritative.

`scripts/build_data.py` scans property/scenario Markdown and produces:

- `properties.parquet` — property-level screening/index data;
- `scenarios.parquet` — property + development strategy rows;
- `site-data.json` — browser-friendly dashboard data.

The generator intentionally tolerates older/incomplete records. Missing data remains null/unknown rather than being invented.

Parquet makes portfolio questions much easier, including:

- which scenarios plausibly finish inside 24 months;
- which require the least peak capital;
- highest return on cash;
- strongest expected profit below a capital ceiling;
- which asking prices are below residual land value;
- which lot-size strategies outperform alternatives on the same parcel.

# Static Development Dashboard

`site/index.html` is a dependency-light static dashboard. It reads `site/site-data.json` and displays a sortable/filterable development portfolio including asking price, acreage, preferred strategy, lot yield, residual land value, minimum upfront capital, peak capital, projected profit, margin and 24-month feasibility.

The dashboard is deliberately static: no application server or database server is required.

It can be hosted later with GitHub Pages or another static host. The repository currently contains the site/build files; publishing/Pages configuration is a separate repository setting.

# Automatic Build

`.github/workflows/build-dashboard.yml` runs the structured-data generator after relevant changes on `main` and can also be triggered manually. It installs the small build dependency set in `requirements-build.txt`, generates Parquet/JSON, and commits changed generated data back to the repository.

If repository Actions permissions prevent workflow commits, enable the repository's GitHub Actions workflow write permission or change the deployment approach. Do not treat a failed generated-data build as loss of authoritative research; Markdown records remain intact.

# Property Investigator

**Purpose:** ingest and initially screen one property/listing at a time.

Investigator should read `criteria.md`, `project-instructions.md`, the sole active development persona, relevant benchmark/finance assumptions and the scenario template. For a promising parcel it should research:

- parcel identity/boundary and legal access;
- zoning, density, minimum lot size/frontage and subdivision process;
- minor vs major subdivision thresholds;
- septic/perc/well/sewer feasibility;
- road, driveway, utility, drainage and sitework burden;
- wetlands/flood/topography/soils;
- deed/easement/OGM/surface-right restrictions;
- local raw/improved lot and finished-home comps;
- what lot sizes/products actually sell;
- absorption/DOM/new-construction competition;
- barndo/conventional/house+garage acceptance where relevant;
- residual land value;
- minimum upfront/peak capital;
- likely time to first sale and 24-month feasibility.

A bare listing URL means run the full Investigator workflow and create/update the normalized GitHub record with prioritized Open Research Tasks.

# Property Researcher

The Researcher closes unanswered questions across existing properties. It prioritizes P0 dealbreakers and P1 decision-critical issues, uses authoritative evidence, marks tasks RESOLVED/PARTIALLY RESOLVED/BLOCKED/STALE, and updates `reports/research-queue.md`.

For the development strategy, especially prioritize unresolved questions that could change:

- legal lot yield;
- septic/buildability;
- infrastructure burden;
- marketable lot-size mix;
- finished product value;
- residual land value;
- peak capital requirement;
- 24-month feasibility.

Never guess to close a task. Non-public dependencies should be marked BLOCKED with the exact required human/external action.

# Property Portfolio

Portfolio should compare **property + scenario combinations**, not merely properties.

Important portfolio metrics include:

- Development Score
- realistic saleable lot yield
- entitlement status
- best lot-size mix
- best product
- asking price vs maximum land basis
- conservative sellout value
- total project cost
- expected gross profit
- margin on cost
- minimum practical upfront capital
- peak capital at risk
- return on cash
- capital required per $1 expected profit
- time to first sale
- time to recover initial cash
- base-case duration
- 24-month feasibility
- absorption risk
- downside sensitivity
- exit flexibility

Do not rank solely by gross profit. A smaller project with faster capital recovery and much lower peak cash exposure may be the superior investment.

# Property Assets / Evidence

Preferred property structure preserves surveys/plats, deeds/title/OGM material, disclosures, septic/perc reports, GIS/FCC evidence, property-tour photos, correspondence, quotes and call notes. `assets.md` indexes supporting evidence.

Before externally researching an unresolved question, inspect relevant stored evidence. Strong primary evidence should not be overwritten by weaker inference.

# Research Standards

Always distinguish **Confirmed / Listing Claim / Estimate / Unknown**. Unknown is never assumed favorable.

For subdivision analysis explicitly distinguish:

**Gross Acres → Constrained Acres → Net Developable Acres → Theoretical Lots → Realistic Saleable Lots**

Never infer that minimum zoning lot size equals practical lot yield. Frontage, roads, drainage, septic reserve areas, utilities, topography, wetlands, access and marketability can materially reduce yield.

Development cost estimates must include appropriate entitlement, survey/engineering, infrastructure/sitework, utilities, vertical construction when applicable, soft costs, finance/carry, selling costs and contingency.

# Research Lifecycle

```text
Find parcel
   ↓
Investigator: screen + initial development concepts
   ↓
Researcher: verify yield / costs / market / entitlement
   ↓
Scenario models: compare alternatives
   ↓
Data build: Parquet + JSON
   ↓
Dashboard / Portfolio: compare capital-efficient opportunities
   ↓
New evidence / price / status / comp
   └──────────────→ refresh analysis
```

# Design Principles

1. **Profit-oriented:** evaluate realized investment return, not nominal acreage or maximum lot count.
2. **Capital-efficient:** minimize upfront and peak cash exposure when returns are otherwise attractive.
3. **Time-bounded:** target a roughly 24-month acquisition-to-profit cycle.
4. **Market-driven:** optimize lot size/product for actual buyer demand and absorption.
5. **Evidence-driven:** research beyond listing claims.
6. **Scenario-driven:** compare multiple plausible development strategies.
7. **Exit-aware:** preserve staged sales and alternative exits.
8. **Uncertainty-aware:** unresolved questions become explicit research tasks.
9. **Structured + readable:** Markdown for authoritative research; Parquet/JSON for analytics.
10. **Static-first:** dashboard should remain useful without maintaining an application server.
11. **GitHub durable:** property facts/evidence survive individual chats and generated-data rebuilds.
