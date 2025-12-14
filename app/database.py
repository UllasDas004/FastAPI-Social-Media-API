from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

url_object = URL.create(
    "postgresql+psycopg2",
    username = settings.database_username,
    password = settings.database_password,
    host = settings.database_hostname,
    database = settings.database_name,
    port = settings.database_port
)

engine = create_engine(url_object)

SessionLocal = sessionmaker(bind = engine,autoflush=False,expire_on_commit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# try:
#     conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD,cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was successful!!")
# except Exception as error:
#     print("Connecting to database failed")
#     print("Error: ", error)
#     time.sleep(4)
#     raise RuntimeError("Database connection failed")