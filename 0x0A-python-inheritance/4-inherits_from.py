#!/usr/bin/python3
"""Module for function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if an object instance inherits from a class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
