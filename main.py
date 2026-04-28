from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Text Summarizer Agent")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Agent is running"}
