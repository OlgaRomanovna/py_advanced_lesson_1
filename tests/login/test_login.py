import copy

import pytest
import requests

from main import url

payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }


class TestLoginUser:

    @pytest.mark.parametrize("expected_token",
        ["QpwL5tke4Pnpja7X4"])
    def test_login_user_successful(self, expected_token):
        response = requests.post(f"{url}/api/login", json=payload)
        print(response.json())
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["token"] == expected_token

    @pytest.mark.parametrize("expected_error",
                             ["Missing password"])
    def test_login_user_without_password(self, expected_error):
        copy_data = copy.deepcopy(payload)
        copy_data.pop("password")
        response = requests.post(f"{url}/api/login", json=copy_data)
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        assert response.json()["error"] == expected_error

    @pytest.mark.parametrize("expected_error",
                             ["Missing email or username"])
    def test_login_user_without_email(self, expected_error):
        copy_data = copy.deepcopy(payload)
        copy_data.pop("email")
        response = requests.post(f"{url}/api/login", json=copy_data)
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        assert response.json()["error"] == expected_error

    @pytest.mark.parametrize("expected_error",
                             ["user not found"])
    def test_login_user_with_wrong_password(self, expected_error):
        copy_data = copy.deepcopy(payload)
        copy_data["password"] = "ertyuio"
        response = requests.post(f"{url}/api/login", json=copy_data)
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        assert response.json()["error"] == expected_error
