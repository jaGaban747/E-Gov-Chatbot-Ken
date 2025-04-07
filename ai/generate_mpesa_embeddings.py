import os
import pandas as pd
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load .env variables
load_dotenv()
API_KEY = os.environ.get("API_KEY")
ENDPOINT_URL = os.environ.get("ENDPOINT_URL")
API_VERSION = "2023-09-01-preview"
EMBEDDING_MODEL = "text-embedding-ada-002-kenya-hack"

# Init client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT_URL,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# Load your CSV
df = pd.read_csv("data/mpesa_cleaned.csv")

# Prepare text column
df["text_chunk"] = df["narration"].astype(str)

# Embedding function
def get_embedding(text):
    try:
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=text,
            encoding_format="float"
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error embedding: {text[:50]}... -> {e}")
        return None

# Generate embeddings
print("Generating embeddings...")
df["embedding"] = df["text_chunk"].apply(get_embedding)

# Drop rows with failed embeddings
df = df.dropna(subset=["embedding"])

# Ensure output folder exists
os.makedirs("data", exist_ok=True)

# Save to new CSV
df[["text_chunk", "embedding"]].to_csv("data/mpesa_embeddings.csv", index=False)

print("✅ Embeddings saved to data/mpesa_embeddings.csv")
