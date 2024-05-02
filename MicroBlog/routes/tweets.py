from fastapi import APIRouter
from database import db_session
from models import Tweet
from schemas import *

router = APIRouter()


@router.get("/tweets/{tweet_id}")
def get_tweet(tweet_id: int):
    tweets = db_session.query(Tweet).filter_by(id=tweet_id).first()
    return tweets

@router.post("/tweets/", status_code=201, response_model=TweetAddResponse)
def add_tweet(request: TweetAdd):
    tweet1 = Tweet(content=request.content, user_id=request.user_id)
    db_session.add(tweet1)
    db_session.commit()


@router.put("/tweets/{tweet_id}")
def change_tweet(tweet_id: int):
    tweets = db_session.query(Tweet).filter_by(id=tweet_id).first()

    return tweets


@router.delete("/tweets/{tweet_id}")
def delete_tweet(tweet_id: int):
    tweet = db_session.query(Tweet).filter_by(id=tweet_id).first()
    db_session.delete(tweet)
    db_session.commit()
