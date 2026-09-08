# PropertyResearch

A Git-backed property due-diligence and decision system for ChatGPT. It separates **property facts**, **supporting evidence**, **personas**, **buyer finance**, **benchmarks**, **research backlog**, and **portfolio rankings** so properties can be researched once and compared repeatedly.

## The Workflow

```text
Listing / Zillow URL
        ↓
PROPERTY INVESTIGATOR
Initial due diligence + hero photo + parcel map
        ↓
GitHub property record + supporting assets
        ↓
PROPERTY RESEARCHER
Closes unresolved questions / verifies dealbreakers
        ↓
PROPERTY PORTFOLIO
Ranks / compares / finances / shortlists
```

GitHub is the durable source of truth. Chats are working sessions.

## Repository Structure

```text
PropertyResearch/
├── README.md
├── criteria.md
├── project-instructions.md          # Investigator rules
├── researcher-instructions.md       # Research Worker rules
├── portfolio-rules.md               # Portfolio rules
├── property-template.md
├── asset-manifest-template.md
│
├── benchmarks/
│   └── active/                      # Current-home/reference benchmarks
├── personas/
│   ├── active/
│   └── inactive/
├── finance/
│   ├── buyer-finance.md
│   └── scenarios/
├── properties/
│   └── <STATE>/
│       └── <property-slug>/
│           ├── property.md
│           ├── assets.md
│           └── assets/
│               ├── documents/
│               ├── images/
│               └── notes/
└── reports/
    ├── research-queue.md
    └── portfolio.md                 # optional/generated
```

Legacy flat property records at `properties/<STATE>/<property>.md` remain supported and can migrate lazily when materially updated or when assets are added.

# Three ChatGPT Projects

## 1. Property Investigator

**Purpose:** ingest one new property at a time.

Create a new chat for each property and paste a Zillow/listing URL or address. A bare URL means run the full workflow.

Investigator should:
- read `criteria.md`, `project-instructions.md`, active personas, benchmarks and finance assumptions;
- show the actual listing hero photo when available;
- show an authoritative satellite/aerial parcel view with boundary when reliable geometry is available, labeled **PARCEL MAP — NOT A SURVEY**;
- research listing status including active-offer status, broadband, land, zoning, access, rights, taxes, house/homesite, utilities, market access, resale/development, value and finance;
- provide a neighboring **BROADBAND LOOKUP PROXY — NOT THE PROPERTY ADDRESS** for vacant/no-address parcels when useful;
- explicitly warn where OGM/mineral rights should not be assumed to convey and assess practical Rights Disturbance Risk;
- compare market trajectory/liquidity with the active current-home benchmark;
- score every active persona and estimate Financial Fit when data allows;
- create/update the property record and its Open Research Tasks.

Suggested Project instruction:

```text
This Project researches new individual real-estate listings.
Read criteria.md and project-instructions.md from the connected PropertyResearch GitHub repository, plus all active personas, benchmarks and finance assumptions. A bare listing URL means run the full Investigator workflow. Create/update the normalized property record in GitHub and leave explicit prioritized Open Research Tasks for anything unresolved. GitHub is the durable source of truth.
```

## 2. Property Researcher

**Purpose:** close unanswered questions across properties already in the repo.

This is the backfill/deep-research worker. It should not superficially redo every property. It reads `researcher-instructions.md`, scans unresolved tasks, prioritizes dealbreakers, researches a manageable batch thoroughly, updates the property records, and maintains `reports/research-queue.md`.

Suggested Project instruction:

```text
This Project is the Property Researcher for the connected PropertyResearch GitHub repository.

Always read researcher-instructions.md first and follow it as authoritative. Read criteria.md, active personas, benchmarks, finance assumptions, property records, and relevant property assets as needed.

When I say "Research backlog", scan all property records, prioritize unresolved P0 then P1 then P2/P3 tasks, deeply research a reasonable batch, update the authoritative property records with findings/sources/confidence, mark tasks RESOLVED/PARTIALLY RESOLVED/BLOCKED/STALE as appropriate, flag RESCORE REQUIRED when material facts change, and update reports/research-queue.md.

Never guess to close a task. If public research cannot resolve it, mark it BLOCKED and state the exact human/external action required.
```

Useful commands:

```text
Research backlog
Research P0 only
Research 3780A Hurricane Creek Rd
Research top contenders
Refresh 54170 Mount Zion Rd
```

