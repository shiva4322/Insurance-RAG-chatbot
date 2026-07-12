import os

from app.pdf_loader import PDFLoader
from app.text_cleaner import TextCleaner
from app.text_chunker import TextChunker
from app.vector_store import VectorStore


def process_pdf(pdf_path):

    print("Loading PDF...")

    text = PDFLoader.load_pdf(pdf_path)

    print("Cleaning text...")

    text = TextCleaner.clean_text(text)

    print("Chunking...")

    chunker = TextChunker()

    chunks = chunker.chunk_text(text)

    print("Creating Vector DB...")

    vector_db = VectorStore()

    vector_db.create_vector_db(chunks)

    return len(chunks)