# 🧠 Wubble AI Agent — Internship Technical Assessment

This project is a production-ready FastAPI service designed to handle user prompts using intelligent agents powered by multiple tools. It includes system prompt control, automated evaluation, Docker-based deployment, and conceptual insights into prompt engineering and agent correctness.

---

## 📁 Repository Structure

```
.
├── part1/                    # Agent implementation, evaluation framework
│   ├── app/
│   │   ├── main.py
│   │   ├── agent.py
|   |   |──tools.py
|   |   |──__init__.py
|   |   |──test_evaluation.py
│   │   └── system_prompt.txt
│   ├── requirements.txt
│   └── .env                  # (not tracked in Git)
│
├── part2/                    # Docker & deployment
│   ├── Dockerfile
│   ├── .dockerignore
│   └── start.sh
│
├── part3/                    # Conceptual questions
│   └── ANSWERS.md            # (included below in this README)
│
├── .gitignore
└── README.md
```

---

## 🚀 Part 1: FastAPI Agent Implementation

### ✅ Features

- **FastAPI backend** with OpenAPI (Swagger) support.
- **Two tools integrated**:
  - `LangChain + Groq LLM` for reasoning and responses.
  - `SerpAPI` for real-time search-based answers.
- **System prompt** defines tone, constraints, and fallback behavior.
- **Automated test evaluation** using rule-based scoring.
- **Pydantic models** used for all request/response validation.

### 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Faiq-Ali10/wubble-ai.git
cd wubble-ai
```

2. **Setup virtual environment**

```bash
cd part1
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Create .env file**

```env
GroqAPI=your_groq_api_key
SERPAPI_API_KEY=your_serp_api_key
```

4. **Run the FastAPI app**

```bash
uvicorn app.main:app 
```

5. **Access the docs at http://localhost:8000/docs**

### 🧪 Evaluation Framework

Run the automated test cases with:

```bash
pytest test_evaluation.py
```

The test suite includes:

- Normal queries (weather, math, translations)
- Edge cases (unanswerable questions)
- Off-topic inputs
- Rule-based checks on tone, content, and tool usage

---

## 🐳 Part 2: Docker & Deployment

### 🧱 Docker Build

From the project root:

```bash
cd part2
docker build -t ai-agent-service .
```

### ▶️ Run Docker Container

```bash
docker run -d -p 8000:8000 \
  --memory=512m --cpus=1 \
  --env-file ../part1/.env \
  ai-agent-service
```

The `start.sh` script automates the build and run steps.

---

## 🧠 Part 3: Conceptual Understanding

### 📌 Agent Evaluation & Correctness

**Q1: How would you measure whether your agent is taking the correct action in response to the prompt?**

- By designing test prompts with known, verifiable outputs.
- Using rule-based validators and optionally LLM-as-judge.
- Checking which tool the agent selected, and whether it was contextually appropriate.

**Q2: Propose a mechanism to detect conflicting or stale results.**

- Add a timestamp or freshness check to API responses (e.g., SERP results).
- Compare results from multiple tools and flag if there's significant disagreement.
- Use metadata from the tool response to determine age, source reliability, and consistency.

### ✨ Prompt Engineering Proficiency

**Q3: How do you design system prompts to guide agent behavior effectively?**

- Be explicit about the role and tone (e.g., "You are a concise, factual assistant").
- Define fallback behavior ("If unsure, respond with 'I don't know'").
- Set tool usage rules (e.g., "Use SerpAPI only for real-time info").

**Q4: What constraints, tone, and structure do you enforce, and how do you test them?**

**Constraints:**
- Do not hallucinate if the answer is unknown.
- Avoid making up citations.

**Tone:**
- Friendly, concise, and non-repetitive.

**Structure:**
- Short paragraphs or lists.
- Include source hints if using external tools.

**Testing:**
- Include test cases that intentionally force fallback or edge-case responses.
- Manually verify tone for representative samples.
- Use regex or keyword checks for specific structure and fallback validation.

---

## 📝 .gitignore

```gitignore
__pycache__/
*.pyc
.env
venv/
*.log
```

---

## 👤 Author

**Faiq Ali**
- 📧 faiqalio1oo@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/faiq-ali-83462a255/)

---

## 📄 License

This repository is created for educational and technical assessment purposes.
