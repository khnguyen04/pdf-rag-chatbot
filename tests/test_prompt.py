from app.services.prompt_service import PromptService


context = """
[SOURCE 1]
Document: scholarship
Page: 1
GPA phải đạt tối thiểu 3.2.

[SOURCE 2]
Document: scholarship
Page: 1
Sinh viên không được vi phạm kỷ luật.
"""


question = "GPA tối thiểu để nhận học bổng là bao nhiêu?"


prompt_service = PromptService()

prompt = prompt_service.build_prompt(
    question=question,
    context=context
)

print("=" * 60)
print("PROMPT")
print("=" * 60)
print(prompt)