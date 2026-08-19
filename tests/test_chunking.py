from app.services.chunking_service import ChunkingService

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

chunking_service = ChunkingService(
    chunk_size=100,
    chunk_overlap=20
)

chunks = chunking_service.chunk_pages(pages)

for index, chunk in enumerate(chunks):
    print("="*50)
    print(f"CHUNK {index}")
    print(f"PAGE: {chunk['page']}")
    print(chunk['text'])