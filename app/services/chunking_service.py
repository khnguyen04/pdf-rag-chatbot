class ChunkingService:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):

        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

        if chunk_overlap < 0:
            raise ValueError("chunk_overlap cannot be negative")

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_pages(
        self,
        pages: list[dict]
    ) -> list[dict]:

        chunks = []

        for page in pages:
            text = page["text"]
            page_number = page["page"]

            start = 0

            while start < len(text):
                end = start + self.chunk_size

                chunk_text = text[start:end]

                if chunk_text.strip():
                    chunks.append({
                        "page": page_number,
                        "text": chunk_text.strip()
                    })

                start += (
                    self.chunk_size -
                    self.chunk_overlap
                )

        return chunks