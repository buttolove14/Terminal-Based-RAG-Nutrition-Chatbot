from config import SUPABASE_URL, SUPABASE_API_KEY
from supabase import create_client
from embed_documents import embed_text

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def get_embedding_for_query(query):
    return embed_text(query)

def retrieve_relevant_chunks(query, top_k=5):
    embedding = get_embedding_for_query(query)

    response = supabase.rpc("match_documents", {
        "query_embedding": embedding,
        "match_count": top_k
    }).execute()

    if response.data:
        return [match["content"] for match in response.data]
    else:
        return []
