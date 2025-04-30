import pathlib

import pydantic_settings

DOTENV = str(pathlib.Path(__file__).resolve().parents[1] / ".env")


class Settings(pydantic_settings.BaseSettings):
    BASE_URL_API: str = ""
    BASE_URL: str = ""
    ENVIRONMENT: str = ""
    EMAIL: str = ""
    PASSWORD: str = ""


settings = Settings
