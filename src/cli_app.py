from resume_loader import load_resume
from chunking import chunk_text
from embeddings import get_embedder
from retriever import build_faiss_index, retrieve
from llm import get_llm

def main():
    print("\n=== ResumeRAG (Command Line Version) ===\n")

    # Load models
    embedder = get_embedder()
    llm = get_llm()

    # Load and prepare resume
    print("Loading resume...")
    resume_text = load_resume()
    chunks = chunk_text(resume_text, 50)
    embeddings = embedder.encode(chunks)
    index = build_faiss_index(embeddings)

    print("Ready! Ask a question about your resume.\n")
    
    while True:
        query = input("Your question (or type 'exit'): ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        retrieved_chunks = retrieve(query, embedder, chunks, index)
        context = "\n\n".join(retrieved_chunks)

        prompt = (
            f"You are a helpful assistant answering questions about a resume.\n\n"
            f"Context from your resume and portfolio:\n{context}\n\n"
            f"Question: {query}\n"
            f"Answer:"
        )

        response = llm(prompt)[0]["generated_text"]
        print("\n--- Answer ---")
        print(response)
        print("\n")

if __name__ == "__main__":
    main()
