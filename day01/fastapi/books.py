from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Fiction"},
    {"title": "Title Three", "author": "Author Three", "category": "Science"},
    {"title": "Title Four", "author": "Author Four", "category": "Fiction"},
    {"title": "Title Five", "author": "Author Five", "category": "Science"},
    {"title": "Title Six", "author": "Author Two", "category": "Science"},
]


@app.get("/api-endpoint")
async def first_api():
    return BOOKS


# @app.get("/books")
# async def read_all_books():
