# import os
# import streamlit as st
# from google import genai
# from dotenv import load_dotenv
#
# load_dotenv()
#
# api_key = os.getenv("GOOGLE_API_KEY")
#
# if not api_key:
#     api_key = st.secrets["GOOGLE_API_KEY"]
#
# client = genai.Client(api_key=api_key)
#
# MODEL_NAME = "gemini-2.5-flash"

import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.write("Environment:", os.getenv("GOOGLE_API_KEY"))

st.write("Secrets keys:", list(st.secrets.keys()))

api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.write("API Key Found:", api_key is not None)

if not api_key:
    st.stop()

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"


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