#!/usr/bin/python3
def no_c(my_string):
    tab = {ord('C'): None, ord('c'): None}
    my_string2 = my_string.translate(tab)
    return(my_string2)
