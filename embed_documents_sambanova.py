import os
import requests
from config import SAMBANOVA_API_KEY

def embed_text(text):
    if not text.strip():
        return None

    try:
        url = "https://api.sambanova.ai/v1/embeddings"
        headers = {
            "Authorization": f"Bearer {SAMBANOVA_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "input": text,
            "model": "E5-Mistral-7B-Instruct"
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["data"][0]["embedding"]
        else:
            print("❌ SambaNova API error:", response.status_code)
            print(response.json())
            return None

    except Exception as e:
        print("❌ Exception during SambaNova embedding:", e)
        return None
