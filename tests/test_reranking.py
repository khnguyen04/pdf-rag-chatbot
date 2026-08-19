from app.services.reranking_service import RerankingService


query = "GPA tối thiểu để nhận học bổng là bao nhiêu?"


chunks = [
    {
        "document_id": "scholarship",
        "page": 1,
        "chunk_index": 0,
        "text": "Sinh viên muốn nhận học bổng phải đáp ứng các điều kiện sau.",
        "score": 0.70
    },
    {
        "document_id": "scholarship",
        "page": 1,
        "chunk_index": 1,
        "text": "GPA phải đạt tối thiểu 3.2.",
        "score": 0.65
    },
    {
        "document_id": "scholarship",
        "page": 1,
        "chunk_index": 2,
        "text": "Sinh viên không được vi phạm kỷ luật.",
        "score": 0.60
    }
]


reranking_service = RerankingService()


results = reranking_service.rerank(
    query=query,
    chunks=chunks,
    top_k=2
)


for index, result in enumerate(results):

    print("=" * 60)
    print(f"RESULT {index + 1}")

    print("Qdrant score:")
    print(result["score"])

    print("Rerank score:")
    print(result["rerank_score"])

    print("Text:")
    print(result["text"])