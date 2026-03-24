from fastapi import FastAPI, HTTPException
from app.models import Book
from app.middleware import request_timer_middleware

app = FastAPI()

# In-memory list
books = []

@app.middleware("http")
async def timing_middleware(request, call_next):
    return await request_timer_middleware(request, call_next)

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="ID already exists")

    books.append(book)
    return {"message": "Book added", "book": book}