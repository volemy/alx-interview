#!/usr/bin/python3
"""
In a text file, there is a single character H. Your editor can execute only two
operations in file: Copy, All and Paste.
"""


def min_operations(n):
    """
    Determine the minimum number of operations
    needed to result in exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required,
    or 0 if n cannot be achieved.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations


if __name__ == "__main__":
    print("Min # of operations to reach {} char: {}".format(4, min_operations(4)))
    print("Min # of operations to reach {} char: {}".format(12, min_operations(12)))
