import pickle
import faiss

from src.embedder import get_embeddings

index = faiss.read_index(
    "vectorstore/faiss.index"
)

with open(
    "vectorstore/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)

def retrieve(query, top_k=5):

    query_embedding = get_embeddings(
        [query]
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results