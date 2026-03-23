# Log summariser
# Sample log data - each log entry is a dictionary with 'timestamp', 'level', and 'message' keys
logs = [
    {"timestamp": "2024-01-01T10:00:00", "level": "INFO",  "message": "Server started"},
    {"timestamp": "2024-01-01T10:05:00", "level": "WARN",  "message": "High memory usage"},
    {"timestamp": "2024-01-01T10:07:00", "level": "ERROR", "message": "DB connection failed"},
    {"timestamp": "2024-01-01T10:09:00", "level": None,    "message": "Unknown event"},
    {"timestamp": "2024-01-01T10:11:00", "level": "ERROR", "message": "Timeout on request"},
]

def summarise_logs(logs, filter_level=None):
    """
    Summarise a list of log entry dicts.

    Args:
        logs (list): List of dicts with keys: timestamp, level, message.
        filter_level (str | None): If provided, return only entries of this level.

    Returns:
        dict: {
            "counts": {"INFO": n, "WARN": n, "ERROR": n},
            "latest_error": str | None
        }
    """
    counts = {}
    error_logs = []

    # Apply filter if given
    if filter_level:
        logs = [log for log in logs if log.get("level") == filter_level]

    # Process logs
    for log in logs:
        level = log.get("level")

        # Skip invalid levels
        if level is None:
            continue

        # Count levels
        counts[level] = counts.get(level, 0) + 1

        # Collect ERROR logs
        if level == "ERROR":
            error_logs.append(log)

    # Find latest ERROR
    latest_error = None

    if error_logs:
        # Using lambda(a one-line function) to extract timestamp from each log and find the most recent one
        latest_log = max(error_logs, key=lambda x: x.get("timestamp", ""))
        latest_error = latest_log.get("message")

    return {
        "counts": counts,
        "latest_error": latest_error
    }
    

# ─────────────────────────────────────────────
#  Tests
# ─────────────────────────────────────────────
# counts should be correct
def test_basic_counts():
    result = summarise_logs(logs)
    assert result["counts"].get("INFO")  == 1, "INFO count should be 1"
    assert result["counts"].get("WARN")  == 1, "WARN count should be 1"
    assert result["counts"].get("ERROR") == 2, "ERROR count should be 2"
    print("\u2713 test_basic_counts passed")      # Unicode(\u2713) tick mark for success indication

# latest_error should be the message of the most recent ERROR log
def test_latest_error():
    result = summarise_logs(logs)
    assert result["latest_error"] == "Timeout on request", \
        f"Expected 'Timeout on request', got '{result['latest_error']}'"
    print("\u2713 test_latest_error passed")

# none_level_skipped should skip logs with None level
def test_none_level_skipped():
    test_logs = [
        {"timestamp": "2024-01-01T10:00:00", "level": None,   "message": "Ghost entry"},
        {"timestamp": "2024-01-01T10:01:00", "level": "INFO", "message": "Normal entry"},
    ]
    result = summarise_logs(test_logs)
    assert result["counts"].get("INFO") == 1, "INFO count should be 1"
    assert None not in result["counts"],      "None should not appear as a key"
    print("\u2713 test_none_level_skipped passed")

# when no ERROR logs exist, latest_error should be None
def test_no_errors_returns_none():
    test_logs = [
        {"timestamp": "2024-01-01T10:00:00", "level": "INFO", "message": "All good"},
        {"timestamp": "2024-01-01T10:01:00", "level": "WARN", "message": "Watch out"},
    ]
    result = summarise_logs(test_logs)
    assert result["latest_error"] is None, "latest_error should be None when no ERRORs exist"
    print("\u2713 test_no_errors_returns_none passed")

# when logs list is empty, counts should be empty and latest_error should be None
def test_empty_list():
    result = summarise_logs([])
    assert result["counts"] == {}, "counts should be empty dict"
    assert result["latest_error"] is None, "latest_error should be None"
    print("\u2713 test_empty_list passed")

# Return only ERROR entries when filter_level is set to "ERROR"
def test_filter_level():
    result = summarise_logs(logs, filter_level="ERROR")
    assert result["counts"] == {"ERROR": 2}
    assert result["latest_error"] == "Timeout on request"
    print("\u2713 test_filter_level passed")



# ─────────────────────────────────────────────
#  Run
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("Running tests...\n")

    test_basic_counts()
    test_latest_error()
    test_none_level_skipped()
    test_no_errors_returns_none()
    test_empty_list()
    test_filter_level()

    print("\nAll tests passed!")
    print("\nSummary of sample logs:")
    print(summarise_logs(logs))
