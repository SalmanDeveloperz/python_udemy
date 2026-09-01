from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
app= FastAPI()

# book is the new book object where we're initializing a constructor that sets all information

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    # Constructor that initialize the object
    def __init__(self, id, title, author, description, rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class ValidRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

BOOKS=[
    Book(1,'computer Science', 'M-Salman', 'Computer Fundamentals', '3'),
    Book(2, 'Python', 'Numan', 'Python OOP Fundamentals', '5'),
    Book(3, 'Mathematics', 'Naveed', 'Operations', '5'),
    Book(4, 'English', 'Hassan Tariq', 'IELTS', '3'),
    Book(5, 'Chemistry', 'Saadullah', 'Organic Chemistry', '4')

]

"""
GET
"""
@app.get("/books")
async def get_books():
    return BOOKS


"""
POST
"""
@app.post("/books/create_book")
async def create_book(book_request: ValidRequest):
    new_book= Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(new_book)



