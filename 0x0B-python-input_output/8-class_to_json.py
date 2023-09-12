#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """return dict discription for JSON serialization"""

    return obj.__dict__
