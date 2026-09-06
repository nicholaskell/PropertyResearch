# PropertyResearch

A Git-backed property research system designed for ChatGPT. It separates **property facts**, **buyer/use-case preferences**, **buyer finance assumptions**, and **portfolio rankings** so listings can be researched consistently and compared later.

The normal user experience is intentionally simple:

**Paste listing link → Property Investigator researches it → normalized Markdown is saved to GitHub → Property Portfolio compares it with everything else, including realistic financing/capital allocation.**

## Architecture

```text
Listing / Zillow URL
        |
        v
Property Investigator
        |
        | due diligence + normalized facts
        v
GitHub PropertyResearch
  |-- criteria.md
  |-- personas/
  |-- finance/
  |-- properties/
  |-- reports/
        |
        v
Property Portfolio
        |
        v
Rank / Compare / Finance / Shortlist / Re-evaluate
```

### Separation of responsibilities

- **Framework files = reusable system.** Research rules, templates, Project instructions and portfolio logic.
- **Property files = user data/facts.** Listing history, acreage, taxes, broadband, zoning, access, OGM/mineral rights, house condition, market access, unresolved research, etc.
- **Persona files = user preferences.** A persona can represent a person, household member, animal, business, lifestyle, or use case.
- **Finance files = buyer financial assumptions.** Home-sale proceeds, down-payment preferences, reserves, target payment and capital-allocation scenarios.
- **Reports = derived user analysis.** Rankings, persona scores and Financial Fit can be regenerated whenever a persona, property or finance assumption changes.
- **Chat = research notebook.** GitHub is the durable source of truth.

## Repository Structure

```text
PropertyResearch/
├── README.md                 # KEEP — setup/adoption documentation
├── criteria.md               # KEEP — reusable research framework
├── project-instructions.md   # KEEP — Investigator behavior
├── property-template.md      # KEEP — normalized property schema
├── portfolio-rules.md        # KEEP — comparison framework
│
├── personas/                 # PERSONALIZE
│   ├── active/               # Personas currently scored
│   └── inactive/             # Saved personas excluded from scoring
│
├── finance/                  # PERSONALIZE
│   ├── buyer-finance.md      # Sale proceeds, reserves, payment targets, etc.
│   └── scenarios/
│       ├── conservative.md
│       ├── balanced.md
│       └── aggressive.md
│
├── properties/               # USER DATA — researched properties
│   ├── WI/
│   ├── PA/
│   ├── OH/
│   └── ...
│
└── reports/                  # GENERATED USER DATA
```

# Quick Start for a New User

If you are adopting/forking this repository from someone else, **do not use their property records, personas or finance assumptions as if they were yours**.

The reusable framework and the original user's data are intentionally separated.

## Keep These Framework Files

Keep these files when making the repository your own:

```text
README.md
criteria.md
project-instructions.md
property-template.md
portfolio-rules.md
finance/scenarios/conservative.md
finance/scenarios/balanced.md
finance/scenarios/aggressive.md
```

The finance scenario files are reusable logic. The actual numbers in `finance/buyer-finance.md` are personal and should be replaced.

## Delete the Previous User's Property Data

Delete the contents of:

```text
properties/
```

Keep the `properties/` directory itself. New state directories will be created as you research properties.

## Delete or Replace the Previous User's Personas

Delete the previous user's persona `.md` files from:

```text
personas/active/
personas/inactive/
```

Then create your own personas. You may intentionally retain a previous persona as a template, but do not assume its priorities apply to you.

## Replace the Previous User's Finance Profile

Replace the personal values in:

```text
finance/buyer-finance.md
```

Do not copy another buyer's sale proceeds, reserve requirements, down-payment targets or monthly-payment limits.

## Delete Generated Reports

Delete generated files under:

```text
reports/
```

Reports are derived from the previous user's properties, personas and finance assumptions.

## Clean-Fork Rule

```text
KEEP / REUSE
├── README.md
├── criteria.md
├── project-instructions.md
├── property-template.md
├── portfolio-rules.md
└── finance/scenarios/

REPLACE WITH YOUR OWN
├── personas/
├── finance/buyer-finance.md
├── properties/
└── reports/
```

## Ask ChatGPT to Clean a Fork

```text
I forked this PropertyResearch repository for my own use.

Preserve the reusable framework and finance scenario files, but remove or reset the previous user's personal data:
- Delete all property records under properties/
- Delete all generated reports under reports/
- Delete all persona .md files under personas/active/ and personas/inactive/
- Reset finance/buyer-finance.md so no previous user's personal finance numbers remain
- Preserve README.md, criteria.md, project-instructions.md, property-template.md, portfolio-rules.md and finance/scenarios/
- Preserve the directory structure

Then help me create my own active personas and buyer finance profile.
```

Review requested deletions before authorizing them.

