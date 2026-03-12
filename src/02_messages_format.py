from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-3-haiku-20240307"

def translate(word, language):
    response = client.messages.create(
        model=model,
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Translate the word '{word}' into {language}. "
                    "Return only the translated word without any additional text."
                )
            }
        ]
    )
    return response.content[0].text

spanish_translation = translate("hello", "Spanish")
print(spanish_translation)
french_translation = translate("hello", "French")
print(french_translation)
japanese_translation = translate("hello", "Japanese")
print(japanese_translation)