# ResumeRAG – A Retrieval‑Augmented Career Assistant

ResumeRAG is a personal Retrieval‑Augmented Generation (RAG) system designed to help job seekers understand, query, and tailor their experience for specific roles. It combines local embeddings, vector search, and an LLM to create a smart assistant that can:

- Answer questions about your resume (“Ask My Resume”)
- Analyze a job description
- Retrieve your most relevant experience
- Generate tailored resume bullet points
- Provide a gap analysis between your background and the job requirements

This project is built entirely with free, local tools — no paid APIs required.

---

## 🚀 Features

### **1. Ask My Resume**
Query your resume like a knowledge base:
- “What cloud technologies have I used”
- “Summarize my leadership experience”
- “Which projects demonstrate data engineering skills”

### **2. Job Description Tailoring**
Paste a job description and the system will:
- Retrieve the most relevant parts of your resume
- Generate customized resume bullets
- Explain why each bullet was selected
- Identify gaps between your experience and the job requirements

### **3. Local, Free, and Private**
- Uses **sentence-transformers** for embeddings  
- Uses **FAISS** for vector search  
- Uses a **local or free LLM** (e.g., Mistral, Llama 3 via HuggingFace or Ollama)  
- No external services needed  

---

## 🧱 Project Structure

ResumeRAG/
│
├── src/
│   ├── init.py
│   ├── app.py               # Streamlit UI
│   ├── resume_loader.py     # PDF extraction
│   ├── chunking.py          # Text chunking logic
│   ├── embeddings.py        # Embedding model loader
│   ├── retriever.py         # FAISS index + retrieval
│   ├── llm.py               # Local/Free LLM interface
│   └── job_tailor.py        # Job description analysis + bullet generation
│
├── data/
│   └── resume.pdf           # Your resume (not committed by default)
│
├── notebooks/
│   └── experiments.ipynb    # Optional experimentation
│
├── tests/
│   └── test_retriever.py    # Example unit tests
│
├── requirements.txt
├── .gitignore
└── README.md




## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ResumeRAG.git
cd ResumeRAG
```

### 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add your resume
### Place your PDF here:
data/resume.pdf

### Running the App
### Launch the Streamlit interface:
streamlit run src/app.py



## How It Works
1. Resume Ingestion
Your resume PDF is parsed into raw text and split into semantic chunks.

2. Embedding + Vector Store
Each chunk is embedded using all-MiniLM-L6-v2

Stored in a FAISS index for fast similarity search

3. Retrieval
Queries or job descriptions are embedded and matched against your resume chunks.

4. LLM Generation
A local or free LLM generates:
* Answers to resume questions
* Tailored resume bullets
* Gap analysis
* Explanation of retrieved evidence

### Example Queries
Ask My Resume
“What programming languages do I have experience with”

“Summarize my cloud background”

“Which projects show leadership”

### Tailor to a Job Description
Paste a job description and ask:

“Generate tailored resume bullets”

“What experience matches this role”

“What skills am I missing”

## 📜 License
MIT License — feel free to use, modify, and build on this project.

## 🙌 Acknowledgments
Built using:
SentenceTransformers
FAISS
Streamlit
HuggingFace Transformers
Copilot
