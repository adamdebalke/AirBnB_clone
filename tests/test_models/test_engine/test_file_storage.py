#!/usr/bin/python3
"""
The ``test_file_storage`` module
==============================

Using ``test_file_storage``
-------------------------

This is a test_file_storage unittest file to test the file_storage module.

"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Defines a class TestFileStorage.

    Test functionality of the file_storage module.
    """
    def tearDown(self):
        """Remove storage file after test ends."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_storage_type(self):
        """Test if the dictionary in storage is actually dict."""
        obj = BaseModel()
        self.assertTrue(type(storage.all()), dict)

    def test_creation(self):
        """Test if the created object is stored."""
        obj = BaseModel()
        self.assertTrue(obj in storage.all().values())

    def test_storage_object(self):
        """Test if the stored object is the actual object."""
        obj = BaseModel()
        all_objs = storage.all()
        self.assertIsInstance(list(all_objs.values())[0], BaseModel)
