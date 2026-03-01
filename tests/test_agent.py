"""
Test file for skill logic.
We test skills directly because that is the "business logic" we care about.
"""

from skills.analyze_log import analyze_log_file


def test_analyze_log_file_returns_expected_values(tmp_path):
    """
    Ensure analyze_log_file returns correct structured data.
    """
    log = tmp_path / "secure.log"
    log.write_text(
        "Failed password for root from 192.168.1.51 port 22 ssh2\n"
        "Failed password for invalid user admin from 192.168.1.50 port 22 ssh2\n"
        "Accepted password for root from 192.168.1.51 port 22 ssh2\n"
    )

    report = analyze_log_file(str(log))

    assert report["total_failed"] == 2
    assert ("root", 1) in report["top_users"]
    assert ("admin", 1) in report["top_users"]
    assert ("192.168.1.51", 1) in report["top_ips"]
    assert ("192.168.1.50", 1) in report["top_ips"]
