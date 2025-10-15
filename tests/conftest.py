import os
import yaml
import pytest


def _load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@pytest.fixture(scope="session")
def base_url() -> str:
    # Allow override via env var for CI/CD flexibility
    env_override = os.getenv("API_BASE_URL")
    if env_override:
        return env_override.rstrip("/")

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, "config", "config.yaml")
    cfg = _load_config(config_path)
    url = cfg.get("base_url")
    if not url:
        raise ValueError("'base_url' missing in config.yaml or env override")
    return str(url).rstrip("/")
