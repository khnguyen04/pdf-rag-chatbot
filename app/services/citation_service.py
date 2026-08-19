from dns import enum
class CitationService:
    
    def build_sources(
        self,
        chunks: list[dict]
    ) -> list[dict]:

        sources = []

        for index, chunk in enumerate(chunks):

            sources.append({
                "source_id": index + 1,
                "document_id": chunk["document_id"],
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"]
            })

        return sources