import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        response = requests.post(f"{self.base_url}/login", json={"username": username, "password": password})
        return response.json()

    def make_payment(self, token, amount):
        response = requests.post(f"{self.base_url}/pay", json={"token": token, "amount": amount})
        return response.json()

    def get_transaction_history(self, token):
        response = requests.get(f"{self.base_url}/transactions", headers={"Authorization": f"Bearer {token}"})
        return response.json()
