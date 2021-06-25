import unittest

from ..caesar_cipher import caesarCipher


class TestCaesar(unittest.TestCase):
    def test_case_1(self):
        string = "xyz"
        key = 2
        output = "zab"
        self.assertEqual(caesarCipher(string, key), output)

    def test_case_2(self):
        string = "abc"
        key = 0
        output = "abc"
        self.assertEqual(caesarCipher(string, key), output)

    def test_case_3(self):
        string = "abc"
        key = 57
        output = "fgh"
        self.assertEqual(caesarCipher(string, key), output)

    def test_case_4(self):
        string = "abc"
        key = 52
        output = "abc"
        self.assertEqual(caesarCipher(string, key), output)

    def test_case_5(self):
        string = "iwu fqnkqk qoolxzzlz ihqfm"
        key = 25
        output = "hvt epmjpj pnnkwyyky hgpel"
        self.assertEqual(caesarCipher(string, key), output)


if __name__ == "__main__":
    unittest.main()
