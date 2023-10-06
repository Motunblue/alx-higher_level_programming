#!/usr/bin/python3
"""Base Class Module"""


class Base:
    """Base class
    Attributes:
    __nb_object (int): number of object
    """

    __nb_object = 0

    def __init__(self, id=None):
        """Initialization of base class
        Args:
           id (int): id of object
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
            
