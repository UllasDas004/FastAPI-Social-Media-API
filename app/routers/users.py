from fastapi import FastAPI , Response , status , HTTPException , Depends,APIRouter
from .. import models, utils, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)


@router.post("/", status_code = status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user : schemas.UserCreate,db : Session = Depends(get_db)):
    email = user.email
    # check existing user in users table
    get_id_query = db.query(models.User).filter(models.User.email == email)
    if get_id_query.first() != None:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT,detail = f"User with email {email} already exists")
    
    # hash the password - user.password
    try:
        hashed_password = utils.hash(user.password)
    except Exception as e:
        # argon2 raises on very long inputs; return a clear client error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id : int,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"User with id {id} not found")
    return user

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_user(db : Session = Depends(get_db),
                current_user: models.User = Depends(oauth2.get_current_user)):
    get_id_query = db.query(models.User).filter(models.User.id == current_user.id)
    if get_id_query.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"User with id {id} not found")
    get_id_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)