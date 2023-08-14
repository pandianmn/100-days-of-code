from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Maths"},
    {"title": "Title Five", "author": "Author Five", "category": "Maths"},
    {"title": "Title Six", "author": "Author Two", "category": "Maths"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_books_by_category(category: str):
    books = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books.append(book)
    return books


@app.get("/books/{book_author}")
async def read_category_by_query(book_author: str, category: str):
    books = []
    for book in BOOKS:
        if (
            book["author"].casefold() == book_author.casefold()
            and book["category"].casefold() == category.casefold()
        ):
            books.append(book)
    return books


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
