import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.main import get_application

TEST_BEARER_TOKEN = "test_token"
os.environ["BEARER_TOKEN"] = TEST_BEARER_TOKEN


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    app = get_application()
    with TestClient(app) as client:
        yield client
