from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends

from app.dependencies import get_ingestion_service
from app.services.ingestion_service import IngestionService

from app.core.logger import get_logger

logger = get_logger(__name__)

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
    file: UploadFile = File(...),
    ingestion_service: IngestionService = Depends(get_ingestion_service)
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

    logger.info(
        "Starting PDF ingestion: %s",
        file.filename
    )

    result = ingestion_service.ingest(
        file_path=str(file_path),
        document_id=document_id
    )

    logger.info(
        "PDF ingestion completed: %s",
        file.filename
    )

    return {
        "message": "PDF uploaded and indexed successfully.",
        "filename": file.filename,
        **result
    }