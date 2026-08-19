from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_version: str
    llm_model: str
    vector_size: int
    collection_name: str

    class Config:
        env_file = ".env"


settings = Settings()