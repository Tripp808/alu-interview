#!/usr/bin/python3

"""
0-main
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    This function generates Pascal's Triangle, a mathematical pattern where each
    number is the sum of the two numbers directly above it. The function returns
    a list of lists representing the rows of the triangle.

    Args:
        n (int): The number of rows to generate. Must be a non-negative integer.

    Returns:
        List[List[int]]: A list of lists representing the Pascal's Triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    :param n: The number of rows to generate in Pascal's Triangle.
    :type n: int
    :return: A list of lists representing Pascal's Triangle.
    :rtype: List[List[int]]
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
