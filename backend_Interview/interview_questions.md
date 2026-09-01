# Python + FastAPI Software Engineer Interview Questions

## 1. Python Fundamentals

1. What is Python? What are its main features?
2. What are the built-in data types in Python?
3. What is the difference between a list, tuple, set, and dictionary?
4. What is the difference between mutable and immutable objects?
5. What is the difference between `==` and `is`?
6. What is type casting/type conversion in Python?
7. What is the difference between `append()`, `extend()`, and `insert()`?
8. What is the difference between `remove()`, `pop()`, and `del`?
9. What is list slicing?
10. How does negative indexing work?
11. What are list comprehensions?
12. What are dictionary comprehensions?
13. What are set comprehensions?
14. How do you check whether an item exists in a list, set, or dictionary?
15. What is the difference between `in` and `not in`?
16. What is the difference between `sort()` and `sorted()`?
17. What is the difference between `copy()` and assigning a variable directly?
18. What is shallow copy vs deep copy?
19. What is `None` in Python?
20. What is truthy and falsy in Python?


## 2. Python Functions

1. How do you define a function in Python?
2. What is the difference between a parameter and an argument?
3. What are positional arguments?
4. What are keyword arguments?
5. What are default arguments?
6. What is the difference between `return` and `print()`?
7. What are `*args` and `**kwargs`?
8. What is variable-length argument handling?
9. What is variable scope in Python?
10. What are local and global variables?
11. What is the `global` keyword?
12. What is the `nonlocal` keyword?
13. What are lambda functions?
14. What is a higher-order function?
15. What are first-class functions?
16. What is recursion?
17. What are `map()`, `filter()`, and `reduce()`?
18. What is a function annotation/type hint?
19. What are positional-only and keyword-only arguments?
20. What happens if a function doesn't explicitly return anything?


## 3. Python OOP

1. What is Object-Oriented Programming?
2. What is a class?
3. What is an object?
4. What is the difference between a class and an object?
5. What is `self`?
6. What is `__init__()`?
7. What are instance attributes?
8. What are class attributes?
9. What is inheritance?
10. What are the different types of inheritance?
11. What is multiple inheritance?
12. What is method overriding?
13. Does Python support method overloading?
14. What is polymorphism?
15. What is encapsulation?
16. What is abstraction?
17. What are the four pillars of OOP?
18. What is `super()`?
19. What is the difference between instance, class, and static methods?
20. What does `@classmethod` do?
21. What does `@staticmethod` do?
22. What are public, protected, and private attributes in Python?
23. What is name mangling?
24. What is composition vs inheritance?
25. When would you prefer composition over inheritance?


## 4. Python Exception Handling

1. What is an exception?
2. What is the difference between an error and an exception?
3. How does `try`/`except` work?
4. What is the purpose of `else` in exception handling?
5. What is the purpose of `finally`?
6. Can you have multiple `except` blocks?
7. What is the difference between `raise` and `return`?
8. How do you raise a custom exception?
9. How do you create a custom exception class?
10. What happens if an exception is not handled?
11. What is exception propagation?
12. Why should you avoid using a bare `except`?
13. How would you handle exceptions in a FastAPI application?


## 5. Python Modules and Packages

1. What is a module?
2. What is a package?
3. What is the difference between a module and a package?
4. What is the difference between:
   - `import module`
   - `from module import something`
   - `from module import *`
5. What is `__init__.py`?
6. What is `if __name__ == "__main__":`?
7. What is a virtual environment?
8. Why do we use `venv`?
9. What is `pip`?
10. What is `requirements.txt`?
11. What is dependency management?


## 6. Python Decorators

1. What is a decorator?
2. Why are decorators used?
3. How do decorators work internally?
4. What is a wrapper function?
5. What does `@decorator` syntax mean?
6. Can a decorator accept arguments?
7. What is `functools.wraps`?
8. Where might decorators be useful in backend development?
9. Can you write a simple custom decorator?


## 7. Python Iterators and Generators

1. What is an iterable?
2. What is an iterator?
3. What is the difference between an iterable and an iterator?
4. What does `iter()` do?
5. What does `next()` do?
6. What is a generator?
7. What does `yield` do?
8. What is the difference between `yield` and `return`?
9. What are the advantages of generators?
10. Generator vs list — when would you use each?
11. What is lazy evaluation?


## 8. Python Async / Await

1. What is synchronous programming?
2. What is asynchronous programming?
3. What is `async`?
4. What is `await`?
5. What is an event loop?
6. How does asynchronous programming work in Python?
7. What is the difference between `def` and `async def`?
8. What happens when Python encounters `await`?
9. What is concurrency?
10. What is parallelism?
11. What is the difference between concurrency and parallelism?
12. When should you use asynchronous programming?
13. Can you use synchronous code inside an `async` function?
14. What happens if you perform a blocking operation inside an async endpoint?
15. Why is async programming important in FastAPI?


# FastAPI

## 9. FastAPI Fundamentals

