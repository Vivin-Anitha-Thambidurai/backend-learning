"""
crud.py

Database operations for Items.
"""

from sqlalchemy.orm import Session
from app import models, schemas


# ------------------------
# Create item
# ------------------------

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name=item.name,
        price=item.price,
        in_stock=item.in_stock
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# ------------------------
# Get all items
# ------------------------

def get_items(db: Session):
    return db.query(models.Item).all()


# ------------------------
# Get item by ID
# ------------------------

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()
