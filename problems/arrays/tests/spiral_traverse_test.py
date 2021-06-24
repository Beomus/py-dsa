import unittest

from ..spiral_traverse import spiralTraverse


class TestSpiralTraverse(unittest.TestCase):
    def test_case_01(self):
        array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        output = [i for i in range(1, 17)]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_02(self):
        array = [[1]]
        output = [1]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_03(self):
        array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        output = [i for i in range(1, 10)]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_04(self):
        array = [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]
        output = [i for i in range(1, 13)]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_05(self):
        array = [[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]
        output = [i for i in range(1, 16)]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_06(self):
        array = [
            [1, 11],
            [2, 12],
            [3, 13],
            [4, 14],
            [5, 15],
            [6, 16],
            [7, 17],
            [8, 18],
            [9, 19],
            [10, 20],
        ]
        output = [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_07(self):
        array = [[1, 2, 3, 4, 5, 6, 7]]
        output = [i for i in range(1, 8)]
        self.assertEqual(spiralTraverse(array), output)

    def test_case_08(self):
        array = [[1], [2], [3], [4], [5], [6], [7]]
        output = [i for i in range(1, 8)]
        self.assertEqual(spiralTraverse(array), output)


if __name__ == "__main__":
    unittest.main()
