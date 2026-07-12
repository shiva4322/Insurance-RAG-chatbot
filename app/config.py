from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

VECTOR_DB_PATH = "vector_db"

COLLECTION_NAME = "insurance_documents"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

MODEL_NAME = "gemini-flash-latest"