# ChatGPT Setup

Create **two ChatGPT Projects** and connect both to this GitHub repository.

## Project 1 — Property Investigator

Purpose: research **one property at a time**.

Create a **new chat for each property**. A bare Zillow/listing URL or property address is enough to start the workflow.

Suggested Project instructions:

```text
This Project researches individual real-estate listings.

When I provide a Zillow/listing URL or property address:

1. Read the current research framework from the PropertyResearch GitHub repository.
2. Follow criteria.md and project-instructions.md.
3. Read every persona in personas/active/.
4. Read finance/buyer-finance.md and active finance scenarios when populated.
5. Research the property using Zillow/listing data plus authoritative external sources.
6. Score every active persona.
7. When enough finance data exists, estimate Financial Fit, Cash to Goal, realistic payment and useful down-payment/improvement-capital structures.
8. Create or update the normalized property Markdown record in properties/<STATE>/.
9. Report the Property Card, fatal-flaw risks, major findings and important unknowns.

GitHub is the durable source of truth. Do not rely on prior chats for property facts when a current repository record exists.

A bare listing URL means: research this property using the full workflow.
```

The Investigator should research beyond the listing. Depending on the property, this can include GIS/parcel records, assessor/tax data, zoning, ordinances, broadband, wetlands/floodplain/soils, access, easements, OGM/mineral rights, utilities, sales/comps and market access.

## Project 2 — Property Portfolio

Purpose: compare **all researched properties** and model realistic purchase structures.

Unlike Investigator, Portfolio normally does **not** receive listing links. It reads the normalized records already stored in GitHub.

Suggested Project instructions:

```text
This Project compares and ranks researched properties.

The PropertyResearch GitHub repository is the authoritative property database.

For portfolio questions:

1. Read portfolio-rules.md.
2. Read every active persona in personas/active/.
3. Read finance/buyer-finance.md and active files under finance/scenarios/.
4. Read the relevant property records under properties/.
5. Recalculate persona scores, Financial Fit and rankings when personas, finance assumptions or properties change.
6. Compare properties using intrinsic characteristics, effective cost-to-goal, Cash to Goal, monthly carry and capital allocation.
7. Never rank solely by one overall score.
8. Highlight fatal flaws, unresolved research items, price/value differences and properties dominated by better alternatives.

GitHub property records are the durable source of truth.
```

# Finance Layer

The finance layer answers a different question than personas:

- **Personas:** Who/what likes this property and why?
- **Finance:** Can the purchase be structured sensibly, and where should available capital go?

Configure:

```text
finance/buyer-finance.md
```

Typical inputs include:

- Conservative / expected / optimistic net home-sale proceeds
- Cash available outside the sale
- Minimum cash reserve
- Preferred and maximum down payment
- Target and maximum monthly housing cost
- Loan term
- Improvement-capital target
- Closing-cost reserve

Until the current home sale is complete, use three sale-proceeds scenarios rather than pretending the final number is known.

## Financial Metrics

**Effective Property Cost = Purchase Price + Required Improvements + Desired Improvements**

**Cash to Goal = Cash required before the property reaches the selected acceptable/desired state**

These are intentionally different. A lower-priced property can require more cash if it needs a large shop, road, well/septic, fencing or other improvements.

## Capital Allocation

For serious contenders, compare alternatives such as:

```text
More down payment
vs.
Retain cash for shop/improvements
vs.
Buy the more expensive property with the feature already built
```

Do not assume all home-sale proceeds should become down payment.

A useful question for Portfolio is:

```text
Where does the next $50,000 or $100,000 create the most value across my current contenders: additional down payment, retained reserves, or specific improvements?
```

Track cash and equity separately. Down payment creates equity, but equity is not the same thing as liquid cash. Future HELOC/home-equity borrowing can be modeled as an optional strategy, never assumed as guaranteed or preferable.

## Financial Fit

Financial Fit is a **derived score/assessment, not a persona**. It should consider:

- Estimated monthly payment versus target/max
- Cash required at closing
- Reserve remaining after closing
- Immediate improvement capital
- Effective Property Cost
- Cash to Goal
- Taxes, insurance and carrying costs
- Financing flexibility
- Value/equity cushion

If finance inputs are incomplete, report **Not Yet Scored** rather than inventing numbers.

# Initialize the Portfolio

A useful first prompt in **Master Property Comparison** is:

