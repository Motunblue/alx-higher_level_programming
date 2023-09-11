#!/usr/bin/python3
"""Lookup Module"""


def lookup(obj):
    """Returns list of available attribules

    Args:
        obj (object): Object whose attributes to return

    """

    return dir(obj)
