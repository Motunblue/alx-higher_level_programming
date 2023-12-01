#!/usr/bin/python3
"""Get script module"""


if __name__ == "__main__":
    """Fetch from url"""
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    content = r.text
    print("Body response:")
    print(f"\t- type: {content.__class__}")
    print(f"\t- content: {content}")
