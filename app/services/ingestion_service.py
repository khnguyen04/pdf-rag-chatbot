class IngestionService:

    def __init__(
        self,
        pdf_loader,
        chunking_service,
        embedding_service,
        vector_store
    ):
        self.pdf_loader = pdf_loader
        self.chunking_service = chunking_service
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def ingest(
        self,
        file_path: str,
        document_id: str
    ):

        # 1. PDF -> pages
        pages = self.pdf_loader.load(
            file_path
        )

        # 2. pages -> chunks
        chunks = self.chunking_service.chunk_pages(
            pages
        )

        # 3. Add metadata
        for index, chunk in enumerate(chunks):
            chunk["document_id"] = document_id
            chunk["chunk_index"] = index

        # 4. chunks -> embeddings
        embedded_chunks = (
            self.embedding_service.embed_chunks(
                chunks
            )
        )

        # 5. embeddings -> Qdrant
        self.vector_store.add_chunks(
            embedded_chunks,
            document_id=document_id
        )

        self.vector_store.close()
        
        return {
            "document_id": document_id,
            "pages": len(pages),
            "chunks": len(chunks)
        }