from sentence_transformers import SentenceTransformer
from endee import Client

model = SentenceTransformer('all-MiniLM-L6-v2')

client = Client()
collection = client.get_or_create_collection("notes")

def ingest_text(text):
    chunks = text.split(".")
    
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()
        
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk]
        )

if __name__ == "__main__":
    sample_text = "Machine learning is a field of AI. It enables systems to learn from data."
    ingest_text(sample_text)