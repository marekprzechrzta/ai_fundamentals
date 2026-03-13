from dotenv import load_dotenv
from anthropic import Anthropic, AsyncAnthropic
import asyncio

load_dotenv()
client = Anthropic()
async_client = AsyncAnthropic()
model = "claude-3-haiku-20240307"

def stream_without_helpers():
    stream = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": (
                    "How do large language models work?"
                )
            }
        ],
        stream=True,
    )

    for event in stream:
        if event.type == "message_start":
            input_tokens = event.message.usage.input_tokens
            print("MESSAGE START EVENT", flush=True)
            print(f"Input tokens used: {input_tokens}", flush=True)
            print("========================")
        elif event.type == "content_block_delta":
            print(event.delta.text, flush=True, end="")
        elif event.type == "message_delta":
            output_tokens = event.usage.output_tokens
            print("\n========================", flush=True)
            print("MESSAGE DELTA EVENT", flush=True)
            print(f"Output tokens used: {output_tokens}", flush=True)

async def stream_with_helpers():
    async with async_client.messages.stream(
        model=model,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": (
                    "How do large language models work?"
                )
            }
        ],
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)

    final_message = await stream.get_final_message()
    print("\n\nSTREAMING IS DONE. HERE IS THE FINAL MESSAGE: ")
    print(final_message.to_json())

#stream_without_helpers()
asyncio.run(stream_with_helpers())