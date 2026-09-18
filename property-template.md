---
record_version: 9
address:
city:
state:
zip:
county:
parcel_id:
listing_url:
zillow_url:
primary_photo_url:
primary_photo_source:
primary_photo_checked_date:
parcel_map_source:
parcel_map_url:
parcel_boundary_source:
parcel_boundary_confidence:
parcel_map_checked_date:
listing_status:
active_offer_status:
asking_price:
original_price:
days_on_market:
property_type:
total_acres:
constrained_acres_est:
usable_acres_est:
prime_acres_est:
house_sqft:
beds:
baths:
annual_property_tax:
broadband_rating:
broadband_status:
ogm_status:
rights_exercise_likelihood:
rights_surface_impact:
rights_disturbance_risk:
legal_access_status:
rv_occupancy_status:
rv_occupancy_max_duration:
market_access_rating:
rdc_30_est:
rdc_45_est:
rdc_60_est:
rdc_confidence:
rdc_suburban_pool_depth:
rdc_rural_interface:
rdc_date_friction:
rdc_growth_direction:
dating_market_access_score:
dating_market_access_confidence:
dating_market_primary_pool:
dating_market_drive_time:
dating_market_practical_radius:
business_customer_demand_rating:
business_customer_demand_confidence:
equine_income_potential:
equine_customer_demand_likelihood:
equine_demand_confidence:
research_status: INITIAL
research_priority:
open_research_count:
p0_open_count:
rescore_required: false
last_deep_research:
research_confidence:
verdict:
reviewed_date:
last_updated:
---

# Property Summary

## Listing Photo
Display the actual primary/hero listing image near the top of the Investigator's first chat analysis when available. Prefer the supplied listing source. Store reference/provenance rather than copied third-party imagery by default.

## Parcel Map / Aerial
Display a satellite/aerial view with the subject parcel boundary whenever reliable parcel geometry can be established. Prefer county/municipal GIS, assessor GIS, state/authoritative cadastral sources, then listing/Zillow only as fallback. Label **PARCEL MAP — NOT A SURVEY** and record boundary confidence.

## Fatal-Flaw Screen
| Item | Result | Notes |
|---|---|---|
| Wired broadband | CLEAR / INVESTIGATE / FAIL | |
| Legal/practical access | CLEAR / INVESTIGATE / FAIL | |
| Buildability/zoning | CLEAR / INVESTIGATE / FAIL | |
| Land constraints | CLEAR / INVESTIGATE / FAIL | |
| Restrictions | CLEAR / INVESTIGATE / FAIL | |
| House/homesite | CLEAR / INVESTIGATE / FAIL | |
| Temporary RV occupancy (vacant/raw land) | CLEAR / INVESTIGATE / FAIL / NOT APPLICABLE | |
| OGM/surface rights | CLEAR / INVESTIGATE / FAIL | |
| Carrying costs | CLEAR / INVESTIGATE / FAIL | |
| Resale/liquidity | CLEAR / INVESTIGATE / FAIL | |

## Listing & Value
Current status, active-offer status, price history, DOM, tax/assessment, comps, fair value and offer range.

## Broadband
Classify: **At House / Along Road / Nearby / Planned / Possible / Unknown**. For vacant/no-address parcels, provide a clearly labeled **BROADBAND LOOKUP PROXY — NOT THE PROPERTY ADDRESS** when practical.

## Land Reality
- Total acres:
- Constrained acres:
- Usable acres:
- Prime/operational acres:
- Primary constraints:
- Best uses:

## Access
Legal frontage/access, private-road/easement issues, driveway and heavy-equipment/construction practicality.

## Zoning & Buildability
Intended uses, accessory-building rules, home business/firewood/sawmill restrictions and permitting concerns.

## Temporary RV Occupancy (Vacant/Raw Land)
Answer the controlling question: **Can Nicholas legally occupy an RV/camper on this parcel while constructing a permanent residence, and for how long?** Use **NOT APPLICABLE** for properties where this transition strategy is irrelevant.

- Status: CLEAR / INVESTIGATE / FAIL / NOT APPLICABLE
- Maximum initial duration:
- Extension/renewal available:
- Building permit required first:
- Active construction/progress required:
- Septic or approved wastewater required:
- Water requirement:
- Electrical/service requirement:
- 911 address or occupancy/inspection requirement:
- Occasional camping allowance (do not treat as residential permission):
- Permanent RV residence allowed:
- Controlling authority and ordinance/permit citation:
- Written local-authority confirmation:
- Enforcement/ambiguity notes:
- Practical winter setup: all-weather access, gravel/elevated pad, drainage/mud, freeze protection and utility lead times
- Exact next validation step:

## Animals & Homestead
Dogs, chickens/roosters, goats, sheep, horses/livestock and nuisance/fencing/setback issues.

