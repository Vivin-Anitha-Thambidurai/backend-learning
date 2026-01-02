"""
background_tasks_and_cache.py

Demonstrates:
- Background tasks in FastAPI
- Simple in-memory caching
"""

from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI(title="Background Tasks & Cache Example")

# ------------------------
# Simple in-memory cache
# ------------------------

cache = {}


# ------------------------
# Background task function
# ------------------------

def write_log(message: str):
    time.sleep(3)  # simulate long task
    with open("app.log", "a") as f:
        f.write(message + "\n")


# ------------------------
# Routes
# ------------------------

@app.get("/")
def root():
    return {"message": "Background tasks & caching API 🚀"}


# Background task example
@app.post("/send-log")
def send_log(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"status": "Log will be written in background"}


# Cached endpoint
@app.get("/slow-data")
def get_slow_data():
    if "data" in cache:
        return {
            "source": "cache",
            "data": cache["data"]
        }

    # Simulate slow computation
    time.sleep(5)
    data = {
        "value": "This took 5 seconds to generate"
    }

    cache["data"] = data
    return {
        "source": "generated",
        "data": data
    }
