from ollama import chat 

class LLMService:

    def __init__(
        self,
        model: str
    ):
        self.model = model

    def generate(
        self,
        prompt: str
    ) -> str:

        response = chat(
            model = self.model,
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content