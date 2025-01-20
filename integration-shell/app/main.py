from fastapi import FastAPI
from pydantic import BaseModel

# from app.api.v1.endpoints import items, users, integrations

from app.api.routes.general import router as general_router
from app.api.v1 import router as v1_router


app = FastAPI()




app.include_router(general_router, prefix="", tags=["General"])
# Rutas de la versión 1 de la API
app.include_router(v1_router, prefix="/v1")







# Routes
# app.include_router(items.router, prefix="/items", tags=["Items"])
# app.include_router(users.router, prefix="/users", tags=["Users"])






# Lista en memoria para almacenar los ítems
# items = []





# # Endpoint POST para agregar un ítem
# @app.post("/items/")
# def create_item(item: Item):
#     items.append(item)
#     return item

# # Endpoint GET para listar todos los ítems
# @app.get("/items/", response_model=List[Item])
# def get_items():
#     return items





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



