from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.item import get_items, create_item
from app.schemas.item import ItemCreate, ItemOut
from app.api.deps import get_db
from typing import List, Union


router = APIRouter()

@router.get("/", response_model=List[ItemOut])
def read_items(db: Session = Depends(get_db)):
    return get_items(db)


@router.post("/", response_model=ItemOut)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)


# @router.post("/items/")
# def create_item(item: ItemBase, db: Session = Depends(get_db)):
#     db_item = Item(**item.dict())  # Convierte de Pydantic a SQLAlchemy
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return item
