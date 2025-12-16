from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal

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

class PostBase(BaseModel): #base model for structure of post in the requests
    title : str
    content : str
    published : bool = True



class PostResponse(PostBase):  #the post model for the responses that this API sends
    id : int
    created_at : datetime
    owner : UserResponse

class PostOut(BaseModel):
    Post: PostResponse
    votes: int
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id : int
    dir : Literal[0,1]