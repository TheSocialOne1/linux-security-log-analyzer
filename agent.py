#!/usr/bin/env python3

import json
import sys

from skills.analyze_log import analyze_log_file
from skills.export_json import export_json


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
