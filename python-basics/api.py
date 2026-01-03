"""
api.py

Central API router.
All route modules are included here.
"""

from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

# ------------------------
# Health / status route
# ------------------------

@api_router.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is healthy ✅"
    }


# ------------------------
# Example route group
# (later we will move this to separate modules)
# ------------------------

@api_router.get("/hello")
def hello(name: str = "world"):
    return {
        "message": f"Hello, {name} 👋"
    }
