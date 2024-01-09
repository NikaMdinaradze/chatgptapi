from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")


async def send_message(value: str):
    client = OpenAI(api_key=api_key)
    value.replace("_", " ")
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user",
         "content": value}
      ]
    )

    return dict(completion.choices[0].message)['content']
