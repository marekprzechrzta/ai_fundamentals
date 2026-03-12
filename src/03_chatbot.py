from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-3-haiku-20240307"

history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model=model,
        max_tokens=100,
        messages=history
    )   

    history.append({"role": "assistant", "content": response.content[0].text})

    print(f"Chatbot: {response.content[0].text}")