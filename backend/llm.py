from google import genai
import os
import json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(question, dashboard_data):

    prompt = f"""
You are an AI Business Intelligence assistant for Skylark Drones.

Use ONLY the business data provided below.
Do NOT say information is missing if it exists in the data.

Business Data:
{json.dumps(dashboard_data, indent=2)}

Instructions:
- Answer in short bullet points.
- Put one point per line.
- Show important numbers.
- Keep the answer under 10 lines.
- Do NOT write long paragraphs.
- End with 2-3 business insights.

Answer the user's question with numbers, insights, and a short conclusion.

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text