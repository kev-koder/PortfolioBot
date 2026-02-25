def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks


def chunk_documents(documents, chunk_size=300):
    """
    Input: list of dicts with keys: filename, text, type, path
    Output: list of chunk dicts: {text, source, chunk_id}
    """
    all_chunks = []
    for doc in documents:
        words = doc["text"].split()
        chunks = [
            " ".join(words[i:i+chunk_size])
            for i in range(0, len(words), chunk_size)
        ]

        for idx, chunk_text in enumerate(chunks):
            if not chunk_text.strip():
                continue
            all_chunks.append({
                "text": chunk_text,
                "source": doc["filename"],
                "chunk_id": idx,
            })

    return all_chunks
