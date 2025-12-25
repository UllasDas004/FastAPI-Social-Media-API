from app import schemas
from app.config import settings
from jose import jwt
import pytest


def test_root(client):
    response = client.get("/")
    print(response.status_code)
    assert response.json().get('message') == 'Welcome to my Social Media API'
    assert response.status_code == 200


def test_create_user(client):
    response = client.post("/users/",json={"email" : "ud2004@gmail.com","password" : "123456"})
    print(response.json())
    new_user = schemas.UserResponse(**response.json())
    assert new_user.email == "ud2004@gmail.com"
    assert response.status_code == 201


def test_login_user(client,test_user):
    response = client.post("/login",data={"username" : test_user['email'],"password" : test_user['password']})
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, key=settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_response.token_type == 'bearer'
    assert response.status_code == 200

@pytest.mark.parametrize("username, password, status_code",[
    ('wrongemail@gmail,com','123456',403),
    ('ud2004@gmail.com','wrong_password',403),
    ('wrongemail@gmail.com','wrong_password',403),
    (None,'123456',422),
    ('ud2004@gmail.com',None,422)
])
def test_incorrect_login(client,username,password,status_code):
    data = {}
    if username is not None:
        data['username'] = username
    if password is not None:
        data['password'] = password
    response = client.post("/login",data=data)
    assert response.status_code == status_code