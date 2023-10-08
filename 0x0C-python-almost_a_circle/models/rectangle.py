#!/usr/bin/python3
"""Module rectangle"""

from models.base import Base


class Rectangle(Base):

    """Class rectangle
    Attributes:
        __width (int): Rectagle width

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for attribute width"""
        self.__width = value

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for attribute height"""

        self.__height = value

    @property
    def x(self):
        """getter for attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for attribute x"""

        self.__x = value

    @property
    def y(self):
        """getter for attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for attribute y"""

        self.__y = value
