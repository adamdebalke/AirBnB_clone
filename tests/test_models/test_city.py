#!/usr/bin/python3
'''Unit testing for City'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.city import City
from datetime import datetime as time


class TestCity(unittest.TestCase):
    '''TestCity - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing City'''
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.created_at, time)
        self.assertIsInstance(city.updated_at, time)
        self.assertNotIsInstance(city.id, uuid.UUID)
        self.assertIsInstance(city.id, str)

    def test_empty(self):
        '''test_empty - testing for an empty attributes'''
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
