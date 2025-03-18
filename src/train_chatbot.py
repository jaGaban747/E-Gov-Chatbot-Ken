import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load API credentials
load_dotenv()
API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

# Initialize OpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version="2024-02-01",
)

# Load FAQ dataset
with open("data/government_faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

# Function to train chatbot with FAQs
def train_chatbot():
    training_data = []
    for faq in faqs:
        training_data.append({"role": "user", "content": faq["question"]})
        training_data.append({"role": "assistant", "content": faq["answer"]})

    return training_data

# Train chatbot
messages = train_chatbot()

response = client.chat.completions.create(
    model="gpt-4o-kenya-hack",
    messages=messages
)

# Print AI-generated responses
print(response.model_dump_json(indent=2))
