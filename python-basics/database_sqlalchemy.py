"""
database_sqlalchemy.py

This file demonstrates how to use SQLAlchemy with FastAPI
to interact with a SQLite database.
"""

from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ------------------------
# Database setup
# ------------------------

DATABASE_URL = "sqlite:///./test.db"

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
    in_stock = Column(Boolean, default=True)


# ------------------------
# App
# ------------------------

app = FastAPI(title="FastAPI + SQLAlchemy")


# ------------------------
# DB Dependency
# ------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------
# Routes
# ------------------------

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.post("/items")
def create_item(name: str, db: Session = Depends(get_db)):
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
