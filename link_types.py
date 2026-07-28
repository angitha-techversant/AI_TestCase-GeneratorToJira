import requests
from config import JIRA_URL, JIRA_TOKEN

url = f"{JIRA_URL}/rest/api/2/issueLinkType"

headers = {
    "Authorization": f"Bearer {JIRA_TOKEN}",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)