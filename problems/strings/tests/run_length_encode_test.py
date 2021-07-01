import unittest

from ..run_length_encode import runLengthEncoding_l, runLengthEncoding_s


class TestRunLength(unittest.TestCase):
    def setUp(self) -> None:
        self.funcs = [runLengthEncoding_l, runLengthEncoding_s]

    def test_case_1(self):
        for func in self.funcs:
            string = "AAAAAAAAAAAAABBCCCCDD"
            output = "9A4A2B4C2D"
            self.assertEqual(func(string), output)

    def test_case_2(self):
        for func in self.funcs:
            string = "aA"
            output = "1a1A"
            self.assertEqual(func(string), output)

    def test_case_3(self):
        for func in self.funcs:
            string = "122333"
            output = "112233"
            self.assertEqual(func(string), output)

    def test_case_4(self):
        for func in self.funcs:
            string = "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"
            output = "9*3*7^6$7%6!9A9A2A"
            self.assertEqual(func(string), output)

    def test_case_5(self):
        for func in self.funcs:
            string = "aAaAaaaaaAaaaAAAABbbbBBBB"
            output = "1a1A1a1A5a1A3a4A1B3b4B"
            self.assertEqual(func(string), output)

    def test_case_6(self):
        for func in self.funcs:
            string = "aAaAaaaaaAaaaAAAABbbbBBBB"
            output = "1a1A1a1A5a1A3a4A1B3b4B"
            self.assertEqual(func(string), output)

    def test_case_7(self):
        for func in self.funcs:
            string = "                          "
            output = "9 9 8 "
            self.assertEqual(func(string), output)

    def test_case_8(self):
        for func in self.funcs:
            string = "[(aaaaaaa,bbbbbbb,ccccc,dddddd)]"
            output = "1[1(7a1,7b1,5c1,6d1)1]"
            self.assertEqual(func(string), output)


if __name__ == "__main__":
    unittest.main()
