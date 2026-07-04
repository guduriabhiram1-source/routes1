from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "this home page"}
@app.get("/about")
def about():
    return {"message": "this about page"}
@app.get("/users")
def users():
    return {"message": {"abhi", "sai", "punni"}}