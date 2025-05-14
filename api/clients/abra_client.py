from api.models.abra_model import LoginRequestModel, LoginResponseModel
from api.models.error_models import ErrorResponseModel
from utils.common_checker import validate_response
from utils.http_client import ClientApi
import allure


class AbraClient(ClientApi):
    def __init__(self):
       super().__init__()

    @allure.step('POST /auth/sign-in')
    def login(self,
              login_request_data: LoginRequestModel,
              expect_error: bool = False,
              expected_status_code: int = 200
              ) -> LoginResponseModel | ErrorResponseModel:

        response = self.request(
            method='post',
            url='/auth/sign-in',
            json=login_request_data.model_dump()
        )
        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )
        return validate_response(
            model=LoginResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )
