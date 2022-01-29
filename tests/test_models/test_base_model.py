#!/usr/bin/python3
'''Unit testing for BaseModel'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from datetime import datetime as time


class TestBase(unittest.TestCase):
    '''TestBase - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing basemodel'''
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, time)
        self.assertIsInstance(base.updated_at, time)
        self.assertNotIsInstance(base.id, uuid.UUID)
        self.assertIsInstance(base.id, str)

    def test_str(self):
        '''test_str - testing string rep'''
        base2 = BaseModel()
        string = "[{}] ({}) {}".format(type(base2).__name__,
                                       base2.id, base2.__dict__)
        self.assertEqual(str(base2), string)

    def test_save(self):
        '''test_save - testing save in BaseModel'''
        base3 = BaseModel()
        old_base = base3.updated_at
        base3.save()
        self.assertNotEqual(old_base, base3.updated_at)
