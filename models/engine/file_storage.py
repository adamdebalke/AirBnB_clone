#!/usr/bin/python3
"""
Manages the storage of JSON strings for all class instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# list or dictionary for case validation (need to add pattern of dict)
a_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """Serializes and deserializes object instances to JSON files
    """

    """Variable names for file to create and store the objects in dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects
        """
        if cls:
            new_obj = {}
            for key, value in FileStorage.__objects.items():
                if type(value).__name__ == cls:
                    new_obj[key] = obj
                return new_obj
        else:
            return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        my_obj = {}
        for key, value in self.__objects.items():
            my_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                djo = json.load(f)
            for key in djo:
                self.__objects[key] = a_dict[djo[key]['__class__']](**djo[key])
        except:
            pass
