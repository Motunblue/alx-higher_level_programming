#!/usr/bin/python3
"""Class Rectangle Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Initialization
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """Defines str()"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
