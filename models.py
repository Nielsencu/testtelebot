from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy_imageattach.entity import Image, image_attachment
from sq1alchemy.orm import relationship


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


class FoodImage(Base, Image):
    """Food Image model"""
    __tablename__ = 'food_image'

    foodset_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    foodset = relationship('FoodSet')

