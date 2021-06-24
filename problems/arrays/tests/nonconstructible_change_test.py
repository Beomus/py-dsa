import unittest

from ..nonconstructible_change import nonConstructibleChange


class TestChange(unittest.TestCase):
    def test_case_1(self):
        coins = [5, 7, 1, 1, 2, 3, 22]
        self.assertEqual(nonConstructibleChange(coins), 20)

    def test_case_2(self):
        coins = [1, 1, 1, 1, 1]
        self.assertEqual(nonConstructibleChange(coins), 6)

    def test_case_3(self):
        coins = [6, 4, 5, 1, 1, 8, 9]
        self.assertEqual(nonConstructibleChange(coins), 3)

    def test_case_4(self):
        coins = []
        self.assertEqual(nonConstructibleChange(coins), 1)

    def test_case_5(self):
        coins = [2]
        self.assertEqual(nonConstructibleChange(coins), 1)

    def test_case_6(self):
        coins = [1]
        self.assertEqual(nonConstructibleChange(coins), 2)


if __name__ == "__main__":
    unittest.main()
