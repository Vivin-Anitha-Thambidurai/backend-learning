"""
models.py

Database models (tables).
"""

from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

# ------------------------
# Item model
# ------------------------

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
