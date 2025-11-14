# 🤝 Assignment: Build Your Full-Stack *Hot Mess Coach* (Backend + LLM + Optional Frontend)

## 📚 Table of Contents

- [Overview](#overview)
- [Part 1 — Backend: Build FastAPI + LLM + Deploy to Vercel 🐍☁️](#part-1--backend-build-fastapi--llm--deploy-to-vercel-️)
  - [Step 1: Set Up Your Environment 🏗️](#step-1-set-up-your-environment-️)
  - [Step 2: Scaffold Your FastAPI Backend 🧱](#step-2-scaffold-your-fastapi-backend-)
  - [Step 3: Add LLM Chat to FastAPI 🤖](#step-3-add-llm-chat-to-fastapi-)
  - [Step 4: Test Locally 🏃](#step-4-test-locally-)
  - [Step 5: Deploy FastAPI to Vercel ☁️](#step-5-deploy-fastapi-to-vercel-️)
- [Part 2 — Advanced Build: Add Frontend to Your Backend (One-Shot Vibecoding) 🎨⚡](#part-2--advanced-build-add-frontend-to-your-backend-one-shot-vibecoding-)
  - [Step 6: Choose Your Frontend (Recommended: Hot Mess Frontend) 💅](#step-6-choose-your-frontend-recommended-hot-mess-frontend-)
  - [Step 7: Generate a New Frontend in v0 with Backend Awareness 🧠→🎬](#step-7-generate-a-new-frontend-in-v0-with-backend-awareness-)
  - [Step 8: Connect Your Frontend → Backend 🔗](#step-8-connect-your-frontend--backend-)
  - [Step 9: Deploy the Frontend to Vercel 🌐](#step-9-deploy-the-frontend-to-vercel-)
- [🏗️ Activity #3: Your Full-Stack Hot Mess Coach](#️-activity-3-your-fullstack-hot-mess-coach)
- [🎓 Tips for Success](#-tips-for-success)

---

# Overview

In this take-home assignment, you will:

1. **Build your own Python FastAPI backend**
2. **Add an LLM endpoint** so users can talk to “Hot Mess Coach”
3. **Deploy the backend to Vercel**
4. (Advanced) **Create a frontend that calls your backend**
5. (Advanced) **Use one-shot vibecoding in v0 to generate a frontend that automatically integrates the backend**

---

# Part 1 — Backend: Build FastAPI + LLM + Deploy to Vercel 🐍☁️

---

## Step 1: Set Up Your Environment 🏗️

```bash
mkdir hot-mess-coach-backend
cd hot-mess-coach-backend
uv venv
source .venv/bin/activate
pip install fastapi uvicorn python-multipart openai
```

---

## Step 2: Scaffold Your FastAPI Backend 🧱

Create `main.py`:

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hot Mess Coach API is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
```

Run:

```bash
uvicorn main:app --reload
```

---

## Step 3: Add LLM Chat to FastAPI 🤖

```python
from pydantic import BaseModel
from openai import OpenAI
client = OpenAI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are the Hot Mess Coach. A chaotic but helpful guide."},
            {"role": "user", "content": req.message}
        ]
    )
    return {"reply": completion.choices[0].message["content"]}
```

---

## Step 4: Test Locally 🏃

```
uvicorn main:app --reload
```

Visit:

- http://localhost:8000  
- http://localhost:8000/docs  

---

## Step 5: Deploy FastAPI to Vercel ☁️

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

# Part 2 — Advanced Build: Add Frontend to Your Backend (One-Shot Vibecoding) 🎨⚡

---

## Step 6: Choose Your Frontend (Recommended: Hot Mess Frontend) 💅

You may reuse the *Hot Mess Tracker* frontend from class or generate a new one.

---

## Step 7: Generate a New Frontend in v0 with Backend Awareness 🧠→🎬

Example prompt:

```
Create me a frontend called “Hot Mess Coach UI”.

This frontend must call my backend:
POST https://YOUR_BACKEND.vercel.app/chat

Body:
{ "message": "text" }

Use React + Tailwind + shadcn/ui.
Add playful chaotic UI elements.
Implement a chat interface that displays the LLM replies.
```

---

## Step 8: Connect Your Frontend → Backend 🔗

```ts
export async function sendMessage(message: string) {
  const res = await fetch("https://YOUR_BACKEND.vercel.app/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });
  return res.json();
}
```

Replace with your backend URL.

---

## Step 9: Deploy the Frontend to Vercel 🌐

```bash
vercel
```

Your full-stack Hot Mess Coach is now live! 🎉

---

# 🏗️ Activity #3: Your Full-Stack Hot Mess Coach

### Required
- Build FastAPI backend  
- Add `/chat` endpoint  
- Deploy backend  

### Advanced
- Create frontend using v0 or reuse Hot Mess frontend  
- Connect to backend  
- Deploy frontend  

---

# 🎓 Tips for Success

- Use Cursor AI agents with your GitFlow rules  
- Test locally before deploying  
- Give v0 clear instructions (backend URL, endpoint, JSON format)  
- Keep your code clean and modular  

---
