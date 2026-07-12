from app.llm import GeminiLLM

class PolicySummarizer:

    @staticmethod
    def summarize(context):

        prompt = f"""
Summarize this insurance policy.

Include

1. Policy Name

2. Coverage

3. Waiting Period

4. Exclusions

5. Claim Process

6. Important Notes

Context

{context}
"""

        return GeminiLLM.generate_answer(
            context=context,
            question=prompt
        )