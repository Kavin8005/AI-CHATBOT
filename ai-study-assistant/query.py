from sentence_transformers import SentenceTransformer
from endee import Client

model = SentenceTransformer('all-MiniLM-L6-v2')

client = Client()
collection = client.get_collection("notes")

def search(query):
    embedding = model.encode(query).tolist()
    
    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )
    
    return results['documents']