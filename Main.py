
from fastapi import FastAPI

app = FastAPI(title="AI Viral Clips Backend")

@app.get("/")
def home():
    return {
        "message": "AI Viral Clips Backend is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
