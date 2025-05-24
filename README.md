# Nutrition RAG Chatbot

A terminal-based chatbot that generates personalized nutrition plans using user inputs and a retrieval-augmented generation (RAG) pipeline.

## Features

- User inputs: age, gender, height, weight, activity, diet, medical summary
- Nutrition context retrieval from embedded documents
- Personalized diet plan
- Entirely terminal-based

## Setup

1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Create a `.env` file using `.env.example`
4. Place nutrition PDFs in `data/sample_docs/`
5. Run `python upload_documents.py` to embed
6. Run `python chatbot.py` to start the chatbot

## Disclaimer

This tool does not provide medical advice. Consult a healthcare provider.
