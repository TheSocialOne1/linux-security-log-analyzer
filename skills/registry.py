"""
registry.py

A tiny registry describing available skills (tools).
Later, an LLM can read this registry to decide which tool to call.

Keeping this as plain Python data keeps it simple and testable.
"""

from typing import Dict

SKILLS: Dict[str, dict] = {
    "analyze-log": {
        "description": "Analyze an SSH auth log and summarize failed login attempts.",
        "args": ["log_file"],
        "returns": "JSON report printed to stdout",
    },
    "export-json": {
        "description": "Analyze a log and save the report to a JSON file.",
        "args": ["log_file", "output.json"],
        "returns": "Writes JSON file + prints report",
    },
}
