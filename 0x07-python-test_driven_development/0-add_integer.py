#!/usr/bin/python3
"""
    Addition Module
"""


def add_integer(a, b=98):
    """Adds 2 numbers

    Args:
        a (int): First number
        b (int): Second number

    Return: result
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
