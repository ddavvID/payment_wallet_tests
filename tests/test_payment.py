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

def test_make_payment_success(api_client, token):
    response = api_client.make_payment(token, 100)
    assert response['status'] == 'success'
    assert response['transaction_id'] is not None

def test_make_payment_failure(api_client, token):
    response = api_client.make_payment(token, -50)  # Invalid amount
    assert response['status'] == 'failure'
