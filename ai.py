from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def generate_testcases(summary, description):

    prompt = f"""
You are a Senior QA Engineer.

Generate exactly 5 software test cases.

Story Summary:
{summary}

Story Description:
{description}

Return ONLY valid JSON.

Format:

[
  {{
    "summary":"",
    "description":"",
    "testSteps":"",
    "expectedResult":""
  }}
]
"""

    response = client.chat.completions.create(
       model="google/gemma-4-26b-a4b-it:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000,
        temperature=0.2
    )

    print("\n===== FULL RESPONSE =====")
    print(response)
    print("=========================\n")

    # Check if the model returned a response
    if not response.choices:
        raise Exception("No response returned from AI.")

    content = response.choices[0].message.content

    if not content:
        raise Exception("AI returned an empty response.")

    # Remove markdown if present
    content = content.replace("```json", "").replace("```", "").strip()

    return content