#!/usr/bin/python3
'''Unit testing for Place'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime as time


class TestPlace(unittest.TestCase):
    '''TestPlace - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing Place'''
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place.created_at, time)
        self.assertIsInstance(place.updated_at, time)
        self.assertNotIsInstance(place.id, uuid.UUID)
        self.assertIsInstance(place.id, str)

    def test_empty(self):
        '''test_empty - testing for an empty attributes'''
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
