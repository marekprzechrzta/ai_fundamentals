from dotenv import load_dotenv
from anthropic import Anthropic
import base64
import httpx

load_dotenv()
client = Anthropic()

image_url = "https://img.freepik.com/free-photo/closeup-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head_488145-3540.jpg"

def get_image_dict_from_url(image_url):
    response = httpx.get(image_url)
    image_content = response.content

    image_extension = image_url.split(".")[-1].lower()
    if image_extension == "jpg" or image_extension == "jpeg":
        image_media_type = "image/jpeg"
    elif image_extension == "png":
        image_media_type = "image/png"
    elif image_extension == "gif":
        image_media_type = "image/gif"
    else:
        raise ValueError("Unsupported image format")

    image_data = base64.b64encode(image_content).decode("utf-8")

    return {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": image_media_type,
            "data": image_data,
        },
    }

messages=[
        {
            "role": "user",
            "content": [
                get_image_dict_from_url(image_url),
                {
                    "type": "text",
                    "text": "Describe this image."
                }
            ],
        }
    ]


response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)

