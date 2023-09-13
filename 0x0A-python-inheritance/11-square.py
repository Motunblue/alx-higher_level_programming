#!/usr/bin/python3
"""Class Square Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Initialization
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Defines str()"""

        return "[sqaure] {}/{}".format(self.__size, self.__size)
