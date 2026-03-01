import json


def export_json(report: dict, out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
