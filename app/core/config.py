from torch import embedding
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_version: str
    llm_model: str
    vector_size: int
    collection_name: str
    chunk_size: int
    chunk_overlap: int
    embedding_model: str
    reranking_model: str

    class Config:
        env_file = ".env"


settings = Settings()