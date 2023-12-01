#!/usr/bin/python3
"""Get script module"""


if __name__ == "__main__":
    """Fetch from url"""
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t - type: {content.__class__}")
        print(f"\t - content: {content}")
        print(f"\t - utf8 content: {content.decode('utf-8')}")
