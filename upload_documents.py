from utils import get_all_documents_chunks
from embed_documents import embed_text
from config import SUPABASE_URL, SUPABASE_API_KEY
from supabase import create_client

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

chunks = get_all_documents_chunks("./data/sample_docs")
print(f"Found {len(chunks)} chunks. Embedding and uploading...")

for i, chunk in enumerate(chunks, 1):
    try:
        print(f"\nProcessing chunk {i}/{len(chunks)}")
        embedding = embed_text(chunk)

        if not embedding:
            print("Skipping empty or failed embedding.")
            continue

        response = supabase.table("documents").insert({
            "content": chunk,
            "embedding": embedding
        }).execute()

        if response.data:
            print("Uploaded chunk.")
        else:
            print("Upload failed. No data returned.")

    except Exception as e:
        print("Exception during upload:", e)
