import os
import time
import pytest
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def _wait_up():
    for _ in range(30):
        try:
            r = requests.get(f"{BASE_URL}/health", timeout=2)
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError("Service did not start in time")

@pytest.mark.acceptance
def test_health():
    _wait_up()
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

@pytest.mark.acceptance
def test_sum():
    _wait_up()
    r = requests.get(f"{BASE_URL}/sum", params={"a": 1, "b": 2}, timeout=5)
    assert r.status_code == 200
    assert r.json()["result"] == 3
