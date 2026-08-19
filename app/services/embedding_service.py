from sentence_transformers import SentenceTransformer


class EmbeddingService:
    
    def __init__(
        self,
        model_name: str = "BAAI/bge-m3"
    ):
        self.model = SentenceTransformer(model_name)

    def embed_text(
        self,
        text: str
    ) -> list[float]:

        embeding = self.model.encode(
            text,
            normalize_embeddings = True
        )

        return embeding.tolist()

    def embed_chunks(
        self,
        chunks: list[dict]
    ) -> list[dict]:

        results = []

        for chunk in chunks:
            embedding = self.embed_text(
                chunk["text"]
            ) 

            results.append({
                **chunk,
                "embedding": embedding
            })
        
        return results