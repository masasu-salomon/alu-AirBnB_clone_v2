#!/usr/bin/python3
""" State Module for HBNB project """
import os

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenities of a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity', back_populates='amenities')

    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
        if not kwargs.get('name'):
            self.name = ""
