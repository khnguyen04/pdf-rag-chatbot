import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from qdrant_client.models import Filter, FieldCondition, MatchValue

class QdrantStore:

    def __init__(
        self,
        collection_name: str,
        vector_size: int
    ):
        self.collection_name = collection_name

        self.client = QdrantClient(
            path="./data/qdrant"
        )

        self._create_collection(vector_size)

    def close(self):
        self.client.close()

    def _create_collection(
        self,
        vector_size: int
    ):
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                )
            )

    def add_chunks(
        self,
        chunks: list[dict],
        document_id: str
    ):
        points = []

        for index, chunk in enumerate(chunks):

            point_id = str(
                uuid.uuid5(
                    uuid.NAMESPACE_DNS,
                    f"{document_id}_{index}"
                )
            )

            points.append(
                PointStruct(
                    id = point_id,
                    vector = chunk["embedding"],
                    payload={
                        "document_id": document_id,
                        "page": chunk["page"],
                        "chunk_index": index,
                        "text": chunk["text"]
                    }
                )
            )
        
        self.client.upsert(
            collection_name = self.collection_name,
            points = points
        )

    def search(
        self,
        query_vector: list[float],
        top_k: int = 3,
        document_id: str | None = None
    ):
        query_filter = None

        if document_id:
            query_filter = Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match = MatchValue(
                            value=document_id
                        )
                    )
                ]
            )

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            query_filter=query_filter,
            limit=top_k,
            with_payload=True
        )

        return results.points