from app.retriever import Retriever
from app.llm import GeminiLLM

question = input("Ask your question: ")

chunks = Retriever.retrieve(question)

print("\nRetrieved Chunks:")
print("=" * 80)

for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk)

context = ""

for i, chunk in enumerate(chunks, 1):
    context += f"\nDocument Chunk {i}:\n{chunk}\n"

answer = GeminiLLM.generate_answer(
    context=context,
    question=question
)

print("\nAnswer:\n")
print(answer)