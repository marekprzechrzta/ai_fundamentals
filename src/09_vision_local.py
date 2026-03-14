from dotenv import load_dotenv
from anthropic import Anthropic
import base64
import mimetypes

load_dotenv()
client = Anthropic()

def create_image_message(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_encoded_data = base64.b64encode(binary_data)
        base64_string = base64_encoded_data.decode("utf-8")
    
    media_type, _ = mimetypes.guess_type(image_path)
    
    return {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": media_type,
            "data": base64_string
        }
    }

messages=[
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Image 1:"},
            create_image_message("./images/animal1.png"),
            {"type": "text", "text": "Image 2:"},
            create_image_message("./images/animal2.png"),
            {"type": "text", "text": "Image 3:"},
            create_image_message("./images/animal3.png"),
            {
                "type": "text",
                "text": "What are these animals?"
            }
        ]
    }
]

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=messages
)

print(response.content[0].text)
