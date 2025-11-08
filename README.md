# Simple API (FastAPI)

This is a minimal FastAPI example implementing CRUD operations using an in-memory store.

Requirements

- Python 3.10+
- Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the app

```bash
# start with reload (good for development)
python main.py

# or run directly with uvicorn
uvicorn main:app --reload
```

API endpoints

- GET / -> welcome message
- GET /items -> list all items
- POST /items -> create item (JSON body: name, description (optional), price)
- GET /items/{item_id} -> get single item
- PUT /items/{item_id} -> update item
- DELETE /items/{item_id} -> delete item

Example create request (curl):

```bash
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d \
'{"name":"Notebook","description":"A spiral notebook","price":4.99}'
```

Open the interactive docs at: http://127.0.0.1:8000/docs
# simple-api