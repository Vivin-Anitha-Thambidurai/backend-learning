"""
main.py

Production-style FastAPI application entry point.
"""

from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(
    title="Backend App",
    version="1.0.0",
    description="Production-ready FastAPI backend"
)

# Include API routes
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Backend project is running 🚀"}
