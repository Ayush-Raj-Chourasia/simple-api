from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple API", version="0.1.0")


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Item(ItemCreate):
    id: int


# In-memory storage
_items: Dict[int, Item] = {}
_next_id = 1


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the Simple API (FastAPI)"}


@app.get("/items", response_model=List[Item])
def list_items():
    return list(_items.values())


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global _next_id
    new_item = Item(id=_next_id, **item.dict())
    _items[_next_id] = new_item
    _next_id += 1
    return new_item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return _items[item_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **item.dict())
    _items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return None


if __name__ == "__main__":
    # Quick local runner: python main.py
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
