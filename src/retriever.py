import faiss
import numpy as np

def build_faiss_index(embeddings):
    embeddings = np.array(embeddings)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def retrieve(query, embedder, chunks, index, k=5):
    q_emb = embedder.encode([query])
    distances, indices = index.search(np.array(q_emb), k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        chunk = chunks[idx]
        results.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "score": float(dist),
        })
    return results
