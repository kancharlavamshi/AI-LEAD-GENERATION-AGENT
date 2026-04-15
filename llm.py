from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_email(name, company, role):
    prompt = f"""
    Write a short personalized cold email.

    Name: {name}
    Company: {company}
    Role: {role}

    Keep it professional, friendly, and concise (max 100 words).
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