## Rights & Restrictions
If the region commonly has severed mineral/OGM/coal or similar rights, explicitly warn that rights **must not be assumed to convey** until deed/title evidence confirms them.

- OGM/minerals: Convey / Partial / Reserved / Unknown
- Coal rights:
- Timber rights:
- Pore-space/other subsurface rights where relevant:
- Current rightsholder/operator if known:
- Active leases/units/permits:
- Surface-use rights:
- Surface-use agreement/protections:
- Easements/ROW:
- HOA/covenants:
- Pipelines/wells/mines/infrastructure:

### Rights Disturbance Risk
- **Exercise Likelihood:** LOW / MODERATE / HIGH / UNKNOWN
- **Surface/Lifestyle Impact if Exercised:** LOW / MODERATE / HIGH / SEVERE / UNKNOWN
- **Overall Rights Disturbance Risk:** 🟢 LOW / 🟡 MODERATE / 🔴 HIGH / ⚫ UNKNOWN
- Evidence for likelihood:
- Plausible physical disturbance:
- Effect on homesites/buildings/privacy/dogs/homestead/business:
- Existing protections/mitigations:
- Most important missing deed/lease/title evidence:

## Taxes & Carrying Cost
Current taxes, reassessment risk, special programs/rollback exposure and regional comparison.

## House / Homesite
Classify foreseeable work: **Cosmetic / Moderate / Major**.

## Utilities
Well/septic, gas/propane, electric service, 3-phase potential and infrastructure.

## Location
- Green Bay, WI:
- Active current-home benchmark:
- Nearest service town:
- Nearest significant city:
- Nearest major metro:
- Shopping:
- Hospital:
- Major highway/interstate:

## Rural Dating Catchment (RDC)
Use `rural-dating-catchment.md`.

- **RDC-30:**
- **RDC-45 (primary):**
- **RDC-60:**
- **RDC Confidence:** LOW / MEDIUM / HIGH
- **Suburban Pool Depth:** SMALL / MEDIUM / LARGE / VERY LARGE / ENORMOUS
- **Rural Interface:** POOR / FAIR / GOOD / EXCELLENT / EXCEPTIONAL
- **Date Friction:** LOW / LOW-MODERATE / MODERATE / HIGH
- **Growth Direction:**
- Suburban dating belt:
- Rural property belt/interface:
- Urban core excluded / treatment:
- RDC × Development intersection:
- Data/MOE limitations:

## Dating Market Access
Evaluate for Nicholas as a 42-year-old heterosexual single man seeking a roughly 34–39-year-old, physically active/fit partner compatible with an outdoors/property-oriented lifestyle. This is a location-access estimate, not a judgment about individual residents.

- **Dating Market Access Score:** XX/100
- **Confidence:** LOW / MEDIUM / HIGH
- Primary realistic dating pool:
- Practical dating radius:
- Typical drive to primary pool:
- Pool scale and relevant age/sex/single-status evidence:
- Growth/transplant dynamics:
- Fitness/outdoor/social opportunity proxies:
- App practicality and travel friction:
- Key limitation/uncertainty:
- Bottom line for a single owner:

## Commercial Market Access
- Best 30-minute market:
- Best 60-minute market:
- Best 90-minute market:
- Best 120-minute market:
- Best opportunities:
- Market rating: 🟢 / 🟡 / 🔴

## Business Customer Demand
Complete for every active business-use-case persona. Keep site suitability separate from actual customer demand.

| Business use case | Service radius | Customer Demand Likelihood | Confidence | Conservative stabilized customers / occupancy | Break-even volume | Key evidence |
|---|---|---|---|---|---|---|
| | | VERY LOW / LOW / MODERATE / HIGH / VERY HIGH / UNKNOWN | LOW / MEDIUM / HIGH | | | |

- Direct competitors, drive times, pricing, capacity/openings and operating-status evidence:
- Demand-base proxies and market trajectory:
- Market gap / differentiated offer:
- Downside case:
- Expected time to stabilization:
- Evidence limitations:
- Next direct validation step:

### Equine / Horse Boarding Opportunity
Complete using `personas/active/equine-horse-boarding.md`. This is optional/bonus-only and should not penalize non-equine properties.

- Equine Income Potential: NONE / LOW / MODERATE / HIGH / EXCEPTIONAL
- Customer Demand Likelihood: VERY LOW / LOW / MODERATE / HIGH / VERY HIGH / UNKNOWN
- Demand Confidence: LOW / MEDIUM / HIGH
- Likely boarding model:
- Feasible capacity / likely stabilized occupancy:
- Monthly rate range:
- Expected stabilization period:
- Stabilized annual gross revenue:
- Annual operating cost:
- Operating income before owner labor, debt service, tax and depreciation:
- Break-even occupied horses:
- 50% / 75% / 90% occupancy cases:
- Owner labor / relief coverage requirement:
- Existing infrastructure and replacement value:
- Additional startup investment:
- Income per operational acre:
- Zoning / insurance / manure / access constraints:
- Alternative use if demand disappoints:
- Next validation step:
- Verdict: Worth further investigation / Opportunistic only / Not attractive

