from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="HotMessCoach")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a supportive mental coach who helps overwhelmed people feel calmer."},
            {"role": "user", "content": req.message},
        ]
    )
    return {"reply": response.choices[0].message.content}

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <h2>🔥 Hot Mess Coach — STEP1 (LLM API)</h2>
    <p>This service exposes <code>POST /chat</code>. Use the interactive docs:</p>
    <p><a href="/docs">Open Swagger UI</a></p>
    """

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

#uvicorn backend.simple_llm:app --reload --host 0.0.0.0 --port 8000