# 🤖 AI Jira Test Case Generator

An AI-powered automation tool that retrieves Jira Stories or Tasks, generates comprehensive software test cases using Large Language Models (LLMs), creates Test Case issues in Jira, and automatically links them back to the original requirement.

---

## 📌 Overview

Manual test case creation is repetitive and time-consuming. This project automates the process by integrating Jira with AI models through OpenRouter.

The application performs the following tasks:

1. Retrieves a Jira Story/Task using the Jira REST API.
2. Extracts the Summary and Description.
3. Sends the requirement to an AI model.
4. Generates structured software test cases.
5. Creates Test Case issues in Jira.
6. Links each Test Case back to the original Story/Task using the **"is tested by"** relationship.

---

## 🚀 Features

- Fetch Jira Story or Task details
- AI-generated software test cases
- Positive test scenarios
- Negative test scenarios
- Boundary value scenarios
- Validation scenarios
- UI test scenarios
- Automatic Jira Test Case creation
- Automatic linking of Test Cases to Story/Task
- Secure configuration using environment variables
- Supports OpenRouter free AI models

---

## 🛠 Tech Stack

- Python 3.x
- Jira REST API
- OpenRouter API
- Requests
- OpenAI Python SDK
- python-dotenv

---

## 📁 Project Structure

```
AI_Jira_TestCase_Generator/
│
├── ai.py                 # AI integration
├── jira.py               # Jira API functions
├── config.py             # Environment configuration
├── main.py               # Application entry point
├── list_models.py        # List available OpenRouter models
├── link_types.py         # Display Jira link types
├── requirements.txt
├── .gitignore
├── README.md
└── .env                  # Not committed to GitHub
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/angitha-techversant/AI_TestCase-GeneratorToJira.git
```

Navigate to the project

```bash
cd AI_TestCase-GeneratorToJira
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
JIRA_URL=https://your-jira-url
JIRA_TOKEN=your_jira_api_token
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## ▶️ Running the Project

Execute:

```bash
python main.py
```

Enter the Jira Story or Task key.

Example:

```
EV-1755
```

The application will:

- Fetch the Jira requirement
- Generate AI-based test cases
- Create Jira Test Case issues
- Link them to the Story

---

## 🔄 Workflow

```
Jira Story
      │
      ▼
Fetch Story Details
      │
      ▼
Extract Summary & Description
      │
      ▼
OpenRouter AI
      │
      ▼
Generate Test Cases
      │
      ▼
Create Jira Test Cases
      │
      ▼
Link using
"is tested by"
```

---

## 📦 Sample Output

```
Story Key: EV-1755

Generating Test Cases...

Created:
EV-1767

Linked Successfully

Created:
EV-1768

Linked Successfully

Created:
EV-1769

Linked Successfully

Finished Successfully
```

---

## 🔮 Future Enhancements

- Generate all possible software test scenarios
- Export test cases to Excel
- Export test cases to CSV
- Export test cases to PDF
- Generate API test cases
- Generate Security test cases
- Generate Performance test cases
- Generate Accessibility test cases
- Duplicate detection
- Streamlit Web UI
- Bulk Story processing
- Direct Jira Plugin integration

---

## 👨‍💻 Author

**Angitha P K**

QA Engineer

---

## 📄 License

This project is intended for educational and internal automation purposes.
