#!/usr/bin/env python3
"""Generate analytical datasets from PropertyResearch Markdown records.

Markdown remains authoritative. This script creates derived JSON/Parquet indexes.
It intentionally tolerates legacy records and missing fields.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROPERTIES = ROOT / "properties"
DATA = ROOT / "data" / "generated"
SITE = ROOT / "site"


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
        files.append(path)
    return sorted(files)


def scenario_files(property_path: Path) -> list[Path]:
    base = property_path.parent
    if property_path.name != "property.md":
        candidate = base / property_path.stem / "scenarios"
    else:
        candidate = base / "scenarios"
    return sorted(candidate.glob("*.md")) if candidate.exists() else []


def build() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    properties: list[dict[str, Any]] = []
    scenarios: list[dict[str, Any]] = []

    for path in property_files():
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        rel = path.relative_to(ROOT).as_posix()
        property_id = str(fm.get("property_id") or fm.get("parcel_id") or path.parent.name if path.name == "property.md" else path.stem)
        row = dict(fm)
        row.update({
            "property_id": property_id,
            "source_path": rel,
            "asking_price": fm.get("price") or heading_value(text, "Asking Price"),
            "acreage": fm.get("acreage") or heading_value(text, "Acreage"),
            "development_score": heading_value(text, "Development Score"),
            "preferred_development_strategy": heading_value(text, "Preferred Development Strategy"),
            "realistic_saleable_lot_yield": heading_value(text, "Realistic Saleable Lot Yield"),
            "twenty_four_month_feasibility": heading_value(text, "24-Month Feasibility"),
            "maximum_land_basis": heading_value(text, "Estimated Maximum Land Basis"),
            "minimum_upfront_capital": heading_value(text, "Minimum Practical Upfront Capital"),
            "peak_capital_at_risk": heading_value(text, "Peak Capital at Risk"),
            "estimated_gross_profit": heading_value(text, "Estimated Gross Profit"),
            "profit_margin_on_cost": heading_value(text, "Profit Margin on Cost"),
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
