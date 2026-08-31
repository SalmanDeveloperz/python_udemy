from fastapi import FastAPI, Body

app= FastAPI()


BOOKS=[
    {'author': 'Salman', 'category':'Male', 'book':'Computer'},
    {'author': 'Iza', 'category': 'Female', 'book': 'English'},
    {'author': 'Ahmad', 'category': 'Male', 'book': 'Computer'},
    {'author': 'Mariyam', 'category': 'female', 'book': 'Urdu'},
    {'author': 'Arham', 'category': 'Male', 'book': 'English'},
    {'author': 'Hamid', 'category': 'Male', 'book': 'Islamic'},

]


"""
GET METHOD
"""


# Get all books
@app.get("/get_books")
async def get_all_books():
    return BOOKS


# Search Books in GET Method
@app.get("/search_books")
async def search_books_by_name_and_category(book: str, category:str):
    list_book= []
    for i in BOOKS:
        if i.get('book').casefold()== book.casefold() and i.get('category').casefold()== category.casefold():
            list_book.append(i)

    return list_book


"""
POST Method
"""
@app.post("/books/new_book")
async def new_book(newbook=Body()):
    BOOKS.append(newbook)


"""
PUT Request Method
"""
@app.put("/books/update_book")
async def update_book(updated_book= Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold()== updated_book.get('author').casefold():
           BOOKS[i]=updated_book



"""
DELETE Request Method
"""

@app.delete("/books/delete_book")
async def delete_book(author_name: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold()== author_name.casefold():
            BOOKS.pop(i)
            break
