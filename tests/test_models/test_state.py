#!/usr/bin/python3
'''Unit testing for State'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.state import State
from datetime import datetime as time


class TestState(unittest.TestCase):
    '''TestState - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing State'''
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.created_at, time)
        self.assertIsInstance(state.updated_at, time)
        self.assertNotIsInstance(state.id, uuid.UUID)
        self.assertIsInstance(state.id, str)

    def test_empty(self):
        '''test_empty - testing for an empty attributes'''
        state = State()
        self.assertIsInstance(state.name, str)
