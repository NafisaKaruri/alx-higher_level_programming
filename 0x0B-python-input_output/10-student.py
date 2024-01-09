#!/usr/bin/python3
"""defines Student class"""


class Student:
    """
    Defines a student by:
        first_name, last_name, age
    have an instantiation method and to_json method
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes the Student info
        arguments:
            first_name (str): the Student first_name
            last_name(str): the Student last_name
            age (int): the Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representatin of Student
        arguments:
            attrs (list): list of strings or None
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic
