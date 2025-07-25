import requests

from utils.static_configutation import BASE_URL


class TestLoginAPI:

    def test_login_valid_credentials(self):
        payload = {"username": "admin", "password": "1234"}
        response = requests.post(f"{BASE_URL}/login", json=payload)
        assert response.status_code == 200, f"Expected status code 200 but the response status code is {response.status_code}"
        assert response.json().get("success")

    def test_login_invalid_credentials(self):
        payload = {"username": "invalid", "password": "wrong"}
        response = requests.post(f"{BASE_URL}/login", json=payload)
        assert response.status_code == 401, f"Expected status code 401 but the response status code is {response.status_code}"
        assert "error" in response.json()
