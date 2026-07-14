from fastapi import FastAPI
from repository import PostgresRepository

app = FastAPI()

repo = PostgresRepository()


@app.get("/")
def home():
    return {"message": "Backend is running!"}


@app.post("/add/{text}")
def add_message(text: str):
    repo.add_message(text)
    return {"added": text}


@app.get("/messages")
def get_messages():
    return repo.get_messages()