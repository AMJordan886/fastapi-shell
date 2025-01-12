from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

# Lista en memoria para almacenar los ítems
items = []

# Modelo Pydantic compatible con Python 3.9
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# Endpoint POST para agregar un ítem
@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item

# Endpoint GET para listar todos los ítems
@app.get("/items/", response_model=List[Item])
def get_items():
    return items





# from typing import Union, List

# from fastapi import FastAPI
# from pydantic import BaseModel



# app = FastAPI()

# items = []


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None






# @app.post("/items/")
# def create_item(item: Item):
#     items.append(item)
#     return item


# @app.get("/items/", response_model=List[Item])
# def get_items():
#     return items








# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}



