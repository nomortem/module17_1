from fastapi import FastAPI
from app.backend.db import create_db
from app.models import User, Task

app = FastAPI()

# Создание таблиц при старте приложения
@app.on_event("startup")
def startup():
    create_db()
    print("Database tables created")

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API!"}