#!/usr/bin/python3
"""Module rectangle"""

from models.base import Base


class Rectangle(Base):

    """Class rectangle
    Attributes:
        width (int): Rectagle width

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for attribute height"""
                            
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for attribute x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for attribute y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for attribute y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
