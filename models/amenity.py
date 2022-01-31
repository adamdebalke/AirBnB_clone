#!/usr/bin/python3
"""
This is the "amenity" module.
The amenity module supplies one class, Amenity, that\
inherits from BaseModel and holds the amenity information\
name.

For example,
Amenity()
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines a class Amenity.

    Attributes:
        name (str): the amenity name
    """
    name = ""
