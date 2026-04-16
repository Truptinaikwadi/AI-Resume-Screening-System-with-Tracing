import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_model(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict resume screening AI. Do not hallucinate."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Groq API Error: {str(e)}"