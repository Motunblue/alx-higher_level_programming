#!/usr/bin/python3
""" My list module"""


class MyList(list):
    """My list class"""

    def __init__(self):
        """Initialize object"""

        super().__init__()

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
