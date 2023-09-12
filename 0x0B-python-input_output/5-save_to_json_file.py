#!/usr/bin/python3
"""Save to json file Module"""
import json


def save_to_json_file(my_obj, filename):
    """Write to a file the JSON representation of an object"""

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
