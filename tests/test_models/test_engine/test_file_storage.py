#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from models.base_model import BaseModel
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "FileStorage tests skipped for DBStorage")
class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        obj = None
        for o in storage.all().values():
            obj = o
        self.assertIsNotNone(obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        if loaded is not None:
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])
        else:
            self.fail("No object loaded from storage after reload.")

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        try:
            storage.reload()
        except Exception:
            self.fail("reload() raised an exception with empty file")

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        new.save()
        temp = None
        for key in storage.all().keys():
            temp = key
        if temp is not None:
            self.assertTrue(temp.startswith('BaseModel.'))
        else:
            self.fail("No key found in storage after creating BaseModel.")

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
