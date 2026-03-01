from log_analyzer import extract_failed_attempts


def test_extract_failed_attempts_basic():
    lines = [
        "Jan 1 00:00:01 host sshd[123]: Failed password for root from 192.168.1.51 port 22 ssh2\n",
        "Jan 1 00:00:02 host sshd[124]: Failed password for invalid user admin from 192.168.1.50 port 22 ssh2\n",
        "Jan 1 00:00:03 host sshd[125]: Accepted password for root from 192.168.1.51 port 22 ssh2\n",
    ]

    user_counts, ip_counts, total_failed = extract_failed_attempts(lines)

    assert total_failed == 2
    assert user_counts["root"] == 1
    assert user_counts["admin"] == 1
    assert ip_counts["192.168.1.51"] == 1
    assert ip_counts["192.168.1.50"] == 1


def test_extract_failed_attempts_no_matches():
    lines = [
        "Jan 1 00:00:03 host sshd[125]: Accepted password for root from 192.168.1.51 port 22 ssh2\n",
        "Some unrelated log line\n",
    ]

    user_counts, ip_counts, total_failed = extract_failed_attempts(lines)

    assert total_failed == 0
    assert user_counts.most_common() == []
    assert ip_counts.most_common() == []
