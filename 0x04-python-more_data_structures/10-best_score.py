#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest_int = None
        biggest_val = None
        for value, integer in a_dictionary.items():
            if biggest_int is None or integer > biggest_int:
                biggest_int = integer
                biggest_val = value
        return biggest_val
