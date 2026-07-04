"""
Application configuration settings for K² Sentinel.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Central configuration loaded from environment variables.
    """

    PROJECT_NAME: str = "K² Sentinel"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    API_PREFIX: str = "/api/v1"

    LOG_LEVEL: str = "INFO"

    DATABASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"


# ✅ THIS IS WHAT WAS MISSING (CRITICAL FIX)
settings = Settings()