#!/usr/bin/python3
"""Text indentaion"""

def text_indentation(text):
    """Print a text with two new line after .? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for c in text:
        if c == " " and flag:
            continue
        else:
            flag = 0
        print("{}".format(c), end="")
        if c in [".", "?", ":"]:
            print("\n")
            flag = 1
