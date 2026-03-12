from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic()

first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Write a haiku about the ocean."}
    ]
)

print(first_message.content[0].text)
