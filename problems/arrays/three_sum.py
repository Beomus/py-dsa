"""
Three Number Sum: write a function that takes in a non-empty array of distinct
integers and an integer representing the target sum. The function should find
all triplets in the array that sum up to the target sum and returns a 2D array
of all these triplets.

The number in each triplet should be sorted in ascending order, and the triplets
themselves should be sorted in ascending orders with respect to the number they
hold. If there are no triplet, return an empty array.
"""


def threeSum(array, target):
    array.sort()
    result = []
    for i, x in enumerate(array):
        p1 = i + 1
        p2 = len(array) - 1
        while p1 < p2:
            tempSum = x + array[p1] + array[p2]
            if tempSum < target:
                p1 += 1
            elif tempSum > target:
                p2 -= 1
            elif tempSum == target:
                result.append([x, array[p1], array[p2]])
                p1 += 1
                p2 -= 1
    return result
