#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computs the square of a matrix"""
    return [[(x ** 2) for x in y] for y in matrix]
