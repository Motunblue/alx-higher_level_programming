#!/usr/bin//python3
def delete_at(my_list=[], idx=0):
    # Delete item at a specific location
    if 0 > idx > len(my_list):
        return my_list
    del my_list[idx]
    return my_list
