from sentence_transformers import SentenceTransformer

def get_embedder():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
