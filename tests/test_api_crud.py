import pytest
import requests


def test_get_post_by_id(base_url: str, http_session: requests.Session, ensure_api_available) -> None:
    response = http_session.get(f"{base_url}/posts/1", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("id") == 1
    assert isinstance(data.get("title"), str)
    assert "userId" in data


def test_create_post(base_url: str, http_session: requests.Session, ensure_api_available) -> None:
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = http_session.post(f"{base_url}/posts", json=payload, timeout=10)
    assert response.status_code == 201
    data = response.json()
    for key, value in payload.items():
        assert data.get(key) == value
    assert "id" in data


def test_update_post(base_url: str, http_session: requests.Session, ensure_api_available) -> None:
    post_id = 1
    payload = {"id": post_id, "title": "updated title", "body": "updated body", "userId": 1}
    response = http_session.put(f"{base_url}/posts/{post_id}", json=payload, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data.get("id") == post_id
    assert data.get("title") == payload["title"]
    assert data.get("body") == payload["body"]
    assert data.get("userId") == payload["userId"]


def test_delete_post(base_url: str, http_session: requests.Session, ensure_api_available) -> None:
    post_id = 1
    response = http_session.delete(f"{base_url}/posts/{post_id}", timeout=10)
    assert response.status_code in (200, 204)
    if response.status_code == 200:
        data = response.json()
        assert data == {} or isinstance(data, dict)
