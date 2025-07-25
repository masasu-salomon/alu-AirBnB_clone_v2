#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os
import unittest


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "FileStorage tests skipped for DBStorage")
class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        if new.city_id is None:
            new.city_id = ""
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if new.user_id is None:
            new.user_id = ""
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if new.name is None:
            new.name = ""
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        if new.description is None:
            new.description = ""
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        if new.number_rooms is None:
            new.number_rooms = 0
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        if new.number_bathrooms is None:
            new.number_bathrooms = 0
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        if new.max_guest is None:
            new.max_guest = 0
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        if new.price_by_night is None:
            new.price_by_night = 0
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        if new.latitude is None:
            new.latitude = 0.0
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        if new.longitude is None:
            new.longitude = 0.0
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
