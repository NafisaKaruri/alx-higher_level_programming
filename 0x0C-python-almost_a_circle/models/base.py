#!/usr/bin/python3
"""Base class"""


from json import dumps, loads
import csv


class Base:
    """The base of our hierarchy"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiates the attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictioinaries"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf_8') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation of json_string"""
        if not json_string or json_string is None:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            created = Rectangle(1, 1)
        elif cls is Square:
            created = Square(1)
        else:
            created = None
        created.update(**dictionary)
        return created

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        from os import path
        file = '{}.json'.format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, 'r', encoding='utf_8')as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
