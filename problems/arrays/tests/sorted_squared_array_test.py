import unittest

from ..sorted_squared_array import sortedSquared


class TestSortedSquared(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        output = [1, 4, 9, 25, 36, 64, 81]
        self.assertEqual(sortedSquared(array), output)

    def test_case_2(self):
        array = [-5, -4, -3, -2, -1]
        output = [1, 4, 9, 16, 25]
        self.assertEqual(sortedSquared(array), output)

    def test_case_3(self):
        array = [-10, -5, 0, 5, 10]
        output = [0, 25, 25, 100, 100]
        self.assertEqual(sortedSquared(array), output)


if __name__ == "__main__":
    unittest.main()
