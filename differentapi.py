from fastapi import FastAPI

app = FastAPI()

# GET
@app.get("/")
def get_data():
    return {"message": "GET API"}

# POST
@app.post("/")
def post_data():
    return {"message": "POST API"}

# PUT
@app.put("/")
def put_data():
    return {"message": "PUT API"}

# DELETE
@app.delete("/")
def delete_data():
    return {"message": "DELETE API"}
