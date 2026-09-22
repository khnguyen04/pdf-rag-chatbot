from app.loaders.pdf_loader import PDFLoader
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.ingestion_service import IngestionService
from app.vector_store.qdrant_store import QdrantStore

from app.core.config import settings

pdf_loader = PDFLoader()

chunking_service = ChunkingService(
    chunk_size=1000,
    chunk_overlap=200
)

embedding_service = EmbeddingService(settings.embedding_model)

vector_store = QdrantStore(
    collection_name="pdf_chunks",
    vector_size=1024
)


ingestion_service = IngestionService(
    pdf_loader=pdf_loader,
    chunking_service=chunking_service,
    embedding_service=embedding_service,
    vector_store=vector_store
)


result = ingestion_service.ingest(
    file_path="data/uploads/QuyDinh2026_Truong.pdf",
    document_id="QuyDinh2026_Truong"
)

print(result)