# FastAPI Routing

## What is a Route?

A **route** is a URL path that your FastAPI application listens to. When a user sends a request to that URL, FastAPI executes the corresponding Python function and returns a response.

Think of a route as:

* **URL (Path)** → The address users visit.
* **Function** → The code that handles the request.
* **Response** → The data returned to the user.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}
```

When you open:

```
http://127.0.0.1:8000/
```

FastAPI returns:

```json
{
  "message": "Welcome to FastAPI!"
}
```

---

## Route Decorators

FastAPI uses decorators to define routes.

| Decorator       | HTTP Method | Purpose                      |
| --------------- | ----------- | ---------------------------- |
| `@app.get()`    | GET         | Retrieve data                |
| `@app.post()`   | POST        | Create new data              |
| `@app.put()`    | PUT         | Replace existing data        |
| `@app.patch()`  | PATCH       | Update part of existing data |
| `@app.delete()` | DELETE      | Delete data                  |

Example:

```python
@app.get("/users")
def get_users():
    return {"users": []}

@app.post("/users")
def create_user():
    return {"message": "User created"}
```

---

## Route Path

A route path is the part of the URL after the domain.

Example:

```python
@app.get("/about")
def about():
    return {"message": "About Page"}
```

URL:

```
http://127.0.0.1:8000/about
```

---

## Path Parameters

Path parameters allow you to pass values directly in the URL.

Example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Request:

```
GET /users/10
```

Response:

```json
{
  "user_id": 10
}
```

---

## Query Parameters

Query parameters come after the `?` in the URL.

Example:

```python
@app.get("/search")
def search(name: str):
    return {"name": name}
```

Request:

```
GET /search?name=Abhi
```

Response:

```json
{
  "name": "Abhi"
}
```

---

## Multiple Routes

A FastAPI application can contain many routes.

```python
@app.get("/")
def home():
    return {"message": "Home"}

@app.get("/about")
def about():
    return {"message": "About"}

@app.get("/contact")
def contact():
    return {"message": "Contact"}
```

---

## Route with Multiple Parameters

```python
@app.get("/students/{student_id}")
def get_student(student_id: int, name: str):
    return {
        "student_id": student_id,
        "name": name
    }
```

Request:

```
GET /students/1?name=Abhi
```

Response:

```json
{
  "student_id": 1,
  "name": "Abhi"
}
```

---

## How FastAPI Matches Routes

When a request arrives:

1. FastAPI reads the requested URL.
2. It finds the matching route.
3. It executes the associated function.
4. The function returns a response.
5. FastAPI converts the response into JSON.

Example:

```
Request
   │
   ▼
URL → /users/5
   │
   ▼
Matching Route
@app.get("/users/{user_id}")
   │
   ▼
Python Function Executes
   │
   ▼
JSON Response Returned
```

---

## Testing Routes

Start the server:

```bash
fastapi dev api.py
```

or

```bash
uvicorn api:app --reload
```

Open your browser:

* API Root:

  ```
  http://127.0.0.1:8000/
  ```

* Interactive Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc Documentation:

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## Best Practices

* Use meaningful route names.
* Keep route functions simple.
* Use nouns in URLs (e.g., `/users`, `/products`).
* Use the correct HTTP method for each operation.
* Group related routes together as your project grows.

---

## Summary

* A **route** connects a URL to a Python function.
* FastAPI uses decorators like `@app.get()` and `@app.post()` to define routes.
* Routes can accept **path parameters** and **query parameters**.
* FastAPI automatically generates interactive API documentation at `/docs`.
* Every API endpoint in a FastAPI application is defined as a route.
# FastAPI CRUD API

A simple FastAPI project demonstrating the basic CRUD (Create, Read, Update, Delete) operations using GET, POST, PUT, and DELETE methods.

## API Methods

### GET
- Retrieves data from the server.
- Does not modify any data.
- Example:
  ```
  GET /students
  ```

### POST
- Creates a new resource or adds new data.
- Example:
  ```
  POST /students
  ```
- Sample Request Body:
  ```json
  {
    "id": 1,
    "name": "Abhi",
    "age": 22
  }
  ```

### PUT
- Updates an existing resource.
- Example:
  ```
  PUT /students/1
  ```
- Sample Request Body:
  ```json
  {
    "id": 1,
    "name": "Abhi Ram",
    "age": 23
  }
  ```

### DELETE
- Deletes an existing resource.
- Example:
  ```
  DELETE /students/1
  ```

## Run the Project

Install the required packages:

```bash
pip install fastapi uvicorn
```

Start the server:

```bash
uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all the API endpoints interactively.
