#!/usr/bin/python3
"""
In a text file, there is a single character H. Your editor can execute only two
operations in file: Copy, All and Paste.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations needed. If n is impossible to achieve, return 0.
    """
    if n < 2:
        return 0

    operations = 0
    current_chars = 2

    while n > 1:
        # If current_chars is a factor of n, we can reach n by copying and pasting
        if n % current_chars == 0:
            operations += current_chars
            n //= current_chars
            current_chars += 1

    return operations
