from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "gemini-3.5-flash"


class GeminiLLM:

    @staticmethod
    def generate_answer(context, question):

        prompt = f"""
You are an expert Insurance Policy Assistant.

Answer ONLY using the information provided in the context.

If the context contains the answer, explain it clearly.

Do NOT say "I couldn't find this information" if the answer is present, even if it is not written as a formal definition.

If the answer is not present in the context, reply exactly:

I couldn't find this information in the insurance policy.

-------------------------
CONTEXT
-------------------------

{context}

-------------------------
QUESTION
-------------------------

{question}

-------------------------
ANSWER
-------------------------
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text