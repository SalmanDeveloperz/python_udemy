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
## What is Pydantics:

Pydantics is libraray of Python used for data modeling, data parsing, and has efficient
error handling
```
from pydantic import BaseModel
```


async def create_book(book_request: ValidRequest):
    new_book= Book(**book_request.model_dump())

--- 

## Status Codes

Help to client to understand what happened on the server side application.

Ensure if the request submission successful or not.

---

### 1xx (100 series)

Request is in progress, something happening behind scenes.

---

### 2xx (200 series): Successful Requests

- **200: OK**
  - Successfully retured data to client, mostly GET request.

- **201: Created**
  - Successfully created a new resource, when POST request happened.

- **204: No Content**
  - The request has been successful, did not create an entity nor return anything. Commonly used with PUT requests.

---

### 3xx (300 series): Redirection

Furture actions must be complete.

---

### 4xx (400 series): Client Errors

Caused by client.

- **400: Bad Request**
  - Cannot process request due to client error. Commonly used for invalid request methods.

- **401: Unauthorized**
  - Client does not have valid authentication for target resources.

- **404: Not Found**
  - The client requested resources can not be found.

- **422: Unprocessable Entity**
  - Semantic Errors in Client Request.

---

### 5xx (500 series): Server Errors

An error that occured on the server.

- **500: Internal Server Error**
  - Generic Error Message, when an unexpected issue on the server happened.



## HTTP Exceptions:
```
rasie HTTPException(status_code=404 , detail='Not found/not added or deleted successfully')
```
