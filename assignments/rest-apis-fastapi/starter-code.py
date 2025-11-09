"""Starter code for Building REST APIs with FastAPI assignment.

This is a minimal FastAPI app students can expand.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int | None = None
    name: str
    price: float

_store: List[Item] = []
_next_id = 1

@app.get("/items", response_model=List[Item])
def list_items():
    return _store

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _store.append(item)
    return item

if __name__ == "__main__":
    print("This file is starter code. Run with: uvicorn starter-code:app --reload")
