#!/usr/bin/python3
"""Find peak module"""


def find_max(arr, low, high):
    """Find the max number in the array"""

    if low == high:
        return arr[low]
    else:
        mid = (low + high) // 2
        max_left = find_max(arr, low, mid)
        max_right = find_max(arr, mid + 1, high)
        return max(max_left, max_right)


def find_peak(list_of_integers):
    """Find the peak value in a unsorted list"""
    if list_of_integers is None or list_of_integers == []:
        return None

    return find_max(list_of_integers, 0, len(list_of_integers) - 1)
