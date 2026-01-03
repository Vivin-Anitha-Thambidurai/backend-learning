"""
security_and_cors.py

Demonstrates:
- CORS configuration
- Security headers
- Production-safe defaults in FastAPI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

app = FastAPI(title="Security & CORS Example")

# ------------------------
# CORS Configuration
# ------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   # frontend dev
        "https://yourfrontend.com" # production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# Security Headers Middleware
# ------------------------

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response: Response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"

        return response


app.add_middleware(SecurityHeadersMiddleware)

# ------------------------
# Routes
# ------------------------

@app.get("/")
def root():
    return {
        "message": "Security headers & CORS enabled 🔐"
    }
