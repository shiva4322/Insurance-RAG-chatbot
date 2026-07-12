from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)


class EmbeddingGenerator:

    @staticmethod
    def generate(text: str):
        return model.encode(text).tolist()