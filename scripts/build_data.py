#!/usr/bin/env python3
"""Generate analytical datasets from PropertyResearch Markdown records.

Markdown remains authoritative. This script creates derived JSON/Parquet indexes.
It intentionally tolerates legacy records and missing fields.

Location-access fields are screening estimates for portfolio comparison. When a
record has coordinates, metro distance is calculated from the parcel/listing
point to a practical regional dating hub and converted to an approximate road
distance/time. Legacy records fall back to locality-level estimates. Shopping
access uses explicit rural-locality overrides where the postal town is not the
most practical staple-shopping stop; otherwise the listing locality is treated
as the local shopping hub.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROPERTIES = ROOT / "properties"
DATA = ROOT / "data" / "generated"
SITE = ROOT / "site"

# Practical dating markets rather than a strict Census-MSA definition. Smaller
# regional cities are included where they are the realistic dating hub for an
# otherwise remote property (for example Green Bay, Marquette or Binghamton).
METROS: dict[str, tuple[float, float]] = {
    "Atlanta, GA": (33.7490, -84.3880),
    "Huntsville, AL": (34.7304, -86.5861),
    "Birmingham, AL": (33.5186, -86.8104),
    "Nashville, TN": (36.1627, -86.7816),
    "Clarksville, TN": (36.5298, -87.3595),
    "Memphis, TN": (35.1495, -90.0490),
    "Chattanooga, TN": (35.0456, -85.3097),
    "Knoxville, TN": (35.9606, -83.9207),
    "Louisville, KY": (38.2527, -85.7585),
    "Lexington, KY": (38.0406, -84.5037),
    "Cincinnati, OH": (39.1031, -84.5120),
    "Evansville, IN": (37.9716, -87.5711),
    "Indianapolis, IN": (39.7684, -86.1581),
    "Columbus, OH": (39.9612, -82.9988),
    "Pittsburgh, PA": (40.4406, -79.9959),
    "Erie, PA": (42.1292, -80.0851),
    "Scranton/Wilkes-Barre, PA": (41.4089, -75.6624),
    "Binghamton, NY": (42.0987, -75.9180),
    "Rochester, NY": (43.1566, -77.6088),
    "Buffalo, NY": (42.8864, -78.8784),
    "Gainesville, FL": (29.6516, -82.3248),
    "Tampa Bay, FL": (27.9506, -82.4572),
    "Orlando, FL": (28.5383, -81.3792),
    "Jacksonville, FL": (30.3322, -81.6557),
    "Green Bay, WI": (44.5133, -88.0133),
    "Fox Cities / Appleton, WI": (44.2619, -88.4154),
    "Madison, WI": (43.0731, -89.4012),
    "Milwaukee, WI": (43.0389, -87.9065),
    "Marquette, MI": (46.5436, -87.3954),
    "Grand Rapids, MI": (42.9634, -85.6681),
    "Charleston, WV": (38.3498, -81.6326),
    "Parkersburg, WV": (39.2667, -81.5615),
}

STATE_METROS: dict[str, tuple[str, ...]] = {
    "AL": ("Huntsville, AL", "Birmingham, AL", "Chattanooga, TN"),
    "FL": ("Gainesville, FL", "Tampa Bay, FL", "Orlando, FL", "Jacksonville, FL"),
    "GA": ("Chattanooga, TN", "Atlanta, GA"),
    "IN": ("Cincinnati, OH", "Louisville, KY", "Indianapolis, IN", "Evansville, IN"),
    "KY": ("Cincinnati, OH", "Louisville, KY", "Lexington, KY", "Nashville, TN", "Evansville, IN"),
    "MI": ("Marquette, MI", "Green Bay, WI", "Grand Rapids, MI"),
    "NY": ("Binghamton, NY", "Rochester, NY", "Buffalo, NY", "Scranton/Wilkes-Barre, PA"),
    "OH": ("Cincinnati, OH", "Columbus, OH", "Pittsburgh, PA"),
    "PA": ("Pittsburgh, PA", "Erie, PA", "Scranton/Wilkes-Barre, PA", "Buffalo, NY"),
    "TN": ("Nashville, TN", "Clarksville, TN", "Memphis, TN", "Chattanooga, TN", "Knoxville, TN", "Huntsville, AL"),
    "WI": ("Green Bay, WI", "Fox Cities / Appleton, WI", "Madison, WI", "Milwaukee, WI"),
    "WV": ("Charleston, WV", "Parkersburg, WV", "Pittsburgh, PA"),
}

# Postal locality -> practical staple-shopping stop where they differ materially.
# Distances/times are approximate screening values, not turn-by-turn routing.
SHOPPING_OVERRIDES: dict[tuple[str, str], tuple[str, float, int]] = {
    ("TN", "Vanleer"): ("Dickson, TN", 15, 20),
    ("TN", "Gruetli-Laager"): ("Tracy City, TN", 15, 20),
    ("TN", "Joelton"): ("Madison / north Nashville, TN", 16, 22),
    ("TN", "Whites Creek"): ("Madison / north Nashville, TN", 13, 18),
    ("TN", "Elmwood"): ("Carthage, TN", 13, 18),
    ("TN", "Bradyville"): ("Woodbury, TN", 12, 16),
    ("TN", "Pleasant Shade"): ("Carthage, TN", 15, 20),
    ("TN", "Hilham"): ("Livingston, TN", 16, 22),
    ("TN", "Cunningham"): ("Clarksville, TN", 14, 20),
    ("TN", "Buffalo Valley"): ("Cookeville, TN", 22, 28),
    ("TN", "Springville"): ("Paris, TN", 18, 24),
    ("TN", "Liberty"): ("Smithville, TN", 12, 16),
    ("TN", "Dowelltown"): ("Smithville, TN", 8, 12),
    ("TN", "Hickman"): ("Carthage, TN", 12, 17),
    ("TN", "Burlison"): ("Covington, TN", 11, 15),
    ("TN", "Southside"): ("Clarksville, TN", 15, 22),
    ("TN", "Christiana"): ("Murfreesboro, TN", 14, 20),
    ("TN", "Pegram"): ("Bellevue / west Nashville, TN", 11, 16),
    ("TN", "Baxter"): ("Cookeville, TN", 10, 14),
    ("TN", "Spencer"): ("McMinnville, TN", 27, 35),
    ("KY", "Means"): ("Mount Sterling, KY", 27, 35),
    ("KY", "Hudson"): ("Leitchfield, KY", 18, 24),
    ("KY", "Mackville"): ("Springfield, KY", 10, 15),
    ("KY", "Roundhill"): ("Bowling Green, KY", 24, 30),
    ("KY", "Frenchburg"): ("Mount Sterling, KY", 26, 34),
    ("KY", "Sharpsburg"): ("Mount Sterling, KY", 18, 24),
    ("KY", "Falmouth"): ("Falmouth, KY", 5, 10),
    ("IN", "Vallonia"): ("Seymour, IN", 18, 24),
    ("IN", "Moores Hill"): ("Aurora / Lawrenceburg, IN", 18, 24),
    ("IN", "Guilford"): ("Lawrenceburg, IN", 13, 18),
    ("MI", "Rapid River"): ("Escanaba, MI", 18, 24),
    ("MI", "Stephenson"): ("Marinette, WI", 32, 40),
    ("NY", "Erin"): ("Horseheads / Elmira, NY", 18, 24),
    ("NY", "Long Eddy"): ("Hancock, NY", 12, 17),
    ("OH", "Pleasant City"): ("Cambridge, OH", 16, 22),
    ("OH", "West Union"): ("West Union, OH", 5, 10),
    ("PA", "Marion Center"): ("Indiana, PA", 13, 18),
    ("PA", "Rimersburg"): ("Clarion, PA", 18, 24),
    ("PA", "New Freeport"): ("Waynesburg, PA", 24, 32),
    ("PA", "Mayport"): ("Punxsutawney, PA", 18, 25),
    ("PA", "West Finley"): ("Washington, PA", 24, 32),
    ("PA", "West Alexander"): ("Washington, PA", 16, 22),
    ("PA", "Ruffs Dale"): ("Greensburg, PA", 20, 27),
    ("PA", "Brockway"): ("DuBois, PA", 12, 17),
    ("PA", "Smethport"): ("Bradford, PA", 20, 28),
    ("WI", "Wausaukee"): ("Marinette, WI", 34, 42),
    ("WI", "Tigerton"): ("Shawano, WI", 22, 28),
    ("WI", "Reedsville"): ("Manitowoc, WI", 18, 24),
    ("WI", "Larsen"): ("Neenah / Fox Cities, WI", 15, 20),
    ("WI", "Abrams"): ("Green Bay, WI", 20, 25),
    ("WV", "Belleville"): ("Parkersburg, WV", 20, 28),
    ("WV", "New Martinsville"): ("New Martinsville, WV", 5, 10),
}

# Legacy/locality fallbacks used only when a record lacks usable coordinates.
METRO_FALLBACKS: dict[tuple[str, str], tuple[str, float, int]] = {
    ("TN", "Nashville"): ("Nashville, TN", 8, 15),
    ("TN", "Goodlettsville"): ("Nashville, TN", 16, 22),
    ("TN", "Greenbrier"): ("Nashville, TN", 26, 35),
    ("TN", "Joelton"): ("Nashville, TN", 17, 24),
    ("TN", "Whites Creek"): ("Nashville, TN", 12, 18),
    ("TN", "Pegram"): ("Nashville, TN", 19, 27),
    ("TN", "Ashland City"): ("Nashville, TN", 25, 35),
    ("TN", "Christiana"): ("Nashville, TN", 42, 50),
    ("TN", "Woodbury"): ("Nashville, TN", 52, 65),
    ("TN", "Bradyville"): ("Nashville, TN", 56, 70),
    ("TN", "Cunningham"): ("Clarksville, TN", 14, 20),
    ("TN", "Southside"): ("Clarksville, TN", 16, 23),
    ("TN", "Vanleer"): ("Clarksville, TN", 35, 45),
    ("TN", "Waverly"): ("Clarksville, TN", 53, 65),
    ("TN", "Millington"): ("Memphis, TN", 18, 25),
    ("TN", "Burlison"): ("Memphis, TN", 38, 48),
    ("TN", "Cleveland"): ("Chattanooga, TN", 33, 40),
    ("TN", "Hixson"): ("Chattanooga, TN", 11, 18),
    ("TN", "Whitwell"): ("Chattanooga, TN", 28, 38),
    ("TN", "Fayetteville"): ("Huntsville, AL", 32, 40),
    ("TN", "Pulaski"): ("Huntsville, AL", 48, 58),
    ("KY", "Bowling Green"): ("Nashville, TN", 66, 70),
    ("KY", "Brownsville"): ("Nashville, TN", 79, 85),
    ("KY", "Horse Cave"): ("Louisville, KY", 84, 90),
    ("KY", "Campbellsville"): ("Louisville, KY", 85, 95),
    ("KY", "Frankfort"): ("Lexington, KY", 28, 35),
    ("KY", "Burlington"): ("Cincinnati, OH", 18, 25),
    ("KY", "Hebron"): ("Cincinnati, OH", 15, 22),
    ("KY", "Petersburg"): ("Cincinnati, OH", 25, 32),
    ("KY", "Falmouth"): ("Cincinnati, OH", 42, 52),
    ("IN", "Lawrenceburg"): ("Cincinnati, OH", 25, 32),
    ("IN", "West Harrison"): ("Cincinnati, OH", 30, 38),
    ("IN", "Madison"): ("Louisville, KY", 55, 65),
    ("IN", "Metamora"): ("Cincinnati, OH", 55, 65),
    ("OH", "Harrison"): ("Cincinnati, OH", 24, 32),
    ("OH", "Cleves"): ("Cincinnati, OH", 18, 25),
    ("OH", "Camden"): ("Cincinnati, OH", 45, 55),
    ("PA", "Pittsburgh"): ("Pittsburgh, PA", 6, 12),
    ("PA", "McKeesport"): ("Pittsburgh, PA", 14, 22),
    ("PA", "Freedom"): ("Pittsburgh, PA", 28, 36),
    ("WI", "De Pere"): ("Green Bay, WI", 8, 15),
    ("WI", "Appleton"): ("Fox Cities / Appleton, WI", 5, 10),
    ("WI", "Neenah"): ("Fox Cities / Appleton, WI", 10, 15),
    ("WI", "Greenville"): ("Fox Cities / Appleton, WI", 10, 15),
    ("WI", "Seymour"): ("Green Bay, WI", 20, 28),
    ("WI", "Luxemburg"): ("Green Bay, WI", 20, 28),
    ("WI", "Peshtigo"): ("Green Bay, WI", 45, 52),
    ("FL", "Crystal River"): ("Tampa Bay, FL", 75, 85),
    ("FL", "Yankeetown"): ("Gainesville, FL", 55, 65),
    ("FL", "Chiefland"): ("Gainesville, FL", 40, 48),
    ("GA", "Trenton"): ("Chattanooga, TN", 22, 28),
    ("GA", "Wildwood"): ("Chattanooga, TN", 13, 20),
    ("AL", "Owens Cross Roads"): ("Huntsville, AL", 17, 24),
    ("MI", "Rapid River"): ("Marquette, MI", 62, 70),
    ("MI", "Gladstone"): ("Marquette, MI", 58, 65),
    ("MI", "Stephenson"): ("Green Bay, WI", 85, 95),
    ("WV", "Belleville"): ("Parkersburg, WV", 20, 28),
    ("WV", "New Martinsville"): ("Parkersburg, WV", 45, 55),
}


def scalar(value: str) -> Any:
    value = value.strip().strip('"').strip("'")
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.lower() in {"null", "none", "unknown", ""}:
        return None
    cleaned = value.replace(",", "").replace("$", "").replace("%", "")
    try:
        return float(cleaned) if "." in cleaned else int(cleaned)
    except ValueError:
        return value


def frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    out: dict[str, Any] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = scalar(value)
    return out


def heading_value(text: str, label: str) -> Any:
    patterns = [
        rf"(?im)^-?\s*\*\*{re.escape(label)}:\*\*\s*(.+)$",
        rf"(?im)^-?\s*{re.escape(label)}:\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return scalar(match.group(1))
    return None


def property_files() -> list[Path]:
    files = []
    if not PROPERTIES.exists():
        return files
    for path in PROPERTIES.rglob("*.md"):
        if path.name in {"assets.md"} or "assets" in path.parts:
            continue
        # Supporting research/strategy notes are evidence, not separate properties.
        if path.name.startswith("research-") or path.name.endswith("-strategy.md"):
            continue
        files.append(path)
    return sorted(files)


def scenario_files(property_path: Path) -> list[Path]:
    base = property_path.parent
    if property_path.name != "property.md":
        candidate = base / property_path.stem / "scenarios"
    else:
        candidate = base / "scenarios"
    return sorted(candidate.glob("*.md")) if candidate.exists() else []


def address_city_state(address: Any, fm: dict[str, Any], path: Path) -> tuple[str | None, str | None]:
    state = str(fm.get("state") or "").upper() or None
    city = str(fm.get("city") or "").strip() or None
    if address:
        m = re.search(r",\s*([^,]+),\s*([A-Z]{2})(?:\s+\d{5}(?:-\d{4})?)?\s*$", str(address))
        if m:
            city = city or m.group(1).strip()
            state = state or m.group(2).upper()
    if not state and len(path.parts) > 1 and path.parts[0] == "properties":
        state = path.parts[1].upper()
    return city, state


def coordinates(fm: dict[str, Any], text: str) -> tuple[float | None, float | None]:
    lat = fm.get("latitude") or fm.get("lat")
    lon = fm.get("longitude") or fm.get("lon") or fm.get("lng")
    try:
        if lat is not None and lon is not None:
            return float(lat), float(lon)
    except (TypeError, ValueError):
        pass
    m = re.search(r"(?i)(?:coordinates?|lat(?:itude)?)[^\d-]*(-?\d{2,3}\.\d+)[^\d-]+(-?\d{2,3}\.\d+)", text)
    if m:
        try:
            return float(m.group(1)), float(m.group(2))
        except ValueError:
            pass
    return None, None


def haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 3958.8
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def nearest_metro(state: str | None, lat: float | None, lon: float | None, city: str | None) -> tuple[str | None, float | None, int | None, str]:
    key = (state or "", city or "")
    if (lat is None or lon is None) and key in METRO_FALLBACKS:
        name, miles, mins = METRO_FALLBACKS[key]
        return name, miles, mins, "LOCALITY_ESTIMATE"
    if lat is None or lon is None or not state:
        return None, None, None, "UNKNOWN"
    candidates = STATE_METROS.get(state, tuple(METROS))
    name = min(candidates, key=lambda n: haversine_miles(lat, lon, *METROS[n]))
    straight = haversine_miles(lat, lon, *METROS[name])
    # Screening conversion from straight-line to practical road distance. Rural
    # roads and mountain/river crossings can move the real route materially.
    road_miles = max(1.0, straight * 1.22)
    drive_minutes = max(8, round((road_miles / 50.0) * 60 + 5))
    return name, round(road_miles), drive_minutes, "COORDINATE_ESTIMATE"


def shopping_access(state: str | None, city: str | None) -> tuple[str | None, float | None, int | None, str]:
    if not state or not city:
        return None, None, None, "UNKNOWN"
    key = (state, city)
    if key in SHOPPING_OVERRIDES:
        name, miles, mins = SHOPPING_OVERRIDES[key]
        return name, miles, mins, "LOCALITY_ESTIMATE"
    # Most listing/postal cities in the portfolio have at least a practical
    # grocery/fuel/pharmacy cluster. Keep a bounded local estimate rather than
    # pretending the parcel-to-store route was measured exactly.
    return f"{city}, {state}", None, 12, "LOCALITY_ESTIMATE"


def access_display(name: str | None, miles: float | None, minutes: int | None) -> str | None:
    if not name:
        return None
    if miles is not None and minutes is not None:
        return f"{name} — ≈{int(round(miles))} mi / ≈{minutes} min"
    if minutes is not None:
        return f"{name} — local / ≈{minutes} min"
    return name


def build() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    properties: list[dict[str, Any]] = []
    scenarios: list[dict[str, Any]] = []

    for path in property_files():
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        rel = path.relative_to(ROOT).as_posix()
        property_id = str(fm.get("property_id") or fm.get("parcel_id") or path.parent.name if path.name == "property.md" else path.stem)
        address = fm.get("address") or heading_value(text, "Address")
        city, state = address_city_state(address, fm, path.relative_to(ROOT))
        lat, lon = coordinates(fm, text)
        metro_name, metro_miles, metro_minutes, metro_conf = nearest_metro(state, lat, lon, city)
        town_name, town_miles, town_minutes, town_conf = shopping_access(state, city)
        row = dict(fm)
        row.update({
            "property_id": property_id,
            "source_path": rel,
            "address": address or fm.get("address"),
            "city": city,
            "state": state,
            "latitude": lat,
            "longitude": lon,
            "asking_price": fm.get("asking_price") or fm.get("price") or heading_value(text, "Asking Price"),
            "acreage": fm.get("acreage") or fm.get("listing_acres") or heading_value(text, "Acreage"),
            "development_score": heading_value(text, "Development Score"),
            "preferred_development_strategy": heading_value(text, "Preferred Development Strategy"),
            "realistic_saleable_lot_yield": heading_value(text, "Realistic Saleable Lot Yield"),
            "twenty_four_month_feasibility": heading_value(text, "24-Month Feasibility"),
            "maximum_land_basis": heading_value(text, "Estimated Maximum Land Basis"),
            "minimum_upfront_capital": heading_value(text, "Minimum Practical Upfront Capital"),
            "peak_capital_at_risk": heading_value(text, "Peak Capital at Risk"),
            "estimated_gross_profit": heading_value(text, "Estimated Gross Profit"),
            "profit_margin_on_cost": heading_value(text, "Profit Margin on Cost"),
            "major_dating_metro": metro_name,
            "major_dating_metro_distance_mi": metro_miles,
            "major_dating_metro_drive_minutes": metro_minutes,
            "major_dating_metro_display": access_display(metro_name, metro_miles, metro_minutes),
            "major_dating_metro_confidence": metro_conf,
            "closest_usable_town": town_name,
            "closest_usable_town_distance_mi": town_miles,
            "closest_usable_town_drive_minutes": town_minutes,
            "closest_usable_town_display": access_display(town_name, town_miles, town_minutes),
            "closest_usable_town_confidence": town_conf,
        })
        properties.append(row)

        for spath in scenario_files(path):
            stext = spath.read_text(encoding="utf-8")
            sfm = frontmatter(stext)
            srow = dict(sfm)
            srow.update({
                "property_id": sfm.get("property_id") or property_id,
                "scenario_id": sfm.get("scenario_id") or spath.stem,
                "source_path": spath.relative_to(ROOT).as_posix(),
                "scenario_name": sfm.get("scenario_name") or spath.stem.replace("-", " ").title(),
                "lot_count": heading_value(stext, "Lot count"),
                "lot_size_mix": heading_value(stext, "Lot-size mix"),
                "total_project_cost": heading_value(stext, "Total Project Cost"),
                "conservative_sellout_value": heading_value(stext, "Conservative Sellout Value"),
                "expected_gross_profit": heading_value(stext, "Expected Gross Profit"),
                "profit_margin_on_cost": heading_value(stext, "Profit Margin on Cost"),
                "minimum_upfront_capital": heading_value(stext, "Minimum Practical Upfront Capital"),
                "peak_capital_at_risk": heading_value(stext, "Peak Capital at Risk"),
                "return_on_cash": heading_value(stext, "Return on Cash Invested"),
                "capital_per_profit_dollar": heading_value(stext, "Capital Required per $1 Expected Profit"),
                "time_to_first_sale_months": heading_value(stext, "Time to First Sale"),
                "time_to_cash_recovery_months": heading_value(stext, "Time to Recover Initial Cash"),
                "project_duration_months": heading_value(stext, "Base-Case Duration"),
                "twenty_four_month_feasibility": heading_value(stext, "24-Month Feasibility"),
                "maximum_land_basis": heading_value(stext, "Maximum Land Basis"),
            })
            scenarios.append(srow)

    return properties, scenarios


def write_outputs(properties: list[dict[str, Any]], scenarios: list[dict[str, Any]]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    SITE.mkdir(parents=True, exist_ok=True)
    payload = {"properties": properties, "scenarios": scenarios}
    (DATA / "site-data.json").write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    (SITE / "site-data.json").write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")

    try:
        import pandas as pd
        pd.DataFrame(properties).to_parquet(DATA / "properties.parquet", index=False)
        pd.DataFrame(scenarios).to_parquet(DATA / "scenarios.parquet", index=False)
    except Exception as exc:
        print(f"Parquet generation skipped/failed: {exc}")


if __name__ == "__main__":
    p, s = build()
    write_outputs(p, s)
    print(f"Generated {len(p)} properties and {len(s)} development scenarios")
