import requests
from config import OPENROUTER_API_KEY

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}"
}

response = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers=headers
)

response.raise_for_status()

for model in response.json()["data"]:
    if ":free" in model["id"]:
        print(model["id"])