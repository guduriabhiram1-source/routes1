from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

@app.get("/users/{user_id}")
def get_users(user_id):
    return {"user_id": user_id}
