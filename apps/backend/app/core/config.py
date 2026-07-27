from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str

    OPENAI_API_KEY: str = ""

    GEMINI_API_KEY: str = ""

    JWT_SECRET_KEY: str

    REDIS_URL: str

    EMAIL_HOST: str = ""

    EMAIL_PORT: int = 587

    EMAIL_USERNAME: str = ""

    EMAIL_PASSWORD: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()