#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False, default="")
    password = Column(String(128), nullable=False, default="")
    first_name = Column(String(128), nullable=True, default="")
    last_name = Column(String(128), nullable=True, default="")
    places = relationship(
        'Place',
        backref='user',
        cascade='all, delete-orphan')
    reviews = relationship(
        'Review',
        backref='user',
        cascade='all, delete-orphan')
