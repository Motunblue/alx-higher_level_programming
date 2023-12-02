#!/usr/bin/python3
"""GITHUB API"""


if __name__ == "__main__":
    """Takes github credential and display the user ID"""
    import requests
    import sys

    url = f"https://api.github.com/user"
    header = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {sys.argv[2]}",
        "X-GitHub-Api-Version": "2022-11-28",
        'User-Agent': sys.argv[2]
    }

    r = requests.get(url, headers=header)
    print(r.json()["id"])
