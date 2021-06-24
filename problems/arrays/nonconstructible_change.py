"""
Non-constructible change

Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of changes (the
minimum sum of money) that you CANNOT create. The given coins can have any
positive integer value and aren't necessarily unique.

Example: coins = [1, 2, 5], the minimum amount of change that you can't create
is 4. If you're given no coins the minimum amount of change you can't create is 1.
"""

from typing import List


def nonConstructibleChange(coins: List) -> int:
    if len(coins) == 0:
        return 1

    change = 0
    for coin in sorted(coins):
        if coin > change + 1:
            return change + 1
        else:
            change += coin
    return change + 1
