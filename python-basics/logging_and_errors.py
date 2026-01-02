"""
logging_and_errors.py

This file demonstrates logging and global error handling
in a FastAPI application.
"""

import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# ------------------------
# Logging setup
# ------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ------------------------
# App
# ------------------------

app = FastAPI(title="Logging & Error Handling Example")


# ------------------------
# Routes
# ------------------------

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Logging enabled ✅"}


@app.get("/divide")
def divide(a: int, b: int):
    logger.info(f"Divide called with a={a}, b={b}")

    try:
        result = a / b
        return {"result": result}
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        return {"error": "Cannot divide by zero"}


# ------------------------
# Global exception handler
# ------------------------

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )
