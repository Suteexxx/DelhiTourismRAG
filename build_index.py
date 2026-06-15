import os
import pickle
import faiss

from pdf_loader import load_pdf
from chunker import create_chunks
from embedder import get_embeddings

print("Loading PDF...")

pages = load_pdf(
    "data/delhi_facts.pdf"
)

print("Creating Chunks...")

chunks = create_chunks(pages)

texts = [
    chunk["content"]
    for chunk in chunks
]

print("Generating Embeddings...")

embeddings = get_embeddings(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

os.makedirs(
    "vectorstore",
    exist_ok=True
)

faiss.write_index(
    index,
    "vectorstore/faiss.index"
)

with open(
    "vectorstore/chunks.pkl",
    "wb"
) as f:
    pickle.dump(chunks, f)

print("Index Built Successfully")