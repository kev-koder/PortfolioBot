import streamlit as st
from portfolio_loader import load_portfolio
from chunking import chunk_documents
from embeddings import get_embedder, embed_chunks
from retriever import build_faiss_index, retrieve
from llm import get_llm

@st.cache_resource
def load_models():
    return get_embedder(), get_llm()

@st.cache_resource
def load_index(_embedder):
    documents = load_portfolio()
    chunks = chunk_documents(documents)
    embeddings = embed_chunks(_embedder, chunks)
    index = build_faiss_index(embeddings)
    return documents, chunks, index

# Streamlit UI
st.title("PortfolioRAG – Ask My Portfolio")

embedder, llm = load_models()
documents, chunks, index = load_index(embedder)

st.caption(f"Loaded {len(documents)} documents: {', '.join(d['filename'] for d in documents)}")

query = st.text_input("Ask a question about your experience")

if query:
    results = retrieve(query, embedder, chunks, index, k=2)

    with st.expander("Retrieved chunks"):
        for r in results:
            st.markdown(f"**[{r['source']} | chunk {r['chunk_id']} | score {r['score']:.4f}]**")
            st.write(r["text"])

    context = "\n\n".join([r["text"] for r in results])

    prompt = (
        f"You are a helpful assistant answering questions about a resume and portfolio.\n"
        f"Use the context to answer the question. Do not make up information. If you cannot answer from the context, say so.\n\n"
        f"Keep your answer short to under 20 words.\n\n"
        f"Context from resume and portfolio:\n{context}\n\n"
        f"Question: {query}\n"
        f"Answer:"
    )

    response = llm(prompt)[0]["generated_text"]
    st.write(response)
