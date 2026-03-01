#!/usr/bin/env python3

import re
import sys
from collections import Counter
from typing import Iterable, Tuple


FAILED_PATTERN = re.compile(
    r"Failed password for (invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"
)


def extract_failed_attempts(lines: Iterable[str]) -> Tuple[Counter, Counter, int]:
    """
    Parse log lines and return:
      - user_counts: Counter of targeted usernames
      - ip_counts: Counter of source IPs
      - total_failed: total number of failed attempts
    """
    users: Counter = Counter()
    ips: Counter = Counter()
    total_failed = 0

    for line in lines:
        match = FAILED_PATTERN.search(line)
        if match:
            user = match.group(2)
            ip = match.group(3)
            users[user] += 1
            ips[ip] += 1
            total_failed += 1

    return users, ips, total_failed


def print_summary(user_counts: Counter, ip_counts: Counter, total_failed: int) -> None:
    print("=== Failed Login Summary ===")
    print(f"Total failed attempts: {total_failed}\n")

    print("Top targeted users:")
    for user, count in user_counts.most_common():
        print(f"{user}: {count}")

    print("\nTop source IPs:")
    for ip, count in ip_counts.most_common():
        print(f"{ip}: {count}")


def main() -> int:
    # Default file if no args provided
    log_file = sys.argv[1] if len(sys.argv) > 1 else "sample_logs/secure.log"

    try:
        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
            user_counts, ip_counts, total_failed = extract_failed_attempts(f)
    except FileNotFoundError:
        print(f"Error: file not found: {log_file}", file=sys.stderr)
        return 2

    print_summary(user_counts, ip_counts, total_failed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
