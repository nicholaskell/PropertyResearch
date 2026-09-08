# Property Research Criteria

## Goal

Find rural/semi-rural U.S. properties that provide the best long-term combination of usable land, buildability, broadband, privacy, house/homesite quality, carrying cost, market access, resale/development outlook and value.

This file defines **property research**, not individual preferences. Persona-specific priorities and scoring live in `personas/active/`.

Always distinguish **Confirmed / Listing Claim / Estimate / Unknown**. Never assume unknowns are favorable.

## Fatal-Flaw Screen

Research and classify material risks such as **CLEAR / INVESTIGATE / FAIL** where appropriate:

- Wired broadband
- Legal/practical access
- Buildability/zoning
- Severe wetlands/flood/topography/soil constraints
- HOA/deed/private restrictions
- House habitability or homesite feasibility
- OGM/mineral/surface-right conflicts where relevant
- Unreasonable carrying costs
- Severe resale/liquidity risk caused by structural local decline or an exceptionally thin buyer pool
- Any property-specific hard constraint

A persona may define additional hard requirements.

## Required Research

Use current listing/MLS-fed sources and authoritative public sources where available. Evaluate:

- Listing/offer status, price history, DOM, prior sales, assessment and taxes.
- Broadband: FCC + ISP availability, speed/technology, fiber location, expansion and extension potential.
- Land: parcel configuration, total/constrained/usable/prime usable acres, topography, wetlands, floodplain, soils, drainage, bedrock, streams, setbacks and septic suitability.
- Access: frontage, public/private/deeded access, maintenance agreements, driveway and equipment/construction access.
- Zoning/buildability: accessory buildings, agricultural uses, home business, outdoor storage, firewood processing, sawmilling and other relevant uses.
- Animals: applicable dog/kennel and livestock/poultry rules.
- Rights/restrictions: HOA, covenants, easements, ROW, private roads and, where relevant, oil/gas/mineral/coal/timber/surface rights, leases, wells and pipelines.
- Taxes: current taxes, reassessment risk, special assessments and agricultural/forest/current-use programs.
- House/homesite: condition, major systems, utilities and foreseeable work.
- Location: always include distance/drive time to **Green Bay, Wisconsin**.
- Market access: identify realistic 30/60/90/120-minute markets for rural/property-based business opportunities.
- **Resale/market trajectory:** evaluate township/municipality, county and nearest meaningful metro for population/household direction, employment base, incomes, housing demand/liquidity, price direction, new construction/permits, infrastructure investment and major growth/decline catalysts. Do not infer future appreciation from one recent sale or asking-price trend.
- **Development optionality:** when acreage/configuration makes it relevant, evaluate subdivision potential, minimum lots/frontage, additional homesites, access, utilities/well/septic, zoning/future land use, wetlands/topography/soils, rights/restrictions and realistic infrastructure cost.
- Nuisances: highways, industry, CAFOs, rail, airports, landfill, quarry/mine, oil/gas, pipelines, transmission lines, ranges and other material concerns.
- Value/comps: fair value, offer range and effective cost-to-goal.

## Market Trajectory / Exit Risk

Every property should receive a market-context assessment separate from its lifestyle/persona scores.

Report:
- **Market Trajectory:** GROWING / EMERGING / STABLE / STAGNANT / DECLINING / UNKNOWN
- **Resale Liquidity:** STRONG / ADEQUATE / THIN / VERY THIN / UNKNOWN
- **Development Optionality:** NONE / LIMITED / PLAUSIBLE / STRONG / EXCEPTIONAL / NOT APPLICABLE

Use evidence at multiple geographic levels. Rural property may sit in a small declining municipality while still benefiting from a growing metro commute shed, recreation market, energy/agricultural economy or path-of-development location; conversely, a cheap property far outside viable demand centers may have substantial exit risk.

Explicitly call out two conditions:

1. **Value Trap Risk:** asking price appears attractive, but structural economic/population weakness, thin sales volume, limited employment/market access or a narrow buyer pool could make resale difficult or appreciation weak.
2. **Growth Tailwind:** credible evidence suggests increasing demand, infrastructure, employment, household growth or metro expansion may make scarce land increasingly valuable.

