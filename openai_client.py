from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client= OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

agent=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you help me with my interview preparation?"}
    ]
)

print(agent.choices[0].message.content)
