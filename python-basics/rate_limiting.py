"""
rate_limiting.py

Demonstrates simple rate limiting in FastAPI
using in-memory storage.
(Production systems use Redis, but this explains the core logic.)
"""

from fastapi import FastAPI, Request, HTTPException
import time

app = FastAPI(title="Rate Limiting Example")

# ------------------------
# Rate limit configuration
# ------------------------

RATE_LIMIT = 5          # max requests
TIME_WINDOW = 60        # seconds

# In-memory store: {ip: [timestamps]}
request_log = {}


# ------------------------
# Middleware
# ------------------------

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    current_time = time.time()

    if client_ip not in request_log:
        request_log[client_ip] = []

    # Remove old requests
    request_log[client_ip] = [
        t for t in request_log[client_ip]
        if current_time - t < TIME_WINDOW
    ]

    if len(request_log[client_ip]) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    request_log[client_ip].append(current_time)
    response = await call_next(request)
    return response


# ------------------------
# Routes
# ------------------------

@app.get("/")
def root():
    return {
        "message": "Rate limiting enabled 🚦",
        "limit": f"{RATE_LIMIT} requests per {TIME_WINDOW} seconds"
    }


@app.get("/data")
def get_data():
    return {"data": "This is protected by rate limiting"}
