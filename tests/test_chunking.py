from app.services.chunking_service import ChunkingService
from app.loaders.pdf_loader import PDFLoader

import json

output = {}

loader = PDFLoader()

pages = loader.load(
    "data/uploads/QuyDinh2026_Truong.pdf"
)


chunking_service = ChunkingService()

chunks = chunking_service.chunk_pages(pages)

for index, chunk in enumerate(chunks):
    output[f"Chunk_{index}"] = {
        "page": chunk['page'],
        "text": chunk['text']
    }
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)