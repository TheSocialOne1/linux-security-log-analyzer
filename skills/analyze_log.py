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
