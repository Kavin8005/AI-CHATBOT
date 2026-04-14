from fastapi import FastAPI
from query import search
import openai

app = FastAPI()

openai.api_key = "YOUR_API_KEY"

@app.get("/ask")
def ask_question(q: str):
    docs = search(q)
    
    context = " ".join([doc[0] for doc in docs])
    
    prompt = f"""
    Answer based on context:
    {context}
    
    Question: {q}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {"answer": response['choices'][0]['message']['content']}