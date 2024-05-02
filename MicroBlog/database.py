from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import config
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(config.PG_DSN)

db_session = sessionmaker(bind=engine)()
