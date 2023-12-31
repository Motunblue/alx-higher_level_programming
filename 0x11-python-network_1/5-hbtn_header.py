#!/usr/bin/python3
"""Get script module"""


if __name__ == "__main__":
    """Send request to a url and display a value"""
    import requests
    import sys

    r = requests.get(sys.argv[1])
    head = r.headers
    if "X-Request-Id" in head:
        print(head.get("X-Request-Id"))
