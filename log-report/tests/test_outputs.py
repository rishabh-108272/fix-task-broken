import json
from pathlib import Path

def get_report_data():
    path = Path("/app/report.json")
    if not path.exists():
        raise AssertionError("report.json not found")
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        raise AssertionError(f"report.json is not valid JSON: {e}")

def test_total_requests():
    """Verifies success criterion 1: total_requests matches the total number of requests in the access log."""
    data = get_report_data()
    assert "total_requests" in data, "total_requests key is missing"
    assert data["total_requests"] == 6, f"Expected total_requests to be 6, got {data['total_requests']}"

def test_unique_ips():
    """Verifies success criterion 2: unique_ips matches the number of unique client IP addresses."""
    data = get_report_data()
    assert "unique_ips" in data, "unique_ips key is missing"
    assert data["unique_ips"] == 3, f"Expected unique_ips to be 3, got {data['unique_ips']}"

def test_top_path():
    """Verifies success criterion 3: top_path matches the most frequently requested path."""
    data = get_report_data()
    assert "top_path" in data, "top_path key is missing"
    assert data["top_path"] == "/index.html", f"Expected top_path to be '/index.html', got '{data['top_path']}'"
