class RetrievalService:

    def __init__(
        self,
        embedding_service,
        vector_store
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        document_id: str,
        top_k: int = 3
    ) -> list[dict]:

        query_embedding = (
            self.embedding_service
            .embed_text(query)
        )

        results = self.vector_store.search(
            query_vector=query_embedding,
            top_k=top_k,
            document_id=document_id
        )

        retrieved_chunks = []

        for result in results:
            retrieved_chunks.append({
                "document_id": result.payload.get("document_id"),
                "page": result.payload.get("page"),
                "chunk_index": result.payload.get("chunk_index"),
                "text": result.payload.get("text"),
                "score": result.score
            })

        return retrieved_chunks