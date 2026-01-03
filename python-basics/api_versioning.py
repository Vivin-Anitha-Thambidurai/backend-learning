"""
api_versioning.py

Demonstrates API versioning in FastAPI.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Versioned API Example",
    description="Demonstrates API versioning best practices",
    version="1.0.0"
)

# ------------------------
# V1 API
# ------------------------

@app.get("/api/v1/status")
def status_v1():
    return {
        "version": "v1",
        "message": "API v1 is stable"
    }


@app.get("/api/v1/users")
def users_v1():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]


# ------------------------
# V2 API
# ------------------------

@app.get("/api/v2/status")
def status_v2():
    return {
        "version": "v2",
        "message": "API v2 with more features 🚀"
    }


@app.get("/api/v2/users")
def users_v2():
    return {
        "count": 2,
        "users": [
            {"id": 1, "name": "Alice", "role": "admin"},
            {"id": 2, "name": "Bob", "role": "user"}
        ]
    }
