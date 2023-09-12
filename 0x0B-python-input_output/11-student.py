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

        if type(attrs) == list and all(isinstance(a, str) for a in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of a the student"""

        for k in json:
            if hasattr(self, k):
                setattr(self, k, json[k])
