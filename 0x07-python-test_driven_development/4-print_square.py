#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """Print a square with character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print("\n".join(["#" * size for i in range(size)]))
