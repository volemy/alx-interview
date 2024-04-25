#!/usr/bin/python3
"""
This returns a list of lists of integers representing the pascal's triangle of n
"""


def pascal_triangle(n):
    """
    This method makes pascal's Triangle upto nth level
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """

    if n <= 0:
        # we define pascal_triangle function that accepts n argument
        # we return an empty list if n is less than or equal to 0
        return []

    # we initialize the triangle with the first row
    triangle = [[1]]

    # we use a for loop to add rows to the triangle list
    for i in range(1, n):
        row = [1]
        p_row = triangle[i - 1]
        for j in range(1, i):
            row.append(p_row[j -1] + p_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
