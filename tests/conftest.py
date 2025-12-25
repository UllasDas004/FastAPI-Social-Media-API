import sys
from pathlib import Path

# Add the workspace root to sys.path so app module can be imported
workspace_root = Path(__file__).parent.parent
sys.path.insert(0, str(workspace_root))

from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base
import pytest

url_object = URL.create(
    "postgresql+psycopg2",
    username = settings.database_username,
    password = settings.database_password,
    host = settings.database_hostname,
    database = settings.test_database_name,
    port = settings.database_port
)

engine = create_engine(url_object)

TestingSessionLocal = sessionmaker(bind = engine,
                                   autoflush=False,
                                   expire_on_commit=False)



@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind = engine) #clear the database
    Base.metadata.create_all(bind = engine) #create the database
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email" : "ud2004@gmail.com","password" : "123456"}
    response = client.post("/users/",json=user_data)
    assert response.status_code == 201
    new_user = response.json()
    new_user['password'] = '123456'
    return new_user

