#!/usr/bin/python3
"""Post email"""


if __name__ == "__main__":
    """Post a email"""
    import urllib.request
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
