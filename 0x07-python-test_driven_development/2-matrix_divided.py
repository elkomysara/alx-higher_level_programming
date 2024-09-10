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
    # Verify matrix is a list of lists containing only integers or floats
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or 
        not all(isinstance(ele, (int, float)) for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Verify that all rows in the matrix have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Verify div is a number (int/float) and handle division by zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
