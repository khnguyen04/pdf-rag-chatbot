from app.services.embedding_service import EmbeddingService
from app.services.retrieval_service import RetrievalService
from app.services.reranking_service import RerankingService
from app.services.context_service import ContextService
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService
from app.services.rag_service import RAGService

from app.vector_store.qdrant_store import QdrantStore

from app.core.config import settings

def create_rag_service():

    embedding_service = EmbeddingService()

    vector_store = QdrantStore(
        collection_name=settings.collection_name,
        vector_size=settings.vector_size
    )

    retrieval_service = RetrievalService(
        embedding_service=embedding_service,
        vector_store=vector_store
    )

    reranking_service = RerankingService()

    context_service = ContextService()

    prompt_service = PromptService()

    llm_service = LLMService(
        model=settings.llm_model
    )

    return RAGService(
        retrieval_service=retrieval_service,
        reranking_service=reranking_service,
        context_service=context_service,
        prompt_service=prompt_service,
        llm_service=llm_service
    )