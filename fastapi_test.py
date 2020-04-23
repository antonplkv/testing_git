from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get('/')
@app.get('/{item_id}')
def start(item_id: str = None, key: str = Query(..., max_length=3), key2: str = None):
    print(key)
    return Item(name='Name', description='desc', price=12.5)