#!/usr/bin/python3
"""Read file Module"""


def read_file(filename=""):
    """Read from a file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
