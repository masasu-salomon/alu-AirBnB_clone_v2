#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
import unittest


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "FileStorage tests skipped for DBStorage")
class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        if new.first_name is None:
            new.first_name = ""
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        if new.last_name is None:
            new.last_name = ""
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        if new.email is None:
            new.email = ""
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        if new.password is None:
            new.password = ""
        self.assertEqual(type(new.password), str)
