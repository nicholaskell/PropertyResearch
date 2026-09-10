# Nashville Land Inventory — 2026-09-10

## Scope
Zillow discovery search for active land listings priced strictly below $500,000 that Zillow's commute filter places within 60 minutes driving, off-peak, of downtown Nashville, Tennessee (anchor approximately 36.1627, -86.7816). Pending, contingent, under-contract, and accepting-backup-offer listings were excluded.

## Result
- Zillow broad search count: **201**
- Verifiable listings priced **under $500,000** imported: **197**
- Exactly $500,000 and excluded: **2**
- No asking price exposed and therefore not provably under $500,000: **2**

### Excluded boundary/unknown-price results
- `0 Lowes Ln Lot 1` — $500,000.
- `0 Green Ln` — $500,000.
- `4414 Maxwell Rd, Antioch, TN 37013` — no asking price exposed.
- `128 Myatt Dr, Madison, TN 37115` — no asking price exposed.

## Enumeration
The broad Zillow result was capped at 100 displayed properties, so inventory was enumerated in non-overlapping price bands:

| Asking price | Imported |
|---|---:|
| Below $100,000 | 13 |
| $100,000–$199,999 | 57 |
| $200,000–$299,999 | 60 |
| $300,000–$399,999 | 40 |
| $400,000–$499,999 | 27 |
| **Total** | **197** |

Each imported listing has a normalized `properties/TN/<address>-<zpid>/property.md` record. ZPID is retained in the folder slug to prevent collisions between repeated street/lot labels.

## Research status
These are discovery/import records, not completed investigations. Zillow-derived price, acreage, classification, coordinates, and active status remain listing claims until independently verified. Each record starts `INITIAL` / `Low` confidence with open fatal-flaw research tasks covering broadband, access/zoning/buildability, wetlands/flood/topography/soils, restrictions/easements/rights, parcel/taxes/usable acreage, and resale/development optionality. No property was scored or advanced to a verdict from Zillow discovery data alone.

## Source
Zillow property-search connector, queried 2026-09-10. Point-in-time inventory; listing status and prices can change after capture.
