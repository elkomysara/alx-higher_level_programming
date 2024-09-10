#!/usr/bin/python3
"""
This module defines the matrix multiplication function.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b and returns the result.
    
    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.
    
    Returns:
        list of lists: A new matrix that is the result of multiplying m_a by m_b.
    
    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats, or if the rows are of different sizes.
        ValueError: If m_a or m_b is empty or can't be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Check if all elements in m_a and m_b are integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    
    # Check if each row in m_a and m_b has the same size
    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Check if matrices can be multiplied (number of columns in m_a == number of rows in m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Matrix multiplication
    result_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            row.append(round(sum_val, 2))  # rounding to two decimal places
        result_matrix.append(row)
    
    return result_matrix
