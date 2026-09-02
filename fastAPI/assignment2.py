"""
Assignment

Here is your opportunity to keep learning!

Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.

Enhance each Book to now have a published_date

Then create a new GET Request method to filter by published_date

"""


from typing import Optional
from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


# book is the new book object where we're initializing a constructor that sets all information

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    # Constructor that initialize the object
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class ValidRequest(BaseModel):
    id: Optional[int] = Field(description='ID not required', default=None)
    # id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=-1, lt=6)  #greater than -1 and less than 6
    published_date: int = Field(gt=1999, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New book ",
                "author": "Muhammad Salman",
                "description": "A Backend Engineer",
                "rating": 5,
                "published_date": 2012

            }
        }
    }


BOOKS = [
    Book(1, 'computer Science', 'M-Salman', 'Computer Fundamentals', 3, 2012),
    Book(2, 'Python', 'Numan', 'Python OOP Fundamentals', 5, 2014),
    Book(3, 'Mathematics', 'Naveed', 'Operations', 5, 2012),
    Book(4, 'English', 'Hassan Tariq', 'IELTS', 3, 2016),
    Book(5, 'Chemistry', 'Saad', 'Organic Chemistry', 4, 2020)

]

"""
GET
"""


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books():
    return BOOKS


#filter out books by ratings until to the condition
@app.get("/books/search_by_rating/", status_code=status.HTTP_200_OK)
async def filter_search_by_rating_show_results_upto_that():
    books_return=[]
    for i in BOOKS:
        if i.rating >= 3:
            books_return.append(i)
    return books_return


# search book by rating
@app.get("/books/search_books/", status_code=status.HTTP_200_OK)
async def search_by_rating(by_rating: int= Query(gt=-1, lt=6)):
    result_list=[]
    for i in BOOKS:
        if i.rating== by_rating:
            result_list.append(i)
    return result_list


# filter books by published_date
@app.get("/books/published_date/", status_code=status.HTTP_200_OK)
async def publish_date(published_date: int):
    result_list=[]
    for i in BOOKS:
        if i.published_date== published_date:
            result_list.append(i)
    return result_list


# search one specific book, from book id, PATH PARAMETERS
@app.get("/books/{book_id}", status_code= status.HTTP_200_OK)
async def search_specific_book_by_id(book_id: int= Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Book not found')


"""
POST
"""
@app.post("/books/create_book", status_code=status.HTTP_201_CREATED)
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
@app.put("/books/update_book", status_code= status.HTTP_204_NO_CONTENT)
async def update_books_record(update_book: ValidRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id== update_book.id:
            BOOKS[i]= update_book
            book_changed= True
    if not book_changed:
        raise HTTPException(status_code=404, detail= 'Book not updated successful')

"""
DELETE
"""
@app.delete("/books/{book_id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int= Path(gt=0)):
    deleted_done= False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            deleted_done= True
            break
    if not deleted_done:
        raise HTTPException(status_code=404, detail='Book not deleted successfully')
