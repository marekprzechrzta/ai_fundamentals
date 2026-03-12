from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-3-haiku-20240307"

def generate_question(topic, num_questions):
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        system=f"You are an expert in the field of {topic}.",
        stop_sequences=[f"{num_questions + 1}."],
        messages=[
            {
                "role": "user",
                "content": (
                    f"Generate {num_questions} thought-provoking"
                    " questions about {topic}."
                )
            }
        ]
    )
    return response.content[0].text

questions = generate_question("machine learning", 3)
print(questions)
