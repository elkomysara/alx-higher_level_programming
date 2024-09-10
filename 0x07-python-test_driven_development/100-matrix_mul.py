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
    # Validate input types
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Validate lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check for empty matrices
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Check that elements are integers or floats
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    
    # Ensure each row has the same size (rectangular matrix)
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Validate matrix multiplication dimensions
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            product_sum = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            result_row.append(product_sum)
        result.append(result_row)
    
    return result
