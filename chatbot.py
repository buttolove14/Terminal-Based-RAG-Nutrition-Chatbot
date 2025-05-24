import requests
from retrieve import retrieve_relevant_chunks

GEMINI_API_KEY = "Your_API_Key"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def collect_user_info():
    print("Welcome to your Nutrition Assistant!")
    print("⚠️ Disclaimer: This tool does not provide medical advice. Consult a healthcare provider.\n")
    return {
        "name": input("Name: "),
        "age": input("Age: "),
        "gender": input("Gender: "),
        "height": input("Height (cm): "),
        "weight": input("Weight (kg): "),
        "activity": input("Activity level (e.g., sedentary, moderate, active): "),
        "diet": input("Dietary preference/restriction (e.g., vegan, diabetic): "),
        "medical": input("Medical test report summary (optional): ")
    }

def generate_prompt(user_info, context_docs):
    context = "\n".join(context_docs)
    return f"""Context:\n{context}

User Profile:
Name: {user_info['name']}
Age: {user_info['age']}
Gender: {user_info['gender']}
Height: {user_info['height']} cm
Weight: {user_info['weight']} kg
Activity Level: {user_info['activity']}
Diet: {user_info['diet']}
Medical: {user_info['medical']}

Generate a complete personalized nutrition plan."""

def call_gemini_api(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print("❌ Error:", response.status_code, response.text)
        return "Failed to generate a nutrition plan."

def main():
    user_info = collect_user_info()
    query = f"Nutrition plan for {user_info['age']} year old {user_info['diet']} with {user_info['medical']}"
    docs = retrieve_relevant_chunks(query)
    prompt = generate_prompt(user_info, docs)
    result = call_gemini_api(prompt)

    print("\nGenerated Personalized Diet Plan:\n")
    print(result)
    print("\n⚠️ Disclaimer: This tool does not provide medical advice. Consult a healthcare provider.")
    print(f"\n🔍 Retrieved {len(docs)} relevant context chunks from Supabase.")

if __name__ == "__main__":
    main()
