from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2') 

def embed_text(text):
    if not text.strip():
        return None
    try:
        embedding = model.encode(text).tolist()
        return embedding
    except Exception as e:
        print("Local embedding error:", e)
        return None
