#!/usr/bin/python3
"""Post email"""


if __name__ == "__main__":
    """Post a email"""
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
