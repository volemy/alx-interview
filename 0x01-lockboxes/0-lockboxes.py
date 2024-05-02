#!/usr/bin/env python3
"""
This module contains a method that determines if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    This is the method that determines if all boxes can be opened
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    def try_unlock(box):
        if not unlocked[box]:
            unlocked[box] = True
            for key in boxes[box]:
                try_unlock(key)

    try_unlock(0)
    return all(unlocked)
