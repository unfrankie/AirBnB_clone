#!/usr/bin/python3
"""
module for FileStorage class
"""
import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serialize instances to a JSON file and deserialize JSON file to instances
    """

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as j:
            json.dump(obj_dict, j)


    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                obj_dict = json.load(f)
                for val in obj_dict.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            return
