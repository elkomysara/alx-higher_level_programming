#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        ValueError: If m_a or m_b is empty or if the matrices cannot be multiplied.
    
    Returns:
        list of lists: A new matrix representing the multiplication of m_a by m_b.
    """

    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate that m_a and m_b are not empty (i.e., no empty lists)
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Validate that all elements of m_a and m_b are integers or floats
    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate that each row in m_a and m_b is of the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate if m_a and m_b can be multiplied (columns of m_a must equal rows of m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            product_sum = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            result_row.append(product_sum)
        result.append(result_row)

    return result