1. What is FastAPI?
2. Why would you use FastAPI?
3. What are the advantages of FastAPI?
4. How is FastAPI different from Flask?
5. How is FastAPI different from Django?
6. How do you create a FastAPI application?
7. What is a route/path operation?
8. What is `@app.get()`?
9. What is `@app.post()`?
10. What is `@app.put()`?
11. What is `@app.patch()`?
12. What is `@app.delete()`?
13. What is Uvicorn?
14. Why do we use Uvicorn with FastAPI?
15. What is ASGI?
16. What is the difference between ASGI and WSGI?
17. What is Swagger UI?
18. What is ReDoc?
19. How does FastAPI automatically generate API documentation?


## 10. HTTP and REST APIs

1. What is an API?
2. What is REST?
3. What makes an API RESTful?
4. What is CRUD?
5. What are HTTP methods?
6. What is GET used for?
7. What is POST used for?
8. What is PUT used for?
9. What is PATCH used for?
10. What is DELETE used for?
11. What is the difference between PUT and PATCH?
12. What is idempotency?
13. What is JSON?
14. What are HTTP headers?
15. What is an HTTP request?
16. What is an HTTP response?
17. What is an HTTP status code?
18. Explain status code `200`.
19. Explain status code `201`.
20. Explain status code `204`.
21. Explain status code `400`.
22. Explain status code `401`.
23. Explain status code `403`.
24. Explain status code `404`.
25. Explain status code `409`.
26. Explain status code `422`.
27. Explain status code `500`.


## 11. FastAPI Parameters

1. What is a path parameter?
2. What is a query parameter?
3. What is a request body?
4. What is the difference between path parameters and query parameters?
5. How do you define a path parameter in FastAPI?
6. How do you define a query parameter?
7. What is `Path()`?
8. What is `Query()`?
9. What is `Body()`?
10. What is `Header()`?
11. What is `Cookie()`?
12. How do you define optional parameters?
13. How do you define default values?
14. How does FastAPI validate parameters?
15. What happens when an invalid parameter is provided?


## 12. Pydantic

1. What is Pydantic?
2. Why does FastAPI use Pydantic?
3. What is `BaseModel`?
4. How do you create a Pydantic model?
5. What is data validation?
6. What happens when invalid data is sent to a Pydantic model?
7. What is serialization?
8. What is deserialization?
9. What are type annotations in Pydantic?
10. How do you define optional fields?
11. How do you define default values?
12. How do you validate a field?
13. What is a request model?
14. What is a response model?
15. What is `response_model` in FastAPI?
16. Why should you use separate request and response schemas?
17. How does Pydantic handle type conversion?
18. How would you validate an email address?
19. How would you validate a field with constraints?
20. What is the difference between a Pydantic model and a normal Python dictionary?


## 13. FastAPI CRUD

1. How would you build a CRUD API using FastAPI?
2. How would you create a resource?
3. How would you retrieve a resource?
4. How would you retrieve multiple resources?
5. How would you update a resource?
6. What is the difference between PUT and PATCH in a CRUD API?
7. How would you delete a resource?
8. How would you return `404 Not Found`?
9. How would you validate incoming data?
10. How would you prevent duplicate resources?
11. How would you implement pagination?
12. How would you implement filtering?
13. How would you implement sorting?
14. How would you implement search?


## 14. FastAPI Dependency Injection

1. What is dependency injection?
2. Why does FastAPI use dependency injection?
3. What is `Depends()`?
4. How do you create a dependency?
5. How can dependencies be shared between multiple endpoints?
6. How would you use dependency injection for database sessions?
7. How would you use dependency injection for authentication?
8. What are the benefits of dependency injection?
9. What is a dependency hierarchy?
10. Can dependencies depend on other dependencies?


## 15. FastAPI Authentication & Authorization

1. What is authentication?
2. What is authorization?
3. What is the difference between authentication and authorization?
4. What is JWT?
5. How does JWT authentication work?
6. What are access tokens?
7. What are refresh tokens?
8. What is OAuth2?
9. How would you protect a FastAPI endpoint?
10. How would you get the current authenticated user?
11. How should passwords be stored?
12. Why should passwords never be stored as plain text?
13. What is password hashing?
14. What is the difference between hashing and encryption?
15. What is role-based access control?
16. How would you restrict an endpoint to administrators?


## 16. FastAPI Database Integration

1. How do you connect FastAPI to a database?
2. What is an ORM?
3. What is SQLAlchemy?
4. Why use SQLAlchemy?
5. What is a database session?
6. What is a transaction?
7. What is a primary key?
8. What is a foreign key?
9. What is a database index?
10. What is connection pooling?
11. What is database migration?
12. What is Alembic?
13. SQL vs NoSQL — what is the difference?
14. PostgreSQL vs MongoDB — when would you use each?
15. How would you handle database errors?
16. What is the N+1 query problem?
17. How would you optimize a slow database query?
18. How would you implement database transactions in FastAPI?


## 17. FastAPI Project Architecture

