#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Return a tuple with the length and its first character
    sentence: Input list
    """
    if len(sentence) == 0:
        res = (0, None)
    else:
        res = (len(sentence), sentence[0])
    return (res)
