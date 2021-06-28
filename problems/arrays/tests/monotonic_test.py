import unittest

from ..monotonic_array import isMonotonic


class TestChange(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        self.assertTrue(isMonotonic(array))

    def test_case_2(self):
        array = []
        self.assertTrue(isMonotonic(array))

    def test_case_3(self):
        array = [1]
        self.assertTrue(isMonotonic(array))

    def test_case_5(self):
        array = [1, 5, 10, 1100, 1101, 1102, 9001]
        self.assertTrue(isMonotonic(array))

    def test_case_6(self):
        array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
        self.assertFalse(isMonotonic(array))

    def test_case_7(self):
        array = [1, 2, 0]
        self.assertFalse(isMonotonic(array))


if __name__ == "__main__":
    unittest.main()