### Research Priority

- **P0 — Dealbreaker:** could make the property unsuitable or materially impair title/use/financing.
- **P1 — Decision-critical:** materially affects value, score or cost-to-goal.
- **P2 — Important refinement:** improves confidence/comparison.
- **P3 — Nice-to-know:** useful but unlikely to change the decision.

Task outcomes are **RESOLVED / PARTIALLY RESOLVED / BLOCKED / STALE-RECHECK**. BLOCKED items should identify exactly what is needed: title commitment, seller disclosure, survey, inspection, ISP construction quote, zoning administrator interpretation, attorney review, etc. The Researcher should not endlessly retry blocked questions.

### Research Status

Property records can use:

```text
INITIAL
NEEDS_RESEARCH
DEEP_RESEARCH
MOSTLY_VERIFIED
VERIFIED
BLOCKED
```

`reports/research-queue.md` is a generated operational dashboard; individual property records remain authoritative.

## 3. Property Portfolio

**Purpose:** compare researched properties rather than ingest new listings.

Portfolio reads `portfolio-rules.md`, all active personas, benchmarks, finance assumptions and relevant property records/assets. It recalculates derived scores when facts or preferences change.

Suggested Project instruction:

```text
This Project compares and ranks researched properties in the connected PropertyResearch GitHub repository. Read portfolio-rules.md, every active persona, active benchmarks, buyer finance/scenarios, and relevant property records. Recalculate persona scores, Financial Fit and rankings when inputs change. Compare intrinsic quality, fatal flaws, Effective Property Cost, Cash to Goal, monthly carry, market trajectory/liquidity, development optionality and capital allocation. Never rank solely by one overall score. GitHub is the durable source of truth.
```

Typical commands:

```text
Update the rankings.
What's currently #1?
Compare Mount Zion against Hurricane Creek.
Which property is best for Thomas?
Which properties have unresolved dealbreakers?
Which is the best use of my home-sale proceeds?
Which properties are value traps?
```

# Property Assets / Evidence

Preferred property layout:

```text
properties/OH/54170-mount-zion-rd-pleasant-city-oh-43772/
├── property.md
├── assets.md
└── assets/
    ├── documents/
    │   ├── survey.pdf
    │   ├── deed.pdf
    │   └── seller-disclosure.pdf
    ├── images/
    │   ├── gis-parcel.png
    │   └── broadband-screenshot.png
    └── notes/
        └── agent-call.md
```

Use `asset-manifest-template.md` for `assets.md`. Appropriate evidence includes surveys/plats, deeds/title/OGM documents, disclosures, inspections, septic reports, GIS/FCC screenshots, your own property-tour photos, agent correspondence, contractor/ISP quotes and call notes.

Before externally researching an unresolved question, Investigator/Researcher should inspect relevant stored evidence. Strong user-provided primary evidence should not be overwritten by weaker web inference.

Public Zillow/MLS imagery should normally remain a URL/reference rather than being copied into GitHub. User-owned/received due-diligence documents can be stored if desired.

# Benchmarks

Benchmarks are reference properties/locations, not purchase candidates. The active current-home benchmark provides a baseline for:

- geographic distance;
- current housing payment/carry;
- estimated equity/home-sale proceeds;
- market trajectory and resale liquidity;
- population/employment direction;
- land scarcity/development pressure;
- taxes and infrastructure/economic catalysts.

This allows the system to explicitly identify when a candidate improves lifestyle but moves from a stronger/liquid market into a weaker one.

When the benchmark home eventually sells, retain it historically and add actual sale price/net proceeds rather than deleting it.

# Finance Layer

Finance is separate from personas and property facts.

Configure `finance/buyer-finance.md` with expected home-sale proceeds, cash outside the sale, reserve requirements, down-payment preferences, target/max monthly housing cost, loan term, improvement-capital target and closing-cost reserve.

Important metrics:

**Gross Equity = Sale Price − Mortgage Payoff**

**Net Spendable Proceeds = Gross Equity − Selling Costs / Concessions / Closing Obligations**

**Effective Property Cost = Purchase Price + Required Improvements + Desired Improvements**

**Cash to Goal = Cash required before the property reaches the selected acceptable/desired state**

**Housing Cost Delta = Candidate Monthly Carry − Current Benchmark Monthly Carry**

