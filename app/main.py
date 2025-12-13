from fastapi import FastAPI , Response , status , HTTPException , Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import posts, users, auth


models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# DB_HOST = 'localhost'
# DB_NAME = 'FastAPI Social Media DB'
# DB_USER = 'postgres'
# DB_PASSWORD = 'Ullasdas2004@'



# try:
#     conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD,cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was successful!!")
# except Exception as error:
#     print("Connecting to database failed")
#     print("Error: ", error)
#     time.sleep(4)
#     raise RuntimeError("Database connection failed")


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def get():
    return {"message" : "Welcome to my Social Media API"}

@app.get("/health")
def run_check():
    return {"message" : "My Social Media API is running fine"}

