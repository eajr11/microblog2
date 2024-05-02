from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    tweets = relationship("Tweet", back_populates="user")
    followers = relationship("Follower", back_populates="followed_user", foreign_keys="[Follower.followed_user_id]")
    following = relationship("Follower", back_populates="follower_user", foreign_keys="[Follower.follower_user_id]")


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="tweets")


class Follower(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    follower_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    followed_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    follower_user = relationship("User", foreign_keys=[follower_user_id])
    followed_user = relationship("User", foreign_keys=[followed_user_id])

