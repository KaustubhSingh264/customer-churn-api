from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Customer Churn Prediction API"
    app_version: str = "1.0.0"
    environment: str = "development"


settings = Settings()