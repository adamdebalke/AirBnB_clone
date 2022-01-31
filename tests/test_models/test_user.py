#!/usr/bin/python3
"""
The ``test_user`` module
==============================
Using ``test_user``
-------------------------
This is a test_user unittest file to test the user module.
"""
import unittest
from models.user import User
import datetime
import json
import os


class TestUser(unittest.TestCase):
    """Defines a class TestUser.
    Test functionality of the user module.
    """
    a = [User, "User"]

    def tearDown(self):
        """Remove storage file after test ends."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_create(self):
        """Test if the created class is same type."""
        obj = TestUser.a[0]()
        self.assertIsInstance(obj, TestUser.a[0])

    def test_id(self):
        """Tests if id is of type str."""
        obj = TestUser.a[0]()
        self.assertEqual(type(obj.id), str)

    def test_time(self):
        """Tests if the created and updated date is equal at creation."""
        obj = TestUser.a[0]()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_created_at(self):
        """Tests if created_at is of type datetime."""
        obj = TestUser.a[0]()
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test is updated_at is of type datetime."""
        obj = TestUser.a[0]()
        self.assertEqual(type(obj.updated_at), datetime.datetime)

    def test_str(self):
        """Tests if the string representation is correct format."""
        obj = TestUser.a[0]()
        self.assertEqual(str(obj), '[{}] ({}) {}'.format(TestUser.a[1],
                         obj.id,
                         obj.__dict__))

    def test_save(self):
        """Tests if the saved attributes are the same as the original."""
        obj = TestUser.a[0]()
        obj.save()
        key = TestUser.a[1] + "." + obj.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], obj.to_dict())
