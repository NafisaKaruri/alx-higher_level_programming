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

    def to_json(self):
        """
        retrieves a dictionary representatin of Student
        """
        return self.__dict__
