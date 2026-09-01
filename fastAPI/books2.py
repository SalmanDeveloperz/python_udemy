from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


# book is the new book object where we're initializing a constructor that sets all information

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    # Constructor that initialize the object
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class ValidRequest(BaseModel):
    id: Optional[int] = Field(description='ID not required', default=None)
    # id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=-1, lt=6)  #greater than -1 and less than 6

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New book ",
                "author": "Muhammad Salman",
                "description": "A Backend Engineer",
                "rating": 5

            }
        }
    }


BOOKS = [
    Book(1, 'computer Science', 'M-Salman', 'Computer Fundamentals', 3),
    Book(2, 'Python', 'Numan', 'Python OOP Fundamentals', 5),
    Book(3, 'Mathematics', 'Naveed', 'Operations', 5),
    Book(4, 'English', 'Hassan Tariq', 'IELTS', 3),
    Book(5, 'Chemistry', 'Saad', 'Organic Chemistry', 4)

]

"""
GET
"""


@app.get("/books")
async def get_books():
    return BOOKS


#search books by ratings
@app.get("/books/search_by_rating")
async def filter_search_by_rating():
    books_return=[]
    for i in BOOKS:
        if i.rating >= 3:
            books_return.append(i)
    return books_return


# search one specific book, from book id
@app.get("/books/{book_id}")
async def search_specific_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return None

"""
POST
"""


@app.post("/books/create_book")
async def create_book(book_request: ValidRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(unique_book_id(new_book))


# Let's create the Primary or Unique id for every iteration
def unique_book_id(i: Book):
    if len(BOOKS) > 0:
        i.id = BOOKS[-1].id + 1
    else:
        i.id = 1

    return i



"""
PUT
"""
@app.put("/books/update_book")
async def update_books_record(update_book: ValidRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id== update_book.id:
            BOOKS[i]= update_book


"""
DELETE
"""
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            break
