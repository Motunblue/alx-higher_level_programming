#!/usr/bin/python3
"""Module defines matrix_divided"""


def matrix_divided(matrix, div):
    """
    Divides all element of a matrix
    """

    if not isinstance(matrix, list) or not all(isinstance(j, list)
                                               for j in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    column = len(matrix[0])
    for m in matrix:
        if len(m) != column:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row = len(matrix)
    new_matrix = [[0 for i in range(column)] for j in range(row)]

    for i in range(row):
        for j in range(column):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return (new_matrix)
