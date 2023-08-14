#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    for x in matrix:
        print(" ".join("{:d}".format(y) for y in x))
