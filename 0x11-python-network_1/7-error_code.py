#!/usr/bin/python3
"""Get script module"""


if __name__ == "__main__":
    """Send request to a url and display a value"""
    import requests
    import sys

    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code:", e.response.status_code)
