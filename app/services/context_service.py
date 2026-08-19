class ContextService:

    def build_context(
        self,
        chunks: list[dict]
    ) -> str:

        context_parts = []
        sources = []

        for index, chunk in enumerate(chunks):

            source_id =index + 1
            
            context_parts.append(
                f"[SOURCE {source_id}]\n"
                f"Document: {chunk['document_id']}\n"
                f"Page: {chunk['page']}\n"
                f"{chunk['text']}"
            )

            sources.append({
                "source_id": source_id,
                "document_id": chunk["document_id"],
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"]
            })
        
        context = "\n\n".join(context_parts)

        return context, sources
        