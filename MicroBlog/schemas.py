from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    id: int
    username: str

class UserResponse(UserBase):
    email: str

class UserCreate(UserBase):
    email: str
    username: str
    password: str

class UserCreateResponse(UserBase):
    email: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class TweetBase(BaseModel):
    id: int



class TweetAdd(TweetBase):
    content: str
    user_id: int


class TweetAddResponse(TweetBase):
    content: str
    user_id: str
    created_at: datetime


class Tweet(TweetBase):
    content: str
    user_id: str

    class Config:
        orm_mode = True


class SubscriptionBase(BaseModel):
    follower_user_id: int


class SubscriptionCreate(SubscriptionBase):
    follower_user_id: str
    followed_user_id: str
    created_at: datetime


class Subscription(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True
