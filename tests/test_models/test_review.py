#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os
import unittest
import sys


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "FileStorage tests skipped for DBStorage")
class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        if new.place_id is None:
            new.place_id = ""
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if new.user_id is None:
            new.user_id = ""
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        if new.text is None:
            new.text = ""
        self.assertEqual(type(new.text), str)
