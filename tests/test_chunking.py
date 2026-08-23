from app.services.chunking_service import ChunkingService
from app.loaders.pdf_loader import PDFLoader


loader = PDFLoader()

pages = loader.load(
    "data/uploads/QuyDinh2026_Truong.pdf"
)


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