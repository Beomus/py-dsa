import unittest

from ..two_sum import twoSum


class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target = 10
        result = twoSum(array, target)
        self.assertCountEqual(result, (11, -1))

    def test_case_2(self):
        array = [4, 6]
        target = 10
        result = twoSum(array, target)
        self.assertCountEqual(result, (4, 6))

    def test_case_3(self):
        array = [4, 6, 1]
        target = 5
        result = twoSum(array, target)
        self.assertCountEqual(result, (4, 1))

    def test_case_4(self):
        array = [4]
        target = 4
        result = twoSum(array, target)
        self.assertCountEqual(result, ())


if __name__ == "__main__":
    unittest.main()
