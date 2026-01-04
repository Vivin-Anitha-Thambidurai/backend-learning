"""
schemas.py

Pydantic models for request and response validation.
"""

from pydantic import BaseModel


# ------------------------
# Base schema
# ------------------------

class ItemBase(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# ------------------------
# Create schema
# ------------------------

class ItemCreate(ItemBase):
    pass


# ------------------------
# Response schema
# ------------------------

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
