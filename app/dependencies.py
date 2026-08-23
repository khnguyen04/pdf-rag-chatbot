from app.loaders.pdf_loader import PDFLoader
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.retrieval_service import RetrievalService
from app.services.reranking_service import RerankingService
from app.services.context_service import ContextService
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService
from app.services.rag_service import RAGService
from app.services.ingestion_service import IngestionService

from app.vector_store.qdrant_store import QdrantStore

from app.core.config import settings


# Shared services

pdf_loader = PDFLoader()

chunking_service = ChunkingService(
    chunk_size=settings.chunk_size,
    chunk_overlap=settings.chunk_overlap
)

embedding_service = EmbeddingService(
    model_name=settings.embedding_model
)

vector_store = QdrantStore(
    collection_name=settings.collection_name,
    vector_size=settings.vector_size
)

retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    vector_store=vector_store
)

reranking_service = RerankingService(
    model_name=settings.reranking_model
)

context_service = ContextService()

prompt_service = PromptService()

llm_service = LLMService(
    model=settings.llm_model
)

# Ingestion service

ingestion_service = IngestionService(
    pdf_loader=pdf_loader,
    chunking_service=chunking_service,
    embedding_service=embedding_service,
    vector_store=vector_store
)

def get_ingestion_service() -> IngestionService:
    return ingestion_service

# RAG service

rag_service = RAGService(
    retrieval_service=retrieval_service,
    reranking_service=reranking_service,
    context_service=context_service,
    prompt_service=prompt_service,
    llm_service=llm_service
)


def get_rag_service() -> RAGService:
    return rag_service