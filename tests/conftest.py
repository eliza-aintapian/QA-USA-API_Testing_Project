import json
import os
from pathlib import Path
from typing import Any, Dict, Generator

import pytest
import requests

CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config() -> Dict[str, Any]:
    if CONFIG_PATH.exists():
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


@pytest.fixture(scope="session")
def base_url() -> str:
    env_base_url = os.getenv("BASE_URL")
    if env_base_url:
        return env_base_url.rstrip("/")

    config = load_config()
    url = config.get("base_url")
    if not url:
        raise RuntimeError(
            "Base URL not configured. Set BASE_URL env var or tests/config.json"
        )
    return str(url).rstrip("/")


@pytest.fixture(scope="session")
def http_session() -> Generator[requests.Session, None, None]:
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json; charset=UTF-8"})
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="session")
def ensure_api_available(base_url: str, http_session: requests.Session) -> None:
    """Skip tests if the API is not reachable in this environment."""
    test_endpoint = f"{base_url}/posts/1"
    try:
        response = http_session.get(test_endpoint, timeout=10)
        if response.status_code != 200:
            pytest.skip(
                f"API not reachable or unexpected status: {response.status_code}"
            )
    except requests.RequestException as exc:
        pytest.skip(f"API not reachable: {exc}")
