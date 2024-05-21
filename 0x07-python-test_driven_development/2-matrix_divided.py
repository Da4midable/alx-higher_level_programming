#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            new_row = [round(num / div, 2) for num in row]
            new_matrix.append(new_row)
    return new_matrix
