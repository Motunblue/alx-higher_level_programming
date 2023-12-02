#!/usr/bin/python3
"""GITHUB API"""


if __name__ == "__main__":
    """List 10 commit"""
    import requests
    import sys

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    header = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        'User-Agent': "Motunble"
    }

    r = requests.get(url, headers=header)
    res = r.json()
    i = 0
    for comit in res:
        i += 1
        print("{}: {}".format(comit["sha"], comit["commit"]["author"]["name"]))
        if i == 10:
            break
