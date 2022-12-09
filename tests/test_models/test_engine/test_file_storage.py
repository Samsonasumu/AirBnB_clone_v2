#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import models
import inspect
import time
import json
from unittest import mock
import os
from models.engine import file_storage
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models import storage
import pep8 as pycodestyle

Model = file_storage.FileStorage
FileStorage = file_storage.FileStorage
path1 = "models/engine/file_storage.py"
path2 = "tests/test_models/test_engine/test_file_storage.py"
module_doc = file_storage.FileStorage.__doc__

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "Review": Review,
           "City": City, "User": User, "State": State, "Place": Place}


class TestBaseModelDocs(unittest.TestCase):
    """Test to check behaviors"""

    @classmethod
    def setUpClass(self):
        """setting up tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8(self):
        """Testing pep8"""
        for path in [path1,
                     path2]:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test classes doctring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """test func dostrings"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


@unittest.skipIf(models.is_db == 'db', 'Not testing Dbstorage')
class Test_FileStorage(unittest.TestCase):
    """Testing proper behavrious"""
    def dic_tests(self):
        """Testing that FileStorage_objects returns properly"""
        f_storage = FileStorage()
        dic = f_storage.all()
        self.assertEqual(type(dic, dict))
        self.assertIs(dic, f_storage.__Filestorage.__objects)

    @unittest.skipIf(models.is_db == 'db', 'Not testing Dbstorage')
    def test_new_method(self):
        """testing that  new method saves on __objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.is_db == 'db', 'Not testing Dbstorage')
    def test_save(self):
        """Testing proper behaviour saving in file.json"""
        os.remove("file.json")
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
