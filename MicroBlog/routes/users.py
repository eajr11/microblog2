from fastapi import APIRouter
import typing
from database import db_session
from schemas import *
from models import User


router = APIRouter()


@router.get("/users/", status_code=200, response_model=typing.List[UserResponse])
def get_users():
    users = db_session.query(User).all()
    return users


@router.get("/users/{user_id}")
def get_user(user_id: int):
    users = db_session.query(User).filter_by(id=user_id).first()
    return users

@router.post("/users/", status_code=201, response_model=UserCreateResponse)
def create_user(request: UserCreate):
    user1 = User(email=request.email, username=request.username, password=request.password)
    db_session.add(user1)
    db_session.commit()
    return UserCreateResponse(id=user1.id, username=user1.username, email=user1.email)

@router.post("/login/")
def login_user():
    pass
