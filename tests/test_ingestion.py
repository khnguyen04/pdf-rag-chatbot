from app.loaders.pdf_loader import PDFLoader
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.ingestion_service import IngestionService
from app.vector_store.qdrant_store import QdrantStore


pdf_loader = PDFLoader()

chunking_service = ChunkingService(
    chunk_size=1000,
    chunk_overlap=200
)

embedding_service = EmbeddingService()

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
    file_path="data/uploads/scholarship.pdf",
    document_id="scholarship"
)

print(result)