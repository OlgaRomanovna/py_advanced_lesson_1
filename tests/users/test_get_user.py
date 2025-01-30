import pytest
import requests

from main import url


class TestGetUser:
    @pytest.mark.parametrize("user_id, expected_email", [
        (2, "janet.weaver@reqres.in"),])
    def test_get_user_successful(self, user_id, expected_email):
        response = requests.get(f"{url}/api/users/{user_id}")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        body = response.json()
        assert "data" in body, "Response body does not contain 'data' key"

        data = body["data"]

        assert data["id"] == user_id, f"Expected id {user_id}, but got {data['id']}"
        assert data["email"] == expected_email, f"Expected email {expected_email}, but got {data['email']}"

    def test_get_user_not_found(self):
        response = requests.get(f"{url}/api/users/34567890")
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
        assert response.json() == {}



