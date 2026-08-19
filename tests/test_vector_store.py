from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.vector_store.qdrant_store import QdrantStore

pages = [
    {
        "page": 1,
        "text": """
        Sinh viên muốn nhận học bổng phải đáp ứng
        các điều kiện sau. GPA phải đạt tối thiểu 3.2.

        Sinh viên không được vi phạm kỷ luật.
        """
    }
]

# 3
chunking_service = ChunkingService(
    chunk_size=100,
    chunk_overlap=20
)

chunks = chunking_service.chunk_pages(pages)

# 4
embedding_service = EmbeddingService()

embedded_chunks = embedding_service.embed_chunks(chunks)

# 5
vector_store = QdrantStore(
    collection_name="pdf_chunks",
    vector_size=1024
)

vector_store.add_chunks(embedded_chunks)

vector_store.close()

print("Chunks insert successfully")