Do not label an area "up and coming" based on marketing language. Identify the actual catalysts and distinguish established trends from speculative announcements.

For development potential, never treat gross acreage as developable acreage or hypothetical future lots as current market value. Account for zoning/entitlement, access, utilities, soils/septic, wetlands/floodplain, topography, infrastructure, carrying cost, absorption and sales risk.

## OGM / Severed Rights Risk

In regions where oil, gas, mineral, coal, timber, pore-space or other subsurface/surface rights are commonly severed, **explicitly warn the user near the top of the chat that those rights must not be assumed to convey**. Do this even when the listing is silent.

Determine, when evidence permits:

- Which rights convey, are reserved/severed, or remain unknown.
- Who currently owns/controls the severed interest when discoverable.
- Whether an active lease, unit, drilling/mining permit, well, pipeline, gathering line, access road, easement, royalty interest, timber right or other development instrument exists.
- Whether the severed estate is dominant or carries express/implied surface-use rights under applicable state law and recorded instruments.
- Whether the surface owner has a surface-use agreement, no-surface-operations clause, location restrictions, compensation rights, setbacks or other protections.
- Nearby/current resource development activity and economic/geologic plausibility of future development.
- Whether modern extraction could occur from an off-site pad or otherwise reduce direct surface disturbance.

If material rights **do not convey**, provide a separate **Rights Disturbance Risk** assessment. This is not merely a title-status label; it estimates the practical likelihood and severity that another rightsholder could exercise those rights in a way that interferes with residential, homestead, business, privacy, building or land-use goals.

Rate both dimensions separately:

- **Exercise Likelihood:** LOW / MODERATE / HIGH / UNKNOWN
- **Surface/Lifestyle Impact if Exercised:** LOW / MODERATE / HIGH / SEVERE / UNKNOWN

Then provide an overall **Rights Disturbance Risk:** 🟢 LOW / 🟡 MODERATE / 🔴 HIGH / ⚫ UNKNOWN.

Base the assessment on evidence such as active leases/permits, nearby wells/mines, production trends, geology/resource play, rightsholder/operator activity, parcel size/configuration, existing infrastructure, access routes, deed/lease language, surface-use protections and the economics/technical feasibility of extraction. Never infer LOW risk merely because no activity is visible today.

Explain the plausible real-world disturbance: e.g. well pad, mine/quarry activity, access road, timber removal, pipeline/gathering line, compressor/equipment, truck traffic, noise/light, loss of buildable area, interference with privacy/animals/business, or minimal/no direct surface use.

Where deed/lease language is unavailable, label the conclusion provisional and recommend title/deed/lease review by a qualified local real-estate or mineral-rights attorney before purchase. Do not present the risk rating as a legal conclusion or guarantee of future activity.

## Land Model

Do not equate acreage with value.

**Total Acres → Constrained Acres → Usable Acres → Prime/Operational Acres**

Prime/operational acres are land especially useful for buildings, equipment, gardens, animals, wood processing, recreation or other intended uses.

## Cost-to-Goal

Classify missing features as **Existing / Easy Value-Add / Major Value-Add / Difficult / Impossible**.

Always distinguish **“doesn't have it” from “can't have it.”**

**Effective Property Cost = Purchase Price + Required Improvements + Desired Improvements**

Permanent characteristics receive the most weight: usable land, location, access, zoning, broadband, wetlands/topography, privacy, rights/restrictions, taxes, market trajectory and market access.

## Persona Scoring

Read **every `.md` file in `personas/active/`** and score the property independently for each active persona. Do not use `personas/inactive/` unless explicitly requested.

Personas may represent people, animals, businesses, lifestyles or other use cases. Their scores are **derived results**, not permanent property facts.

Do not assume all personas have equal importance. `default_weight` is available for aggregate scenarios, but comparisons should preserve each individual persona score.

The central question remains:

**At this price, how good is this opportunity considering what exists, what is missing, what can change, what it costs to get there, and how defensible the eventual exit is?**
