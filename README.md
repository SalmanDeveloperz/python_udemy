# GET REQUEST

## For installation of Python virtual Environment:-

```
python -m venv fastvenv
```

## To activate the Virtual Environment:-
```
fastvenv\Scripts\activate.bat
```

## Endpoints:
An endpoint are a specific doorway into your API.
If your API is a building, each endpoint is a different door that performs a particular job.

## Uvicorn:-
Uvicorn is the FAST API server

For uvicorn Installation:-
```
pip install "uvicorn[standard]"
```

## Path Parameters:
the way for us to be able to locate in FASTAPI where we want an application to run and it's just overall path or the URL

```
uvicorn books:app --reload
```

## casefold():
casefold() converts a string into a form designed for case-insensitive comparison.

## Path parameter:
A path parameter is a variable value embedded directly into the URL path that identifies or selects a specific resource.

**Path parameter** = **"WHICH ONE?"**

```
@app.get("/books/{book}")
async def get_book(book: str):
    return {"book": book}
```

## Query parameters:

Query parameters are the request parameters that have been attachend after "?"

It's the way to filter data based on the URL provider. It have name=value pairs

```
@app.get("/search_books")
async def search_books_by_name_and_category(book: str, category: str):
```
