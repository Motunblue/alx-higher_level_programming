#!/usr/bin/python3
"""From json string module"""
import json


def from_json_string(my_str):
    """return the python representation of a JSON string"""

    return json.loads(my_str)
