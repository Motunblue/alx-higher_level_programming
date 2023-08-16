#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = set()
    for i in my_list:
        uniques.add(i)
    return sum(uniques)
