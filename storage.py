from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, ForeignKey, CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *
import json

engine = create_engine("postgresql://mike:mitdemBus357MAG@localhost/books")
base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def GetTestDatabase():
    data = session.query(book).all()

    return None