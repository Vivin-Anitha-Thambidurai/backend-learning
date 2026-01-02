"""
celery_worker.py

Celery worker that executes long-running tasks.
"""

from celery import Celery
import time

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


@celery.task(name="tasks.long_task")
def long_task(number: int):
    time.sleep(5)  # simulate heavy work
    return {
        "input": number,
        "result": number * number
    }
