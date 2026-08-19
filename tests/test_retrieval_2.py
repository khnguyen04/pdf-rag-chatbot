from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.retrieval_service import RetrievalService
from app.vector_store.qdrant_store import QdrantStore

pages_a = [
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

pages_b = [
    {
        "page": 1,
        "text": """
        Sinh viên phải đóng học phí trước ngày
        30 tháng 9.

        Học phí học kỳ là 15 triệu đồng.
        """
    }
]


chunking_service = ChunkingService(
    chunk_size=100,
    chunk_overlap=20
)

embedding_service = EmbeddingService()

vector_store = QdrantStore(
    collection_name="pdf_chunks",
    vector_size=1024
)

# Document a
chunks_a = chunking_service.chunk_pages(
    pages_a
)

embedded_a = embedding_service.embed_chunks(
    chunks_a
)

vector_store.add_chunks(
    embedded_a,
    document_id="scholarship"
)

# Document b
chunks_b = chunking_service.chunk_pages(
    pages_b
)

embedded_b = embedding_service.embed_chunks(
    chunks_b
)

vector_store.add_chunks(
    embedded_b,
    document_id="tuition"
)

retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    vector_store=vector_store
)

results = retrieval_service.retrieve(
    query="GPA tối thiểu để nhận học bổng là bao nhiêu?",
    document_id="scholarship",
    top_k=3
)

for i, result in enumerate(results):

    print("=" * 60)

    print(f"RESULT {i + 1}")

    print("Score:", result["score"])

    print("Document:", result["document_id"])

    print("Page:", result["page"])

    print("Text:")

    print(result["text"])


vector_store.close()