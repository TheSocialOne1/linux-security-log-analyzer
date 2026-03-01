#!/usr/bin/env python3

import json
import sys
from pathlib import Path

from log_analyzer import extract_failed_attempts


def analyze_log_file(path: str) -> dict:
    p = Path(path)
    with p.open("r", encoding="utf-8", errors="replace") as f:
        user_counts, ip_counts, total_failed = extract_failed_attempts(f)

    return {
        "total_failed": total_failed,
        "top_users": user_counts.most_common(10),
        "top_ips": ip_counts.most_common(10),
    }


def export_json(report: dict, out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python agent.py <log_file> [output.json]")
        return 2

    log_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None

    report = analyze_log_file(log_file)
    print("=== Agent Report ===")
    print(json.dumps(report, indent=2))

    if out_file:
        export_json(report, out_file)
        print(f"\nSaved report to: {out_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
