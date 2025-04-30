import pytest
import requests

from api.clients.abra_client import AbraClient


@pytest.fixture(scope="session")
def abra_client() -> AbraClient:
    return AbraClient()