# ai/chatbot.py

import os
import time
from dotenv import load_dotenv
from openai import AzureOpenAI
from openai import RateLimitError

# Load .env variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT_URL")
API_VERSION = os.getenv("API_VERSION")
MODEL_NAME = "gpt-4o-kenya-hack"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# AI interaction with retry on 429
def chat_with_ai(user_message, max_retries=3):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant for small business owners in Kenya. Provide useful insights and advice."
        },
        {"role": "user", "content": user_message}
    ]

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages
            )
            return response.choices[0].message.content

        except RateLimitError as e:
            wait = 2 * (attempt + 1)
            print(f"⏳ Rate limit hit. Retrying in {wait}s...")
            time.sleep(wait)

        except Exception as e:
            return f"❌ Error: {str(e)}"

    return "❌ Failed after multiple retries. Please try again later."
