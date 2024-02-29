#!/usr/bin/python3
"""module finds the peak of an array of integers"""


def find_peak(list_of_integers):
    """
    finds a peak element in a list of unsorted integers

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        the peak element, or None if list is empty
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
