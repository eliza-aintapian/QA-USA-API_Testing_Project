import requests


def test_get_echoes_query_and_headers(base_url):
    params = {"search": "widgets", "page": "2"}
    headers = {"X-Test": "pytest"}
    resp = requests.get(f"{base_url}/get", params=params, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["args"]["search"] == "widgets"
    assert data["args"]["page"] == "2"
    assert data["headers"]["X-Test"] == "pytest"
    assert data["url"].startswith(f"{base_url}/get")
