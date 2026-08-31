from fastapi import FastAPI
app= FastAPI()
BOOKS=[
    {'author': 'Salman', 'category':'Male', 'book':'Computer'},
    {'author': 'Iza', 'category': 'Female', 'book': 'English'},
    {'author': 'Ahmad', 'category': 'Male', 'book': 'Computer'},
    {'author': 'Mariyam', 'category': 'female', 'book': 'Urdu'},
    {'author': 'Arham', 'category': 'Male', 'book': 'English'},
    {'author': 'Hamid', 'category': 'Male', 'book': 'Islamic'},

]

@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/search_books")
async def search_books_by_author(book: str, category:str):
    book_return=[]
    for i in BOOKS:
        if i.get('book').casefold()==book.casefold() and \
                i.get('category').casefold()==category.casefold():
            book_return.append(i)

    return book_return
