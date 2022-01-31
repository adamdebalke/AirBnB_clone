#!/usr/bin/python3
"""
This is the "state" module.
The state module supplies one class, State, that\
inherits from BaseModel and holds the state information\
name.

For example,
State()
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a class State.

    Attributes:
        name (str): the state name
    """
    name = ""
