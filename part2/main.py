from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Item(BaseModel):
    name: str
    price: int
    tax: Optional[int] = None


# decorator provides the method
@app.get("/")
async def read_root():
    return {"message":"Hello, World!"}


@app.get("/items/{item_name}")
async def get_items(item_name:str,q:Optional[float]=None):
    return {"item_name":item_name,"q":q}
