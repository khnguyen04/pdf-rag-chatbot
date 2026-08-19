class PromptService:

    def build_prompt(
        self,
        question: str,
        context: str
    ) -> str:

        return f"""
Bạn là trợ lý hỏi đáp dựa trên tài liệu.

Hãy trả lời câu hỏi CHỈ dựa trên CONTEXT được cung cấp.

Quy tắc:
- Chỉ sử dụng thông tin có trong CONTEXT.
- Không sử dụng kiến thức bên ngoài tài liệu.
- Không tự bịa thông tin.
- Nếu CONTEXT không đủ thông tin,
  hãy nói rằng không tìm thấy thông tin trong tài liệu.
- Trả lời rõ ràng, ngắn gọn.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""".strip()