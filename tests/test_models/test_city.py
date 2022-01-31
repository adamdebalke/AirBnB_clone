#!/usr/bin/python3
"""
The ``test_city`` module
==============================
Using ``test_city``
-------------------------
This is a test_city unittest file to test the city module.
"""
import unittest
from models.city import City
import datetime
import json
import os


class TestCity(unittest.TestCase):
    """Defines a class TestCity.
    Test functionality of the city module.
    """
    a = [City, "City"]

    def tearDown(self):
        """Remove storage file after test ends."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_create(self):
        """Test if the created class is same type."""
        obj = TestCity.a[0]()
        self.assertIsInstance(obj, TestCity.a[0])

    def test_id(self):
        """Tests if id is of type str."""
        obj = TestCity.a[0]()
        self.assertEqual(type(obj.id), str)

    def test_time(self):
        """Tests if the created and updated date is equal at creation."""
        obj = TestCity.a[0]()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_created_at(self):
        """Tests if created_at is of type datetime."""
        obj = TestCity.a[0]()
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test is updated_at is of type datetime."""
        obj = TestCity.a[0]()
        self.assertEqual(type(obj.updated_at), datetime.datetime)

    def test_str(self):
        """Tests if the string representation is correct format."""
        obj = TestCity.a[0]()
        self.assertEqual(str(obj), '[{}] ({}) {}'.format(TestCity.a[1],
                         obj.id,
                         obj.__dict__))

    def test_save(self):
        """Tests if the saved attributes are the same as the original."""
        obj = TestCity.a[0]()
        obj.save()
        key = TestCity.a[1] + "." + obj.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], obj.to_dict())
