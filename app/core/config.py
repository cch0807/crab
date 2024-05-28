from functools import lru_cache
from pathlib import Path

from pydantic import AnyHttpUrl, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_DIR = Path(__file__).parent.parent.parent


class Security(BaseModel):
    allowed_hosts: list[str] = ["localhost", "127.0.0.1"]
    backend_cors_origins: list[AnyHttpUrl] = []


class Redis(BaseModel):
    host: str = "redis"
    port: str = "6379"
    db: int = 0
    encoding: str = "utf-8"
    decode_responses: bool = True


class Settings(BaseSettings):
    security: Security
    redis: Redis

    model_config = SettingsConfigDict(
        env_file=f"{PROJECT_DIR}/.env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
