import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    client = APIClient("https://api.example.com")
    yield client

@pytest.fixture(scope="module")
def token(api_client):
    login_response = api_client.login("test_user", "secure_password")
    return login_response['token']

def test_get_transaction_history(api_client, token):
    response = api_client.get_transaction_history(token)
    assert response['status'] == 'success'
    assert isinstance(response['transactions'], list)
