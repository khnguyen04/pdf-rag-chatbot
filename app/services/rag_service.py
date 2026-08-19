class RAGService:

    def __init__(
        self,
        retrieval_service,
        reranking_service,
        context_service,
        prompt_service,
        llm_service
    ):
        self.retrieval_service = retrieval_service
        self.reranking_service = reranking_service
        self.context_service = context_service
        self.prompt_service = prompt_service
        self.llm_service = llm_service

    def ask(
        self,
        question: str,
        document_id: str
    ):
        
        results = self.retrieval_service.retrieve(
            query=question,
            document_id=document_id,
            top_k=10
        )

        reranked_redults = self.reranking_service.rerank(
            query=question,
            chunks=results,
            top_k=3
        )

        context, sources = self.context_service.build_context(
            reranked_redults
        )

        prompt = self.prompt_service.build_prompt(
            question=question,
            context=context
        )

        answer = self.llm_service.generate(prompt)

        return {
            "answer": answer,
            "sources": sources
        }