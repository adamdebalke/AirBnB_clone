#!/usr/bin/python3
'''Unit testing for Review'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime as time


class TestReview(unittest.TestCase):
    '''TestReview - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing Review'''
        rev = Review()
        self.assertIsInstance(rev, BaseModel)
        self.assertIsInstance(rev.created_at, time)
        self.assertIsInstance(rev.updated_at, time)
        self.assertNotIsInstance(rev.id, uuid.UUID)
        self.assertIsInstance(rev.id, str)

    def test_empty(self):
        '''test_empty - testing for an empty attributes'''
        rev = Review()
        self.assertIsInstance(rev.place_id, str)
        self.assertIsInstance(rev.text, str)
        self.assertIsInstance(rev.user_id, str)
