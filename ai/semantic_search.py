import pandas as pd
import numpy as np
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("ENDPOINT_URL"),
    api_key=os.getenv("API_KEY"),
    api_version="2023-09-01-preview"
)

EMBEDDING_MODEL = "text-embedding-ada-002-kenya-hack"
EMBEDDINGS_CSV = "data/mpesa_embeddings.csv"

def get_embedding(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
        encoding_format="float"
    )
    return response.data[0].embedding

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_mpesa(query, top_k=5):
    query_embedding = get_embedding(query)
    df = pd.read_csv(EMBEDDINGS_CSV)
    df["embedding"] = df["embedding"].apply(eval)  # Convert string to list
    df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity(x, query_embedding))
    results = df.sort_values("similarity", ascending=False).head(top_k)
    return results[["text_chunk", "similarity"]]
