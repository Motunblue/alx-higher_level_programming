#!/usr/bin/python3
"""Student class Module
"""


class Student:
    """Class of student

    Attributes:
        first_name (str):
        last_name (str):
        age (int):

    """

    def __init__(self, first_name, last_name, age):
        """Initializer

        Args:

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrievees a dictionary representation of Student"""

        return self.__dict__
