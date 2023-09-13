#!/usr/bin/python3
"""Pascal triangle Module
"""


def pascal_triangle(n):
    """Returns list of integers representing Pascal triangle of n
    """

    mylist = [[1]]
    if n <= 0:
        return []

    for i in range(n - 1):
        tmp = [1]
        for j in range(i):
            tmp.append(mylist[-1][j] + mylist[-1][j + 1])
        tmp.append(1)
        mylist.append(tmp)

    return mylist
