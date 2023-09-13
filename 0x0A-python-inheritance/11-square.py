#!/usr/bin/python3
"""Class Square Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Initialization
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Defines str()"""

        return "[Square] {}/{}".format(self.__size, self.__size)
