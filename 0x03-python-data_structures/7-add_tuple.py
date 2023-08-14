#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    This function adds 2 tuples
    tuple_a: The first tuple
    tupple_b: The second tuple
    Return: addition of the two tuples
    """
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 < 2:
        tuple_a += (0,) * (2 - len1)
    if len2 < 2:
        tuple_b += (0,) * (2 - len2)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
