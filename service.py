from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
     name: str
     price: float
     is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q":q}


@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {"item_name": item.pr, "item_id": item_id}     

