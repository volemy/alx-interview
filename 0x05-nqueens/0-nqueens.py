#!/usr/bin/python3

""" N queens 00 """

import sys


def get_size():
    """
    Getting board size.
    """
    arguments = sys.argv
    if len(arguments) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(arguments[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be an integer')
        sys.exit(1)
    return n


def unsafe_position(
        board,
        row,
        col,
        current) -> bool:
    """
    If the queen is in the same column, or in the same diagonal,
    as any other queen, then it is not unsafe.
    """

    if (board[row] == col) or \
        (board[row] == col - row + current) or\
            (board[row] == row - current + col):
        return True
    return False


def print_board(board, n):
    """
    It takes a board and an n, and returns a list of the
    coordinates.
    """

    result = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                result.append([i, j])
    print(result)


def fill_positions(board, row,  n):
    """
    For each row, try each column, and if it's safe, recurse on the next row.
    """

    if row == n:
        print_board(board, n)
    else:

        for j in range(n):
            is_safe = True
            for i in range(row):
                if unsafe_position(board, i, j, row):
                    is_safe = False
            if is_safe:
                board[row] = j
                fill_positions(board, row + 1, n)


if __name__ == '__main__':
    board_size = get_size()
    initial_list = [0] * board_size
    fill_positions(initial_list, 0, board_size)
