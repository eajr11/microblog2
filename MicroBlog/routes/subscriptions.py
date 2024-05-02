from fastapi import APIRouter
from database import db_session
from models import Follower
from schemas import *

router = APIRouter()

@router.post("/subscriptions/")
def add_sub():
    sub = session.query(Follower).filter_by(id='Alice').first()
    session.delete(user)
    session.commit()

@router.delete("/subscriptions/{user_id}")
def delete_sub():
    sub = session.query(Follower).filter_by(id='Alice').first()
    session.delete(user)
    session.commit()