from config import SQL_ENGINE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tele_id = Column(Integer)
    tele_handle = Column(String(20))
    name = Column(String(100))


class FoodSet(Base):
    __tablename__ = 'food_set'

    id= Column(Integer, primary_key=True)
    settype= Column(String(100))
    breakfastbool = Column(Boolean)
    picture = image_attachment('FoodImage')
    rating = Column(Integer, default=0)
    total_rater = Column(Integer, default=0)
    last_rated_at = Column(String(100), default = '')
    child = relationship("FoodImage", uselist=False, back_populates="parent")


class FoodImage(Base, Image):
    """Food Image model"""
    __tablename__ = 'food_image'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('food_set.id'))
    parent = relationship("FoodSet", back_populates="child")

Base.metadata.create_all(bind=SQL_ENGINE)


