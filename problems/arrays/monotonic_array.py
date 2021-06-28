"""
Monotonic array: write a function that takes in an array of integers and returns
a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are
entirely non-increasing or entirely non-decreasing.
(Non-increasing elements aren’t necessarily exclusively decreasing;
they simply don’t increase.)
"""


def isMonotonic(array) -> bool:
    def breaksDirection(direction, pre, cur):
        diff = cur - pre
        if direction > 0:
            return diff < 0
        return diff > 0

    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True
