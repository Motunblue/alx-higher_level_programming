#!/usr/bin/python3
"""Get script module"""


if __name__ == "__main__":
    """Send request to a url and display a value"""
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers
        print(head['X-Request-Id'])
