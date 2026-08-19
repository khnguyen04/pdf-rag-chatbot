from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.retrieval_service import RetrievalService
from app.services.context_service import ContextService
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService
from app.services.reranking_service import RerankingService

from app.vector_store.qdrant_store import QdrantStore

# pages = [
#     {
#         "page": 1,
#         "text": """
#         Sinh viên muốn nhận học bổng phải đáp ứng
#         các điều kiện sau.

#         GPA phải đạt tối thiểu 3.2.

#         Sinh viên không được vi phạm kỷ luật.
#         """
#     }
# ]

# chunking_service = ChunkingService(
#     chunk_size=200,
#     chunk_overlap=30
# )

# chunks = chunking_service.chunk_pages(
#     pages
# )

embedding_service = EmbeddingService()

# embedded_chunks = embedding_service.embed_chunks(
#     chunks
# )

vector_store = QdrantStore(
    collection_name="pdf_chunks",
    vector_size=1024
)

# vector_store.add_chunks(
#     embedded_chunks,
#     document_id="scholarship"
# )

retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    vector_store=vector_store
)

question = "GPA tối thiểu để nhận học bổng là bao nhiêu?"

results = retrieval_service.retrieve(
    query=question,
    document_id="scholarship",
    top_k=3
)

reranking_service = RerankingService()

reranked_results = reranking_service.rerank(
    query=question,
    chunks=results,
    top_k=3
)

context_service = ContextService()

context, sources = context_service.build_context(
    reranked_results
)

prompt_service = PromptService()

prompt = prompt_service.build_prompt(
    question=question,
    context=context
)

llm_service = LLMService(
    model="qwen2.5:3b"
)

answer = llm_service.generate(
    prompt
)

print("=" * 60)
print("QUESTION")
print("=" * 60)

print(question)


print("=" * 60)
print("ANSWER")
print("=" * 60)

print(answer)


for source in sources:
    print(
        f"[SOURCE {source['source_id']}] "
        f"Document: {source['document_id']} "
        f"Page: {source['page']}"
    )
    
vector_store.close()