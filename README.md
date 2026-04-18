# 🤖 Autonomous AI Agent

An autonomous AI agent that thinks, decides, and acts on its own to complete goals — built using **Tool Use** and the **Claude API by Anthropic**.

---

## 💡 What It Does

Give the agent a goal in plain English. It will figure out the steps needed, use the right tools, and complete the task — all without you doing anything else.

**Example goals:**
- *"Research Python developer salaries in Dublin and calculate the average"*
- *"Search for the top software companies hiring in Ireland"*
- *"Find information about RAG in AI and summarise it"*

---

## 🧠 What is an AI Agent?

Unlike a regular chatbot that just answers questions, an AI agent can **take actions** to complete a goal:

```
🎯 You give a goal
    ↓
🤔 Claude THINKS  — "What do I need to do?"
    ↓
🔧 Claude ACTS    — uses a tool (search / calculate)
    ↓
👀 Claude OBSERVES — reads the result
    ↓
🤔 Claude THINKS again — "Is the goal done? What's next?"
    ↓
✅ Final answer when goal is complete
```

This is called a **ReAct loop** — the same architecture used in ChatGPT, Perplexity AI, and every modern AI assistant.

---

## 🛠️ Tools Available

| Tool | What it does |
|------|-------------|
| 🔍 `search_web` | Searches DuckDuckGo for current information |
| 🧮 `calculate` | Evaluates mathematical expressions |

---

## 💻 Tech Stack

- **Python 3.10+**
- **Claude API** (Anthropic) — `claude-sonnet-4-6`
- **Tool Use** — Claude's native function calling feature
- **requests** — HTTP calls to DuckDuckGo search API
- **python-dotenv** — secure API key management

---

## 🚀 How to Run It

### 1. Clone the repo
```bash
git clone https://github.com/AnanthiMuthu02/ai-agent.git
cd ai-agent
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install anthropic python-dotenv requests
```

### 4. Set up your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```
Get your key at [platform.claude.com](https://platform.claude.com)

### 5. Run the agent
```bash
python agent.py
```

---

## 💬 Example Output

```
🤖 AI Agent — powered by Claude
----------------------------------------
Give me a goal to work on: Research Python developer salaries in Dublin and calculate the average

🎯 Goal: Research Python developer salaries in Dublin and calculate the average
==================================================

🔧 Agent using tool: search_web
   Input: {'query': 'Python developer salary Dublin Ireland 2026'}
   Result: Python developers in Dublin earn between €50,000 and €75,000...

🔧 Agent using tool: calculate
   Input: {'expression': '(50000+75000)/2'}
   Result: Result: 62500...

✅ Final Answer:
Based on my research, Python developers in Dublin, Ireland earn
between €50,000 and €75,000 annually. The average salary is
approximately €62,500, making it one of the more competitive
tech markets in Europe.
```

---

## 🔑 Key Concepts Learned

| Concept | Description |
|--------|-------------|
| AI Agents | Autonomous systems that think and act to complete goals |
| Tool Use | Giving Claude the ability to call external functions |
| ReAct Loop | Think → Act → Observe → Repeat pattern |
| Function Calling | Claude decides which tool to use and when |
| DuckDuckGo API | Free search API for real-time web information |

---

## 🔒 Security Note

Never commit your `.env` file. This repo includes a `.gitignore` that automatically excludes it.

---

## 👩‍💻 Author

**Ananthi Muthu**
Backend & Full Stack Software Engineer | Dublin, Ireland
[LinkedIn](https://www.linkedin.com/in/ananthi-muthu-76b3101a8/) | [GitHub](https://github.com/AnanthiMuthu02)

---

## 📌 Part of my AI/ML Portfolio

- ✅ Project 1: [AI Resume Tailor](https://github.com/AnanthiMuthu02/ai-resume-tailor)
- ✅ Project 2: [AI Chatbot with Memory](https://github.com/AnanthiMuthu02/ai-chatbot-memory)
- ✅ Project 3: [AI Document Q&A with RAG](https://github.com/AnanthiMuthu02/ai-document-qa)
- ✅ Project 4: Autonomous AI Agent ← You are here
