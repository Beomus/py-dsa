import unittest

from ..palindrome import isPalindrome


class TestPalindrome(unittest.TestCase):
    def test_case_1(self):
        string = "abcdcba"
        self.assertTrue(isPalindrome(string))

    def test_case_2(self):
        string = "a"
        self.assertTrue(isPalindrome(string))

    def test_case_3(self):
        string = "ab"
        self.assertFalse(isPalindrome(string))

    def test_case_4(self):
        string = "aba"
        self.assertTrue(isPalindrome(string))


if __name__ == "__main__":
    unittest.main()
