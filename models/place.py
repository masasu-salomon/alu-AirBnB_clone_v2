#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, Integer, Float, DateTime
from models.base_model import BaseModel, Base
from datetime import datetime
from uuid import uuid4


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    PlaceBase = Base
else:
    PlaceBase = object


class Place(BaseModel, PlaceBase):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        id = Column(String(60), primary_key=True, nullable=False)
        city_id = Column(String(60), nullable=False)
        user_id = Column(String(60), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        created_at = Column(
            DateTime, default=datetime.now, nullable=False)
        updated_at = Column(
            DateTime, default=datetime.now, nullable=False)
        # amenity_ids is not a column,
        # it's a relationship in full implementation
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

    # Ensure amenity_ids is always available
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        super().__init__(
            *args,
            **kwargs
        )
