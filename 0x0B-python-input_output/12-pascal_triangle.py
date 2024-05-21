#!/usr/bin/python3
"""Module for defining a Pascal's Triangle function."""


def pascal_triangle(n):
    """function for representing a Pascal's Triangle of size n.

    Returns a list of lists of integers that represents the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        buffer = [1]
        for i in range(len(tri) - 1):
            buffer.append(tri[i] + tri[i + 1])
        buffer.append(1)
        triangle.append(buffer)
    return triangle
