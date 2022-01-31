#!/usr/bin/python3
"""
This is the "file_storage" module.
The file_storage module supplies one class, FileStorage, that\
that serializes instances to a JSON file and deserializes JSON\
file to instances.

For example,
FileStorage()
"""
import json


class FileStorage:
    """Defines a class FileStorage.

    Attributes:
        __file_path (str): id of the class
        __objects (dictionary): created date of the class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({obj_key: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            save_r = {}
            save_r.update(FileStorage.__objects)
            for key, value in save_r.items():
                save_r.update({key: value.to_dict()})
            json.dump(save_r, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON\
        file (__file_path) exists.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        all_classes = {'BaseModel': BaseModel, 'User': User,
                       'State': State, 'City': City,
                       'Amenity': Amenity, 'Place': Place,
                       'Review': Review}
        try:
            with open(FileStorage.__file_path, "r") as f:
                open_r = json.load(f)
                for key, value in open_r.items():
                    FileStorage.__objects.update(
                        {key: all_classes[value['__class__']](**value)})
        except Exception:
            pass
