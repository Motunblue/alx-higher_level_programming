#!/usr/bin/python3
"""Write_file Module"""


def write_file(filename="", text=""):
    """Writes a string to a textfile"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
