import chromadb

from app.config import VECTOR_DB_PATH, COLLECTION_NAME

client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


class VectorStore:

    @staticmethod
    def add_chunks(chunks):

        from app.embedding import EmbeddingGenerator

        ids = []
        embeddings = []
        documents = []

        for i, chunk in enumerate(chunks):
            ids.append(str(i))
            documents.append(chunk)
            embeddings.append(
                EmbeddingGenerator.generate(chunk)
            )

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )