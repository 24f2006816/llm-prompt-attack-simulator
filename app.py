from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.post("/solve")
async def solve(payload: dict):
    task = payload.get("task") or str(payload)
    output = run_agent(task)
    return {"result": output}

@app.get("/")
async def home():
    return {"status": "OK", "message": "GROQ-backed API live!"}
