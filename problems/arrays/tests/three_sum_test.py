import unittest

from ..three_sum import threeSum


class TestThreeSum(unittest.TestCase):
    def test_case_1(self):
        array = [12, 3, 1, 2, -6, 5, -8, 6]
        target = 0
        output = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
        self.assertEqual(threeSum(array, target), output)

    def test_case_2(self):
        array = [1, 2, 3]
        target = 6
        output = [[1, 2, 3]]
        self.assertEqual(threeSum(array, target), output)

    def test_case_3(self):
        array = [1, 2, 3]
        target = 7
        output = []
        self.assertEqual(threeSum(array, target), output)

    def test_case_4(self):
        array = [12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5]
        target = 0
        output = [
            [-8, 2, 6],
            [-8, 3, 5],
            [-6, 0, 6],
            [-6, 1, 5],
            [-5, -1, 6],
            [-5, 0, 5],
            [-5, 2, 3],
            [-1, 0, 1],
        ]
        self.assertEqual(threeSum(array, target), output)

    def test_case_5(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        target = 5
        output = []
        self.assertEqual(threeSum(array, target), output)


if __name__ == "__main__":
    unittest.main()
