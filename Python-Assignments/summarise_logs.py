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
        latest_log = max(error_logs, key=lambda x: x.get("timestamp", ""))
        latest_error = latest_log.get("message")

    return {
        "counts": counts,
        "latest_error": latest_error
    }
    

# ─────────────────────────────────────────────
#  Tests
# ─────────────────────────────────────────────

def test_basic_counts():
    result = summarise_logs(logs)
    assert result["counts"].get("INFO")  == 1, "INFO count should be 1"
    assert result["counts"].get("WARN")  == 1, "WARN count should be 1"
    assert result["counts"].get("ERROR") == 2, "ERROR count should be 2"
    print("\u2713 test_basic_counts passed")      # Unicode(\u2713) tick mark for success indication

def test_latest_error():
    result = summarise_logs(logs)
    assert result["latest_error"] == "Timeout on request", \
        f"Expected 'Timeout on request', got '{result['latest_error']}'"
    print("\u2713 test_latest_error passed")


# ─────────────────────────────────────────────
#  Run
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("Running tests...\n")

    test_basic_counts()
    test_latest_error()

    print("\nAll tests passed!")
    print("\nSummary of sample logs:")
    print(summarise_logs(logs))
