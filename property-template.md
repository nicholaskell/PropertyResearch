---
record_version: 5
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
market_access_rating:
research_confidence:
verdict:
reviewed_date:
last_updated:
---

# Property Summary

## Listing Photo

Display the actual primary/hero listing image near the top of the Investigator's first chat analysis when available. Prefer the supplied listing source. `primary_photo_url` is a reference only; do not download or commit third-party listing images by default. If a stable direct image URL is unavailable, leave it blank and record the source/listing page instead.

## Parcel Map / Aerial

Display a satellite/aerial view with the subject parcel boundary whenever reliable parcel geometry can be established.

- **Boundary preference:** county/municipal GIS → assessor/parcel GIS → state/authoritative cadastral source → listing/Zillow only as fallback.
- **Address-less parcels:** identify the parcel using APN/parcel ID, legal description, official GIS, listing coordinates, road frontage and adjoining parcels. Do not assume the listing pin is the parcel.
- Label the chat image **PARCEL MAP — NOT A SURVEY**.
- State the boundary source and imagery source when known.
- `parcel_boundary_confidence`: HIGH / MEDIUM / LOW / UNVERIFIED.
- Zillow/listing parcel lines are evidence, not authoritative boundaries; explicitly label them listing-derived when used.
- Never invent or hand-draw a boundary when parcel identity/geometry is uncertain.
- If an accurate satellite overlay cannot be produced, show/link the best authoritative parcel map available and explain the limitation rather than creating false precision.
- Store source/reference metadata, not copied third-party imagery, by default.

## Fatal-Flaw Screen

| Item | Result | Notes |
|---|---|---|
| Wired broadband | CLEAR / INVESTIGATE / FAIL | |
| Legal/practical access | CLEAR / INVESTIGATE / FAIL | |
| Buildability/zoning | CLEAR / INVESTIGATE / FAIL | |
| Land constraints | CLEAR / INVESTIGATE / FAIL | |
| Restrictions | CLEAR / INVESTIGATE / FAIL | |
| House/homesite | CLEAR / INVESTIGATE / FAIL | |
| OGM/surface rights | CLEAR / INVESTIGATE / FAIL | |
| Carrying costs | CLEAR / INVESTIGATE / FAIL | |

## Listing & Value

Current status, active-offer status, price history, DOM, tax/assessment, comps, fair value and offer range.

## Broadband

Classify: **At House / Along Road / Nearby / Planned / Possible / Unknown**.

For vacant/no-address parcels, provide a clearly labeled **BROADBAND LOOKUP PROXY — NOT THE PROPERTY ADDRESS** using the closest confirmed neighboring residential/serviceable address when practical. Broadband at the proxy does not prove availability at the subject parcel.

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

Intended uses, accessory-building rules, home-business/firewood/sawmill restrictions and permitting concerns.

## Animals & Homestead

Dogs, chickens/roosters, goats, sheep, horses/livestock and nuisance/fencing/setback issues.

## Rights & Restrictions

If this property is in a region where mineral/OGM/coal or similar rights are commonly severed, explicitly state near the top of the chat that these rights **must not be assumed to convey** until deed/title evidence confirms them.

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

Required when material OGM/mineral/coal/timber or similar rights do not convey; use provisionally when status is unknown but regional severance risk is material.

- **Exercise Likelihood:** LOW / MODERATE / HIGH / UNKNOWN
- **Surface/Lifestyle Impact if Exercised:** LOW / MODERATE / HIGH / SEVERE / UNKNOWN
- **Overall Rights Disturbance Risk:** 🟢 LOW / 🟡 MODERATE / 🔴 HIGH / ⚫ UNKNOWN
- Evidence for likelihood:
- Plausible physical disturbance:
- Effect on homesites/buildings/privacy/dogs/homestead/business:
- Existing protections/mitigations:
- Most important missing deed/lease/title evidence:

Assess practical risk using active leases/permits, nearby wells/mines, geology/resource economics, operator/rightsholder activity, existing infrastructure, parcel geometry, access routes and recorded surface-use language. Do not call risk LOW merely because no current surface activity is visible. Distinguish likelihood from consequence: a low-probability right may still have severe consequences if exercised.

## Taxes & Carrying Cost

Current taxes, reassessment risk, special programs/rollback exposure and regional comparison.

## House / Homesite

Classify foreseeable work: **Cosmetic / Moderate / Major**.

## Utilities

Well/septic, gas/propane, electric service, 3-phase potential and infrastructure.

## Location

- Green Bay, WI:
- Nearest service town:
- Nearest significant city:
- Nearest major metro:
- Shopping:
- Hospital:
- Major highway/interstate:

## Commercial Market Access

- Best 30-minute market:
- Best 60-minute market:
- Best 90-minute market:
- Best 120-minute market:
- Best opportunities:
- Market rating: 🟢 / 🟡 / 🔴

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

## Capital Allocation

Compare when useful:

- Additional down payment and estimated payment savings
- Retaining cash for high-value improvements
- Buying required features already built versus constructing later
- Optional future equity financing, without assuming it is available or preferable

## Persona Scores

Read every active persona dynamically and list each score with concise reasoning.

| Persona | Score | Key reason |
|---|---:|---|
| | /100 | |

## Financial Fit

**Financial Fit:** XX/100 or Not Yet Scored

Explain monthly affordability, cash-to-close, reserve remaining, improvement capital needs, effective cost and financing flexibility. Do not score when key buyer-finance inputs are missing; identify what is needed instead.

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
**Research Confidence:** High / Medium / Low  

**Persona Scores:** list every active persona dynamically.  
**Financial Fit:** XX/100 or Not Yet Scored  

**Quick Ratings:** Broadband | Move-In/Homesite | Shop | Build Freedom | Usable Land | Access | Animals | Privacy | Zoning | Wetlands/Flood | OGM/Rights | Rights Disturbance | Taxes | Market Access | Value

**Rights Disturbance:** Exercise Likelihood | Surface/Lifestyle Impact | Overall Risk  
**Effective Property Cost:**  
**Cash to Goal:**  
**Estimated Monthly Carry:**  

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

Track unresolved items that materially affect ranking, financing or purchase confidence.

- [ ]

## Sources

Record authoritative sources, listing sources and dates checked.