```text
Read the current PropertyResearch GitHub repository, including portfolio-rules.md, all active personas, finance/buyer-finance.md, active finance scenarios and every property record.

Build my current Master Property Portfolio.

For each property show:
- Price
- Total / usable / prime acreage
- Taxes
- Listing status
- Research confidence
- Fatal-flaw risks
- Every active persona score
- Effective Property Cost
- Cash to Goal
- Estimated monthly carry when finance inputs allow
- Financial Fit
- Overall opportunity assessment

Rank the properties overall and separately for each active persona.

Also identify:
- Best overall opportunity
- Best Financial Fit
- Best value
- Best land value
- Best move-in-ready property
- Best long-term property
- Best business property
- Best homestead
- Best for each household persona
- Best use of available home-sale proceeds
- Properties with unresolved dealbreakers
- The 5 most important unanswered research questions across the portfolio

Do not rely on previous conversation context for property facts. Use the current GitHub records as the source of truth.
```

After initialization, useful Portfolio prompts include:

```text
Update the rankings.
```

```text
What's currently #1?
```

```text
Compare Mount Zion against Meade.
```

```text
Which property gives me the most usable acreage per $100,000 of effective cost?
```

```text
If my net home-sale proceeds are $150,000, how should I structure each of my top three purchases?
```

```text
For this property, compare $50k down + $100k shop versus $150k down and financing the shop later.
```

```text
Which property leaves me with the strongest cash reserve after reaching my target setup?
```

# Personas

Every `.md` file in `personas/active/` is an independent scoring lens. The system should discover them dynamically rather than hard-coding specific people.

Personas can represent household members, pets, businesses, homesteading, firewood/lumber, investment, retirement, recreation, farming or any future use case.

To deactivate a persona without losing it, move its Markdown file from `personas/active/` to `personas/inactive/`. Move it back to reactivate it.

Persona scores are **derived data**. Changing a persona should allow Portfolio to rescore existing properties without rewriting underlying property facts.

## Adding a Persona

```markdown
---
name: Example Persona
type: person
active: true
default_weight: 0.7
status: rough-draft
---

# Example Persona

## Hard Requirements
- Requirement that can cause a property to fail.

## Priorities
| Factor | Weight |
|---|---:|
| Important Factor | 30 |
| Another Factor | 20 |
| Other Factors | 50 |

## Evaluation Notes
- Explain how ambiguous situations should be judged.
```

Weights within a persona should normally total 100. `default_weight` is for optional aggregate scenarios; individual persona scores should always remain visible.

# Property Records

Use `property-template.md` as the normalized format.

A property record should emphasize durable facts and clearly distinguish:

- **Confirmed** — supported by authoritative/current evidence
- **Listing Claim** — stated by seller/agent/MLS but not independently verified
- **Estimate** — reasoned planning estimate
- **Unknown** — unresolved; never assume favorable

## Land

Do not equate acreage with value:

**Total Acres → Constrained Acres → Usable Acres → Prime/Operational Acres**

## Cost-to-Goal

Classify important features as:

**Existing / Easy Value-Add / Major Value-Add / Difficult / Impossible**

Always distinguish **“doesn't have it” from “can't have it.”**

## Fatal Flaws

A high numeric score should not hide a hard failure. Examples include inadequate wired broadband, no satisfactory legal access, prohibited intended use, severe land constraints, unacceptable restrictions, OGM/surface-right conflicts, or an impractical house/homesite.

Use **CLEAR / INVESTIGATE / FAIL** before relying on the final score.

# Research Lifecycle

Revisit a property when price/listing status changes, broadband changes, new zoning/access/OGM/title information appears, inspection/disclosure information becomes available, finance assumptions materially change, the current home sale becomes more certain, or another property changes its relative attractiveness.

# Recommended Daily Workflow

```text
1. Find interesting listing
        ↓
2. Open Property Investigator
        ↓
3. Start new property chat
        ↓
4. Paste URL
        ↓
5. Investigator researches + writes GitHub record
        ↓
6. Continue property-specific due diligence if needed
        ↓
7. Open Property Portfolio
        ↓
8. Say "Update the rankings"
        ↓
9. Compare / finance / shortlist / eliminate
```

# Optional Portfolio Report

The Portfolio can maintain a generated summary at:

```text
reports/portfolio.md
```

Treat it as a **snapshot**, not the authoritative property database.

# Design Principles

1. **Portable:** Work for properties in any U.S. state.
2. **Evidence-driven:** Research beyond listing claims.
3. **Persona-driven:** Different people/use cases can score the same property differently.
4. **Finance-aware:** Price alone is not affordability; model cash, payment, reserves and improvements.
5. **Facts separate from preferences and finance:** Property records survive changes in personas or buyer capital.
6. **Permanent characteristics matter most:** Location, usable land, access, zoning, broadband, rights and restrictions generally matter more than easy cosmetic improvements.
7. **Unknown is not favorable:** Missing evidence lowers confidence.
8. **GitHub is durable:** Chats are working sessions; Markdown is the reusable dataset.
9. **Keep adoption simple:** A new user should be able to fork/connect the repo, remove personal data, configure personas/finance, create the two Projects, and start by pasting a listing URL.
