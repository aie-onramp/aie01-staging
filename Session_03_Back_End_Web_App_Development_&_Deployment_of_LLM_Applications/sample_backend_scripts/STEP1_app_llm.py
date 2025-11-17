from fastapi import FastAPI
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

#uv run uvicorn STEP1_app_llm:app --reload --host 0.0.0.0 --port 8000