from app.services.context_service import ContextService

chunks = [
    {
        "document_id": "scholarship",
        "page": 1,
        "chunk_index": 0,
        "text": "Sinh viên muốn nhận học bổng phải đáp ứng các điều kiện sau.",
        "score": 0.82
    },
    {
        "document_id": "scholarship",
        "page": 1,
        "chunk_index": 1,
        "text": "GPA phải đạt tối thiểu 3.2.",
        "score": 0.79
    }
]

context_service = ContextService()

context = context_service.build_context(
    chunks
)

print("=" * 60)
print(context)