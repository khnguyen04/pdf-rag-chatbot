from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/rag")
async def rag_page():
    return FileResponse("app/templates/rag.html")