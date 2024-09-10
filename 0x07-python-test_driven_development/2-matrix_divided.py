#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number (div).
    
    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int/float): The number by which to divide the matrix elements.
    
    Returns:
        A new matrix where all elements have been divided by div and rounded
        to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
                   If rows in the matrix are not of the same size.
                   If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists containing integers or floats
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all elements in the matrix are either integers or floats
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows have the same length
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Ensure div is a number (int or float) and is not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round results to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
