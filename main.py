from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Conda API"}

@app.get("/users")
def get_users():
    return {"users": ["John", "Alex"]}