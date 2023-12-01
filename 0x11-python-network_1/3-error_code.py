#!/usr/bin/python3
"""Get script module"""


if __name__ == "__main__":
    """Send request to a url and display a value"""
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
