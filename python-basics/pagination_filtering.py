"""
pagination_filtering.py

This file demonstrates pagination, filtering,
and search using FastAPI and SQLAlchemy.
"""

from fastapi import FastAPI, Depends, Query
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional

# ------------------------
# Database setup
# ------------------------

DATABASE_URL = "sqlite:///./pagination.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


# ------------------------
# Model
# ------------------------

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    in_stock = Column(Boolean, default=True)


# ------------------------
# App
# ------------------------

app = FastAPI(title="Pagination & Filtering API")


# ------------------------
# Dependency
# ------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# ------------------------
# Routes
# ------------------------

@app.get("/items")
def get_items(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    in_stock: Optional[bool] = None,
    search: Optional[str] = None,
):
    query = db.query(Item)

    if in_stock is not None:
        query = query.filter(Item.in_stock == in_stock)

    if search:
        query = query.filter(Item.name.contains(search))

    total = query.count()
    items = query.offset(offset).limit(limit).all()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "items": items,
    }
