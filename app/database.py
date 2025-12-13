from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url_object = URL.create(
    "postgresql+psycopg2",
    username = "postgres",
    password = "Ullasdas2004@",
    host = "localhost",
    database = "FastAPI Social Media DB",
    port = 5432
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
