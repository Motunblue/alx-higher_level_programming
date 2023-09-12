#!/usr/bin/python3
"""Append Write Module"""


def append_write(filename="", text=""):
    """Appends a string to a textfile"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
