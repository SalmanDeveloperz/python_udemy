"""
Assignment

Here is your opportunity to keep learning!

1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters
 or Query Parameters.

Solution in next video

"""

from fastapi import FastAPI, Body
app= FastAPI()

BOOKS=[
    {'book_id':'1', 'author':'Salman','name':'Mathematics'},
    {'book_id': '2', 'author': 'Saim', 'name': 'English'},
    {'book_id': '3', 'author': 'Asim', 'name': 'Mathematics'},
    {'book_id': '4', 'author': 'Faisal', 'name': 'Urdu'},
]

@app.get("/get_books")
async def get_boos():
    return BOOKS

"""
Search via id and Author
"""

@app.get("/books/search")
async def search(id:str, name:str):
    result=[]
    for i in BOOKS:
        if i.get('book_id').casefold()==id.casefold() and i.get('author').casefold()== name.casefold():
            result.append(i)

    return result


"""
Search author by id using Path parameter or Query parameter
"""
@app.get("/books/search_id{id}")
async def book_id_search(book_id: str):
    book_result=[]
    for i in BOOKS:
        if i.get('book_id').casefold()== book_id.casefold():
            book_result.append(i)

    return book_result


"""
POST
"""

@app.post("/books/new_book")
async def add_book(new_book=Body()):
    BOOKS.append(new_book)




"""
DELETE
"""

@app.delete("/books/del_book")
async def remove_book(del_book=str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('book_id').casefold()== del_book.casefold:
            BOOKS.pop(i)
            break







"""
PUT 
"""
# Comparing by id, if id matches then the result should update

@app.put("/books/update_book")
async def update(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('book_id').casefold()== update_book.get('book_id').casefold():
            BOOKS[i]=update_book




