from app.retriever import Retriever

query = input("Ask a question: ")

results = Retriever.retrieve(query)

print("\nTop Matching Chunks:\n")

for i, chunk in enumerate(results, start=1):
    print(f"Chunk {i}")
    print("-" * 40)
    print(chunk)
    print()