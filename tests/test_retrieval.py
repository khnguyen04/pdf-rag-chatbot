from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.retrieval_service import RetrievalService
from app.vector_store.qdrant_store import QdrantStore

pages = [
    {
        "page": 1,
        "text": """
        Sinh viên muốn nhận học bổng phải đáp ứng
        các điều kiện sau.

        GPA phải đạt tối thiểu 3.2.

        Sinh viên không được vi phạm kỷ luật.
        """
    }
]


# Step 3: Chunking
chunking_service = ChunkingService(
    chunk_size=100,
    chunk_overlap=20
)

chunks = chunking_service.chunk_pages(
    pages
)


# Step 4: Embedding
embedding_service = EmbeddingService()

embedded_chunks = embedding_service.embed_chunks(
    chunks
)


# Step 5: Vector DB
vector_store = QdrantStore(
    collection_name="pdf_chunks",
    vector_size=1024
)

vector_store.add_chunks(
    embedded_chunks
)


# Step 6: Retrieval
retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    vector_store=vector_store
)


query = "GPA tối thiểu để nhận học bổng là bao nhiêu?"


results = retrieval_service.retrieve(
    query=query,
    top_k=3
)


for i, result in enumerate(results):

    print("=" * 60)

    print(f"RESULT {i + 1}")

    print("Score:", result["score"])

    print("Page:", result["page"])

    print("Text:")

    print(result["text"])


vector_store.close()