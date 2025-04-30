from calendar import error

import allure
import pytest

from api.clients.abra_client import AbraClient
from api.models.abra_model import LoginRequestModel, LoginResponseModel
from config import settings
from utils.common_checker import check_difference_between_objects


@pytest.mark.api
class TestSignIn:
    @allure.title("Test successful log in")
    @allure.description("Test successful log in")
    def test_login(
            self,
            abra_client: AbraClient,
            email: settings.EMAIL,
            password: settings.PASSWORD):
        login_request_data = LoginRequestModel(
            email=email,
            password=password
        )
        login = abra_client.login(login_request_data=login_request_data)
        expected_response = LoginResponseModel(
            ok=True,
            result=True,
            detail="Login successful",
            error="",
            error_code=0
        )
        check_difference_between_objects(actual_result=login, expected_result=expected_response)

