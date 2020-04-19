from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, ForeignKey, CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


engine = create_engine("postgresql://mike:mitdemBus357MAG@localhost/books")

base = declarative_base(engine)

class book(base):
    __tablename__ = "book"
    __table_args__ = {"autoload": True}