from sentence_transformers import SentenceTransformer

def get_embedder():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_chunks(embedder, chunks):
    texts = [c["text"] for c in chunks]
    embeddings = embedder.encode(texts)
    return embeddings
