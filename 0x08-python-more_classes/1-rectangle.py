#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines a rectangle

    Attributes:
       __width (int): Rectangle width
       __height (int): Rectangle height

    """
    def __init__(self, width=0, height=0):
        """Initializing

        Args:
            width (int)
            height (int)

        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
