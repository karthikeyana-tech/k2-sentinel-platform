from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    PROJECT_NAME: str = "K² Sentinel API"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # Environment
    ENVIRONMENT: str = "development"

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env.example",
        extra="ignore",
    )


settings = Settings()