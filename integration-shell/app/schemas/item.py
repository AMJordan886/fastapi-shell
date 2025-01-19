from pydantic import BaseModel
from typing import Union




class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    class Config:
        # orm_mode = True
        from_attributes = True  # ✅ Nuevo en Pydantic V2









class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True  # ✅ Nuevo en Pydantic V2


