#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    state_id = Column(
        String(60), ForeignKey("states.id"), nullable=False
    )
    name = Column(
        String(128), nullable=False
    )
    places = relationship("Place", backref="cities", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialize City"""
        super().__init__(*args, **kwargs)
        if not kwargs.get('state_id'):
            self.state_id = ""
        if not kwargs.get('name'):
            self.name = ""
