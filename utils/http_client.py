import typing
from typing import Optional

import requests
from config import settings
from utils.allure_helper import AllureHelper


class ClientApi:
    def __int__(self) -> None:
        self.settings = settings
        self.env = settings.ENVIRONMENT
        self.BASE_URL_API = settings.BASE_URL_API
        self.allure_helper = AllureHelper()
        self._session = self._initialize_session()

    @staticmethod
    def _initialize_session() -> requests.Session:
        return requests.Session()



    def request(self,
                method: str,
                url: typing.Optional[str] = None,
                params: typing.Optional[dict] = None,
                headers: typing.Optional[dict] = None,
                cookies: typing.Optional[dict] = None,
                files: typing.Optional[dict] = None,
                json: typing.Optional[dict] = None,
                data: typing.Optional[dict | str | list] = None,
                #allow_redirects: bool = True,
                #cert: typing.Optional[str | tuple] = None,
                verify: bool = False,
                timeout: typing.Optional[float] = None,
    ) -> requests.Response:
        response = self._session.request(
            method=method,
            #url=special_url
            #   or f"https://{self.service}.{self.base_url}.{self.env}{url}",
            url = self.BASE_URL_API + url,
            headers=headers,
            params=params,
            cookies=cookies,
            json=json,
            data=data,
            files=files,
            #allow_redirects=allow_redirects,
            #cert=cert,
            verify=verify,
            timeout=timeout,
        )
        self.allure_helper.enrich_allure(response)
        return response
