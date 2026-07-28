import requests
from config import JIRA_URL, JIRA_TOKEN

headers = {
    "Authorization": f"Bearer {JIRA_TOKEN}",
    "Accept": "application/json"
}


def get_story(story_key):

    url = f"{JIRA_URL}/rest/api/2/issue/{story_key}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    print("Error:", response.text)
    return None


def create_testcase(testcase):

    url = f"{JIRA_URL}/rest/api/2/issue"

    payload = {
        "fields": {
            "project": {
                "key": "EV"
            },
            "summary": testcase["summary"],
            "description": testcase["description"],
            "issuetype": {
                "name": "Test Case"
            },
            "customfield_10208": testcase["testSteps"],
            "customfield_10209": testcase["expectedResult"]
        }
    }

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {JIRA_TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        json=payload
    )

    print("Create Test Case Status:", response.status_code)
    print(response.text)

    if response.status_code == 201:
        return response.json()

    return None


def link_testcase(story_key, testcase_key):

    url = f"{JIRA_URL}/rest/api/2/issueLink"

    payload = {
        "type": {
            "name": "is tested by"
        },
        "inwardIssue": {
            "key": story_key
        },
        "outwardIssue": {
            "key": testcase_key
        }
    }

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {JIRA_TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        json=payload
    )

    print("\n===== LINK RESPONSE =====")
    print("Story :", story_key)
    print("Test  :", testcase_key)
    print("Status:", response.status_code)
    print("Body  :", response.text)
    print("=========================\n")