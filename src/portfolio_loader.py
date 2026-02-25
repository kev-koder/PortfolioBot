import os
from pypdf import PdfReader

SUPPORTED_EXTENSIONS = [".pdf", ".txt", ".md"]

def load_portfolio(folder_path="./data"):
    documents = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if not os.path.isfile(full_path):
            continue

        ext = os.path.splitext(filename)[1].lower()
        if ext not in SUPPORTED_EXTENSIONS:
            continue

        if ext == ".pdf":
            text = _load_pdf(full_path)
        else:
            text = _load_text(full_path)

        if not text.strip():
            continue

        documents.append({
            "filename": filename,
            "path": full_path,
            "type": ext.lstrip("."),
            "text": text,
        })

    return documents

def _load_pdf(path):
    reader = PdfReader(path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return text

def _load_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
