"""
Smallest difference: write a function that takes in two non-empty arrays of
integers, finds the pair of numbers (one from each array) whose ABSOLUTE
difference is closest to zero, and returns an array containing these two
numbers, with the number from the first array in the first position.
"""


def minDifference(array1, array2):
    array1.sort()
    array2.sort()
    p1, p2 = 0, 0
    current, smallest = float("inf"), float("inf")
    while p1 < len(array1) and p2 < len(array2):
        firstNum = array1[p1]
        secondNum = array2[p2]
        if firstNum < secondNum:
            current = secondNum - firstNum
            p1 += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            p2 += 1
        else:
            return [firstNum, secondNum]

        if current < smallest:
            smallest = current
            pair = [firstNum, secondNum]
    return pair
