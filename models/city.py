#!/usr/bin/python3
"""
This is the "city" module.
The city module supplies one class, City, that\
inherits from BaseModel and holds the city information\
name and state_id

For example,
City()
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a class City.

    Attributes:
        name (str): the city name
        state_id (str): the state id
    """
    state_id = ""
    name = ""