Do not assume all sale proceeds should become down payment. Compare larger down payment against retaining capital for high-value improvements/reserves. Equity and liquid cash are different resources.

# Personas

Every `.md` file in `personas/active/` is an independent scoring lens. Personas may represent people, pets, businesses, homesteading, lumber/firewood, investment/resale or other use cases. Move a persona to `personas/inactive/` to retain it without scoring it.

The Resale/Development lens should consider **Market Trajectory**, **Resale Liquidity**, **Development Optionality**, **Value Trap Risk** and **Growth Tailwind**. A cheap property in a structurally weak/illiquid market should not automatically score as good value.

# Property Research Standards

Always distinguish **Confirmed / Listing Claim / Estimate / Unknown**. Unknown is never assumed favorable.

Permanent characteristics generally deserve more weight than easy cosmetic changes: usable land, location, legal access, zoning, broadband, wetlands/topography, privacy, rights/restrictions, taxes, market trajectory and market access.

Land should be modeled as:

**Total Acres → Constrained Acres → Usable Acres → Prime/Operational Acres**

Missing features should be classified:

**Existing / Easy Value-Add / Major Value-Add / Difficult / Impossible**

Always distinguish **“doesn't have it” from “can't have it.”**

# Research Lifecycle

A property is not finished after the initial Investigator pass. Revisit it when:

- unresolved P0/P1 tasks remain;
- price/listing/offer status changes;
- broadband deployment changes;
- zoning/access/OGM/title evidence changes;
- disclosures, surveys or inspections arrive;
- finance assumptions/current-home sale become firmer;
- market trajectory or permits materially change;
- another property changes its relative attractiveness.

Recommended operating loop:

```text
Find property
    ↓
Investigator: ingest + initial research
    ↓
Researcher: close uncertainty
    ↓
Portfolio: compare/rank
    ↓
New evidence / price / status
    └──────────────→ Researcher / Portfolio refresh
```

# Automation

Once the Researcher has been tested manually, it can be scheduled to run periodically. A good default is nightly because most due-diligence facts do not change hourly.

A scheduled run should instruct the Researcher to work the highest-priority unresolved tasks, update property records and `reports/research-queue.md`, and avoid repeatedly retrying BLOCKED items.

Suggested automation prompt:

```text
Read researcher-instructions.md in the PropertyResearch GitHub repository. Run the Research backlog workflow against the highest-priority unresolved questions. Work a reasonable batch thoroughly, prioritize P0 before P1/P2/P3, update authoritative property records with findings and sources, mark unresolved non-public items BLOCKED with the required next action, flag RESCORE REQUIRED when material facts change, and update reports/research-queue.md. Report only meaningful completed work, new risks/opportunities, blocked actions and the next highest priorities.
```

# Adoption / Clean Fork

A new adopter should keep the reusable framework and replace personal data.

```text
KEEP / REUSE
├── README.md
├── criteria.md
├── project-instructions.md
├── researcher-instructions.md
├── portfolio-rules.md
├── property-template.md
├── asset-manifest-template.md
└── finance/scenarios/

REPLACE / RESET
├── benchmarks/
├── personas/
├── finance/buyer-finance.md
├── properties/
└── reports/
```

Clean-fork prompt:

```text
I forked this PropertyResearch repository for my own use. Preserve the reusable framework and finance scenario files, but remove/reset the previous user's personal data: benchmarks, persona files, buyer-finance values, property records and generated reports. Preserve the directory structure. Then help me create my own personas, benchmark and finance profile.
```

Review destructive changes before authorizing them.

# Design Principles

1. **Portable:** work for properties in any U.S. state.
2. **Evidence-driven:** research beyond listing claims.
3. **Visual:** use the actual listing hero photo and authoritative parcel/aerial context when available.
4. **Evidence-preserving:** store relevant due-diligence documents with the property.
5. **Persona-driven:** different people/use cases can score the same property differently.
6. **Finance-aware:** model payment, equity, cash, reserves and improvement capital.
7. **Exit-aware:** consider resale liquidity, economic trajectory and development optionality.
8. **Uncertainty-aware:** unanswered questions become prioritized research tasks rather than optimistic assumptions.
9. **GitHub is durable:** property facts/evidence survive individual chats.
10. **Automatable:** Researcher can systematically reduce uncertainty across a growing portfolio.
