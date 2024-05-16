#!/usr/bin/python3
"""
This program resolves the N queens problem
using backtracking algorithm
"""
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Extract N from the command line argument
N = sys.argv[1]

# Check if N is a number
if not N.isdigit():
    print("N must be a number")
    exit(1)

# Convert N to an integer
N = int(N)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    exit(1)
