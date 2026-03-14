from dotenv import load_dotenv
from anthropic import Anthropic
import base64

load_dotenv()
client = Anthropic()

with open("./images/uh_oh.png", "rb") as image_file:
    binary_data = image_file.read()
    base64_encoded_data = base64.b64encode(binary_data)
    base64_string = base64_encoded_data.decode("utf-8")

messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": base64_string
                }
            },
            {
                "type": "text",
                "text": "What could this person have done to prevent this?"
            }
        ]
    },
]

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=messages
)

print(response.content[0].text)
