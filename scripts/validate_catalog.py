from pathlib import Path
import csv

path = Path(__file__).resolve().parents[1] / "catalog" / "datasets.csv"
with path.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
required = {"name", "domain", "modalities", "project_role", "url"}
assert rows, "Catalog is empty"
assert required.issubset(rows[0]), f"Missing required columns: {required - set(rows[0])}"
assert all(r["url"].startswith("http") for r in rows), "All entries must contain source URLs"
print(f"Validated {len(rows)} dataset records")
