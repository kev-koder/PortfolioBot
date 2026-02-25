# PortfolioRAG – A Retrieval‑Augmented Career Knowledge Base

PortfolioRAG is a personal Retrieval‑Augmented Generation (RAG) system that transforms your entire career portfolio into a searchable knowledge base. Instead of relying on a single resume, the system ingests **all PDFs, text files, and Markdown documents** in a designated folder and makes them queryable through both a Streamlit UI and a command‑line interface.

This allows you to ask questions across your entire professional history, including:
- Your resume
- Project write‑ups
- Leadership stories
- Technical deep dives
- Case studies
- Any other documents you include in your portfolio

The result is a powerful, private, local system that can answer questions about your experience and help tailor your background to job descriptions.

---

## 🚀 Features

### **1. Portfolio‑Wide Ingestion**
The system automatically loads every `.pdf`, `.txt`, and `.md` file in the `data/portfolio/` folder.  
No subfolders are scanned, keeping the ingestion logic simple and predictable.

Each document is stored with metadata:
- `filename`
- `type` (pdf, txt, md)
- `path`
- `text`

### **2. Chunk‑Level Retrieval**
Each document is split into manageable chunks (default: 300 words).  
Each chunk is stored with metadata:
- `text`
- `source` (filename)
- `chunk_id`

This enables precise retrieval and transparent source attribution.

### **3. Vector Search with FAISS**
All chunks are embedded using `sentence-transformers/all-MiniLM-L6-v2` and indexed using FAISS for fast similarity search.

### **4. Local or Free LLM Generation**
The system uses a lightweight, CPU‑friendly model (`Phi-3-mini-4k-instruct`) to generate answers based on retrieved context.

### **5. Two Interfaces**
- **Streamlit UI** (`app.py`)  
  A clean, interactive interface for exploring your portfolio.
- **Command‑Line Interface** (`cli_app.py`)  
  Ideal for debugging or quick queries.

---

## 🧱 Project Structure

PortfolioBot/
│
├── src/
│   ├── app.py               # Streamlit UI
│   ├── cli_app.py           # Command-line interface
│   ├── portfolio_loader.py  # Loads all PDFs/TXTs/MDs in data/portfolio
│   ├── chunking.py          # Splits documents into chunks with metadata
│   ├── embeddings.py        # Embedding model + chunk embedding
│   ├── retriever.py         # FAISS index + retrieval with scores
│   ├── llm.py               # Local LLM interface (Phi-3 Mini)
│   └── job_tailor.py        # (future) Job description tailoring
│
├── data/
│   └── portfolio/           # All your documents go here
│       ├── resume.pdf
│       ├── project1.pdf
│       ├── leadership_story.txt
│       └── ...
│
├── requirements.txt
└── README.md


---

## 🛠️ Installation

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/ResumeRAG.git
cd ResumeRAG
```

### **2. Create a virtual environment
```python -m venv venv
venv\Scripts\activate   # Windows
```

### **3. Install dependencies
pip install -r requirements.txt

### **4. Add your portfolio documents
Place all .pdf, .txt, and .md files into: data/

### **5. Running the App
Command-Line Interface:
python src/cli_app.py

