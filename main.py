import os
from app.pdf_loader import PDFLoader
from app.text_cleaner import TextCleaner
from app.chunker import TextChunker

loader = PDFLoader("data/insurance.pdf")

text = loader.extract_text()

clean_text = TextCleaner.clean(text)

chunker = TextChunker()

chunks = chunker.chunk_text(clean_text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk)

# Create output/chunks folder
os.makedirs("output/chunks", exist_ok=True)

# Save all chunks
for i, chunk in enumerate(chunks):
    with open(f"output/chunks/chunk_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(chunk)

print("\n All chunks saved successfully!")

from app.vector_store import VectorStore

VectorStore.add_chunks(chunks)

print("\n✅ Embeddings generated and stored in ChromaDB!")