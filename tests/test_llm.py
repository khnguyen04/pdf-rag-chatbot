from app.services.llm_service import LLMService

llm_service = LLMService(
    model="qwen2.5:3b"
)

prompt = """
Bạn là một trợ lý hỏi đáp.

Hãy trả lời câu hỏi dựa trên thông tin được cung cấp.

CONTEXT:
GPA tối thiểu để nhận học bổng là 3.2.

QUESTION:
GPA tối thiểu để nhận học bổng là bao nhiêu?

ANSWER:
"""

answer = llm_service.generate(
    prompt
)

print("=" * 60)
print("ANSWER")
print("=" * 60)
print(answer)