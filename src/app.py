import streamlit as st
from resume_loader import load_resume
from chunking import chunk_text
from embeddings import get_embedder
from retriever import build_faiss_index, retrieve
from llm import get_llm

# Load models
embedder = get_embedder()
llm = get_llm()

# Load and prepare resume
resume_text = load_resume()
chunks = chunk_text(resume_text)
embeddings = embedder.encode(chunks)
index = build_faiss_index(embeddings)

# Streamlit UI
st.title("ResumeRAG – Ask My Resume")

query = st.text_input("Ask something about your experience")

if query:
    retrieved_chunks = retrieve(query, embedder, chunks, index)
    context = "\n\n".join(retrieved_chunks)

    prompt = (
        f"Use the context to answer the question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        f"Answer:"
    )

    response = llm(prompt)[0]["generated_text"]
    st.write(response)
