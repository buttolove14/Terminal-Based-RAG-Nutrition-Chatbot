import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")

if __name__ == "__main__":
    print("SUPABASE_URL:", SUPABASE_URL)
    print("SUPABASE_API_KEY:", SUPABASE_API_KEY)