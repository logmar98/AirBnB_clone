#!/usr/bin/python3
"""
FileStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    This class is responsible for storing & retrieving objects in a JSON file.
    It provides methods for managing objects, saving them to the file,
    and reloading them from the file.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the FileStorage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the FileStorage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves all objects in the FileStorage to the JSON file.
        """
        ser_obj = {}
        for key, val in FileStorage.__objects.items():
            ser_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as file:
            json.dump(ser_obj, file)

    def reload(self):
        """
        Reloads objects from the JSON file into the FileStorage.
        """
        class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                deserialized_file = json.load(file)
                for val in deserialized_file.values():
                    clss_name = val["__class__"]
                    del val["__class__"]
                    obj_class = class_map.get(clss_name, BaseModel)
                    obj = obj_class(**val)
                    self.new(obj)
        except FileNotFoundError:
            return
