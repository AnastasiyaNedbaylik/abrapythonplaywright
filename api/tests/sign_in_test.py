import allure
import pytest

from api.clients.abra_client import AbraClient
from api.clients.postgres_client import PostgresClient
from api.models.abra_model import LoginRequestModel, LoginResponseModel
from api.models.postgres_model import UserModel
from config import settings
from utils.common_checker import check_difference_between_objects


#@pytest.mark.api
class TestSignIn:
    @allure.title("Test successful log in")
    @allure.description("Test successful log in")
    def test_login(
            self,
            abra_client: AbraClient,
            postgres_client: PostgresClient):
        email = settings.EMAIL
        password= settings.PASSWORD
        login_request_data = LoginRequestModel(
            email=email,
            password=password
        )
        login = abra_client.login(login_request_data=login_request_data
                                  #expect_error=True,
                                  #expected_status_code=422,
                                  )
        expected_response = LoginResponseModel(
            ok=True,
            result=True
        )
        check_difference_between_objects(actual_result=login, expected_result=expected_response)
        postgres_client.check_user_from_db(is_deleted=False,
                                           is_verified=True,
                                           email=settings.EMAIL,
                                           expected_user=UserModel(email=settings.EMAIL, is_verified=True, is_deleted=False),
                                           )
        assert len(postgres_client.get_user_from_db(email=settings.EMAIL,
                                                    is_deleted=False,
                                                    is_verified=True)) == 1
