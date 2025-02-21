import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """Fixture to create a single instance of the APIClient for all tests."""
    client = APIClient("https://api.example.com")
    yield client

@pytest.fixture(scope="module")
def token(api_client):
    """Fixture to handle user login and provide a token for authentication."""
    login_response = api_client.login("test_user", "secure_password")
    assert login_response['status'] == 'success'
    return login_response['token']
