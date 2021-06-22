import unittest

from .matching_brackets import balancedBrackets_v1, balancedBrackets_v2


class TestBrackets(unittest.TestCase):
    def test_case_1(self):
        funcs = [balancedBrackets_v1, balancedBrackets_v2]
        for func in funcs:
            self.assertTrue(func(r"([])(){}(())()()"))


if __name__ == "__main__":
    unittest.main()
