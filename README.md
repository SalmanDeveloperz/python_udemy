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

```
uvicorn books:app --reload
```
## casefold():
casefold() converts a string into a form designed for case-insensitive comparison. It makes strings into lowercase like `"Salman" = "salman"`

## Path Parameters:
Path Parameters are dynamic variables embedded directly inside the URL path. They are primarily used to uniquely pinpoint a specific resource within an API.
```
@app.get("/items/{item_id}")
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

```
async def create_book(book_request: ValidRequest):
    new_book= Book(**book_request.model_dump())
```
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
