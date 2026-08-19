from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.ingestion_service import IngestionService
from app.loaders.pdf_loader import PDFLoader
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.vector_store.qdrant_store import QdrantStore


router = APIRouter(
    prefix="/api",
    tags=["upload_pdf"]
)


UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload_pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    file_path = UPLOAD_DIR / file.filename

    file_path.write_bytes(content)
    document_id = Path(file.filename).stem

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
        file_path=str(file_path),
        document_id=document_id
    )

    vector_store.close()

    return {
        "message": "PDF uploaded and indexed successfully.",
        "filename": file.filename,
        **result
    }