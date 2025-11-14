# 🚀 Breakout Room #1: Build & Deploy Your First Backend – *Hot Mess Coach*

Welcome! In this breakout room we switch from frontend to backend—students will build a **Python FastAPI application**, integrate **LLM-powered chat**, analyze documents (PDF, CSV), and deploy the full backend to **Vercel**.

---

## 📚 Table of Contents

- [What Is This Demo?](#what-is-this-demo)
- [Prerequisites](#prerequisites)
- [Overview](#overview)
- [Step 1: Create Your FastAPI "Hot Mess Coach" App 🐍](#step-1-create-your-fastapi-hot-mess-coach-app-)
- [Step 2: Run Locally 🏃](#step-2-run-locally-)
- [Step 3: Add GitFlow + Cursor Rules 📝](#step-3-add-gitflow--cursor-rules-)
- [Step 4: Deploy FastAPI Backend to Vercel ☁️](#step-4-deploy-fastapi-backend-to-vercel-️)
- [Step 5: Add LLM Chat to Hot Mess Coach 🤖](#step-5-add-llm-chat-to-hot-mess-coach-)
- [Step 6: Context Engineering + Document Analysis (PDF/CSV) 📄➡️🧠](#step-6-context-engineering--document-analysis-pdfcsv-️)
- [Advanced Module: Chunking + Uploading CSV/PDF + Local Testing + Re-deploy 🚀](#advanced-module-chunking--uploading-csvpdf--local-testing--re-deploy-)
- [🏗️ Activity #1](#️-activity-1)

---

## Prerequisites

- Python 3.10+
- Cursor IDE
- GitHub account
- Vercel account
- Install Vercel CLI:
  ```bash
  npm install -g vercel
  ```

---

## 🤝 Breakout Room #1

A full hands-on backend session using FastAPI + LLM + document analysis + deployment.

---

# What Is This Demo?

Students will:

- Build a FastAPI backend
- Use Cursor agents with GitFlow rules
- Deploy to Vercel
- Add LLM chat
- Add PDF/CSV document analysis
- Learn context engineering
- Learn chunking + JSON structuring
- Test locally + redeploy

---

# 📝 Step 1: Add GitFlow + Cursor Rules

Add:

- `gitflow_rules.md`
- `cursor_rules.md`

Teach feature branches, PRs, merging into `develop`, releasing to `main`.

---

# 🏃 Step 2: Run Locally

Visit:
- http://localhost:8000
- http://localhost:8000/docs

---
# 🐍 Step 3: Create Your FastAPI "Hot Mess Coach" App

```bash
mkdir hot-mess-coach
cd hot-mess-coach
uv venv
source .venv/bin/activate
pip install fastapi uvicorn python-multipart
```

Create `main.py` with a basic FastAPI app + `/analyze` endpoint.

Run locally:
```bash
uvicorn main:app --reload
```

---

# ☁️ Step 4: Deploy FastAPI Backend to Vercel

Create `vercel.json`:

```json
{
  "builds": [{ "src": "main.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}
```

Deploy:

```bash
vercel
```

---

# 🤖 Step 5: Add LLM Chat to Hot Mess Coach

Add `/chat` endpoint:

- Input: `{"message": "..."}`
- Output: LLM-powered response
- Add persona: “Hot Mess Coach”

Add system instructions for context engineering.

---

# 📄➡️🧠 Step 6: Context Engineering + Document Analysis

Add endpoints:

### `/upload-csv`
- Accept CSV → convert to JSON → summarize via LLM

### `/upload-pdf`
- Extract text → send structured JSON to LLM

---

# 🚀 Advanced Module: Chunking + Local Testing + Re-deploy

Chunking helper:

```python
def chunk_text(text, size=1500):
    return [text[i:i+size] for i in range(0, len(text), size)]
```

Test in a notebook → integrate into FastAPI → run locally → deploy again.

---

# 🏗️ Activity #1

Now it's your turn to experiment and get creative! Use this time to practice what you've learned and explore the tools.

**Experiment with Backend Customization:**

- Create a new .py file containing your FastAPI application
- Add an LLM-powered chatbot endpoint
- use .env for API-KEY
- Create feature branches for each new addition
- Implement extra features (new routes, utilities, or enhancements)
- Open and merge pull requests following GitFlow best practices
- Deploy your updated backend to Vercel



---

Enjoy building your backend AI app! 🎉
