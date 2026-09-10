# Nashville Land Inventory — 2026-09-10

## Scope
Zillow discovery search for active land listings priced strictly below $500,000 that Zillow's commute filter places within 60 minutes driving, off-peak, of downtown Nashville, Tennessee (anchor approximately 36.1627, -86.7816). Pending, contingent, and under-contract listings were excluded.

## Current portfolio filter
On 2026-09-10 the imported Nashville inventory was narrowed to:

- **5.00 acres or more**, OR
- **asking price strictly below $20,000**, regardless of acreage.

The acreage threshold is inclusive: a listing reported by Zillow as exactly 5.00 acres is retained.

## Result
- Original verifiable under-$500,000 import: **197**
- Listings retained at **5.00+ acres**: **32**
- Verifiable sub-$20,000 exceptions retained: **0**
- Listings removed for being under 5 acres and not qualifying for the sub-$20,000 exception: **165**
- **Current retained Nashville import: 32 listings**

A fresh Zillow check using the 5-acre filter returned 33 results, but one (`4414 Maxwell Rd, Antioch, TN 37013`) still exposes no asking price and was not part of the original under-$500,000 import. A separate under-$20,000 search exposed only two no-price listings (`4414 Maxwell Rd` and `128 Myatt Dr`), so neither can be verified as a qualifying sub-$20,000 exception.

## Boundary handling
The original import excluded two listings priced exactly $500,000 and two listings with no exposed asking price. Those exclusions remain unchanged.

## Research status
Retained properties remain discovery/import records, not completed investigations. Zillow-derived price, acreage, classification, coordinates, and active status remain listing claims until independently verified. Each retained record remains `INITIAL` / `Low` confidence with open fatal-flaw research tasks. No property was scored or advanced to a verdict from Zillow discovery data alone.

## Source
Zillow property-search connector, queried and acreage-filtered 2026-09-10. Point-in-time inventory; listing status, prices, and acreage claims can change after capture.
