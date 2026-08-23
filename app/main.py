from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.chat import router as chat_router
from app.api.upload_pdf import router as upload_pdf_router
from app.pages import router as pages_router

from app.core.config import settings
from app.dependencies import vector_store

from app.core.logger import get_logger
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting PDF RAG application...")

    yield

    logger.info("Shutting down PDF RAG application...")

    vector_store.close()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan
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