1. How would you structure a production FastAPI project?
2. Why should you separate routers from business logic?
3. What is `APIRouter`?
4. Why should you use multiple routers?
5. What is the purpose of a `services` layer?
6. What is the purpose of a `models` directory?
7. What is the purpose of a `schemas` directory?
8. What is the difference between models and schemas?
9. Where would you put database configuration?
10. Where would you put authentication logic?
11. How would you manage environment variables?
12. How would you manage application configuration?
13. How would you avoid putting secrets directly in source code?


## 18. FastAPI Middleware and CORS

1. What is middleware?
2. How does middleware work?
3. What can middleware be used for?
4. What is CORS?
5. Why does CORS exist?
6. How do you configure CORS in FastAPI?
7. What is a preflight request?
8. What is the difference between middleware and dependencies?


## 19. FastAPI Error Handling

1. How does FastAPI handle exceptions?
2. What is `HTTPException`?
3. How do you return a custom error response?
4. How do you create a custom exception handler?
5. How would you handle validation errors?
6. What HTTP status code should be returned when a resource doesn't exist?
7. What HTTP status code should be returned when authentication fails?
8. How would you handle unexpected server errors?
9. Why shouldn't you expose internal errors to API clients?


## 20. FastAPI Testing

1. How do you test a FastAPI application?
2. What is pytest?
3. What is unit testing?
4. What is integration testing?
5. What is a pytest fixture?
6. How do you test a GET endpoint?
7. How do you test a POST endpoint?
8. How do you test invalid input?
9. How do you test authentication?
10. How would you mock an external API?
11. What is the difference between unit and integration tests?


# Backend / Software Engineering

## 21. API Design

1. How would you design a REST API for a task management application?
2. How would you design a user registration API?
3. How would you design a login API?
4. How would you design an API for uploading files?
5. How would you implement pagination?
6. How would you implement filtering?
7. How would you implement sorting?
8. How would you version an API?
9. What is API versioning?
10. How would you maintain backward compatibility?
11. How would you prevent duplicate requests?
12. What is rate limiting?
13. How would you implement rate limiting?
14. What is caching?
15. Where could you use caching in a backend application?


## 22. Security

1. What are common API security vulnerabilities?
2. What is SQL injection?
3. How do you prevent SQL injection?
4. What is XSS?
5. What is CSRF?
6. What is CORS?
7. What is authentication vs authorization?
8. How should passwords be stored?
9. How should API secrets be stored?
10. Why should secrets not be committed to Git?
11. What is HTTPS?
12. Why should APIs use HTTPS?
13. What is rate limiting and why is it important?


## 23. Production / Scenario-Based Questions

1. Your FastAPI endpoint is taking 5 seconds to respond. How would you investigate?
2. Your API suddenly starts returning HTTP 500 errors. What would you do?
3. Your database query is very slow. How would you debug it?
4. Your API works locally but fails in production. How would you investigate?
5. An external API that your service depends on is down. What should your application do?
6. Two users try to update the same resource at the same time. How would you handle it?
7. Your API is receiving a very large number of requests. How would you scale it?
8. How would you improve API performance?
9. How would you monitor a FastAPI application in production?
10. What metrics would you monitor?
11. What would you log?
12. How would you investigate high API latency?
13. How would you investigate high CPU usage?
14. How would you investigate high memory usage?
15. How would you deploy FastAPI to production?
16. How would Docker help with deploying FastAPI?
17. How would you configure environment variables in production?
18. How would you handle database migrations during deployment?
19. How would you perform a zero-downtime deployment?
20. What would you do if a deployment breaks production?


# High-Priority Questions for Associate-Level Interviews

## Python

1. List vs tuple vs set vs dictionary
2. Mutable vs immutable
3. `==` vs `is`
4. List comprehensions
5. `*args` and `**kwargs`
6. Function arguments
7. Scope
8. Exception handling
9. OOP and its four pillars
10. Class vs object
11. `self`
12. `__init__`
13. Inheritance
14. Method overriding
15. Decorators
16. Generators
17. Iterators
18. `yield`
19. Modules and packages
20. `async` / `await`

## FastAPI

1. What is FastAPI?
2. Why FastAPI?
3. FastAPI vs Flask/Django
4. GET/POST/PUT/PATCH/DELETE
5. Path vs query parameters
6. Request body
7. Pydantic
8. `BaseModel`
9. Request vs response models
10. `response_model`
11. HTTP status codes
12. CRUD
13. REST
14. `Depends()`
15. Dependency injection
16. Authentication vs authorization
17. JWT
18. Database integration
19. `APIRouter`
20. Middleware
21. CORS
22. Error handling
23. Testing
24. Project architecture
25. Async endpoints

## Backend Scenarios

1. Design a CRUD API.
2. Debug a slow API.
3. Debug a 500 error.
4. Handle database failures.
5. Handle external API failures.
6. Implement authentication.
7. Implement pagination.
8. Implement filtering/search.
9. Secure an API.
10. Deploy and monitor a FastAPI application.
