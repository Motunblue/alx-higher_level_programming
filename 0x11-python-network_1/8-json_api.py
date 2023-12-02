#!/usr/bin/python3
"""JSON API"""


if __name__ == "__main__":
    """Send a post request"""
    import requests
    import sys

    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        res = r.json()
        if not res:
            print("No result")
        else:
            print("[{}] {}".format(res["id"], res["name"]))
    except ValueError:
        print("Not a valid JSON")
    