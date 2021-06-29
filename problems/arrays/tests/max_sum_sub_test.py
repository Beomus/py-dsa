import unittest

from ..max_sum_subarray import maxSumSub


class TestMaxSub(unittest.TestCase):
    def test_case_1(self):
        array = [1]
        output = 1
        self.assertEqual(maxSumSub(array), output)

    def test_case_2(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(maxSumSub(array), output)

    def test_case_3(self):
        array = [5, 4, -1, 7, 8]
        output = 23
        self.assertEqual(maxSumSub(array), output)

    def test_case_4(self):
        array = [1, -2, 3, -1, 5, -5, 6, -7, 123, -112, -11, 9, 10]
        output = 124
        self.assertEqual(maxSumSub(array), output)


if __name__ == "__main__":
    unittest.main()
