import os
import fitz  #
import re

def load_and_chunk_pdf_by_section(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()

    pattern = r"(=== Section:.*?===)"
    parts = re.split(pattern, full_text)

    chunks = []
    if len(parts) <= 1:
        # Fallback: chunk by ~1000 characters
        for i in range(0, len(full_text), 1000):
            chunk = full_text[i:i+1000].strip()
            if chunk:
                chunks.append(chunk)
        return chunks

    for i in range(1, len(parts), 2):
        section_header = parts[i].strip()
        section_body = parts[i+1].strip() if i + 1 < len(parts) else ""
        chunk = f"{section_header}\n{section_body}"
        chunks.append(chunk)

    return chunks

def get_all_documents_chunks(folder_path):
    chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            chunks.extend(load_and_chunk_pdf_by_section(file_path))
    return chunks
