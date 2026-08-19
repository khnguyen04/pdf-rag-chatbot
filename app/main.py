from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.chat import router as chat_router
from app.api.upload_pdf import router as upload_pdf_router
from app.pages import router as pages_router

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

@app.get("/")
async def root():
    return {
        "message": "PDF RAG Chatbox is running"
    }

app.include_router(chat_router)
app.include_router(upload_pdf_router)
app.include_router(pages_router)
