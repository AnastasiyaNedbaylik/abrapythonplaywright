import pytest
import requests

from api.clients.abra_client import AbraClient
from api.clients.postgres_client import PostgresClient


@pytest.fixture(autouse=True)
def abra_client() -> AbraClient:
    return AbraClient()

@pytest.fixture(autouse=True)
def postgres_client() -> PostgresClient:
    return PostgresClient()
