from app.loaders.pdf_loader import PDFLoader


loader = PDFLoader()

pages = loader.load(
    "data/uploads/QuyDinh2026_Truong.pdf"
)

for page in pages:

    print("=" * 60)
    print(f"PAGE {page['page']}")
    print(page["text"])