from portfolio_loader import load_portfolio
from chunking import chunk_documents
from embeddings import get_embedder, embed_chunks
from retriever import build_faiss_index, retrieve
from llm import get_llm

def main():
    print("\n=== PortfolioRAG (Command Line Version) ===\n")

    embedder = get_embedder()
    llm = get_llm()

    print("Loading portfolio...")
    documents = load_portfolio()
    print(f"Loaded {len(documents)} documents:")
    for doc in documents:
        print(f" - {doc['filename']} ({doc['type']})")

    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    embeddings = embed_chunks(embedder, chunks)
    index = build_faiss_index(embeddings)

    print("\nReady! Ask a question about your portfolio.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Your question: ")

        if query.lower().strip() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if len(query.split()) < 3:
            print("Please ask a slightly more specific question.\n")
            continue

        results = retrieve(query, embedder, chunks, index,2)

        print("\n--- Retrieved Chunks ---")
        for r in results:
            print(f"[{r['source']} | chunk {r['chunk_id']} | score {r['score']:.4f}]")
            print(r["text"])
            print("---")

        context = "\n\n".join([r["text"] for r in results])

        prompt = (
            f"You are a helpful assistant answering questions about a resume and portfolio.\n"
            f"Use the context to answer the question. Do not make up information.  If you cannot answer from the context, say so.\n\n"
            f"Keep your answer short to under 20 words.\n\n"
            f"Context from resume and portfolio:\n{context}\n\n"
            f"Question: {query}\n"
            f"Answer:"
        )

        response = llm(prompt)[0]["generated_text"]
        print("\n--- Answer ---")
        print(response)
        print()

if __name__ == "__main__":
    main()
