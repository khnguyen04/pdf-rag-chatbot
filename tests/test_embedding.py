from app.services.embedding_service import EmbeddingService


embedding_service = EmbeddingService()


text = "Sinh viên phải đạt GPA tối thiểu 3.2"

embedding = embedding_service.embed_text(text)


print("Embedding type:", type(embedding))
print("Embedding dimension:", len(embedding))
print("First 10 values:", embedding[:10])