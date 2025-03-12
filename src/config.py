from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Final

DB: Final = "postgresql"
DB_ENGINE: Final = "asyncpg"


class Settings(BaseSettings):
    MODE: Literal["TEST", "LOCAL", "DEV", "PROD"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"{DB}+{DB_ENGINE}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    API_HOST: str
    API_PORT: int

    CORS_ORIGIN: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
