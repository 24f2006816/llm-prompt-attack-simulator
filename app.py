from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent
import os

SECRET = os.getenv("SECRET")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/solve")
async def solve(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    url = data.get("url")
    secret = data.get("secret")

    if secret != SECRET:
        return JSONResponse(status_code=403, content={"detail": "Invalid secret"})

    background_tasks.add_task(run_agent, url)

    return {"status": "ok"}
