import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    client = APIClient("https://api.example.com")
    yield client

def test_login_success(api_client):
    response = api_client.login("test_user", "secure_password")
    assert response['status'] == 'success'
    assert 'token' in response

def test_login_failure(api_client):
    response = api_client.login("test_user", "wrong_password")
    assert response['status'] == 'failure'
