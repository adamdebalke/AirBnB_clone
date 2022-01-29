#!/usr/bin/python3
"""city class, inherits base"""


from models.base_model import BaseModel


class City(BaseModel):
    """a class named User template that inherits from BaseModel"""

    state_id = ""
    name = ""
