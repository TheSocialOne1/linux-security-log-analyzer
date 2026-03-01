#!/usr/bin/env python3
"""
agent.py

A simple command-dispatching "agent".

Why this exists:
- It provides a clean pattern for "skills" (tools) that can be called by name.
- Today, YOU choose the command.
- Later, an LLM (Claude) can choose the command automatically.

Commands:
- analyze-log <log_file>
- export-json <log_file> <output.json>
"""

import json
import sys

from skills.analyze_log import analyze_log_file
from skills.export_json import export_json


def print_help() -> None:
    """Print CLI usage instructions."""
    print(
        "Usage:\n"
        "  python agent.py analyze-log <log_file>\n"
        "  python agent.py export-json <log_file> <output.json>\n"
        "\n"
        "Examples:\n"
        "  python agent.py analyze-log sample_logs/secure.log\n"
        "  python agent.py export-json sample_logs/secure.log report.json\n"
    )


def main() -> int:
    """
    Entry point. Parses CLI args, dispatches to skills, returns exit code.
    """
    # Need at least a command name
    if len(sys.argv) < 2:
        print_help()
        return 2

    command = sys.argv[1]

    # Command: analyze-log <log_file>
    if command == "analyze-log":
        if len(sys.argv) < 3:
            print("Error: missing <log_file>\n")
            print_help()
            return 2

        log_file = sys.argv[2]
        report = analyze_log_file(log_file)

        print("=== Agent Report ===")
        print(json.dumps(report, indent=2))
        return 0

    # Command: export-json <log_file> <output.json>
    if command == "export-json":
        if len(sys.argv) < 4:
            print("Error: missing arguments\n")
            print_help()
            return 2

        log_file = sys.argv[2]
        out_file = sys.argv[3]

        report = analyze_log_file(log_file)
        export_json(report, out_file)

        print("=== Agent Report (saved) ===")
        print(json.dumps(report, indent=2))
        print(f"\nSaved report to: {out_file}")
        return 0

    # Unknown command
    print(f"Error: unknown command '{command}'\n")
    print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
