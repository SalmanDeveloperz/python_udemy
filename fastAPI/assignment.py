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
PUT 
"""
# Comparing by id, if id matches then the result should update

@app.put("/books/update_book")
async def update(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('book_id').casefold()== update_book.get('book_id').casefold():
            BOOKS[i]=update_book
