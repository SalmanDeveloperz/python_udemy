from fastapi import FastAPI

app= FastAPI()

BOOKS=[
    {'title': 'Title One', 'author': 'Muhammad', 'category': 'Spirtual'},
    {'title': 'Title two', 'author': 'Salman', 'category': 'Science'},
    {'title': 'Title One', 'author': 'Ahsan', 'category': 'Spirtual'},
    {'title': 'Title One', 'author': 'Umar', 'category': 'English'},
    {'title': 'Title One', 'author': 'Zain', 'category': 'Computer'}

]
@app.get("/books") #root decorator
async def read_all_books(): #FastAPI supports asynchronous endpoints. so tha't why used async
    return BOOKS

@app.get("/books/mybook")
async def book_reading():
    return {'book_title': 'My favourite book'}

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return{'dynamic_param': dynamic_param}

@app.get("/books/{book_title}")
async def read_book_in_loop(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


async def read_books_category(category:str):
    books_return=[]
    for i in BOOKS:
        if i.get('category').casefold()== category.casefold():
            books_return.append(i)
        return book_return
