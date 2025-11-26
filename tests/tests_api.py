import requests

BASE_URL = "http://localhost:8000"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_backup_flow():
    payload = {"backup_id": "test1", "data": "hello backup"}
    r = requests.post(f"{BASE_URL}/backup", json=payload)
    assert r.status_code == 200

    r2 = requests.get(f"{BASE_URL}/backup/test1")
    assert r2.status_code == 200
    body = r2.json()
    assert body["id"] == "test1"
    assert body["data"] == "hello backup"
