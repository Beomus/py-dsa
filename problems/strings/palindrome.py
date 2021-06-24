"""
Write a function to check if a non-empty string is a palindrome or not.
"""


def isPalindrome(string):
    return string == string[::-1]
