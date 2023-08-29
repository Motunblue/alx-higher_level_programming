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
        if type(size) is int:
            if size >= 0:
                self.__size = size
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
