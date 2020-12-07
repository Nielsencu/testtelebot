from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tele_id = Column(Integer)
    tele_handle = Column(String(20))
    name = Column(String(100))