## Resale / Development
- Market Trajectory: GROWING / EMERGING / STABLE / STAGNANT / DECLINING / UNKNOWN
- Resale Liquidity: STRONG / ADEQUATE / THIN / VERY THIN / UNKNOWN
- Development Optionality: NONE / LIMITED / PLAUSIBLE / STRONG / EXCEPTIONAL / NOT APPLICABLE
- Value Trap Risk:
- Growth Tailwind:
- Comparison vs current-home benchmark:

## Nuisances / Surroundings
Material nearby risks and positive location features.

## Cost to Goal
- Purchase:
- Immediate work:
- Desired improvements:
- Effective Property Cost:
- Cash to Goal:
- Missing features classified as Existing / Easy / Major / Difficult / Impossible:

## Purchase Structure
Complete when `finance/buyer-finance.md` has enough data. Use current rate assumptions and label estimates.
- Finance scenario:
- Purchase price:
- Suggested down payment:
- Estimated loan amount:
- Estimated cash at closing:
- Cash remaining after closing:
- Immediate improvement capital:
- Remaining reserve:

## Estimated Monthly Carry
- Principal + interest:
- Property tax:
- Homeowners insurance:
- PMI:
- HOA/required fees:
- Other material recurring costs:
- Estimated PITI:
- Estimated total property carry:
- Housing Cost Delta vs current benchmark:

## Capital Allocation
Compare additional down payment, retained improvement capital, buying features already built, and optional future equity financing when useful.

## Persona Scores
| Persona | Score | Key reason |
|---|---:|---|
| | /100 | |

## Dating Market Access
**Dating Market Access:** XX/100 or Not Yet Scored  
**Confidence:** LOW / MEDIUM / HIGH

## Financial Fit
**Financial Fit:** XX/100 or Not Yet Scored

## Property Card
**Address:**  
**Price:**  
**Type:**  
**Acres:** Total | Usable | Prime  
**House:** sqft | bed | bath  
**Setting:** Rural / Semi-Rural / Suburban / Urban  
**Status:**  
**DOM:**  
**Taxes:** $/yr  
**Parcel Boundary Confidence:** High / Medium / Low / Unverified  
**Research Status:** INITIAL / NEEDS_RESEARCH / DEEP_RESEARCH / MOSTLY_VERIFIED / VERIFIED / BLOCKED  
**Research Confidence:** High / Medium / Low  

**Persona Scores:** list every active persona dynamically.  
**Dating Market Access:** XX/100 (LOW / MEDIUM / HIGH confidence)  
**Financial Fit:** XX/100 or Not Yet Scored  

**Quick Ratings:** Broadband | Move-In/Homesite | Temporary RV Occupancy | Shop | Build Freedom | Usable Land | Access | Animals | Privacy | Zoning | Wetlands/Flood | OGM/Rights | Rights Disturbance | Taxes | Market Access | Dating Market Access | Business Customer Demand | Equine Potential | Resale/Liquidity | Value

**Rights Disturbance:** Exercise Likelihood | Surface/Lifestyle Impact | Overall Risk  
**Market Trajectory:**  
**Resale Liquidity:**  
**Development Optionality:**  
**Effective Property Cost:**  
**Cash to Goal:**  
**Estimated Monthly Carry:**  
**Housing Cost Delta:**  

**Best Feature:**  
**Biggest Weakness:**  
**Dealbreaker Risk:**  
**Best Value-Add:**  
**Most Important Unknown:**  

**VERDICT:** STRONG CONTENDER / CONTENDER / MAYBE / WEAK CONTENDER / PASS

**Bottom Line:**  
**Fair Value:**  
**Suggested Offer:**  
**At Asking:** GREAT / GOOD / FAIR / OVERPRICED / POOR  
**Strong-Contender Price:**  

## Open Research Tasks

Use priority and completion state explicitly. Preserve completed tasks as history.

- [ ] **P0** — Question — `OPEN`
- [ ] **P1** — Question — `OPEN`
- [ ] **P2** — Question — `OPEN`
- [ ] **P3** — Question — `OPEN`

Completion examples:
- [x] **P0** — Verify wired broadband — `RESOLVED 2026-09-08` — Fiber confirmed at house by ISP/FCC.
- [ ] **P0** — Confirm OGM deed language — `BLOCKED 2026-09-08` — Obtain title commitment/deed copy.
- [ ] **P1** — Confirm second homesite — `PARTIALLY RESOLVED 2026-09-08` — Zoning allows it; septic suitability still unknown.

## Sources
Record authoritative sources, listing sources and dates checked.
