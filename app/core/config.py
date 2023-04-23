import os
from pathlib import Path
from typing import Any, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_PATH: str = "/api"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, list[str]]
    ) -> Union[list[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]
    SQLALCHEMY_ASYNC_DATABASE_URI: Optional[str]

    @validator("POSTGRES_DB", always=True)
    def postgres_db(cls, value: Optional[str]) -> Any:
        return value if os.getenv('TEST', 'False') == 'False' else 'test'

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: Optional[str], values: dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=str(values.get("POSTGRES_PORT")),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    @validator("SQLALCHEMY_ASYNC_DATABASE_URI", pre=True)
    def assemble_async_db_connection(
        cls, v: Optional[str], values: dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return (
            f"postgresql+asyncpg://"
            f'{values.get("POSTGRES_USER")}:'
            f'{values.get("POSTGRES_PASSWORD")}@'
            f'{values.get("POSTGRES_SERVER")}:'
            f'{values.get("POSTGRES_PORT")}/'
            f'{values.get("POSTGRES_DB") or ""}'
        )

    RUN_INIT_SCRIPT: Optional[bool]

    DOMAIN: str

    BASE_DIR: str = str(Path(os.path.dirname(__file__)).parents[1])
    BASE_DIR_APP: str = str(Path(os.path.dirname(__file__)).parents[0])

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
