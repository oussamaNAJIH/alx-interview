#!/usr/bin/python3
"""
minOperations(n) module
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    """
    if n <= 0:
        return 0
    result = "H"
    tmp = ""
    num_operations = 0
    while len(result) < n:
        if n % len(result) == 0:
            tmp = result
            result += tmp
            num_operations += 2
            continue
        elif n % len(result) != 0:
            result += tmp
            num_operations += 1
            continue
    if len(result) == n:
        return num_operations
    return 0
