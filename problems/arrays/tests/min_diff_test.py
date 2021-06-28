import unittest

from ..min_diff import minDifference


class TestMinDiff(unittest.TestCase):
    def test_case_1(self):
        array1 = [-1, 5, 10, 20, 28, 3]
        array2 = [26, 134, 135, 15, 17]
        output = [28, 26]
        self.assertCountEqual(minDifference(array1, array2), output)

    def test_case_2(self):
        array1 = [-1, 5, 10, 20, 3]
        array2 = [26, 134, 135, 15, 17]
        output = [20, 17]
        self.assertCountEqual(minDifference(array1, array2), output)

    def test_case_3(self):
        array1 = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530]
        array2 = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
        output = [530, 530]
        self.assertCountEqual(minDifference(array1, array2), output)

    def test_case_4(self):
        array1 = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
        array2 = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
        output = [-123, -124]
        self.assertCountEqual(minDifference(array1, array2), output)


if __name__ == "__main__":
    unittest.main()
