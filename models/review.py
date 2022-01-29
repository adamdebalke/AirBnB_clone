#!/usr/bin/python3
"""Review class, inherits base"""


from models.base_model import BaseModel


class Review(BaseModel):
    """a class named Amenity template that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
