"""
celery_app.py

FastAPI + Celery integration example.
"""

from fastapi import FastAPI
from celery import Celery

app = FastAPI(title="FastAPI + Celery Example")

# ------------------------
# Celery configuration
# ------------------------

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


# ------------------------
# Routes
# ------------------------

@app.get("/")
def root():
    return {"message": "Celery background worker ready 🚀"}


@app.post("/process-task")
def process_task(number: int):
    task = celery_app.send_task("tasks.long_task", args=[number])
    return {
        "task_id": task.id,
        "status": "Task sent to background worker"
    }
