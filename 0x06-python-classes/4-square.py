#!/usr/bin/python3
""" Define a Square class """


class Square:
    """A square

    Attributes:
       __size (int): size of square
    """
    def __init__(self, size=0):
        """Square initialization

        Args:
           size (int): square size

        """
        self.__size = size

    @property
    def size(self):
        """int: size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Area of a square

        Returns:
           square area

        """
        return self.__size * self.__size
