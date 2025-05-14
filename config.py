import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = pathlib.Path(__file__).resolve().parent / ".env"

class Settings(BaseSettings):
    BASE_URL_API: str = ""
    BASE_URL: str = ""
    ENVIRONMENT: str = ""
    EMAIL: str = ""
    PASSWORD: str = ""

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    model_config = SettingsConfigDict(env_file=str(DOTENV))

settings = Settings()
