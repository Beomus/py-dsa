"""
Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether
the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in
the array but that are in the same order as they appear in the array. For instance,
the number [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do [2 ,4].

Note that a single number in an array and the array itself are both valid
subsequences of the array.
"""


def isValidSubsequence(array, sequence):
    if len(sequence) > len(array):
        return False

    p1 = 0
    for i in array:
        if i == sequence[p1]:
            p1 += 1
            if p1 == len(sequence):
                return True
    return False
