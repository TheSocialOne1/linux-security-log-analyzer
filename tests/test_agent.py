from agent import analyze_log_file


def test_analyze_log_file_returns_expected_keys(tmp_path):
    log = tmp_path / "secure.log"
    log.write_text(
        "Failed password for root from 192.168.1.51\n"
        "Failed password for invalid user admin from 192.168.1.50\n"
    )

    report = analyze_log_file(str(log))

    assert report["total_failed"] == 2
    assert "top_users" in report
    assert "top_ips" in report
