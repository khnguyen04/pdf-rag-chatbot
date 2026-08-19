from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import create_rag_service
from app.services.rag_service import RAGService

class ChatRequest(BaseModel):
    document_id: str
    question: str

class Source(BaseModel):
    source_id: int
    document_id: str
    page: int
    chunk_index: int

class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]

router = APIRouter(
    prefix="/api",
    tags=["chat"]
)

@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    rag_service: RAGService = Depends(create_rag_service)
):

    return rag_service.ask(
        question=request.question,
        document_id=request.document_id
    )
