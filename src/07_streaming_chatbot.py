from dotenv import load_dotenv
from anthropic import AsyncAnthropic
import asyncio

load_dotenv()
client = AsyncAnthropic()
model = "claude-3-haiku-20240307"
green='\033[32m'
reset='\033[0m'
history = []


async def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        async with client.messages.stream(
            model=model,
            max_tokens=1000,
            messages=history,
        ) as stream:
            async for text in stream.text_stream:
                print(f"{green}{text}{reset}", end="", flush=True)   

        print("\n")

        whole_message = await stream.get_final_message()
        history.append({"role": "assistant", "content": f"whole_message.content[0].text"})

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
