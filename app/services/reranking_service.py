from sentence_transformers import CrossEncoder

class RerankingService:

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-v2-m3"
    ):

        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        chunks: list[dict],
        top_k: int = 3
    ) -> list[dict]:

        if not chunks:
            return []

        pairs = [
            [query, chunk["text"]]
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        reranked_chunks = []

        for chunk, score in zip(chunks, scores):
            reranked_chunks.append({
                **chunk,
                "rerank_score": float(score)
            })

        reranked_chunks.sort(
            key=lambda x : x["rerank_score"],
            reverse=True
        )

        return reranked_chunks[:top_k]