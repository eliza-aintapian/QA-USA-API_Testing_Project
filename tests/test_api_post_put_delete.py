import requests
import uuid


def test_post_returns_sent_json(base_url):
    payload = {"title": f"title-{uuid.uuid4().hex}", "body": "hello", "userId": 1}
    resp = requests.post(f"{base_url}/post", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["json"] == payload


def test_put_updates_and_echoes_json(base_url):
    payload = {"id": 123, "title": "updated-title"}
    resp = requests.put(f"{base_url}/put", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["json"] == payload


def test_delete_returns_200_and_url(base_url):
    resp = requests.delete(f"{base_url}/delete")
    assert resp.status_code == 200
    data = resp.json()
    assert data["url"].endswith("/delete")
