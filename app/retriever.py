import chromadb
from app.config import VECTOR_DB_PATH, COLLECTION_NAME
from app.embedding import EmbeddingGenerator

client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


class Retriever:

    @staticmethod
    def retrieve(query, top_k=3):

        query_embedding = EmbeddingGenerator.generate(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]