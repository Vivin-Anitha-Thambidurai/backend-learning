"""
basic_fastapi_app.py

A simple FastAPI application demonstrating:
- GET and POST endpoints
- Path parameters
- Request body validation
- Async backend programming
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="My First FastAPI App")


# ------------------------
# Data model
# ------------------------

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# Fake database
items_db: List[Item] = []


# ------------------------
# Routes
# ------------------------

@app.get("/")
async def root():
    return {"message": "FastAPI is running 🚀"}


@app.get("/items")
async def get_items():
    return items_db


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        return {"error": "Item not found"}
    return items_db[item_id]


@app.post("/items")
async def create_item(item: Item):
    items_db.append(item)
    return {
        "message": "Item added successfully",
        "item": item
    }
