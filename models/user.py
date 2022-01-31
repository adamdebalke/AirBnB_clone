#!/usr/bin/python3
"""
This is the "user" module.
The user module supplies one class, User, that\
inherits from BaseModel and holds user information\
such as email, password, first name and last name.

For example,
User()
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a class User.

    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
