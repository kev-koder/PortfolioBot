from pathlib import Path
from pypdf import PdfReader

def load_resume(path="data/resume.txt"):
    # Convert string path to a Path object
    file_path = Path(path)
    
    # .suffix gets the extension including the dot (e.g., '.pdf')
    extension = file_path.suffix.lower()

    if extension == ".pdf":
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages)
    
    elif extension == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    
    else:
        raise ValueError(f"Unsupported file type: {extension}. Please use .pdf or .txt")
