import unittest

from ..remove_element import removeElement


class TestRemove(unittest.TestCase):
    def test_case_1(self):
        array = [3, 2, 2, 3]
        val = 3
        output = 2
        self.assertEquals(removeElement(array, val), output)

    def test_case_2(self):
        array = [3]
        val = 3
        output = 0
        self.assertEquals(removeElement(array, val), output)

    def test_case_3(self):
        array = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        output = 5
        self.assertEquals(removeElement(array, val), output)

    def test_case_4(self):
        array = [1, 1, 1, 1, 1, 0, 1, 2, 3, 1, 1, 1, 1, 5]
        val = 1
        output = 4
        self.assertEquals(removeElement(array, val), output)


if __name__ == "__main__":
    unittest.main()
