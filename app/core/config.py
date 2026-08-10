from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PDF RAG Chatbot"
    app_version: str = "0.1.0"

    class Config:
        env_file = ".env"


settings = Settings()