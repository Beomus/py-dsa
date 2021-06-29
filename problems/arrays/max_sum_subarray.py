"""
Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def maxSumSub(array):
    maxSum = array[0]
    curSum = 0
    for i in array:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSum = max(maxSum, curSum)
    return maxSum
