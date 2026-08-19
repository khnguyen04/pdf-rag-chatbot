from pypdf import PdfReader

class PDFLoader:

    def load(
        self,
        file_path: str
    ) -> list[dict]:

        reader = PdfReader(file_path)

        pages = []
        
        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text() or ""

            if text.strip():
                pages.append({
                    "page": page_number,
                    "text": text.strip()
                })
        
        return pages