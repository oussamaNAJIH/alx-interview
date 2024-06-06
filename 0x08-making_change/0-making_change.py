#!/usr/bin/python3

"""
Module to solve the coin change problem using dynamic
programming with optimized space complexity
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to be met with the coins.

    Returns:
        int: Fewest number of coins needed to meet the total,
             or -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity values, except dp[0] which is 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build up the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
