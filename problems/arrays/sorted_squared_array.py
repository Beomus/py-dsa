"""
Sorted squared array

Write a function that takes a non-empty array of integers that are sorted in
ascending order and returns a new array of the same length with the squares of
the original integers also sorted in ascending order.
"""


def sortedSquared(array):
    return sorted([x ** 2 for x in array])
