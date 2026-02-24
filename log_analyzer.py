#!/usr/bin/env python3

import re
from collections import Counter

log_file = "sample_logs/secure.log"

failed_pattern = re.compile(r"Failed password for (invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)")

failed_attempts = []
source_ips = []

with open(log_file, "r") as f:
    for line in f:
        match = failed_pattern.search(line)
        if match:
            user = match.group(2)
            ip = match.group(3)
            failed_attempts.append(user)
            source_ips.append(ip)

print("=== Failed Login Summary ===")
print(f"Total failed attempts: {len(failed_attempts)}\n")

print("Top targeted users:")
for user, count in Counter(failed_attempts).most_common():
    print(f"{user}: {count}")

print("\nTop source IPs:")
for ip, count in Counter(source_ips).most_common():
    print(f"{ip}: {count}")

