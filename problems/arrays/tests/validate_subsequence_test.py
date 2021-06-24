import unittest

from ..validate_subsequence import isValidSubsequence


class TestSubsequence(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_case_2(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [22, 25, 6]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_case_3(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_case_4(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [25]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_case_5(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10, 12]
        self.assertFalse(isValidSubsequence(array, sequence))

    def test_case_6(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [4, 5, 1, 22, 25, 6, -1, 8, 10]
        self.assertFalse(isValidSubsequence(array, sequence))


if __name__ == "__main__":
    unittest.main()
