import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env (for local development)
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets.get("GOOGLE_API_KEY")
    except Exception:
        pass

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found.")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Model name for google-genai v2.11.0
MODEL_NAME = "gemini-3.5-flash"


class GeminiLLM:

    @staticmethod
    def generate_answer(context, question):

        prompt = f"""
You are an expert Insurance Policy Assistant.

Answer the user's question ONLY using the information provided in the context.

If the answer can be inferred from one or more document chunks, combine the information and explain it clearly.

Do NOT require the answer to appear as an exact sentence.

Only reply with:

I couldn't find this information in the insurance policy.

if the context contains absolutely no relevant information.

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

        return response.text.strip()