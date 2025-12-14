from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users, auth
from .config import settings

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def get():
    return {"message" : "Welcome to my Social Media API"}

@app.get("/health")
def run_check():
    return {"message" : "My Social Media API is running fine"}

