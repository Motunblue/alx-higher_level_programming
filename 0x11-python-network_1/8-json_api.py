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
    dic = eval(r.text)
    if not isinstance(dic, dict):
        print("Not a valid JSON")
    elif not dic:
        print("No result")
    else:
        print("[{}] {}".format(dic["id"], dic["name"]))
