#!/usr/bin/python3
""" Define a Square class """


class Square:
    """A square

    Attributes:
       __size (int): size of square
       __position (tuple): position of square

    """
    def __init__(self, size=0, position=(0, 0)):
        """Square initialization

        Args:
           size (int): square size
           position (tuple): square position

        """
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def size(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) and num > 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Area of a square

        Returns:
           square area

        """
        return self.__size * self.__size

    def my_print(self):
        """print a square"""

        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
