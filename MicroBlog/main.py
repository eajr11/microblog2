from fastapi import FastAPI
from routes import users, tweets, subscriptions

app = FastAPI()

app.include_router(users.router)
app.include_router(tweets.router)
app.include_router(subscriptions.router)
