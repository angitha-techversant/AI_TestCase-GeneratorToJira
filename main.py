import json

from jira import (
    get_story,
    create_testcase,
    link_testcase
)

from ai import generate_testcases


story_key = input("Story Key : ")

story = get_story(story_key)

if story is None:
    exit()

summary = story["fields"]["summary"]
description = story["fields"]["description"] or ""

print("\nGenerating Test Cases...\n")

response = generate_testcases(summary, description)

print(response)

testcases = json.loads(response)
print(f"Number of test cases generated: {len(testcases)}")

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(testcases, f, indent=4)

print("\nCreating Jira Test Cases...\n")

for testcase in testcases:

    created = create_testcase(testcase)

    if created:

        testcase_key = created["key"]

        print("Created:", testcase_key)

        link_testcase(story_key, testcase_key)

print("\nFinished Successfully")