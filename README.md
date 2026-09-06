# PropertyResearch

A Git-backed property research system designed for ChatGPT. It separates **property facts**, **buyer/use-case preferences**, and **portfolio rankings** so listings can be researched consistently and compared later.

The normal user experience is intentionally simple:

**Paste listing link → Property Investigator researches it → normalized Markdown is saved to GitHub → Property Portfolio compares it with everything else.**

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
  |-- properties/
  |-- reports/
        |
        v
Property Portfolio
        |
        v
Rank / Compare / Shortlist / Re-evaluate
```

### Separation of responsibilities

- **Property files = facts.** Listing history, acreage, taxes, broadband, zoning, access, OGM/mineral rights, house condition, market access, unresolved research, etc.
- **Persona files = preferences.** A persona can represent a person, household member, animal, business, lifestyle, or use case.
- **Reports = derived analysis.** Rankings and scores can be recalculated whenever a persona or property changes.
- **Chat = research notebook.** GitHub is the durable source of truth.

## Repository Structure

```text
PropertyResearch/
├── README.md
├── criteria.md
├── project-instructions.md
├── property-template.md
├── portfolio-rules.md
├── personas/
│   ├── active/
│   │   ├── nicholas.md
│   │   ├── brittany.md
│   │   ├── thomas.md
│   │   ├── dogs.md
│   │   ├── kell-and-son.md
│   │   ├── homestead.md
│   │   ├── firewood-lumber.md
│   │   └── resale-investment.md
│   └── inactive/
├── properties/
│   ├── WI/
│   ├── PA/
│   ├── OH/
│   └── ...
└── reports/
```

## ChatGPT Setup

Create **two ChatGPT Projects** and connect both to this GitHub repository.

### Project 1 — Property Investigator

Purpose: research **one property at a time**.

Recommended organization:

```text
PROPERTY INVESTIGATOR
├── 54170 Mount Zion Rd
├── N3328 Meade St
├── 213 E Turnpike Rd
└── ...
```

Create a **new chat for each property**. A bare Zillow/listing URL or property address is enough to start the workflow.

Suggested Project instructions:

```text
This Project researches individual real-estate listings.

When I provide a Zillow/listing URL or property address:

1. Read the current research framework from the PropertyResearch GitHub repository.
2. Follow criteria.md and project-instructions.md.
3. Read every persona in personas/active/.
4. Research the property using Zillow/listing data plus authoritative external sources.
5. Score every active persona.
6. Create or update the normalized property Markdown record in properties/<STATE>/.
7. Report the Property Card, fatal-flaw risks, major findings and important unknowns.

GitHub is the durable source of truth. Do not rely on prior chats for property facts when a current repository record exists.

A bare listing URL means: research this property using the full workflow.
```

The Investigator should research beyond the listing. Depending on the property, this can include GIS/parcel records, assessor/tax data, zoning, ordinances, broadband, wetlands/floodplain/soils, access, easements, OGM/mineral rights, utilities, sales/comps and market access.

### Project 2 — Property Portfolio

Purpose: compare **all researched properties**.

Unlike Investigator, Portfolio normally does **not** receive listing links. It reads the normalized records already stored in GitHub.

Create one main chat such as **Master Property Comparison**.

Suggested Project instructions:

```text
This Project compares and ranks researched properties.

The PropertyResearch GitHub repository is the authoritative property database.

For portfolio questions:

1. Read portfolio-rules.md.
2. Read every active persona in personas/active/.
3. Read the relevant property records under properties/.
4. Recalculate persona scores/rankings when criteria or personas have changed.
5. Compare properties using both intrinsic characteristics and effective cost-to-goal.
6. Never rank solely by one overall score.
7. Highlight fatal flaws, unresolved research items, price/value differences and properties dominated by better alternatives.

GitHub property records are the durable source of truth.
```

## Initialize the Portfolio

A useful first prompt in **Master Property Comparison** is:

```text
Read the current PropertyResearch GitHub repository, including portfolio-rules.md, all active personas, and every property record.

Build my current Master Property Portfolio.

For each property show:
- Price
- Total / usable / prime acreage
- Taxes
- Listing status
- Research confidence
- Fatal-flaw risks
- Every active persona score
- Effective cost when available
- Overall opportunity assessment

Then rank the properties overall and separately for each active persona.

