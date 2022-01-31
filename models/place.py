#!/usr/bin/python3
"""
This is the "place" module.
The place module supplies one class, Place, that\
inherits from BaseModel and holds the state informations\
listed below in the attributes.

For example,
Place()
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a class Place.

    Attributes:
        city_id (str): the city id
        user_id (str): the user id
        name (str): the state name
        description (str): description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum of amount guest
        price_by_night (int): price at night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list): list of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
