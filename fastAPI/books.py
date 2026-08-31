from fastapi import FastAPI

app= FastAPI()

BOOKS=[
    {'title': 'Title One', 'author': 'Muhammad', 'category': 'Spirtual'},
    {'title': 'Title two', 'author': 'Salman', 'category': 'Science'},
    {'title': 'Title One', 'author': 'Ahsan', 'category': 'Mathematics'},
    {'title': 'Title One', 'author': 'Umar', 'category': 'English'},
    {'title': 'Title One', 'author': 'Zain', 'category': 'Computer'}

]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def book_reading():
    return {'book_title': 'My favourite book'}

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return{'dynamic_param': dynamic_param}