Identify:
- Best overall opportunity
- Best value
- Best land value
- Best move-in-ready property
- Best long-term property
- Best business property
- Best homestead
- Best for each household persona
- Properties with unresolved dealbreakers
- The 5 most important unanswered research questions across the portfolio

Do not rely on previous conversation context for property facts. Use the current GitHub records as the source of truth.
```

After initialization, normal Portfolio prompts can be short:

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
Rank everything for Nicholas only.
```

```text
Which property is best for Thomas if a future homesite is a hard requirement?
```

```text
Which property gives me the most usable acreage per $100,000 of effective cost?
```

```text
Which properties should I eliminate?
```

```text
If Property A dropped to $475,000, how would the rankings change?
```

## Personas

Every `.md` file in `personas/active/` is an independent scoring lens. The system should discover them dynamically rather than hard-coding specific people.

Personas can represent almost anything:

- Individual household members
- Dogs/pets
- A business
- Homesteading
- Firewood/lumber operations
- Resale/investment
- Retirement
- Hunting/recreation
- Farming
- Any future use case

To deactivate a persona without losing it, move its Markdown file from:

```text
personas/active/
```

to:

```text
personas/inactive/
```

Move it back to reactivate it.

Persona scores are **derived data**. Changing a persona should allow the Portfolio to rescore existing properties without rewriting the underlying property facts.

## Adding a Persona

Use a structure similar to:

```markdown
---
name: Example Persona
type: person
a​​ctive: true
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
- Explain what should receive bonuses or penalties.
```

Weights within a persona should normally total 100. `default_weight` is for optional aggregate scenarios; individual persona scores should always remain visible.

## Property Records

Use `property-template.md` as the normalized format.

A property record should emphasize durable facts and clearly distinguish:

- **Confirmed** — supported by authoritative/current evidence
- **Listing Claim** — stated by seller/agent/MLS but not independently verified
- **Estimate** — reasoned planning estimate
- **Unknown** — unresolved; never assume favorable

Important concepts include:

### Land

Do not equate acreage with value:

**Total Acres → Constrained Acres → Usable Acres → Prime/Operational Acres**

### Cost-to-Goal

Do not simply penalize missing features:

**Purchase Price + Required Improvements + Desired Improvements = Effective Property Cost**

Classify important features as:

**Existing / Easy Value-Add / Major Value-Add / Difficult / Impossible**

Always distinguish **“doesn't have it” from “can't have it.”**

### Fatal Flaws

A high numeric score should not hide a hard failure. Examples include:

- Inadequate wired broadband where it is required
- No satisfactory legal access
- Zoning that prohibits the intended use
- Severe land constraints
- Unacceptable deed/HOA restrictions
- OGM/surface-right conflicts
- Uninhabitable house or impractical homesite

Use **CLEAR / INVESTIGATE / FAIL** before relying on the final score.

## Research Lifecycle

A property record is not necessarily finished after the first pass. Revisit it when:

- Price changes
- Listing status changes
- It goes under contract or returns to market
- Broadband availability changes
- New zoning/access/OGM/title information is found
- Inspection/disclosure information becomes available
- Another property changes its relative attractiveness

Unresolved items should remain explicit so the next research pass knows exactly what still needs verification.

## Recommended Daily Workflow

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
6. Continue property-specific due diligence in that chat if needed
        ↓
7. Open Property Portfolio
        ↓
8. Say "Update the rankings"
        ↓
9. Compare / shortlist / eliminate
```

## Optional Portfolio Report

The Portfolio can maintain a generated summary at:

```text
reports/portfolio.md
```

This should be treated as a **snapshot**, not the authoritative property database. It can contain the current leaderboard, persona winners, unresolved dealbreakers and shortlist. Rankings should still be recalculated from current property/persona files when needed.

## Design Principles

1. **Portable:** The system should work for properties in any U.S. state.
2. **Evidence-driven:** Research beyond listing claims.
3. **Persona-driven:** Different people/use cases can legitimately score the same property very differently.
4. **Facts separate from preferences:** Property records should survive changes in buyer priorities.
5. **Permanent characteristics matter most:** Location, usable land, access, zoning, broadband, rights and restrictions generally matter more than easy cosmetic improvements.
6. **Unknown is not favorable:** Missing evidence lowers confidence.
7. **GitHub is durable:** Chats are working sessions; Markdown is the reusable dataset.
8. **Keep adoption simple:** A new user should be able to connect the repo, create the two Projects, and start by pasting a listing URL.
