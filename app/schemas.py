from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel): #base model for structure of post in the requests
    title : str
    content : str
    published : bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):  #the post model for the responses that this API sends
    id : int
    created_at : datetime
    owner_id : int

class UserCreate(BaseModel):
    email : EmailStr
    password : str


class UserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime


class UserLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None