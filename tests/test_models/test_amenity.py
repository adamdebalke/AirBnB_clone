#!/usr/bin/python3
'''Unit testing for Amenity'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime as time


class TestAmenity(unittest.TestCase):
    '''TestAmenity - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing amenity'''
        amen = Amenity()
        self.assertIsInstance(amen, BaseModel)
        self.assertIsInstance(amen.created_at, time)
        self.assertIsInstance(amen.updated_at, time)
        self.assertNotIsInstance(amen.id, uuid.UUID)
        self.assertIsInstance(amen.id, str)

    def test_str(self):
        '''test_str - testing for an empty string'''
        amen = Amenity()
        self.assertIsInstance(amen.name, str)
