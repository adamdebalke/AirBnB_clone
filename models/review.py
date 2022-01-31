#!/usr/bin/python3
"""
This is the "review" module.
The review module supplies one class, Review, that\
inherits from BaseModel and holds user information\
such as place_id, user_id and text.

For example,
Review()
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a class Review.

    Attributes:
        place_id (str): id of the place
        user_id (str): id of the user
        text (str): the review text
    """
    place_id = ""
    user_id = ""
    text = ""
